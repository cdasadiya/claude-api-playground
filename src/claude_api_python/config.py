"""Application configuration with graceful fallback when optional deps are missing."""

from __future__ import annotations

import os

try:
    from pydantic import Field
    from pydantic_settings import BaseSettings, SettingsConfigDict

    class Settings(BaseSettings):
        anthropic_api_key: str = Field(alias="ANTHROPIC_API_KEY")
        claude_model: str = Field(default="claude-3-5-sonnet-latest", alias="CLAUDE_MODEL")
        claude_max_tokens: int = Field(default=512, alias="CLAUDE_MAX_TOKENS", ge=1, le=8192)
        request_timeout_seconds: float = Field(default=45.0, alias="REQUEST_TIMEOUT_SECONDS", gt=0)

        model_config = SettingsConfigDict(env_file=".env", extra="ignore")

except ImportError:  # pragma: no cover
    class Settings:  # type: ignore[override]
        def __init__(self) -> None:
            self.anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY", "")
            self.claude_model = os.environ.get("CLAUDE_MODEL", "claude-3-5-sonnet-latest")
            self.claude_max_tokens = int(os.environ.get("CLAUDE_MAX_TOKENS", "512"))
            self.request_timeout_seconds = float(os.environ.get("REQUEST_TIMEOUT_SECONDS", "45"))
            if not self.anthropic_api_key:
                raise ValueError("ANTHROPIC_API_KEY is required")
