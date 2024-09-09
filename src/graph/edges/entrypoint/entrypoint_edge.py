"""Entry point edge."""

from ...enums import NodeName
from ...langgraph_state import State
from ...utils import get_last_human_message
from .check_calculator import check_calculator_chain


def conditional_entry_point(state: State) -> str:
    """
    Determine the entry point based on the user's last message and a calculator check.

    Args:
        state (State): The current state of the conversation.

    Returns:
        str: Returns the entry point node name. If the last user message indicates a calculator query,
             it returns the start calculator node name; otherwise, it returns the chat bot node name.
    """
    user_query = get_last_human_message(state)
    if user_query:
        checking_calculator_result = check_calculator_chain.invoke({"user_query": user_query})
        if checking_calculator_result.content.lower() == "yes":
            return NodeName.START_CALCULATOR.value

    return NodeName.CHAT_BOT.value
