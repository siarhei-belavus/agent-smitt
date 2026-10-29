from __future__ import annotations

import re
import runpy
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PACKAGER = runpy.run_path(str(ROOT / "bin" / "sync-skill-references"))
LINKS = PACKAGER["markdown_links"]


def assert_local_links(directory: Path) -> None:
    for source in directory.rglob("*.md"):
        for _, _, url in LINKS(source.read_text(encoding="utf-8")):
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            target = (source.parent / unquote(parts.path)).resolve()
            if not target.is_relative_to(directory.resolve()) or not target.exists():
                raise AssertionError(f"Unpackaged reference in {source}: {url}")


class DistributionTest(unittest.TestCase):
    def test_every_skill_works_without_sibling_directories(self) -> None:
        for skill_file in (ROOT / "skills").glob("*/*/SKILL.md"):
            with self.subTest(skill=skill_file.parent.name), tempfile.TemporaryDirectory() as temp:
                isolated = Path(temp) / skill_file.parent.name
                shutil.copytree(skill_file.parent, isolated)
                assert_local_links(isolated)
                self.assertEqual((isolated / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())

    def test_generated_references_are_current(self) -> None:
        result = subprocess.run(
            ["python3", str(ROOT / "bin" / "sync-skill-references"), "--check"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_packager_refreshes_changed_sources_and_removes_unused_references(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repository = Path(temp)
            script = repository / "bin" / "sync-skill-references"
            script.parent.mkdir()
            shutil.copy2(ROOT / "bin" / "sync-skill-references", script)
            (repository / "LICENSE").write_text("Test license\n")
            consumer = repository / "skills" / "engineering" / "consumer"
            shared = repository / "skills" / "engineering" / "shared"
            consumer.mkdir(parents=True)
            shared.mkdir()
            source = consumer / "SKILL.md"
            source.write_text("Read [contract](../shared/contract.md).\n")
            contract = shared / "contract.md"
            contract.write_text("Original contract.\n")

            def run(*args):
                return subprocess.run(["python3", str(script), *args], capture_output=True, text=True)

            result = run()
            self.assertEqual(result.returncode, 0, result.stderr)
            bundled = consumer / "references" / "bundled" / "shared" / "contract.md"
            self.assertEqual(bundled.read_text(), contract.read_text())
            assert_local_links(consumer)
            contract.write_text("Updated contract.\n")
            self.assertEqual(run("--check").returncode, 1)
            self.assertEqual(bundled.read_text(), "Original contract.\n")
            self.assertEqual(run().returncode, 0)
            self.assertEqual(bundled.read_text(), contract.read_text())
            source.write_text("No external references remain.\n")
            self.assertEqual(run().returncode, 0)
            self.assertFalse(bundled.exists())
            self.assertEqual(run("--check").returncode, 0)

    def test_catalog_contains_exactly_the_public_skills(self) -> None:
        skills = list((ROOT / "skills").glob("*/*/SKILL.md"))
        catalog = (ROOT / "docs" / "skills.md").read_text(encoding="utf-8")
        listed = re.findall(r"\]\(\.\./(skills/[^)]+/SKILL\.md)\)", catalog)
        self.assertEqual(set(listed), {p.relative_to(ROOT).as_posix() for p in skills})
        self.assertEqual(len(listed), len(skills))
        for skill in skills:
            text = skill.read_text(encoding="utf-8")
            name = re.search(r"^name: (.+)$", text, re.MULTILINE).group(1)
            self.assertEqual(name, skill.parent.name)
            self.assertRegex(text, r"(?m)^description: .+")

    def test_public_documentation_links_resolve(self) -> None:
        files = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *(ROOT / "docs").glob("*.md")]
        files.extend((ROOT / "skills").glob("*/README.md"))
        for source in files:
            for _, _, url in LINKS(source.read_text(encoding="utf-8")):
                parts = urlsplit(url)
                if not parts.scheme and not parts.netloc and parts.path:
                    self.assertTrue((source.parent / unquote(parts.path)).exists(), f"{source}: {url}")


if __name__ == "__main__":
    unittest.main()
