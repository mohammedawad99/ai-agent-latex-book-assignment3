"""Task specifications and their sequential context flow.

The descriptions are bound to a ``ProjectContext`` so the crew writes about the
configured topic with the real cover metadata (see decision D-025). The mandatory
PDF elements are listed in the outline and review tasks.
"""

from __future__ import annotations

from agentic_latex_book.crew.context import GENERIC_CONTEXT, ProjectContext
from agentic_latex_book.crew.instructions import (
    MANDATORY_PDF_ELEMENTS,
    draft_instructions,
    outline_instructions,
    references_instructions,
    review_instructions,
)
from agentic_latex_book.crew.specs import TaskSpec

__all__ = ["MANDATORY_PDF_ELEMENTS", "build_task_specs", "task_specs"]


def build_task_specs(context: ProjectContext) -> tuple[TaskSpec, ...]:
    """Build the four task specs with descriptions bound to ``context``."""
    return (
        TaskSpec(
            name="outline",
            description=outline_instructions(context),
            expected_output=(
                "A structured outline listing chapters/sections with target lengths "
                "and the planned placement of every mandatory PDF element."
            ),
            agent_name="planner",
            output_schema_name="outline_output",
        ),
        TaskSpec(
            name="draft",
            description=draft_instructions(context),
            expected_output="Draft text for each chapter/section, following the outline.",
            agent_name="writer",
            output_schema_name="draft_output",
            context_task_names=("outline",),
        ),
        TaskSpec(
            name="review",
            description=review_instructions(context),
            expected_output=(
                "A revised draft plus review notes confirming coverage of the "
                "mandatory elements or listing what is missing."
            ),
            agent_name="reviewer",
            output_schema_name="review_output",
            context_task_names=("outline", "draft"),
        ),
        TaskSpec(
            name="references",
            description=references_instructions(context),
            expected_output="A bibliography plus a citation map keyed to the content.",
            agent_name="reference_curator",
            output_schema_name="references_output",
            context_task_names=("outline", "draft", "review"),
        ),
    )


def task_specs() -> tuple[TaskSpec, ...]:
    """Return the task specs with the generic context (structure + offline uses)."""
    return build_task_specs(GENERIC_CONTEXT)
