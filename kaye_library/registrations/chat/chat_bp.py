"""
kaye_library.registrations.chat.chat_bp.py

register the chat stack in every setup: ``chat-basic``, ``chat`` (both
persona-free), ``chat-basic-kaye`` and ``chat-kaye``, the last over the
public Kaye persona; a package replaces ``chat`` in place with
``override_blueprint`` and re-homes ``chat-kaye``; and, for the standalone
setup alone, the default ``secretary-email-authuser`` substitution
"""

from kaye_engine import (
    StringDynamicSubstitution,
    register_dynamic_substitution,
)
from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
    replace_meta,
)

from kaye_engine.prompt.blueprint.render_profile import RenderProfile

from .._common import (
    SIDECAR_FOR_KAYE,
    SIDECAR_IN_CHAT,
    register_exportable,
    register_internal,
)

__all__ = (
    "register_chat_blueprints",
    "register_standalone_dynamic_substitutions",
)

# the Agentic root and its Turn Progress Dispatch node
_CHAT_PATHS = (
    ("Agentic",),
    ("Agentic", "Turn Progress Dispatch"),
)

# the Chat Agent root, whose every section the chat takes
_CHAT_AGENT_PATH = ("Chat Agent",)

# every chat blueprint describes itself by the Chat Agent's own sidecars
_CHAT_META = {
    "description_node": ("Chat Agent", "{description}"),
    "when_to_use_node": ("Chat Agent", "{when_to_use}"),
}


def register_standalone_dynamic_substitutions():
    """
    register the default ``secretary-email-authuser`` (account ``0``), the
    first signed-in Gmail account, so a standalone export leaves no
    placeholder behind
    """
    register_dynamic_substitution(
        "secretary-email-authuser", StringDynamicSubstitution("0")
    )


def register_chat_blueprints():
    """
    register the chat stack:

    - ``chat-basic``: the Agentic and Chat Agent rules, Markdown and chat
      sequence numbering, persona-free
    - ``chat``: ``chat-basic`` alone, the name a package replaces in place
      with its fuller conversation rules
    - ``chat-basic-kaye``: ``chat-basic`` over the public Kaye persona, the
      Hermes root soul
    - ``chat-kaye``: ``chat`` over the public Kaye persona, the default
      skill, always applied


    :raises KeyError: ``style-markdown``, ``persona`` or
            ``element-alphabetical-sequence-numbering-in-chat`` is not yet
            registered
    """
    bp = create_blueprint(
        dependencies=[
            "style-markdown",
            "element-alphabetical-sequence-numbering-in-chat",
        ]
    )
    for path in _CHAT_PATHS:
        bp = checkmark_nodes(bp, path)
    bp = checkmark_nodes(bp, _CHAT_AGENT_PATH, is_recursive=True)
    register_internal(
        "chat-basic",
        replace_meta(bp, display_name="Chat Basic", **_CHAT_META),
        llm_invokable=False,
    )

    register_internal(
        "chat",
        replace_meta(
            create_blueprint(dependencies=["chat-basic"]),
            display_name="Chat",
            **_CHAT_META,
        ),
        llm_invokable=False,
    )

    kaye_profile = RenderProfile(
        conditional_sidecars=(SIDECAR_FOR_KAYE, SIDECAR_IN_CHAT)
    )
    register_internal(
        "chat-basic-kaye",
        replace_meta(
            create_blueprint(dependencies=["chat-basic", "persona"]),
            display_name="Chat Basic Kaye",
            **_CHAT_META,
        ),
        render_profile=kaye_profile,
        llm_invokable=False,
    )

    register_exportable(
        "chat-kaye",
        replace_meta(
            create_blueprint(dependencies=["chat", "persona"]),
            display_name="Chat Kaye",
            **_CHAT_META,
        ),
        render_profile=kaye_profile,
        llm_invokable=False,
        always_apply=True,
    )
