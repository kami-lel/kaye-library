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
    register ``personality-formatting``, the persona-free rule that
    splits Personality Content from Task Content

    internal, not exportable: it lists the Kaye signifier alone, a
    building block for a package that composes its own personas
    """
    formatting_node = get_corpus_node("Personality")["Personality Formatting"]
    register_blueprint(
        "personality-formatting",
        replace_meta(
            create_blueprint_from_node(formatting_node),
            display_name="Personality Formatting",
            description=(
                "the rule that separates Personality Content from Task"
                " Content"
            ),
        ),
        is_exportable=False,
    )
