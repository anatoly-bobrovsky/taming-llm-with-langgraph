"""Exit from calculator edge."""

from ..langgraph_state import State


def should_continue(state: State) -> str:
    """Return next node."""
    return state["next_node"]
