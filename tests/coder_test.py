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
from kaye_engine.prompt.blueprint.render_profile_registry import (
    render_profile_registry,
)

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

    def test_coder_depends_on_chat_and_persona_by_name(_):
        dependencies = blueprint_registry["coder"].blueprint.dependencies

        assert "chat" in dependencies
        assert "persona" in dependencies
        assert "chat-kaye" not in dependencies
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


def _text_with_descendants(node):
    nodes = [node, *node.descendants]
    return "\n".join("\n".join(n.content_lines()) for n in nodes)


class TestPlanForSuiteDecide:

    def _text(_):
        node = get_corpus_tree()["Coder"]["Plan for Suite"][
            "Bar 2: Write the Plan"
        ]
        return _text_with_descendants(node)

    @pytest.mark.parametrize(
        "needle",
        [
            "open with a Movement that cuts it",
            "that Movement also plants the linked worktree",
            "favor the Main Voice",
            "stretch of 3+ Movements you perform alone",
        ],
    )
    def test_decides_branch_worktree_and_voices(self, needle):
        assert needle in self._text()

    def test_leaves_voice_mode_to_execution(self):
        assert "**Mode**" not in self._text()

    def test_gather_decides_nothing(_):
        node = get_corpus_tree()["Coder"]["Plan for Suite"]["Bar 1: Gather"]
        text = "\n".join(node.content_lines())

        assert "open with a Movement that cuts it" not in text


class TestPlanForSuiteWrite:

    def _text(_):
        node = get_corpus_tree()["Coder"]["Plan for Suite"]
        return _text_with_descendants(node["Bar 2: Write the Plan"])

    def test_write_bar_holds_its_topics_as_nodes(_):
        node = get_corpus_tree()["Coder"]["Plan for Suite"]
        names = [n.name for n in node["Bar 2: Write the Plan"].children]

        assert names == [
            "Plan File",
            "Housekeeping Movements",
        ]

    def test_record_has_no_order_field(self):
        assert "- Order:" not in self._text()

    @pytest.mark.parametrize(
        "needle",
        [
            "each [Housekeeping Movements](#housekeeping-movements) decision",
            "cutting its instrumental branch from the feature branch",
            "then scrubs up per [Scrub After Feature Landing]",
            "`## Order`",
            "`## Main Voice`",
            "`🎻a: Title`",
        ],
    )
    def test_plans_decisions_and_voices(self, needle):
        assert needle in self._text()

    def test_movement_heading_drops_total(self):
        assert "🧩5\\8" not in self._text()

    def test_parallel_paragraph_is_gone(_):
        content = exportable_registry["plan-for-suite"].content()

        assert "Parallel execution" not in content

    def test_depends_on_diagrams(_):
        deps = blueprint_registry["plan-for-suite"].blueprint.dependencies

        assert "style-markdown-diagrams" in deps


class TestSoloVoice:

    @staticmethod
    def _content(surface):
        profile = render_profile_registry[surface].profile
        return exportable_registry["solo-voice"].content(profile=profile)

    @pytest.mark.parametrize("surface", ["claude-vsc", "hermes"])
    def test_carries_no_dispatch(self, surface):
        content = self._content(surface)

        for mark in ("🎏", "🎌", "🏁"):
            assert mark not in content

    def test_reports_through_send_message_on_claude_vsc(self):
        assert "`SendMessage`" in self._content("claude-vsc")

    def test_user_carries_report_on_hermes(self):
        content = self._content("hermes")

        assert "for the user to carry back" in content
        assert "`SendMessage`" not in content

    def test_takes_core_not_dispatch_marks(_):
        nodes = blueprint_registry["solo-voice"].blueprint.nodes

        assert not any(path[-1] == "Dispatch Marks" for path in nodes)

    def test_plan_for_suite_leaves_it_out(_):
        content = exportable_registry["plan-for-suite"].content()

        assert "### Solo Voice" not in content


class TestExecutionSplit:

    def test_execution_blueprint_is_internal(_):
        assert not blueprint_registry["plan-for-suite-execution"].is_exportable

    def test_execute_plan_for_suite_is_gone(_):
        assert "execute-plan-for-suite" not in blueprint_registry

    def test_play_suite_carries_execution_and_dispatch_marks(_):
        content = exportable_registry["play-suite"].content()

        assert "### Plan for Suite: Execution" in content
        assert "### Play Suite" in content
        assert "### Dispatch Marks" in content

    def test_solo_voice_shares_execution_only(_):
        deps = blueprint_registry["solo-voice"].blueprint.dependencies
        content = exportable_registry["solo-voice"].content()

        assert list(deps) == ["plan-for-suite-execution"]
        assert "### Plan for Suite: Execution" in content
        assert "### Play Suite" not in content

    def test_preface_names_play_suite_and_solo_voice(_):
        content = exportable_registry["plan-for-suite"].content()

        assert "`play-suite` if you run the Main Voice" in content
        assert "`solo-voice` if you run an instrumental Voice" in content
        assert "through the `Skill` tool" not in content


class TestPlaySuiteDispatch:

    @staticmethod
    def _content(surface):
        profile = render_profile_registry[surface].profile
        return exportable_registry["play-suite"].content(profile=profile)

    @pytest.mark.parametrize(
        "surface, needle",
        [
            ("claude-vsc", "1 `Agent` call in the background"),
            ("hermes", "1 `delegate_task` call"),
            ("codex", "With no subagent tool, run every instrumental Voice"),
        ],
    )
    def test_dispatch_route_per_surface(self, surface, needle):
        assert needle in self._content(surface)

    @pytest.mark.parametrize(
        "needle",
        [
            "##### Instrumental Voices",
            "merging its instrumental branch into the feature branch",
            "each open instrumental branch, and their linked worktrees still exist",
            "the instrumental Voice cuts its instrumental branch",
            "🎌 Violin Test Fixtures Merged Back",
        ],
    )
    def test_states_voice_lifecycle(self, needle):
        assert needle in self._content("claude-vsc")

    def test_next_line_drops_total(self):
        assert "🧭 🧩4\\7" not in self._content("claude-vsc")
