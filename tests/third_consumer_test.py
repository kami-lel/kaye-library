"""
third_consumer_test.py

Unit Tests (using pytest) for: a throwaway third consumer building on the
library steps -- its corpus sources register under the root and under
nodes, in one process, before the tree loads
"""

import subprocess
import sys
import textwrap

_SCRIPT = textwrap.dedent(
    """
    import kaye_library
    from kaye_engine import (
        load_corpus_tree,
        populate_abbr_data_with_json_file,
        register_blueprint,
        register_consumer,
        register_corpus_under_node,
    )
    from kaye_engine.exportable import exportable_registry
    from kaye_engine.prompt import get_corpus_tree
    from kaye_engine.prompt.blueprint import create_blueprint_from_node
    from kaye_engine.cli.claude.plugin_marketplace_name import (
        get_plugin_consumers,
    )

    kaye_library.register_kaye_library_consumer()
    register_consumer("Third Package", "third-pkg", "3.0.0")
    kaye_library.register_kaye_library_abbr_glossaries()
    populate_abbr_data_with_json_file(
        kaye_library.get_kaye_library_abbrs_json_path()
    )
    kaye_library.register_kaye_library_dynamic_substitutions()
    kaye_library.register_kaye_library_corpus()

    # the third consumer: under the root, under its own node, and under a
    # node of the library
    register_corpus_under_node((), "# Fixture Root\\nroot text\\n")
    register_corpus_under_node(
        ("Fixture Root",), "## Fixture Child\\nchild text\\n"
    )
    register_corpus_under_node(("Coder",), "## Fixture Language\\nlang\\n")
    load_corpus_tree()

    kaye_library.register_kaye_library_blueprints()
    tree = get_corpus_tree()
    register_blueprint(
        "third-skill",
        create_blueprint_from_node(tree["Fixture Root"], is_recursive=True),
        consumer="third-pkg",
    )

    print("root:", "Fixture Root" in [c.name for c in tree.children])
    print(
        "child:",
        [c.name for c in tree["Fixture Root"].children],
    )
    print("under library:", "Fixture Language" in [
        c.name for c in tree["Coder"].children
    ])
    print("owner:", exportable_registry["third-skill"].consumer)
    print(
        "plugins:",
        sorted(c.canonical_name for c in get_plugin_consumers()),
    )
    print("content:", exportable_registry["third-skill"].content().count("text"))
    """
)


def test_third_consumer_registers_under_root_and_nodes():
    result = subprocess.run(
        [sys.executable, "-c", _SCRIPT],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "root: True" in result.stdout
    assert "child: ['Fixture Child']" in result.stdout
    assert "under library: True" in result.stdout
    assert "owner: third-pkg" in result.stdout
    assert "plugins: ['kaye-library', 'third-pkg']" in result.stdout
    assert "content: 2" in result.stdout
