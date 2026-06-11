"""Tests for the crew agent/task specifications. Deterministic and offline."""

from __future__ import annotations

from agentic_latex_book.crew.agents import agent_specs
from agentic_latex_book.crew.schemas import output_schema_specs
from agentic_latex_book.crew.tasks import MANDATORY_PDF_ELEMENTS, task_specs

_EXPECTED_AGENTS = {"planner", "writer", "reviewer", "reference_curator"}
_EXPECTED_TASKS = {"outline", "draft", "review", "references"}
_EXPECTED_SCHEMAS = {
    "outline_output",
    "draft_output",
    "review_output",
    "references_output",
}


def test_all_expected_agents_exist() -> None:
    """The four planned agents are present with non-empty role and goal."""
    agents = agent_specs()
    assert {a.name for a in agents} == _EXPECTED_AGENTS
    for agent in agents:
        assert agent.role and agent.goal and agent.backstory


def test_all_expected_tasks_exist() -> None:
    """The four planned tasks are present with non-empty descriptions."""
    tasks = task_specs()
    assert {t.name for t in tasks} == _EXPECTED_TASKS
    for task in tasks:
        assert task.description and task.expected_output


def test_every_task_references_a_known_agent() -> None:
    """Each task's agent_name matches a defined agent."""
    agent_names = {a.name for a in agent_specs()}
    for task in task_specs():
        assert task.agent_name in agent_names


def test_task_context_references_only_earlier_tasks() -> None:
    """Context tasks must appear before the task that uses them."""
    seen: set[str] = set()
    for task in task_specs():
        for ctx in task.context_task_names:
            assert ctx in seen
        seen.add(task.name)


def test_mandatory_pdf_elements_in_outline_and_review() -> None:
    """Outline and review descriptions mention every mandatory PDF element."""
    tasks = {t.name: t for t in task_specs()}
    for element in MANDATORY_PDF_ELEMENTS:
        assert element in tasks["outline"].description
        assert element in tasks["review"].description


def test_all_expected_output_schemas_exist() -> None:
    """The four planned output schemas exist with non-empty fields."""
    schemas = output_schema_specs()
    assert {s.name for s in schemas} == _EXPECTED_SCHEMAS
    for schema in schemas:
        assert schema.description
        assert schema.fields


def test_every_task_references_a_known_output_schema() -> None:
    """Each task's output_schema_name matches a defined schema."""
    schema_names = {s.name for s in output_schema_specs()}
    for task in task_specs():
        assert task.output_schema_name in schema_names
