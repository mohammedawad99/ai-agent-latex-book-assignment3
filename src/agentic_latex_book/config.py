"""Project configuration loader.

Loads the non-secret TOML configuration (``config/default.toml`` by default)
into a structured object and validates the parts Stage 6 depends on. Secrets are
never read from here; they come from the environment.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

from agentic_latex_book.paths import repo_paths


class ConfigError(ValueError):
    """Raised when the configuration is missing, malformed, or invalid."""


# Path keys that must be present and non-empty in the [paths] section.
REQUIRED_PATH_KEYS = (
    "latex_project",
    "results",
    "logs",
    "crew_outputs",
    "validation_reports",
    "final_pdf",
    "assets_generated",
    "assets_figures",
)


@dataclass(frozen=True)
class Config:
    """Structured view of the project configuration."""

    topic: str
    group_code: str
    paths: dict[str, str]
    page_count_min: int
    page_count_max: int
    model_provider: str
    model_name: str
    cost_tracking_enabled: bool
    source_path: Path


def _require_section(data: dict, name: str) -> dict:
    section = data.get(name)
    if not isinstance(section, dict):
        raise ConfigError(f"Missing or invalid [{name}] section in config.")
    return section


def _require_str(section: dict, key: str, where: str) -> str:
    value = section.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ConfigError(f"Config key [{where}].{key} must be a non-empty string.")
    return value


def _validate_paths(paths: dict) -> dict[str, str]:
    """Validate the required path keys and return them as a string mapping."""
    validated: dict[str, str] = {}
    for key in REQUIRED_PATH_KEYS:
        if key not in paths:
            raise ConfigError(f"Missing required [paths] key: {key}.")
        validated[key] = _require_str(paths, key, "paths")
    return validated


def load_config(path: Path | None = None) -> Config:
    """Load and validate the configuration. Raises ConfigError on any problem."""
    config_path = path if path is not None else repo_paths().default_config
    if not config_path.is_file():
        raise ConfigError(f"Config file not found: {config_path}")

    try:
        with config_path.open("rb") as handle:
            data = tomllib.load(handle)
    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(f"Could not parse TOML config {config_path}: {exc}") from exc

    project = _require_section(data, "project")
    paths = _require_section(data, "paths")
    pdf = _require_section(data, "pdf")
    model = _require_section(data, "model")
    cost = _require_section(data, "cost")

    page_min = pdf.get("page_count_min")
    page_max = pdf.get("page_count_max")
    if not isinstance(page_min, int) or not isinstance(page_max, int):
        raise ConfigError("[pdf].page_count_min/max must be integers.")
    if page_min <= 0 or page_max < page_min:
        raise ConfigError("[pdf] page counts must satisfy 0 < min <= max.")

    tracking = cost.get("tracking_enabled")
    if not isinstance(tracking, bool):
        raise ConfigError("[cost].tracking_enabled must be a boolean.")

    return Config(
        topic=_require_str(project, "topic", "project"),
        group_code=_require_str(project, "group_code", "project"),
        paths=_validate_paths(paths),
        page_count_min=page_min,
        page_count_max=page_max,
        # Provider/name are placeholders in Stage 5/6 and may be empty (see D-014).
        model_provider=str(model.get("provider", "")),
        model_name=str(model.get("name", "")),
        cost_tracking_enabled=tracking,
        source_path=config_path,
    )
