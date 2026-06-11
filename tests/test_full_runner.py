"""Tests for the full content-pipeline runner. Offline: the real path is never run."""

from __future__ import annotations

import json

import pytest

from agentic_latex_book import cli
from agentic_latex_book.config import ConfigError, load_config
from agentic_latex_book.crew import full_runner
from agentic_latex_book.crew.full_runner import (
    _collect_task_outputs,
    _default_full_run_id,
    run_full,
)
from agentic_latex_book.crew.persist import persist_full_run
from agentic_latex_book.evidence import create_run_directory

_EXPECTED_SCHEMAS = {
    "outline_output",
    "draft_output",
    "review_output",
    "references_output",
}


class _FakeTaskOutput:
    def __init__(self, raw: str) -> None:
        self.raw = raw


class _FakeResult:
    def __init__(self, texts: list[str]) -> None:
        self.tasks_output = [_FakeTaskOutput(t) for t in texts]


def test_dry_run_writes_no_files(tmp_path) -> None:
    summary = run_full(dry_run=True, real=False, results_dir=tmp_path)
    assert summary["mode"] == "dry-run"
    assert "blueprint" in summary and "note" in summary
    assert list(tmp_path.iterdir()) == []


def test_dry_run_never_enters_real_path(tmp_path, monkeypatch) -> None:
    def _boom(*args, **kwargs):
        raise AssertionError("real path must not run in dry-run")

    monkeypatch.setattr(full_runner, "_run_real_full", _boom)
    summary = run_full(dry_run=True, real=False, results_dir=tmp_path)
    assert summary["mode"] == "dry-run"


def test_real_without_model_fails_and_writes_nothing(tmp_path) -> None:
    with pytest.raises(ConfigError):
        run_full(real=True, results_dir=tmp_path)
    assert list(tmp_path.iterdir()) == []


def test_cli_run_full_dry_run_exits_zero(capsys) -> None:
    exit_code = cli.main(["run-full"])
    out = capsys.readouterr().out
    assert exit_code == 0
    assert "dry-run" in out
    assert "no crew was run" in out


def test_cli_run_full_dry_run_and_real_conflict() -> None:
    with pytest.raises(SystemExit) as exc:
        cli.main(["run-full", "--dry-run", "--real"])
    assert exc.value.code == 2


def test_cli_run_full_real_without_config_fails(monkeypatch, capsys) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "FAKEKEY-NOLEAK")
    default_config = load_config().source_path
    exit_code = cli.main(["--config", str(default_config), "run-full", "--real"])
    out = capsys.readouterr().out
    assert exit_code == 1
    assert "could not start a real run" in out
    assert "FAKEKEY-NOLEAK" not in out


def test_default_full_run_id_is_timestamped() -> None:
    """The default run id is UTC-stamped and not the old static string."""
    run_id = _default_full_run_id()
    assert run_id.startswith("stage8c3-full-gemini-")
    assert run_id != "stage8c3-full-gemini"
    # prefix + YYYYMMDD-HHMMSS suffix
    suffix = run_id.removeprefix("stage8c3-full-gemini-")
    assert len(suffix) == 15 and suffix[8] == "-"


def test_collect_task_outputs_maps_by_order() -> None:
    result = _FakeResult(["outline text", "draft text", "review text", "references text"])
    outputs = _collect_task_outputs(result)
    assert outputs == {
        "outline": "outline text",
        "draft": "draft text",
        "review": "review text",
        "references": "references text",
    }


def test_persist_writes_all_files_without_secrets(tmp_path) -> None:
    run_dir = create_run_directory(tmp_path, "fake-full-run")
    task_outputs = {
        "outline": "an outline",
        "draft": "a draft",
        "review": "review notes",
        "references": "a bibliography",
    }
    runtime = {"label": "run-full", "elapsed_seconds": 1.0, "prompt_tokens": None}
    env_meta = {
        "provider": "gemini",
        "model": "gemini/gemini-2.5-flash",
        "base_url_present": False,
        "api_key_present": True,
    }
    persist_full_run(run_dir, task_outputs, runtime, env_meta)

    for name in task_outputs:
        assert (run_dir.crew_outputs / f"{name}.txt").is_file()
    assert (run_dir.root / "runtime.json").is_file()
    assert (run_dir.logs / "run.log").is_file()
    assert (run_dir.validation_reports / "run_note.md").is_file()

    index = json.loads((run_dir.crew_outputs / "_index.json").read_text(encoding="utf-8"))
    assert {entry["output_schema"] for entry in index.values()} == _EXPECTED_SCHEMAS
    assert all(entry["non_empty"] for entry in index.values())

    combined = "".join(
        p.read_text(encoding="utf-8") for p in run_dir.root.rglob("*") if p.is_file()
    )
    # Build the forbidden key prefixes by concatenation so the literals never
    # appear in this file (keeps the repo secret scan clean).
    for prefix in ("sk" + "-", "AI" + "za"):
        assert prefix not in combined
