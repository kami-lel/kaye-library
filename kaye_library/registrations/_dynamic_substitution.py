"""
kaye_library.registrations._dynamic_substitution.py

shared auxiliaries for the ``register_*_dynamic_substitutions``
functions; kept apart from ``_common`` since it needs no corpus tree
"""

import kamilog
from kaye_engine import (
    StringDynamicSubstitution,
    register_dynamic_substitution,
)

from kaye_library import LOGGER_NAME

__all__ = ("register_md_file_dynamic_substitution",)


def register_md_file_dynamic_substitution(
    name, md_file_path, *, logger_name=LOGGER_NAME
):
    """
    register the text of ``md_file_path`` as the
    ``StringDynamicSubstitution`` ``name``


    :param logger_name: logger a read failure reports through, so a
            consumer package logs under its own name
    :type logger_name: str, optional
    :raises SystemExit: the file cannot be read
    """
    try:
        content = md_file_path.read_text()
    except OSError as err:
        kamilog.getLogger(logger_name).critical(
            f"cannot read {name} file {md_file_path}:\t" + str(err)
        )
        raise SystemExit(1) from err

    register_dynamic_substitution(name, StringDynamicSubstitution(content))
