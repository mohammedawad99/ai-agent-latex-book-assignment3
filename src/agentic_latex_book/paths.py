"""Central repository paths.

Keeping path resolution in one place avoids scattered hardcoded strings in the
rest of the package and makes the locations easy to test.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

# This file lives at src/agentic_latex_book/paths.py, so the repository root is
# three parents up.
_REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class RepoPaths:
    """Resolved locations for the project, relative to a repository root."""

    root: Path

    @property
    def config_dir(self) -> Path:
        return self.root / "config"

    @property
    def default_config(self) -> Path:
        return self.config_dir / "default.toml"

    @property
    def results(self) -> Path:
        return self.root / "results"

    @property
    def logs(self) -> Path:
        return self.results / "logs"

    @property
    def crew_outputs(self) -> Path:
        return self.results / "crew_outputs"

    @property
    def validation_reports(self) -> Path:
        return self.results / "validation_reports"

    @property
    def final_pdf(self) -> Path:
        return self.results / "final_pdf"

    @property
    def latex_project(self) -> Path:
        return self.root / "latex_project"

    @property
    def assets_figures(self) -> Path:
        return self.root / "assets" / "figures"

    @property
    def assets_generated(self) -> Path:
        return self.root / "assets" / "generated"


def repo_paths(root: Path | None = None) -> RepoPaths:
    """Return the project paths, rooted at ``root`` (defaults to the repo root)."""
    return RepoPaths(root=root if root is not None else _REPO_ROOT)
