"""Shared schemas."""

from __future__ import annotations

try:
    from pydantic import BaseModel, Field

    class PythonTip(BaseModel):
        title: str = Field(description="Short title")
        explanation: str = Field(description="Detailed explanation")
        example: str = Field(description="Python code snippet")

    class TokenUsage(BaseModel):
        input_tokens: int = Field(default=0, ge=0)
        output_tokens: int = Field(default=0, ge=0)

        @property
        def total_tokens(self) -> int:
            return self.input_tokens + self.output_tokens

except ImportError:  # pragma: no cover
    from dataclasses import dataclass

    @dataclass
    class PythonTip:
        title: str
        explanation: str
        example: str

    @dataclass
    class TokenUsage:
        input_tokens: int = 0
        output_tokens: int = 0

        @property
        def total_tokens(self) -> int:
            return self.input_tokens + self.output_tokens
