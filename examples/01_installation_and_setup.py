"""Example 01: Validate environment and configuration."""
from __future__ import annotations

import typer
from rich import print

from claude_api_python.client import ClaudeService
from claude_api_python.config import Settings
from claude_api_python.logging_utils import setup_logging

def main() -> None:
    """Validate local setup without performing a network call."""
    setup_logging()
    settings = Settings()
    print(f"[green]Loaded model:[/green] {settings.claude_model}")
    print("[green]Environment looks good. You can now run request-based examples.[/green]")


if __name__ == "__main__":
    typer.run(main)
