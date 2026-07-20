# Commitment Ledger

Grammar: `- [ ] YYYY-MM-DD · @owner · commitment · due:YYYY-MM-DD|none · src:[[slug]] · [S]|[M]|[AI]`

States: open `[ ]`, done `[x]`, plus inline `STALE`/`DROPPED`. Nothing is ever
deleted; done/dropped lines migrate to `## Archive` monthly. Status changes are
appended to the line (`— STATUS 2026-02-01: ...`), never rewritten over.

## Open

- [ ] 2026-01-15 · @operator · Get the partnership terms in writing · due:2026-01-31 · src:[[acme-studios]] · [S]
- [ ] 2026-01-15 · @cos-ai · Draft the intro note for review · due:2026-01-17 · src:[[jane-doe]] · [S]
- [ ] 2026-01-16 · @jane · Send the revised deck (her commitment, tracked here) · due:none · src:[[2026-01-15_jane-1on1]] · [M]

## Needs review

- Lines whose src: doesn't resolve, or that need the operator's judgment call.

## Archive
<!-- READ SCOPE: routine reads STOP here. Below is history — grep on demand only. -->

### Archived 2026-01-31 (done/dropped, moved from Open)
- [x] 2026-01-10 · @operator · Example completed item · done:2026-01-12 · src:[[acme-studios]] · [S]
