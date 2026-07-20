# Daily briefing — YYYY-MM-DD

## Ingest pull
What arrived from pipelines/other systems since the last briefing. New meeting
notes read (cheap layer first), anything that contradicts vault state flagged
CONFLICT rather than merged.

## Calendar
| Time | What | Prep |
|---|---|---|

## Ledger — due / overdue / new
Open items due today or slipped, from `30_ledger/ledger.md` (## Open only —
reads stop at the archive marker).

## Stale (max 5, oldest first)
Items untouched longest. Five, not fifty... the cap is what keeps this read.

## Flags
- CONFLICTs awaiting the operator
- [gap]s worth filling this week
- Anything the instruments tripped

## Commit step (end of briefing, non-optional)
Write agreed changes back: goals changelog, ledger flips, entity pages. Run the
index generator. Then save this briefing to `40_views/daily/YYYY-MM-DD.md` and
commit. The briefing that isn't saved didn't happen.
