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

## Minimal-Run Metadata Format (Stage 8A scaffolding)

The Stage 8A runner is prepared to write a per-run `runtime.json` for the first
real minimal run (Stage 8B). It captures only safe, non-secret fields:

```json
{
  "label": "run-minimal",
  "started_at": <unix-seconds>,
  "ended_at": <unix-seconds>,
  "elapsed_seconds": <float>,
  "prompt_tokens": <int|null>,
  "completion_tokens": <int|null>,
  "model": "<model-name>",
  "llm_environment": {
    "provider": "openai",
    "model": "<model-name>",
    "base_url_present": <bool>,
    "api_key_present": <bool>
  }
}
```

Token fields are `null` when the provider does not expose usage; that is recorded
honestly as "not available" rather than estimated. No API key or base-URL value is
ever written — only presence booleans.

## Honest Reporting Policy

- Record **measured data only**. Do not present estimates as facts.
- If a metric is unavailable (for example, tokens not exposed by the provider), write "unavailable" and explain why.
- Note any assumptions behind a figure (for example, the model version or pricing basis) next to it.
- Do not retroactively invent costs for stages that did no paid work.

## Current Cost Note (through Stage 8A)

Stages 0–4 are documentation-only. Stages 5–7 added project setup and the offline
CrewAI core. Stage 8A added the controlled-run scaffolding (LLM resolver, minimal
runner, `run-minimal` CLI) and its offline tests — but performed **no real run**:
no `kickoff`, no LLM/API call, no tokens consumed, and no `runtime.json` written.
Stage 8A.1 extended the resolver with Gemini provider support, still fully offline.
Stage 8B.0 installed the Gemini provider dependency (`crewai[google-genai]`) so a
Gemini `LLM` can be constructed — but **no real Gemini call or cost occurred in
Stage 8B.0**: the dependency was installed and an offline construction test added,
with no `kickoff` and no model call. **No cost was incurred in Stages 8A, 8A.1, or
8B.0.** The only resources used so far are local editing, testing, dependency
installation, and Git operations, which are not metered for this assignment. The
first real cost data is expected when the student executes the minimal run
(Stage 8B.1); fuller figures follow at the end-to-end run (Stage 14).
