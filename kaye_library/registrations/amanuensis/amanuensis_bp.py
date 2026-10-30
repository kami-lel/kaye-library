"""
kaye_library.registrations.amanuensis.amanuensis_bp.py

register Amanuensis related blueprints
"""

from kaye_engine.prompt.blueprint import (
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
)

from .._common import (
    register_children,
    register_exportable,
    register_leaf,
    register_node,
)

__all__ = ("register_amanuensis_blueprints",)


def _register_chicago_citation_leaf(slug, leaf_name, dependencies=None):
    """
    register a Chicago Citation leaf with its shared content
    """
    register_leaf(
        register_exportable,
        slug,
        ["Amanuensis", "Chicago Citation"],
        leaf_name,
        dependencies=dependencies,
    )


def _register_dispositor_family(amanuensis_node):
    """
    register Dispositor and its child blueprints
    """
    dispositor_node = amanuensis_node["Dispositor"]

    register_exportable(
        "dispositor",
        replace_meta(
            create_blueprint_from_node(
                dispositor_node,
                dependencies=["style-heading-separation", "style-good-writing"],
            ),
            display_name="Dispositor",
        ),
        llm_invokable=False,
    )

    register_children(
        register_exportable,
        "dispositor",
        dispositor_node,
        (
            ("scholiast", "Scholiast"),
            ("minutes-clerk", "Minutes Clerk"),
        ),
        llm_invokable=False,
    )

    register_node(
        register_exportable,
        "config-writer",
        dispositor_node,
        "Config Writer",
        recursively=True,
        dependencies=["dispositor", "style-briefness-style"],
        llm_invokable=False,
    )

    register_node(
        register_exportable,
        "keybinding-writer",
        dispositor_node["Config Writer"],
        "Keybinding Writer",
        recursively=True,
        dependencies=["config-writer"],
        llm_invokable=False,
    )


def register_amanuensis_blueprints():
    """
    register Chicago Note, Chicago Bibliography, Bibliographer, assemble
    bibliography, Dispositor (with its Scholiast, Config Writer,
    Keybinding Writer, and Minutes Clerk children), Redactor


    :raises KeyError: ``style-heading-separation``,
            ``style-good-writing``, or ``style-briefness-style`` is not
            yet registered
    """
    amanuensis_node = get_corpus_node("Amanuensis")

    _register_chicago_citation_leaf(
        "amanuensis-chicago-note",
        "Chicago Note",
        dependencies=["style-markdown-footnotes"],
    )

    _register_chicago_citation_leaf(
        "amanuensis-chicago-bibliography", "Chicago Bibliography"
    )

    bibliographer = register_node(
        register_exportable,
        "bibliographer",
        amanuensis_node,
        "Bibliographer",
        recursively=True,
        dependencies=["style-markdown-footnotes"],
        llm_invokable=False,
    )
    bibliographer.blueprint = replace_meta(
        bibliographer.blueprint,
        description=(
            "coordinates citation and bibliography assembly across the other"
            " Amanuensis skills"
        ),
    )

    register_node(
        register_exportable,
        "assemble-bibliography",
        amanuensis_node,
        "assemble bibliography",
        recursively=True,
        dependencies=["amanuensis-chicago-bibliography"],
        llm_invokable=False,
    )

    _register_dispositor_family(amanuensis_node)

    register_node(
        register_exportable,
        "redactor",
        amanuensis_node,
        "Redactor",
        recursively=True,
        llm_invokable=False,
    )
