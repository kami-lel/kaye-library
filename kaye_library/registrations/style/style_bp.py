"""
kaye_library.registrations.style.style_bp.py

register Style related blueprints
"""

from kaye_engine.prompt.blueprint import (
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
)

from .._common import (
    register_exportable,
    register_internal,
    register_leaf,
    register_node,
)

__all__ = ("register_style_blueprints",)


# Markdown Format children registered alone, each its own skill
_MARKDOWN_RULES = (
    ("style-markdown-heading", "Markdown Heading Format"),
    ("style-markdown-list", "List Format"),
    ("style-markdown-math", "Math Formatting"),
    ("style-markdown-diagrams", "Diagrams"),
    ("style-markdown-reference-link", "Reference Link Format"),
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
    Writing, Markdown Format, its Heading, List, Math, Diagrams and
    Reference Link rules, Markdown Footnotes,
    Markdown Endnotes, Markdown File Assets, Header Separation (plus its
    Long File and Medium File leaves)

    (Title Case and Commentary Case moved to the Letter Case blueprint,
    see ``register_letter_case_blueprints``)
    """
    style_node = get_corpus_node("Style Guide")

    register_internal(
        "style",
        replace_meta(
            create_blueprint_from_node(style_node, is_recursive=True),
            display_name="Style Guide",
        ),
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

    for slug, name in _MARKDOWN_RULES:
        register_node(
            register_exportable,
            slug,
            style_node["Style Guide Markdown Format"],
            name,
        )

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
        "style-markdown-file-assets",
        style_node["Style Guide Markdown Format"],
        "Markdown File Assets",
        recursively=True,
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
