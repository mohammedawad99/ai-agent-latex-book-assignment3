"""Planned agent specifications for the book-writing crew.

Roles follow the PLAN: a planner/outliner, a writer, a reviewer/editor, and a
reference curator. These are descriptions only — no CrewAI agent is built here.
"""

from __future__ import annotations

from agentic_latex_book.crew.specs import AgentSpec

PLANNER = AgentSpec(
    name="planner",
    role="Planner / Outliner",
    goal=(
        "Turn the chosen topic into a structured ~15-page outline and decide "
        "where each mandatory PDF element will appear."
    ),
    backstory=(
        "An experienced technical editor who is good at shaping a topic into a "
        "coherent, well-sized chapter structure."
    ),
)

WRITER = AgentSpec(
    name="writer",
    role="Writer",
    goal=(
        "Draft clear, accurate chapter content that follows the outline and "
        "the planned length for each section."
    ),
    backstory=(
        "A technical writer who explains AI-engineering topics in plain, "
        "professional English without marketing tone."
    ),
)

REVIEWER = AgentSpec(
    name="reviewer",
    role="Reviewer / Editor",
    goal=(
        "Check coherence, length, and that every mandatory PDF element planned "
        "in the outline is actually present, and request fixes when it is not."
    ),
    backstory=("A careful editor who values correctness and completeness over volume."),
)

REFERENCE_CURATOR = AgentSpec(
    name="reference_curator",
    role="Reference Curator",
    goal=(
        "Assemble a bibliography and map in-text citation points to it, for "
        "human review before use."
    ),
    backstory=("A meticulous researcher who keeps references consistent and traceable."),
)


def agent_specs() -> tuple[AgentSpec, ...]:
    """Return all planned agent specifications in a stable order."""
    return (PLANNER, WRITER, REVIEWER, REFERENCE_CURATOR)
