# Claude API Python: Beginner-to-Production Guide

A production-oriented learning repository inspired by Real Python's Claude API tutorial, expanded with architecture, reliability, testing, and deployment workflows.

## Features
- 30 standalone examples (`examples/01` → `examples/30`) covering beginner to advanced topics.
- Reusable SDK wrapper (`ClaudeService`) with retries, validation, and typed usage helpers.
- Config-driven setup via `.env` + Pydantic settings.
- CI pipeline with lint + tests.
- Docker and docker-compose support.

## Learning Roadmap
1. Setup and first requests (Examples 01–04)
2. Context, usage tracking, and templates (05–10)
3. Reliability + scaling patterns (11–13)
4. Structured outputs and tools (14–22)
5. Multimodal and app integrations (23–30)

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
python examples/02_first_claude_request.py
```

## Environment Variables
| Variable | Required | Default | Description |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | Yes | — | Anthropic API key |
| `CLAUDE_MODEL` | No | `claude-3-5-sonnet-latest` | Claude model name |
| `CLAUDE_MAX_TOKENS` | No | `512` | Max response tokens |
| `REQUEST_TIMEOUT_SECONDS` | No | `45` | API timeout |

## Testing
```bash
python -m compileall src examples tests
pytest -q
```

## Docker
```bash
docker compose up --build
```

## Project Structure
- `src/claude_api_python/`: library code.
- `examples/`: runnable scripts.
- `tests/`: unit tests (network-free via mocks).
- `.github/workflows/ci.yml`: CI checks.

## License
MIT
