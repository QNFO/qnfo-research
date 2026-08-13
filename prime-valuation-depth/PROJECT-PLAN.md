# WBS: QNFO.RES.004

# Prime Valuation Depth — Project Plan

**Project:** Prime Valuation Depth — valuation as depth: the bridge between the calculus of indications and number theory, with quantum-mechanical consequences
**WBS:** QNFO.RES.004
**Program:** QNFO.RES (QNFO Research Archive)
**Repo:** QNFO/qnfo-research
**Branch:** res/paper/prime-valuation-depth
**Slug:** prime-valuation-depth
**Created:** 2026-08-13
**Status:** Phase 0 (scaffold)

---

## §1 Charter

Multiplication is standardly defined by recursive addition, but recursion hides a structural fact: multiplication generates a new dimension of distinctions. This project develops that structural fact into a research program: (1) the p-adic valuation as a measure of depth along a prime branch (not size), grounded in Ostrowski's theorem; (2) the bridge between the calculus of indications (branching distinctions) and number theory (the tree of prime divisors); and (3) the transfer of the valuation-as-depth reading to quantum mechanics, where the tensor product's multiplicative branching yields a structural reading of the no-cloning theorem and adjacent no-go theorems.

## §2 Core Claim (LOCKED — P6)

**Primary claim [TERRITORY — established, Ostrowski 1916]:**
Every positive integer is a finite product of prime powers; each prime is a distinct branch type and the exponent counts the depth of nesting along that branch. The p-adic valuation v_p(n) is therefore a measure of depth along a prime branch, not a measure of size.

**Bridge claim [MAP — interpretive reading to be defended]:**
The valuation-as-depth reading is the bridge between the calculus of indications (branching distinctions) and number theory (the tree of prime divisors). [Falsifiability condition: disconfirmed if no nontrivial structure-preserving correspondence exists between nested distinctions and p-adic valuations — i.e., if the correspondence reduces to relabeling with no shared structural laws.]

**Extension claim [MAP — speculative, to be developed]:**
The same reading transfers to quantum mechanics. The tensor product is not a Cartesian product; it multiplies dimensions, generating paired distinctions. Prime factorization of Hilbert-space dimension identifies branch type and depth (dim H = 2^n for n qubits, so v_2(dim H) = n). The no-cloning theorem is then structural: cloning would require the diagonal map |psi> -> |psi> (x) |psi>, which is nonlinear (quadratic in the amplitudes), and quantum evolution preserves only linear (additive) structure. [Falsifiability condition: the extension is interpretive; it is disconfirmed if it yields no explanatory or predictive content beyond the standard formalism — i.e., if it is pure relabeling.]

## §3 Research Questions

| ID | Question |
|:---|:---------|
| RQ1 | What is the precise formal correspondence between Spencer-Brown's distinction/branching and the prime-factor tree of the integers? |
| RQ2 | In what sense does Ostrowski's theorem (all nontrivial absolute values on Q are Archimedean or p-adic) make the prime-depth valuations exhaustive? |
| RQ3 | Does the valuation-as-depth reading of the tensor product yield a resource-theoretic statement (v_p(dim H) as tensor-branch depth) that is formally defensible? |
| RQ4 | Does the structural reading of no-cloning (no linear diagonal map; monoidal-but-not-Cartesian category) add explanatory content to standard proofs? |
| RQ5 | Do adjacent no-go theorems (no-broadcasting, monogamy of entanglement) admit the same branch-depth reading, and does that reading survive adversarial review? |
| RQ6 | What would an adelic (Archimedean + p-adic) formulation of state space contribute, and what does it predict that is falsifiable? |

## §4 Phases (QNFO Standard Pipeline)

| Phase | Name | Deliverables |
|:------|:-----|:-------------|
| P0 | Project Init | This scaffold, WBS, core claim lock, D1 + KG registration (current) |
| P1 | Due Diligence | KG + D1 + Vectorize cross-reference, gap analysis, consilience gate (KIF-29) |
| P2 | Literature Search | 8-source parallel search (LoF, p-adic analysis, p-adic QM, categorical QM), classification |
| P3 | Citation Management | Verified BibTeX (P3.AUTHOR-GATE), citation audit |
| P4 | Deep Research | Formal correspondence LoF x prime-tree, no-cloning structural proof, red-team challenge, calibration register |
| P5 | Publication | prime-valuation-depth.md + PDF (CDP pipeline) + Zenodo DOI + BP-1..BP-10 gates |
| P6 | Deployment | D1 living-paper row, papers-server, KG node + Vectorize index |
| P7 | Dissemination | SEO, social, Internet Archive |
| P8 | Core Distribution | R2 archive, GitHub tag, 4-layer verification |

## §5 Deliverable Registry

| ID | Deliverable | Type | Path | Target |
|:---|:------------|:-----|:-----|:-------|
| DL-00 | PROJECT-PLAN.md | Document | PROJECT-PLAN.md | GitHub (this commit) |
| DL-01 | README.md | Document | README.md | GitHub |
| DL-02 | Core claim lock | Document | docs/core-claim.md | GitHub |
| DL-03 | Due-diligence report | Analysis | artifacts/due-diligence.md | GitHub |
| DL-04 | Consilience gate audit | Analysis | artifacts/consilience-gate.md | GitHub |
| DL-05 | Literature classification | Analysis | artifacts/literature-classification.md | GitHub |
| DL-06 | Citation audit | Analysis | artifacts/citation-audit.md | GitHub |
| DL-07 | Deep-research draft | Paper | prime-valuation-depth.md | Zenodo + R2 + D1 |
| DL-08 | PDF | Paper | prime-valuation-depth.pdf | Zenodo |
| DL-09 | Calibration register | Analysis | artifacts/calibration-register.md | GitHub |

## §6 Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|:---|:-----|:-----------|:-------|:-----------|
| R1 | The LoF x prime-tree correspondence is judged trivial (relabeling) | Medium | High | Require shared structural laws (not mere naming); KIF-60 Bayesian evidential weight gate; minimum-viable-finding gate |
| R2 | The QM extension is judged to add no content beyond standard no-cloning proofs | Medium | High | RQ4 demands explicit delta vs standard proofs; cap at [RETRODICTION — not evidence] if no delta found; publish the number-theoretic bridge independently |
| R3 | p-adic QM literature engagement is thin (niche field) | Medium | Medium | 8-source search incl. arXiv quant-ph + math-ph; cite Khrennikov / Vladimirov-Volovich line |
| R4 | Anthropomorphic overreach (valuation-as-depth presented as ontology rather than map) | Medium | Medium | MAP-TERRITORY labels on every identity claim; falsifiability condition per claim |
| R5 | Scope creep into full adelic QM program | Medium | Medium | RQ6 is a frontier question only; P5 publishes the bridge + structural no-cloning reading |

## §7 Success Criteria

1. P5 published on Zenodo with DOI; PDF built via the canonical CDP pipeline; all BP-gates pass.
2. The LoF x prime-tree correspondence survives a 5-adversary red-team challenge with at least one non-trivial shared structural law identified.
3. The structural no-cloning reading states a falsifiable delta vs the standard linearity proof (or is explicitly capped as retrodiction).
4. Calibration register seeded with dated, strength-graded predictions.

## §8 Prior Art and Intellectual Lineage

| Prior Work | Identifier | Relevance |
|:-----------|:-----------|:----------|
| Ostrowski's theorem (1916) | Ostrowski, Acta Math. 41 | Exhaustiveness of Archimedean + p-adic absolute values |
| Laws of Form (1969) | Spencer-Brown | Calculus of indications; distinction as primitive |
| p-adic QM | Vladimirov-Volovich; Khrennikov | p-adic Hilbert spaces; non-Archimedean quantum formalisms |
| ODR-BT synthesis (QNFO internal) | — | Compton count -> prime factorization -> p-adic valuation -> BT-tree depth chain |
| Five Pillars / WBS.6 synthesis | 10.5281/zenodo.21547793 | Cross-pillar consilience methodology |

## §9 Version History

| Version | Date | Author | Changes |
|:--------|:-----|:-------|:--------|
| v0.1-phase0 | 2026-08-13 | QNFO Research Collective | Phase 0 scaffold: charter, WBS, core claim lock, deliverable registry, risk register |
