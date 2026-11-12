"""
kaye_library.registrations.p4v.p4v_bp.py

register Perforce related blueprints
"""

from kaye_engine.prompt.blueprint import get_corpus_node

from .._common import register_exportable, register_node

__all__ = ("register_p4v_blueprints",)


def register_p4v_blueprints():
    """
    register every blueprint under the "Perforce" corpus node
    """
    # Working with Perforce
    register_node(
        register_exportable,
        "working-with-p4v",
        get_corpus_node("Perforce"),
        "Working with Perforce",
        recursively=True,
    )
