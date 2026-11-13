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

# discover and summary are h3 sections, so they nest under the feature branch
# definition in the corpus
_FEATURE_BRANCH_PATH = ("Git", "feature branch")


def register_branch_blueprints():
    """
    register the feature branch definition and the feature landing and
    version release workflow prompts


    :raises KeyError: ``proj-version-extended``, ``style-briefness-style``,
            or ``style-letter-case-commentary-case`` is not yet registered
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

    # Feature Discover
    register_leaf(
        _register_internal,
        "git-feature-discover",
        _FEATURE_BRANCH_PATH,
        "discover feature branch",
        display_name="Git Feature Discover",
    )

    # Feature Summary
    register_leaf(
        _register_internal,
        "git-feature-summary",
        _FEATURE_BRANCH_PATH,
        "feature branch summary",
        display_name="Git Feature Summary",
        dependencies=[
            "git-feature-discover",
            "style-briefness-style",
            "style-letter-case-commentary-case",
        ],
    )

    # Ready Land Feature
    register_node(
        register_prompt,
        "ready-land-feature",
        git_node,
        "Ready for Feature Landing",
        dependencies=["git-feature-discover"],
    )

    # Ready Release Version
    register_node(
        register_prompt,
        "ready-release-version",
        git_node,
        "Ready for Version Release",
        dependencies=["proj-version-extended"],
    )

    # Land Feature
    register_node(
        register_prompt,
        "land-feature",
        git_node,
        "Perform Feature Landing",
    )

    # Release Version
    register_node(
        register_prompt,
        "release-version",
        git_node,
        "Perform Version Release",
    )
