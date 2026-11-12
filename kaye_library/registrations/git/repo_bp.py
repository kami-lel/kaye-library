"""
kaye_library.registrations.git.repo_bp.py

register Repository related blueprints
"""

from kaye_engine.prompt.blueprint import (
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
)

from .._common import register_exportable, register_node, register_prompt

__all__ = ("register_repo_blueprints",)


def _register_changelog_writer():
    """
    register Repository CHANGELOG Writer
    """
    changelog_node = get_corpus_node("Git")[
        "Repository CHANGELOG Writer"
    ]

    bp = create_blueprint_from_node(
        changelog_node,
        is_recursive=True,
        dependencies=[
            "style-briefness-style",
            "proj-version-extended",
            "style-good-writing",
        ],
    )

    register_exportable(
        "repo-changelog-writer",
        replace_meta(bp, display_name="Repository CHANGELOG Writer"),
    )


def register_repo_blueprints():
    """
    register Repository Structure and the Repository README/CHANGELOG/
    CONTEXT Writers, leaving both AGENTS Writers to ``project_bp.py``,
    and the Submit Pull Request prompt


    :raises KeyError: ``style-briefness-style``, ``proj-version-extended``,
            ``ready-land-feature``, or ``git-feature-summary`` is not yet
            registered
    """
    repo_node = get_corpus_node("Git")

    register_node(
        register_exportable,
        "repo-structure",
        repo_node,
        "Repository Structure",
    )

    register_node(
        register_exportable,
        "repo-readme-writer",
        repo_node,
        "Repository README Writer",
        dependencies=["style-briefness-style"],
    )

    register_node(
        register_exportable,
        "repo-context-writer",
        repo_node,
        "Repository CONTEXT Writer",
    )

    _register_changelog_writer()

    # Clean Up Branches
    register_node(
        register_prompt,
        "prune-merged-branches",
        repo_node,
        "Clean Up Branches",
        recursively=True,
    )

    # Submit Pull Request: readies the branch, then words the pull request
    # from the feature branch summary
    register_node(
        register_prompt,
        "submit-pr",
        repo_node,
        "Submit Pull Request",
        recursively=True,
        dependencies=["ready-land-feature", "git-feature-summary"],
    )
