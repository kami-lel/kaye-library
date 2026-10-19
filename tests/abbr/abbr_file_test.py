"""
abbr_file_test.py

Unit Tests (using pytest) for: the library's own ``abbrs.json``, which
loads standalone and names only glossaries the library registers
"""

import json

import kaye_library
import pytest
from kaye_engine.abbr_collection import (
    AbbrTags,
    abbr_glossary_registry,
    get_abbr_data,
)


def _load_json():
    with open(
        kaye_library.get_kaye_library_abbrs_json_path(), encoding="utf-8"
    ) as file:
        return json.load(file)


def _entries():
    for meaning, obj in _load_json().items():
        for abbr, entry in obj["abbrs"].items():
            yield meaning, abbr, entry


class TestFile:

    def test_not_empty(_):
        assert _load_json()

    def test_every_entry_carries_a_library_glossary(_):
        for meaning, abbr, entry in _entries():
            glossaries = [t for t in entry["tags"] if t not in AbbrTags.__members__]
            assert glossaries, f"{abbr}:{meaning} names no glossary"

    def test_names_only_registered_library_glossaries(_):
        for meaning, abbr, entry in _entries():
            for tag in entry["tags"]:
                assert tag in AbbrTags.__members__ or (
                    tag in abbr_glossary_registry
                ), f"{abbr}:{meaning} names unknown glossary {tag}"

    def test_carries_no_habit_flag(_):
        for meaning, abbr, entry in _entries():
            assert "always_understand" not in entry["tags"], (abbr, meaning)
            assert "common" not in entry["tags"], (abbr, meaning)


class TestLoaded:

    @pytest.mark.parametrize("glossary", sorted(abbr_glossary_registry))
    def test_every_library_glossary_has_entries(_, glossary):
        entries = [e for e in get_abbr_data().abbrs if glossary in e.glossaries]

        assert entries, f"glossary {glossary} has no entry"
