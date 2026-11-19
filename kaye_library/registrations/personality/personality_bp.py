"""
kaye_library.registrations.personality.personality_bp.py

register Personality related blueprints
"""

from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
)

from .._common import register_internal

__all__ = ("register_personality_blueprints",)

_SIGNATURE_PATH = ("Personality", "Signature")

_DIATHESIS_PATH = ("Personality", "Diathesis Public")

_SPEECH_HABIT_PATH = ("Personality", "Speech Habit Public")

_IN_CHAT_PATH = ("Personality", "{in chat}")


def register_personality_blueprints():
    """
    register the internal, not exportable Personality blueprints:

    - ``persona-kaye-speech-habit``: Kaye's speech habits, free of any
      form of address
    - ``persona-kaye``: Kaye's Diathesis Public with the Signature section
      and the ``{in chat}`` formatting rule, over its speech habits
    """
    register_internal(
        "persona-kaye-speech-habit",
        replace_meta(
            create_blueprint_from_node(
                get_corpus_node(*_SPEECH_HABIT_PATH), is_recursive=True
            ),
            display_name="Kaye Speech Habit",
            description="Kaye's speech habits, free of any form of address",
        ),
    )

    # the whole Diathesis Public node, so a package's sections nested
    # beneath it ride along, gated by their sidecars; the Personality root
    # and the signature heading with Kaye's own section only, so a
    # package's other personas nested beside it stay out of this blueprint
    kaye = create_blueprint_from_node(
        get_corpus_node(*_DIATHESIS_PATH),
        is_recursive=True,
        dependencies=["persona-kaye-speech-habit"],
    )
    for path in (
        ("Personality",),
        _SIGNATURE_PATH,
        (*_SIGNATURE_PATH, "{for Kaye}"),
    ):
        kaye = checkmark_nodes(kaye, path)
    # the chat-only format, gated by the entry's ``in chat``
    kaye = checkmark_nodes(kaye, _IN_CHAT_PATH, is_recursive=True)
    register_internal(
        "persona-kaye",
        replace_meta(
            kaye,
            display_name="Kaye",
            description="composed, exacting assistant persona",
        ),
    )
