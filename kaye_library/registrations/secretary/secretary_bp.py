"""
kaye_library.registrations.secretary.secretary_bp.py

register Secretary related blueprints
"""

import functools

from kaye_engine import register_blueprint
from kaye_engine.prompt.sidecar_node import get_sidecar_name
from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
    uncheckmark_nodes,
)

from .._common import (
    mark_as_leaf,
    register_exportable,
    register_leaf,
    walk_and_checkmark,
)

__all__ = ("register_secretary_blueprints",)

# internal, not exportable: reused only as a dependency by other
# Secretary blueprints, never surfaced on its own
_register_internal = functools.partial(register_blueprint, is_exportable=False)


def _register_node_blueprint(
    slug, name, node_name, recursively=False, dependencies=()
):
    """
    register a blueprint from one corpus node
    """
    bp = create_blueprint_from_node(
        node_name,
        is_recursive=recursively,
        dependencies=list(dependencies),
    )

    register_exportable(
        slug,
        replace_meta(bp, display_name=name),
        llm_invokable=False,
    )


# the two Scan Event Radar variants differ in this node alone
_GATHER_OF_DAY = "Bar 1: Gather event for today"
_GATHER_OF_WEEK = "Bar 1: Gather event of week"


def _register_scan_event_radar(slug, name, dropped_gather_node):
    """
    register one Scan Event Radar variant
    """
    bp = create_blueprint_from_node(
        "scan event radar",
        is_recursive=True,
        dependencies=[
            "secretary-event-brief-format",
            "agent-unreachable-task-workaround",
        ],
    )
    try:
        bp = uncheckmark_nodes(bp, dropped_gather_node)
    except ValueError:
        # a gather Bar a consumer supplies is absent when the library
        # runs alone, so there is nothing to drop
        pass

    register_exportable(
        slug,
        replace_meta(bp, display_name=name),
        llm_invokable=False,
    )


def _register_manage_calendar_leaf(slug, name, leaf_name):
    """
    register a Calendar Management leaf with its parent
    """
    register_leaf(
        register_exportable,
        slug,
        ["Secretary", "calendar management"],
        leaf_name,
        display_name=name,
        llm_invokable=False,
    )


def _register_manage_gtd_leaf(slug, name, leaf_name):
    """
    register a GTD Management leaf with its parent
    """
    register_leaf(
        register_exportable,
        slug,
        ["Secretary", "getting-things-done management"],
        leaf_name,
        display_name=name,
        llm_invokable=False,
    )


_DATE_TIME_DEPENDENCIES = (
    "element-dt-month-day-format",
    "element-dt-time-format",
)

_REPORT_INFO_FIELD_NAMES = (
    (
        "secretary-report-info-field-date-time",
        "Date Time Field",
        _DATE_TIME_DEPENDENCIES,
    ),
    (
        "secretary-report-info-field-deadline",
        "Deadline Field",
        _DATE_TIME_DEPENDENCIES,
    ),
    ("secretary-report-info-field-location", "Location Field", ()),
    ("secretary-report-info-field-link", "Link Field", ()),
    ("secretary-report-info-field-ticket", "Ticket Field", ()),
    ("secretary-report-info-field-source", "Source Field", ()),
)

# the fields an Event Brief renders: date/time, location, link, ticket
# (no Deadline Field)
_EVENT_BRIEF_FIELD_SLUGS = (
    "secretary-report-info-field-date-time",
    "secretary-report-info-field-location",
    "secretary-report-info-field-link",
    "secretary-report-info-field-ticket",
)


def _register_report_info_field_leaf(slug, leaf_name, dependencies=()):
    """
    register an internal Common Report Info Field leaf
    """
    bp = create_blueprint(dependencies=list(dependencies))
    bp, common_field_path = walk_and_checkmark(
        bp, ["Secretary", "Common Report Format", "Common Report Info Field"]
    )
    bp = mark_as_leaf(bp, (*common_field_path, leaf_name))

    _register_internal(slug, replace_meta(bp, display_name=leaf_name))


_DAILY_RECAP_LEAF_NAMES = ("recap yesterday", "recap today")


def _register_daily_recap_leaf(slug, name, leaf_name):
    """
    register a Daily Recap leaf with its parent
    """
    bp = create_blueprint(
        dependencies=[
            "style-briefness-style",
            "element-dt-watch-day",
        ],
    )
    bp, daily_recap_path = walk_and_checkmark(bp, ["Secretary", "daily recap"])
    daily_recap = get_corpus_node(*daily_recap_path)
    for child in daily_recap.children:
        if child.name not in _DAILY_RECAP_LEAF_NAMES:
            # a sidecar is only ever selected by name, never via a subtree
            bp = checkmark_nodes(
                bp, child, is_recursive=get_sidecar_name(child) is None
            )

    bp = mark_as_leaf(bp, (*daily_recap_path, leaf_name))

    register_exportable(
        slug,
        replace_meta(bp, display_name=name),
        llm_invokable=False,
    )


def register_secretary_blueprints():
    """
    register every Secretary blueprint


    :raises KeyError: ``style-briefness-style`` is not yet registered
    """
    _register_node_blueprint("draft-email", "Draft Email", "draft email")

    for slug, leaf_name, dependencies in _REPORT_INFO_FIELD_NAMES:
        _register_report_info_field_leaf(slug, leaf_name, dependencies)

    _register_node_blueprint(
        "secretary-event-brief-format",
        "Event Brief Format",
        "event brief format",
        recursively=True,
        dependencies=["style-briefness-style", *_EVENT_BRIEF_FIELD_SLUGS],
    )

    _register_node_blueprint(
        "sweep-email-inbox",
        "Sweep Email Inbox",
        "sweep email inbox",
        dependencies=[
            "secretary-report-info-field-deadline",
            "secretary-report-info-field-link",
            "secretary-report-info-field-source",
        ],
    )

    _register_scan_event_radar(
        "scan-event-radar-daily", "Scan Event Radar Daily", _GATHER_OF_WEEK
    )

    _register_scan_event_radar(
        "scan-event-radar-weekly", "Scan Event Radar Weekly", _GATHER_OF_DAY
    )

    _register_manage_calendar_leaf(
        "push-event-to-calendar",
        "Push Event to Calendar",
        "Push Event to Calendar",
    )

    _register_manage_calendar_leaf(
        "pull-event-from-calendar",
        "Pull Event from Calendar",
        "Pull Event from Calendar",
    )

    _register_manage_gtd_leaf(
        "push-task-to-gtd", "Push Task to GTD", "Push Task to GTD"
    )

    _register_manage_gtd_leaf(
        "pull-task-from-gtd", "Pull Task from GTD", "Pull Task from GTD"
    )

    _register_daily_recap_leaf(
        "recap-yesterday",
        "Recap Yesterday",
        "recap yesterday",
    )

    _register_daily_recap_leaf(
        "recap-today",
        "Recap Today",
        "recap today",
    )
