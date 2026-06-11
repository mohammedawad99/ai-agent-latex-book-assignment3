"""Tests for LLM config resolution. Offline: no model is ever called."""

from __future__ import annotations

import pytest

from agentic_latex_book.config import (
    ConfigError,
    is_model_configured,
    load_config,
    require_model_config,
)
from agentic_latex_book.crew.llm import (
    LLMConfigError,
    describe_llm_environment,
    resolve_llm,
)

_CONFIG_TEMPLATE = """\
[project]
topic = "Test topic"
group_code = "MaRs-777"

[paths]
latex_project = "latex_project"
results = "results"
logs = "results/logs"
crew_outputs = "results/crew_outputs"
validation_reports = "results/validation_reports"
final_pdf = "results/final_pdf"
assets_generated = "assets/generated"
assets_figures = "assets/figures"

[pdf]
page_count_min = 13
page_count_max = 17

[model]
provider = "{provider}"
name = "{name}"

[cost]
tracking_enabled = true
"""


def _config(tmp_path, provider, name):
    path = tmp_path / "config.toml"
    path.write_text(_CONFIG_TEMPLATE.format(provider=provider, name=name), encoding="utf-8")
    return load_config(path)


def test_is_model_configured_false_for_placeholders() -> None:
    assert is_model_configured(load_config()) is False


def test_is_model_configured_true_when_set(tmp_path) -> None:
    assert is_model_configured(_config(tmp_path, "openai", "gpt-4o-mini")) is True


def test_require_model_config_raises_on_placeholders() -> None:
    with pytest.raises(ConfigError):
        require_model_config(load_config())


def test_describe_environment_hides_raw_secret(tmp_path, monkeypatch) -> None:
    """The environment description exposes booleans only, never the raw key."""
    monkeypatch.setenv("OPENAI_API_KEY", "FAKEKEY-DO-NOT-LOG")
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    meta = _config_env_describe(tmp_path)
    assert meta["api_key_present"] is True
    assert "FAKEKEY-DO-NOT-LOG" not in str(meta)
    assert meta["provider"] == "openai"


def _config_env_describe(tmp_path):
    return describe_llm_environment(_config(tmp_path, "openai", "gpt-4o-mini"))


def test_resolve_llm_fails_without_model() -> None:
    with pytest.raises(ConfigError):
        resolve_llm(load_config())


def test_resolve_llm_rejects_unsupported_provider(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "FAKEKEY")
    with pytest.raises(LLMConfigError):
        resolve_llm(_config(tmp_path, "anthropic", "claude-x"))


def test_resolve_llm_fails_without_credentials(tmp_path, monkeypatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    with pytest.raises(LLMConfigError):
        resolve_llm(_config(tmp_path, "openai", "gpt-4o-mini"))
