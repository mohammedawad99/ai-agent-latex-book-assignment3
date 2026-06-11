"""Offline structured-output schema specifications.

These describe the structured contract each task's output is *intended* to follow
in later stages. They are plain data — no Pydantic, no dependency, and no
enforcement against real LLM output yet. They exist so the crew design names its
output shapes explicitly and so tasks can reference a known schema.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OutputSchemaSpec:
    """A named, planned structure for a task's output."""

    name: str
    description: str
    fields: tuple[str, ...]


OUTLINE_OUTPUT = OutputSchemaSpec(
    name="outline_output",
    description="Structured outline with chapters and mandatory-element placement.",
    fields=("chapters", "section_titles", "target_lengths", "element_placement"),
)

DRAFT_OUTPUT = OutputSchemaSpec(
    name="draft_output",
    description="Drafted chapter/section content following the outline.",
    fields=("chapters", "section_texts"),
)

REVIEW_OUTPUT = OutputSchemaSpec(
    name="review_output",
    description="Revised draft plus review notes on mandatory-element coverage.",
    fields=("revised_chapters", "review_notes", "missing_elements"),
)

REFERENCES_OUTPUT = OutputSchemaSpec(
    name="references_output",
    description="Bibliography entries plus an in-text citation map.",
    fields=("bibliography", "citation_map"),
)


def output_schema_specs() -> tuple[OutputSchemaSpec, ...]:
    """Return all planned output schema specifications in a stable order."""
    return (OUTLINE_OUTPUT, DRAFT_OUTPUT, REVIEW_OUTPUT, REFERENCES_OUTPUT)
