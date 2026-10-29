#!/usr/bin/env python3
"""Exercise the real Skills CLI without touching user-level installations."""
from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path

from test_distribution import assert_local_links


ROOT = Path(__file__).resolve().parents[1]
CLI_VERSION = os.environ.get("SKILLS_CLI_VERSION", "1.7.4")


def main() -> None:
    expected = {p.parent.name for p in (ROOT / "skills").glob("*/*/SKILL.md")}
    for selection, copy in [("*", False), ("*", True), ("coordinate-delivery", True)]:
        with tempfile.TemporaryDirectory(prefix="agent-smitt-cli-") as temp:
            command = ["npx", "--yes", f"skills@{CLI_VERSION}", "add", str(ROOT),
                       "--skill", selection, "--agent", "codex", "--yes"]
            if copy:
                command.append("--copy")
            env = dict(os.environ, DISABLE_TELEMETRY="1")
            result = subprocess.run(command, cwd=temp, env=env, capture_output=True, text=True)
            if result.returncode:
                raise SystemExit(result.stdout + result.stderr)
            installed = Path(temp) / ".agents" / "skills"
            actual = {p.parent.name for p in installed.glob("*/SKILL.md")}
            wanted = expected if selection == "*" else {selection}
            if actual != wanted:
                raise AssertionError(f"CLI discovery mismatch: {actual ^ wanted}")
            for name in wanted:
                assert_local_links(installed / name)
            print(f"Skills CLI {CLI_VERSION}: verified {len(actual)} skills; copy={copy}")


if __name__ == "__main__":
    main()
