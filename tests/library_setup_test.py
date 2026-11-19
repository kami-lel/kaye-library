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
from kaye_engine.prompt.blueprint.registry import blueprint_registry
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

        chat = exportable_registry["chat-kaye"]

        assert chat.always_apply is True
        assert chat.consumer == "kaye-library"

    def test_chat_speaks_as_kaye(_):
        from kaye_engine.exportable import exportable_registry

        content = exportable_registry["chat-kaye"].content()

        assert "# Chat Agent" in content
        assert "## Diathesis Public" in content
        assert "Kaye LeL" in content

    def test_chat_stack_is_layered(_):
        from kaye_engine.exportable import exportable_registry

        assert "chat" not in exportable_registry
        for name in ("chat-basic", "chat", "chat-basic-kaye"):
            assert not blueprint_registry[name].is_exportable
        assert blueprint_registry["chat"].blueprint.dependencies == (
            "chat-basic",
        )
        assert blueprint_registry["chat-kaye"].blueprint.dependencies == (
            "chat",
            "persona",
        )

    def test_chat_basic_is_persona_free(_):
        content = blueprint_registry["chat"].content()

        assert "# Chat Agent" in content
        assert "Kaye" not in content.replace("Kaye Library", "")

    def test_hermes_soul_equals_chat_kaye(_):
        assert (
            blueprint_registry["chat-basic-kaye"].content().split("<!--")[0]
            == blueprint_registry["chat-kaye"].content().split("<!--")[0]
        )

    def test_cli_names_chat_and_coder(_):
        from kaye_engine.exportable import exportable_registry

        assert "chat-coder" not in exportable_registry
        assert exportable_registry["coder"].always_apply is True

    def test_email_authuser_defaults_to_zero(_, testee_skills_folder):
        body = (
            testee_skills_folder / "sweep-email-inbox" / "SKILL.md"
        ).read_text(encoding="utf-8")

        assert "?authuser=0#all/" in body
