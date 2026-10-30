"""
kaye_library.__init__.py

the shareable layer over kaye-engine: style, element, git, repository,
agent, coder, and meta prompts; importing this module alone loads nothing

a consumer package, or ``setup_kaye_library_for_kaye_engine`` standalone,
calls the six steps below in this order: consumer, abbr glossaries, abbr
data (``get_kaye_library_abbrs_json_path``), dynamic substitutions,
corpus, then blueprints once the corpus tree is loaded
"""

from importlib.metadata import version
from pathlib import Path

import kamilog
from kaye_engine import (
    load_corpus_tree,
    populate_abbr_data_with_json_file,
    register_comment_line,
    register_consumer,
    set_entry_consumer,
    setup_claude_cli,
    setup_hermes_cli,
)

__all__ = (
    "KAYE_LIBRARY_DISPLAY_NAME",
    "LOGGER_NAME",
    "PACKAGE_NAME",
    "PROGRAM_NAME",
    "get_kaye_library_abbrs_json_path",
    "register_kaye_library_abbr_glossaries",
    "register_kaye_library_blueprints",
    "register_kaye_library_consumer",
    "register_kaye_library_corpus",
    "register_kaye_library_dynamic_substitutions",
    "setup_kaye_library_for_kaye_engine",
)


# constants  ###################################################################
PROGRAM_NAME = "kaye-library"
PACKAGE_NAME = "kaye-library"
LOGGER_NAME = "kaye.library"
KAYE_LIBRARY_DISPLAY_NAME = "Kaye Library"

_CORPUS_DIR = Path(__file__).resolve().parent / "registrations"
_ABBRS_JSON_FILE_PATH = Path(__file__).resolve().parent / "abbrs.json"

# corpus files, in registration order: (node path, file), a file's top
# headings sitting one level below its node
_CORPUS_SOURCES = [
    ((), "dynamic_nodes/dynamic_nodes.md"),
    ((), "agent/agent.md"),
    ((), "style/style.md"),
    ((), "element/element.md"),
    ((), "project/project.md"),
    ((), "repo/repo.md"),
    ((), "git/git.md"),
    ((), "meta_prompt/meta_prompt.md"),
    ((), "coder/coder.md"),
    (("Coder",), "coder/coder-bash.md"),
    (("Coder",), "coder/coder-powershell.md"),
    (("Coder",), "coder/coder-c-and-cpp.md"),
    (("Coder",), "coder/coder-unreal-engine.md"),
    (("Coder",), "coder/coder-c-sharp.md"),
    (("Coder",), "coder/coder-u3d.md"),
    (("Coder",), "coder/coder-gdscript.md"),
    (("Coder",), "coder/coder-html.md"),
    (("Coder",), "coder/coder-javascript-and-typescript.md"),
    (("Coder",), "coder/coder-python.md"),
]


# Public API  ##################################################################
def register_kaye_library_consumer():
    """
    register this package's consumer record, which owns every exportable
    it registers, and the ``Kaye Library vX`` line of every generated
    prompt comment
    """
    package_version = version(PACKAGE_NAME)
    register_consumer(KAYE_LIBRARY_DISPLAY_NAME, PACKAGE_NAME, package_version)
    register_comment_line(
        "{} v{}".format(KAYE_LIBRARY_DISPLAY_NAME, package_version)
    )


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
    record every kaye-library corpus file under its node of the tree, the
    root or its own Coder node; the caller loads the tree once every
    consumer has registered


    :raises ValueError: the corpus tree is already loaded
    """
    from kaye_engine import (  # pylint: disable=C0415
        register_corpus_under_node,
    )

    for node_path, source in _CORPUS_SOURCES:
        register_corpus_under_node(node_path, _CORPUS_DIR / source)


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


def setup_kaye_library_for_kaye_engine():
    """
    load, in this order, everything the library supplies on its own:

    1. the consumer record and its ``Kaye Library vX`` comment line
    2. every abbr glossary, registered into ``abbr_glossary_registry``
    3. abbr database
    4. every dynamic substitution
    5. prompt corpus tree, built from the sources registered under the
       root
    6. every library blueprint, registered into ``blueprint_registry``
    7. the entry consumer, via ``set_entry_consumer``
    8. the Claude CLI and Hermes CLI configuration, naming no chat or
       coder exportable and no Hermes soul

    a process runs exactly one setup function: a package building on the
    library calls the six steps instead, and never this one
    """
    logger = kamilog.getLogger(LOGGER_NAME)

    register_kaye_library_consumer()

    try:
        register_kaye_library_abbr_glossaries()
        populate_abbr_data_with_json_file(get_kaye_library_abbrs_json_path())
        register_kaye_library_dynamic_substitutions()
        register_kaye_library_corpus()
        load_corpus_tree()
    except OSError as err:
        logger.critical("cannot load library corpus/abbr data:\t" + str(err))
        raise SystemExit(1) from err

    try:
        register_kaye_library_blueprints()
    except (KeyError, AttributeError) as err:
        logger.critical("failed to register library blueprints:\t" + str(err))
        raise SystemExit(1) from err

    set_entry_consumer(PACKAGE_NAME)
    setup_claude_cli()
    setup_hermes_cli()
