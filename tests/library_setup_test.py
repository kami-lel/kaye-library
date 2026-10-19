"""
library_setup_test.py

Unit Tests (using pytest) for: setup_kaye_library_for_kaye_engine run
standalone over the library's own corpus
"""

import kaye_library
from kaye_engine.consumer import (
    get_consumer,
    get_consumer_canonical_name,
    get_consumer_display_name,
    iter_consumers,
)
from kaye_engine.prompt import get_corpus_tree
from kaye_engine.prompt.blueprint.render.comment import comment_line_registry


class TestStructure:

    def test_library_is_the_only_consumer(_):
        assert [c.canonical_name for c in iter_consumers()] == [
            "kaye-library"
        ]

    def test_library_is_entry_consumer(_):
        assert get_consumer_canonical_name() == "kaye-library"
        assert get_consumer_display_name() == "Kaye Library"

    def test_consumer_version_is_package_version(_):
        from importlib.metadata import version

        assert get_consumer("kaye-library").version == version("kaye-library")

    def test_corpus_tree_is_loaded(_):
        assert get_corpus_tree() is not None

    def test_comment_line_registered(_):
        assert any(
            line.startswith("Kaye Library v") for line in comment_line_registry
        )

    def test_abbrs_json_path_exists(_):
        assert kaye_library.get_kaye_library_abbrs_json_path().is_file()
