"""
kaye_library.registrations.git.branch_bp.py

register Git branch related blueprints: the feature branch definition and
the feature landing and version release workflows
"""

import functools

from kaye_engine import register_blueprint
from kaye_engine.prompt.blueprint import get_corpus_node

from .._common import register_leaf, register_node, register_prompt

__all__ = ("register_branch_blueprints",)

_register_internal = functools.partial(register_blueprint, is_exportable=False)


def register_branch_blueprints():
    """
    register the feature branch definition and the feature landing and
    version release workflow prompts


    :raises KeyError: ``proj-version-extended`` is not yet registered
    """
    git_node = get_corpus_node("Git")

    # Feature Branch
    register_leaf(
        _register_internal,
        "git-feature-branch",
        ("Git",),
        "feature branch",
        display_name="Git Feature Branch",
    )

    # Ready Land Feature
    register_node(
        register_prompt,
        "ready-land-feature",
        git_node,
        "Prepare for Feature Landing",
    )

    # Ready Release Version
    register_node(
        register_prompt,
        "ready-release-version",
        git_node,
        "Prepare for Version Release",
        dependencies=["proj-version-extended"],
    )

    # TODO land feature & release version hold placeholder text, so both
    # stay internal (not exportable) until their text is written

    # Land Feature
    register_node(
        _register_internal,
        "land-feature",
        git_node,
        "Perform Feature Landing",
    )

    # Release Version
    register_node(
        _register_internal,
        "release-version",
        git_node,
        "Perform Version Release",
    )
