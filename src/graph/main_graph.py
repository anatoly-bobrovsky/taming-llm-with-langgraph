"""Main graph."""

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from .edges import choose_tool
from .enums import NodeName
from .langgraph_state import State
from .nodes import call_chat_bot
from .tools import call_tool

# Define a new graph
workflow = StateGraph(State)

# add nodes
workflow.add_node(NodeName.CHAT_BOT.value, call_chat_bot)
workflow.add_node(NodeName.ABOUT.value, call_tool)

# add edges
workflow.add_edge(START, NodeName.CHAT_BOT.value)
workflow.add_conditional_edges(
    NodeName.CHAT_BOT.value,
    choose_tool,
)
workflow.add_edge(NodeName.ABOUT.value, END)

compiled_graph = workflow.compile(checkpointer=MemorySaver())
