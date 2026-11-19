"""
commit_sense_test.py

Unit Tests (using pytest) for: the library's own ``commit-sense`` and
``commit-sense-branch-merging`` skills: the Co-author Trailer rule,
signed as Kaye
"""

import pytest
from kaye_engine.exportable import exportable_registry
from kaye_engine.prompt.blueprint.registry import blueprint_registry
from kaye_engine.prompt.blueprint.render_profile import RenderProfile


@pytest.fixture(scope="module")
def content():
    return exportable_registry["commit-sense"].content()


class TestOwnership:

    def test_skill_belongs_to_the_library(_):
        assert exportable_registry["commit-sense"].consumer == "kaye-library"

    def test_no_separate_core_entry(_):
        assert "commit-sense-core" not in blueprint_registry

    def test_skill_is_the_one_exportable_entry(_):
        assert blueprint_registry["commit-sense"].is_exportable
        assert exportable_registry["commit-sense"] is (
            blueprint_registry["commit-sense"]
        )


class TestContent:

    def test_generic_co_author_trailer(_, content):
        assert "3. Co-author Trailer: optional" in content
        assert "Co-authored-by: Example Bot <bot@example.com>" in content

    def test_keeps_the_trailer_last(_, content):
        assert "It is the **last line** of the message" in content

    def test_names_no_generic_ai(_, content):
        assert "Claude" not in content

    def test_selects_ascii_only(_, content):
        assert "# ASCII only" in content or "ASCII only" in content

    def test_ledger_sigils_render(_, content):
        assert "per-file change sigil" in content


_KAYE_TRAILER = (
    "`Co-authored-by: Kaye LeL"
    " <341862645+kaye-lel@users.noreply.github.com>`"
)


class TestSignedAsKaye:

    @pytest.mark.parametrize(
        "name", ["commit-sense", "commit-sense-branch-merging"]
    )
    def test_leaves_the_persona_out(_, name):
        content = exportable_registry[name].content()

        assert "## Diathesis Public" not in content
        assert "# Personality" not in content

    @pytest.mark.parametrize(
        "name", ["commit-sense", "commit-sense-branch-merging"]
    )
    def test_renders_kaye_s_trailer(_, name):
        content = exportable_registry[name].content()

        assert _KAYE_TRAILER in content

    def test_signs_only_changes_the_persona_wrote(_, content):
        assert "When you wrote the changes a commit records" in content
        assert "end it with no trailer" in content

    def test_avoids_a_generic_ai_trailer(_):
        # every surface renders {avoid}; a bare render needs it named
        profile = RenderProfile(conditional_sidecars=("avoid",))
        text = exportable_registry["commit-sense"].content(profile=profile)

        assert "A generic AI trailer naming a tool or model" in text
