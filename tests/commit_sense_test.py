"""
commit_sense_test.py

Unit Tests (using pytest) for: the library's own ``commit-sense`` and
``commit-sense-branch-merging`` skills: the Co-author Trailer rule,
signed as Kaye
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

    def test_no_separate_core_entry(_):
        assert "commit-sense-core" not in blueprint_registry

    def test_skill_is_the_one_exportable_entry(_):
        assert blueprint_registry["commit-sense"].is_exportable
        assert exportable_registry["commit-sense"] is (
            blueprint_registry["commit-sense"]
        )


class TestContent:

    def test_co_author_trailer_example_signs_as_kaye(_, content):
        assert "3. Co-author Trailer: optional" in content
        # the sidecar line plus the example under the Kaye node
        assert content.count(_KAYE_TRAILER_PLAIN) >= 2
        assert "Example Bot" not in content

    def test_keeps_the_trailer_last(_, content):
        assert "as the **last line**" in content

    def test_names_no_generic_ai(_, content):
        assert "Claude" not in content

    def test_selects_ascii_only(_, content):
        assert "# ASCII only" in content or "ASCII only" in content

    def test_ledger_sigils_render(_, content):
        assert "per-file change sigil" in content


_KAYE_TRAILER_PLAIN = (
    "Co-authored-by: Kaye LeL <341862645+kaye-lel@users.noreply.github.com>"
)
_KAYE_TRAILER = f"`{_KAYE_TRAILER_PLAIN}`"


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
        assert "add no trailer" in content

    def test_bans_a_generic_model_or_provider_trailer(_, content):
        assert "**never** write a generic model or provider name" in content

    def test_merge_message_always_carries_the_trailer(_):
        content = exportable_registry["commit-sense-branch-merging"].content()

        assert "**always** append your [Co-author Trailer]" in content
