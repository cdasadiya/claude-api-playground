from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    anthropic_api_key: str = Field(alias="ANTHROPIC_API_KEY")
    claude_model: str = Field(default="claude-sonnet-4-6", alias="CLAUDE_MODEL")
    claude_max_tokens: int = Field(default=512, alias="CLAUDE_MAX_TOKENS")

    class Config:
        env_file = ".env"
        extra = "ignore"
