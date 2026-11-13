"""
anchor_test.py

Unit Tests (using pytest) for: every `#anchor` link in a corpus file
names a heading some library corpus file holds
"""

import pathlib
import re

import kaye_library
import pytest

_PACKAGE_DIR = pathlib.Path(kaye_library.__file__).resolve().parent
_CORPUS_FILES = sorted(_PACKAGE_DIR.rglob("*.md"))
_LINK = re.compile(r"\]\(#([^)\s]+)\)")
_FENCE = re.compile(r"^```.*?^```", re.DOTALL | re.MULTILINE)
_HEADING = re.compile(r"^#+ (.*)$", re.MULTILINE)


def _slug(heading):
    slug = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return slug.replace(" ", "-")


def _read(path):
    return _FENCE.sub("", path.read_text(encoding="utf-8"))


_ANCHORS = {
    _slug(m.group(1))
    for path in _CORPUS_FILES
    for m in _HEADING.finditer(_read(path))
}


@pytest.mark.parametrize(
    "path", _CORPUS_FILES, ids=lambda p: str(p.relative_to(_PACKAGE_DIR))
)
def test_every_anchor_matches_a_library_heading(path):
    dead = sorted(a for a in _LINK.findall(_read(path)) if a not in _ANCHORS)

    assert not dead, dead
