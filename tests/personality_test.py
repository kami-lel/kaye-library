"""
personality_test.py

Unit Tests (using pytest) for: the library's internal, persona-free
``persona`` blueprint, which takes every persona kind node whole and
renders only the persona the entry's profile turns on, its ``{in chat}``
formatting rule only where the entry turns ``in chat`` on
"""

import pytest
from kaye_engine.exportable import exportable_registry
from kaye_engine.prompt.blueprint.registry import blueprint_registry
from kaye_engine.prompt.blueprint.render_profile import RenderProfile
from kaye_library.registrations._common import (
    SIDECAR_FOR_KAYE,
    SIDECAR_IN_CHAT,
)

_NAME = "persona"


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
            "persona-kaye",
            "persona-kaye-speech-habit",
        ],
    )
    def test_folds_into_persona(_, name):
        assert name not in blueprint_registry


class TestContent:

    def test_opens_with_the_formatting_rule(_, content):
        assert content.startswith("# Personality")
        assert "## Diathesis Public" in content

    def test_holds_the_signature(_, content):
        assert "## Signature" in content

    def test_leaves_the_trailer_to_git(_, kaye_content):
        assert "Co-author Trailer" not in kaye_content
        assert "kaye-lel@users.noreply.github.com" not in kaye_content

    def test_kaye_name_shows_for_kaye(_, kaye_content):
        # persona-free: Kaye's name needs the entry's ``for Kaye``
        assert "Kaye LeL" in kaye_content

    def test_takes_every_kind_node_whole(_):
        bp = blueprint_registry[_NAME].blueprint

        assert {tuple(p) for p in bp.nodes} == {("Personality",)}
        assert {tuple(p) for p in bp.subtrees} == {
            ("Personality", "Signature"),
            ("Personality", "Diathesis Public"),
            ("Personality", "Speech Habit Public"),
            ("Personality", "{in chat}"),
        }
        assert not bp.dependencies

    def test_names_no_persona_of_its_own(_):
        profile = RenderProfile(conditional_sidecars=("for Ria",))
        content = blueprint_registry[_NAME].content(profile=profile)

        assert "Kaye LeL" not in content
        assert "You are **Kaye**" not in content


class TestInChat:

    _RULE = "You speak as a persona, so a response can carry two content types"
    _EXAMPLE = "> 🫖 I hope this reads clearly."
    _RAPPORT_ONLY = "🫖 Good evening. I hope the day has treated you gently."

    def test_chat_kaye_renders_the_rule_and_example(self):
        content = exportable_registry["chat-kaye"].content()

        assert "## {in chat}" in content
        assert self._RULE in content
        assert self._EXAMPLE in content
        assert self._RAPPORT_ONLY in content

    def test_persona_alone_leaves_them_out(self, kaye_content):
        assert self._RULE not in kaye_content
        assert self._EXAMPLE not in kaye_content
        assert self._RAPPORT_ONLY not in kaye_content

    @pytest.mark.parametrize("name", ["chat-kaye", "chat-basic-kaye", "coder"])
    def test_entry_profile_turns_in_chat_on(_, name):
        sidecars = blueprint_registry[name].render_profile.conditional_sidecars

        assert SIDECAR_FOR_KAYE in sidecars
        assert SIDECAR_IN_CHAT in sidecars
