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
from .coder_u3d_bp import register_coder_u3d_blueprints

__all__ = ("register_coder_pl_blueprints",)


def register_coder_pl_blueprints(coder_node):
    """
    register every per-language Coder profile


    :param coder_node: the ``Coder`` corpus node
    :type coder_node: BasePromptNode
    """
    # Bash Shell
    coder_bash_shell = register_node(
        register_exportable,
        "coder-bash-shell",
        coder_node["Bash"],
        "Coder Bash Shell",
    )
    coder_bash_shell.blueprint = checkmark_nodes(
        coder_bash_shell.blueprint, coder_node["Bash"]
    )

    # Bash Script
    coder_bash_script = register_exportable(
        "coder-bash-script",
        replace_meta(
            merge_blueprints(
                create_blueprint_from_node(
                    coder_node["Bash"]["Coder Bash Script"], is_recursive=True
                ),
                glossary_blueprint("coder-documentation-field-shorthand"),
            ),
            display_name="Coder Bash Script",
        ),
    )
    coder_bash_script.blueprint = checkmark_nodes(
        coder_bash_script.blueprint, coder_node["Bash"]
    )

    # Coder PowerShell
    register_node(
        register_exportable, "coder-powershell", coder_node, "Coder PowerShell"
    )

    # Coder C
    coder_c = register_node(register_exportable, "coder-c", coder_node, "Coder C")
    coder_c.blueprint = checkmark_nodes(
        coder_c.blueprint, coder_node["Brace Style"]
    )

    # Coder C++
    coder_cpp = register_node(
        register_exportable,
        "coder-cpp",
        coder_node,
        "Coder CPP",
        dependencies=["coder-c"],
    )
    coder_cpp.blueprint = checkmark_nodes(
        coder_cpp.blueprint, coder_node["Brace Style"]
    )

    # Coder Unreal Engine
    coder_ue = register_node(
        register_exportable,
        "coder-ue",
        coder_node,
        "Coder Unreal Engine",
        dependencies=["coder-cpp"],
    )
    coder_ue.blueprint = checkmark_nodes(
        coder_ue.blueprint, coder_node["Brace Style"]
    )

    # Coder C Sharp
    coder_csharp = register_node(
        register_exportable, "coder-c-sharp", coder_node, "Coder C Sharp"
    )
    coder_csharp.blueprint = checkmark_nodes(
        coder_csharp.blueprint, coder_node["Brace Style"]
    )

    # Coder Unity
    register_coder_u3d_blueprints(coder_node)

    # Coder GDScript
    register_node(
        register_exportable, "coder-gdscript", coder_node, "Coder GDScript"
    )

    # Coder HTML
    register_node(register_exportable, "coder-html", coder_node, "Coder HTML")

    # Coder JavaScript and TypeScript
    coder_js_ts = register_node(
        register_exportable,
        "coder-javascript-and-typescript",
        coder_node,
        "Coder JavaScript and TypeScript",
        recursively=True,
    )
    coder_js_ts.blueprint = checkmark_nodes(
        coder_js_ts.blueprint, coder_node["Brace Style"]
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
