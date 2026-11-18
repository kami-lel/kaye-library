"""
personality_test.py

Unit Tests (using pytest) for: the library's internal
``personality-persona-identity`` blueprint, which ships the Persona
Trailer rule and empty identity headings, never a persona's values
"""

import pytest
from kaye_engine.exportable import exportable_registry
from kaye_engine.prompt.blueprint.registry import blueprint_registry

_NAME = "personality-persona-identity"


@pytest.fixture(scope="module")
def content():
    return blueprint_registry[_NAME].content()


class TestStructure:

    def test_is_registered(_):
        assert _NAME in blueprint_registry

    def test_is_internal(_):
        assert not blueprint_registry[_NAME].is_exportable
        assert _NAME not in exportable_registry


class TestContent:

    @pytest.mark.parametrize(
        "heading",
        [
            "## Persona Identity",
            "### Display Name",
            "### GitHub Bot Account Email",
            "### Persona Trailer",
        ],
    )
    def test_holds_heading(_, content, heading):
        assert heading in content

    def test_names_only_a_persona_co_author(_, content):
        assert "Only a [Personality](#personality) may be co-author" in content

    def test_example_trailer_is_generic(_, content):
        assert "Co-authored-by: Example Bot <bot@example.com>" in content

    def test_formatting_rule_leaves_identity_out(_):
        text = blueprint_registry["personality-formatting"].content()

        assert "Persona Identity" not in text
