"""
example_consumer.__init__.py

a minimal package built on kaye-library: it composes the library's six
steps, adds its own corpus and values, takes one library skill over, and
names itself the entry consumer
"""

from importlib.metadata import version
from pathlib import Path

import kaye_library
from kaye_engine import (
    StringDynamicSubstitution,
    load_corpus_tree,
    override_exportable,
    populate_abbr_data_with_json_file,
    register_blueprint,
    register_consumer,
    register_corpus_under_node,
    register_dynamic_substitution,
    set_entry_consumer,
)
from kaye_engine.prompt.blueprint import (
    create_blueprint,
    create_blueprint_from_node,
    get_blueprint,
    get_corpus_node,
    replace_meta,
)

__all__ = ("PACKAGE_NAME", "PROGRAM_NAME", "setup_example_consumer")

PACKAGE_NAME = "example-consumer"
PROGRAM_NAME = "example-consumer"
DISPLAY_NAME = "Example Consumer"

_FOLDER = Path(__file__).resolve().parent


def setup_example_consumer():
    """
    run the library's steps in order, with the package's own values and
    corpus between them; a process runs exactly this one setup
    """
    # 1. consumer records: the library's, then this package's
    kaye_library.register_kaye_library_consumer()
    register_consumer(DISPLAY_NAME, PACKAGE_NAME, version(PACKAGE_NAME))

    # 2. glossaries, then abbr data: the library's, then this package's own
    #    entries, here one more calendar
    kaye_library.register_kaye_library_abbr_glossaries()
    populate_abbr_data_with_json_file(
        kaye_library.get_kaye_library_abbrs_json_path()
    )
    populate_abbr_data_with_json_file(_FOLDER / "abbrs.json")

    # 3. substitutions: the library registers none a consumer must supply,
    #    so this package registers the personal one, its Gmail account
    kaye_library.register_kaye_library_dynamic_substitutions()
    register_dynamic_substitution(
        "secretary-email-authuser", StringDynamicSubstitution("1")
    )

    # 4. corpus: the library's files, then this package's own, then load
    kaye_library.register_kaye_library_corpus()
    register_corpus_under_node((), _FOLDER / "example.md")
    load_corpus_tree()

    # 5. blueprints: the library's, then this package's
    kaye_library.register_kaye_library_blueprints()
    _register_example_blueprints()

    set_entry_consumer(PACKAGE_NAME)


def _register_example_blueprints():
    """
    register the package's own skill, then take over ``style-good-writing``
    as the library skill plus the package's house rules
    """
    register_blueprint(
        "example-house-rules",
        create_blueprint_from_node(
            get_corpus_node("Example House Rules"), is_recursive=True
        ),
        consumer=PACKAGE_NAME,
    )

    # the library skill enters by object, taken before the override: a
    # string dependency on its own name would form a cycle
    library_entry = get_blueprint("style-good-writing")
    library_meta = library_entry.blueprint.meta
    bp = replace_meta(
        create_blueprint(
            dependencies=[library_entry.blueprint, "example-house-rules"]
        ),
        display_name="Style Good Writing",
        description_node=library_meta.description_node,
        when_to_use_node=library_meta.when_to_use_node,
    )
    override_exportable("style-good-writing", bp, consumer=PACKAGE_NAME)
