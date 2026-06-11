"""Command-line entry point for the agentic LaTeX book project.

This is a Stage 5 setup skeleton. It is intentionally safe: it does not run
CrewAI, does not call any LLM, and does not create any output artifacts. Its
only job for now is to confirm the package is installed and to report the
current project status.
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
    "The CrewAI pipeline is not implemented yet. This command only reports "
    "project status; it does not generate content, call an LLM, or build a PDF."
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


def main(argv: list[str] | None = None) -> int:
    """Parse arguments and dispatch. Returns a process exit code."""
    parser = argparse.ArgumentParser(
        prog="agentic-latex-book",
        description=(
            "Setup skeleton for the CrewAI LaTeX book pipeline. No pipeline is implemented yet."
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

    args = parser.parse_args(argv)

    # Default behavior (no subcommand) is the safe status report.
    if args.command in (None, "status"):
        return _print_status(args.config)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
