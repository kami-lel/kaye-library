"""
u3d_test.py

Unit Tests (using pytest) for: the Unity Engine corpus and skills the
library ships -- a root node of its own, skills without the ``coder-``
prefix, persona-free
"""

import pytest
from kaye_engine.exportable import exportable_registry
from kaye_engine.prompt import get_corpus_tree
from kaye_engine.prompt.blueprint.registry import blueprint_registry

_U3D_SKILLS = (
    "u3d",
    "u3d-assets-management",
    "u3d-coding",
    "u3d-common-type-and-suffix",
    "u3d-game-tuning",
    "u3d-if",
    "u3d-mb",
    "u3d-naming",
    "u3d-owner-driven-activation",
    "u3d-pfb",
    "u3d-so",
)


class TestCorpus:

    def test_unity_engine_is_a_root_node(_):
        names = {c.name for c in get_corpus_tree().children}

        assert "Unity Engine" in names

    def test_unity_engine_is_not_under_coder(_):
        names = {c.name for c in get_corpus_tree()["Coder"].children}

        assert "Coder Unity Engine" not in names
        assert "Unity Engine" not in names


class TestBlueprints:

    @pytest.mark.parametrize("name", _U3D_SKILLS)
    def test_skill_registered_by_library(_, name):
        assert exportable_registry[name].consumer == "kaye-library"

    def test_no_coder_prefixed_alias(_):
        stale = [n for n in blueprint_registry if n.startswith("coder-u3d")]

        assert not stale

    def test_core_depends_on_c_sharp(_):
        dependencies = blueprint_registry["u3d"].blueprint.dependencies

        assert "coder-c-sharp" in dependencies

    def test_mb_depends_on_briefness(_):
        dependencies = blueprint_registry["u3d-mb"].blueprint.dependencies

        assert "style-briefness-style" in dependencies


class TestRender:

    @pytest.mark.parametrize("name", _U3D_SKILLS)
    def test_skill_renders_without_persona(_, name):
        content = exportable_registry[name].content()

        assert content.strip()
        for needle in ("Kaye", "Persona", "Kami"):
            assert needle not in content, name

    def test_core_keeps_top_heading(_):
        assert "\n# Unity Engine\n" in "\n" + (
            blueprint_registry["u3d"].content()
        )
