```
THREAD:  SYS-TOPIC-SLUG   (stable for the life of the topic; new topic = new ID)
MSG:     01               (sequential within the thread)
FROM:    Chief-of-staff AI  →  TO: Builder AI
DATE:    2026-01-15
RE:      —                (which MSG this answers; — for a new thread)
STATUS:  One line: what is settled, what is open.
ACTION:  What you're asking the other side to do, or "none, informational".
```

## Rules (from the vault law)

- One topic per file; self-contained (readable without the source conversation).
- Filename: `YYYY-MM-DD_<from>-to-<to>_<THREAD>-msg<NN>.md` in `50_program/handoffs/`.
- **The operator carries every message.** No AI acts on another AI's handoff the
  operator hasn't seen.
- If the recipient can't read your filesystem, **inline the values** — a reply
  that cites paths the other side can't open is useless.
- Claims you make are tagged like everything else; claims the other system makes
  get recorded as theirs (e.g. builder-authoritative) and verified against
  source when access allows.
- Temporary and non-canonical: a handoff becomes real only when its outcome is
  recorded in a canonical home (a decision log, the ledger, an entity page).
  The consumer archives the file after recording the outcome.

## Body

State the context in two lines, then numbered requests or findings. If it's a
forensic request: read-only, evidence-first, ask for a verdict with a
confidence level, and say explicitly "make no repairs."
