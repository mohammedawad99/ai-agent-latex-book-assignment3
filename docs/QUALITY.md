# Quality Strategy

## Purpose

This document defines how quality is enforced in the project: the gates that confirm the generated PDF and the repository meet the mandatory requirements, and the code-quality tooling that keeps the implementation maintainable. Assignment 1 feedback noted that quality standards were not clearly established, so we set them out explicitly here and tie each gate to a concrete check. This is a planning-stage document; it describes the intended quality system, which is implemented across later stages.

## Current Status

No implementation exists yet. Therefore:

- There are **no tests** yet.
- There is **no lint/format configuration** running yet.
- There is **no coverage measurement** yet.
- No quality gate has been executed against a real PDF yet.

Nothing in this document should be read as a passing result. These are planned checks, and their real outcomes will be recorded once they run.

## Planned Quality Gates (Mandatory PDF and Repository Checks)

Each gate is an independent check that produces a pass/fail with evidence, implemented in Stage 12 and run for real in Stage 14. The planned gates:

| Gate | What it checks | Requirement |
| --- | --- | --- |
| Build gate | The LaTeX project compiles successfully | FR-8 / PDF build |
| Page-count gate | The PDF is approximately 15 pages (threshold TBD, e.g. 13–17) | PDF-1 |
| Cover-page gate | Cover present with topic, author(s), course, lecturer, date | PDF-2 |
| ToC gate | Table of contents present | PDF-3 |
| Structure gate | Multiple chapters/sections present | PDF-4 |
| Headers/footers gate | Running headers/footers with page numbers | PDF-5 |
| Image gate | At least one image present | PDF-6 |
| Python-generated graph gate | A Python-generated graph present | PDF-7 |
| Table gate | At least one table present | PDF-8 |
| Formula gate | At least one mathematical formula present | PDF-9 |
| BiDi gate | Hebrew–English bidirectional section present and rendered | PDF-10 |
| Bibliography / citation-link gate | Bibliography present with linked in-text citations | PDF-11 |
| Repository gate | Required files exist (README, PRD, PLAN, TODO, `latex_project/`, `results/`) | Repository requirements |

A run that fails any mandatory gate is reported as failed, not silently accepted. Exact detection methods (PDF text extraction, source inspection, page counting) and the page-count threshold are finalized during implementation and recorded here.

## Planned Code Quality

- **pytest** — unit tests, focused first on the deterministic components (config, evidence, cost tracker, validation gates).
- **ruff** — linting and formatting with project rules.
- **mypy** — optional; the decision to adopt it is made and recorded in Stage 5/13.
- **Coverage target** — a coverage goal for the deterministic modules, enforced in Stage 13 (exact target recorded then).
- **File-length check** — enforce short, maintainable Python files; the limit is recorded here once chosen.
- **Local quality command** — a single command/script that runs lint + tests (and later types + coverage + length check) so quality can be checked from a clean checkout.

## Quality Timeline

To avoid bolting quality on at the end, basic tooling starts early:

- **Stage 5** — basic pytest and ruff configuration are added when `pyproject.toml` is created, plus an initial local quality command and a trivial smoke test.
- **Stage 6** — the first deterministic tests are written, and pytest/ruff/the quality command are run on every deterministic increment.
- **Stages 7–12** — tests accompany the components they cover; validation gates are implemented and tested.
- **Stage 13** — final quality hardening: coverage enforcement, optional mypy finalization, file-length check, command consolidation, and clean-checkout validation.

## No Fake Passing Claims

We do not record a gate or check as passing unless it has actually run and passed on real output. Planned gates are clearly labeled as planned. Real results, with their evidence locations, are added once the checks run.

## Quality Report Locations

- Validation gate reports (machine- and human-readable): `results/validation_reports/`
- Test, lint, and coverage output: produced by the local quality command; key results summarized in this document once available.
- Build logs relevant to the build gate: `results/logs/`
