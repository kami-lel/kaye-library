"""
kaye_library.registrations.agent.agent_bp.py

register Agent Behavior related blueprints
"""

from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
)

from .._common import register_exportable

__all__ = ("register_agent_blueprints",)


def register_agent_blueprints():
    """
    register every Agent Behavior blueprint
    """
    agent_behavior_node = get_corpus_node("Agentic")
    movement_and_suite_node = agent_behavior_node["Movement and Suite"]

    # Movement and Suite
    register_exportable(
        "agent-movement-and-suite",
        replace_meta(
            checkmark_nodes(
                create_blueprint_from_node(movement_and_suite_node),
                movement_and_suite_node["Movement Notation"],
            ),
            display_name="Agent Movement and Suite",
        ),
    )

    # Movement and Suite with Count
    register_exportable(
        "agent-movement-and-suite-with-count",
        replace_meta(
            checkmark_nodes(
                create_blueprint_from_node(
                    movement_and_suite_node["Movement with Count"]
                ),
                movement_and_suite_node,
            ),
            display_name="Agent Movement and Suite with Count",
        ),
    )

    # Halt Each Movement
    register_exportable(
        "halt-each-movement",
        replace_meta(
            create_blueprint_from_node(
                agent_behavior_node["Halt Each Movement"],
                dependencies=["agent-movement-and-suite"],
            ),
            display_name="Halt Each Movement",
        ),
    )

    # Cascade All Movements
    register_exportable(
        "cascade-all-movements",
        replace_meta(
            create_blueprint_from_node(
                agent_behavior_node["Cascade All Movements"],
                dependencies=["agent-movement-and-suite"],
            ),
            display_name="Cascade All Movements",
        ),
    )
