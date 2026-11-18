"""
kaye_library.registrations.personality.personality_glossary.py

register Personality related abbr glossaries
"""

from .._common import register_abbr_glossary

__all__ = ("register_personality_abbr_glossaries",)


def register_personality_abbr_glossaries():
    """
    register ``person-signifier``, which lists the Kaye signifier; a
    package building on the library adds its own personas' signifiers
    through its own ``abbrs.json``
    """
    register_abbr_glossary(
        "person-signifier", False, is_dyn_substitution=True
    )
