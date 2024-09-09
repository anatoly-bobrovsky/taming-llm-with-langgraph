"""Checker."""

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from env_settings import env

llm = ChatOpenAI(openai_api_key=env.OPENAI_API_KEY, model=env.OPENAI_MODEL, temperature=0)

template = """
Task: Determine which category the user's response belongs to: {options}. If the text cannot be classified, return "None".

Examples:

{examples}

User's response: "{user_response}"
Category:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["options", "examples", "user_response"],
)

checker_chain = prompt | llm
