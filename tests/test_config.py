"""Tests for the configuration loader. Deterministic and offline."""

from __future__ import annotations

import pytest

from agentic_latex_book.config import REQUIRED_PATH_KEYS, ConfigError, load_config

_VALID_CONFIG = """\
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
provider = ""
name = ""

[cost]
tracking_enabled = true
"""


def test_loads_default_config() -> None:
    """The repository's default config loads and validates."""
    config = load_config()
    assert config.group_code == "MaRs-777"
    assert config.topic
    assert config.page_count_min <= config.page_count_max
    assert isinstance(config.cost_tracking_enabled, bool)


def test_loads_custom_config(tmp_path) -> None:
    """A custom config path is honored."""
    path = tmp_path / "custom.toml"
    path.write_text(_VALID_CONFIG, encoding="utf-8")
    config = load_config(path)
    assert config.topic == "Test topic"
    assert config.source_path == path


def test_missing_config_fails(tmp_path) -> None:
    """A missing file raises ConfigError."""
    with pytest.raises(ConfigError):
        load_config(tmp_path / "does_not_exist.toml")


def test_malformed_toml_fails(tmp_path) -> None:
    """Unparseable TOML raises ConfigError."""
    path = tmp_path / "bad.toml"
    path.write_text("this is = = not valid toml", encoding="utf-8")
    with pytest.raises(ConfigError):
        load_config(path)


def test_missing_section_fails(tmp_path) -> None:
    """A config missing a required section raises ConfigError."""
    path = tmp_path / "partial.toml"
    path.write_text('[project]\ntopic = "x"\ngroup_code = "y"\n', encoding="utf-8")
    with pytest.raises(ConfigError):
        load_config(path)


def test_invalid_page_counts_fail(tmp_path) -> None:
    """min > max is rejected."""
    path = tmp_path / "pages.toml"
    bad = _VALID_CONFIG.replace("page_count_min = 13", "page_count_min = 20")
    path.write_text(bad, encoding="utf-8")
    with pytest.raises(ConfigError):
        load_config(path)


def test_default_config_has_all_required_paths() -> None:
    """The default config exposes every required path key."""
    config = load_config()
    for key in REQUIRED_PATH_KEYS:
        assert key in config.paths
        assert config.paths[key]


def test_missing_required_path_key_fails(tmp_path) -> None:
    """Dropping a required [paths] key is rejected."""
    path = tmp_path / "paths.toml"
    bad = _VALID_CONFIG.replace('final_pdf = "results/final_pdf"\n', "")
    path.write_text(bad, encoding="utf-8")
    with pytest.raises(ConfigError):
        load_config(path)


def test_empty_path_value_fails(tmp_path) -> None:
    """An empty/non-string path value is rejected."""
    path = tmp_path / "paths.toml"
    bad = _VALID_CONFIG.replace('results = "results"', 'results = ""')
    path.write_text(bad, encoding="utf-8")
    with pytest.raises(ConfigError):
        load_config(path)


def test_non_string_path_value_fails(tmp_path) -> None:
    """A non-string [paths] value (e.g. an integer) is rejected."""
    path = tmp_path / "paths.toml"
    bad = _VALID_CONFIG.replace('results = "results"', "results = 123")
    path.write_text(bad, encoding="utf-8")
    with pytest.raises(ConfigError):
        load_config(path)
