"""
kaye_library.registrations.personality.personality_bp.py

register Personality related blueprints
"""

from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
    replace_meta,
)

from .._common import register_internal

__all__ = ("register_personality_blueprints",)

# every persona kind node ``persona`` takes whole; each holds one
# ``{for NAME}`` section per persona, so the entry's profile picks one
_PERSONA_PATHS = (
    ("Personality", "Signature"),
    ("Personality", "Diathesis Public"),
    ("Personality", "Speech Habit Public"),
    ("Personality", "{in chat}"),
)


def register_personality_blueprints():
    """
    register the internal, not exportable ``persona``: the Personality root
    with its Signature, Diathesis Public, Speech Habit Public and
    ``{in chat}`` nodes, each whole

    persona-free: it names no persona of its own, so an entry renders the
    one its render profile turns on (``for Kaye``), and a package nesting
    another persona's ``{for NAME}`` sections beneath these nodes never
    leaks it into a Kaye entry; a package replaces it in place, by name,
    with ``override_blueprint``
    """
    bp = checkmark_nodes(create_blueprint(), ("Personality",))
    for path in _PERSONA_PATHS:
        bp = checkmark_nodes(bp, path, is_recursive=True)
    register_internal(
        "persona",
        replace_meta(
            bp,
            display_name="Persona",
            description=(
                "the persona layer, its persona picked by the entry's "
                "render profile"
            ),
        ),
    )
