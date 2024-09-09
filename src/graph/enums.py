"""Langgraph enums."""

from enum import Enum


class NodeName(Enum):
    """Node name."""

    START = "start"
    CHAT_BOT = "chat_bot"
    ABOUT = "about"

    ASK_HUMAN = "ask_human"
    SHOULD_CONTINUE_NODE = "should_continue_node"

    # calculator nodes
    START_CALCULATOR = "start_calculator"
    GENDER = "gender_node"
    BREED = "breed_node"
    WEIGHT = "weight"
