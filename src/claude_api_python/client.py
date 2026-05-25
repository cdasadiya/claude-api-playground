from __future__ import annotations

import anthropic
from tenacity import retry, stop_after_attempt, wait_exponential

from .config import Settings


class ClaudeService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

    @retry(wait=wait_exponential(min=1, max=8), stop=stop_after_attempt(3), reraise=True)
    def ask(self, prompt: str, system: str | None = None) -> str:
        response = self.client.messages.create(
            model=self.settings.claude_model,
            max_tokens=self.settings.claude_max_tokens,
            system=system,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text if response.content else ""
