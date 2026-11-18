"""
personality_test.py

Unit Tests (using pytest) for: the library's internal
``personality-persona-identity`` blueprint, which ships the Persona
Co-author Trailer rule and Kaye's values, each behind its ``{for Kaye}`` sidecar
"""

import pytest
from kaye_engine.exportable import exportable_registry
from kaye_engine.prompt.blueprint.registry import blueprint_registry
from kaye_engine.prompt.blueprint.render_profile import RenderProfile
from kaye_library.registrations._common import SIDECAR_FOR_KAYE

_NAME = "personality-persona-identity"


@pytest.fixture(scope="module")
def content():
    return blueprint_registry[_NAME].content()


@pytest.fixture(scope="module")
def kaye_content():
    profile = RenderProfile(conditional_sidecars=(SIDECAR_FOR_KAYE,))
    return blueprint_registry[_NAME].content(profile=profile)


class TestStructure:

    def test_is_registered(_):
        assert _NAME in blueprint_registry

    def test_is_internal(_):
        assert not blueprint_registry[_NAME].is_exportable
        assert _NAME not in exportable_registry


class TestContent:

    @pytest.mark.parametrize(
        "heading",
        ["## Display Name", "## Persona Co-author Trailer"],
    )
    def test_holds_heading(_, content, heading):
        assert heading in content

    def test_signs_only_changes_the_persona_wrote(_, content):
        assert "When you wrote the changes a commit records" in content
        assert "end it with no trailer" in content

    def test_avoids_a_generic_ai_trailer(_):
        # every surface renders {avoid}; a bare render needs it named
        profile = RenderProfile(conditional_sidecars=("avoid",))
        text = blueprint_registry[_NAME].content(profile=profile)

        assert "A generic AI trailer naming a tool or model" in text

    def test_kaye_trailer_is_whole(_, kaye_content):
        assert (
            "Co-authored-by: Kaye LeL"
            " <341862645+kaye-lel@users.noreply.github.com>"
        ) in kaye_content

    @pytest.mark.parametrize(
        "value",
        ["Kaye LeL", "341862645+kaye-lel@users.noreply.github.com"],
    )
    def test_kaye_value_hides_without_sidecar(_, content, value):
        assert value not in content

    @pytest.mark.parametrize(
        "value",
        ["Kaye LeL", "341862645+kaye-lel@users.noreply.github.com"],
    )
    def test_kaye_value_shows_with_sidecar(_, kaye_content, value):
        assert value in kaye_content



class TestPersonaKaye:

    def test_formatting_folds_into_kaye(_):
        assert "personality-formatting" not in blueprint_registry

    def test_opens_with_the_formatting_rule(_):
        text = blueprint_registry["persona-kaye"].content()

        assert text.startswith("# Personality")
        assert "## Kaye" in text

    def test_leaves_identity_out(_):
        text = blueprint_registry["persona-kaye"].content()

        assert "Display Name" not in text
        assert "Persona Co-author Trailer" not in text
