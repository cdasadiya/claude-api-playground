# Claude API Python: Beginner-to-Production Guide

Production-ready companion project inspired by Real Python's "How to Use the Claude API in Python" article.

## What this repo includes
- Article coverage: setup, first prompt, system prompts, structured JSON with schema/Pydantic, troubleshooting.
- Expanded production topics: retries, timeouts, structured logging, cost tracking, FastAPI, Streamlit, CLI, testing.
- 30 runnable examples under `examples/`.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
python examples/02_first_claude_request.py --prompt "What is the Zen of Python?"
```

## Structure
- `src/claude_api_python/`: reusable SDK wrapper and utilities.
- `examples/`: standalone scripts mapped to concepts.
- `tests/`: unit tests for config, schema parsing, and safeguards.
- `.github/workflows/ci.yml`: lint + test pipeline.

## Notes
- Requires `ANTHROPIC_API_KEY` in environment.
- Examples are safe to run independently.
