# CMD RED TEAM SUB — Post-Publication Adversarial Analysis Report

**Project:** QNFO.RES.006 | **Slug:** prime-valuation-qec-implications
**Date:** 2026-08-13 (2nd cycle of the publish-then-audit loop)
**Audited artifacts:** Zenodo 10.5281/zenodo.21922813 (v0.1, prior), 10.5281/zenodo.21923000 (v0.2, current) + GitHub branch deliverables
**Protocol:** CMD RED TEAM SUB — 3 reviewer subagents dispatched (Accuracy / Completeness / Dependency) plus findings from two completed prior-cycle reviewers; direct parent-agent audit executed as fallback; **all completed reviewer findings incorporated** (READ-ONLY vs published records).

## 1. Findings incorporated from dispatched reviewers

**HARD (3) — all in BRANCH deliverables, all FIXED this cycle (commit below):**

**H1 — due-diligence-phase1.md §1 stale 83% DOI (reviewer 8bvnvYY6lp7g2aKl0FHR5).**
§1 attributed the QNFO.UF 83%-accuracy result to 10.5281/zenodo.21046993. Live: 21046993 = "Ultrametric
Quantum Computing: Tree-Topology Error Correction" — NOT the 83% classifier paper. Canonical source =
10.5281/zenodo.21193487 ("Number-Theoretic Ultrametric Foundations"), which PROJECT-PLAN/core-claim cite
correctly. Root cause: the D1 program_registry QNFO.UF row still carries the stale DOI. FIXED in the
artifact; D1 registry row updated (see Dependency).

**H2 — due-diligence.md §2 "Ultrametric Code Spaces" DOI (reviewer 8bvnvYY6lp7g2aKl0FHR5).**
Listed 10.5281/zenodo.21819232, which is "Archimedean Shadows: The QEC-Darwinism Tradeoff". Correct DOI =
21824195 ("Ultrametric Code Spaces: The Bruhat-Tits Tree..."). Each due-diligence artifact carried exactly
one wrong DOI, in opposite directions. FIXED in the artifact.

**H3 — rq3-reproduction-report.md F2 magnitude argument mathematically invalid (reviewer D8nsljceeOgHQ7XhJGz3N).**
The claim "v_p^max = 28 impossible at n <= 18 because |c_j| is bounded by 2^(n-k)" is NOT generally valid:
the binomial-weighted finite-difference transform can exceed any single A_i (max |c_j| <= 2^(n-k) * max_i C(j,i)).
F2 rewritten as an EMPIRICAL claim (max observed v_p^max = 6 across 55 codes, nowhere near 28). The empirical
negative result STANDS; the theoretical leg was over-claimed and is corrected.

## 2. Direct parent-agent audit (fallback, live-verified)

**Accuracy:** record 21922813 (v0.1, 14 files, isSupplementTo+isDerivedFrom) PASS; newversion 21923000
published mid-audit (v0.2, 41 files, full provenance incl. rq3-* and this cycle's audit) PASS;
rq3-results.json 55/55 valid, family values PASS; DOI spot-checks PASS (Gubser-Knaute 403 = HEAD-method
artifact; CrossRef + GET resolve ATMP 21:1655-1678).
**Completeness:** branch artifacts 7/7 present; C1-C8 register complete; negative result disclosed;
83% labeled UNVERIFIED-INTERNAL. PASS.
**Dependency:** 46 bib keys map to 14 manuscript references; citation-audit 21193487 canonical;
KG node + BELONGS_TO/CITES edges; D1 row + kg_node_id; branch exists. PASS.

## 3. Remediation executed this cycle (branch only; published records untouched)

1. due-diligence-phase1.md §1 83% DOI -> 21193487.
2. due-diligence.md §2 Ultrametric Code Spaces -> 21824195.
3. rq3-reproduction-report.md F2 rewritten empirical; §3 headline qualified; R5 robustness added.
4. D1 program_registry QNFO.UF zenodo_doi -> 10.5281/zenodo.21193487 (root-cause metadata fix).
5. This report revised to include reviewer findings.

## 4. Residual items (next cycle)

- Branch now diverges from published records 21922813/21923000 on the three fixed artifacts; a future
  newversion (or post-publication note) should carry the corrections (per publish-then-audit loop).
- Reviewer D8nsljceeOgHQ7XhJGz3N also noted: min_stab_weight is only a crude distance proxy; the notebook
  never computes true code distance d — comparability with NTOF Lemma 10 (d >= 3) remains unverified.
- Three current-cycle reviewers (Accuracy/Completeness/Dependency) were still running at aggregation time;
  their output, if any, will be folded into the next cycle.

## 5. Verdict

**FAIL-GATES on branch deliverables (3 HARD) — all FIXED and re-verified this cycle.** Published records
21922813/21923000 remain read-only; the fixes feed the next newversion. The RQ3 empirical negative result
stands; its theoretical magnitude argument is corrected to empirical scope.
