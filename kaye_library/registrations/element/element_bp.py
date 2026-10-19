"""
kaye_library.registrations.element.element_bp.py

register Element related blueprints
"""

from kaye_engine import register_blueprint
from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
)

from .._common import (
    mark_as_leaf,
    register_exportable,
    register_node,
)

__all__ = ("register_element_blueprints",)


# auxiliaries  #################################################################
def _register_date_time_leaf(slug, leaf_name):
    """
    register a Date and Time Format leaf
    """
    date_time_path = ("Elements", "Date and Time Format")

    bp = checkmark_nodes(create_blueprint(), date_time_path)
    bp = checkmark_nodes(bp, "(element-dt-days-of-week)")
    bp = mark_as_leaf(bp, (*date_time_path, leaf_name))

    register_exportable(slug, replace_meta(bp, display_name=leaf_name))


# Public API  ##################################################################
def register_element_blueprints():
    """
    register the Elements-family blueprints
    """
    date_time = get_corpus_node("Elements")["Date and Time Format"]

    # Year Month Day Format
    _register_date_time_leaf(
        "element-dt-year-month-day-format", "Year Month Day Format"
    )

    # Month Day Format
    _register_date_time_leaf("element-dt-month-day-format", "Month Day Format")

    # Time Format
    register_node(
        register_exportable,
        "element-dt-time-format",
        date_time,
        "Time Format",
    )

    # Watch Day
    register_node(
        register_exportable,
        "element-dt-watch-day",
        date_time,
        "Watch Day",
        dependencies=["element-dt-time-format"],
    )

    # Watch Week
    register_node(
        register_exportable,
        "element-dt-watch-week",
        date_time,
        "Watch Week",
    )

    # Numerical Values with Units
    register_exportable(
        "element-numerical-values-with-units",
        replace_meta(
            create_blueprint_from_node("Numerical Values with Units"),
            display_name="Numerical Values with Units",
        ),
    )

    # Triage Tags
    register_node(
        register_exportable,
        "element-triage-tags",
        get_corpus_node("Elements"),
        "Triage Tags",
        recursively=True,
    )

    # Sort and Group Triage Tag
    register_node(
        register_exportable,
        "sort-and-group-triage-tag",
        get_corpus_node("Elements")["Triage Tags"],
        "Sort and Group Triage Tag",
        recursively=True,
    )

    # International Phonetic Alphabet
    register_node(
        register_exportable,
        "element-international-phonetic-alphabet",
        get_corpus_node("Elements"),
        "International Phonetic Alphabet",
    )

    # Alphabetical Sequence Numbering
    register_node(
        register_exportable,
        "element-alphabetical-sequence-numbering",
        get_corpus_node("Elements"),
        "Alphabetical Sequence Numbering",
    )

    # Alphabetical Sequence Numbering in Chat
    register_node(
        register_blueprint,
        "element-alphabetical-sequence-numbering-in-chat",
        get_corpus_node("Elements")["Alphabetical Sequence Numbering"],
        "Alphabetical Sequence Numbering in Chat",
        dependencies=["element-alphabetical-sequence-numbering"],
        is_exportable=False,
    )
