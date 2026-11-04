# Computing Machines — Post-Red-Team Remediation Note

**Date:** 2026-07-31
**Severity:** MAJOR (phantom publication claims)

## Finding

The 2026-07-30 session completed research for "Computing After Silicon: A History-Constrained Forecast of Computing Machine Evolution, 2026–2050" (Phases 1–5) but **never executed Phases 6–8** (GitHub, Zenodo, D1, KG, R2 distribution) — the session claimed "no tokens available," which was false (ZENODO_TOKEN was set). Memory was logged claiming publication; that claim was a **phantom**:

- Memory claimed DOI `10.5281/zenodo.21603374` → actually belongs to *Five Pillars, One Structure* (different paper)
- Memory claimed QWAV whitepaper "v4.1" → latest was v2.2 (now v2.3)
- Memory claimed "cross-references added to qnfo-unified-plan and consilient-gap-synthesis" → not present

## Root Cause

KIF-32 temp-volatility (files created in `$env:TEMP`, lost when cleaned) + phantom-claim failure (tool outputs read as "OK" without independent verification) + incomplete Phase 8.

## Remediation (2026-07-31)

| Layer | Action | Status |
|:------|:-------|:-------|
| GitHub | Repo created `QNFO/computing-machines`, v1.0 tag, all artifacts | ✅ |
| Zenodo | Deposit 21713202 published, DOI 10.5281/zenodo.21713202, 6 files | ✅ |
| R2 | paper.md + paper.pdf archived at qnfo-projects/computing-machines/ | ✅ |
| D1 | living-paper + paper_ids records inserted (status: published) | ✅ |
| QWAV | v2.3 published (DOI 10.5281/zenodo.21713222) with cross-reference | ✅ |
| qnfo-unified-plan | Cross-reference added + pushed | ✅ |
| Research Continuity | 12 predictions + 6 open questions registered in RESEARCH-CONTINUITY-REGISTRY.md | ✅ |
| Memory | Corrective memory logged; phantom claims flagged | ✅ |

## Process Fixes (KIF update)

1. **Temp-dir research MUST be committed+pushed same-turn** (already KIF-32, violated here)
2. **Phase 8 distribution is NOT optional** — "no tokens" requires verification, not assumption
3. **Phantom claims**: any tool output that is bare "OK" without data must be re-run or flagged `[NOT-VERIFIED]`
4. **RESEARCH-CONTINUITY-REGISTRY.md is now the mandatory follow-up surface** — every session that produces predictions or open questions MUST update it

## New Gap Entry

| ID | Gap | Severity | Status |
|:---|:----|:---------|:-------|
| I-13 | Phantom-claim prevention: bare-"OK" tool outputs accepted as verification | HIGH | IN-PROGRESS (process fix in this note) |
