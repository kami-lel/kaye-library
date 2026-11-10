"""
kaye_library.registrations.u3d.u3d_glossary.py

register Unity Engine related abbr glossaries
"""

from .._common import register_abbr_glossary

__all__ = ("register_u3d_abbr_glossaries",)


def register_u3d_abbr_glossaries():
    """
    register ``u3d-abbr``, ``u3d-identifier`` and ``u3d-units``
    """
    register_abbr_glossary("u3d-abbr", False, is_dyn_substitution=True)
    register_abbr_glossary("u3d-identifier", False, is_dyn_substitution=True)
    register_abbr_glossary("u3d-units", False, is_dyn_substitution=True)
