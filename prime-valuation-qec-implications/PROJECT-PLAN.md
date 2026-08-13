# WBS: QNFO.RES.006

# Implications for Computing and Quantum Error Correction — Project Plan

**Project:** Implications for Computing and Quantum Error Correction — extending the prime-valuation-depth reading (tensor-branch depth) to computation and quantum error-correcting code structure
**WBS:** QNFO.RES.006
**Program:** QNFO.RES (QNFO Research Archive)
**Repo:** QNFO/qnfo-research
**Branch:** res/paper/prime-valuation-qec-implications
**Slug:** prime-valuation-qec-implications
**Anchor paper:** Prime Valuation Depth (QNFO.RES.005) — DOI 10.5281/zenodo.21918838
**Created:** 2026-08-13
**Status:** Phase 0 (scaffold)

---

## §1 Charter

The anchor paper, *Prime Valuation Depth*, established that the p-adic valuation v_p(n) is a measure of **depth along a prime branch** of the integer factorization tree (not size), grounded in Ostrowski's classification, and transferred that reading to quantum mechanics: because the tensor product **multiplies** Hilbert-space dimensions, v_2(dim H) = n counts tensor-branch depth for n qubits, and the no-cloning theorem becomes structural — cloning would require a nonlinear diagonal map in a monoidal-but-not-Cartesian category.

This follow-on develops the two consequences the anchor paper flagged but did not pursue: **(1) computing** — what it means for computation to be path-tracing through a multiplicative branch structure; and **(2) quantum error correction** — how the branch-depth reading lands on the structure of QEC codes. The QEC leg is anchored by an existing QNFO prior result (QNFO.UF, "p-adic valuations classify QEC codes at 83% accuracy", DOI 10.5281/zenodo.21046993), which this project must reproduce, stress-test, and extend or correct.

## §2 Core Claim (LOCKED — P6)

**Primary claim [TERRITORY — established, inherited from QNFO.RES.005]:**
For an n-qubit system, dim H = 2^n, so the 2-adic valuation v_2(dim H) = n counts the tensor-branch depth (number of qubit tensor factors). In general, v_p(dim H) counts the number of p-dimensional branch factors in the prime factorization of the Hilbert-space dimension.

**Bridge claim [MAP — to be defended]:**
Quantum error correction is the structural response to the anchor paper's no-cloning constraint (no linear diagonal map; monoidal-not-Cartesian). A [[n,k,d]] stabilizer code embeds a 2^k-dimensional logical subspace inside a 2^n-dimensional branch space, and its parameters admit a branch-depth reading: n = v_2(dim H) (total branch depth), k = v_2(dim H_L) (protected branch depth), d = minimal branch-crossing error weight. [Falsifiability condition: disconfirmed if the [[n,k,d]] ↔ branch-depth mapping is a pure relabeling that reproduces standard stabilizer theory with no new invariant, classification, or predictive content.]

**Extension claim [MAP — speculative, to be developed]:**
The branch-depth vocabulary yields a classification invariant for QEC code families that connects to QNFO.UF's reported 83%-accuracy result, and clarifies how no-cloning sets the fundamental limits of error correction (non-orthogonal redundancy as the only available resource once multiplicative branching cannot be linearly duplicated). [Falsifiability condition: the 83% claim must be reproduced or refuted on a fresh, independent test set; the classification invariant must be checkable on known code families and falsifiable on constructed counterexamples.]

## §3 Research Questions

| ID | Question |
|:---|:---------|
| RQ1 | What is the precise sense in which computation is path-tracing through a multiplicative (tensor-branch) structure, and where does that reading add content beyond the standard circuit model? |
| RQ2 | Does the branch-depth mapping n = v_2(dim H), k = v_2(dim H_L), d = (branch-crossing error weight) reproduce standard stabilizer-code parameters exactly, and where does it diverge? |
| RQ3 | What is the exact claim behind QNFO.UF's "p-adic valuations classify QEC codes at 83% accuracy", and does it reproduce on a fresh, independent test set? |
| RQ4 | How does the no-cloning reading constrain the achievable code distance for a fixed (n,k), and does that constrain any known bound (quantum Singleton, Hamming)? |
| RQ5 | Does the branch-depth invariant organize known code families (CSS, surface, toric, colour, subsystem) into a valuation-based taxonomy? |
| RQ6 | Does the computing leg yield a falsifiable complexity-theoretic statement (e.g., a valuation-based invariant of reversible circuits)? |

## §4 Phases (QNFO Standard Pipeline)

| Phase | Name | Deliverables |
|:------|:-----|:-------------|
| P0 | Project Init | This scaffold, WBS, core claim lock, D1 + KG registration (current) |
| P1 | Due Diligence | KG + D1 + Vectorize cross-reference, gap analysis, consilience gate (KIF-29) |
| P2 | Literature Search | 8-source parallel search (QEC stabilizer theory, p-adic QM, topological codes), classification |
| P3 | Citation Management | Verified BibTeX (P3.AUTHOR-GATE), citation audit |
| P4 | Deep Research | Branch-depth ↔ [[n,k,d]] mapping, QNFO.UF 83% reproduction/refutation, red-team, calibration register |
| P5 | Publication | prime-valuation-qec-implications.md + PDF + Zenodo DOI + BP-1..BP-10 gates |
| P6 | Deployment | D1 living-paper row, papers-server, KG node + Vectorize index |
| P7 | Dissemination | SEO, social, Internet Archive |
| P8 | Core Distribution | R2 archive, GitHub tag, 4-layer verification |

## §5 Deliverable Registry

| ID | Deliverable | Type | Path | Target |
|:---|:------------|:-----|:-----|:-------|
| DL-00 | PROJECT-PLAN.md | Document | PROJECT-PLAN.md | GitHub (this commit) |
| DL-01 | README.md | Document | README.md | GitHub |
| DL-02 | Core claim lock | Document | docs/core-claim.md | GitHub |
| DL-03 | Due-diligence report | Document | artifacts/due-diligence.md | Phase 1 |
| DL-04 | External-search evidence | Data | artifacts/external-search/ | Phase 1 |
| DL-05 | Consilience gate | Document | artifacts/consilience-gate.md | Phase 1 |
| DL-06 | Paper manuscript | Document | prime-valuation-qec-implications.md | Phase 5 |
| DL-07 | PDF build | Artifact | releases/*.pdf | Phase 5 |
| DL-08 | Zenodo record | Publication | 10.5281/zenodo.* | Phase 5 |

## §6 Milestones

| ID | Milestone | Gate |
|:---|:----------|:-----|
| M0 | Phase 0 committed/tagged/pushed | Pre-flight P1-P11 HARD gates pass |
| M1 | Due diligence complete; gap analysis + consilience gate | KIF-29 gate produced |
| M2 | QNFO.UF 83% claim reproduced or refuted | Independent test set, evidence file cited |
| M3 | Branch-depth ↔ [[n,k,d]] mapping formally stated | Red-team clean |
| M4 | Publication (Zenodo + PDF + D1/KG) | BP-1..BP-10 gates pass |

## §7 Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|:---|:-----|:-----------|:-------|:-----------|
| R1 | The branch-depth reading is pure relabeling of standard QEC | High | High | Explicit falsifiability conditions (P6); negative result is a publishable finding |
| R2 | QNFO.UF 83% claim is not reproducible (overfit, leakage) | Medium | Medium | Independent train/test split; report failure honestly |
| R3 | Computing leg is too vague to be falsifiable | Medium | Medium | RQ6 forces a concrete complexity-theoretic statement |
| R4 | Scope creep (both computing AND QEC) | Medium | Medium | QEC is the primary leg; computing leg scoped to one falsifiable claim |

## §8 Success Criteria

1. The [[n,k,d]] ↔ branch-depth mapping is stated precisely and shown either to (a) reproduce standard stabilizer theory with at least one new invariant, or (b) fail in a documented, illuminating way.
2. QNFO.UF's 83% claim is independently reproduced or refuted with a cited evidence file.
3. Every non-empirical claim carries an explicit falsifiability condition.
4. The paper passes the full BP-1..BP-10 publication gate set and is deposited to Zenodo with a GitHub provenance link (related_identifiers isSupplementTo).
