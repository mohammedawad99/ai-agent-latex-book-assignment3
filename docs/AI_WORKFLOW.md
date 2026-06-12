# AI Workflow

## Purpose

This document explains how AI assistance is used in this project and how that use is kept transparent, reviewable, and honest. The course treats the AI-assisted workflow as part of the deliverable, so we document it deliberately rather than hiding it. This is a planning-stage document: it describes how we intend to work as the project moves from documentation into implementation, and it will be updated to reflect what actually happened as work proceeds.

## How AI Assistance Is Used

AI assistance is used as a drafting and reasoning aid under human direction. In practice that means:

- Helping draft and refine planning documents (PRD, PLAN, TODO) and the supporting documents in this folder.
- Helping reason about architecture options, trade-offs, and risks.
- Later, helping draft and review implementation code, LaTeX, and validation logic.
- Helping check documents and code for consistency, gaps, and unclear wording.

AI is a tool in the loop. It does not make final decisions, and it does not get to declare work "done." Those are group responsibilities.

## Student Responsibility and Review Policy

The group (MaRs-777: Mohamed Awad, Rawey Sleiman) is responsible for everything in this repository, regardless of how a given artifact was drafted. Our review policy:

- Every AI-assisted artifact is read and reviewed by a group member before it is committed.
- We confirm that documents match the actual state of the project and do not claim more than is true.
- We confirm that any code (in later stages) is understood by the group, not just pasted in.
- We confirm that any evidence committed comes from a real run, not from a model's description of a hypothetical run.

If something is unclear or unverified, we mark it as open rather than presenting it as settled.

## Boundaries

The division of responsibility we follow:

- **AI may:** help plan, draft, write, refactor, and review.
- **The group owns:** decisions, validation, correctness, and submission. The group is accountable for the result.

Concretely, AI can propose an architecture or a validation gate, but the group decides whether to adopt it, and the group is responsible for confirming that a gate actually passes on real output.

## How Prompts, Decisions, Evidence, and Costs Are Tracked

- **Prompts** — summarized in `docs/PROMPTS.md` using a consistent template (stage, date, goal, tool/model, prompt summary, constraints, output artifact, review result).
- **Decisions** — recorded in `docs/DECISIONS.md` as numbered decision records with context, alternatives, rationale, and consequences.
- **Evidence** — stored under `results/` (logs, crew outputs, validation reports, final PDF) and produced only by real runs in later stages.
- **Costs** — recorded in `docs/COSTS.md` (runtime, token usage where the provider exposes it, model/provider, agent-call counts), reported from measured data only.

## Rules

These rules are binding for the whole project:

- **No fake evidence.** Results are committed only after a real run produces them. Until then, `results/` holds only structural placeholder markers.
- **No overclaiming production readiness.** This is a credible proof-of-concept-to-production exercise, not a finished production system. Limitations are stated plainly.
- **Standard student authorship in Git.** Commits are authored by the student/group with normal Git identity. We do not add AI/bot/co-author/generated-by metadata to commits or files. The AI-assisted workflow is documented here, in plain description, rather than as commit boilerplate.

## Staged Workflow

The project follows this order, with each stage reviewed before the next begins:

1. **PRD** — define the problem, goals, scope, and acceptance criteria (`docs/PRD.md`).
2. **PLAN** — design the architecture and strategy (`docs/PLAN.md`).
3. **TODO** — break the plan into staged, actionable tasks (`docs/TODO.md`).
4. **Supporting docs** — this stage: AI workflow, prompts, decisions, costs, quality, submission checklist, and an initial README.
5. **Setup** — project tooling, dependencies, and a CLI skeleton (Stage 5).
6. **Implementation** — deterministic foundation, then the CrewAI pipeline, assembler, figures, and PDF build (Stages 6–11).
7. **Validation** — quality gates that check the mandatory PDF and repository requirements (Stage 12).
8. **Evidence** — a real end-to-end run that produces logs, outputs, reports, and the final PDF (Stage 14).
9. **Submission** — final documentation hardening and the final repository review / GitHub submission (Stages 15–16).

## Current Status

Stages 0–3 (skeleton, PRD, PLAN, TODO) are complete and pushed. Stage 4 (this supporting-documentation set) is in progress. No implementation code, dependencies, or LaTeX sources exist yet. Everything beyond Stage 4 is described as planned.
