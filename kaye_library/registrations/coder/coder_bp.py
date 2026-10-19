"""
kaye_library.registrations.coder.coder_bp.py

register Coder related blueprints
"""

from kaye_engine import register_blueprint
from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
    create_blueprint_from_node,
    get_corpus_node,
    merge_blueprints,
    replace_meta,
)

from .._common import (
    glossary_blueprint,
    register_exportable,
    register_node,
    register_prompt,
)
from .coder_pl_bp import register_coder_pl_blueprints

__all__ = ("register_coder_blueprints",)


def register_coder_blueprints():
    """
    register the persona-free Coder: the internal ``coder-core``, the
    ``coder`` skill over it, its workflows, and every per-language coder
    profile

    a package may take ``coder`` over with ``override_exportable``, adding
    the conversation rules and persona it wants around ``coder-core``


    :raises KeyError: a depended-on blueprint is not yet registered
    """
    coder_node = get_corpus_node("Coder")

    # Coder Core
    # the Coder rules and glossaries, with no conversation rules
    register_blueprint(
        "coder-core",
        replace_meta(
            merge_blueprints(
                create_blueprint_from_node(
                    coder_node,
                    dependencies=[
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
            display_name="Coder Core",
        ),
        is_exportable=False,
    )

    # Coder
    # the Coder rules as a skill, naming no persona; a package may take it
    # over with its own conversation rules around coder-core
    register_exportable(
        "coder",
        replace_meta(
            create_blueprint(dependencies=["coder-core"]),
            display_name="Coder",
            description_node=("Coder", "{description}"),
            when_to_use_node=("Coder", "{when_to_use}"),
        ),
    )

    # Plan for Suite
    plan_for_suite_node = coder_node["Plan for Suite"]
    plan_for_suite_execution_node = plan_for_suite_node[
        "Plan for Suite: Bar 3: Execution"
    ]

    plan_for_suite = register_prompt(
        "plan-for-suite",
        replace_meta(
            create_blueprint_from_node(
                plan_for_suite_node,
                is_recursive=True,
                dependencies=["agent-movement-and-suite"],
            ),
            display_name="Plan for Suite",
        ),
    )
    plan_for_suite.blueprint = checkmark_nodes(
        plan_for_suite.blueprint, plan_for_suite_execution_node
    )

    # Plan for Suite Execution
    register_exportable(
        "plan-for-suite-execution",
        replace_meta(
            create_blueprint_from_node(
                plan_for_suite_execution_node,
                is_recursive=True,
                dependencies=["agent-movement-and-suite"],
            ),
            display_name="Plan for Suite Execution",
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
    cb_in_code_comment = register_exportable(
        "coder-comment-banner-in-code-comment",
        replace_meta(
            create_blueprint_from_node(cb_node["CB in Code Comment"]),
            display_name="Code Comment Banner in Code Comment",
        ),
    )
    cb_in_code_comment.blueprint = checkmark_nodes(
        cb_in_code_comment.blueprint, cb_node
    )

    # Code Comment Banner in Print Out
    cb_in_print_out = register_exportable(
        "coder-comment-banner-in-print-out",
        replace_meta(
            create_blueprint_from_node(cb_node["CB in Print Out"]),
            display_name="Code Comment Banner in Print Out",
        ),
    )
    cb_in_print_out.blueprint = checkmark_nodes(
        cb_in_print_out.blueprint, cb_node
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
