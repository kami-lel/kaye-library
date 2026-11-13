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
    register_abbr_glossary(
        "units-of-measure",
        True,
        is_dyn_substitution=True,
        description=(
            "Decodes unit abbreviations such as ft, lb, and mi to the units"
            " they name."
        ),
        when_to_use=(
            "Trigger when a unit abbreviation such as ft, lb, or hr appears,"
            " or the user asks what a unit symbol means."
        ),
    )

    register_abbr_glossary(
        "element-dt-days-of-week",
        True,
        is_sorted=True,
        description=(
            "Maps the single-letter day-of-week codes used in dates and"
            " schedules to their weekday names."
        ),
        when_to_use=(
            "Trigger when a date or schedule carries a day-of-week code, or"
            " the user asks what a weekday letter means."
        ),
    )
    register_abbr_glossary(
        "element-dt-watch-day-abbr", False, is_dyn_substitution=True
    )
    register_abbr_glossary(
        "element-dt-watch-week-abbr", False, is_dyn_substitution=True
    )
