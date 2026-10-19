"""
privacy_test.py

Unit Tests (using pytest) for: the library ships no private or personal
string in any corpus file, abbreviation entry, or registration
"""

import pathlib

import kaye_library
import pytest

_PACKAGE_DIR = pathlib.Path(kaye_library.__file__).resolve().parent

# personal identifiers, contact data, and files only a private install has
_FORBIDDEN = (
    "prompt-writer",
    "/mnt/skills",
    "usc.edu",
    "1352194030",
    "kamilel",
    "kami-lel",
    "yangyi",
    "lu164457053",
    "盧仰一",
)

_SHIPPED_FILES = sorted(
    p
    for p in _PACKAGE_DIR.rglob("*")
    if p.is_file()
    and p.suffix in {".md", ".py", ".json"}
    and "__pycache__" not in p.parts
)


@pytest.mark.parametrize(
    "path", _SHIPPED_FILES, ids=lambda p: str(p.relative_to(_PACKAGE_DIR))
)
def test_no_private_string(path):
    text = path.read_text(encoding="utf-8").lower()

    for needle in _FORBIDDEN:
        assert needle.lower() not in text, needle
