"""
coder_test.py

Unit Tests (using pytest) for: the Coder corpus and skills the library
ships -- ``coder`` as Kaye Peer Coder, ``chat`` plus the rules; every
language profile under the ``Coder`` node, persona-free
"""

import pytest
from kaye_engine.exportable import exportable_registry
from kaye_engine.prompt import get_corpus_tree
from kaye_engine.prompt.blueprint.registry import blueprint_registry

_LANGUAGE_NODES = (
    "Bash",
    "Coder PowerShell",
    "Coder C",
    "Coder CPP",
    "Coder Unreal Engine",
    "Coder C Sharp",
    "Coder GDScript",
    "Coder HTML",
    "Coder JavaScript and TypeScript",
    "Coder Python",
)
_CODER_SKILLS = sorted(
    name
    for name, entry in exportable_registry.items()
    if entry.consumer == "kaye-library"
    and (
        name.startswith("coder-")
        or name in {"review-gaps", "sync-unit-test"}
    )
)


class TestCorpus:

    def test_root_is_coder(_):
        names = {c.name for c in get_corpus_tree().children}

        assert "Coder" in names
        assert "Kaye Peer Coder" not in names

    @pytest.mark.parametrize("name", _LANGUAGE_NODES)
    def test_language_file_registers_under_coder(_, name):
        assert name in {c.name for c in get_corpus_tree()["Coder"].children}

    def test_links_point_at_coder(_):
        text = "\n".join(
            "\n".join(node.content_lines())
            for node in get_corpus_tree()["Coder"].descendants
        )

        assert "(#kaye-peer-coder)" not in text
        assert "[Coder](#coder)" in text


class TestBlueprints:

    def test_no_separate_core_entry(_):
        assert "coder-core" not in blueprint_registry

    def test_coder_skill_is_kaye_peer_coder_and_the_library_s(_):
        entry = exportable_registry["coder"]

        assert entry.consumer == "kaye-library"
        assert "element-triage-tags" in entry.blueprint.dependencies
        assert entry.display_name == "Kaye Peer Coder"
        assert entry.always_apply

    def test_gap_review_has_its_final_name(_):
        assert "review-gaps" in exportable_registry
        assert "gap-review" not in exportable_registry

    def test_sync_unit_test_ships(_):
        assert "sync-unit-test" in exportable_registry

    def test_coder_depends_on_chat_kaye_by_name(_):
        dependencies = blueprint_registry["coder"].blueprint.dependencies

        assert "chat-kaye" in dependencies
        assert "element-triage-tags" in dependencies

    def test_chat_coder_is_gone(_):
        assert "chat-coder" not in blueprint_registry


class TestRender:

    def test_coder_renders_the_rules(_):
        content = blueprint_registry["coder"].content()

        assert "# Coder" in content
        assert "explore first, per [Project Context Engineering]" in content
        assert "each line must not exceed **80 characters**" in content

    def test_coder_speaks_as_kaye(_):
        content = exportable_registry["coder"].content()

        assert "# Chat Agent" in content
        assert "## Diathesis Public" in content
        assert "Kaye LeL" in content

    @pytest.mark.parametrize("needle", ["Kami", "Sir"])
    def test_coder_names_no_user(_, needle):
        assert needle not in blueprint_registry["coder"].content()

    @pytest.mark.parametrize("name", _CODER_SKILLS)
    def test_skill_renders_without_persona(_, name):
        content = exportable_registry[name].content()

        assert content.strip()
        for needle in ("Kaye", "Persona", "Kami"):
            assert needle not in content, name
