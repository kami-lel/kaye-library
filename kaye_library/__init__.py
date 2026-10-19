"""
kaye_library.__init__.py

the shareable layer over kaye-engine: style, element, git, repository,
agent, and coder prompts; importing this module alone loads nothing

a consumer package, or ``setup_kaye_library_for_kaye_engine`` standalone,
calls the six steps below in this order: consumer, abbr glossaries, abbr
data (``get_kaye_library_abbrs_json_path``), dynamic substitutions,
corpus, then blueprints once the corpus tree is loaded
"""

from importlib.metadata import version
from pathlib import Path

from kaye_engine import register_comment_line, register_consumer

__all__ = (
    "CONSUMER_DISPLAY_NAME",
    "LOGGER_NAME",
    "PACKAGE_NAME",
    "PROGRAM_NAME",
    "get_kaye_library_abbrs_json_path",
    "register_kaye_library_abbr_glossaries",
    "register_kaye_library_blueprints",
    "register_kaye_library_consumer",
    "register_kaye_library_corpus",
    "register_kaye_library_dynamic_substitutions",
)


# constants  ###################################################################
PROGRAM_NAME = "kaye-library"
PACKAGE_NAME = "kaye-library"
LOGGER_NAME = "kaye.library"
CONSUMER_DISPLAY_NAME = "Kaye Library"

_CORPUS_DIR = Path(__file__).resolve().parent / "registrations"
_ABBRS_JSON_FILE_PATH = Path(__file__).resolve().parent / "abbrs.json"

# corpus files, in registration order; each registers under the root
_CORPUS_SOURCES = []


# Public API  ##################################################################
def register_kaye_library_consumer():
    """
    register this package's consumer record, which owns every exportable
    it registers, and the ``Kaye Library vX`` line of every generated
    prompt comment
    """
    package_version = version(PACKAGE_NAME)
    register_consumer(CONSUMER_DISPLAY_NAME, PACKAGE_NAME, package_version)
    register_comment_line("Kaye Library v{}".format(package_version))


def register_kaye_library_abbr_glossaries():
    """
    register every kaye-library abbr glossary
    """
    from kaye_library.registrations import (  # pylint: disable=C0415
        register_kaye_library_abbr_glossaries as register_glossaries,
    )

    register_glossaries()


def get_kaye_library_abbrs_json_path():
    """
    :return: path of the library's ``abbrs.json``, for
            ``populate_abbr_data_with_json_file`` after the glossaries
            are registered
    :rtype: Path
    """
    return _ABBRS_JSON_FILE_PATH


def register_kaye_library_dynamic_substitutions():
    """
    register every kaye-library dynamic substitution
    """
    from kaye_library.registrations import (  # pylint: disable=C0415
        register_kaye_library_dynamic_substitutions as register_substitutions,
    )

    register_substitutions()


def register_kaye_library_corpus():
    """
    record every kaye-library corpus file under the root of the tree;
    the caller loads the tree once every consumer has registered


    :raises ValueError: the corpus tree is already loaded
    """
    from kaye_engine import register_corpus_under_node  # pylint: disable=C0415

    for source in _CORPUS_SOURCES:
        register_corpus_under_node((), _CORPUS_DIR / source)


def register_kaye_library_blueprints():
    """
    register every kaye-library blueprint

    Prerequisite: the corpus tree is loaded


    :raises ValueError: the corpus tree is not yet loaded
    """
    from kaye_library.registrations import (  # pylint: disable=C0415
        register_kaye_library_blueprints as register_blueprints,
    )

    register_blueprints()
