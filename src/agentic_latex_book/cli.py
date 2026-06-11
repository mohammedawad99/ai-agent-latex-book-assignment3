"""Command-line entry point for the agentic LaTeX book project.

The CLI currently supports safe, offline commands: a project ``status`` report
and a ``crew-plan`` that prints the planned agents, tasks, and output schemas. It
is intentionally safe: it does not run CrewAI (no ``kickoff``), does not call any
LLM, and does not create any output artifacts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from agentic_latex_book import __version__
from agentic_latex_book.config import ConfigError, load_config
from agentic_latex_book.paths import repo_paths

_DEFAULT_CONFIG = repo_paths().default_config

_NOT_IMPLEMENTED_NOTICE = (
    "The CrewAI pipeline is not implemented yet. The current commands only report "
    "project status or a dry-run crew plan; they do not generate content, call an "
    "LLM, run kickoff, or build a PDF."
)


def _print_status(config_path: Path) -> int:
    """Print a safe project-status summary. Performs no external calls."""
    print(f"agentic-latex-book version {__version__}")
    try:
        config = load_config(config_path)
    except ConfigError as exc:
        print(f"config: <error> {exc}")
        print(_NOT_IMPLEMENTED_NOTICE)
        return 0

    print(f"group: {config.group_code}")
    print(f"topic: {config.topic}")
    print(f"config: {config.source_path}")
    print(f"page-count target: {config.page_count_min}-{config.page_count_max}")
    print(_NOT_IMPLEMENTED_NOTICE)
    return 0


def _print_crew_plan() -> int:
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
    print(_NOT_IMPLEMENTED_NOTICE)
    return 0


def main(argv: list[str] | None = None) -> int:
    """Parse arguments and dispatch. Returns a process exit code."""
    parser = argparse.ArgumentParser(
        prog="agentic-latex-book",
        description=(
            "Safe offline CLI for the CrewAI LaTeX book pipeline. It can report "
            "status and print the planned crew blueprint; it does not run the "
            "pipeline yet."
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"agentic-latex-book {__version__}",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=_DEFAULT_CONFIG,
        help="Path to the TOML config file (default: config/default.toml).",
    )
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser(
        "status",
        help="Print current project status and exit (safe, offline).",
    )
    subparsers.add_parser(
        "crew-plan",
        help="Print the planned crew agents and tasks (safe, offline; no run).",
    )

    args = parser.parse_args(argv)

    if args.command == "crew-plan":
        return _print_crew_plan()

    # Default behavior (no subcommand) is the safe status report.
    if args.command in (None, "status"):
        return _print_status(args.config)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
