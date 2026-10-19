"""
kaye_library.registrations.style.style_glossary.py

register Style related abbr glossaries
"""

from .._common import register_abbr_glossary

__all__ = ("register_style_abbr_glossaries",)


def register_style_abbr_glossaries():
    """
    register ``briefness-shorthand``, ``style-md-heading-abbr``,
    ``table-cell-values-shorthand``
    """
    register_abbr_glossary(
        "briefness-shorthand", False, is_dyn_substitution=True
    )
    register_abbr_glossary(
        "style-md-heading-abbr",
        False,
        is_sorted=True,
        is_dyn_substitution=True,
    )
    register_abbr_glossary(
        "table-cell-values-shorthand",
        False,
        is_dyn_substitution=True,
        is_sorted=True,
    )
