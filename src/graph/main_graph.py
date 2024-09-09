"""Main graph."""

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from .edges import choose_tool, conditional_entry_point, should_continue
from .enums import NodeName
from .langgraph_state import State
from .nodes import (
    ask_human,
    breed_node,
    call_chat_bot,
    gender_node,
    should_continue_node,
    start_calculator,
    start_node,
    weight_node,
)
from .tools import call_tool

# Define a new graph
workflow = StateGraph(State)

# add nodes
workflow.add_node(NodeName.START.value, start_node)
workflow.add_node(NodeName.CHAT_BOT.value, call_chat_bot)
workflow.add_node(NodeName.ABOUT.value, call_tool)

workflow.add_node(NodeName.START_CALCULATOR.value, start_calculator)
workflow.add_node(NodeName.GENDER.value, gender_node)
workflow.add_node(NodeName.BREED.value, breed_node)
workflow.add_node(NodeName.WEIGHT.value, weight_node)

workflow.add_node(NodeName.ASK_HUMAN.value, ask_human)
workflow.add_node(NodeName.SHOULD_CONTINUE_NODE.value, should_continue_node)

# add edges
workflow.add_edge(START, NodeName.START.value)
workflow.add_conditional_edges(
    NodeName.START.value,
    conditional_entry_point,
)

workflow.add_conditional_edges(
    NodeName.CHAT_BOT.value,
    choose_tool,
)
workflow.add_edge(NodeName.ABOUT.value, END)

workflow.add_edge(NodeName.START_CALCULATOR.value, NodeName.ASK_HUMAN.value)
workflow.add_edge(NodeName.GENDER.value, NodeName.ASK_HUMAN.value)
workflow.add_edge(NodeName.BREED.value, NodeName.ASK_HUMAN.value)
workflow.add_edge(NodeName.WEIGHT.value, NodeName.ASK_HUMAN.value)
workflow.add_edge(NodeName.ASK_HUMAN.value, NodeName.SHOULD_CONTINUE_NODE.value)
workflow.add_conditional_edges(
    NodeName.SHOULD_CONTINUE_NODE.value,
    should_continue,
)

compiled_graph = workflow.compile(
    checkpointer=MemorySaver(),
    interrupt_before=[NodeName.ASK_HUMAN.value],
)
