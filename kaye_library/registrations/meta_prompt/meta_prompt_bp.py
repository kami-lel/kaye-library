"""
kaye_library.registrations.meta_prompt.meta_prompt_bp.py

register Meta Prompt related blueprints
"""

from kaye_engine.prompt.blueprint import get_corpus_node

from .._common import register_internal, register_exportable, register_node

__all__ = ("register_meta_prompt_blueprints",)


def register_meta_prompt_blueprints():
    """
    register every Meta Prompt blueprint
    """
    meta_prompt_node = get_corpus_node("Meta Prompt")

    register_node(
        register_internal, "meta-prompt", get_corpus_node(), "Meta Prompt"
    )

    register_node(
        register_exportable,
        "write-llm-prompt",
        meta_prompt_node,
        "Write Large Language Model Prompt",
        recursively=True,
        dependencies=["meta-prompt"],
        llm_invokable=False,
    )

    write_for_skill_node = meta_prompt_node["Write for Skill"]

    register_node(
        register_internal,
        "write-for-skill",
        meta_prompt_node,
        "Write for Skill",
        dependencies=["meta-prompt"],
    )

    register_node(
        register_exportable,
        "write-skill-description",
        write_for_skill_node,
        "Write Skill Description",
        dependencies=["write-for-skill"],
        llm_invokable=False,
    )

    register_node(
        register_exportable,
        "write-skill-when-to-use",
        write_for_skill_node,
        "Write Skill When to Use",
        dependencies=["write-for-skill"],
        llm_invokable=False,
    )

    register_node(
        register_exportable,
        "write-skill-description-and-when-to-use",
        write_for_skill_node,
        "Write Skill Description and When to Use",
        dependencies=[
            "write-skill-description",
            "write-skill-when-to-use",
        ],
        llm_invokable=False,
    )
