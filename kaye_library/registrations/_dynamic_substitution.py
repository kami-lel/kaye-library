"""
kaye_library.registrations._dynamic_substitution.py

binds the engine's ``register_md_file_dynamic_substitution`` to the
library logger; kept apart from ``_common`` since it needs no corpus tree
"""

import functools

from kaye_engine import register_md_file_dynamic_substitution as _register

from kaye_library import LOGGER_NAME

__all__ = ("register_md_file_dynamic_substitution",)

register_md_file_dynamic_substitution = functools.partial(
    _register, logger_name=LOGGER_NAME
)
