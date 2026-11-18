"""
kaye_library.registrations.personality.personality_bp.py

register Personality related blueprints
"""

from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
    uncheckmark_nodes,
)

from .._common import register_internal

__all__ = ("register_personality_blueprints",)

_SIGNATURE_PATH = ("Personality", "Personality Signature")


def register_personality_blueprints():
    """
    register the internal, not exportable Personality blueprints:

    - ``persona-kaye-speech-habit``: Kaye's speech habits, free of any
      form of address
    - ``persona-kaye``: the whole Kaye node under the Personality formatting
      rule, with the Personality Signature section, over its speech habits
    """
    kaye_node = get_corpus_node("Personality", "Kaye")
    register_internal(
        "persona-kaye-speech-habit",
        replace_meta(
            create_blueprint_from_node(
                kaye_node["Speech Habit Public"], is_recursive=True
            ),
            display_name="Kaye Speech Habit",
            description="Kaye's speech habits, free of any form of address",
        ),
    )

    # the whole Kaye node, so a package's sections nested beneath it ride
    # along, gated by their sidecars, less the speech habit, which comes by
    # its own blueprint; the Personality root and the signature heading
    # with Kaye's own section only, so a package's other personas nested
    # beside it stay out of this blueprint
    kaye = create_blueprint_from_node(
        kaye_node,
        is_recursive=True,
        dependencies=["persona-kaye-speech-habit"],
    )
    kaye = uncheckmark_nodes(
        kaye, kaye_node["Speech Habit Public"], is_recursive=True
    )
    for path in (
        ("Personality",),
        _SIGNATURE_PATH,
        (*_SIGNATURE_PATH, "{for Kaye}"),
    ):
        kaye = checkmark_nodes(kaye, path)
    register_internal(
        "persona-kaye",
        replace_meta(
            kaye,
            display_name="Kaye",
            description="composed, exacting assistant persona",
        ),
    )
