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
            "Movement and Suite",
            "Halt Each Movement",
            "Cascade All Movements",
        ],
    )
    def test_node_under_agentic(_, name):
        assert name in {c.name for c in _agentic().children}

    def test_no_chat_agent_node(_):
        assert "Chat Agent" not in {c.name for c in get_corpus_tree().children}
        assert "Chat Agent" not in {c.name for c in _agentic().children}

    def test_agent_sidecar_stays_under_agentic(_):
        names = {c.name for c in _agentic().children}

        assert "{[ClaudeCode:Agent~] Usage}" in names


class TestTurnProgressDispatch:

    def test_glossary_is_spliced(_):
        text = "\n".join(_agentic()["Turn Progress Dispatch"].content_lines())

        assert "(((agent-chat-turn-progress-dispatch-decorative)))" in text

    def test_names_no_chat_only_rule(_):
        text = "\n".join(_agentic()["Turn Progress Dispatch"].content_lines())

        assert "em dash" not in text
        assert "DNT" not in text


class TestUnreachableTaskWorkaround:

    def test_node_under_agentic(_):
        names = {c.name for c in _agentic().children}

        assert "Unreachable Task Workaround" in names

    def test_blueprint_is_internal(_):
        entry = blueprint_registry["agent-unreachable-task-workaround"]

        assert not entry.is_exportable
        assert "agent-unreachable-task-workaround" not in exportable_registry
