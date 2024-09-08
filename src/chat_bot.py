"""Chat bot."""

from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from env_settings import env

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
        MessagesPlaceholder("history"),  # we'll add the memory in the following steps
    ]
)

chat_bot_chain = prompt | llm
