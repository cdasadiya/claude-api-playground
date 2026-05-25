from claude_api_python.config import Settings


def test_settings_aliases(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "k")
    s = Settings()
    assert s.anthropic_api_key == "k"
