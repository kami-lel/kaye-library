"""
kaye_library.registrations.coder.coder_glossary.py

register Coder related abbr glossaries
"""

from .._common import register_abbr_glossary

__all__ = (
    "DEFAULT_CODING_TERMS_THRESHOLD",
    "register_coder_abbr_glossaries",
)

DEFAULT_CODING_TERMS_THRESHOLD = 10


def register_coder_abbr_glossaries():
    """
    register ``coder-abbr``, ``coder-identifier-shorthand``,
    ``coder-documentation-field-shorthand``, ``coder-u3d-abbr``,
    ``coder-u3d-identifier``, ``programming-language-codes``
    """
    register_abbr_glossary(
        "coder-documentation-field-shorthand",
        False,
        is_dyn_substitution=True,
    )
    register_abbr_glossary("coder-abbr", True, is_dyn_substitution=True)
    register_abbr_glossary(
        "coder-identifier-shorthand", False, is_dyn_substitution=True
    )
    register_abbr_glossary(
        "programming-language-codes",
        True,
        is_dyn_substitution=True,
    )
    register_abbr_glossary("coder-u3d-abbr", False, is_dyn_substitution=True)
    register_abbr_glossary(
        "coder-u3d-identifier", False, is_dyn_substitution=True
    )
