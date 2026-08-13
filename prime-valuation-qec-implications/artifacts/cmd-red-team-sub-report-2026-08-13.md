# CMD RED TEAM SUB — Post-Publication Adversarial Analysis Report

**Project:** QNFO.RES.006 | **Slug:** prime-valuation-qec-implications
**Date:** 2026-08-13 (2nd cycle of the publish-then-audit loop)
**Audited artifacts:** Zenodo 10.5281/zenodo.21922813 (v0.1, prior) and 10.5281/zenodo.21923000 (v0.2, current, published mid-audit) + GitHub branch `res/paper/prime-valuation-qec-implications`
**Protocol:** CMD RED TEAM SUB — 3 reviewer subagents dispatched (Accuracy / Completeness / Dependency), queued but no output after bounded wait; per fallback, **direct parent-agent audit** executed with live tool verification covering all three dimensions. READ-ONLY vs published records.

## 1. Accuracy (live-verified)

| Check | Result |
|:------|:-------|
| Record 21922813: title/version v0.1/date 2026-08-13/DOI/license cc-by-4.0 | PASS |
| 21922813 file count 14 + related_identifiers (isSupplementTo GitHub branch, isDerivedFrom 21918838) | PASS |
| Deposited manuscript lags branch: 21922813 carries pre-YAML v0.1 (16,107 chars); branch head v0.2 (20,409 chars) | CONFIRMED — but see REMEDIATION below (21923000 carries v0.2) |
| rq3-results.json: 55 codes, 55 valid, 0 invalid; CSS [1,1], Surface [1,3], Optimal [4], Random median 3 max 6 | PASS |
| L2 claim 35/50 random codes min_stab_weight <= 2 (dist 18@1, 17@2, 9@3, 6@4) | PASS (35 of 50) |
| Reference DOIs: 10.1038/299802a0, 10.1007/jhep01(2018)139, 10.4310/atmp.2017.v21.n7.a3 | PASS (after method fix, see S1) |
| 83% source 21193487 + distinct paper 21046993 | PASS (titles verified) |
| Newversion 21923000: status published, version v0.2, 41 files, YAML-frontmatter manuscript (20,628 chars), isSupplementTo + isDerivedFrom | PASS — published mid-audit |

## 2. Completeness

| Check | Result |
|:------|:-------|
| Record 21922813 provenance set: 13/14 required files present; missing citation-audit.md | SOFT (S2 below) |
| Newversion 21923000 provenance set: 41 files incl. citation-audit.md, RESEARCH-CONTINUITY-REGISTRY, red-team-P4, calibration-register, rq3-* (report+json+notebook), post-publication-audit-21922813.md, external-search evidence, HTML+PDF | PASS — full PUBLICATION-SOURCE-COMPLETENESS-1 set |
| Branch artifacts 7/7: citation-audit, red-team-P4, calibration-register, rq3-report, rq3-results, post-publication-audit, notebook | PASS |
| Manuscript C1–C8 falsifiability register complete | PASS |
| Negative reproduction (C7.3' NOT reproduced at n<=18) disclosed in manuscript | PASS |
| 83% labeled UNVERIFIED-INTERNAL | PASS |

## 3. Dependency

| Check | Result |
|:------|:-------|
| references.bib: 46 keys; all 14 manuscript References items map (author-year heuristic) | PASS |
| citation-audit: 21193487 canonical 83% source | PASS |
| KG node paper:prime-valuation-qec-implications + edges BELONGS_TO prog-res, CITES paper:prime-valuation-depth | PASS |
| D1 living-paper row (doi 21922813, kg_node_id backfilled) | PASS |
| GitHub branch exists (HTTP 200) | PASS |
| Newversion 21923000 published (remediates H3/S1/S2 of the prior audit) | PASS |

## 4. Findings

**HARD: 0.** The single candidate (Gubser-Knaute DOI 403) was an audit-method artifact — doi.org HEAD rejected by the publisher (International Press); CrossRef + doi.org GET both resolve (ATMP 21:1655-1678, "A $p$-adic version of AdS/CFT"). Per BLAME-EXTERNAL-1 / API-FAILURE PROTOCOL: bug was my method, not the reference.

**SOFT: 3**
- S1 (audit process): doi.org HEAD is unreliable for this publisher; use GET with browser UA. Recorded for future audits.
- S2 (completeness): record 21922813 (v0.1) lacks citation-audit.md; moot now — 21923000 (v0.2) contains it.
- S3 (consistency, minor): references.bib GubserKnaute2017 page range 1655-1683 vs CrossRef 1655-1678; branch citation-audit.md (concurrent version) omits the explicit 21046993 attribution-artifact sentence (info survives in red-team-phase1.md + post-publication-audit-21922813.md). Non-blocking; fix at next cycle.

**DESIGN: 2**
- D1 (positive): the publish-then-audit loop CLOSED this cycle — publish 21922813 → audit (3 HARD) → remediate 21923000 (v0.2, full provenance incl. reproduction artifacts + audit) → re-audit (this pass: clean, 0 HARD). This is the canonical execution of the post-publication adversarial analysis gate.
- D2: reviewer subagents continue to stall in this environment (6th consecutive session-wide pattern); the direct parent-agent audit remains the reliable enforcement path. Logged for kaizen.

## 5. Verdict

**PASS (0 HARD).** Both records verified live; the current canonical record 21923000 (v0.2) carries the full provenance set and the corrected manuscript. The reproduction artifacts and this audit are deposited. Remaining items are SOFT/process-only and non-blocking.
