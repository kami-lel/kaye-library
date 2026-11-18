"""
library_setup_test.py

Unit Tests (using pytest) for: setup_kaye_library_for_kaye_engine run
standalone over the library's own corpus
"""

import kaye_library
from importlib.metadata import version

from kaye_engine.consumer import (
    get_consumer,
    get_consumer_canonical_name,
    get_consumer_display_name,
    get_default_consumer,
    iter_consumers,
)
from kaye_engine.repo import get_repo_name, get_repo_version
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

    def test_library_is_default_consumer(_):
        assert get_default_consumer().canonical_name == "kaye-library"

    def test_repo_name_and_version_are_the_librarys_own(_):
        assert get_repo_name() == "kaye-library"
        assert get_repo_version() == version("kaye-library")

    def test_corpus_tree_is_loaded(_):
        assert get_corpus_tree() is not None

    def test_comment_line_registered(_):
        assert any(
            line.startswith("Kaye Library v") for line in comment_line_registry
        )

    def test_abbrs_json_path_exists(_):
        assert kaye_library.get_kaye_library_abbrs_json_path().is_file()


class TestChatBase:

    def test_chat_is_always_applied(_):
        from kaye_engine.exportable import exportable_registry

        chat = exportable_registry["chat"]

        assert chat.always_apply is True
        assert chat.consumer == "kaye-library"

    def test_chat_speaks_as_kaye(_):
        from kaye_engine.exportable import exportable_registry

        content = exportable_registry["chat"].content()

        assert "# Chat Agent" in content
        assert "## Kaye" in content
        assert "Kaye LeL" in content

    def test_chat_coder_is_not_invokable(_):
        from kaye_engine.exportable import exportable_registry

        entry = exportable_registry["chat-coder"]

        assert entry.llm_invokable is False
        assert entry.is_user_invokable is False

    def test_email_authuser_defaults_to_zero(_, testee_skills_folder):
        body = (
            testee_skills_folder / "sweep-email-inbox" / "SKILL.md"
        ).read_text(encoding="utf-8")

        assert "?authuser=0#all/" in body
