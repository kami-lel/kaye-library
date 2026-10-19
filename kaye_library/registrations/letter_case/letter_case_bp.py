"""
kaye_library.registrations.letter_case.letter_case_bp.py

register Letter Case related blueprints
"""

from .._common import register_exportable, register_leaf

__all__ = ("register_letter_case_blueprints",)


def _register_letter_case_leaf(slug, leaf_name):
    """
    register a Letter Case sub-case with its ancestor nodes
    """
    register_leaf(
        register_exportable,
        slug,
        ["Style Guide", "Letter Case"],
        leaf_name,
    )


def register_letter_case_blueprints():
    """
    register Letter Case's sub-cases: Snake Case, Kebab Case,
    Pascal Case, Camel Case, All Caps, Title Case, Commentary Case
    """
    _register_letter_case_leaf(
        "style-letter-case-snake-case", "Letter Case Snake Case"
    )

    _register_letter_case_leaf(
        "style-letter-case-kebab-case", "Letter Case Kebab Case"
    )

    _register_letter_case_leaf(
        "style-letter-case-pascal-case", "Letter Case Pascal Case"
    )

    _register_letter_case_leaf(
        "style-letter-case-camel-case", "Letter Case Camel Case"
    )

    _register_letter_case_leaf(
        "style-letter-case-all-caps", "Letter Case All Caps"
    )

    _register_letter_case_leaf(
        "style-letter-case-title-case", "Letter Case Title Case"
    )

    _register_letter_case_leaf(
        "style-letter-case-commentary-case", "Letter Case Commentary Case"
    )
