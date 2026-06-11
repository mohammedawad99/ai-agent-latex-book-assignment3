# ai-agent-latex-book-assignment3

A CrewAI multi-agent pipeline that generates an approximately 15-page article/book and compiles it into a polished PDF using LaTeX.

## Group

- **Group code:** MaRs-777
- **Members:** Mohamed Awad, Rawey Sleiman
- **Maintainer:** Mohamed Awad

## Assignment Context

This is Assignment 3 for the AI Agents / Vibe Coding course. The task is to build a multi-agent system, orchestrated with CrewAI, that writes a ~15-page article/book on a chosen topic and produces a professional LaTeX PDF. The work is graded as a software engineering project: the repository must show a clear engineering process (planning, a real LaTeX project, reproducible runs, quality checks) and a meaningful commit history. The generated PDF is the main evaluated artifact.

Working topic for the generated book: *"From PoC to Production: Building Reliable AI Agent Systems with CrewAI, LaTeX, Observability, Security, and Cost Awareness."*

## Current Status

**Planning / documentation stage. No implementation exists yet.**

Completed and pushed so far:

| Stage | Description | Commit |
| --- | --- | --- |
| 0 | Repository skeleton and initial GitHub setup | `a0f8734` |
| 1 | PRD (`docs/PRD.md`) | `b501a36` |
| 2 | PLAN (`docs/PLAN.md`) | `6baece3` |
| 3 | TODO (`docs/TODO.md`) | `a722f64` |
| 4 | Supporting documentation (this set) | Stage 4 documentation prepared |

There is currently no pipeline code, no dependencies, and no LaTeX sources. Everything in the "planned" sections below is design intent, not working software.

## What This Project Will Build

A pipeline that takes a topic and configuration as input and produces:

- a ~15-page LaTeX PDF satisfying all mandatory elements (cover page, table of contents, chapters, headers/footers, an image, a Python-generated graph, a table, a mathematical formula, a Hebrew–English bidirectional section, and a bibliography with linked citations);
- the LaTeX project used to build it;
- evidence from real runs (logs, agent outputs, validation reports, the final PDF);
- a record of cost/resource usage.

## Planned Architecture Summary

The design separates the agentic layer from the deterministic layer:

- **CrewAI agents** plan, write, and review the content (planner/outliner, writer, reviewer/editor, reference curator).
- **Deterministic Python** assembles the LaTeX, generates the graph, builds the PDF, and validates the mandatory requirements.

This keeps PDF correctness under deterministic checks rather than trusting model output. See `docs/PLAN.md` for the full design.

## Repository Structure

```
docs/                          Planning and process documentation
src/agentic_latex_book/        Python package for the CrewAI pipeline (not implemented yet)
scripts/                       Helper / automation scripts (planned)
tests/                         Test suite (planned)
latex_project/                 LaTeX source for the generated book (planned)
results/                       Reproducible run evidence (real runs only)
  logs/                        Execution logs
  crew_outputs/                Raw agent / crew outputs
  validation_reports/          Quality-gate and validation reports
  final_pdf/                   Final compiled PDF deliverable
assets/figures/                Authored figures
assets/generated/              Python-generated assets
```

## Planned Usage (Not Working Yet)

> The commands below are **planned** for later stages. They do not work yet because the implementation does not exist. They are listed here to show the intended workflow and will be finalized in Stage 5 (setup) and Stage 11 (PDF build).

- Project setup and dependency installation will be defined in Stage 5 (uv + `pyproject.toml`).
- Running the pipeline via a CLI entry point will be defined in Stages 5–8.
- Building the PDF via a reproducible script under `scripts/` will be defined in Stage 11.

Exact, runnable commands will be added to this README only once they actually work.

## Development Workflow

The project follows a staged plan (`docs/TODO.md`): skeleton → PRD → PLAN → TODO → supporting docs → setup → deterministic foundation → CrewAI core → content generation → LaTeX assembler → graph/assets → PDF build → validation → testing/quality hardening → real end-to-end run → documentation hardening → submission. Each stage is committed and pushed in meaningful increments with standard student authorship.

## Quality and Evidence Policy

- Mandatory PDF and repository requirements are checked by automated quality gates (see `docs/QUALITY.md`).
- All evidence under `results/` comes from real runs only; no fabricated outputs.
- Cost/resource usage is tracked honestly from measured data (see `docs/COSTS.md`).
- The project does not overclaim production readiness; it is a proof-of-concept-to-production exercise with stated limitations.

## Documentation

| Document | Purpose |
| --- | --- |
| [docs/PRD.md](docs/PRD.md) | Product requirements |
| [docs/PLAN.md](docs/PLAN.md) | Technical architecture plan |
| [docs/TODO.md](docs/TODO.md) | Staged task plan |
| [docs/AI_WORKFLOW.md](docs/AI_WORKFLOW.md) | How AI assistance is used |
| [docs/PROMPTS.md](docs/PROMPTS.md) | Prompt log |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Decision log |
| [docs/COSTS.md](docs/COSTS.md) | Cost / resource tracking |
| [docs/QUALITY.md](docs/QUALITY.md) | Quality strategy |
| [docs/SUBMISSION_CHECKLIST.md](docs/SUBMISSION_CHECKLIST.md) | Submission checklist |

## Submission Note

Two separate PDFs are involved in this assignment:

1. The **generated article/book PDF** — produced by the pipeline, stored in `results/final_pdf/`; this is the main evaluated artifact.
2. The **Moodle submission PDF** — `MaRs-777-ex03.pdf`, created separately from the official Word template, carrying the exercise number, group code, GitHub link, and final self-assessment score.

The GitHub repository will be public or shared with the lecturer at rmisegal@gmail.com before submission.
