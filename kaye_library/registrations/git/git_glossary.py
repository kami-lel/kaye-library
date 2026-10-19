"""
kaye_library.registrations.git.git_glossary.py

register Git related abbr glossaries
"""

from .._common import register_abbr_glossary

__all__ = ("register_git_abbr_glossaries",)


def register_git_abbr_glossaries():
    """
    register ``git-abbr``, ``commit-sense-shorthand``,
    ``commit-sense-sigil``
    """
    register_abbr_glossary("git-abbr", False, is_dyn_substitution=True)

    # commit sense
    register_abbr_glossary(
        "commit-sense-shorthand",
        False,
        is_remark_disabled=True,
        is_dyn_substitution=True,
    )
    register_abbr_glossary(
        "commit-sense-sigil",
        False,
        is_numbered_list=True,
        is_sorted=True,
        is_dyn_substitution=True,
    )
