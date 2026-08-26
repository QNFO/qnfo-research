# PROJECT-PLAN: Error Correction Is a Landauer Machine — The Thermodynamic Floor of Quantum Error-Correction Overhead

**WBS:** QNFO.JPC.003
**Author:** Rowan Brad Quni-Gudzinas (QNFO)
**Date:** 2026-08-26
**Status:** Phase 0 — Scaffold (core claim LOCKED)
**License:** CC BY 4.0 (publication); source in `QNFO/qnfo-research`, branch `res/paper/jpcub-qec-landauer`
**Parent Program:** QNFO.JPC — JPCub Validation (tier-1 core strategy)
**Extends:** QNFO.JPC.002 — JPCUB (joules-per-solution); this paper applies the metric to quantum error correction and to classical storage.

---

## §1. Charter

### §1.1 Problem Statement

Quantum error correction (QEC) is priced almost exclusively in combinatorial currency: code rate, distance, threshold, logical qubits per physical qubit. The physical bill — the energy cost of performing correction — is paid in a different currency that the field's headline metrics do not count. Every active QEC cycle is an **erasure engine**: syndrome extraction records error information that must then be reset; majority votes and ancilla re-initializations destroy the very redundancy they read. Landauer's principle prices each such erasure at no less than kT·ln2 per bit. More aggressive correction requires more redundancy, hence more erasures per logical operation. The consequence is a limit that is thermodynamic, not combinatorial: **QEC overhead does not converge to zero as codes improve; it converges to a positive thermodynamic floor.** Nature runs robust quantum processes — photosynthetic excitation transfer, radical-pair magnetoreception — with no correction scaffold at all, showing the floor is an architecture choice, not a law of physics. JPCUB — joules per correct answer — measures how far any code architecture stands from that floor, and it does so for classical storage too: the same nested-structure codes guard flash RAM, where the hypothesis is falsifiable today, without quantum hardware.

### §1.2 Core Claim (LOCKED)

> **Every active quantum error-correction cycle is an erasure process priced at no less than kT·ln2 per erased bit. Because correcting more errors requires more redundancy and therefore more erasures per logical operation, QEC overhead converges to a positive thermodynamic floor rather than to zero; JPCUB (joules per correct logical answer) measures how far a given code architecture stands from that floor; and structurally protected quantum systems (nature's witness) show the floor is a design choice, not a physical law.**

Formally: let E_cor(T, ε) be the total system energy consumed by error-corrected computation of task T at correctness ε, and E_floor(T, ε) = n_erase(T, ε) · kT·ln2, where n_erase(T, ε) is the minimum number of irreversibly erased bits per correct logical operation under any correction scheme achieving ε. The claim asserts:

1. E_cor(T, ε) ≥ E_floor(T, ε) > 0 for every active-correction architecture (Landauer bound applied to the erasure count of the correction cycle).
2. E_floor(T, ε) does not scale to zero as codes improve — redundancy grows with the corrected error budget, so the erasure count per logical operation is bounded below by a positive quantity.
3. JPCUB ranking of code architectures (repetition → Hamming → surface → qLDPC/tree) is by E_cor, not by rate alone; a code with better rate but worse erasure profile can lose.
4. Existence witness for the alternative: biological systems (photosynthetic energy transfer; radical-pair magnetoreception) run robust quantum behavior with structural protection and no active correction cycle.

**Falsifiability conditions:**
- (F1) A real QEC implementation whose measured energy-per-corrected-logical-error falls below the Landauer floor implied by its measured erasure count would disconfirm claim 1.
- (F2) If the redundancy required for correctness ε did NOT grow with the corrected error budget (i.e., overhead → 0 combinatorially at fixed physical error rate), claim 2 would be vacuous. The published record on code families (rate 1/n repetition vs. constant-rate qLDPC) is the evidence this is not so.
- (F3, classical, near-term) **Flash-memory test:** on a standard NAND bit-flip workload, tree-structured / nested-ball codes (ultrametric hierarchy) will match or beat LDPC baselines of equal rate on energy-per-corrected-bit including endurance amortization (P/E cycle wear). If LDPC wins on both endurance and energy at equal rate, the structural-protection hypothesis loses its near-term testbed.

**Scope:** This paper is a thermodynamic-cost analysis of QEC plus one pre-registered classical test. It does NOT claim a new code construction (unless Phase 3 produces one), does NOT assert a threshold-theory result, and does not rehearse the continuum/no-continuum ontology (UMP program territory).

### §1.3 Evidence Lineage

- CWI Summer School on QA & QEC, 24–25 Aug 2026 (Amsterdam): day notes in the Obsidian vault (2026-08-24.md, 2026-08-25.md); the QEC poster was withdrawn, but the JPCUB pricing thread survives and is the seed of this project.
- Landauer, R. (1961) "Irreversibility and Heat Generation in the Computing Process," IBM J. Res. Dev. 5, 183; Bennett, C. H. (1982) reversible computation — the kT·ln2 pricing of erasure and its reversibility caveat (reversible distinctions are free; correction resets are not).
- JPCUB metric: QNFO.JPC.002 (`joules-per-compute-benchmark`, PROJECT-PLAN §1.2 — advantage defined by total system energy per correct solution).
- QEC anatomy: Nielsen & Chuang ch. 10; surface-code threshold results; quantum LDPC/tree constructions (Tanner-graph counting bound: k ≥ n(1 − δb/δc)).
- Nature witness: Engel et al. (2007) 2D spectroscopy of photosynthetic complexes; Hore & Mouritsen (2016) radical-pair magnetoreception. (Microtubule/POSNER literature excluded — contested.)
- Anti-gaming discipline (JPCUB): all energy counted at system level — control electronics, reset pulses, ancilla preparation, cooling amortization, memory-controller overhead — never decode energy alone.

### §1.4 Hypothesis Cards (pre-registered)

- **H1 — Thermodynamic floor.** Prediction: measured E_cor per corrected logical error, across repetition/Hamming/surface/qLDPC families at fixed ε, decreases monotonically with better codes but remains ≥ the erasure-count floor. Falsifier: any scheme measuring below its floor. Surprisal: high if the floor is approached within ~10× already; low if everyone is orders of magnitude above it (status quo).
- **H2 — Flash-RAM structural protection.** Prediction: nested-ball/tree codes ≥ LDPC baselines (equal rate) on energy-per-corrected-bit incl. P/E endurance amortization. Falsifier: LDPC dominant on both axes. Surprisal: high — this is a cheap, classical, publishable-or-null test runnable this quarter.
- **H3 — Structure vs. erasure ratio.** Prediction: E_cor/E_useful is lower in structurally protected systems (photosynthetic complexes vs. man-made QEC devices at comparable robustness). Falsifier: a structurally protected system with a HIGHER ratio. Surprisal: medium; serves as the cross-domain bridge (biology ↔ engineering) and the terminology crosswalk anchor.

## §2. Premise Depth (where the premises end)

- **L0 (unanalyzable primitive):** energy and dissipation — thermodynamics as the background cost structure of any physical computation.
- **L1 (named imported inputs):** Landauer's principle (kT·ln2 per erased bit; imported from Bennett/Landauer literature); the JPCUB metric definition (imported from QNFO.JPC.002); standard QEC cycle anatomy (imported from Nielsen–Chuang and the QEC literature).
- **L2 (derived in this paper):** the erasure-count decomposition of a QEC cycle; redundancy-monotonicity → the positive-floor claim; the E_cor ≥ E_floor inequality per family.
- **L3 (empirical citations):** photosynthetic coherence spectroscopy; magnetoreception behavioral/spectroscopic evidence; NAND P/E endurance data.
- **L4 (conjecture/testable, not yet established):** H1–H3; the claim that the floor is an architecture choice in engineered systems (only nature currently witnesses it).

## §3. Why a Reader Should Care

Every group optimizing QEC overhead — and every funder pricing fault-tolerant machines — is optimizing against a limit they have not named. If the limit is thermodynamic, then the combinatorial route (better rate, higher threshold) yields diminishing physical returns, and the winning architectures will be the ones that minimize erasure, not the ones that maximize rate. The paper gives: (a) the floor estimate and the ranking method (JPCUB applied to QEC), (b) a classical, near-term, cheap testbed (flash memory) where the core hypothesis can be falsified this quarter without quantum hardware, and (c) a cross-domain bridge between thermodynamic computing, QEC engineering, and quantum biology — three communities that currently price correction in three different vocabularies.

## §4. Practitioner Section

**What a practitioner can do with this result:**

1. **Flash-memory test (immediate).** A storage engineer can implement the H2 benchmark today: take an open NAND error-model workload (bit-flip rates by P/E cycle age), implement (i) an LDPC decoder baseline and (ii) a nested-ball/tree code decoder of equal rate, and measure joules per corrected bit including write-amplification and P/E wear amortization. The paper will publish the exact protocol, thresholds, and the pre-registered falsifier.
2. **QEC cost accounting.** A QEC researcher can apply the erasure-count decomposition to their own architecture's cycle and compute its floor. The paper provides the counting template (syndrome extraction, majority vote, ancilla re-init) and worked examples for repetition, Hamming, surface, and qLDPC families.
3. **JPCUB instrumentation.** A quantum-computing vendor can report E_cor per logical operation alongside rate/distance/threshold, following the JPCUB anti-gaming rules (system-level energy, no cherry-picked decode-only numbers).

## §5. Method and Phases

- **P0 (this plan):** WBS claim, branch, core-claim lock. DONE below.
- **P0.5:** Universal Ignorance Audit (15 questions) on the core claim.
- **P1:** Corpus due diligence (DUE-DILIGENCE-DEPTH-1: ≥3 query formulations, limit ≥20, cross-system ID validation, ≥2 adjacent WBS domains — QEC engineering + INM/information physics + quantum biology; external verification of Landauer lineage and nature-witness citations; arXiv sweep for recent QEC-energy work).
- **P2:** Draft paper (plain scholarly prose; no internal pipeline vocabulary; title-visible bridge already in the title; explicit terminology crosswalk table: erasure ↔ syndrome reset ↔ information destruction; kT·ln2 ↔ bit erasure cost; structural protection ↔ passive stability; JPCUB ↔ energy-per-correct-answer).
- **P3:** Computational verification (COMPUTATIONAL-VERIFICATION-1): Landauer arithmetic at 300 K and 4 K; erasure-count per cycle per family; E_cor ≥ E_floor inequality checks; NAND P/E energy model; seeded Monte Carlo for H2's flash workload. Scripts + outputs into `artifacts/verification/`; reproducibility statement.
- **P4:** Gap analysis vs. corpus; reconcile hypothesis-card wording with executed tests (HYPOTHESIS-CARD-EXECUTION-PARITY-1).
- **P5:** Self-review; internal-counts sweep; premise-depth disclosure in the abstract-adjacent text.
- **P6:** Commit-tag-lock v0.4; red-team reviewer dispatch.
- **P8:** Publish (TITLE-EXISTENCE-PRE-PUBLISH-1 already cleared: 0 Zenodo hits for this title; PUBLISH-LOCK-1 before publish; Zenodo + R2 mirror `qnfo-releases/YYYY/MM/jpcub-qec-landauer/` + D1 papers + KG node + Vectorize index; METADATA-RELATIONS-ASSERT-1; POST-PUBLISH-FRONTMATTER-ASSERT-1).

## §6. Verification Plan (gates)

- Landauer arithmetic: golden values kT·ln2 at 300 K (~2.87×10⁻²¹ J ≈ 0.0179 eV) and 4 K (~3.8×10⁻²³ J); script-verified against independent computation.
- Erasure counts: per-cycle erasure table for repetition [n,1], Hamming [7,4], surface-code round, qLDPC round — every number recomputed in code.
- NAND energy model: E/P-cycle per cell, corrected-bit energy comparison, endurance amortization — scripted with seeded RNG.
- Rendering gates before publish: check_rendering.py (odd-$, currency escaping, frontmatter duplication, glyph checks).
- Reference fidelity: REFERENCE-TITLE-FIDELITY-1 (rendered list from citation-audited bib, cross-checked).

## §7. Open Questions and Risks

- **Rate vs. energy confusion risk:** constant-rate quantum LDPC codes (Haah et al.) show combinatorial overhead can approach constants; this paper claims nothing against that — the floor claim is about ENERGY, not rate. The paper must state both and keep them distinct, or it will be misread as a threshold-theory challenge.
- **Nature-witness strength:** photosynthesis/magnetoreception evidence is behavioral/spectroscopic, not a direct energy-per-operation measurement; H3 is therefore comparative and qualitative until instrumentation exists. Stated as such.
- **Erasure-count floor estimate could be challenged** on reversible-QEC grounds (e.g., measurement-free logical operations that avoid resets). Acknowledged in L2: the bound applies to active-correction architectures that reset their syndrome registers; reversible corrections escape the erasure bill and will be discussed as the boundary of the claim.
- **Flash-memory baseline choice:** LDPC is the industry standard for NAND; using it as the baseline is the strongest possible test, and also the hardest to beat — that is the point.

## §8. Phase-0 Closeout (this document)

- WBS row: `QNFO.JPC.003` inserted in `portfolio-state.program_registry` (parent `QNFO.JPC`, order 3).
- Branch: `res/paper/jpcub-qec-landauer` on `QNFO/qnfo-research`, created from clean `origin/main`.
- Title uniqueness: 0 Zenodo records, 0 D1 paper rows for the title/slug.
- Tag: `v0.1-phase0-jpc003`.
