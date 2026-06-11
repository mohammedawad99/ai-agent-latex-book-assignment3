"""LLM resolution for real-mode runs only.

Reads provider/model from config and credentials from ``os.environ`` (no `.env`
auto-loading, no extra dependency). It never prints, logs, or returns the raw
API key. A CrewAI ``LLM`` object is constructed only when ``resolve_llm`` is
called — and even then nothing is sent to a model here.
"""

from __future__ import annotations

import os

from agentic_latex_book.config import Config, require_model_config

# Stage 8A supports the OpenAI / OpenAI-compatible path only (see D-018).
_SUPPORTED_PROVIDERS = ("openai",)


class LLMConfigError(ValueError):
    """Raised when the LLM provider/model/environment is not usable for a run."""


def _api_key_present() -> bool:
    return bool(os.environ.get("OPENAI_API_KEY", "").strip())


def _base_url() -> str:
    return os.environ.get("OPENAI_BASE_URL", "").strip()


def describe_llm_environment(config: Config) -> dict:
    """Return safe, non-secret metadata about the LLM configuration.

    Never includes raw key or base-url values — only presence booleans.
    """
    return {
        "provider": config.model_provider,
        "model": config.model_name,
        "base_url_present": bool(_base_url()),
        "api_key_present": _api_key_present(),
    }


def resolve_llm(config: Config):
    """Build and return a CrewAI ``LLM`` for a real run. Performs no model call.

    Raises LLMConfigError if the provider is unsupported or credentials are
    missing. The raw key is never logged or returned.
    """
    require_model_config(config)

    provider = config.model_provider.strip().lower()
    if provider not in _SUPPORTED_PROVIDERS:
        raise LLMConfigError(
            f"Provider {config.model_provider!r} is not supported in Stage 8A; "
            f"only {_SUPPORTED_PROVIDERS} (OpenAI / OpenAI-compatible) is available."
        )

    base_url = _base_url()
    # An OpenAI-compatible local endpoint may not need a real key; external
    # OpenAI does.
    if not base_url and not _api_key_present():
        raise LLMConfigError(
            "Missing credentials: set OPENAI_API_KEY (external OpenAI) or "
            "OPENAI_BASE_URL (OpenAI-compatible local endpoint) in the environment."
        )

    from crewai import LLM

    kwargs = {"model": config.model_name}
    if base_url:
        kwargs["base_url"] = base_url
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if api_key:
        kwargs["api_key"] = api_key
    return LLM(**kwargs)
