"""Tests for the crew builder and CLI crew-plan. Deterministic and offline."""

from __future__ import annotations

import pytest

from agentic_latex_book.cli import main
from agentic_latex_book.crew.builder import (
    CrewSpecError,
    crew_blueprint,
    crew_specs,
    validate_specs,
)
from agentic_latex_book.crew.specs import AgentSpec, TaskSpec


def test_default_specs_validate() -> None:
    """The shipped agent/task specs pass validation."""
    agents, tasks = crew_specs()
    validate_specs(agents, tasks)  # should not raise


def test_blueprint_is_stable_and_complete() -> None:
    """The dry-run blueprint lists every agent and task (with schema) in order."""
    blueprint = crew_blueprint()
    assert blueprint["process"] == "sequential"
    assert [a["name"] for a in blueprint["agents"]] == [
        "planner",
        "writer",
        "reviewer",
        "reference_curator",
    ]
    assert [t["name"] for t in blueprint["tasks"]] == [
        "outline",
        "draft",
        "review",
        "references",
    ]
    assert [t["output_schema"] for t in blueprint["tasks"]] == [
        "outline_output",
        "draft_output",
        "review_output",
        "references_output",
    ]


def test_validation_rejects_unknown_agent() -> None:
    """A task pointing at a missing agent is rejected."""
    agents = (AgentSpec(name="a", role="r", goal="g", backstory="b"),)
    tasks = (
        TaskSpec(
            name="t",
            description="d",
            expected_output="e",
            agent_name="x",
            output_schema_name="outline_output",
        ),
    )
    with pytest.raises(CrewSpecError):
        validate_specs(agents, tasks)


def test_validation_rejects_unknown_output_schema() -> None:
    """A task referencing an unknown output schema is rejected."""
    agents = (AgentSpec(name="a", role="r", goal="g", backstory="b"),)
    tasks = (
        TaskSpec(
            name="t",
            description="d",
            expected_output="e",
            agent_name="a",
            output_schema_name="nope_output",
        ),
    )
    with pytest.raises(CrewSpecError):
        validate_specs(agents, tasks)


def test_validation_rejects_forward_context() -> None:
    """A task referencing a later task as context is rejected."""
    agents = (AgentSpec(name="a", role="r", goal="g", backstory="b"),)
    tasks = (
        TaskSpec(
            name="t1",
            description="d",
            expected_output="e",
            agent_name="a",
            output_schema_name="outline_output",
            context_task_names=("t2",),
        ),
        TaskSpec(
            name="t2",
            description="d",
            expected_output="e",
            agent_name="a",
            output_schema_name="draft_output",
        ),
    )
    with pytest.raises(CrewSpecError):
        validate_specs(agents, tasks)


def test_cli_crew_plan_exits_zero(capsys) -> None:
    """The crew-plan command prints agents/tasks and exits 0, offline."""
    exit_code = main(["crew-plan"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "planner" in captured.out
    assert "outline" in captured.out
    assert "not implemented yet" in captured.out.lower()


def test_build_crew_constructs_without_running(monkeypatch) -> None:
    """build_crew constructs CrewAI objects but never runs them (no kickoff)."""
    # Disable any telemetry so the test stays fully offline.
    monkeypatch.setenv("CREWAI_DISABLE_TELEMETRY", "true")
    monkeypatch.setenv("OTEL_SDK_DISABLED", "true")
    from agentic_latex_book.crew.builder import build_crew

    crew = build_crew()
    assert len(crew.agents) == 4
    assert len(crew.tasks) == 4
