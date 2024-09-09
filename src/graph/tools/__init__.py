"""Tools Package."""

from langgraph.prebuilt import ToolNode

from .about_tool import about

all_tools = [about]
call_tool = ToolNode(all_tools)
