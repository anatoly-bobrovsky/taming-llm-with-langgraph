"""About tool."""

from langchain_core.tools import StructuredTool


def get_about_message(query: str) -> str:
    """
    Generate an 'about' message.

    Args:
        query (str): The input query string.

    Returns:
        str: A formatted 'about' message string.
    """
    return "I am a cat expert from 'Cats Inc.'. How can I help?"


about = StructuredTool.from_function(
    func=get_about_message,
    name="about",
    description="Useful when you are asked to tell what you can do",
    return_direct=True,
)
