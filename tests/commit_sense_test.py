"""
commit_sense_test.py

Unit Tests (using pytest) for: the library's own ``commit-sense`` skill,
which names no persona and shows a generic co-author trailer
"""

import pytest
from kaye_engine.exportable import exportable_registry
from kaye_engine.prompt.blueprint.registry import blueprint_registry


@pytest.fixture(scope="module")
def content():
    return exportable_registry["commit-sense"].content()


class TestOwnership:

    def test_skill_belongs_to_the_library(_):
        assert exportable_registry["commit-sense"].consumer == "kaye-library"

    def test_core_is_internal(_):
        assert not blueprint_registry["commit-sense-core"].is_exportable

    def test_skill_builds_on_the_core(_):
        blueprint = blueprint_registry["commit-sense"].blueprint

        assert blueprint.dependencies == ("commit-sense-core",)


class TestContent:

    def test_generic_co_author_trailer(_, content):
        assert "3. Co-author Trailer: optional" in content
        assert "Co-authored-by: Example Bot <bot@example.com>" in content

    def test_keeps_the_trailer_last(_, content):
        assert "Keep the trailer last." in content

    @pytest.mark.parametrize(
        "needle",
        ["Personality", "Persona Trailer", "Kaye LeL", "kaye-lel", "Claude"],
    )
    def test_names_no_persona(_, content, needle):
        assert needle not in content

    def test_selects_ascii_only(_, content):
        assert "# ASCII only" in content or "ASCII only" in content

    def test_ledger_sigils_render(_, content):
        assert "per-file change sigil" in content
