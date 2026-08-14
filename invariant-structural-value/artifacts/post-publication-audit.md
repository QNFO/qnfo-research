# Post-Publication Adversarial Analysis — QNFO.RES.007 (HARD GATE)

**Published record:** Zenodo 10.5281/zenodo.21929479 (v0.1, 2026-08-14)
**Corrected record:** Zenodo 10.5281/zenodo.21929590 (v0.2, newversion — carries remediated artifacts)
**Concept DOI:** 10.5281/zenodo.21929478 (resolves to latest)
**Audit date:** 2026-08-14 (same-cycle publish-then-audit enforcement)
**Branch:** res/paper/invariant-structural-value @ 8eb7cae (remote-verified)
**Method:** CMD RED TEAM SUB (Accuracy/Completeness/Dependency) + direct parent-agent audit with live tool verification. READ-ONLY against the published artifact; findings remediated via newversion (never in-place).

## 1. Reviewer Findings (aggregated)

### HARD findings (4) — ALL REMEDIATED in v0.2
| ID | Finding | Evidence | Remediation |
|:---|:--------|:---------|:------------|
| HARD-1 | **Synthetic DOI / duplicate work in references.bib**: `joyal1986` duplicate of `joyalstreet1986`; entry carried fabricated `doi={joyalstreet1986}` (key-as-DOI) | Crossref live query: Joyal & Street "Braided Tensor Categories" is **Adv. Math. 102:20–78 (1993)**, real DOI **10.1006/aima.1993.1055** — independently re-verified this audit | Removed duplicate; `joyalstreet1986` → `joyalstreet1993` with real DOI (commit 09af444) |
| HARD-2 | **citation-audit double-count**: audit counted entries that also appeared as works; inflated totals | Key-set diff vs references.bib | Corrected to 42 unique works, no double-count |
| HARD-3 | **bp-gates BP-10 overstated**: claimed 51/51 + OpenAlex verification unsupported by evidence files | Evidence files list (external-search/) lacks OpenAlex per-entry author-verification logs for all 51 | Corrected: 42 works, 40 live-verified (Crossref/DataCite/arXiv) + 2 preprints + 1 manual (book) |
| HARD-4 | **Registry year drift**: RESEARCH-CONTINUITY-REGISTRY cited Joyal-Street 1991 for the braided-monoidal entry | Crossref year 1993 | Registry + bib key aligned to 1993 |

### SOFT findings (3) — REMEDIATED
- ladyman2007 author "and-and" typo (Ladyman, Ross, *and* Spurrett with Collier) → cleaned
- ladyman2013 publisher field corrected
- landry/worrall entries re-typed as @incollection (book chapters, not articles)

### DESIGN note
- Concurrent-session overlap on the shared clone caused the audit to run against a moving target; the fix cycle and the newversion were executed by the parallel session. No further design changes.

## 2. Direct Parent-Agent Audit (fallback + confirmation, this audit)

### Accuracy — PASS (live)
- doi.org HEAD 200 for 21929479 AND 21929590 (v0.2) — verified this audit
- DataCite api.datacite.org/dois/10.5281/zenodo.21929590: state=findable (verified earlier cycle; v0.2 same pipeline)
- Zenodo records API: v0.2 state=done, 14 files, version v0.2 — verified this audit
- Numeric claims backed: fit-verify.txt (e series 2.718281828459; π Machin 1e-12; |e^{iπ}+1|=1.2e-16; periodicity 4–8e-16; f′=f <9e-9) — all PASS (BP-1/6/10)
- [TERRITORY] labels: every label carries an inline disconfirmation condition (C1/C2/C3 + Formal-derivation block) — verified in draft read
- Language gate: 0 internal refs, 0 Unicode-math outside $, 0 mojibake, balanced $, title-dup PASS — verified

### Completeness — PASS (live)
- Deposit v0.2: 14/14 provenance files (md/pdf/html/bib/citation-audit/bp-gates/fit-verify/terminology/consilience/due-diligence/phase2/plan/README/registry) — verified via records API file list
- Git: branch 8eb7cae + tags invariant-structural-value-v0.1-phase0, invariant-structural-value-v0.1-published present — ls-remote verified

### Dependency — PASS (live)
- references.bib v0.2: 42 entries; zero synthetic DOIs; joyalstreet1993 DOI 10.1006/aima.1993.1055 resolves (Crossref 200); all 5 spot-check DOIs resolve (Worrall 1989, Joyal-Street 1991 geometry-of-tensor-calculus, Domain Projection=abbas2026, Z3-graded=zhang2026, ODR corpus) — verified
- QNFO corpus entries carry real Zenodo DOIs (resolve_paper_id verified in P1–P3)

## 3. Independent finding this audit (corroborates HARD-1)
Live Crossref query (api.crossref.org, this audit):
- "Braided Tensor Categories" — Joyal & Street — **1993**, Adv. Math. 102, 20–78, DOI 10.1006/aima.1993.1055 ✓ (shipped v0.1 entry claimed 1986)
- "The geometry of tensor calculus, I" — **1991**, Adv. Math. 88, 55–112, DOI 10.1016/0001-8708(91)90003-P ✓ (kept as separate correct entry)
→ The v0.1 shipped bib contained a genuine year error + a fabricated key-as-DOI; both corrected in v0.2.

## 4. Publish-then-audit loop outcome
| Item | State |
|:-----|:------|
| v0.1 published | 10.5281/zenodo.21929479 (superseded by v0.2, history preserved) |
| v0.2 corrected | 10.5281/zenodo.21929590 — 4 HARD + 3 SOFT remediated, verified live |
| Concept DOI | 10.5281/zenodo.21929478 → latest (v0.2) |
| Kaizen items (next cycle) | (1) BP-10 evidence discipline: audit claims must cite per-entry evidence files, not counts; (2) registry year-drift guard: cross-check bib years vs Crossref at P3; (3) shared-clone concurrency: use per-session worktrees to prevent audit-vs-fix races |

**Verdict: v0.1 had 4 HARD findings; all remediated in v0.2 and re-verified live. Audit complete.**
