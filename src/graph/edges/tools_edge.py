"""Choose tools."""

from langgraph.graph import END

from ..enums import NodeName
from ..langgraph_state import State


def choose_tool(state: State) -> str:
    """
    Determine the appropriate tool to use based on the given state.

    Args:
        state (State): The current state containing messages and tool calls.

    Returns:
        str: The name of the tool to use or 'END' if no appropriate tool is found.
    """
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        tool_name = last_message.tool_calls[0]["name"]
        if tool_name == "about":
            return NodeName.ABOUT.value
    else:
        return END
