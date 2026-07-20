---
type: instrument
started: 2026-01-15
last-updated: 2026-01-15
review-trigger: 2026-02-15 · hard floor 8 rows
status: OPEN — 0 rows
---
# <Name> — measurement log

**What this measures:** the suspicion, stated as a testable claim. Example:
"the summary layer loses nuance that forces full-source reads."

**Why it exists:** the operator's instinct that triggered it, dated and tagged.
An instrument turns a recurring argument into a measurement.

## Baseline
Whatever you measured when creating this (costs, ratios, counts), so the log
has something to compare against.

## Decision rule (current, to be tested by this log)
The rule you're operating under while data accumulates — stated so the log can
prove it wrong.

## Log
One row per event, logged **at the moment it happens**, not reconstructed later.

| # | Date | Event | What was needed | What was used | Sufficed? | What was missing |
|---|---|---|---|---|---|---|
| | | | | | | |

## Analysis (fires at the trigger date, IF ≥ floor rows)
The computation, written in advance so the trigger can't be gamed:
- the metric (e.g. % of events where the cheap layer sufficed)
- the thresholds and what each implies (keep / tighten / fix upstream)
- segment by any column that separates "the layer failed" from "the fallback
  wasn't available" — pooling those blames the wrong system.

If the date arrives under the floor: report the row count and let the operator
decide. A thin log is itself a finding (the event is rarer than assumed);
averaging noise is worse than waiting.
