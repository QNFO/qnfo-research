# Bayesian Evidential Weight Gate — QNFO.INM.001 (KIF-60, HARD sub-gate of KIF-29)

**WBS:** QNFO.INM.001 — Signal-Worker Boundary Confinement
**Date:** 2026-08-16 · **Phase:** 1b · **Immutable anchors:** the git commit containing this file (hash in session memory/tape) + sha256 recorded in the commit exec output. This document IS the pre-registration record.

---

## 1. Pre-Registration Record (timestamped predictions, pre-observation)

| ID | Prediction (stated 2026-08-16, BEFORE any new observation) | Falsification condition |
|:---|:-----------------------------------------------------------|:------------------------|
| PRE-REG-1 | In any non-Hermitian system with point-gap topology (NHSE), boundary-localized skin modes will NOT exhibit quantized conductance G = nG0, and will NOT be describable as classical field redistribution (skin effect). | Observation of G = nG0 quantization in an NHSE-metallic regime, or demonstration that NHSE localization is classical field redistribution → trichotomy (CORR-3) is WRONG. |
| PRE-REG-2 | Cooper-pair boundary transport in a topological-insulator geometry will NOT obey the original S-W "boson=signal" mapping (composite-boson exception C4 holds). | If Cooper-pair boundary transport obeys boson=signal with no exception → C4 is wrong and the corrected ontology over-claims. |
| PRE-REG-3 | The surface/bulk category distinction becomes experimentally indistinguishable as k_BT → Δ_gap: quantized edge conductance will vanish continuously with T/T_gap → 1. | Quantized edge conductance surviving at k_BT >> Δ_gap → thermal-blurring prediction is wrong. |

Platforms already exist for PRE-REG-1 (experimental NHSE: Schneider et al., arXiv 2505.03658, 2025) and PRE-REG-3 (standard TI transport).

## 2. Falsifiability Matrix

| Claim | Type | Disconfirmation condition | Status |
|:------|:-----|:--------------------------|:-------|
| C1 | established | — (physics) | established — zero novelty weight |
| C2 | MAP | no new observable consequence → relabeling | OPEN — currently [RETRODICTION] |
| C3 (LCI) | MAP-speculative | independent derivation/reproduction fails | OPEN, flagged |
| C4 (composite bosons) | MAP | a closed mapping under composites exists | OPEN — PRE-REG-2 anchors it |
| CORR-3 (NHSE third category) | MAP | PRE-REG-1 fails | OPEN — pre-registered |
| CORR-4 (count/Ostrowski) | analytical | n/a as physics | [UNTESTED] — defers to UMP corpus |

## 3. Surprise Accounting Table (P(match | random structure))

| Claim | Null model | P(match \| random) | Note |
|:------|:-----------|:-------------------|:-----|
| C1 trichotomy classification | random assignment of 14 corpus hits + 3 external literatures to 3 categories | ~0.02 (3! / 3^17 if arbitrary) | classification-by-construction for the 3 established phenomena; the risky component is DISJOINTNESS, tested by the Weyl case |
| PRE-REG-1 (no quantization in NHSE) | NHSE metallic regime randomly exhibiting quantized conductance | LOW (quantization requires a gap + protected edge; point-gap NHSE has no line gap) — genuine risky prediction | positive weight if confirmed |
| PRE-REG-2 (Cooper pairs break mapping) | boson=signal mapping arbitrarily extended to composites | ~0.5 (both outcomes plausible a priori) | weak prior; confirmation gives modest weight |
| PRE-REG-3 (thermal blurring at T_gap) | edge quantization surviving arbitrarily above Δ/k_B | LOW (thermal occupation of bulk states is generic) | positive weight if confirmed; note: partially retrodictive — established physics already shows thermal activation |

## 4. Δlog-odds Summary

| Claim | Δlog-odds | Classification |
|:------|:----------|:---------------|
| C1 | ≈ 0 | [RETRODICTION — not evidence] (labeled established physics, no novelty claim) |
| C2 | ≤ 0 | [RETRODICTION] until PRE-REG-1/2 confirmations arrive |
| CORR-3 via PRE-REG-1 | > 0 IF experiment confirms | positive evidential weight — the honest novelty carrier |
| CORR-3 via PRE-REG-3 | ~0 (retrodictive component) | zero weight for the part already known |
| CORR-4 | n/a | [UNTESTED] — deferred |

**Consequence:** the corrected ontology's novelty claim is bounded by PRE-REG-1 (and secondarily PRE-REG-2). Until PRE-REG-1 is tested, the paper's MAP claims must stay labeled "unconfirmed internal proposal" (they do — core-claim.md C2 label).

## 5. Tautology Trap Audit

| Trap | Audit | Result |
|:-----|:------|:-------|
| Overfitting | Categories = 3; free parameters ≈ 3 ratio thresholds; established phenomena classified = 3 + Weyl counterexample handled as mode-confinement-of-bulk (named complication, NOT a 4th category). dof < matches. | PASS (marginal — thresholds must be pre-fixed, they are: δ/λ_F, ℓ/λ_F, k_BT/Δ) |
| Cherry-Picking | Denominator reported: 14 corpus hits (corpus-sweep-f1/f2/f3.json) + 3 external literatures; each classified; the Weyl bulk-conducting case is the named MISS, not hidden. | PASS |
| Absorption | Pre-declared: NO new category and NO new duality may absorb a counterexample without a new observable (the Weyl case is classified as mode confinement of a bulk Fermi arc — a complication within category 2, declared, not absorbed silently). | PASS |

## 6. Gate Output

KIF-60 satisfied: pre-registration record (this file), falsifiability matrix, surprise accounting, Δlog-odds summary, trap audit. Cross-domain correspondence claims carry zero evidential weight until PRE-REG-1/2/3 are tested; the paper's labels reflect this.
