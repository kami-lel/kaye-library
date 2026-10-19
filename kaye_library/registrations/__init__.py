"""
kaye_library.registrations.__init__.py

register every kaye-library blueprint, abbr glossary, and dynamic
substitution; ``*_bp.py`` imports stay function-local until the corpus
tree is loaded
"""

from .element.element_glossary import register_element_abbr_glossaries
from .git.git_glossary import register_git_abbr_glossaries
from .style.style_glossary import register_style_abbr_glossaries

__all__ = (
    "register_kaye_library_abbr_glossaries",
    "register_kaye_library_blueprints",
    "register_kaye_library_dynamic_substitutions",
)


def register_kaye_library_blueprints():
    """
    register every kaye-library blueprint into kaye-engine's
    ``blueprint_registry``, in dependency order


    :raises ValueError: the default corpus tree is not yet loaded
    """


def register_kaye_library_abbr_glossaries():
    """
    register every kaye-library abbr glossary, one call per feature
    group, order-independent
    """
    register_element_abbr_glossaries()
    register_git_abbr_glossaries()
    register_style_abbr_glossaries()


def register_kaye_library_dynamic_substitutions():
    """
    register every kaye-library dynamic substitution
    """
