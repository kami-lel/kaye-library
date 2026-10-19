"""
kaye_library.registrations.repo.workflows_bp.py

register invokable Repository workflow prompts
"""

from kaye_engine.prompt.blueprint import get_corpus_node

from .._common import register_node, register_prompt

__all__ = ("register_repo_workflow_blueprints",)


def register_repo_workflow_blueprints():
    """
    register every invokable workflow prompt


    :raises KeyError: a depended-on ``repo-*`` or ``project-*`` blueprint
            is not yet registered
    """
    repo_node = get_corpus_node("Repositories")
    proj_node = get_corpus_node("Projects")

    # Create README
    register_node(
        register_prompt,
        "create-readme",
        repo_node,
        "Create README",
        recursively=True,
        dependencies=["repo-readme-writer", "style-good-writing"],
        llm_invokable=True,
    )

    # Maintain README
    register_node(
        register_prompt,
        "maintain-readme",
        repo_node,
        "Maintain README",
        dependencies=["repo-readme-writer", "style-good-writing"],
        llm_invokable=True,
    )

    # Create CHANGELOG
    register_node(
        register_prompt,
        "create-changelog",
        repo_node,
        "Create CHANGELOG",
        dependencies=["repo-changelog-writer"],
        llm_invokable=True,
    )

    # Maintain CHANGELOG
    register_node(
        register_prompt,
        "maintain-changelog",
        repo_node,
        "Maintain CHANGELOG",
        recursively=True,
        dependencies=["repo-changelog-writer"],
        llm_invokable=True,
    )

    # Condense CHANGELOG
    register_node(
        register_prompt,
        "condense-changelog",
        repo_node,
        "Condense CHANGELOG",
        recursively=True,
        dependencies=["repo-changelog-writer"],
        llm_invokable=True,
    )

    # Create & Maintain Repository AGENTS
    for verb in ("Create", "Maintain"):
        register_node(
            register_prompt,
            "{}-repo-agents".format(verb.lower()),
            proj_node["agents writer"],
            "{} Repository AGENTS".format(verb),
            dependencies=["repo-agents-writer"],
            llm_invokable=True,
        )

    # Condense AGENTS and CONTEXT
    register_node(
        register_prompt,
        "condense-agents-and-context",
        repo_node,
        "Condense AGENTS and CONTEXT",
        dependencies=["repo-agents-writer", "repo-context-writer"],
        llm_invokable=True,
    )

    # Create & Maintain Repository Docs
    for verb in ("Create", "Maintain"):
        register_node(
            register_prompt,
            "{}-repo-docs".format(verb.lower()),
            proj_node["doc writer"],
            "{} Repository Docs".format(verb),
            dependencies=["repo-doc-writer"],
            llm_invokable=True,
        )

    # Initialize Repository
    register_node(
        register_prompt,
        "initialize-repo",
        repo_node,
        "Initialize Repository",
        dependencies=["style-good-writing"],
    )

    # Ready Land Feature
    register_node(
        register_prompt,
        "ready-land-feature",
        repo_node,
        "Prepare for Feature Landing",
    )

    # Ready Release Version
    register_node(
        register_prompt,
        "ready-release-version",
        repo_node,
        "Prepare for Version Release",
        dependencies=["proj-version-extended"],
    )

    # Maintenance Before Compact
    register_node(
        register_prompt,
        "maintenance-before-compact",
        repo_node,
        "Maintenance Before Compact",
        dependencies=["style-good-writing"],
    )

    # todo land feature & release version hold placeholder text

    # Land Feature
    register_node(
        register_prompt,
        "land-feature",
        repo_node,
        "Perform Feature Landing",
    )

    # Release Version
    register_node(
        register_prompt,
        "release-version",
        repo_node,
        "Perform Version Release",
    )
