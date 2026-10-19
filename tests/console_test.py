"""
console_test.py

Unit Tests (using pytest) for: the ``kaye-library`` console command and
``python -m kaye_library``, run as subprocesses over the library's own
corpus
"""

import json
import subprocess
import sys

import pytest


def _run(*args, command=("kaye-library",)):
    return subprocess.run(
        [*command, *args], capture_output=True, text=True, check=False
    )


class TestHelp:

    @pytest.mark.parametrize(
        "command",
        [("kaye-library",), (sys.executable, "-m", "kaye_library")],
    )
    def test_help_exits_zero(_, command):
        result = _run("--help", command=command)

        assert result.returncode == 0
        assert "kaye-library" in result.stdout

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
        assert "coder-core" in names
        assert "chat" not in names
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
        assert len(names) == 1 and names[0].startswith("kaye-library-")

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

    @pytest.mark.parametrize(
        "args, message",
        [
            (("claude", "code"), "Coder exportable name"),
            (("claude", "user-system-prompt"), "Chat exportable name"),
            (("claude", "vs-code-extension"), "Coder exportable name"),
            (("hermes",), "soul blueprint name"),
        ],
    )
    def test_exits_one_with_a_clear_message(_, tmp_path, args, message):
        extra = (str(tmp_path),) if args[-1] in {"vs-code-extension", "hermes"} else ()
        result = _run(*args, *extra)

        assert result.returncode == 1
        assert message in result.stderr
