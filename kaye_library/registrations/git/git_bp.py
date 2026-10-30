"""
kaye_library.registrations.git.git_bp.py

register Git related blueprints
"""

import functools

from kaye_engine import register_blueprint
from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
    get_corpus_node,
    replace_meta,
)

from .._common import (
    mark_as_leaf,
    register_exportable,
    register_leaf,
    register_node,
    register_prompt,
)

__all__ = ("register_git_blueprints",)

# internal, not exportable: the feature branch definition, and building
# blocks of the commit sense skill and its Dify prompts
_register_internal = functools.partial(register_blueprint, is_exportable=False)

_COMMIT_SENSE_PATH = ("Git", "commit sense")
_SIGIL_PATH = (*_COMMIT_SENSE_PATH, "per-file change sigil")
_NO_FIT_SIGIL_PATH = (*_SIGIL_PATH, "No Fit Fallback Sigil")
_ORDINARY_EDIT_SIGIL_PATH = (*_SIGIL_PATH, "Ordinary Edit Fallback Sigil")


def register_git_blueprints():
    """
    register every blueprint under the "Gits" corpus node
    """
    git_node = get_corpus_node("Git")

    # Clean Up Branches
    register_node(
        register_prompt,
        "prune-merged-branches",
        git_node,
        "Clean Up Branches",
        recursively=True,
    )

    # Resolve Merge Conflict
    register_node(
        register_prompt,
        "resolve-merge-conflict",
        git_node,
        "Resolve Merge Conflict",
        recursively=True,
    )

    # Feature Branch
    register_leaf(
        _register_internal,
        "git-feature-branch",
        ("Git",),
        "feature branch",
        display_name="Git Feature Branch",
    )

    # Open Pull Request
    register_node(
        register_prompt,
        "submit-pr",
        git_node,
        "Open Pull Request",
        recursively=True,
    )

    register_git_commit_sense_blueprints()


def _register_commit_sense_leaf(
    register_fn,
    slug,
    leaf_name,
    *,
    dependencies,
    extra_checkmarks=(),
    is_recursive=True,
    description_node=None,
    when_to_use_node=None,
    **register_kwargs,
):
    """
    register ``leaf_name`` under ``commit sense``, leaving the ``Git``
    heading out of the render

    :param extra_checkmarks: node paths checkmarked beside the leaf
    :type extra_checkmarks: tuple[tuple[str, ...], ...], optional
    :param is_recursive: whether the leaf takes every descendant; if not,
            only the descendants in ``extra_checkmarks`` render
    :type is_recursive: bool, optional
    :param description_node: node path of the skill description; ``None``
            keeps the default naming lookup
    :type description_node: tuple[str, ...], optional
    :param when_to_use_node: node path of the skill when-to-use text;
            ``None`` keeps the default naming lookup
    :type when_to_use_node: tuple[str, ...], optional
    """
    bp = create_blueprint(dependencies=dependencies)
    bp = checkmark_nodes(bp, _COMMIT_SENSE_PATH)
    for path in extra_checkmarks:
        bp = checkmark_nodes(bp, path)
    leaf_path = (*_COMMIT_SENSE_PATH, leaf_name)
    if is_recursive:
        bp = mark_as_leaf(bp, leaf_path)
    else:
        bp = checkmark_nodes(bp, leaf_path)
    meta_kwargs = {}
    if description_node is not None:
        meta_kwargs["description_node"] = description_node
    if when_to_use_node is not None:
        meta_kwargs["when_to_use_node"] = when_to_use_node
    register_fn(
        slug,
        replace_meta(bp, display_name=leaf_name, **meta_kwargs),
        **register_kwargs,
    )


def register_git_commit_sense_blueprints():
    """
    register the internal ``git-sense-*`` blueprints and the exportable
    ``commit-sense`` skill built on them

    a package building on the library may take the skill over with
    ``override_exportable("commit-sense", ...)``, building its own blueprint
    over the blueprint object ``get_blueprint("commit-sense").blueprint``
    """
    core_bp = create_blueprint()
    for path in (
        ("Elements", "ASCII only"),
        ("Elements", "Triage Tags"),
        ("Style Guide", "Letter Case", "Letter Case Commentary Case"),
        ("Style Guide", "Style Guide Briefness Style"),
        _COMMIT_SENSE_PATH,
    ):
        core_bp = checkmark_nodes(core_bp, path)
    _register_internal(
        "git-sense-core",
        replace_meta(core_bp, display_name="Git Sense Core"),
    )

    # the sigil leaf carries only the No Fit fallback: the Ordinary Edit
    # fallback is for the skill alone, added on its own blueprint below
    for slug, leaf_name, extra, is_recursive in (
        ("git-sense-primary-summary", "primary summary", (), True),
        (
            "git-sense-per-file-change-sigil",
            "per-file change sigil",
            (_NO_FIT_SIGIL_PATH,),
            False,
        ),
        ("git-sense-per-file-summary", "per-file summary", (), True),
    ):
        _register_commit_sense_leaf(
            _register_internal,
            slug,
            leaf_name,
            dependencies=["git-sense-core"],
            extra_checkmarks=extra,
            is_recursive=is_recursive,
        )

    # the skill itself, under the leaf's own descriptors
    commit_sense_path = (*_COMMIT_SENSE_PATH, "Perform Commit Sense")
    _register_commit_sense_leaf(
        register_exportable,
        "commit-sense",
        "Perform Commit Sense",
        dependencies=[
            "git-sense-primary-summary",
            "git-sense-per-file-change-sigil",
            "git-sense-per-file-summary",
        ],
        extra_checkmarks=(_ORDINARY_EDIT_SIGIL_PATH,),
        description_node=(*commit_sense_path, "{description}"),
        when_to_use_node=(*commit_sense_path, "{when_to_use}"),
    )

    # Dify prompts
    _register_internal(
        "git-sense-dify-primary",
        replace_meta(
            create_blueprint(dependencies=["git-sense-primary-summary"]),
            display_name="Git Sense Dify Primary",
        ),
    )
    per_file_bp = create_blueprint(
        dependencies=[
            "git-sense-per-file-change-sigil",
            "git-sense-per-file-summary",
        ]
    )
    per_file_bp = checkmark_nodes(
        per_file_bp, (*_COMMIT_SENSE_PATH, "Per-File Summary Task")
    )
    _register_internal(
        "git-sense-dify-per-file",
        replace_meta(per_file_bp, display_name="Git Sense Dify Per File"),
    )
