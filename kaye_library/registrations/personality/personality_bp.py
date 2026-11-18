"""
kaye_library.registrations.personality.personality_bp.py

register Personality related blueprints
"""

from kaye_engine import register_blueprint
from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
)

__all__ = ("register_personality_blueprints",)


def register_personality_blueprints():
    """
    register the internal, not exportable Personality blueprints:

    - ``persona-kaye-speech-habit``: Kaye's speech habits, free of any
      form of address
    - ``persona-kaye``: the Kaye persona under the Personality formatting
      rule, with the Personality Signature section, over its speech habits
    """
    kaye_node = get_corpus_node("Personality", "Kaye")
    register_blueprint(
        "persona-kaye-speech-habit",
        replace_meta(
            create_blueprint_from_node(
                kaye_node["Speech Habit Public"], is_recursive=True
            ),
            display_name="Kaye Speech Habit",
            description="Kaye's speech habits, free of any form of address",
        ),
        is_exportable=False,
    )

    # the Personality root alone: the rule separating Personality Content
    # from Task Content, which every persona speaks under; the signature
    # whole, each persona's name behind its {for <persona>} sidecar
    kaye = checkmark_nodes(
        create_blueprint_from_node(
            kaye_node, dependencies=["persona-kaye-speech-habit"]
        ),
        ("Personality",),
    )
    kaye = checkmark_nodes(
        kaye, ("Personality", "Personality Signature"), is_recursive=True
    )
    register_blueprint(
        "persona-kaye",
        replace_meta(
            kaye,
            display_name="Kaye",
            description="composed, exacting assistant persona",
        ),
        is_exportable=False,
    )
