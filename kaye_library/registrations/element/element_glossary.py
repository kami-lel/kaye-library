"""
kaye_library.registrations.element.element_glossary.py

register Element related abbr glossaries
"""

from .._common import register_abbr_glossary

__all__ = ("register_element_abbr_glossaries",)


def register_element_abbr_glossaries():
    """
    register ``units-of-measure``, ``element-dt-days-of-week``,
    ``element-dt-watch-day-abbr``, ``element-dt-watch-week-abbr``
    """
    register_abbr_glossary("units-of-measure", True, is_dyn_substitution=True)

    register_abbr_glossary(
        "element-dt-days-of-week",
        True,
        is_sorted=True,
    )
    register_abbr_glossary(
        "element-dt-watch-day-abbr", False, is_dyn_substitution=True
    )
    register_abbr_glossary(
        "element-dt-watch-week-abbr", False, is_dyn_substitution=True
    )
