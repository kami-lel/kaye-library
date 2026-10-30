"""
kaye_library.registrations.amanuensis.amanuensis_glossary.py

register Amanuensis related abbr glossaries
"""

from .._common import register_abbr_glossary

__all__ = ("register_amanuensis_abbr_glossaries",)


def register_amanuensis_abbr_glossaries():
    """
    register Amanuensis writer shorthand glossaries
    """
    register_abbr_glossary(
        "amanuensis-config-writer-shorthand",
        False,
        is_dyn_substitution=True,
    )
    register_abbr_glossary(
        "amanuensis-keybinding-writer-shorthand",
        False,
        is_dyn_substitution=True,
        is_sorted=True,
    )
