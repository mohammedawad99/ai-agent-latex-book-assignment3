"""Context-bound task instructions for the content-generation crew.

The instruction builders take a ``ProjectContext`` and produce descriptions that
bind the crew to the configured topic and cover metadata, and explicitly forbid
the failure modes seen in the first full run (wrong topic, placeholders, stale
date, too-short content). See decision D-025.
"""

from __future__ import annotations

from agentic_latex_book.crew.context import ProjectContext

# Mandatory PDF elements (PRD PDF-1..PDF-11). Defined once and reused.
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


def _constraints(ctx: ProjectContext) -> str:
    return (
        f'Write strictly about this project topic: "{ctx.topic}". Do NOT write '
        "about any unrelated topic — in particular do NOT produce a Gradient "
        "Descent / generic machine-learning article. Use the real cover metadata: "
        f"group {ctx.group_code}, authors {ctx.authors_text}, date {ctx.project_date}. "
        "Never use placeholder fields such as [Your Name], [Your Name/Placeholder "
        "Name], [Optional Affiliation/Institution], or a stale date like October "
        f"2023. Target approximately {ctx.page_count_min}-{ctx.page_count_max} pages "
        "(about 15)."
    )


def outline_instructions(ctx: ProjectContext) -> str:
    return (
        f"{_constraints(ctx)} Produce a structured outline for the ~15-page "
        "article/book. Decide chapter/section titles and target lengths, and "
        "assign where each mandatory PDF element will appear: "
        f"{_ELEMENTS_TEXT}. The cover page must show the real topic, group, "
        "authors, course/assignment context, and the configured date."
    )


def draft_instructions(ctx: ProjectContext) -> str:
    return (
        f"{_constraints(ctx)} Write the chapter/section content following the "
        "outline and its target lengths. Keep the writing clear, professional, "
        "and free of marketing tone. Expand explanations enough to reach about "
        "15 pages; do not stop at ~10 pages."
    )


def review_instructions(ctx: ProjectContext) -> str:
    return (
        f"{_constraints(ctx)} Review the draft against the outline and explicitly "
        "check for and report: (a) wrong/unrelated topic, (b) any placeholder "
        "author/date fields, (c) too-short length (under ~15 pages), (d) missing "
        f"mandatory PDF elements ({_ELEMENTS_TEXT}), and (e) a weak bibliography or "
        "citation map. List every problem found and request fixes."
    )


def references_instructions(ctx: ProjectContext) -> str:
    return (
        f"{_constraints(ctx)} Assemble a bibliography with linked in-text "
        "citation points relevant to the actual topic: CrewAI and agentic "
        "multi-agent workflows, LaTeX / BiDi / PDF generation, and software "
        "engineering process. Do NOT cite Gradient Descent or unrelated ML "
        "sources. Map each citation point to the content for human review."
    )
