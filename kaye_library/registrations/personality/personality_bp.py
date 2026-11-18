"""
kaye_library.registrations.personality.personality_bp.py

register Personality related blueprints
"""

from kaye_engine import register_blueprint
from kaye_engine.prompt.blueprint import (
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
)

__all__ = ("register_personality_blueprints",)


def register_personality_blueprints():
    """
    register the internal, not exportable Personality blueprints:

    - ``personality-formatting``: the persona-free rule that splits
      Personality Content from Task Content; it lists the Kaye signifier
      alone, a building block for a package that composes its own personas
    - ``persona-kaye-speech-habit``: Kaye's speech habits, free of any
      form of address
    - ``persona-kaye``: the Kaye persona, over its speech habits
    """
    register_blueprint(
        "personality-formatting",
        replace_meta(
            create_blueprint_from_node(get_corpus_node("Personality")),
            display_name="Personality Formatting",
            description=(
                "the rule that separates Personality Content from Task"
                " Content"
            ),
        ),
        is_exportable=False,
    )

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
    register_blueprint(
        "persona-kaye",
        replace_meta(
            create_blueprint_from_node(
                kaye_node, dependencies=["persona-kaye-speech-habit"]
            ),
            display_name="Kaye",
            description="composed, exacting assistant persona",
        ),
        is_exportable=False,
    )
