"""
console_test.py

Unit Tests (using pytest) for: the ``kaye-library`` console command and
``python -m kaye_library``, run as subprocesses over the library's own
corpus
"""

import json
import pathlib
import subprocess
import sys

import pytest

_ROOT = pathlib.Path(__file__).resolve().parent.parent


def _run(*args, command=(sys.executable, "-m", "kaye_library")):
    # run from the repository root, so the working tree is what runs
    return subprocess.run(
        [*command, *args],
        capture_output=True,
        text=True,
        check=False,
        cwd=_ROOT,
    )


class TestHelp:

    @pytest.mark.parametrize(
        "command",
        [("kaye-library",), (sys.executable, "-m", "kaye_library")],
    )
    def test_help_exits_zero(_, command):
        result = _run("--help", command=command)

        assert result.returncode == 0
        assert "Kaye Engine CLI: " in result.stdout

    def test_version(_):
        result = _run("--version")

        assert result.returncode == 0
        assert result.stdout.strip()


class TestEngineSubcommands:

    def test_blueprint_list_shows_only_library_blueprints(_):
        result = _run("blueprint", "list")

        assert result.returncode == 0
        names = result.stdout.split()
        assert "commit-sense" in names
        assert "coder" in names
        assert "chat" in names
        assert "chat-coder" in names
        assert "kaye-chat" not in names

    def test_skill_all_exports_every_skill(_, tmp_path):
        result = _run("skill", "--all", str(tmp_path))

        assert result.returncode == 0
        assert (tmp_path / "commit-sense" / "SKILL.md").is_file()
        assert (tmp_path / "style-markdown" / "SKILL.md").is_file()

    def test_claude_plugin_writes_one_plugin(_, tmp_path):
        result = _run("claude", "plugin", str(tmp_path))

        assert result.returncode == 0
        assert [p.name for p in tmp_path.iterdir()] == ["kaye-library"]

    def test_claude_plugin_zip_writes_one_zip(_, tmp_path):
        result = _run("claude", "plugin", "-z", str(tmp_path))

        assert result.returncode == 0
        names = [p.name for p in tmp_path.iterdir()]
        assert len(names) == 1 and names[0].startswith("kaye-library-claude-")

    def test_marketplace_is_engine_named_with_library_plugin_only(
        _, tmp_path
    ):
        result = _run("claude", "marketplace", str(tmp_path))
        data = json.loads(
            (tmp_path / ".claude-plugin" / "marketplace.json").read_text(
                encoding="utf-8"
            )
        )

        assert result.returncode == 0
        assert data["name"] == "kaye-engine"
        assert [p["name"] for p in data["plugins"]] == ["kaye-library"]


class TestChatBoundSubcommands:

    def test_claude_code_writes_a_folder(_, tmp_path):
        result = _run("claude", "code", str(tmp_path))

        assert result.returncode == 0, result.stderr
        assert (tmp_path / "CLAUDE.md").is_file()

    def test_user_system_prompt_is_persona_free_chat(_):
        result = _run("claude", "user-system-prompt")

        assert result.returncode == 0, result.stderr
        assert "Chat Agent" in result.stdout
        assert "Turn Progress Dispatch" in result.stdout
        assert "(((" not in result.stdout

    def test_hermes_writes_a_soul(_, tmp_path):
        result = _run("hermes", str(tmp_path))

        assert result.returncode == 0, result.stderr
        assert (tmp_path / "SOUL.md").is_file()

    def test_standalone_exports_leave_no_placeholder(_, tmp_path):
        result = _run("skill", "--all", str(tmp_path))

        assert result.returncode == 0, result.stderr
        assert "unresolved" not in result.stderr
        assert not [
            p
            for p in tmp_path.rglob("SKILL.md")
            if "(((" in p.read_text(encoding="utf-8")
        ]
