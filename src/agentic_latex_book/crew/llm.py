"""LLM resolution for real-mode runs only.

Reads provider/model from config and credentials from ``os.environ`` (no `.env`
auto-loading, no extra dependency). It never prints, logs, or returns the raw
API key. A CrewAI ``LLM`` object is constructed only when ``resolve_llm`` is
called — and even then nothing is sent to a model here.

Supported providers (offline-wired): ``openai`` and ``gemini`` (see D-018/D-020).
"""

from __future__ import annotations

import os

from agentic_latex_book.config import Config, require_model_config

_SUPPORTED_PROVIDERS = ("openai", "gemini")


class LLMConfigError(ValueError):
    """Raised when the LLM provider/model/environment is not usable for a run."""


def _provider(config: Config) -> str:
    return config.model_provider.strip().lower()


def _openai_key() -> str:
    return os.environ.get("OPENAI_API_KEY", "").strip()


def _openai_base_url() -> str:
    return os.environ.get("OPENAI_BASE_URL", "").strip()


def _gemini_key() -> str:
    """Gemini key from the environment. GEMINI_API_KEY takes precedence (it matches
    the ``gemini/`` provider prefix); GOOGLE_API_KEY is the documented fallback."""
    return (
        os.environ.get("GEMINI_API_KEY", "").strip() or os.environ.get("GOOGLE_API_KEY", "").strip()
    )


def _api_key_present(provider: str) -> bool:
    if provider == "openai":
        return bool(_openai_key())
    if provider == "gemini":
        return bool(_gemini_key())
    return False


def _base_url_present(provider: str) -> bool:
    # Only the OpenAI-compatible path supports a base_url; Gemini does not here.
    return provider == "openai" and bool(_openai_base_url())


def describe_llm_environment(config: Config) -> dict:
    """Return safe, non-secret metadata about the LLM configuration.

    Never includes raw key or base-url values — only presence booleans.
    """
    provider = _provider(config)
    return {
        "provider": config.model_provider,
        "model": config.model_name,
        "base_url_present": _base_url_present(provider),
        "api_key_present": _api_key_present(provider),
    }


def _openai_kwargs(config: Config) -> dict:
    base_url = _openai_base_url()
    key = _openai_key()
    if not base_url and not key:
        raise LLMConfigError(
            "Missing credentials: set OPENAI_API_KEY (external OpenAI) or "
            "OPENAI_BASE_URL (OpenAI-compatible local endpoint) in the environment."
        )
    kwargs = {"model": config.model_name}
    if base_url:
        kwargs["base_url"] = base_url
    if key:
        kwargs["api_key"] = key
    return kwargs


def _gemini_kwargs(config: Config) -> dict:
    key = _gemini_key()
    if not key:
        raise LLMConfigError(
            "Missing Gemini credentials: set GEMINI_API_KEY (preferred) or "
            "GOOGLE_API_KEY in the environment."
        )
    return {"model": config.model_name, "api_key": key}


def resolve_llm(config: Config):
    """Build and return a CrewAI ``LLM`` for a real run. Performs no model call.

    Raises LLMConfigError if the provider is unsupported, credentials are
    missing, or the provider's client package is not installed. The raw key is
    never logged or returned.
    """
    require_model_config(config)
    provider = _provider(config)
    if provider not in _SUPPORTED_PROVIDERS:
        raise LLMConfigError(
            f"Provider {config.model_provider!r} is not supported; "
            f"choose one of {_SUPPORTED_PROVIDERS}."
        )

    kwargs = _openai_kwargs(config) if provider == "openai" else _gemini_kwargs(config)

    from crewai import LLM

    try:
        return LLM(**kwargs)
    except ImportError as exc:
        # e.g. Gemini needs crewai[google-genai]; surface a safe, clear message.
        raise LLMConfigError(
            f"Provider {provider!r} client package is not installed: {exc}. "
            "Installing it is a Stage 8B dependency decision."
        ) from exc
