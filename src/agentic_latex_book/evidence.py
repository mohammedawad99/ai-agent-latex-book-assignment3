"""Per-run evidence directory helper.

Creates the directory structure a real pipeline run would write its evidence
into. Stage 6 only provides and tests the helper (with pytest ``tmp_path``); it
does not write any committed evidence under ``results/``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

# Subdirectories created inside each run directory.
RUN_SUBDIRS = ("logs", "crew_outputs", "validation_reports", "final_pdf")

# A safe run_id is made only of letters, digits, underscore, dash, and dot.
_RUN_ID_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+$")


def _validate_run_id(run_id: str) -> None:
    """Reject empty, reserved, or unsafe run IDs."""
    if not run_id or run_id in (".", ".."):
        raise ValueError(f"Invalid run_id: {run_id!r}")
    if not _RUN_ID_PATTERN.fullmatch(run_id):
        raise ValueError(f"Invalid run_id: {run_id!r}")


@dataclass(frozen=True)
class RunDirectory:
    """Locations inside a single run's evidence directory."""

    root: Path

    @property
    def logs(self) -> Path:
        return self.root / "logs"

    @property
    def crew_outputs(self) -> Path:
        return self.root / "crew_outputs"

    @property
    def validation_reports(self) -> Path:
        return self.root / "validation_reports"

    @property
    def final_pdf(self) -> Path:
        return self.root / "final_pdf"


def create_run_directory(base_dir: Path, run_id: str, *, exist_ok: bool = False) -> RunDirectory:
    """Create ``base_dir/run_id`` and its standard subdirectories.

    Raises FileExistsError if the run directory already exists and ``exist_ok``
    is False, to avoid silently overwriting a previous run's evidence.
    """
    _validate_run_id(run_id)

    run_root = base_dir / run_id
    if run_root.exists() and not exist_ok:
        raise FileExistsError(f"Run directory already exists: {run_root}")

    for sub in RUN_SUBDIRS:
        (run_root / sub).mkdir(parents=True, exist_ok=True)

    return RunDirectory(root=run_root)
