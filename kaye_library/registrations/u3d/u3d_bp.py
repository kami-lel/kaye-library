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


# (slug, parent node name or None for the root, node name, dependencies)
_U3D_SECTIONS = (
    ("u3d-naming", None, "Unity Naming", None),
    ("u3d-common-type-and-suffix", None, "Common Type and Suffix", None),
    ("u3d-if", "Unity Coding", "Inspector Field", None),
    ("u3d-assets-management", None, "Assets Management", None),
    (
        "u3d-mb",
        "Unity Coding",
        "MonoBehaviour",
        ["style-briefness-style"],
    ),
    ("u3d-so", "Unity Coding", "Scriptable Object", None),
    ("u3d-pfb", None, "Prefab Usage", None),
    ("u3d-owner-driven-activation", None, "Owner-Driven Activation", None),
    ("u3d-game-tuning", None, "Game Tuning", None),
)


def register_u3d_blueprints():
    """
    register the Unity Engine core profile, its coding profile and its
    independent sections

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

    # Unity coding, own content only; the
    # Inspector Field, MonoBehaviour & Scriptable Object children are skills
    coding_node = u3d_node["Unity Coding"]
    register_exportable(
        "u3d-coding",
        replace_meta(
            create_blueprint_from_node(
                coding_node,
                dependencies=["coder-c-sharp"],
            ),
            display_name="Unity Coding",
        ),
    )

    # Unity sections
    for slug, parent, name, dependencies in _U3D_SECTIONS:
        register_node(
            register_exportable,
            slug,
            u3d_node if parent is None else u3d_node[parent],
            name,
            recursively=True,
            dependencies=dependencies,
        )
