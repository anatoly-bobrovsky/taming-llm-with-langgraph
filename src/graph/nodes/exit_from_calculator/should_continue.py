"""Main node."""

from ...enums import NodeName
from ...langgraph_state import State
from .checker import checker_chain


def should_continue_node(state: State):
    """
    Determine whether the conversation should continue based on the last user message and the next node.

    Args:
        state (State): The current state of the conversation.

    Returns:
        dict or None: A dictionary containing the next node and any data needed to continue the conversation,
                      or None if no continuation is needed.
    """
    last_message = state["messages"][-1].content.lower()

    if state["next_node"] in (
        NodeName.START.value,
        NodeName.BREED.value,
    ):
        return

    elif state["next_node"] == NodeName.GENDER.value:
        prompt_examples = """
        User's response: "boy"
        Category: male

        User's response: "tell me about yourself"
        Category: None

        User's response: "girl"
        Category: female
        """

        result = checker_chain.invoke(
            {"options": "female, male", "examples": prompt_examples, "user_response": last_message}
        )
        if result.content != "None":
            return {"should_continue_data": result.content}

    elif state["next_node"] == NodeName.WEIGHT.value:
        if last_message.isdigit():
            return {"should_continue_data": int(last_message)}

    return {
        "next_node": NodeName.START.value,
        "should_continue_data": None,
    }
