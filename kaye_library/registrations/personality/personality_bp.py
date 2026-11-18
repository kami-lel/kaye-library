"""
kaye_library.registrations.personality.personality_bp.py

register Personality related blueprints
"""

from kaye_engine import register_blueprint
from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
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
    - ``personality-persona-identity``: the Display Name and the Persona
      Co-author Trailer rule, each holding one ``{for <persona>}`` section
      per persona: Kaye's here, others' from a package
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

    # recursive, so each persona's {for <persona>} values a package
    # registers under these headings come along
    identity = create_blueprint()
    for name in ("Display Name", "Persona Co-author Trailer"):
        identity = checkmark_nodes(
            identity, ("Personality", name), is_recursive=True
        )
    register_blueprint(
        "personality-persona-identity",
        replace_meta(
            identity,
            display_name="Persona Identity",
            description=(
                "each persona's display name and co-author trailer, under"
                " the rule for when to sign"
            ),
        ),
        is_exportable=False,
    )
