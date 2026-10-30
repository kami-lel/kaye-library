"""
kaye_library.registrations.secretary.secretary_glossary.py

register Secretary related abbr glossaries
"""

from .._common import register_abbr_glossary

__all__ = ("register_secretary_abbr_glossaries",)


def register_secretary_abbr_glossaries():
    """
    register the generic ``secretary-*`` abbr glossaries; the glossaries
    that carry personal values are left to the consumer, so a skill
    splicing one renders its placeholder literally until a consumer
    registers it
    """
    register_abbr_glossary(
        "secretary-common-shorthand", False, is_dyn_substitution=True
    )
    register_abbr_glossary(
        "secretary-eisenhower-matrix-quadrant", True, is_sorted=True
    )
    register_abbr_glossary(
        "secretary-eisenhower-matrix-quadrant-base",
        False,
        is_sorted=True,
        is_dyn_substitution=True,
    )
