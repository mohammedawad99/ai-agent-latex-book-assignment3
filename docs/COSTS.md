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

## Run Cost Records

Measured data from real runs. This is **only the minimal wiring-check run** — not
the full pipeline and not the final cost. Token/runtime figures are read straight
from the committed `runtime.json`; no money cost is estimated (Gemini pricing is
not asserted here).

| Run ID / date | Model / provider | Runtime (s) | Prompt tokens | Completion tokens | Agent calls | Retries | PDF build time (s) | Notes / evidence link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stage8b1-minimal-gemini-20260611-154559 / 2026-06-11 | gemini/gemini-2.5-flash / Gemini | 3.181496632001654 | 85 | 33 | 1 (minimal task) | not recorded | n/a (no PDF build yet) | `results/stage8b1-minimal-gemini-20260611-154559/runtime.json` |
| stage8c3-full-gemini-20260611-164153 / 2026-06-11 | gemini/gemini-2.5-flash / Gemini | 249.02091293899866 | 153748 | 200472 | 4 (outline, draft, review, references) | not recorded | n/a (no PDF build yet) | `results/stage8c3-full-gemini-20260611-164153/runtime.json` — technically successful, content **rejected for final PDF** |
| stage8c7-full-gemini-20260611-173125 / 2026-06-11 | gemini/gemini-2.5-flash / Gemini | 300.68034328000067 | 213664 | 235436 | 4 (outline, draft, review, references) | not recorded | n/a (no PDF build yet) | `results/stage8c7-full-gemini-20260611-173125/runtime.json` — technically successful; **candidate** content; not final PDF-ready |

**Important:** the figures above (runtime/tokens) are the project's measured resource
data from `runtime.json`. Numbers that appear *inside the generated text* — e.g.
"185 minutes", "99.1%", "1.8M tokens" in the 8C.7 draft/review — are **not** accepted
project measurements; they are unsupported values produced by the model and must be
removed or replaced during content QA (Stage 8C.8).

The full run (`stage8c3-...`) is the first end-to-end content run: it proves the
runner and persistence work, but its content is rejected (wrong topic, placeholder
author/date, ~10 pages). **Stage 8C.6 hardened topic/metadata binding offline and
incurred no LLM/API cost.** **Stage 8C.7 ran a second full run** (table row above):
~300.7 s, 213,664 + 235,436 tokens, producing accepted **candidate** content (basic
content gate passes) that is **not yet final PDF-ready**. Token/resource data is
recorded from each committed `runtime.json`; no money cost is asserted (Gemini
pricing is not claimed here). **Stages 8C.8.0 (plan), 8C.8.1 (the deterministic
offline QA scanner), and 8C.8.2 (the cleaned Markdown content under
`latex_project/content/`) incurred no LLM/API cost** — pure string checks and
human-reviewed text editing, no real run, no `kickoff`, no new tokens. The
cleaned content reuses the already-measured 8C.7 run values rather than
generating new ones. Further token cost would only arise if content QA later
requires a constrained re-run. **Stage 9.0 (the LaTeX assembly plan, D-030) is
likewise docs-only and incurred no LLM/API cost** — no real run, no `kickoff`,
no tokens; the planned Stages 9.1–9.6 are deterministic (TeX Live compilation
and matplotlib scripts) and are expected to incur no LLM/API cost either.

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
Stage 8B.0 installed the Gemini provider dependency (`crewai[google-genai]`) with no
real call. **Stage 8B.1 performed the first real run:** a single minimal Gemini
`kickoff` to `gemini/gemini-2.5-flash` (3.18 s; 85 prompt + 33 completion tokens),
recorded in the table below from its committed `runtime.json`. This is a tiny
wiring-check run only — **not the full pipeline and not the final cost**, and no
money figure is asserted (provider pricing is not claimed here). Stage 8C.1 added
the offline `run-full` scaffolding and **incurred no LLM/API cost** (no real run,
no `kickoff`, no tokens). Fuller figures follow at the first full content-generation
run (Stage 8C.3) and the end-to-end run (Stage 14).
