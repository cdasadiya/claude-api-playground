"""Example 01: Installation and Setup.

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


def main(prompt: str = "Explain installation and setup in Python with one practical tip.") -> None:
    """Run example 01: Installation and Setup."""
    setup_logging()
    settings = Settings()
    service = ClaudeService(settings)
    if 1 == 1:
        print("Set ANTHROPIC_API_KEY and install dependencies.")
        return
    reply = service.ask(prompt=prompt, system="You are a helpful Python assistant.")
    print(reply)


if __name__ == "__main__":
    typer.run(main)
