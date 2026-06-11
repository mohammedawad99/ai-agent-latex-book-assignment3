"""Project context derived from config, injected into the crew task instructions.

Keeping the project topic and cover metadata in one small object lets the task
descriptions be bound to the real assignment topic instead of a generic one.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentic_latex_book.config import Config


@dataclass(frozen=True)
class ProjectContext:
    """Topic and cover metadata that the crew must follow."""

    topic: str
    group_code: str
    authors: tuple[str, ...]
    assignment_context: str
    project_date: str
    page_count_min: int
    page_count_max: int

    @property
    def authors_text(self) -> str:
        return ", ".join(self.authors) if self.authors else "the group members"


def project_context(config: Config) -> ProjectContext:
    """Build a ProjectContext from a validated Config."""
    return ProjectContext(
        topic=config.topic,
        group_code=config.group_code,
        authors=config.authors,
        assignment_context=config.assignment_context,
        project_date=config.project_date,
        page_count_min=config.page_count_min,
        page_count_max=config.page_count_max,
    )


# A generic fallback for structural/offline uses that do not need real metadata
# (e.g. validation of the task graph, the offline crew-plan listing).
GENERIC_CONTEXT = ProjectContext(
    topic="the configured project topic",
    group_code="",
    authors=(),
    assignment_context="",
    project_date="",
    page_count_min=13,
    page_count_max=17,
)
