"""Calculator nodes."""


from langchain_core.messages import AIMessage

from calculator import get_cat_cost

from ..enums import NodeName
from ..langgraph_state import State


def ask_human(state: State):
    """Fake node to ask the human."""
    pass


def start_calculator(state: State):
    """
    Initiate the calculator process by asking for the cat's gender.

    Args:
        state (State): The current state of the conversation.

    Returns:
        dict: A dictionary containing the next message and the next node name.
    """
    next_node = NodeName.GENDER.value
    next_message = "What is your cat's gender?"

    return {
        "messages": [AIMessage(content=next_message)],
        "next_node": next_node,
    }


def gender_node(state: State):
    """
    Process the gender input and asks for the cat's breed.

    Args:
        state (State): The current state of the conversation.

    Returns:
        dict: A dictionary containing the gender, the next message, and the next node name.
    """
    next_node = NodeName.BREED.value
    next_message = "What is your cat's breed?"

    return {
        "gender": state["should_continue_data"],
        "messages": [AIMessage(content=next_message)],
        "next_node": next_node,
    }


def breed_node(state: State):
    """
    Process the breed input and asks for the cat's weight.

    Args:
        state (State): The current state of the conversation.

    Returns:
        dict: A dictionary containing the breed, the next message, and the next node name.
    """
    last_message = state["messages"][-1].content.lower()

    next_node = NodeName.WEIGHT.value
    next_message = "What is the weight of your cat in kilograms?"

    return {
        "breed": last_message,
        "messages": [AIMessage(content=next_message)],
        "next_node": next_node,
    }


def weight_node(state: State):
    """
    Process the weight input and calculates the cost of the cat.

    Args:
        state (State): The current state of the conversation.

    Returns:
        dict: A dictionary containing the final message with the cat's cost and the next node name.
    """
    cost = get_cat_cost(gender=state["gender"], breed=state["breed"], weight_kg=state["should_continue_data"])

    next_node = NodeName.START.value
    next_message = f"Your cat is worth {cost} dollars"

    return {
        "messages": [AIMessage(content=next_message)],
        "next_node": next_node,
    }
