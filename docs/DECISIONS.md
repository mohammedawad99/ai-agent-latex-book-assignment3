# Decision Log

## Purpose

This document records the significant decisions made during the project, so the reasoning behind the design is visible and can be revisited. Each decision is a numbered record with enough context to understand why it was made and what it implies. Decisions can be revised later; when that happens, we add a new record or update the status rather than silently rewriting history.

## Decision Record Format

Each record uses these fields:

- **ID** — `D-NNN`.
- **Date** — when the decision was made (YYYY-MM-DD).
- **Status** — Accepted / Superseded / Revisit at Stage N.
- **Context** — the situation that required a decision.
- **Decision** — what was decided.
- **Alternatives considered** — other options we weighed.
- **Rationale** — why we chose this option.
- **Consequences** — what follows from it.

---

## D-001 — Repository / Project Name

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** Assignment 3 needs its own repository, clearly separated from earlier assignments.
- **Decision:** Use the repository/project name `ai-agent-latex-book-assignment3`.
- **Alternatives considered:** Reusing or renaming an earlier assignment repository; a shorter generic name.
- **Rationale:** A descriptive, assignment-specific name avoids confusion with Assignment 2 and makes the submission link unambiguous.
- **Consequences:** The submitted GitHub link and the Moodle wrapper PDF must reference this exact repository.

## D-002 — Documentation-First Workflow

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** Assignment 1 feedback flagged weak planning and low visibility of process.
- **Decision:** Complete PRD, PLAN, TODO, and supporting documentation before writing implementation code.
- **Alternatives considered:** Start coding immediately and document afterwards.
- **Rationale:** Doc-first work makes scope, acceptance criteria, and the engineering process explicit, and directly addresses prior feedback.
- **Consequences:** Stages 0–4 produce no code; dependencies and implementation begin at Stage 5.

## D-003 — CrewAI as the Orchestration Mechanism

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** The assignment requires a multi-agent system, and the course specifies CrewAI.
- **Decision:** Use CrewAI as the required orchestration mechanism for the agent pipeline.
- **Alternatives considered:** Other agent frameworks; a single-prompt approach.
- **Rationale:** CrewAI is the mandated framework and fits a multi-role writing/review pipeline.
- **Consequences:** The content-generation layer is built on CrewAI; the model/provider behind it is decided separately (see D-007).

## D-004 — Separate Agentic Generation from Deterministic Build/Validation

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** PDF correctness must be guaranteed, but model output is not deterministic.
- **Decision:** Let CrewAI agents handle writing/review, and handle LaTeX assembly, PDF build, and validation with deterministic Python code.
- **Alternatives considered:** An all-agent pipeline that also assembles and validates.
- **Rationale:** Correctness of the mandatory PDF elements should be enforced by code and checks, not by trusting a model's claims; this supports the evidence-first principle.
- **Consequences:** Clear module boundaries; validation gates are independent, testable Python.

## D-005 — Include the LaTeX Project in the Repository

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** The assignment requires the LaTeX sources used to build the PDF to be available.
- **Decision:** Keep all LaTeX sources under `latex_project/` in the repository; ignore only transient build artifacts.
- **Alternatives considered:** Committing only the final PDF; generating LaTeX outside the repo.
- **Rationale:** Including the sources is required and makes the build reproducible and reviewable.
- **Consequences:** `.gitignore` must exclude build artifacts while keeping sources and the final PDF tracked.

## D-006 — Article PDF and Moodle Wrapper PDF Are Separate

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** The submission requires a Moodle wrapper document distinct from the generated article.
- **Decision:** Treat the generated article/book PDF (the main evaluated artifact) and the Moodle submission PDF (`MaRs-777-ex03.pdf`) as two separate deliverables.
- **Alternatives considered:** Submitting only the article PDF; merging both into one file.
- **Rationale:** They serve different purposes — the article is the evaluated output; the wrapper carries submission metadata (exercise number, group code, GitHub link, self-score).
- **Consequences:** The wrapper is created manually from the official Word template, not produced by the pipeline.

## D-007 — Defer Dependencies and Model/Provider Choice to Stage 5

- **Date:** 2026-06-11
- **Status:** Revisit at Stage 5
- **Context:** Choosing dependencies and an LLM provider early would lock in decisions before setup.
- **Decision:** Add no dependencies and choose no model/provider until Stage 5 (Project Setup).
- **Alternatives considered:** Selecting the model and libraries during planning.
- **Rationale:** Keeps the planning stages clean and avoids premature commitment; the choice has cost and BiDi implications best handled at setup.
- **Consequences:** No `pyproject.toml` exists yet; the model/provider, plotting library, and LaTeX engine are open questions tracked in PLAN §27 and TODO §11.

## D-008 — Evidence Only From Real Runs

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** Assignment feedback emphasized that claims must be backed by evidence, not description.
- **Decision:** Commit evidence (logs, crew outputs, validation reports, final PDF) only when produced by a real run; never fabricate placeholder results.
- **Alternatives considered:** Adding sample/mock evidence to illustrate structure.
- **Rationale:** Fabricated evidence would be dishonest and would undermine the whole submission.
- **Consequences:** `results/` holds only `.gitkeep` markers until Stage 14 produces real artifacts.

## D-009 — Incremental GitHub Commit History

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** A professional process should be visible in the repository history.
- **Decision:** Commit and push at meaningful increments throughout the project, not in a single final dump.
- **Alternatives considered:** Developing locally and pushing everything at the end.
- **Rationale:** Incremental history demonstrates the engineering process and makes review easier.
- **Consequences:** Each stage is its own commit (or coherent set of commits) with standard student authorship.

---

## Open Decisions (To Be Recorded Later)

The following are not yet decided and will become decision records when resolved (sourced from PLAN §27 / TODO §11):

- LLM provider/model for CrewAI (Stage 5).
- Python plotting library for the generated graph (Stage 5/10).
- LaTeX engine and BiDi package (Stage 9/11).
- Sequential vs parallel chapter drafting (Stage 8).
- Page-count threshold for the page-count gate (Stage 12).
- Whether to adopt mypy and whether to add CI (Stage 13).
