"""Example 26: Code generation assistant prompt patterns."""
from __future__ import annotations

import typer
from rich import print

from claude_api_python.client import ClaudeService
from claude_api_python.config import Settings
from claude_api_python.logging_utils import setup_logging

def main(prompt: str = "Explain code generation assistant in Python with one practical tip.") -> None:
    """Code generation assistant prompt patterns."""
    setup_logging()
    service = ClaudeService(Settings())
    response = service.ask(prompt=prompt, system="You are a precise Python tutor.")
    print(response)


if __name__ == "__main__":
    typer.run(main)
