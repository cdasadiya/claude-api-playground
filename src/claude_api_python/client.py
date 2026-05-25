from __future__ import annotations

import json
import uuid
from typing import Any

try:
    from tenacity import retry, stop_after_attempt, wait_exponential
except ImportError:  # pragma: no cover
    def retry(*args, **kwargs):
        def _wrap(func):
            return func
        return _wrap

    def stop_after_attempt(_n):
        return None

    def wait_exponential(**_kwargs):
        return None

from .config import Settings
from .schemas import TokenUsage


class ClaudeService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        try:
            import anthropic
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("anthropic package is required. Install project dependencies first.") from exc
        self.client = anthropic.Anthropic(api_key=settings.anthropic_api_key, timeout=settings.request_timeout_seconds)

    @retry(wait=wait_exponential(min=1, max=8), stop=stop_after_attempt(3), reraise=True)
    def ask(self, prompt: str, system: str | None = None, max_tokens: int | None = None) -> str:
        if not prompt.strip():
            raise ValueError("prompt must not be empty")
        _ = str(uuid.uuid4())
        response = self.client.messages.create(
            model=self.settings.claude_model,
            max_tokens=max_tokens or self.settings.claude_max_tokens,
            system=system,
            messages=[{"role": "user", "content": prompt}],
        )
        return self._extract_text(response)

    def ask_json(self, prompt: str, schema: dict[str, Any], system: str | None = None) -> dict[str, Any]:
        text = self.ask(
            prompt=f"Return ONLY JSON matching schema {json.dumps(schema)}. Request: {prompt}",
            system=system,
        )
        return json.loads(text)

    def usage_from_response(self, response: Any) -> TokenUsage:
        usage = getattr(response, "usage", None)
        return TokenUsage(getattr(usage, "input_tokens", 0) if usage else 0, getattr(usage, "output_tokens", 0) if usage else 0)

    @staticmethod
    def _extract_text(response: Any) -> str:
        blocks = []
        for block in getattr(response, "content", []) or []:
            text = getattr(block, "text", "")
            if text:
                blocks.append(text)
        return "\n".join(blocks).strip()
