"""
personality_test.py

Unit Tests (using pytest) for: the library's internal ``persona-kaye``
blueprint, which carries the Personality formatting rule and the
Personality Signature section, Kaye's name behind its ``{for Kaye}`` sidecar
"""

import pytest
from kaye_engine.exportable import exportable_registry
from kaye_engine.prompt.blueprint.registry import blueprint_registry
from kaye_engine.prompt.blueprint.render_profile import RenderProfile
from kaye_library.registrations._common import SIDECAR_FOR_KAYE

_NAME = "persona-kaye"


@pytest.fixture(scope="module")
def content():
    return blueprint_registry[_NAME].content()


@pytest.fixture(scope="module")
def kaye_content():
    profile = RenderProfile(conditional_sidecars=(SIDECAR_FOR_KAYE,))
    return blueprint_registry[_NAME].content(profile=profile)


class TestStructure:

    def test_is_internal(_):
        assert not blueprint_registry[_NAME].is_exportable
        assert _NAME not in exportable_registry

    @pytest.mark.parametrize(
        "name",
        [
            "personality-formatting",
            "personality-persona-identity",
            "personality-signature",
        ],
    )
    def test_folds_into_kaye(_, name):
        assert name not in blueprint_registry


class TestContent:

    def test_opens_with_the_formatting_rule(_, content):
        assert content.startswith("# Personality")
        assert "## Kaye" in content

    def test_holds_the_signature(_, content):
        assert "## Personality Signature" in content

    def test_leaves_the_trailer_to_git(_, kaye_content):
        assert "Co-author Trailer" not in kaye_content
        assert "kaye-lel@users.noreply.github.com" not in kaye_content

    def test_kaye_name_hides_without_sidecar(_, content):
        assert "Kaye LeL" not in content

    def test_kaye_name_shows_with_sidecar(_, kaye_content):
        assert "Kaye LeL" in kaye_content
