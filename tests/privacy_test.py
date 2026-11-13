"""
privacy_test.py

Unit Tests (using pytest) for: the library ships no private or personal
string in any corpus file, abbreviation entry, or registration

Generic strings live here. Personal strings (names, emails, ids, domains)
live in the gitignored `tests/privacy-forbidden.local.txt`, 1 per line;
`#` starts a comment. Without that file only the generic list runs.
"""

import pathlib

import kaye_library
import pytest

_PACKAGE_DIR = pathlib.Path(kaye_library.__file__).resolve().parent
_LOCAL_FILE = pathlib.Path(__file__).resolve().parent / (
    "privacy-forbidden.local.txt"
)

# files and words only a private install has
_FORBIDDEN = (
    "vault",
    "/mnt/skills",
    "prompt-writer",
    "persona trailer",
)


def _load_local_forbidden():
    if not _LOCAL_FILE.is_file():
        return ()
    lines = _LOCAL_FILE.read_text(encoding="utf-8").splitlines()
    return tuple(
        s.strip() for s in lines if s.strip() and not s.startswith("#")
    )


_LOCAL_FORBIDDEN = _load_local_forbidden()

_SHIPPED_FILES = sorted(
    p
    for p in _PACKAGE_DIR.rglob("*")
    if p.is_file()
    and p.suffix in {".md", ".py", ".json"}
    and "__pycache__" not in p.parts
)


def _scan(path, needles):
    text = path.read_text(encoding="utf-8").lower()

    for needle in needles:
        assert needle.lower() not in text, needle


@pytest.mark.parametrize(
    "path", _SHIPPED_FILES, ids=lambda p: str(p.relative_to(_PACKAGE_DIR))
)
def test_no_generic_private_string(path):
    _scan(path, _FORBIDDEN)


@pytest.mark.skipif(
    not _LOCAL_FORBIDDEN,
    reason="tests/privacy-forbidden.local.txt absent: personal strings "
    "are not checked",
)
@pytest.mark.parametrize(
    "path", _SHIPPED_FILES, ids=lambda p: str(p.relative_to(_PACKAGE_DIR))
)
def test_no_local_private_string(path):
    _scan(path, _LOCAL_FORBIDDEN)
