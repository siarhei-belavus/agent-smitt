#!/usr/bin/env python3
"""Read-only checks of local delivery state and declared evidence dependencies."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys


class InvalidInput(ValueError):
    """The request cannot be checked without guessing."""


def require(condition: bool, location: str) -> None:
    if not condition:
        raise InvalidInput(location)


def nonempty(value) -> bool:
    return isinstance(value, str) and bool(value.strip()) and '\x00' not in value


def fields(value, expected: set[str], location: str) -> None:
    require(isinstance(value, dict) and set(value) == expected, location)


def check_request(request) -> None:
    fields(request, {'schema_version', 'deliveries', 'observations',
                     'required_evidence', 'evidence'}, 'request')
    require(type(request['schema_version']) is int and request['schema_version'] == 1,
            'schema_version')
    for name in ('deliveries', 'required_evidence', 'evidence'):
        require(isinstance(request[name], list), name)
    require(bool(request['deliveries'] or request['required_evidence'] or request['evidence']),
            'empty_request')
    observations = request['observations']
    require(isinstance(observations, dict), 'observations')
    require(all(nonempty(key) and (value is None or nonempty(value))
                for key, value in observations.items()), 'observations')
    repositories = set()
    for index, delivery in enumerate(request['deliveries']):
        location = 'deliveries[' + str(index) + ']'
        fields(delivery, {'repository_id', 'path', 'remote', 'branch', 'base', 'head'}, location)
        require(all(nonempty(value) for value in delivery.values()), location)
        require(Path(delivery['path']).is_absolute(), location + '.path')
        for name in ('head', 'base'):
            require(re.fullmatch(r'(?:[0-9a-f]{40}|[0-9a-f]{64})', delivery[name]) is not None,
                    location + '.' + name)
        repository_id = delivery['repository_id']
        require(repository_id not in repositories, location + '.repository_id')
        require('head:' + repository_id not in observations, location + '.observed_head')
        repositories.add(repository_id)
    required = request['required_evidence']
    require(all(nonempty(value) for value in required), 'required_evidence')
    require(len(set(required)) == len(required), 'required_evidence')
    identifiers = set()
    for index, record in enumerate(request['evidence']):
        location = 'evidence[' + str(index) + ']'
        fields(record, {'id', 'result', 'dependencies'}, location)
        require(nonempty(record['id']) and record['id'] not in identifiers, location + '.id')
        identifiers.add(record['id'])
        require(isinstance(record['result'], str) and record['result'] in {'pass', 'fail', 'pending'},
                location + '.result')
        dependencies = record['dependencies']
        require(isinstance(dependencies, dict) and bool(dependencies), location + '.dependencies')
        require(all(nonempty(key) and nonempty(value) for key, value in dependencies.items()),
                location + '.dependencies')


def unique_object(pairs) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, 'duplicate_key')
        result[key] = value
    return result

def git(path: Path, *arguments: str) -> str:
    config_selectors = {'GIT_CONFIG_GLOBAL', 'GIT_CONFIG_SYSTEM', 'GIT_CONFIG_NOSYSTEM'}
    environment = {key: value for key, value in os.environ.items()
                   if not key.startswith('GIT_') or key in config_selectors}
    environment.update(GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0',
                       GIT_NO_LAZY_FETCH='1', GIT_ALLOW_PROTOCOL='')
    result = subprocess.run(
        ['git', '--no-optional-locks', '-c', 'core.fsmonitor=false',
         '-c', 'core.untrackedCache=false', '-C', str(path), *arguments],
        env=environment, capture_output=True, text=True, encoding='utf-8',
        errors='replace', timeout=30, check=True,
    )
    return result.stdout.strip()


def cleanliness_blocker(path: Path) -> str | None:
    # Submodule status can invoke filters in another repository's configuration.
    entries = git(path, 'ls-files', '--stage', '-z').split('\x00')
    if any(entry.startswith('160000 ') for entry in entries):
        return 'submodules_require_manual_check'
    try:
        git(path, 'config', '--get-regexp', r'^filter\..*\.(clean|process)$')
    except subprocess.CalledProcessError as error:
        if error.returncode == 1:
            return None  # No configured clean/process command.
        raise
    # Even a passthrough filter can write or contact a service.
    return 'filters_require_manual_check'

def inspect_delivery(delivery: dict) -> tuple[dict, list[dict]]:
    repository_id = delivery['repository_id']
    result = {'repository_id': repository_id, 'head': None, 'clean': None}
    issues = []

    def issue(code):
        issues.append({'code': code, 'subject': repository_id})

    try:
        path = Path(delivery['path']).resolve()
        if Path(git(path, 'rev-parse', '--show-toplevel')).resolve() != path:
            issue('not_repository_root')
            return result, issues
        result['head'] = git(path, 'rev-parse', '--verify', 'HEAD')
        if result['head'] != delivery['head']:
            issue('head_mismatch')
        if git(path, 'symbolic-ref', '--quiet', '--short', 'HEAD') != delivery['branch']:
            issue('branch_mismatch')
        if git(path, 'remote', 'get-url', 'origin') != delivery['remote']:
            issue('remote_mismatch')
        try:
            base = git(path, 'rev-parse', '--verify', delivery['base'] + '^{commit}')
            if base != delivery['base']:
                issue('base_unavailable')
        except subprocess.CalledProcessError:
            issue('base_unavailable')
        blocker = cleanliness_blocker(path)
        if blocker:
            issue(blocker)
            return result, issues
        result['clean'] = not git(path, 'status', '--porcelain=v1', '--untracked-files=all',
                                  '--ignore-submodules=none')
        if not result['clean']:
            issue('dirty_worktree')
        if git(path, 'rev-parse', '--verify', 'HEAD') != result['head']:
            issue('head_changed_during_check')
            result['head'] = None
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError):
        issue('git_unavailable')
        result['head'] = None
        result['clean'] = None
    return result, issues

def validate(request: dict) -> dict:
    observations = dict(request['observations'])
    issues = []
    deliveries = []
    for delivery in request['deliveries']:
        result, local_issues = inspect_delivery(delivery)
        issues.extend(local_issues)
        deliveries.append(result)
        # A changed head is observable; wrong identity or dirty state is not usable evidence.
        trustworthy = all(item['code'] == 'head_mismatch' for item in local_issues)
        observations['head:' + delivery['repository_id']] = result['head'] if trustworthy else None
    evidence = []
    for record in request['evidence']:
        dependencies = record['dependencies']
        missing = sorted(key for key in dependencies if observations.get(key) is None)
        changed = sorted(key for key, value in dependencies.items()
                         if observations.get(key) is not None and observations[key] != value)
        if record['result'] != 'pass':
            status = 'not_passed'
        elif missing:
            status = 'unknown'
        elif changed:
            status = 'stale'
        else:
            status = 'current'
        evidence.append({'id': record['id'], 'status': status,
                         'changed': changed, 'missing': missing})
    available = {record['id'] for record in request['evidence']}
    for name in request['required_evidence']:
        if name not in available:
            issues.append({'code': 'missing_evidence', 'subject': name})
    attention = bool(issues) or any(record['status'] != 'current' for record in evidence)
    return {'schema_version': 1, 'status': 'attention' if attention else 'consistent',
            'issues': issues, 'deliveries': deliveries, 'evidence': evidence}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='UTF-8 JSON file, or - for stdin')
    args = parser.parse_args()
    try:
        if args.input == '-':
            raw = sys.stdin.buffer.read().decode('utf-8')
        else:
            raw = Path(args.input).read_text(encoding='utf-8')
        request = json.loads(raw, object_pairs_hook=unique_object)
        check_request(request)
        report = validate(request)
    except (OSError, ValueError, RecursionError) as error:
        # Never print input values, provider URLs, Git stderr, or exception payloads.
        subject = str(error) if isinstance(error, InvalidInput) else 'input'
        report = {'schema_version': 1, 'status': 'invalid',
                  'issues': [{'code': 'invalid_input', 'subject': subject}],
                  'deliveries': [], 'evidence': []}
    print(json.dumps(report, ensure_ascii=True, sort_keys=True))
    return {'consistent': 0, 'attention': 1, 'invalid': 2}[report['status']]


if __name__ == '__main__':
    raise SystemExit(main())
