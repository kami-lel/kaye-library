"""
tests/conftest.py

load the library standalone, once per session, before any test module
is imported
"""

import zipfile
from importlib.metadata import version

import kaye_library

kaye_library.setup_kaye_library_for_kaye_engine()

import pytest  # pylint: disable=wrong-import-position
from kaye_engine.prompt.blueprint.render_profile import (  # noqa: E402
    RenderProfile,
)
from kaye_engine.skill.export_folders import (  # noqa: E402
    export_skills_as_folders,
)
from kaye_engine.skill.export_zips import export_skills_as_zips  # noqa: E402

_RENDER_PROFILE = RenderProfile(sparseness=0, show_comment=False)


# Pytest fixtures  #############################################################
@pytest.fixture(scope="session")
def testee_skills_folder(tmp_path_factory):
    """
    every skill the library registers, exported as folders
    """
    folder = tmp_path_factory.mktemp("skills")
    export_skills_as_folders(
        folder,
        version=version("kaye-library"),
        render_profile=_RENDER_PROFILE,
        consumer="kaye-library",
    )
    return folder


@pytest.fixture(scope="session")
def testee_skill_zips_folder(tmp_path_factory):
    """
    every skill the library registers, exported as .zip packages
    """
    folder = tmp_path_factory.mktemp("skill_zips")
    export_skills_as_zips(
        folder,
        version=version("kaye-library"),
        render_profile=_RENDER_PROFILE,
        names=_library_skill_names(),
    )
    return folder


@pytest.fixture(scope="session")
def testee_extracted_skills_folder(testee_skill_zips_folder, tmp_path_factory):
    """
    every .zip package of ``testee_skill_zips_folder``, extracted
    """
    folder = tmp_path_factory.mktemp("extracted")
    for zip_file in testee_skill_zips_folder.glob("*.zip"):
        with zipfile.ZipFile(zip_file) as archive:
            archive.extractall(folder)
    return folder


def _library_skill_names():
    from kaye_engine.exportable import exportable_registry  # noqa: E402

    return [
        name
        for name, entry in exportable_registry.items()
        if entry.consumer == "kaye-library"
    ]
