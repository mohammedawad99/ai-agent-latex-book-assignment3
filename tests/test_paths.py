"""Tests for the central path helpers. Deterministic and offline."""

from __future__ import annotations

from pathlib import Path

from agentic_latex_book.paths import repo_paths


def test_default_repo_paths_point_at_real_repo() -> None:
    """The default paths resolve to the actual repository layout."""
    paths = repo_paths()
    assert paths.default_config.is_file()
    assert paths.config_dir.is_dir()
    assert paths.results.name == "results"


def test_custom_root_is_respected(tmp_path) -> None:
    """A custom root reroutes every derived path beneath it."""
    paths = repo_paths(tmp_path)
    assert paths.root == tmp_path
    assert paths.logs == tmp_path / "results" / "logs"
    assert paths.crew_outputs == tmp_path / "results" / "crew_outputs"
    assert paths.validation_reports == tmp_path / "results" / "validation_reports"
    assert paths.final_pdf == tmp_path / "results" / "final_pdf"
    assert paths.latex_project == tmp_path / "latex_project"
    assert paths.assets_generated == tmp_path / "assets" / "generated"


def test_paths_are_path_objects() -> None:
    """All helpers return pathlib.Path values."""
    paths = repo_paths()
    assert isinstance(paths.default_config, Path)
    assert isinstance(paths.assets_figures, Path)
