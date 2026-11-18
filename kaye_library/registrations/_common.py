"""
kaye_library.registrations._common.py

shared auxiliaries for the ``register_*_blueprints`` functions; the
generic helpers come from ``kaye_engine``, re-exported here, and the
registrars below are bound to this package's own consumer
"""

from kaye_engine import (
    bind_registrars,
    glossary_blueprint,
    mark_as_leaf,
    register_leaf,
    register_node,
    walk_and_checkmark,
)

__all__ = (
    "CONSUMER_NAME",
    "SIDECAR_FOR_KAYE",
    "glossary_blueprint",
    "mark_as_leaf",
    "register_abbr_glossary",
    "register_children",
    "register_exportable",
    "register_internal",
    "register_leaf",
    "register_node",
    "register_prompt",
    "walk_and_checkmark",
)

# canonical name of this package's consumer record, the owner of every
# exportable registered here; equals ``kaye_library.PACKAGE_NAME``
CONSUMER_NAME = "kaye-library"

# conditional sidecar holding Kaye's own values, e.g. the signature
SIDECAR_FOR_KAYE = "for Kaye"

(
    register_exportable,
    register_prompt,
    register_internal,
    register_abbr_glossary,
) = bind_registrars(CONSUMER_NAME)


def register_children(
    register_fn, parent_slug, container, children, *, recursively=True, **extra
):
    """
    register each ``children`` entry depending on ``parent_slug``
    """
    for slug, display_name in children:
        register_node(
            register_fn,
            slug,
            container,
            display_name,
            recursively=recursively,
            dependencies=[parent_slug],
            **extra,
        )
