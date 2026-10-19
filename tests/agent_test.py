"""
agent_test.py

Unit Tests (using pytest) for: the Agentic corpus the library ships -- the
workflow skeleton, with Turn Progress Dispatch a node of its own and no
conversation-persona rules
"""

import pytest
from kaye_engine.prompt import get_corpus_tree


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
