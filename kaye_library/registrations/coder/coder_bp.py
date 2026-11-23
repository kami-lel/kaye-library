"""
kaye_library.registrations.coder.coder_bp.py

register Coder related blueprints
"""

from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
    create_blueprint_from_node,
    get_corpus_node,
    merge_blueprints,
    replace_meta,
)

from kaye_engine.prompt.blueprint.render_profile import RenderProfile

from .._common import (
    SIDECAR_FOR_KAYE,
    SIDECAR_IN_CHAT,
    glossary_blueprint,
    register_exportable,
    register_node,
    register_prompt,
)
from .coder_pl_bp import register_coder_pl_blueprints

__all__ = ("register_coder_blueprints",)


def register_coder_blueprints():
    """
    register the Coder: the ``coder`` skill, Kaye Peer Coder, its
    workflows, and every per-language coder profile

    ``coder`` is ``chat`` and ``persona`` plus the Coder rules, both named
    as string dependencies, so a package replacing either in place reaches
    ``coder`` too; never ``chat-kaye``, so what a package adds to
    ``chat-kaye`` alone stays out of ``coder``; the per-language profiles
    stay persona-free, invoking ``coder``


    :raises KeyError: a depended-on blueprint is not yet registered
    """
    coder_node = get_corpus_node("Coder")

    # Coder
    # Kaye Peer Coder: the conversation rules and persona, plus the Coder
    # rules and glossaries
    register_exportable(
        "coder",
        replace_meta(
            merge_blueprints(
                create_blueprint_from_node(
                    coder_node,
                    dependencies=[
                        "chat",
                        "persona",
                        "element-triage-tags",
                        "repo-structure",
                        "proj-context-engineering",
                        "style-briefness-style",
                        "style-letter-case-snake-case",
                        "style-letter-case-all-caps",
                    ],
                ),
                glossary_blueprint("coder-abbr", "coder-identifier-shorthand"),
            ),
            display_name="Kaye Peer Coder",
            description_node=("Coder", "{description}"),
            when_to_use_node=("Coder", "{when_to_use}"),
        ),
        render_profile=RenderProfile(
            conditional_sidecars=(SIDECAR_FOR_KAYE, SIDECAR_IN_CHAT)
        ),
        always_apply=True,
    )

    # Plan for Suite
    plan_for_suite_node = coder_node["Plan for Suite"]
    plan_for_suite_execution_node = plan_for_suite_node[
        "Plan for Suite: Bar 3: Execution"
    ]
    plan_for_suite_rework_node = plan_for_suite_node["Plan for Suite: Rework"]

    plan_for_suite_bp = checkmark_nodes(
        checkmark_nodes(
            create_blueprint_from_node(
                plan_for_suite_node,
                is_recursive=True,
                dependencies=[
                    "agent-movement-and-suite",
                    "agent-files-and-folders",
                ],
            ),
            plan_for_suite_execution_node,
        ),
        plan_for_suite_rework_node,
    )
    register_prompt(
        "plan-for-suite",
        replace_meta(plan_for_suite_bp, display_name="Plan for Suite"),
    )

    # Execute Plan for Suite
    register_exportable(
        "execute-plan-for-suite",
        replace_meta(
            create_blueprint_from_node(
                plan_for_suite_execution_node,
                is_recursive=True,
                dependencies=["agent-movement-and-suite"],
            ),
            display_name="Execute Plan for Suite",
        ),
    )

    # Rework Plan for Suite
    register_exportable(
        "rework-plan-for-suite",
        replace_meta(
            create_blueprint_from_node(
                plan_for_suite_rework_node,
                is_recursive=True,
                dependencies=["agent-movement-and-suite"],
            ),
            display_name="Rework Plan for Suite",
        ),
    )

    # Sync Unit Test
    # pylint: disable-next=redundant-keyword-arg
    register_prompt(
        "sync-unit-test",
        replace_meta(
            create_blueprint_from_node(
                coder_node["Sync Unit Test"],
                is_recursive=True,
                dependencies=[
                    "agent-movement-and-suite-with-count",
                    "element-triage-tags",
                ],
            ),
            display_name="Sync Unit Test",
        ),
        llm_invokable=True,
    )

    # Review Gaps
    register_node(
        register_prompt,
        "review-gaps",
        coder_node,
        "Gap Review",
        recursively=True,
        dependencies=["element-triage-tags"],
    )

    # Comment Banner  --------------------------------------------------------
    cb_node = coder_node["Comment Banner"]

    # Code Comment Banner in Code Comment
    register_exportable(
        "coder-comment-banner-in-code-comment",
        replace_meta(
            checkmark_nodes(
                create_blueprint_from_node(cb_node["CB in Code Comment"]),
                cb_node,
            ),
            display_name="Code Comment Banner in Code Comment",
        ),
    )

    # Code Comment Banner in Print Out
    register_exportable(
        "coder-comment-banner-in-print-out",
        replace_meta(
            checkmark_nodes(
                create_blueprint_from_node(cb_node["CB in Print Out"]),
                cb_node,
            ),
            display_name="Code Comment Banner in Print Out",
        ),
    )

    # Code Command Usage Message
    register_exportable(
        "coder-command-usage-message",
        replace_meta(
            create_blueprint_from_node(
                coder_node["Command Usage Message"],
                is_recursive=True,
                dependencies=["style-letter-case-all-caps"],
            ),
            display_name="Code Command Usage Message",
        ),
    )

    register_coder_pl_blueprints(coder_node)
