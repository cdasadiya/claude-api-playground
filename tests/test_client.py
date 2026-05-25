from __future__ import annotations

import types

from claude_api_python.client import ClaudeService
from claude_api_python.config import Settings


class _FakeResponse:
    def __init__(self, text: str) -> None:
        self.content = [types.SimpleNamespace(text=text)]


class _FakeMessages:
    def create(self, **_: object) -> _FakeResponse:
        return _FakeResponse("ok")


class _FakeAnthropicClient:
    def __init__(self, **_: object) -> None:
        self.messages = _FakeMessages()


def test_ask_returns_text(monkeypatch):
    fake_mod = types.SimpleNamespace(Anthropic=_FakeAnthropicClient)
    monkeypatch.setitem(__import__("sys").modules, "anthropic", fake_mod)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    service = ClaudeService(Settings())
    assert service.ask("hello") == "ok"


def test_ask_rejects_empty_prompt(monkeypatch):
    fake_mod = types.SimpleNamespace(Anthropic=_FakeAnthropicClient)
    monkeypatch.setitem(__import__("sys").modules, "anthropic", fake_mod)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    service = ClaudeService(Settings())
    try:
        service.ask("   ")
    except ValueError as exc:
        assert "must not be empty" in str(exc)
    else:
        raise AssertionError("Expected ValueError")
