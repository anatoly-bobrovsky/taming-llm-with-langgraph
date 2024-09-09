"""Utils."""


from langchain_core.messages import HumanMessage

from .langgraph_state import State


def get_last_human_message(state: State) -> str:
    """
    Retrieve the content of the last human message from the conversation state.

    Args:
        state (State): The current state of the conversation.

    Returns:
        str: The content of the last human message.
    """
    messages = state["messages"]
    for message in reversed(messages):
        if isinstance(message, HumanMessage):
            return message.content
