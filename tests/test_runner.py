"""Tests for the minimal controlled runner. Offline: real mode is never run."""

from __future__ import annotations

import pytest

from agentic_latex_book import cli
from agentic_latex_book.config import ConfigError, load_config
from agentic_latex_book.crew import runner
from agentic_latex_book.crew.llm import LLMConfigError

_CONFIGURED = """\
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
provider = "openai"
name = "gpt-4o-mini"

[cost]
tracking_enabled = true
"""


def _configured_path(tmp_path):
    path = tmp_path / "config.toml"
    path.write_text(_CONFIGURED, encoding="utf-8")
    return path


def test_dry_run_never_enters_real_path(tmp_path, monkeypatch) -> None:
    """Dry-run returns a summary without ever constructing an LLM or running."""

    def _boom(*args, **kwargs):
        raise AssertionError("real path must not run in dry-run")

    monkeypatch.setattr(runner, "_run_real", _boom)
    summary = runner.run_minimal(dry_run=True, real=False, results_dir=tmp_path)
    assert summary["mode"] == "dry-run"
    assert "blueprint" in summary
    assert "note" in summary


def test_dry_run_creates_no_files(tmp_path) -> None:
    """Dry-run writes nothing under the provided results directory."""
    runner.run_minimal(dry_run=True, real=False, results_dir=tmp_path)
    assert list(tmp_path.iterdir()) == []


def test_real_without_model_fails_and_writes_nothing(tmp_path) -> None:
    """real=True with placeholder config raises and creates no artifacts."""
    with pytest.raises(ConfigError):
        runner.run_minimal(real=True, results_dir=tmp_path)
    assert list(tmp_path.iterdir()) == []


def test_real_without_credentials_fails_and_writes_nothing(tmp_path, monkeypatch) -> None:
    """real=True with a model but no key/base_url raises before any file is made."""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    with pytest.raises(LLMConfigError):
        runner.run_minimal(real=True, config_path=_configured_path(tmp_path), results_dir=tmp_path)
    # tmp_path only holds the config file we wrote; no run directory was created.
    assert [p.name for p in tmp_path.iterdir()] == ["config.toml"]


def test_cli_run_minimal_dry_run_exits_zero(capsys) -> None:
    exit_code = cli.main(["run-minimal"])
    out = capsys.readouterr().out
    assert exit_code == 0
    assert "dry-run" in out
    assert "no crew was run" in out


def test_cli_run_minimal_dry_run_and_real_conflict(tmp_path) -> None:
    """`run-minimal --dry-run --real` is rejected by argparse before any runner call."""
    with pytest.raises(SystemExit) as exc:
        cli.main(["run-minimal", "--dry-run", "--real"])
    assert exc.value.code == 2
    # argparse fails during parsing, so no run directory could have been created.
    assert list(tmp_path.iterdir()) == []


def test_cli_run_minimal_real_without_config_fails(tmp_path, monkeypatch, capsys) -> None:
    """`run-minimal --real` with placeholder config exits non-zero, leaks no key, no files."""
    monkeypatch.setenv("OPENAI_API_KEY", "FAKEKEY-NOLEAK")
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    default_config = load_config().source_path
    exit_code = cli.main(["--config", str(default_config), "run-minimal", "--real"])
    out = capsys.readouterr().out
    assert exit_code == 1
    assert "could not start a real run" in out
    assert "FAKEKEY-NOLEAK" not in out
