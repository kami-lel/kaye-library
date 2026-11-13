"""
example_consumer_test.py

Unit Tests (using pytest) for: examples/minimal-consumer installs and
runs in a subprocess, adds its own skill, replaces the default values,
and takes one library skill over
"""

import os
import pathlib
import re
import subprocess
import sys
import tomllib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parent.parent
_EXAMPLE = _ROOT / "examples" / "minimal-consumer"


@pytest.fixture(scope="module")
def installed(tmp_path_factory):
    pytest.importorskip("setuptools")
    target = tmp_path_factory.mktemp("install")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--no-deps",
            "--no-build-isolation",
            "--target",
            str(target),
            str(_EXAMPLE),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return target


def _run(installed, *args):
    env = {
        **os.environ,
        "PYTHONPATH": os.pathsep.join(
            [str(installed), os.environ.get("PYTHONPATH", "")]
        ),
    }
    return subprocess.run(
        [sys.executable, "-m", "example_consumer", *args],
        capture_output=True,
        text=True,
        check=False,
        cwd=_ROOT,
        env=env,
    )


@pytest.fixture(scope="module")
def exported(installed, tmp_path_factory):
    folder = tmp_path_factory.mktemp("skills")
    result = _run(installed, "skill", "--all", str(folder))
    assert result.returncode == 0, result.stderr
    return folder


def _skill(exported, name):
    return (exported / name / "SKILL.md").read_text(encoding="utf-8")


class TestExampleConsumer:

    def test_pin_matches_library_version(_):
        library = tomllib.loads(
            (_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        )["project"]["version"]
        base = re.match(r"\d+\.\d+\.\d+", library).group(0)
        example = (_EXAMPLE / "pyproject.toml").read_text(encoding="utf-8")

        pin = re.search(r"kaye-library\.git@(v[^\"\s]+)", example)
        assert pin is not None
        assert pin.group(1) == "v" + base

    def test_help_runs(_, installed):
        result = _run(installed, "--help")

        assert result.returncode == 0

    def test_adds_its_own_skill(_, exported):
        assert "Lead every answer" in _skill(exported, "example-house-rules")

    def test_replaces_the_default_authuser(_, exported):
        body = _skill(exported, "sweep-email-inbox")

        assert "?authuser=1#all/" in body
        assert "?authuser=0#all/" not in body

    def test_adds_its_own_calendar(_, exported):
        assert "Side Project" in _skill(exported, "push-event-to-calendar")

    def test_takes_a_library_skill_over(_, exported):
        body = _skill(exported, "style-good-writing")

        assert "Lead every answer" in body
        assert "Correct spelling, grammar" in body

    def test_leaves_no_placeholder(_, exported):
        assert not [
            p
            for p in exported.rglob("SKILL.md")
            if "(((" in p.read_text(encoding="utf-8")
        ]
