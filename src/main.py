"""Entrypoint."""

from uuid import uuid4

from langchain_core.messages import HumanMessage

from graph import compiled_graph


def get_response_from_bot(user_message: str, thread_id: str) -> str:
    """
    Get a response from the bot based on the user's message and thread ID.

    Args:
        user_message (str): The message from the user.
        thread_id (str): The thread ID to maintain conversation context.

    Returns:
        str: The bot's response message.
    """
    config = {"configurable": {"thread_id": thread_id}}

    final_state = compiled_graph.invoke(
        {"messages": [HumanMessage(content=user_message)]},
        config=config,
    )

    return final_state["messages"][-1].content


if __name__ == "__main__":
    print("BOT: Hi, I know all about cats!")
    thread_id = str(uuid4())  # create random thread ID

    while True:
        user_message = input("YOU: ")
        print(f"BOT: {get_response_from_bot(user_message=user_message, thread_id=thread_id)}")
