"""
kaye_library.registrations.chat.chat_bp.py

register the standalone chat base: a persona-free ``chat``, the
non-invokable ``chat-coder`` merging it with ``coder``, and the default
``secretary-email-authuser`` substitution

only ``setup_kaye_library_for_kaye_engine`` calls these, so a package
building on the library never sees any of them and supplies its own chat
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

from .._common import CONSUMER_NAME

__all__ = (
    "register_standalone_chat_blueprints",
    "register_standalone_dynamic_substitutions",
)

# the Agentic root, its Turn Progress Dispatch node, and the Chat Agent root
_CHAT_PATHS = (
    ("Agentic",),
    ("Agentic", "Turn Progress Dispatch"),
    ("Chat Agent",),
)


def register_standalone_dynamic_substitutions():
    """
    register the default ``secretary-email-authuser`` (account ``0``), the
    first signed-in Gmail account, so a standalone export leaves no
    placeholder behind
    """
    register_dynamic_substitution(
        "secretary-email-authuser", StringDynamicSubstitution("0")
    )


def register_standalone_chat_blueprints():
    """
    register ``chat`` and ``chat-coder``


    :raises KeyError: ``style-markdown``, ``coder`` or
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
    register_blueprint(
        "chat",
        replace_meta(
            bp,
            display_name="Chat",
            description="default for general conversation, with no persona",
        ),
        llm_invokable=False,
        always_apply=True,
        consumer=CONSUMER_NAME,
    )

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
