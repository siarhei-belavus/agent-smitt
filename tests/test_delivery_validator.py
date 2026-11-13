from __future__ import annotations

import json
import copy
import os
import shutil
import shlex
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/engineering/federated-workflow/scripts/validate_delivery.py'


class DeliveryValidatorTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='delivery validator ')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.repo = self.root / 'repo with spaces'
        self.repo.mkdir()
        self.env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
        self.env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull)
        self.git('init', '-b', 'delivery')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.invalid')
        self.git('config', 'commit.gpgsign', 'false')
        self.git('config', 'core.autocrlf', 'false')
        self.git('remote', 'add', 'origin', 'https://example.invalid/api.git')
        (self.repo / 'file.txt').write_text('first\n', encoding='utf-8')
        self.git('add', 'file.txt')
        self.git('commit', '-m', 'Initial')
        self.head = self.git('rev-parse', 'HEAD')

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repo), *args], env=self.env,
                              capture_output=True, text=True, check=True).stdout.strip()

    def request(self):
        return {
            'schema_version': 1,
            'deliveries': [{'repository_id': 'api', 'path': str(self.repo),
                            'remote': 'https://example.invalid/api.git',
                            'branch': 'delivery', 'base': self.head, 'head': self.head}],
            'observations': {'authority:ticket': 'sha256:accepted-body-and-source-set'},
            'required_evidence': ['api-tests'],
            'evidence': [{'id': 'api-tests', 'result': 'pass',
                          'dependencies': {'head:api': self.head,
                                           'authority:ticket': 'sha256:accepted-body-and-source-set'}}],
        }

    def run_validator(self, request, script=SCRIPT, env=None):
        result = subprocess.run([sys.executable, str(script), '-'],
                                input=json.dumps(request), capture_output=True, text=True,
                                encoding='utf-8', env=env or self.env)
        self.assertEqual(result.stderr, '')
        return result.returncode, json.loads(result.stdout)

    def test_clean_delivery_and_current_evidence_are_consistent_without_writes(self):
        index = self.repo / '.git' / 'index'
        before = index.read_bytes(), index.stat().st_mtime_ns
        code, report = self.run_validator(self.request())
        self.assertEqual(code, 0)
        self.assertEqual(report['status'], 'consistent')
        self.assertEqual(report['evidence'][0]['status'], 'current')
        self.assertEqual((index.read_bytes(), index.stat().st_mtime_ns), before)
        self.assertEqual(self.git('status', '--porcelain'), '')

    def test_changed_head_invalidates_only_dependent_evidence(self):
        request = self.request()
        request['evidence'].append({'id': 'independent', 'result': 'pass',
                                    'dependencies': {'authority:ticket': 'sha256:accepted-body-and-source-set'}})
        self.git('commit', '--allow-empty', '-m', 'Change')
        code, report = self.run_validator(request)
        self.assertEqual(code, 1)
        self.assertIn({'code': 'head_mismatch', 'subject': 'api'}, report['issues'])
        self.assertEqual(report['evidence'][0]['status'], 'stale')
        self.assertEqual(report['evidence'][0]['changed'], ['head:api'])
        self.assertEqual(report['evidence'][1]['status'], 'current')

    def test_missing_required_evidence_and_unknown_authority_prevent_success(self):
        request = self.request()
        request['required_evidence'].append('bundle-spec')
        request['observations'] = {}
        code, report = self.run_validator(request)
        self.assertEqual(code, 1)
        self.assertIn({'code': 'missing_evidence', 'subject': 'bundle-spec'}, report['issues'])
        self.assertEqual(report['evidence'][0]['status'], 'unknown')

    def test_failed_validation_cannot_be_reused_with_matching_inputs(self):
        request = self.request()
        request['evidence'][0]['result'] = 'fail'
        code, report = self.run_validator(request)
        self.assertEqual(code, 1)
        self.assertEqual(report['evidence'][0]['status'], 'not_passed')

    def test_dirty_worktree_is_not_evidence_for_head(self):
        (self.repo / 'untracked.txt').write_text('uncommitted', encoding='utf-8')
        code, report = self.run_validator(self.request())
        self.assertEqual(code, 1)
        self.assertIn({'code': 'dirty_worktree', 'subject': 'api'}, report['issues'])
        self.assertEqual(report['evidence'][0]['status'], 'unknown')

    def test_wrong_repository_branch_base_and_subdirectory_are_rejected(self):
        cases = [('remote', 'https://example.invalid/other.git', 'remote_mismatch'),
                 ('branch', 'other', 'branch_mismatch'),
                 ('base', '0' * 40, 'base_unavailable'),
                 ('path', str(self.repo / 'child'), 'not_repository_root')]
        (self.repo / 'child').mkdir()
        for field, value, expected in cases:
            with self.subTest(field=field):
                request = self.request()
                request['deliveries'][0][field] = value
                code, report = self.run_validator(request)
                self.assertEqual(code, 1)
                self.assertIn({'code': expected, 'subject': 'api'}, report['issues'])

    def test_incomplete_or_ambiguous_inputs_fail_closed(self):
        original = self.request()
        cases = [None, {}, dict(original, schema_version=True),
                 dict(original, schema_version=2), dict(original, extra='typo'),
                 dict(original, deliveries=[original['deliveries'][0]] * 2),
                 dict(original, evidence=original['evidence'] * 2),
                 dict(original, required_evidence=['api-tests'] * 2),
                 dict(original, observations={'head:api': self.head}),
                 dict(original, deliveries=[], evidence=[], required_evidence=[])]
        for field, value in [('head', 'HEAD'), ('path', 'relative'), ('branch', ''),
                             ('base', '-bad-ref'), ('remote', None)]:
            request = copy.deepcopy(original)
            request['deliveries'][0][field] = value
            cases.append(request)
        for field, value in [('dependencies', {}), ('result', 'success'),
                             ('dependencies', {'head:api': None})]:
            request = copy.deepcopy(original)
            request['evidence'][0][field] = value
            cases.append(request)
        for request in cases:
            with self.subTest(request=request):
                code, report = self.run_validator(request)
                self.assertEqual(code, 2)
                self.assertEqual(report['status'], 'invalid')

    def test_duplicate_json_keys_are_not_silently_overwritten(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '-'],
                                input='{"schema_version": 2, "schema_version": 1}',
                                capture_output=True, text=True, env=self.env)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stderr, '')
        self.assertEqual(json.loads(result.stdout)['status'], 'invalid')

    def test_changed_authority_invalidates_evidence_even_with_same_head(self):
        request = self.request()
        request['observations']['authority:ticket'] = 'sha256:new-source-membership'
        code, report = self.run_validator(request)
        self.assertEqual(code, 1)
        self.assertEqual(report['evidence'][0]['changed'], ['authority:ticket'])

    def test_resume_can_check_published_dependencies_without_local_worktrees(self):
        request = self.request()
        request['deliveries'] = []
        request['observations']['head:api'] = self.head
        code, report = self.run_validator(request)
        self.assertEqual(code, 0)
        self.assertEqual(report['deliveries'], [])
        del request['observations']['head:api']
        code, report = self.run_validator(request)
        self.assertEqual(code, 1)
        self.assertEqual(report['evidence'][0]['status'], 'unknown')

    def test_linked_worktree_and_inherited_git_environment(self):
        worktree = self.root / 'linked worktree'
        self.git('worktree', 'add', '-b', 'linked', str(worktree))
        request = self.request()
        request['deliveries'][0].update(path=str(worktree), branch='linked')
        env = dict(self.env, GIT_DIR=str(self.root / 'absent'),
                   GIT_WORK_TREE=str(self.root), GIT_INDEX_FILE=str(self.root / 'foreign-index'))
        code, report = self.run_validator(request, env=env)
        self.assertEqual(code, 0)
        self.assertEqual(report['status'], 'consistent')
        self.assertFalse((self.root / 'foreign-index').exists())

    def test_missing_git_or_repository_returns_attention_without_traceback(self):
        request = self.request()
        request['deliveries'][0]['path'] = str(self.root / 'absent')
        code, report = self.run_validator(request)
        self.assertEqual(code, 1)
        self.assertIn({'code': 'git_unavailable', 'subject': 'api'}, report['issues'])

    def test_cyclic_path_returns_attention_without_exposing_the_path(self):
        loop = self.root / 'cyclic-path-placeholder'
        try:
            loop.symlink_to(loop.name, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest('Host does not allow symlink creation')
        request = self.request()
        request['deliveries'][0]['path'] = str(loop)
        code, report = self.run_validator(request)
        self.assertEqual(code, 1)
        self.assertIn({'code': 'git_unavailable', 'subject': 'api'}, report['issues'])
        self.assertNotIn(loop.name, json.dumps(report))

    def test_file_input_and_errors_do_not_echo_input_values(self):
        request = self.request()
        source = self.root / 'input.json'
        source.write_text(json.dumps(request), encoding='utf-8')
        result = subprocess.run([sys.executable, str(SCRIPT), str(source)],
                                capture_output=True, text=True, env=self.env)
        self.assertEqual(result.returncode, 0)
        source.write_text('{"sensitive-placeholder": invalid}', encoding='utf-8')
        result = subprocess.run([sys.executable, str(SCRIPT), str(source)],
                                capture_output=True, text=True, env=self.env)
        self.assertEqual(result.returncode, 2)
        self.assertNotIn('sensitive-placeholder', result.stdout + result.stderr)

    def test_installed_validator_runs_without_source_repository(self):
        for skill in ('deliver-ticket', 'code-review'):
            with self.subTest(skill=skill):
                source = ROOT / 'skills' / 'engineering' / skill
                installed = self.root / skill
                shutil.copytree(source, installed)
                script = installed / 'references/bundled/federated-workflow/scripts/validate_delivery.py'
                self.assertEqual(script.read_bytes(), SCRIPT.read_bytes())
                code, report = self.run_validator(self.request(), script=script)
                self.assertEqual(code, 0)
                self.assertEqual(report['status'], 'consistent')

    def test_partial_clone_does_not_fetch_a_missing_base_or_write_git_state(self):
        self.git('config', 'uploadpack.allowFilter', 'true')
        self.git('config', 'uploadpack.allowAnySHA1InWant', 'true')
        checkout = self.root / 'partial clone'
        subprocess.run(['git', 'clone', '--filter=blob:none', self.repo.as_uri(), str(checkout)],
                       env=self.env, capture_output=True, text=True, check=True)
        self.git('commit', '--allow-empty', '-m', 'Remote only')
        request = self.request()
        request['deliveries'][0].update(path=str(checkout), remote=self.repo.as_uri(),
                                        base=self.git('rev-parse', 'HEAD'))

        def git_files():
            return {p.relative_to(checkout).as_posix(): p.read_bytes()
                    for p in (checkout / '.git').rglob('*') if p.is_file()}

        before = git_files()
        code, report = self.run_validator(request)
        self.assertEqual(code, 1)
        self.assertIn({'code': 'base_unavailable', 'subject': 'api'}, report['issues'])
        self.assertEqual(git_files(), before)

    def test_configured_clean_filter_is_not_executed(self):
        (self.repo / '.gitattributes').write_text('file.txt filter=probe\n', encoding='utf-8')
        self.git('add', '.gitattributes')
        self.git('commit', '-m', 'Attributes')
        self.head = self.git('rev-parse', 'HEAD')
        marker = self.repo / '.git' / 'validator-side-effect'
        program = ('import pathlib,sys; pathlib.Path(' + repr(str(marker)) +
                   ').write_text("side effect"); sys.stdout.buffer.write(sys.stdin.buffer.read())')
        self.git('config', 'filter.probe.clean', shlex.quote(sys.executable) + ' -c ' + shlex.quote(program))
        stat = (self.repo / 'file.txt').stat()
        os.utime(self.repo / 'file.txt', (stat.st_atime, stat.st_mtime + 60))
        code, report = self.run_validator(self.request())
        self.assertEqual(code, 1)
        self.assertIn({'code': 'filters_require_manual_check', 'subject': 'api'}, report['issues'])
        self.assertFalse(marker.exists())
        self.assertIsNone(report['deliveries'][0]['clean'])
        self.assertEqual(report['evidence'][0]['status'], 'unknown')

    def test_submodule_state_requires_manual_check_without_entering_it(self):
        self.git('update-index', '--add', '--cacheinfo', '160000,' + self.head + ',module')
        self.git('commit', '-m', 'Gitlink')
        self.head = self.git('rev-parse', 'HEAD')
        code, report = self.run_validator(self.request())
        self.assertEqual(code, 1)
        self.assertIn({'code': 'submodules_require_manual_check', 'subject': 'api'}, report['issues'])
        self.assertIsNone(report['deliveries'][0]['clean'])

    def test_global_process_filter_requires_manual_check_even_when_unused(self):
        config = self.root / 'global.gitconfig'
        config.write_text('[filter "probe"]\n\tprocess = never-execute-this-command\n', encoding='utf-8')
        env = dict(self.env, GIT_CONFIG_GLOBAL=str(config))
        code, report = self.run_validator(self.request(), env=env)
        self.assertEqual(code, 1)
        self.assertIn({'code': 'filters_require_manual_check', 'subject': 'api'}, report['issues'])
        self.assertIsNone(report['deliveries'][0]['clean'])


if __name__ == '__main__':
    unittest.main()
