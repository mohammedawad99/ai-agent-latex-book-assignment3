"""Minimal controlled runner for the first real CrewAI execution.

Default behaviour is a safe dry-run: it builds the offline blueprint and reports
what *would* run, constructing no LLM and calling no model. A real run happens
only when ``real=True`` and the provider/model/environment validate; that path
contains the single, explicit CrewAI execution and writes per-run evidence.
"""

from __future__ import annotations

import json
from pathlib import Path

from agentic_latex_book.config import Config, is_model_configured, load_config
from agentic_latex_book.crew.builder import crew_blueprint
from agentic_latex_book.crew.llm import describe_llm_environment, resolve_llm
from agentic_latex_book.evidence import create_run_directory
from agentic_latex_book.paths import repo_paths
from agentic_latex_book.runtime import RuntimeTracker

_DRY_RUN_NOTE = (
    "Dry-run only: no LLM was constructed, no crew was run, and no files were "
    "written. Use --real (with provider/model and credentials) for a real run."
)


def _summary(config: Config, real: bool) -> dict:
    """Build the safe, secret-free summary common to both modes."""
    return {
        "mode": "real" if real else "dry-run",
        "model_configured": is_model_configured(config),
        "llm_environment": describe_llm_environment(config),
        "blueprint": crew_blueprint(),
    }


def _build_minimal_crew(llm):
    """Construct a one-agent, one-task crew for a controlled minimal run."""
    from crewai import Agent, Crew, Process, Task

    agent = Agent(
        role="Minimal Checker",
        goal="Confirm the crew wiring works with a tiny task.",
        backstory="A minimal agent used only to verify a single controlled run.",
        allow_delegation=False,
        verbose=False,
        llm=llm,
        max_iter=1,
    )
    task = Task(
        description="Reply with the single word: ok.",
        expected_output="The word ok.",
        agent=agent,
    )
    return Crew(agents=[agent], tasks=[task], process=Process.sequential)


def _write_evidence(run_dir, result, tracker: RuntimeTracker, env_meta: dict) -> None:
    """Write safe, secret-free evidence for a completed real run."""
    (run_dir.logs / "run.log").write_text(
        f"provider={env_meta['provider']} model={env_meta['model']} "
        f"api_key_present={env_meta['api_key_present']} "
        f"base_url_present={env_meta['base_url_present']}\n",
        encoding="utf-8",
    )
    (run_dir.crew_outputs / "minimal_task.txt").write_text(str(result), encoding="utf-8")
    runtime = dict(tracker.to_dict())
    runtime["llm_environment"] = env_meta
    (run_dir.root / "runtime.json").write_text(json.dumps(runtime, indent=2), encoding="utf-8")
    (run_dir.validation_reports / "run_note.md").write_text(
        "# Minimal run note\n\nA single controlled minimal crew run executed.\n",
        encoding="utf-8",
    )


def _run_real(config: Config, run_id: str | None, results_dir: Path | None) -> dict:
    """Validate, run one controlled crew execution, and write evidence."""
    llm = resolve_llm(config)  # raises before any file is created if misconfigured
    env_meta = describe_llm_environment(config)
    base = results_dir if results_dir is not None else repo_paths().results
    run_dir = create_run_directory(base, run_id or "run-minimal")

    tracker = RuntimeTracker(label="run-minimal").start()
    crew = _build_minimal_crew(llm)
    result = crew.kickoff()
    tracker.stop()
    tracker.prompt_tokens = getattr(getattr(result, "token_usage", None), "prompt_tokens", None)
    tracker.completion_tokens = getattr(
        getattr(result, "token_usage", None), "completion_tokens", None
    )
    tracker.model = config.model_name

    _write_evidence(run_dir, result, tracker, env_meta)
    summary = _summary(config, real=True)
    summary["run_dir"] = str(run_dir.root)
    return summary


def run_minimal(
    dry_run: bool = True,
    real: bool = False,
    config_path: Path | None = None,
    run_id: str | None = None,
    results_dir: Path | None = None,
) -> dict:
    """Run the minimal crew. Dry-run by default; real only when ``real=True``."""
    config = load_config(config_path)
    if not real:
        summary = _summary(config, real=False)
        summary["note"] = _DRY_RUN_NOTE
        return summary
    return _run_real(config, run_id, results_dir)
