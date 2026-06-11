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

**Project setup stage. A safe CLI skeleton, uv setup, pytest, and ruff are configured. The CrewAI pipeline itself is not implemented yet.**

Completed and pushed so far:

| Stage | Description | Commit |
| --- | --- | --- |
| 0 | Repository skeleton and initial GitHub setup | `a0f8734` |
| 1 | PRD (`docs/PRD.md`) | `b501a36` |
| 2 | PLAN (`docs/PLAN.md`) | `6baece3` |
| 3 | TODO (`docs/TODO.md`) | `a722f64` |
| 4 | Supporting documentation | `495f966` |
| 5 | Project setup (uv, deps, CLI skeleton) | `d21b3c7` |

There are declared dependencies and a safe CLI skeleton, but no CrewAI agents, no LLM calls, no LaTeX sources, no PDF build, and no generated evidence yet. Everything in the "planned" sections below is design intent, not working software.

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

## Setup and Working Commands (Stage 5)

The project uses [uv](https://docs.astral.sh/uv/) for environment and dependency
management. The following commands work now:

```bash
# Create/sync the virtual environment from pyproject.toml + uv.lock
uv sync

# Show the CLI help (safe, offline)
uv run agentic-latex-book --help

# Print current project status (safe, offline; does not run the pipeline)
uv run agentic-latex-book

# Run the test suite
uv run pytest

# Lint and format checks
uv run ruff check .
uv run ruff format --check .
```

Secrets: copy `.env.example` to `.env` and fill in real values locally. Never
commit a real `.env`.

> The CLI is a **setup skeleton only**. It reports status and does not run
> CrewAI, call an LLM, or build a PDF — none of that is implemented yet.

## Planned Usage (Not Working Yet)

> The items below are **planned** for later stages and do not work yet.

- Running the full CrewAI pipeline will be defined in Stages 6–8.
- Building the PDF via a reproducible script under `scripts/` will be defined in Stage 11.

Exact, runnable pipeline commands will be added to this README only once they actually work.

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
