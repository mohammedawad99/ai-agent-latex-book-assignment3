"""Command handlers for the CLI.

Kept separate from ``cli.py`` so that module stays focused on argparse setup and
dispatch. All handlers here are safe and offline except ``run_minimal_command``
with a real run, which only proceeds when explicitly requested and configured.
"""

from __future__ import annotations

from pathlib import Path

from agentic_latex_book import __version__
from agentic_latex_book.config import ConfigError, load_config
from agentic_latex_book.crew.llm import LLMConfigError

NOT_IMPLEMENTED_NOTICE = (
    "The CrewAI pipeline is not implemented yet. The current commands only report "
    "project status or a dry-run crew plan; they do not generate content, call an "
    "LLM, run kickoff, or build a PDF."
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


def run_minimal_command(config_path: Path, real: bool, run_id: str | None) -> int:
    """Run the minimal crew (dry-run by default). Real mode fails safe if unconfigured."""
    from agentic_latex_book.crew.runner import run_minimal

    try:
        summary = run_minimal(dry_run=not real, real=real, config_path=config_path, run_id=run_id)
    except (ConfigError, LLMConfigError) as exc:
        # Safe failure: clear message, no secret values, no files created.
        print(f"run-minimal could not start a real run: {exc}")
        return 1

    env = summary["llm_environment"]
    print(f"mode: {summary['mode']}")
    print(f"provider: {env['provider'] or '<unset>'}  model: {env['model'] or '<unset>'}")
    print(f"api_key_present: {env['api_key_present']}  base_url_present: {env['base_url_present']}")
    if summary["mode"] == "dry-run":
        print(summary["note"])
    else:
        print(f"run_dir: {summary.get('run_dir')}")
    return 0
