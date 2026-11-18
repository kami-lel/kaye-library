"""
kaye_library.registrations.coder.coder_pl_bp.py

register per-language Coder blueprints, split out of
``coder_bp.py`` and called by it rather than by the package root
"""

from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint_from_node,
    merge_blueprints,
    replace_meta,
)

from .._common import (
    glossary_blueprint,
    register_exportable,
    register_node,
)

__all__ = ("register_coder_pl_blueprints",)


def _register_with_checkmark(
    slug, container, name, checkmarked_node, *, recursively=False,
    dependencies=None,
):
    """
    register ``name`` from ``container`` as an exportable, with
    ``checkmarked_node`` also checkmarked non-recursively
    """
    bp = checkmark_nodes(
        create_blueprint_from_node(
            container[name],
            is_recursive=recursively,
            dependencies=dependencies or (),
        ),
        checkmarked_node,
    )
    register_exportable(slug, replace_meta(bp, display_name=name))


def register_coder_pl_blueprints(coder_node):
    """
    register every per-language Coder profile


    :param coder_node: the ``Coder`` corpus node
    :type coder_node: BasePromptNode
    """
    # Bash Shell
    _register_with_checkmark(
        "coder-bash-shell",
        coder_node["Bash"],
        "Coder Bash Shell",
        coder_node["Bash"],
    )

    # Bash Script
    register_exportable(
        "coder-bash-script",
        replace_meta(
            checkmark_nodes(
                merge_blueprints(
                    create_blueprint_from_node(
                        coder_node["Bash"]["Coder Bash Script"],
                        is_recursive=True,
                    ),
                    glossary_blueprint("coder-documentation-field-shorthand"),
                ),
                coder_node["Bash"],
            ),
            display_name="Coder Bash Script",
        ),
    )

    # Coder PowerShell
    register_node(
        register_exportable, "coder-powershell", coder_node, "Coder PowerShell"
    )

    # Coder C
    _register_with_checkmark(
        "coder-c", coder_node, "Coder C", coder_node["Brace Style"]
    )

    # Coder C++
    _register_with_checkmark(
        "coder-cpp",
        coder_node,
        "Coder CPP",
        coder_node["Brace Style"],
        dependencies=["coder-c"],
    )

    # Coder Unreal Engine
    _register_with_checkmark(
        "coder-ue",
        coder_node,
        "Coder Unreal Engine",
        coder_node["Brace Style"],
        dependencies=["coder-cpp"],
    )

    # Coder C Sharp
    _register_with_checkmark(
        "coder-c-sharp",
        coder_node,
        "Coder C Sharp",
        coder_node["Brace Style"],
    )

    # Coder GDScript
    register_node(
        register_exportable, "coder-gdscript", coder_node, "Coder GDScript"
    )

    # Coder HTML
    register_node(register_exportable, "coder-html", coder_node, "Coder HTML")

    # Coder JavaScript and TypeScript
    _register_with_checkmark(
        "coder-javascript-and-typescript",
        coder_node,
        "Coder JavaScript and TypeScript",
        coder_node["Brace Style"],
        recursively=True,
    )

    # Python  ------------------------------------------------------------
    # Coder Python
    register_node(register_exportable, "coder-python", coder_node, "Coder Python")

    # Coder Python Docstring
    register_exportable(
        "coder-python-docstring-style",
        replace_meta(
            merge_blueprints(
                create_blueprint_from_node(
                    coder_node["Coder Python"]["Coder Python Docstring Style"],
                    is_recursive=True,
                ),
                glossary_blueprint("coder-documentation-field-shorthand"),
            ),
            display_name="Coder Python Docstring Style",
        ),
    )

    # Coder Python Testing
    register_node(
        register_exportable,
        "coder-python-testing-guidelines",
        coder_node["Coder Python"],
        "Coder Python Testing Guidelines",
    )
