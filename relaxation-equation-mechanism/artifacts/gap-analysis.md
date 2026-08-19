# Gap Analysis + SO-WHAT — QNFO.RES.018 Phase 1

**Date:** 2026-08-19 · **Phase:** P1 due diligence (DUE-DILIGENCE-DEPTH-1)

---

## 1. Corpus coverage (QNFO cross-reference)

- **Corpus size (query_graph stats):** 8,307 nodes · 1,645 Paper nodes · 154 Projects (8303→8307 since RES.016 — concurrent growth).
- **Semantic sweep (built-in search_papers channel; qnfo-memory-mcp unavailable this session):** 4 formulations × limit 16 (VECTORIZE-TOP-K-50-1 compliant) + search_papers_enriched + recall_facts.
- **Top relevant hits:** `hydrodynamic-stability-hypothesis` (the framework under test), `pqs-critique-adjudication` (the adjudication that escalated FQ1 — now indexed), `stability` (Stability Compiler), `topological-quantization-and-spectral-filtration`, `syntactic-token-calculus` v3, `structural-vs-driven-quantum-coherence`.
- **Domains covered:** RES (primary), UMP (adjacent), SLB (adjacent via distinction calculus), INM (adjacent via information physics).
- **What the corpus does NOT contain:** any record analyzing whether Reddiger's Radon–Nikodym local-random-variable formalism is dynamical; no record on measurement as conditional-probability vs. relaxation dynamics; no GRW/CSL constraint comparison for the HSH program. **These are the project's genuine gap.**

## 2. Kill-question resolution (UIA Q8/Q15 — decisive evidence)

**Q:** Is Reddiger's 2017/2026 Radon–Nikodym local-random-variable formalism dynamical at all?

**A (full-text verified, evidence files in artifacts/external-search/):**
1. **TOA2026 (arXiv 2405.05710, full text fetched):** *"the dynamics is borrowed from quantum mechanics and the basic quantities are rigorously defined in the context of said dynamics"* — the formalism is **kinematical/probabilistic**: RN-based local random variables on a Kolmogorovian probability space, with the unitary evolution $t \mapsto U_t$ **explicitly imported from QM**. *"The projection postulate and the question of measurement are addressed via conditional probabilities in Part III"* — measurement is **NOT a dynamical relaxation** in Reddiger's framework; it is conditional probability.
2. **MADELUNG2017 (arXiv 2207.11367 = Reddiger & Poirier 2023, "Towards a mathematical Theory of the Madelung Equations: Takabayasi's Quantization Condition, Quantum Quasi-Irrotationality, variational Formulations, and the Wallstrom Phenomenon"):** the Madelung system IS dynamical (time-dependent PDEs for density $\rho$ and current velocity $\mathbf{v}$), but the paper's scope is well-posedness, the Wallstrom phenomenon, and the Takabayasi quantization condition — **not measurement dynamics**.
3. **Consequence for CC-1:** a measurement-triggered relaxation dynamics (basins of attraction) **cannot be read off Reddiger's formalism** — it is genuinely unconstructed. The kill-question answer is: *the RN formalism is not inherently dynamical in the measurement sense; the RN variables live inside an externally supplied unitary dynamics; measurement is conditional probability.* **CC-1 remains a genuine constructive task** — the project's necessity is confirmed, and its premise-depth is sharpened (see §4).

## 3. Cross-system ID validation + data-quality findings

| Hit | Resolution | Finding |
|:----|:-----------|:--------|
| `hydrodynamic-stability-hypothesis` | slug → D1 DOI **10.5281/zenodo.21993240** (was 21993494 during RES.016) | **DOI-DRIFT: version chain, same concept.** DataCite: 21993240 = v1.1.2, 21993494 = v1.1.3, both `IsVersionOf` concept 10.5281/zenodo.17721007; 21993494 additionally `IsObsoletedBy` → 21993240. D1 row re-pointed by a concurrent session to the current chain head. **Version-label anomaly:** the record labeled 1.1.2 (21993240) supersedes the record labeled 1.1.3 (21993494) per DataCite — labels are out of order with the obsoletion direction. Flag for corpus owner (P5.OWNERSHIP-class audit of that chain). **Not a blocker:** RES.016's citation of 21993494 remains valid (a member of the same concept chain); RES.018 cites the HSH concept + D1 body text, which is unaffected. |
| `pqs-critique-adjudication` | 10.5281/zenodo.22010489 (concept 22009652) | ✓ consistent; now Vectorize-indexed (sweep returns it) |

## 4. SO-WHAT — why should a reader care

The Hydrodynamic Stability Hypothesis (HSH) concedes its own central weakness: no mechanism explains how the probability fluid "clumps" into eigenstate configurations during measurement (HSH §1.6, verified in RES.016). The natural rescue — anchoring such a mechanism in Reddiger's rigorous Kolmogorovian re-grounding — **turns out to be unprovided by Reddiger himself**: his formalism borrows the unitary dynamics from quantum mechanics and treats measurement as conditional probability (Part III), not as relaxation. This project therefore attacks a **real, confirmed, and currently unconstructed gap** at the exact point where the framework is strongest (a rigorous probability-theoretic foundation) and weakest (no measurement dynamics). The reader should care because the outcome is binary and pre-registered: either a relaxation equation reproducing Born statistics within tolerance is constructed (framework gains its missing mechanism), or it is demonstrated that no such equation can be specified without smuggling in auxiliary stochasticity (the strongest objection stands with proof).

**Premise-depth disclosure:** This project's derived claims go as deep as (i) the primary texts of Reddiger (2017/2026, full texts archived), (ii) the HSH primary text as deposited in the corpus (concept 17721007; D1 body read), (iii) the RES.016 adjudication (DOI 10.5281/zenodo.22010489) that established the mechanism gap, and (iv) the collapse-model constraint literature (Bassi–Ghirardi 2003, verified). Named imported inputs: the Born rule as the empirical target (standard QM, not re-derived here); the 2-level system as the testbed. **Where the premises END:** at the pre-registered simulation's statistical tolerance (ε=1e-2 on 1e5 shots). The project does not claim the HSH framework is correct; it tests whether CC-1's constructive claim is achievable. A deviation beyond ε falsifies CC-1 regardless of the framework's other merits.

## 5. Practitioner relevance (PRACTITIONER-RELEVANCE-1)

**What can a practitioner DO with this result?** (1) A pre-registered, runnable falsification harness for any "relaxation-into-eigenstates" mechanism proposal — parameterized Python simulation with a fixed 2-level protocol, sha256-sealed before first run, PASS/FAIL verdict output. (2) A **negative-result template**: if CC-1 fails, the verdict record demonstrates *why* (parameterization degree-of-freedom violation, or deviation beyond tolerance) — directly reusable by grant reviewers and patent examiners evaluating hydrodynamic/relaxation-based quantum-foundations claims. (3) A **literature anchor for the gap**: the kill-question evidence (Reddiger's measurement = conditional probability, not relaxation) is a two-page dossier any practitioner can cite when evaluating claims that "the measurement problem is solved by hydrodynamic re-grounding." (4) The harness pattern transfers to any mechanism proposal — swap the dynamics family, keep the test protocol.

## 6. Novelty

- No corpus record addresses Reddiger's dynamical status or the measurement-as-conditional-probability point for the HSH program.
- External literature: Reddiger himself leaves the projection postulate to conditional probabilities (Part III); Bassi–Ghirardi's dynamical reduction models are stochastic — a **deterministic** relaxation reproducing Born statistics within tolerance is not established in the verified literature.
- **Genuine gap confirmed** → Phase 2 (literature triage) + Phase 4 (constructive task) proceed.

## 7. External verification summary (evidence files)

| Claim | Verification | Evidence |
|:------|:-------------|:---------|
| Reddiger 2017 = Madelung picture foundation (Found. Phys. 47:1317) | ✓ Crossref 10.1007/s10701-017-0112-5 | crossref-s10701-017-0112-5.json |
| Reddiger 2026 = ToA via probability theory (Phil Mag) | ✓ Crossref 10.1080/14786435.2026.2627725 | crossref-14786435.2026.2627725.json |
| RN formalism dynamical status | **RESOLVED: kinematical; dynamics borrowed from QM; measurement = conditional probability (Part III)** | reddiger-2405.05710-text.txt (full text) |
| Madelung equations well-posedness/Wallstrom | ✓ full text (Reddiger & Poirier 2023) | reddiger-2207.11367-text.txt |
| Bassi–Ghirardi 2003 dynamical reduction models, 257–426 | ✓ Crossref | crossref-bassighirardi2003-full.json |
| Wu et al. 2013 Bohmian HHG reproduction | ✓ Crossref | crossref-wu2013-full.json |
| HSH DOI chain (21993240/21993494 → concept 17721007) | ✓ DataCite + Zenodo (4 files) | datacite-zenodo.21993240.json, datacite-zenodo.21993494.json, zenodo-21993240.json, zenodo-21993494.json |
| Hardy 2001 five axioms | ✓ (RES.016 evidence: arxiv-hardy2001.json in corpus) | corpus evidence dir |

**Evidence discipline:** every count/DOI above has a saved evidence file in artifacts/external-search/ (13 files this phase + corpus provenance).
