"""
kaye_library.registrations.coder.coder_u3d_bp.py

register the Coder Unity Engine (u3d) blueprints, split out of
``coder_pl_bp.py`` and called by it rather than by the package root
"""

from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint_from_node,
    replace_meta,
)

from .._common import register_exportable, register_node

__all__ = ("register_coder_u3d_blueprints",)


_U3D_SECTIONS = (
    ("coder-u3d-assets-management", "Assets Management", None),
    (
        "coder-u3d-mb",
        "MonoBehaviour",
        ["style-briefness-style"],
    ),
    ("coder-u3d-so", "Scriptable Object", None),
)


def register_coder_u3d_blueprints(coder_node):
    """
    register the Unity Engine core profile and its 3 independent sections
    """
    u3d_node = coder_node["Coder Unity Engine"]

    # Coder Unity core, own content only
    coder_u3d = register_exportable(
        "coder-u3d",
        replace_meta(
            create_blueprint_from_node(
                u3d_node,
                dependencies=["coder-c-sharp"],
            ),
            display_name="Coder Unity Engine",
        ),
    )
    coder_u3d.blueprint = checkmark_nodes(
        coder_u3d.blueprint, coder_node["Brace Style"]
    )

    # Coder Unity sections
    for slug, name, dependencies in _U3D_SECTIONS:
        register_node(
            register_exportable,
            slug,
            u3d_node,
            name,
            recursively=True,
            dependencies=dependencies,
        )
