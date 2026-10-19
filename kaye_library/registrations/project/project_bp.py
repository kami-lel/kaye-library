"""
kaye_library.registrations.project.project_bp.py

register Project related blueprints
"""

import functools

from kaye_engine import register_blueprint
from kaye_engine.prompt.blueprint import get_corpus_node

from .._common import register_exportable, register_leaf, register_node

__all__ = ("register_project_blueprints",)

_register_internal = functools.partial(register_blueprint, is_exportable=False)


def _register_semantic_version_extended():
    """
    register Semantic Version Extended with its parent
    """
    register_leaf(
        register_exportable,
        "proj-version-extended",
        ["Projects", "Project Semantic Version"],
        "Semantic Version Extended",
    )


def _register_agents_writer(slug, leaf_name):
    """
    register one AGENTS Writer version, ``leaf_name``
    """
    register_node(
        register_exportable,
        slug,
        get_corpus_node("Projects")["agents writer"],
        leaf_name,
        recursively=True,
        dependencies=["proj-agents"],
    )


def _register_doc_writer(slug, leaf_name):
    """
    register one Doc Writer version, ``leaf_name``
    """
    register_node(
        register_exportable,
        slug,
        get_corpus_node("Projects")["doc writer"],
        leaf_name,
        recursively=True,
        dependencies=["proj-docs", "style-good-writing"],
    )


def _register_workflow(slug, container_name, name, writer_slug):
    """
    register the workflow ``name`` from ``container_name``, depending on
    its writer ``writer_slug``
    """
    register_node(
        register_exportable,
        slug,
        get_corpus_node("Projects")[container_name],
        name,
        dependencies=[writer_slug],
    )


def register_project_blueprints():
    """
    register Project Semantic Version, its Semantic Version Extended
    sibling, the internal ``proj-agents``, ``proj-docs`` and
    ``proj-context-engineering`` blueprints, the Project and Repository
    AGENTS and Doc Writers depending on their internal base, and the
    Create and Maintain Project workflows depending on their writer
    """
    proj_node = get_corpus_node("Projects")

    register_node(
        register_exportable,
        "proj-version",
        proj_node,
        "Project Semantic Version",
        is_user_invokable=False,
        llm_invokable=False,
    )

    _register_semantic_version_extended()

    register_node(
        _register_internal,
        "proj-agents",
        proj_node,
        "agents writer",
    )

    register_node(
        _register_internal,
        "proj-docs",
        proj_node,
        "doc writer",
    )

    register_node(
        _register_internal,
        "proj-context-engineering",
        proj_node,
        "Project Context Engineering",
        recursively=True,
    )

    _register_agents_writer("proj-agents-writer", "Project AGENTS Writer")
    _register_agents_writer("repo-agents-writer", "Repository AGENTS Writer")

    _register_doc_writer("proj-doc-writer", "Project Doc Writer")
    _register_doc_writer("repo-doc-writer", "Repository Doc Writer")

    register_node(
        register_exportable,
        "equip-proj-for-agent",
        proj_node,
        "Equip Project for Agent",
        dependencies=["proj-context-engineering"],
    )

    for verb in ("Create", "Maintain"):
        _register_workflow(
            "{}-project-agents".format(verb.lower()),
            "agents writer",
            "{} Project AGENTS".format(verb),
            "proj-agents-writer",
        )
        _register_workflow(
            "{}-project-docs".format(verb.lower()),
            "doc writer",
            "{} Project Docs".format(verb),
            "proj-doc-writer",
        )
