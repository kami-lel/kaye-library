"""
kaye_library.registrations.__init__.py

register every kaye-library blueprint, abbr glossary, and dynamic
substitution; ``*_bp.py`` imports stay function-local until the corpus
tree is loaded
"""

from .agent.agent_glossary import register_agent_abbr_glossaries
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
    from .agent.agent_bp import (  # pylint: disable=C0415
        register_agent_blueprints,
    )
    from .element.element_bp import (  # pylint: disable=C0415
        register_element_blueprints,
    )
    from .project.project_bp import (  # pylint: disable=C0415
        register_project_blueprints,
    )
    from .repo.repo_bp import (  # pylint: disable=C0415
        register_repo_blueprints,
    )
    from .repo.workflows_bp import (  # pylint: disable=C0415
        register_repo_workflow_blueprints,
    )
    from .git.git_bp import (  # pylint: disable=C0415
        register_git_blueprints,
    )
    from .letter_case.letter_case_bp import (  # pylint: disable=C0415
        register_letter_case_blueprints,
    )
    from .style.style_bp import (  # pylint: disable=C0415
        register_style_blueprints,
    )

    register_agent_blueprints()
    register_style_blueprints()
    register_letter_case_blueprints()
    register_element_blueprints()
    register_project_blueprints()
    register_repo_blueprints()
    register_repo_workflow_blueprints()
    register_git_blueprints()


def register_kaye_library_abbr_glossaries():
    """
    register every kaye-library abbr glossary, one call per feature
    group, order-independent
    """
    register_agent_abbr_glossaries()
    register_element_abbr_glossaries()
    register_git_abbr_glossaries()
    register_style_abbr_glossaries()


def register_kaye_library_dynamic_substitutions():
    """
    register every kaye-library dynamic substitution
    """
