"""
kaye_library.registrations.style.style_bp.py

register Style related blueprints
"""

from kaye_engine import register_blueprint
from kaye_engine.prompt.blueprint import (
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
)

from .._common import register_exportable, register_leaf, register_node

__all__ = ("register_style_blueprints",)


def _register_markdown_extended():
    """
    register Markdown Format with its Extended child
    """
    register_leaf(
        register_exportable,
        "style-markdown-extended",
        ["Style Guide", "Style Guide Markdown Format"],
        "Extended Markdown Format",
    )


def _register_heading_separation_leaf(slug, leaf_name):
    """
    register a Header Separation leaf with its shared content
    """
    register_leaf(
        register_exportable,
        slug,
        ["Style Guide", "Style Guide Markdown Format", "Header Separation"],
        leaf_name,
    )


def register_style_blueprints():
    """
    register Style Guide and its sub-styles: Briefness Style, Good
    Writing, Markdown Format, Markdown Extended, Header Separation
    (plus its Long File and Medium File leaves)

    (Title Case and Commentary Case moved to the Letter Case blueprint,
    see ``register_letter_case_blueprints``)
    """
    style_node = get_corpus_node("Style Guide")

    register_blueprint(
        "style",
        replace_meta(
            create_blueprint_from_node(style_node, is_recursive=True),
            display_name="Style Guide",
        ),
        is_exportable=False,
    )

    register_exportable(
        "style-briefness-style",
        replace_meta(
            create_blueprint_from_node(
                style_node["Style Guide Briefness Style"]
            ),
            display_name="Style Guide Briefness Style",
        ),
    )

    register_node(
        register_exportable,
        "style-good-writing",
        style_node,
        "Style Guide Good Writing",
    )

    register_node(
        register_exportable,
        "style-markdown",
        style_node,
        "Style Guide Markdown Format",
        is_user_invokable=False,
    )

    _register_markdown_extended()

    register_node(
        register_exportable,
        "style-markdown-footnotes",
        style_node["Style Guide Markdown Format"],
        "Markdown Footnotes",
    )

    register_node(
        register_exportable,
        "style-markdown-endnotes",
        style_node["Style Guide Markdown Format"],
        "Markdown Endnotes",
    )

    register_node(
        register_exportable,
        "style-heading-separation",
        style_node["Style Guide Markdown Format"],
        "Header Separation",
        recursively=True,
    )

    _register_heading_separation_leaf(
        "style-heading-separation-long", "Long File"
    )

    _register_heading_separation_leaf(
        "style-heading-separation-medium", "Medium File"
    )
