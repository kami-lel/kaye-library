"""
kaye_library.registrations.agent.agent_glossary.py

register Agentic related abbr glossaries
"""

from .._common import register_abbr_glossary

__all__ = ("register_agent_abbr_glossaries",)


def register_agent_abbr_glossaries():
    """
    register ``agent-chat-decorative``, ``agent-chat-discourse-unit``,
    ``agent-chat-turn-progress-dispatch-decorative``, and
    ``natural-language-codes``
    """
    register_abbr_glossary(
        "agent-chat-decorative", False, is_dyn_substitution=True
    )
    register_abbr_glossary(
        "agent-chat-discourse-unit",
        False,
        is_sorted=True,
        is_dyn_substitution=True,
    )
    register_abbr_glossary(
        "natural-language-codes",
        True,
        is_dyn_substitution=True,
        description=(
            "Decodes language codes such as en, zh, and jp to the natural"
            " languages they name."
        ),
        when_to_use=(
            "When a language code such as de, en, zh, zhs, zht, or jp"
            " appears in a message, a prompt, or a reply-language rule."
        ),
    )
    register_abbr_glossary(
        "agent-chat-turn-progress-dispatch-decorative",
        False,
        is_sorted=True,
        is_dyn_substitution=True,
    )
