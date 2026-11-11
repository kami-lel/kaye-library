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
    ``coder-documentation-field-shorthand``, ``programming-language-codes``
    """
    register_abbr_glossary(
        "coder-documentation-field-shorthand",
        False,
        is_dyn_substitution=True,
    )
    register_abbr_glossary(
        "coder-abbr",
        True,
        is_dyn_substitution=True,
        description=(
            "Decodes common programming abbreviations such as ctor, iface,"
            " and mpl."
        ),
        when_to_use=(
            "Trigger when a user writes programming shorthand such as ctor,"
            " iface, or xcp, or asks what a code abbreviation stands for."
        ),
    )
    register_abbr_glossary(
        "coder-identifier-shorthand", False, is_dyn_substitution=True
    )
    register_abbr_glossary(
        "programming-language-codes",
        True,
        is_dyn_substitution=True,
        description=(
            "Maps short language codes such as py, ts, and cpp to the"
            " programming languages they name."
        ),
        when_to_use=(
            "Trigger when a language code such as py, js, or cpp appears,"
            " or the user asks which language an abbreviation names."
        ),
    )
