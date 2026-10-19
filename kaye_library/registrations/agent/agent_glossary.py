"""
kaye_library.registrations.agent.agent_glossary.py

register Agentic related abbr glossaries
"""

from .._common import register_abbr_glossary

__all__ = ("register_agent_abbr_glossaries",)


def register_agent_abbr_glossaries():
    """
    register ``agent-chat-turn-progress-dispatch-decorative``
    """
    register_abbr_glossary(
        "agent-chat-turn-progress-dispatch-decorative",
        False,
        is_sorted=True,
        is_dyn_substitution=True,
    )
