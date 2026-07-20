#!/usr/bin/env python3
"""generate_index.py — regenerate 00_index/index.md from vault state.

The index rots when hand-maintained (measured: 12 days stale, 9 entities
undercounted by 2026-07-19). So it is generated, like the context pack.
Run at every morning briefing, and after any entity add/remove:

    python3 90_system/generate_index.py

Fails closed: any structural surprise exits non-zero and leaves the old
index untouched. Hand edits to 00_index/index.md WILL be overwritten —
curation belongs in the entity pages themselves, not the map of them.
"""
import os, re, sys, datetime

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(VAULT, "00_index", "index.md")

# placeholder link targets used illustratively in specs/templates — never "broken"
PLACEHOLDER = re.compile(r"^(YYYY|<|.*-slug$|kebab-slug$|linked-entity)", re.I)

def md_files(*parts):
    d = os.path.join(VAULT, *parts)
    if not os.path.isdir(d):
        sys.exit(f"FAIL-CLOSED: missing directory {d}")
    return sorted(f[:-3] for f in os.listdir(d) if f.endswith(".md"))

def read(p):
    with open(p, encoding="utf-8", errors="ignore") as f:
        return f.read()

def section_counts(ledger_text):
    """Count checkbox lines per ## section of the ledger."""
    counts, current = {}, None
    for ln in ledger_text.split("\n"):
        if ln.startswith("## "):
            current = ln[3:].strip()
            counts.setdefault(current, {"open": 0, "done": 0})
        elif current:
            if ln.startswith("- [ ]"): counts[current]["open"] += 1
            elif ln.startswith("- [x]"): counts[current]["done"] += 1
    return counts

def main():
    people    = md_files("20_derived", "people")
    companies = md_files("20_derived", "companies")
    projects  = md_files("20_derived", "projects")
    health    = md_files("20_derived", "health") if os.path.isdir(
                    os.path.join(VAULT, "20_derived", "health")) else []

    ledger_path = os.path.join(VAULT, "30_ledger", "ledger.md")
    ledger = read(ledger_path)
    lc = section_counts(ledger)
    if "Open" not in lc:
        sys.exit("FAIL-CLOSED: ledger has no ## Open section")

    # sweep all md for [gap], CONFLICT, and wikilink health
    gaps, conflicts, links, files_scanned = {}, {}, set(), 0
    all_md_names = set()
    for root, dirs, fs in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in (".git", ".obsidian")]
        for f in fs:
            if not f.endswith(".md"): continue
            p = os.path.join(root, f)
            rel = os.path.relpath(p, VAULT)
            all_md_names.add(f[:-3])
            t = read(p); files_scanned += 1
            n_gap = len(re.findall(r"\[gap\]", t))
            if n_gap: gaps[rel] = n_gap
            n_c = len(re.findall(r"\bCONFLICT\b", t))
            if n_c and "20_derived" in rel: conflicts[rel] = n_c
            for m in re.findall(r"\[\[([^\]|#]+)", t):
                links.add(m.strip())
    broken = sorted(t for t in links
                    if t and t not in all_md_names and not PLACEHOLDER.match(t))

    today = datetime.date.today().isoformat()
    def bullets(names): return ", ".join(names) if names else "(none)"

    out = f"""---
generated: {today}
generator: 90_system/generate_index.py — DO NOT HAND-EDIT (edits are overwritten)
---
# IntelVault — Index

Master map: what exists, where, how fresh. Regenerated at every morning
briefing; if `generated:` above is older than the last briefing, run the
generator — a stale index caused a retracted finding once already.

## Entities

### People (`20_derived/people/`) — {len(people)}
{bullets(people)}

### Companies (`20_derived/companies/`) — {len(companies)}
{bullets(companies)}

### Projects (`20_derived/projects/`) — {len(projects)}
{bullets(projects)}
""" + (f"""
### Health (`20_derived/health/`) — {len(health)}
{bullets(health)}
""" if health else "") + f"""
## Ledger
- [ledger.md](../30_ledger/ledger.md) — **{lc['Open']['open']} open** · {lc['Open']['done']} done-unmigrated in Open · {sum(v['done'] for k,v in lc.items() if k.startswith('Archive'))} archived · Needs review: {lc.get('Needs review', {}).get('open', 0)} open
- Migration health: {"✅ Open section is clean" if lc['Open']['done']==0 else f"⚠️ {lc['Open']['done']} done lines await monthly migration to ## Archive"}

## Health metrics (auto-counted)
- **`[gap]` tags:** {sum(gaps.values())} across {len(gaps)} files — top: {", ".join(f"{os.path.basename(k)} ×{v}" for k,v in sorted(gaps.items(), key=lambda x:-x[1])[:5])}
- **CONFLICT markers in derived pages:** {sum(conflicts.values())} across {len(conflicts)} files{" — " + ", ".join(os.path.basename(k) for k in conflicts) if conflicts else ""}
- **Broken wikilinks (non-placeholder):** {len(broken)}{" — " + ", ".join(f"[[{b}]]" for b in broken[:8]) if broken else ""}
- Files scanned: {files_scanned} md

## Views
- `40_views/daily/` — daily briefings · `40_views/weekly/` — weekly reviews
- Instruments and trackers live flat in `40_views/` (opportunity-tracker, health-tracker, notes-effectiveness-log, …)

## System
- [chief_of_staff_instructions.md](../90_system/chief_of_staff_instructions.md) — the law
- [ingest_log.md](../90_system/ingest_log.md) — what was consumed, when
- [generate_context_pack.py](../90_system/generate_context_pack.py) · [generate_index.py](../90_system/generate_index.py) — the two generators
"""
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"index regenerated: {len(people)}p/{len(companies)}c/{len(projects)}proj · "
          f"{lc['Open']['open']} open · {sum(gaps.values())} gaps · {len(broken)} broken links")

if __name__ == "__main__":
    main()
