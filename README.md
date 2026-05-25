# Claude API Python: Beginner-to-Production Guide

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

**Author:** Chaitanya Dasadiya  
**Repository:** [https://github.com/cdasadiya/claude-api-playground](https://github.com/cdasadiya/claude-api-playground)  
**LinkedIn:** [https://www.linkedin.com/in/chaitanya-dasadiya](https://www.linkedin.com/in/chaitanya-dasadiya)

A production-oriented learning repository inspired by Real Python's Claude API tutorial, expanded with architecture, reliability, testing, and deployment workflows.

## 📚 Table of Contents

- [Features](#features)
- [Learning Roadmap](#learning-roadmap)
- [Quick Start](#quick-start)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Running Examples](#running-examples)
- [Testing](#testing)
- [Docker Deployment](#docker-deployment)
- [Development Tools](#development-tools)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Resources](#resources)
- [License](#license)

## ✨ Features

- **30 Standalone Examples** (`examples/01` → `examples/30`) covering beginner to advanced topics.
- **Reusable SDK Wrapper** (`ClaudeService`) with retries, validation, and typed usage helpers.
- **Config-Driven Setup** via `.env` + Pydantic settings for flexible configuration.
- **CI Pipeline** with lint + tests for continuous quality assurance.
- **Docker & Docker Compose Support** for containerized deployment.
- **Production Patterns** including error handling, logging, and resource management.
- **Comprehensive Testing** with network-free mocks for reliable unit tests.

## 🎓 Learning Roadmap

### Phase 1: Setup & Fundamentals (Examples 01–04)
- 01: Installation and Setup
- 02: Send your first Claude API request
- 03: Streaming responses
- 04: System prompts for behavior control

### Phase 2: Context & Advanced Patterns (Examples 05–10)
- 05: Manage rolling conversation history
- 06: Token usage tracking and accounting
- 07: Multimodal request payloads
- 08: Async requests with asyncio
- 09: Batch processing
- 10: Prompt templates for reusable instructions

### Phase 3: Reliability & Scaling (Examples 11–13)
- 11: Retry mechanism with tenacity
- 12: Rate limit handler and backoff strategy
- 13: Context window management

### Phase 4: Structured Outputs & Tools (Examples 14–22)
- 14: JSON mode and strict output parsing
- 15: Function calling patterns
- 16: RAG (Retrieval-Augmented Generation) pipeline
- 17: Embedding workflow architecture
- 18: PDF summarizer
- 19: Chatbot with persistent memory
- 20: Conversation manager with turn limits
- 21: Agentic workflows (planner/executor loops)
- 22: Tool use and selection examples

### Phase 5: Multimodal & Integration (Examples 23–30)
- 23: Image understanding
- 24: Audio transcription pipeline
- 25: Long-form document analysis
- 26: Code generation assistant
- 27: API wrapper and SDK patterns
- 28: FastAPI integration
- 29: Streamlit chatbot UI
- 30: Interactive CLI chat application

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- `pip` and `venv`
- An Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com))

### Installation

```bash
# Clone the repository
git clone https://github.com/cdasadiya/claude-api-playground.git
cd claude-api-playground

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install package with dev dependencies
pip install -e .[dev]

# Copy environment template
cp .env.example .env

# Add your ANTHROPIC_API_KEY to .env
# ANTHROPIC_API_KEY=your-key-here
```

### Run Your First Example

```bash
python examples/02_first_claude_request.py
```

## 🔧 Environment Variables

| Variable | Required | Default | Description |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | Yes | — | Your Anthropic API key |
| `CLAUDE_MODEL` | No | `claude-3-5-sonnet-latest` | Claude model identifier |
| `CLAUDE_MAX_TOKENS` | No | `512` | Maximum tokens in response |
| `REQUEST_TIMEOUT_SECONDS` | No | `45` | API request timeout in seconds |
| `LOG_LEVEL` | No | `INFO` | Logging level (DEBUG, INFO, WARNING, ERROR) |

### Example `.env` File

```bash
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxx
CLAUDE_MODEL=claude-3-5-sonnet-latest
CLAUDE_MAX_TOKENS=1024
REQUEST_TIMEOUT_SECONDS=60
LOG_LEVEL=INFO
```

## 📁 Project Structure

```
claude-api-playground/
├── README.md                          # This file
├── pyproject.toml                     # Project metadata and dependencies
├── .env.example                       # Environment template
├── .github/
│   └── workflows/
│       └── ci.yml                     # CI/CD pipeline
├── src/
│   └── claude_api_python/
│       ├── __init__.py
│       ├── client.py                  # ClaudeService wrapper
│       ├── config.py                  # Pydantic settings
│       ├── logging_utils.py           # Logging configuration
│       └── schemas.py                 # Pydantic models
├── examples/
│   ├── 01_installation_and_setup.py
│   ├── 02_first_claude_request.py
│   ├── ...
│   └── 30_cli_chat_application.py
├── tests/
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_client.py
│   └── test_schemas.py
├── Dockerfile
└── docker-compose.yml
```

## ▶️ Running Examples

### Run a Single Example

```bash
# Default prompt
python examples/02_first_claude_request.py

# Custom prompt
python examples/02_first_claude_request.py --prompt "What is machine learning?"
```

### Run All Examples

```bash
# Using bash
for i in {1..30}; do
  python examples/$(printf '%02d' $i)_*.py
done
```

### View Example Help

```bash
python examples/02_first_claude_request.py --help
```

## 🧪 Testing

### Run All Tests

```bash
pytest -v
```

### Run Specific Test File

```bash
pytest tests/test_client.py -v
```

### Run with Coverage

```bash
pytest --cov=src --cov-report=html
```

### Lint Code

```bash
ruff check src examples tests
```

### Format Code

```bash
ruff format src examples tests
```

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t claude-api-python:latest .
```

### Run Container

```bash
docker run --env-file .env claude-api-python:latest \
  python examples/02_first_claude_request.py
```

### Docker Compose (Recommended)

```bash
# Start services
docker-compose up --build

# Run an example
docker-compose exec app python examples/02_first_claude_request.py
```

## 🛠️ Development Tools

### Makefile Commands

```bash
make install      # Install dependencies
make test         # Run tests
make lint         # Lint code
make format       # Format code
make docker-build # Build Docker image
make clean        # Clean build artifacts
```

### Pre-commit Hooks (Optional)

```bash
pip install pre-commit
pre-commit install
```

## 🐛 Troubleshooting

### Issue: `ANTHROPIC_API_KEY not found`

**Solution:**
1. Create `.env` file from `.env.example`
2. Add your API key: `ANTHROPIC_API_KEY=sk-ant-...`
3. Verify with: `echo $ANTHROPIC_API_KEY`

### Issue: `ModuleNotFoundError: No module named 'claude_api_python'`

**Solution:**
```bash
pip install -e .
```

### Issue: Network timeout errors

**Solution:**
1. Increase timeout in `.env`:
   ```bash
   REQUEST_TIMEOUT_SECONDS=120
   ```
2. Check internet connection
3. Verify API key validity

### Issue: Rate limit errors (HTTP 429)

**Solution:**
- Use example 12 for rate limit handling
- Implement exponential backoff
- Reduce concurrent requests

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Commit changes**: `git commit -m "Add your feature"`
4. **Push to branch**: `git push origin feature/your-feature`
5. **Open a Pull Request**

### Code Standards
- Use `ruff` for linting and formatting
- Add tests for new features
- Follow PEP 8 conventions
- Include docstrings for functions and classes
- Update README if adding new examples

## 🔒 Security Best Practices

1. **Never commit `.env` file** to version control
2. **Rotate API keys** regularly
3. **Use environment variables** for secrets
4. **Validate user input** before passing to Claude API
5. **Monitor token usage** to prevent unexpected costs
6. **Implement rate limiting** for production applications
7. **Use HTTPS** for all API communications

## 📊 Token Usage & Cost Tracking

Example 06 demonstrates token usage tracking:

```python
response = service.ask(prompt="Your prompt")
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

### Cost Calculation

- **Input**: $3 per 1M tokens
- **Output**: $15 per 1M tokens

See [Anthropic Pricing](https://www.anthropic.com/pricing) for current rates.

## 📚 Additional Resources

- [Anthropic Documentation](https://docs.anthropic.com/)
- [Claude API Reference](https://docs.anthropic.com/claude/reference/)
- [Python SDK Repository](https://github.com/anthropics/anthropic-sdk-python)
- [Real Python Claude API Tutorial](https://realpython.com/)
- [Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)

## 🙏 Acknowledgments

This project is inspired by and builds upon:
- Real Python's comprehensive Claude API tutorial
- Anthropic's official documentation and SDKs
- Community best practices and patterns

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📮 Support

For issues, questions, or suggestions:

1. **Check existing issues** on GitHub
2. **Create a new issue** with detailed information
3. **Contact the author on LinkedIn**: [https://www.linkedin.com/in/chaitanya-dasadiya](https://www.linkedin.com/in/chaitanya-dasadiya)

---

**Happy coding!** 🚀

*Last updated: 2026-05-25*
