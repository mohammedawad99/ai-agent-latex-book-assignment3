"""Full content-generation pipeline runner.

Default behaviour is a safe dry-run that reports the full crew blueprint without
constructing an LLM or running anything. A real run happens only when ``real=True``
and the provider/model/environment validate; that path contains the single,
explicit CrewAI execution for the full pipeline and persists per-task evidence.
"""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from agentic_latex_book.config import Config, is_model_configured, load_config
from agentic_latex_book.crew.builder import build_crew, crew_blueprint
from agentic_latex_book.crew.llm import describe_llm_environment, resolve_llm
from agentic_latex_book.crew.persist import persist_full_run
from agentic_latex_book.crew.tasks import task_specs
from agentic_latex_book.evidence import create_run_directory
from agentic_latex_book.paths import repo_paths
from agentic_latex_book.runtime import RuntimeTracker

_DRY_RUN_NOTE = (
    "Dry-run only: no LLM was constructed, no crew was run, and no files were "
    "written. Use --real (with provider/model and credentials) for a real run."
)


def _default_full_run_id() -> str:
    """Return a fresh UTC-stamped run id: stage8c3-full-gemini-YYYYMMDD-HHMMSS."""
    stamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    return f"stage8c3-full-gemini-{stamp}"


def _base_summary(config: Config, mode: str) -> dict:
    """Build the safe, secret-free summary shared by both modes."""
    return {
        "mode": mode,
        "model_configured": is_model_configured(config),
        "llm_environment": describe_llm_environment(config),
        "blueprint": crew_blueprint(),
    }


def _collect_task_outputs(result) -> dict:
    """Map ordered task names to their raw text from a CrewOutput (no model call)."""
    names = [task.name for task in task_specs()]
    tasks_output = getattr(result, "tasks_output", None) or []
    outputs: dict[str, str] = {}
    for index, name in enumerate(names):
        if index < len(tasks_output):
            outputs[name] = str(getattr(tasks_output[index], "raw", ""))
        else:
            outputs[name] = ""
    return outputs


def _run_real_full(config: Config, run_id: str | None, results_dir: Path | None) -> dict:
    """Validate, run one controlled full-pipeline execution, and persist evidence."""
    llm = resolve_llm(config)  # raises before any file is created if misconfigured
    env_meta = describe_llm_environment(config)
    base = results_dir if results_dir is not None else repo_paths().results
    run_dir = create_run_directory(base, run_id or _default_full_run_id())

    tracker = RuntimeTracker(label="run-full").start()
    crew = build_crew(llm)
    result = crew.kickoff()
    tracker.stop()
    usage = getattr(result, "token_usage", None)
    tracker.prompt_tokens = getattr(usage, "prompt_tokens", None)
    tracker.completion_tokens = getattr(usage, "completion_tokens", None)
    tracker.model = config.model_name

    persist_full_run(run_dir, _collect_task_outputs(result), tracker.to_dict(), env_meta)
    summary = _base_summary(config, "real")
    summary["run_dir"] = str(run_dir.root)
    return summary


def run_full(
    dry_run: bool = True,
    real: bool = False,
    config_path: Path | None = None,
    run_id: str | None = None,
    results_dir: Path | None = None,
) -> dict:
    """Run the full pipeline. Dry-run by default; real only when ``real=True``."""
    config = load_config(config_path)
    if not real:
        summary = _base_summary(config, "dry-run")
        summary["note"] = _DRY_RUN_NOTE
        return summary
    return _run_real_full(config, run_id, results_dir)
