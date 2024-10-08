"""Langgraph State."""

from typing import Annotated, Any

from langgraph.graph.message import AnyMessage, add_messages
from typing_extensions import TypedDict


class State(TypedDict):
    """
    Represents the state of the Langgraph, containing a list of messages.

    Attributes:
        messages (list[AnyMessage]): A list of messages with additional metadata added by `add_messages`.
    """

    messages: Annotated[list[AnyMessage], add_messages]
    next_node: str
    should_continue_data: Any

    gender: str
    breed: str
