"""Example 10: Use prompt templates for reusable instructions.

Author: Chaitanya Dasadiya
Repository: https://github.com/cdasadiya/claude-api-playground
License: MIT
"""
from __future__ import annotations

import typer
from rich import print

from claude_api_python.client import ClaudeService
from claude_api_python.config import Settings
from claude_api_python.logging_utils import setup_logging


def main(prompt: str = "Explain prompt templates in Python with one practical tip.") -> None:
    """Use prompt templates for reusable instructions."""
    setup_logging()
    service = ClaudeService(Settings())
    response = service.ask(prompt=prompt, system="You are a precise Python tutor.")
    print(response)


if __name__ == "__main__":
    typer.run(main)
