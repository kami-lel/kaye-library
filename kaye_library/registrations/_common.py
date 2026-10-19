"""
kaye_library.registrations._common.py

shared auxiliaries for the ``register_*_blueprints`` functions; the
generic helpers take their ``register_fn``, so any consumer package
may build on them, while the partials below bind this package's own
consumer
"""

import functools

from kaye_engine import register_abbr_glossary as _register_abbr_glossary
from kaye_engine import register_blueprint
from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
    create_blueprint_from_node,
    get_corpus_index,
    replace_meta,
)

__all__ = (
    "CONSUMER_NAME",
    "glossary_blueprint",
    "mark_as_leaf",
    "register_abbr_glossary",
    "register_children",
    "register_exportable",
    "register_leaf",
    "register_node",
    "register_prompt",
    "walk_and_checkmark",
)

# canonical name of this package's consumer record, the owner of every
# exportable registered here; equals ``kaye_library.PACKAGE_NAME``
CONSUMER_NAME = "kaye-library"

register_exportable = functools.partial(
    register_blueprint, is_exportable=True, consumer=CONSUMER_NAME
)

register_prompt = functools.partial(
    register_blueprint,
    is_exportable=True,
    llm_invokable=False,
    consumer=CONSUMER_NAME,
)

register_abbr_glossary = functools.partial(
    _register_abbr_glossary, consumer=CONSUMER_NAME
)


def register_node(
    register_fn,
    slug,
    container,
    name,
    *,
    recursively=False,
    dependencies=None,
    display_name=None,
    **extra,
):
    """
    register ``name`` from ``container`` under ``slug`` via ``register_fn``
    """
    bp = create_blueprint_from_node(
        container[name],
        is_recursive=recursively,
        dependencies=dependencies or (),
    )

    return register_fn(
        slug,
        replace_meta(bp, display_name=display_name or name),
        **extra,
    )


def walk_and_checkmark(bp, ancestor_path):
    """
    walk ``ancestor_path``, checkmarking each node non-recursively


    :return: the blueprint with every node on the path checkmarked, and
            the path of the last one
    :rtype: tuple[Blueprint, tuple[str, ...]]
    """
    path = ()
    for name in ancestor_path:
        path = (*path, name)
        bp = checkmark_nodes(bp, path)
    return bp, path


def mark_as_leaf(bp, leaf_path):
    """
    checkmark the node at ``leaf_path`` recursively, and point the
    blueprint's meta at the leaf's own ``{description}``,
    ``{when_to_use}`` and ``{globs}`` sidecar nodes, where it has them


    :return: the blueprint with the leaf and its descriptors marked
    :rtype: Blueprint
    """
    index = get_corpus_index()

    bp = checkmark_nodes(bp, leaf_path, is_recursive=True)

    descriptors = {}
    for field, name in (
        ("description_node", "{description}"),
        ("when_to_use_node", "{when_to_use}"),
        ("globs_node", "{globs}"),
    ):
        path = (*leaf_path, name)
        if path in index.idx_by_path:
            descriptors[field] = path

    return replace_meta(bp, **descriptors)


def register_leaf(
    register_fn,
    slug,
    ancestor_path,
    leaf_name,
    *,
    display_name=None,
    dependencies=None,
    extra_checkmarks=(),
    **extra,
):
    """
    register ``leaf_name`` under the node at ``ancestor_path``
    """
    bp = create_blueprint(dependencies=dependencies or ())
    bp, ancestor_path = walk_and_checkmark(bp, ancestor_path)

    for extra_node_name in extra_checkmarks:
        bp = checkmark_nodes(bp, (extra_node_name,))

    bp = mark_as_leaf(bp, (*ancestor_path, leaf_name))

    bp = replace_meta(bp, display_name=display_name or leaf_name)

    return register_fn(slug, bp, **extra)


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


def glossary_blueprint(*glossary_names):
    """
    build a blueprint checkmarking each of ``glossary_names``
    """
    bp = create_blueprint()
    for name in glossary_names:
        bp = checkmark_nodes(bp, f"({name})")
    return bp
