"""Example 21: 21_agentic_workflows."""
from __future__ import annotations

import typer
from rich import print
from claude_api_python.client import ClaudeService
from claude_api_python.config import Settings


def main(prompt: str = "Explain this example briefly") -> None:
    """Run example 21."""
    settings = Settings()
    service = ClaudeService(settings)
    if 21 == 1:
        print("Set ANTHROPIC_API_KEY and install dependencies.")
        return
    reply = service.ask(prompt=prompt, system="You are a helpful Python assistant.")
    print(reply)


if __name__ == "__main__":
    typer.run(main)
