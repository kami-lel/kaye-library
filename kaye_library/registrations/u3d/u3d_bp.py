"""
kaye_library.registrations.u3d.u3d_bp.py

register Unity Engine related blueprints
"""

from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint_from_node,
    get_corpus_node,
    replace_meta,
)

from .._common import register_exportable, register_node

__all__ = ("register_u3d_blueprints",)


_U3D_SECTIONS = (
    ("u3d-assets-management", "Assets Management", None),
    (
        "u3d-mb",
        "MonoBehaviour",
        ["style-briefness-style"],
    ),
    ("u3d-so", "Scriptable Object", None),
)


def register_u3d_blueprints():
    """
    register the Unity Engine core profile and its 3 independent sections

    Prerequisite: the Coder blueprints are registered, since ``u3d``
    depends on ``coder-c-sharp``
    """
    coder_node = get_corpus_node("Coder")
    u3d_node = get_corpus_node("Unity Engine")

    # Unity core, own content only
    u3d = register_exportable(
        "u3d",
        replace_meta(
            create_blueprint_from_node(
                u3d_node,
                dependencies=["coder-c-sharp"],
            ),
            display_name="Unity Engine",
        ),
    )
    u3d.blueprint = checkmark_nodes(u3d.blueprint, coder_node["Brace Style"])

    # Unity sections
    for slug, name, dependencies in _U3D_SECTIONS:
        register_node(
            register_exportable,
            slug,
            u3d_node,
            name,
            recursively=True,
            dependencies=dependencies,
        )
