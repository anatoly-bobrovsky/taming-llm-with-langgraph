"""Chat bot."""

from langchain_core.messages import AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from env_settings import env

from ..langgraph_state import State
from ..tools import all_tools

llm = ChatOpenAI(openai_api_key=env.OPENAI_API_KEY, model=env.OPENAI_MODEL, temperature=0)

system_message = SystemMessage(
    content="""
You are a cat expert with extensive knowledge in feline behavior, health, and care.
You have years of experience working with different breeds of cats, understanding their unique personalities and needs.
You can provide detailed advice on everything from feeding and grooming to health issues and training.
When answering questions, offer practical, evidence-based advice, and explain your reasoning clearly.
"""
)

prompt = ChatPromptTemplate.from_messages(
    [
        system_message,
        MessagesPlaceholder("history"),
    ]
)


def call_chat_bot(state: State) -> dict[str, list[AIMessage]]:
    """
    Call the chat bot with the given state and returns the response.

    Args:
        state (State): The current state containing messages.

    Returns:
        dict[str, list[AIMessage]]: A dictionary containing the AI message as the response.
    """
    llm_with_tools = llm.bind_tools(all_tools)
    chat_bot_chain = prompt | llm_with_tools
    response = chat_bot_chain.invoke({"history": state["messages"]})
    return {"messages": [response]}
