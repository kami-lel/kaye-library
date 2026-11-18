"""
kaye_library.registrations.git.branch_bp.py

register Git branch related blueprints: the feature, hotfix, and release
branch definitions and
the feature landing and version release workflows, each with its ready and
scrub halves
"""

from kaye_engine.prompt.blueprint import get_corpus_node

from .._common import (
    register_internal,
    register_leaf,
    register_node,
    register_prompt,
)

__all__ = ("register_branch_blueprints",)


# discover and summary are h3 sections, so they nest under the feature branch
# definition in the corpus
_FEATURE_BRANCH_PATH = ("Git", "feature branch")


def register_branch_blueprints():
    """
    register the feature branch definition and the feature landing and
    version release workflow prompts


    :raises KeyError: ``proj-version-extended``, ``proj-version-title``,
            ``style-briefness-style``, or
            ``style-letter-case-commentary-case`` is not yet registered
    """
    git_node = get_corpus_node("Git")

    # Feature Branch
    register_leaf(
        register_internal,
        "git-feature-branch",
        ("Git",),
        "feature branch",
        display_name="Git Feature Branch",
    )

    # Hotfix Branch
    register_leaf(
        register_internal,
        "git-hotfix-branch",
        ("Git",),
        "hotfix branch",
        display_name="Git Hotfix Branch",
    )

    # Release Branch
    register_leaf(
        register_internal,
        "git-release-branch",
        ("Git",),
        "release branch",
        display_name="Git Release Branch",
    )

    # Feature Discover
    register_leaf(
        register_internal,
        "git-feature-discover",
        _FEATURE_BRANCH_PATH,
        "discover feature branch",
        display_name="Git Feature Discover",
    )

    # Feature Summary
    register_leaf(
        register_internal,
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

    # Scrub Landed Feature
    register_node(
        register_prompt,
        "scrub-landed-feature",
        git_node,
        "Scrub After Feature Landing",
        dependencies=["git-feature-branch"],
    )

    # Scrub Released Version
    register_node(
        register_prompt,
        "scrub-released-version",
        git_node,
        "Scrub After Version Release",
        dependencies=["proj-version-title"],
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
