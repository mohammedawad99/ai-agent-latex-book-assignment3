# Cost and Resource Tracking

## Purpose

This document tracks the cost and resource usage of the project, so that resource awareness is visible rather than hidden. Assignment 1 feedback noted that cost/resource awareness was missing, so we treat it as a first-class concern here. All figures recorded in this document must come from measured data; where a number is not available, we say so plainly instead of estimating.

## Current Status

No LLM/API runs have been performed yet. The project is at the documentation stage (Stages 0–4), which involves repository structure and writing planning documents only. Therefore:

- There is **no measured token usage** yet.
- There is **no measured API cost** yet.
- There is **no PDF build time** yet, because no LaTeX build has run.

This section will be updated with real measurements once the pipeline runs (Stage 14).

## What Will Be Tracked Later

Once implementation and real runs begin, each run will record:

- **Runtime** — wall-clock time per run and, where practical, per stage.
- **Token usage** — prompt/completion tokens where the model provider exposes them.
- **Model / provider** — which model was used (decided in Stage 5).
- **Number of agent calls** — how many agent/task invocations a run made.
- **Retries / re-draft iterations** — how many bounded re-draft loops were triggered.
- **PDF build time** — time taken by the LaTeX compilation step.

If the provider does not expose token counts, that limitation is stated rather than filled with invented numbers.

## Cost Evidence Locations

- Per-run logs: `results/logs/`
- Raw crew outputs (useful for counting agent calls): `results/crew_outputs/`
- Validation reports (build/run context): `results/validation_reports/`
- The summarized cost figures: this document, referencing the underlying run records.

## Future Run Cost Record Template

Use this table for each real run once measurements exist:

| Run ID / date | Model / provider | Runtime (s) | Prompt tokens | Completion tokens | Agent calls | Retries | PDF build time (s) | Notes / evidence link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| _none yet_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | _n/a_ | No paid run has been performed |

## Honest Reporting Policy

- Record **measured data only**. Do not present estimates as facts.
- If a metric is unavailable (for example, tokens not exposed by the provider), write "unavailable" and explain why.
- Note any assumptions behind a figure (for example, the model version or pricing basis) next to it.
- Do not retroactively invent costs for stages that did no paid work.

## Current Stage 0–4 Cost Note

Stages 0–4 are documentation-only. No paid API run has been recorded, no tokens were consumed by the pipeline (which does not exist yet), and no LaTeX build has been performed. The only resources used so far are local editing and Git operations, which are not metered for this assignment. The first real cost data is expected at Stage 14, when the end-to-end pipeline runs for real.
