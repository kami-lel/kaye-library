"""
kaye_library.registrations.chat.chat_bp.py

register ``chat``, the conversation rules over the public Kaye persona,
in every setup, so a package takes it over with ``override_exportable``;
and, for the standalone setup alone, the non-invokable ``chat-coder``
merging it with ``coder`` and the default ``secretary-email-authuser``
substitution
"""

from kaye_engine import (
    StringDynamicSubstitution,
    register_blueprint,
    register_dynamic_substitution,
)
from kaye_engine.prompt.blueprint import (
    checkmark_nodes,
    create_blueprint,
    get_blueprint,
    replace_meta,
)

from kaye_engine.prompt.blueprint.render_profile import RenderProfile

from .._common import CONSUMER_NAME, SIDECAR_FOR_KAYE

__all__ = (
    "register_chat_blueprints",
    "register_standalone_chat_blueprints",
    "register_standalone_dynamic_substitutions",
)

# the Agentic root and its Turn Progress Dispatch node
_CHAT_PATHS = (
    ("Agentic",),
    ("Agentic", "Turn Progress Dispatch"),
)

# the Chat Agent root, whose every section the chat takes
_CHAT_AGENT_PATH = ("Chat Agent",)


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
    register ``chat``: the conversation rules over the public Kaye persona,
    rendering Kaye's own sections


    :raises KeyError: ``style-markdown``, ``persona-kaye`` or
            ``element-alphabetical-sequence-numbering-in-chat`` is not yet
            registered
    """
    bp = create_blueprint(
        dependencies=[
            "style-markdown",
            "element-alphabetical-sequence-numbering-in-chat",
            "persona-kaye",
        ]
    )
    for path in _CHAT_PATHS:
        bp = checkmark_nodes(bp, path)
    bp = checkmark_nodes(bp, _CHAT_AGENT_PATH, is_recursive=True)
    register_blueprint(
        "chat",
        replace_meta(
            bp,
            display_name="Chat",
            description_node=("Chat Agent", "{description}"),
            when_to_use_node=("Chat Agent", "{when_to_use}"),
        ),
        render_profile=RenderProfile(conditional_sidecars=(SIDECAR_FOR_KAYE,)),
        llm_invokable=False,
        always_apply=True,
        consumer=CONSUMER_NAME,
    )


def register_standalone_chat_blueprints():
    """
    register ``chat-coder``, for the standalone setup alone


    :raises KeyError: ``chat`` or ``coder`` is not yet registered
    """
    # the library's own coder enters by object, so the pair stays acyclic
    coder = get_blueprint("coder")
    coder_meta = coder.blueprint.meta
    register_blueprint(
        "chat-coder",
        replace_meta(
            create_blueprint(dependencies=["chat", coder.blueprint]),
            display_name="Chat Coder",
            description_node=coder_meta.description_node,
            when_to_use_node=coder_meta.when_to_use_node,
        ),
        is_user_invokable=False,
        llm_invokable=False,
        consumer=CONSUMER_NAME,
    )
