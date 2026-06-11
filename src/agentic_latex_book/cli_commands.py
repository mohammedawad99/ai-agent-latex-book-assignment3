"""Command handlers for the CLI.

Kept separate from ``cli.py`` so that module stays focused on argparse setup and
dispatch. ``print_status``, ``print_crew_plan``, and ``content_qa_command`` are
offline. ``run_minimal_command`` and ``run_full_command`` are dry-run by default
and only execute a real run when explicitly requested through ``--real``.
"""

from __future__ import annotations

from pathlib import Path

from agentic_latex_book import __version__
from agentic_latex_book.config import ConfigError, load_config
from agentic_latex_book.crew.llm import LLMConfigError

NOT_IMPLEMENTED_NOTICE = (
    "status and crew-plan are safe offline commands. PDF/LaTeX generation is not "
    "implemented yet. Real CrewAI runs require an explicit --real flag and "
    "credentials; no command prints raw secrets."
)


def print_status(config_path: Path) -> int:
    """Print a safe project-status summary. Performs no external calls."""
    print(f"agentic-latex-book version {__version__}")
    try:
        config = load_config(config_path)
    except ConfigError as exc:
        print(f"config: <error> {exc}")
        print(NOT_IMPLEMENTED_NOTICE)
        return 0

    print(f"group: {config.group_code}")
    print(f"topic: {config.topic}")
    print(f"config: {config.source_path}")
    print(f"page-count target: {config.page_count_min}-{config.page_count_max}")
    print(NOT_IMPLEMENTED_NOTICE)
    return 0


def print_crew_plan() -> int:
    """Print the planned crew agents and tasks. Builds no objects, runs nothing."""
    from agentic_latex_book.crew.builder import crew_blueprint

    blueprint = crew_blueprint()
    print(f"crew process: {blueprint['process']}")
    print("agents:")
    for agent in blueprint["agents"]:
        print(f"  - {agent['name']}: {agent['role']}")
    print("tasks (in order):")
    for task in blueprint["tasks"]:
        context = ", ".join(task["context"]) or "-"
        print(
            f"  - {task['name']} (agent: {task['agent']}, "
            f"schema: {task['output_schema']}, context: {context})"
        )
    print(NOT_IMPLEMENTED_NOTICE)
    return 0


def _print_run_summary(summary: dict) -> None:
    """Print a run summary using presence booleans only (never a raw key)."""
    env = summary["llm_environment"]
    print(f"mode: {summary['mode']}")
    print(f"provider: {env['provider'] or '<unset>'}  model: {env['model'] or '<unset>'}")
    print(f"api_key_present: {env['api_key_present']}  base_url_present: {env['base_url_present']}")
    if summary["mode"] == "dry-run":
        print(summary["note"])
    else:
        print(f"run_dir: {summary.get('run_dir')}")


def run_minimal_command(config_path: Path, real: bool, run_id: str | None) -> int:
    """Run the minimal crew (dry-run by default). Real mode fails safe if unconfigured."""
    from agentic_latex_book.crew.runner import run_minimal

    try:
        summary = run_minimal(dry_run=not real, real=real, config_path=config_path, run_id=run_id)
    except (ConfigError, LLMConfigError) as exc:
        # Safe failure: clear message, no secret values, no files created.
        print(f"run-minimal could not start a real run: {exc}")
        return 1
    _print_run_summary(summary)
    return 0


def content_qa_command(path: str) -> int:
    """Scan content for QA risks (offline). Returns 0 if clean, 1 if any blocking error."""
    from agentic_latex_book.content_qa import scan

    report = scan(path)
    print(f"files checked: {len(report.checked_files)}")
    print(f"ok: {report.ok}  errors: {len(report.errors)}  warnings: {len(report.warnings)}")
    for err in report.errors:
        print(f"  ERROR: {err}")
    for warn in report.warnings:
        print(f"  WARN: {warn}")
    return 0 if report.ok else 1


def run_full_command(config_path: Path, real: bool, run_id: str | None) -> int:
    """Run the full content pipeline (dry-run by default). Real mode fails safe if unconfigured."""
    from agentic_latex_book.crew.full_runner import run_full

    try:
        summary = run_full(dry_run=not real, real=real, config_path=config_path, run_id=run_id)
    except (ConfigError, LLMConfigError) as exc:
        # Safe failure: clear message, no secret values, no files created.
        print(f"run-full could not start a real run: {exc}")
        return 1
    _print_run_summary(summary)
    return 0
