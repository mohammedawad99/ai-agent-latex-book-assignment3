# ai-agent-latex-book-assignment3

> Draft placeholder for planning. No implementation has been completed yet.

A CrewAI-based multi-agent pipeline that generates an approximately 15-page
article/book and produces a polished PDF using LaTeX.

## Status

**Stage 0 — Repository skeleton only.**
No agents, no LaTeX content, and no generated outputs exist yet. This repository
currently contains only the planned directory structure and placeholder
documentation to support later PRD, planning, implementation, and submission work.

## Planned structure

```
docs/                          Planning and process documentation
src/agentic_latex_book/        Python package for the CrewAI pipeline
scripts/                       Helper / automation scripts
tests/                         Test suite
latex_project/                 LaTeX source for the generated book
results/                       Reproducible run evidence
  logs/                        Execution logs
  crew_outputs/                Raw agent / crew outputs
  validation_reports/          Quality-gate and validation reports
  final_pdf/                   Final compiled PDF deliverable
assets/                        Static and generated supporting assets
  figures/                     Authored figures
  generated/                   Programmatically generated assets
```

## Documentation

| Document | Purpose |
| --- | --- |
| [docs/PRD.md](docs/PRD.md) | Product requirements |
| [docs/PLAN.md](docs/PLAN.md) | Implementation plan |
| [docs/TODO.md](docs/TODO.md) | Task tracking |
| [docs/AI_WORKFLOW.md](docs/AI_WORKFLOW.md) | AI-assisted workflow documentation |
| [docs/PROMPTS.md](docs/PROMPTS.md) | Prompt log |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Decision log |
| [docs/COSTS.md](docs/COSTS.md) | Cost tracking |
| [docs/QUALITY.md](docs/QUALITY.md) | Quality gates |
| [docs/SUBMISSION_CHECKLIST.md](docs/SUBMISSION_CHECKLIST.md) | Submission checklist |
