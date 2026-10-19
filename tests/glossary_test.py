"""
glossary_test.py

Unit Tests (using pytest) for: the abbr glossaries the library registers
"""

import pytest
from kaye_engine.abbr_collection import abbr_glossary_registry

_LIBRARY_GLOSSARIES = (
    "briefness-shorthand",
    "commit-sense-shorthand",
    "commit-sense-sigil",
    "element-dt-days-of-week",
    "element-dt-watch-day-abbr",
    "element-dt-watch-week-abbr",
    "git-abbr",
    "style-md-heading-abbr",
    "table-cell-values-shorthand",
    "units-of-measure",
)


class TestRegistered:

    @pytest.mark.parametrize("name", _LIBRARY_GLOSSARIES)
    def test_glossary_registered(_, name):
        assert name in abbr_glossary_registry

    def test_only_library_glossaries_registered(_):
        assert set(abbr_glossary_registry) == set(_LIBRARY_GLOSSARIES)

    @pytest.mark.parametrize("name", _LIBRARY_GLOSSARIES)
    def test_exportable_glossary_names_library_consumer(_, name):
        reg = abbr_glossary_registry[name]

        assert reg.consumer == "kaye-library"
