"""
kaye_library.registrations.general.general_bp.py

register general-purpose blueprints
"""

from kaye_engine import register_blueprint
from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
    replace_meta,
)

__all__ = ("register_general_blueprints",)


def register_general_blueprints():
    """
    register Rapid


    :raises ValueError: ``style-markdown`` is not yet registered
    """
    # Rapid
    # depends on Style Guide Markdown Format, reusing its own
    # standalone registered blueprint instead of re-inlining it
    rapid = register_blueprint(
        "rapid",
        replace_meta(
            checkmark_nodes(
                create_blueprint(dependencies=["style-markdown"]),
                ("Style Guide",),
            ),
            display_name="Rapid",
        ),
        is_exportable=False,
    )
    rapid.blueprint = replace_meta(
        rapid.blueprint,
        description=(
            "quick, mechanical text or data tasks with no persona or role"
        ),
    )
