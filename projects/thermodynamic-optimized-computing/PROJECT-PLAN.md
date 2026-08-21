# PROJECT-PLAN: Thermodynamically Optimized (Topological/Quantum) Computing

**WBS:** QNFO.JPC.002
**Version:** v0.1-phase0
**Date:** 2026-08-21
**Repo:** QNFO/qnfo-research (host repo — QNFO/jpcub-validation is archived/read-only)
**Branch:** res/paper/thermodynamic-optimized-computing
**Parent mission:** QNFO.JPC.001 (JPCub Validation) — "What does a correct quantum answer cost in energy?"
**Seeds (vault notes, 2026-08-21):** _26233102906, _26233103004, _26233102948, _26233103017, _26233102902, _26233103051

---

## 1. Charter

Quantum-computing scaling is currently framed as a qubit-count and error-correcting-code problem. This project tests a different frame: **the binding constraint is thermodynamic, and the engineering response is hardware-level protection, not software-level correction.** Active quantum error correction (QEC) is an energy expenditure layered on fragile physical qubits. Hardware-level protection — topological order, Majorana/anyon modes, dissipation-structured passive architectures, high-coherence materials — substitutes material structure for correction energy. That is the quantum analogue of the classical semiconductor's noise margin: silicon logic needs no active error correction because a bit is carried collectively by ~10^4–10^6 electrons with gain restoration. A "quantum semiconductor" — a protected-qubit substrate requiring little or no active QEC — is the target architecture class, and platforms are ranked by JPCUB (joules per correct solution).

This project: (1) sharpens that claim into a falsifiable design thesis; (2) scores candidate platforms on a JPCUB proxy; (3) pre-registers the prediction of the crossover where hardware protection beats active QEC energetically; (4) feeds the CWI Quantum Algorithms / QEC Summer School poster (2026-08-24 decision item in GTD).

## 2. Core Claim (LOCKED at P0)

> **C1.** The dominant cost of quantum computation — energy per correct solution — is a thermodynamic quantity set by (a) proximity to the Landauer erasure bound, (b) the Margolus–Levitin speed limit, and (c) the error-suppression budget of the substrate. Active QEC is an energy tax on fragile qubits; hardware-level protection substitutes material structure for correction energy, as the classical noise margin did for silicon. Under the JPCUB metric, the target architecture is a quantum semiconductor: a protected-qubit substrate with minimal active QEC, and entropy gradients — not Hilbert-space axioms — are the sufficient design vocabulary.

**Sub-claims (ordered by testability):**
- C1a. JPCUB ranking separates platforms more sharply than qubit-count or gate-fidelity rankings (testable with published platform data).
- C1b. There exists a noise-regime crossover where protected qubits beat QEC-protected fragile qubits at equal JPCUB (model testable; hardware testable in the long run).
- C1c. The 1D entropy-gradient vocabulary reproduces the thermodynamic bounds without Hilbert-space structure (foundation link to QNFO.RES.021; weakest, least needed for the engineering thesis).

## 3. Premise-Depth Disclosure (SO-WHAT-GATE-1)

Where the premises end and what is derived:

| Layer | Status | Content |
|---|---|---|
| L0 | **Imported primitive** | Second law / entropy; Landauer bound kT ln 2; Margolus–Levitin bound; no-cloning theorem; JPCUB metric definition (from QNFO.JPC.001) |
| L1 | Derived (textbook) | Classical semiconductors need no active QEC because of collective encoding + gain restoration |
| L2 | Derived (standard) | No-cloning ⇒ no quantum majority vote ⇒ active QEC unavoidable for unprotected qubits |
| L3 | **Imported, experimentally unproven at scale** | Topological protection suppresses local errors exponentially (TQC literature, Majorana); dissipation-structured passive architectures (QNFO.RES.017 claim, no hardware demo) |
| L4 | **This paper's own claim** | The thermodynamic-optimization synthesis: hardware protection as energy strategy, quantum-semiconductor target, JPCUB ranking, entropy-gradient vocabulary |

The theory is as deep as L4, which is a synthesis resting on L3's unproven imports. The paper must NOT present L4 as a theorem. Honest-negatives ledger: under independent errors the program's own tree-code thresholds sit ~55× worse than surface codes (Qudit QEC thesis 10.5281/zenodo.21046993; prime-valuation correction 10.5281/zenodo.21979060 published as self-falsification) — the protection claim lives only in the correlated-failure regime.

## 4. SO-WHAT (why a reader should care)

QC R&D is committing tens of billions to qubit counts and QEC overhead. If C1 is right, a material-science dollar buys more joules-per-solution than a decoder-engineering dollar, and the field's roadmap metric (logical error rate at any energy cost) is the wrong selection criterion. A reader gets: (a) a falsifiable design thesis; (b) a concrete platform-ranking table; (c) a pre-registered crossover prediction that any hardware group can check.

## 5. Practitioner Relevance (PRACTITIONER-RELEVANCE-1)

- **Decision tool:** JPCUB proxy scorecard for superconducting transmon / trapped-ion / topological (Majorana) / silicon-spin / photonic platforms, computable from published per-gate energy, coherence, and correction-overhead data.
- **Engineering target:** the crossover curve — physical-error rate p and protection exponent Λ(p) at which passive architectures win energetically — expressed in a spec-sheet form a device physicist can build against.
- **Language:** energy (J), power (W), error rate, overhead factor, dilution-fridge baseline — no niche-terminology dead-ends; the ultrametric/tree-code machinery enters only where it buys a concrete number.

## 6. Computational Verification Plan (COMPUTATIONAL-VERIFICATION-1)

Every quantitative claim verified in code BEFORE publication; scripts + outputs deposited (artifacts/verification/):
1. **Golden values:** Landauer kT ln 2 at 300 K / 4 K / 15 mK; Margolus–Levitin E ≥ πħ/(2Δt) evaluations for GHz–THz operation; Bremermann bound numbers.
2. **Crossover model:** energy-per-logical-operation E_QEC(p, d) vs E_passive(Λ, p) as functions of physical error rate and protection exponent; find the crossover; sensitivity to decoder efficiency and fridge overhead.
3. **Seeded Monte Carlo:** threshold-comparison statistics for the tree-code claims already in the corpus (BTQP 10.5281/zenodo.20109836 golden values re-run; RES.019 verify-scripts re-run).
4. **Reproducibility statement:** runtime, seeds, dependency versions, re-run instructions.
5. **Demo gate (flagship only):** interactive JPCUB crossover explorer via qwav-demo-kit (DEM-E0-T01..T05) if the paper reaches flagship status.

## 7. Universal Ignorance Audit (ZENODO-INQUIRY-1, administered P0 on C1)

Target: core claim C1. Answers written, not resolved (Phases 1–4 hold tension):

1. **Scaffolds:** (a) energy is the binding QC-scaling constraint, not coherence engineering or control wiring; (b) hardware protection is engineerable to competitive logical rates; (c) JPCUB is measurable across paradigms.
2. **Map–territory:** "quantum semiconductor" imports silicon economics; topological protection is probabilistic suppression, not a deterministic threshold margin — the map may mislead.
3. **Wobble:** the program's own data puts the tree-code advantage in the correlated-failure regime only; under independent errors it is ~55× worse than surface codes. The claim is strongest exactly where its own evidence is weakest.
4. **Inversion:** if active-QEC energy cost falls faster than protection engineering improves (better decoders, cryo-CMOS), the thesis inverts — software beats materials.
5. **Falsifiability:** kill-conditions — no platform reduces JPCUB below the fragile-qubit + QEC baseline within a stated window, or protected-qubit logical rates never exceed QEC-achieved rates at equal energy. Pre-register in the RES.017 register style.
6. **Invariant:** the thermodynamic bounds (Landauer, Margolus–Levitin) hold regardless of substrate — the invariant core is the bounds, not any specific material bet.
7. **Observer shift:** device physicist sees fabrication risk; QEC theorist sees decoding as the real lever; VC sees metric risk. Each would write a different paper.
8. **Power:** who benefits — protection-hardware vendors, topological labs, QWAV (JPCUB adoption); who is challenged — QEC-centric incumbents.
9. **Dangerous question:** does QWAV's JPCUB metric survive if the winning platform is NOT ultrametric/topological (e.g., photonic)? The mission could outgrow its founding narrative.
10. **Somatic:** discomfort lives in betting against the field's QEC consensus — the risk of reading contrarian.
11. **Willful ignorance:** the independent-error data already weakens the tree-code case and was not foregrounded until the honest-negatives review surfaced it.
12. **What the unknown wants:** a bounded, falsifiable engineering thesis — not another unification grand claim.
13. **Actionable now:** score 4–6 platforms on the JPCUB proxy; pre-register the crossover; draft the CWI poster around the honest ledger.
14. **Gift of not-knowing:** whether protection can win energetically is exactly the open research space QWAV can occupy; resolving it too early collapses the program's option value.
15. **Recursive meta-question:** is JPCUB itself well-defined across paradigms, or does it smuggle in a silicon-era notion of "solution"? (Seed of the next audit pass.)

## 8. Phase Plan (WBS-coded)

- [QNFO.JPC.002.P0] WBS resolve + branch + claim lock + this plan — THIS COMMIT
- [QNFO.JPC.002.P1] Corpus due diligence (DUE-DILIGENCE-DEPTH-1): ≥3 query formulations, full-corpus sweep, cross-system ID validation, ≥2 adjacent WBS domains (UMP/QEC/RES + CMP), external verification
- [QNFO.JPC.002.P2] Gap analysis + platform scorecard draft
- [QNFO.JPC.002.P3] Computational verification (Section 6 items 1–3)
- [QNFO.JPC.002.P4] Paper draft (plain publication prose; PUBLICATION-PROSE-GATE-1 + PAPERS-NO-NAVEL-GAZING-1 + PUBLICATION-BRAND-LANGUAGE-1)
- [QNFO.JPC.002.P5] Red-team + publish checklist (Zenodo + R2 + D1/KG + registry re-point)
- [QNFO.JPC.002.P6] Publish + post-publication adversarial audit

## 9. Pre-Mortem & Steelman

- **Most likely failure:** the crossover model shows active QEC wins at every plausible protection exponent — the paper then publishes that negative honestly (per program discipline) and the contribution becomes the scorecard + pre-registered kill-conditions. Acceptable outcome; not a failure of the pipeline.
- **Steelman against this project:** QEC overhead is already below the energy noise floor of any realistic fridge; hardware protection is decades away; JPCUB is not yet a field-accepted metric. Response: the paper's value is precisely the falsifiable frame + scorecard, independent of which side wins.

## 10. Status

Phase 0 committed 2026-08-21 (repo QNFO/qnfo-research after QNFO/jpcub-validation archived). Phase 1 due diligence runs in the same cycle.
