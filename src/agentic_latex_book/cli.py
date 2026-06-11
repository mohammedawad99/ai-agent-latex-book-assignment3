"""Command-line entry point for the agentic LaTeX book project.

The default commands are safe and offline: ``status`` reports project state and
``crew-plan`` prints the planned agents, tasks, and output schemas. ``run-minimal``
defaults to a dry-run (no LLM, no run, no files). A real run happens only with the
explicit ``run-minimal --real`` flag and a configured provider/model plus
credentials; without those it fails safely and writes nothing.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from agentic_latex_book import __version__
from agentic_latex_book.cli_commands import (
    print_crew_plan,
    print_status,
    run_full_command,
    run_minimal_command,
)
from agentic_latex_book.paths import repo_paths

_DEFAULT_CONFIG = repo_paths().default_config


def _build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser, including subcommands."""
    parser = argparse.ArgumentParser(
        prog="agentic-latex-book",
        description=(
            "Safe offline CLI for the CrewAI LaTeX book pipeline. It can report "
            "status and print the planned crew blueprint; it does not run the "
            "pipeline yet."
        ),
    )
    parser.add_argument("--version", action="version", version=f"agentic-latex-book {__version__}")
    parser.add_argument(
        "--config",
        type=Path,
        default=_DEFAULT_CONFIG,
        help="Path to the TOML config file (default: config/default.toml).",
    )
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("status", help="Print current project status (safe, offline).")
    subparsers.add_parser(
        "crew-plan", help="Print the planned crew agents and tasks (safe, offline; no run)."
    )
    _add_run_subparser(
        subparsers, "run-minimal", "Run a minimal crew; dry-run by default, --real to execute."
    )
    _add_run_subparser(
        subparsers,
        "run-full",
        "Run the full content pipeline; dry-run by default, --real to execute.",
    )
    return parser


def _add_run_subparser(subparsers, name: str, help_text: str) -> None:
    """Add a run subcommand with mutually-exclusive --dry-run/--real and --run-id."""
    parser = subparsers.add_parser(name, help=help_text)
    # Dry-run and real are mutually exclusive so a real run is never ambiguous.
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Safe offline dry-run (default).")
    mode.add_argument(
        "--real", action="store_true", help="Real run (needs provider/model + credentials)."
    )
    parser.add_argument("--run-id", default=None, help="Optional run id for the evidence dir.")


def main(argv: list[str] | None = None) -> int:
    """Parse arguments and dispatch. Returns a process exit code."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "crew-plan":
        return print_crew_plan()
    if args.command == "run-minimal":
        return run_minimal_command(args.config, args.real, args.run_id)
    if args.command == "run-full":
        return run_full_command(args.config, args.real, args.run_id)
    if args.command in (None, "status"):
        return print_status(args.config)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
