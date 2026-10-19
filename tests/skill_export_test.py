"""
skill_export_test.py

Unit Tests (using pytest) for: every skill the library registers,
exported as a folder and as a .zip package -- structure, frontmatter,
and the wording the skill must render
"""

import pytest
from kaye_engine.exportable import exportable_registry

from tests import data
from tests.support import (
    VERSION_LINE_PATTERN,
    is_frontmatter_md_file_basic_structure,
    split_frontmatter_md_file,
)

SKILL_NAMES = sorted(
    name
    for name, entry in exportable_registry.items()
    if entry.consumer == "kaye-library"
)


def _read(folder, name):
    return (folder / name / "SKILL.md").read_text(encoding="utf-8")


@pytest.fixture(scope="module", params=("folder", "zip"))
def skills_folder(request, testee_skills_folder, testee_extracted_skills_folder):
    if request.param == "folder":
        return testee_skills_folder
    return testee_extracted_skills_folder


class TestBasic:

    @pytest.mark.parametrize("name", SKILL_NAMES)
    def test_skill_file_exists(_, skills_folder, name):
        assert (skills_folder / name / "SKILL.md").is_file()

    def test_exports_nothing_else(_, skills_folder):
        assert sorted(p.name for p in skills_folder.iterdir()) == SKILL_NAMES


class TestHeader:

    @pytest.mark.parametrize("name", SKILL_NAMES)
    def test_name_and_version(_, skills_folder, name):
        header, _body = split_frontmatter_md_file(_read(skills_folder, name))

        assert "name: " + name in header
        assert any(VERSION_LINE_PATTERN.match(line) for line in header)

    @pytest.mark.parametrize("name", sorted(data.DESCRIPTION_CONTENT))
    def test_description(_, skills_folder, name):
        header, _body = split_frontmatter_md_file(_read(skills_folder, name))

        assert any(data.DESCRIPTION_CONTENT[name] in line for line in header)

    @pytest.mark.parametrize("name", sorted(data.WHEN_TO_USE_CONTENT))
    def test_when_to_use(_, skills_folder, name):
        header, _body = split_frontmatter_md_file(_read(skills_folder, name))

        assert any(data.WHEN_TO_USE_CONTENT[name] in line for line in header)


class TestStructure:

    @pytest.mark.parametrize("name", SKILL_NAMES)
    def test_frontmatter_and_body(_, skills_folder, name):
        assert is_frontmatter_md_file_basic_structure(
            _read(skills_folder, name)
        )

    @pytest.mark.parametrize("name", SKILL_NAMES)
    def test_no_unresolved_placeholder(_, skills_folder, name):
        assert "(((" not in _read(skills_folder, name)


class TestContent:

    @pytest.mark.parametrize("name", sorted(data.FILE_CONTENT))
    def test_wording(_, skills_folder, name):
        _header, body = split_frontmatter_md_file(_read(skills_folder, name))

        for snippet in data.FILE_CONTENT[name]:
            assert snippet in body, snippet
