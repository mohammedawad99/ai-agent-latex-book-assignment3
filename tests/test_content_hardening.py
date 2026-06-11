"""Tests for Stage 8C.6 topic/metadata hardening. Offline; no model is called."""

from __future__ import annotations

import pytest

from agentic_latex_book.config import ConfigError, load_config
from agentic_latex_book.crew.builder import crew_blueprint
from agentic_latex_book.crew.content_checks import (
    check_content,
    find_forbidden_terms,
    find_placeholders,
    missing_mandatory_elements,
)
from agentic_latex_book.crew.context import project_context
from agentic_latex_book.crew.tasks import build_task_specs

_REQUIRED_TOPIC = (
    "From PoC to Production: A CrewAI Multi-Agent Pipeline for Generating a LaTeX Book"
)

_TEMPLATE = """\
[project]
topic = "Test topic"
group_code = "MaRs-777"
{metadata}

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

_GOOD_METADATA = (
    'authors = ["Mohamed Awad", "Rawey Sleiman"]\n'
    'assignment_context = "AI agents / CrewAI / LaTeX book generation assignment"\n'
    'project_date = "2026-06-11"'
)


def _write(tmp_path, metadata):
    path = tmp_path / "config.toml"
    path.write_text(_TEMPLATE.format(metadata=metadata), encoding="utf-8")
    return path


def test_default_config_has_required_metadata() -> None:
    config = load_config()
    assert config.topic == _REQUIRED_TOPIC
    assert config.authors == ("Mohamed Awad", "Rawey Sleiman")
    assert config.assignment_context
    assert config.project_date


def test_missing_authors_fails(tmp_path) -> None:
    metadata = 'assignment_context = "x"\nproject_date = "2026-06-11"'
    with pytest.raises(ConfigError):
        load_config(_write(tmp_path, metadata))


def test_empty_authors_fails(tmp_path) -> None:
    metadata = 'authors = []\nassignment_context = "x"\nproject_date = "2026-06-11"'
    with pytest.raises(ConfigError):
        load_config(_write(tmp_path, metadata))


def test_missing_project_date_fails(tmp_path) -> None:
    metadata = 'authors = ["A"]\nassignment_context = "x"'
    with pytest.raises(ConfigError):
        load_config(_write(tmp_path, metadata))


def test_blueprint_includes_configured_topic() -> None:
    blueprint = crew_blueprint(project_context(load_config()))
    assert blueprint["topic"] == _REQUIRED_TOPIC


def test_task_instructions_include_author_group_date() -> None:
    context = project_context(load_config())
    tasks = {t.name: t for t in build_task_specs(context)}
    outline = tasks["outline"].description
    assert "MaRs-777" in outline
    assert "Mohamed Awad" in outline
    assert "2026-06-11" in outline
    assert _REQUIRED_TOPIC in outline


def test_content_checks_reject_gradient_descent() -> None:
    text = "Understanding and Implementing Gradient Descent: A Practical Guide"
    assert find_forbidden_terms(text)
    assert check_content(text, _REQUIRED_TOPIC)["ok"] is False


def test_content_checks_reject_placeholders() -> None:
    text = "Author: [Your Name/Placeholder Name]\nDate: October 2023"
    assert find_placeholders(text)
    assert check_content(text, _REQUIRED_TOPIC)["ok"] is False


def test_content_checks_accept_on_topic() -> None:
    text = (
        "From PoC to Production: A CrewAI Multi-Agent Pipeline. "
        "Authors: Mohamed Awad, Rawey Sleiman. Date: 2026-06-11."
    )
    result = check_content(text, _REQUIRED_TOPIC)
    assert result["on_topic"] is True
    assert result["ok"] is True


def test_missing_mandatory_elements_flags_absent() -> None:
    assert "a table of contents" not in missing_mandatory_elements("table of contents only")
    assert missing_mandatory_elements("nothing relevant here")
