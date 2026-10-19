"""
general_test.py

Unit Tests (using pytest) for: the general blueprint ``rapid`` and the
``(today)`` dynamic node, which render in the library alone, and the
library text, which splices no ``(decode-only-abbr)``
"""

import pathlib

import kaye_library
from kaye_engine.exportable import exportable_registry
from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
    render_prompt,
)
from kaye_engine.prompt.blueprint.registry import blueprint_registry
from kaye_engine.prompt.blueprint.render_profile import RenderProfile

_PACKAGE_DIR = pathlib.Path(kaye_library.__file__).resolve().parent


class TestRapid:

    def test_registered_not_exportable(_):
        assert "rapid" in blueprint_registry
        assert "rapid" not in exportable_registry

    def test_renders_markdown_rules(_):
        content = blueprint_registry["rapid"].content()

        assert "Style Guide Markdown Format" in content
        assert "Use **double asterisks**" in content

    def test_describes_itself(_):
        meta = blueprint_registry["rapid"].blueprint.meta

        assert meta.description.startswith("quick, mechanical")


class TestToday:

    def test_renders_current_date(_):
        bp = checkmark_nodes(create_blueprint(), "(today)")

        content = render_prompt(bp, profile=RenderProfile(sparseness=0))

        assert "Current" in content
        assert "Date" in content


class TestDecodeOnlyAbbr:

    def test_no_library_text_splices_it(_):
        for path in _PACKAGE_DIR.rglob("*.md"):
            assert "decode-only-abbr" not in path.read_text(encoding="utf-8")

    def test_no_library_blueprint_selects_it(_):
        for entry in blueprint_registry.values():
            nodes = entry.blueprint.nodes | entry.blueprint.subtrees
            assert ("(decode-only-abbr)",) not in nodes, entry.canonical_name
