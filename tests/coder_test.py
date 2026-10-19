"""
coder_test.py

Unit Tests (using pytest) for: the Coder corpus and skills the library
ships -- persona-free, the rules in an internal ``coder-core``, every
language profile under the ``Coder`` node
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
    "Coder Unity Engine",
    "Coder GDScript",
    "Coder HTML",
    "Coder JavaScript and TypeScript",
    "Coder Python",
)
_CODER_SKILLS = sorted(
    name
    for name, entry in exportable_registry.items()
    if entry.consumer == "kaye-library"
    and (name.startswith("coder-") or name in {"review-gaps", "sync-unit-test"})
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

    def test_core_is_internal(_):
        assert "coder-core" in blueprint_registry
        assert "coder-core" not in exportable_registry

    def test_no_persona_coder_skill(_):
        assert "coder" not in exportable_registry

    def test_gap_review_has_its_final_name(_):
        assert "review-gaps" in exportable_registry
        assert "gap-review" not in exportable_registry

    def test_sync_unit_test_ships(_):
        assert "sync-unit-test" in exportable_registry

    def test_core_depends_on_no_conversation_rules(_):
        dependencies = blueprint_registry["coder-core"].blueprint.dependencies

        assert "chat" not in dependencies
        assert "element-triage-tags" in dependencies


class TestRender:

    def test_core_renders_the_rules(_):
        content = blueprint_registry["coder-core"].content()

        assert "# Coder" in content
        assert "explore first, per [Project Context Engineering]" in content
        assert "each line must not exceed **80 characters**" in content

    @pytest.mark.parametrize(
        "needle", ["Kaye", "Personality", "Persona", "Kami", "Sir"]
    )
    def test_core_names_no_persona(_, needle):
        assert needle not in blueprint_registry["coder-core"].content()

    @pytest.mark.parametrize("name", _CODER_SKILLS)
    def test_skill_renders_without_persona(_, name):
        content = exportable_registry[name].content()

        assert content.strip()
        for needle in ("Kaye", "Persona", "Kami"):
            assert needle not in content, name
