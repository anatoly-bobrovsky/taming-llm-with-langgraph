"""Env Settings."""

from pydantic_settings import BaseSettings


class EnvSettings(BaseSettings):
    """Class for environment."""

    # OpenAI
    OPENAI_API_KEY: str
    OPENAI_MODEL: str


env = EnvSettings()
