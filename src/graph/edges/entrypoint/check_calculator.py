"""Check calculator chain."""

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from env_settings import env

# LLM
llm = ChatOpenAI(openai_api_key=env.OPENAI_API_KEY, model=env.OPENAI_MODEL, temperature=0)

template = """
Please determine whether the following user query relates to the cost estimation of a single cat.

Return "Yes" or "No".

Examples:

User query: "I want to know how much a cat costs."
Answer: Yes

User query: "Tell me something about cats."
Answer: No

User query: {user_query}
Answer:
"""

# Prompt
prompt = PromptTemplate(
    template=template,
    input_variables=["user_query"],
)

# Chain
check_calculator_chain = prompt | llm
