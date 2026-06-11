# Cleaned Content (`latex_project/content/`)

This directory holds the **cleaned Markdown source** for the article/book. It is
the input for the later LaTeX-assembly stage. No LaTeX or PDF is produced here.

## What this is

- `book.md` — the cleaned, human-reviewed content for the article
  *From PoC to Production: A CrewAI Multi-Agent Pipeline for Generating a LaTeX Book*
  (group MaRs-777; authors Mohamed Awad, Rawey Sleiman; date June 11, 2026).
- `README.md` — this file.

## Source evidence

This content is **derived** from one real full pipeline run, recorded as
immutable evidence at:

```
results/stage8c7-full-gemini-20260611-173125/
```

The cleaned text in `book.md` was edited by the students from that run's
`crew_outputs/` (outline and draft), with the measured cost figures taken from
the same run's `runtime.json` and `crew_outputs/_index.json`.

## Evidence was not edited

The original run evidence under
`results/stage8c7-full-gemini-20260611-173125/` was **not** modified in any way.
It remains the immutable record of what the model produced. This `book.md` is a
separate, derived artifact; the evidence and the cleaned content are kept apart
on purpose.

## What the cleanup changed

The raw run was on-topic but not yet publication-ready. The students removed or
rewrote the known risks before LaTeX assembly:

- removed fabricated citation links and placeholder reference entries, replacing
  them with a conservative bibliography of well-known sources plus
  project-internal references that actually exist in this repository;
- removed aggregate performance numbers that were never measured, and replaced
  them with the actual measured cost of the recorded run (runtime and token
  counts read straight from `runtime.json`), clearly separating measured results
  from proposed future metrics;
- removed references to a specific commercial model report, using neutral "LLM"
  wording or the model actually used in the run
  (`gemini/gemini-2.5-flash`);
- replaced wording that described running headers and footers only in the
  abstract with an explicit statement that they will be implemented during LaTeX
  assembly using the document title, the group code, and automatic page numbers;
- removed hand-written page markers in favour of chapter/section structure, so
  page numbers are produced by LaTeX at compile time.

## How this content is gated

The cleaned content must pass the deterministic offline content-QA scanner
before it is committed and before LaTeX assembly. The scanner command is:

```
uv run agentic-latex-book content-qa latex_project/content/
```

It exits `0` only when the content contains the required topic, the group code,
both authors, an accepted date, and every mandatory PDF element, and contains
none of the blocking risks. The scanner is offline, uses no model or API key,
and modifies nothing.

## Status

LaTeX and PDF assembly are **future stages**. This directory currently contains
cleaned Markdown source only — no `.tex` and no `.pdf` files exist yet.
