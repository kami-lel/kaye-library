"""
agent_test.py

Unit Tests (using pytest) for: the Agentic corpus the library ships -- the
workflow skeleton, with Turn Progress Dispatch a node of its own and no
conversation-persona rules
"""

import pytest
from kaye_engine.exportable import exportable_registry
from kaye_engine.prompt import get_corpus_tree
from kaye_engine.prompt.blueprint.registry import blueprint_registry


def _agentic():
    return get_corpus_tree()["Agentic"]


class TestStructure:

    @pytest.mark.parametrize(
        "name",
        [
            "Turn Progress Dispatch",
            "Files & Folders",
            "Movement, Voice, and Suite",
            "Halt Each Movement",
            "Cascade All Movements",
        ],
    )
    def test_node_under_agentic(_, name):
        assert name in {c.name for c in _agentic().children}

    def test_chat_agent_is_a_root_node_not_under_agentic(_):
        assert "Chat Agent" in {c.name for c in get_corpus_tree().children}
        assert "Chat Agent" not in {c.name for c in _agentic().children}

    def test_agent_sidecar_stays_under_agentic(_):
        names = {c.name for c in _agentic().children}

        assert "{[Claude:Agent~] Usage}" in names


class TestTurnProgressDispatch:

    def test_glossary_is_spliced(_):
        text = "\n".join(_agentic()["Turn Progress Dispatch"].content_lines())

        assert "(((agent-chat-turn-progress-dispatch-decorative)))" in text

    def test_names_no_chat_only_rule(_):
        text = "\n".join(_agentic()["Turn Progress Dispatch"].content_lines())

        assert "em dash" not in text
        assert "DNT" not in text


class TestTaskBlockageWorkaround:

    def test_node_under_agentic(_):
        names = {c.name for c in _agentic().children}

        assert "Task Blockage Workaround" in names

    def test_blueprint_is_internal(_):
        entry = blueprint_registry["agent-task-blockage-workaround"]

        assert not entry.is_exportable
        assert "agent-task-blockage-workaround" not in exportable_registry


class TestMovementVoiceAndSuite:

    def _node(_):
        return _agentic()["Movement, Voice, and Suite"]

    def test_dispatch_marks_is_a_child_node(self):
        names = {c.name for c in self._node().children}

        assert "Dispatch Marks" in names

    def test_core_body_carries_no_dispatch(self):
        text = "\n".join(self._node().content_lines())

        assert "🎏" not in text
        assert "Turn Progress Dispatch" not in text

    def test_notation_carries_no_total(self):
        node = self._node()["Movement Notation"]
        text = "\n".join(node.content_lines())

        assert "🧩a\\b" not in text
        assert "🧩a SUMMARY" in text

    @pytest.mark.parametrize(
        "name",
        ["agent-movement-and-suite", "agent-movement-and-suite-with-count"],
    )
    def test_blueprint_checkmarks_dispatch_marks(_, name):
        nodes = blueprint_registry[name].blueprint.nodes

        assert any(path[-1] == "Dispatch Marks" for path in nodes)

    def test_defines_instrumental_voice_in_2_modes(self):
        text = "\n".join(self._node().content_lines())

        assert "**instrumental Voice**" in text
        assert "soloed by a subagent" in text
        assert "run in its own session" in text

    def test_dispatch_marks_kept_to_main_session(self):
        node = self._node()["Dispatch Marks"]
        text = "\n".join(node.content_lines())

        assert "Only the main session writes these marks" in text


class TestHaltAndCascadeVoices:

    @pytest.mark.parametrize(
        "name", ["Halt Each Movement", "Cascade All Movements"]
    )
    def test_governs_main_voice_only(_, name):
        text = "\n".join(_agentic()[name].content_lines())

        assert "Main Voice only" in text
        assert "🎌 Violin" in text
        assert "🧩4\\7" not in text

    @pytest.mark.parametrize(
        "name", ["Halt Each Movement", "Cascade All Movements"]
    )
    def test_states_session_case(_, name):
        text = "\n".join(_agentic()[name].content_lines())

        assert "whatever halt mode its own session loads" in text
        assert "sent from its session" in text
