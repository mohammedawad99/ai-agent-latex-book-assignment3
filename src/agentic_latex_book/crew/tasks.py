"""Planned task specifications and their sequential context flow.

The outline and review tasks explicitly list the mandatory PDF elements so the
crew plans and checks for all of them. No task is executed here.
"""

from __future__ import annotations

from agentic_latex_book.crew.specs import TaskSpec

# Mandatory PDF elements (PRD PDF-1..PDF-11). Defined once and reused so the
# outline and review descriptions stay in sync.
MANDATORY_PDF_ELEMENTS = (
    "cover page",
    "table of contents",
    "chapters/sections",
    "headers and footers",
    "at least one image",
    "at least one Python-generated graph",
    "at least one table",
    "at least one mathematical formula",
    "a Hebrew-English BiDi section",
    "a bibliography with linked citations",
)

_ELEMENTS_TEXT = "; ".join(MANDATORY_PDF_ELEMENTS)

OUTLINE_TASK = TaskSpec(
    name="outline",
    description=(
        "Produce a structured outline for an approximately 15-page article/book "
        "on the given topic. Decide chapter/section titles and target lengths, "
        "and assign where each mandatory PDF element will appear: "
        f"{_ELEMENTS_TEXT}."
    ),
    expected_output=(
        "A structured outline listing chapters/sections with target lengths and "
        "the planned placement of every mandatory PDF element."
    ),
    agent_name="planner",
    output_schema_name="outline_output",
)

DRAFT_TASK = TaskSpec(
    name="draft",
    description=(
        "Write the chapter/section content following the outline and its target "
        "lengths. Keep the writing clear, professional, and free of marketing tone."
    ),
    expected_output="Draft text for each chapter/section, following the outline.",
    agent_name="writer",
    output_schema_name="draft_output",
    context_task_names=("outline",),
)

REVIEW_TASK = TaskSpec(
    name="review",
    description=(
        "Review the draft against the outline for coherence and length, and "
        "confirm that every mandatory PDF element is covered: "
        f"{_ELEMENTS_TEXT}. List any missing element and request fixes."
    ),
    expected_output=(
        "A revised draft plus review notes confirming coverage of the mandatory "
        "elements or listing what is missing."
    ),
    agent_name="reviewer",
    output_schema_name="review_output",
    context_task_names=("outline", "draft"),
)

REFERENCES_TASK = TaskSpec(
    name="references",
    description=(
        "Assemble a bibliography for the reviewed content and map in-text "
        "citation points to it, ready for human review."
    ),
    expected_output="A bibliography plus a citation map keyed to the content.",
    agent_name="reference_curator",
    output_schema_name="references_output",
    context_task_names=("outline", "draft", "review"),
)


def task_specs() -> tuple[TaskSpec, ...]:
    """Return all planned task specifications in execution order."""
    return (OUTLINE_TASK, DRAFT_TASK, REVIEW_TASK, REFERENCES_TASK)
