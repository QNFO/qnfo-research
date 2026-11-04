# H3 Gate Memo: COTT vs Standard Reversible Logic

**Project:** qnfo-photon-audit — Task 1.5.3  
**Date:** 2026-07-21  
**Status:** Phase 1.5 Pre-Registration Gate  
**Gate:** Resolve analytically: does COTT permit any operation standard reversible logic cannot?

---

## 1. Gate Question

The Phase 0 project plan ([§1.2 core claim reformulated in PROJECT-PLAN.md](PROJECT-PLAN.md)) anticipated that the COTT/Silent Radix claim group might possess computational capabilities not available to standard reversible logic (Bennett 1973, Toffoli 1980, Fredkin 1982). This gate memo resolves whether that claim is substantiated.

---

## 2. Lit Review Finding

The H3 literature review (rtifacts/lit-review-h3.md, 18 external + 2 QNFO-internal sources) established:

1. **Zero external COTT papers:** No dedicated COTT paper exists in arXiv, Semantic Scholar, or web search outside the QNFO corpus ([QNFO-INTERNAL] only). This is a **critical validation gap**.

2. **Standard reversible logic already achieves zero dissipation:** Bennett (1973) proved that logically reversible computations can in principle dissipate zero energy. Toffoli (1980) and Fredkin (1982) provided universal reversible gate sets.

3. **No experimental evidence for sub-Landauer computation:** The Landauer principle's lower bound of kT ln 2 per erased bit has been experimentally confirmed (Bérut et al. 2012, Nature). No peer-reviewed experiment demonstrates computation below this bound.

4. **COTT is a redundant formalism:** Standard reversible logic (Bennett, Toffoli, Fredkin) already achieves exactly what COTT would need to achieve. COTT adds no explanatory power beyond what reversible logic already provides.

---

## 3. Analytic Resolution

### 3a. What standard reversible logic can do

Bennett (1973) proved: **any Turing-computable function can be computed by a logically reversible machine with no theoretical lower bound on energy dissipation other than zero.** The catch: the machine must retain all intermediate results (no erasure), requiring memory that grows with computation length.

The universal gate set {Toffoli, CNOT, NOT} is logically reversible and logically complete:
- NOT: 1-bit, self-inverse, energy cost = 0 in principle
- CNOT: 2-bit, self-inverse, energy cost = 0 in principle  
- Toffoli (CCNOT): 3-bit, universal for classical reversible computation

Any logically reversible Boolean function can be implemented with these gates. The energy cost of a Bennett-clocked reversible computation is determined by the adiabatic switching speed — arbitrarily close to zero as the clock period → infinity.

### 3b. What COTT claims to enable

The COTT concept (as described in QNFO-internal documents) claims that:
1. Charge-only thermodynamic processes can encode and process information
2. These processes bypass the Landauer limit through charge conservation
3. The photonic substrate enables computation through charge-only dynamics

### 3c. Gap analysis

| COTT Claim | Standard Reversible Logic | Gap |
|-----------|--------------------------|-----|
| Zero-dissipation computation | Achieved (Bennett 1973) — logically reversible computation has no theoretical lower bound on dissipation | **No advantage** |
| Below-Landauer erasure | Not possible — Landauer limit applies specifically to erasure; reversible logic AVOIDS erasure entirely | **Category error:** COTT conflates erasure (which reversible logic avoids) with computation (which is already zero-dissipation in principle) |
| Charge-based encoding | Equivalent to voltage/current-based encoding — any physical state variable can encode bits | **No new capability** |
| Photonic substrate advantage | Bennett's proof is substrate-independent — applies to ANY physical system with Hamiltonian dynamics | **No substrate-specific advantage** |

### 3d. Formal statement

**THEOREM (informal):** COTT does not permit any logical operation that standard reversible logic (Bennett 1973, Toffoli 1980) cannot perform, nor does it achieve below-Landauer erasure (which would violate the Second Law of Thermodynamics in the form proven by Frank 2018, arXiv:1806.10183).

**Proof sketch:**
1. Bennett (1973) proves: any Turing-computable function is logically-reversibly computable → all logical operations achievable
2. Landauer (1961) + Frank (2018) prove: erasing one bit at temperature T dissipates ≥ kT ln 2 (rigorous consequence of mathematical physics)
3. COTT claims below-Landauer computation via charge-only processes → this is EITHER:
   - (a) A claim about logically reversible computation, in which case it is redundant with Bennett (already proven), OR
   - (b) A claim about below-Landauer erasure, in which case it would violate the Landauer limit unless a specific loophole in the proof is identified — which no COTT paper does
4. In no case does COTT provide a capability beyond standard reversible logic

---

## 4. Verdict

**H3 gate: CONFIRMED BIN C.**

COTT provides no operation or capability beyond standard reversible logic (Bennett 1973, Toffoli 1980, Fredkin 1982). The claim that COTT enables computational advantages through charge-only thermodynamics is (a) redundant with established reversible computing theory if interpreted as a logical reversibility claim, or (b) in conflict with the Landauer limit if interpreted as a sub-Landauer erasure claim — and in neither case does it provide any independently validated computational capability.

### Falsifiability

The COTT claim would be SUPPORTED if: a published, peer-reviewed COTT proof demonstrates an operation achievable by charge-only processes that is not achievable by standard Toffoli-Fredkin reversible logic. It would be DISCONFIRMED if: a proof shows COTT is mathematically equivalent to standard reversible logic (expected outcome based on current evidence).

---

## 5. Relationship to H3 Lit Review

This gate memo is the formal resolution of the H3 literature review. The lit review found zero external COTT papers; this gate memo closes the logical loop by proving that even if COTT were formally defined, it would provide no capability beyond standard reversible logic.

### Recommendation for Gate Summary (Task 1.5.5)

- **H3 → Bin C (confirmed):** Log as formally untestable because no external COTT definition exists. Recommend no Phase 2 test for COTT. Standard reversible logic comparison suffices as gate resolution.
