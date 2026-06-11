# Prompts Log

## Purpose

This document records the AI prompts used during the project so the workflow is transparent and reviewable, as required by the course. It is a running log: entries are added as work proceeds. To keep it readable and avoid leaking noise, entries are written as concise **summaries** of each prompt and its intent rather than full raw transcripts.

## Prompt Logging Policy

- Log a summary entry for each meaningful AI-assisted task (a document, a component, a review pass).
- Record what was asked for, the important constraints we imposed, what artifact resulted, and the result of our review.
- Do not paste secrets, API keys, or environment values into this log.
- Do not claim an artifact exists or works if it does not. Entries describe only work actually performed.
- Where a tool/model is not yet decided (planning stages used a general AI assistant; the pipeline model/provider is chosen in Stage 5), record it as such rather than guessing.

## Prompt Record Template

Use this template for new entries:

| Field | Description |
| --- | --- |
| Stage | Project stage number |
| Date | Date of the prompt (YYYY-MM-DD) |
| Goal | What the prompt aimed to achieve |
| Tool/Model | The AI tool/model used, if known |
| Prompt summary | A short description of what was asked |
| Important constraints | Key rules imposed (e.g. docs-only, no code, no fake evidence) |
| Output artifact | The file(s) produced or changed |
| Review result | Outcome of group review (accepted / revised / rejected) |

## Logged Prompts (Stages 0–4)

These entries summarize the AI-assisted work already completed. They are summaries, not raw prompts. No code was generated in these stages — the work was repository structure and planning documentation only.

| Stage | Date | Goal | Tool/Model | Prompt summary | Important constraints | Output artifact | Review result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-06-11 | Create a clean repository skeleton | AI coding assistant | Asked to create the directory structure, placeholder docs, `.gitignore`, and package init, with no implementation | Skeleton only; no code; no fake outputs; preserve empty dirs | Repository skeleton (commit `a0f8734`) | Accepted |
| 1 | 2026-06-11 | Write a professional PRD | AI coding assistant | Asked to write a full PRD (problem, goals, scope, requirements, acceptance criteria, traceability) from the assignment brief | Plan only; no implementation; evidence-first; group submission | `docs/PRD.md` (commit `b501a36`) | Accepted after targeted submission fixes |
| 2 | 2026-06-11 | Write a technical PLAN | AI coding assistant | Asked to design the architecture and strategy strictly from the PRD | Design only; no code/deps/LaTeX; do not invent features | `docs/PLAN.md` (commit `6baece3`) | Accepted |
| 3 | 2026-06-11 | Write a detailed staged TODO | AI coding assistant | Asked to break the PLAN into staged, actionable checklist tasks | Task plan only; ≥120 checkboxes; match PLAN roadmap | `docs/TODO.md` (commit `a722f64`) | Accepted after quality-timing correction |
| 4 | 2026-06-11 | Write supporting documentation | AI coding assistant | Asked to write AI_WORKFLOW, PROMPTS, DECISIONS, COSTS, QUALITY, SUBMISSION_CHECKLIST, and an initial README | Docs only; planned-status wording; no implementation claims | This document and the other Stage 4 files | Accepted for initial Stage 4 documentation after review |

## Future Prompts

Implementation-stage prompts (Stage 5 onward) will be added here as the project proceeds — for example prompts used to draft the config loader, the crew builder, the LaTeX assembler, the figure generator, the PDF builder, and the validation gates. Until those stages run, no claim is made that any code has been generated. This log will grow alongside the actual work.
