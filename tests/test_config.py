from claude_api_python.config import Settings


def test_settings_aliases(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "k")
    s = Settings()
    assert s.anthropic_api_key == "k"


def test_settings_defaults(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "k")
    s = Settings()
    assert s.claude_max_tokens > 0
    assert s.request_timeout_seconds > 0
