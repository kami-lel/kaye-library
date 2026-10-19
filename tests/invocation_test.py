"""
invocation_test.py

Unit Tests (using pytest) for: every skill the library text tells the
assistant to invoke is a skill the library registers, so no instruction
dangles under the standalone command
"""

import pathlib
import re

import kaye_library
import pytest
from kaye_engine.exportable import exportable_registry

_ROOT = pathlib.Path(kaye_library.__file__).resolve().parent / "registrations"
# tool names and non-skill words that appear beside an Invoke instruction
_NOT_SKILLS = {"skill", "Skill", "Agent", "TodoWrite", "ReportFindings"}
_INVOKE = re.compile(r"[Ii]nvoke|`Skill`")


def _invocations():
    found = []
    for path in sorted(_ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for number, line in enumerate(text.split("\n"), 1):
            if not _INVOKE.search(line):
                continue
            for name in re.findall(r"`([a-z][a-z0-9-]+)`", line):
                if name not in _NOT_SKILLS:
                    found.append((f"{path.name}:{number}", name))
    return found


@pytest.mark.parametrize("where, name", _invocations())
def test_invoked_skill_is_registered(where, name):
    assert name in exportable_registry, f"{where} invokes `{name}`"


def test_some_invocations_are_checked():
    assert len(_invocations()) > 10
