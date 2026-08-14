# Deep Research — QNFO.RES.009 (P4 working draft, skeleton)

**WBS:** QNFO.RES.009.P4 · **Date:** 2026-08-14 · **Status:** DRAFT (skeleton for derivation work)

## 0. Framing

Known part [KNOWN]: in 3+1D relativistic QFT, spin and statistics are locked (Pauli
1940; Duck-Sudarshan 1998); in 2+1D, anyons realize fractional exchange phases
(Leinaas-Myrheim 1977; Wilczek); the categorical statement is that exchange phase
equals topological spin, R = e^{2πis} (ribbon braided tensor categories; Johnson-Freyd
2015 for TQFT; Oeckl 2000 for quantum-group unification; Trung 2022; Nardin 2022 for
FQH).

Novel target [NOT YET EVIDENCE]: F2 — a calculus of re-entrant distinctions can
*derive* the two 1-dimensional representations of the symmetric group S_n (trivial =
bosonic symmetric algebra; sign = fermionic exterior algebra) from the act of
distinction itself, without importing QFT postulates.

## 1. The two modal exponentials

Standard model of `!` in the treatise (Appendix A): !A = ⊕_n S^n(A) (symmetric
algebra) — silently bosonic. Proposal (seed: Obsidian _26226132526, 2026-08-14):

    !_S A = ⊕_n S^n(A)          (bosonic: symmetric power, the loop)
    !_Λ A = ⊕_n Λ^n(A)          (fermionic: exterior power, the tree)

Both are idempotent-projector eigenspaces of the exchange operator P (P² = 1):
P_sym = (1+P)/2, P_antisym = (1-P)/2, with P_sym² = P_sym, P_antisym² = P_antisym.

TASK T1: formalize the two modal exponentials in a graded/differential linear logic
(DiLL), with grading ε ∈ {0,1} and braiding σ_{A,B}(a⊗b) = (-1)^{|a||b|} b⊗a.
Deliverable: proof that !_S and !_Λ are both exponential modalities (digging +
dereliction + promotion) of the graded symmetric monoidal category.

## 2. The braiding of two marks

TASK T2: construct, in a compact closed category with a distinguished object M (the
mark: M ⊗ M → M by Calling; M → M by Crossing), the exchange of two marks as a
morphism σ_{M,M} and show that the monodromy constraint (exchange twice = identity
up to the ribbon twist) forces σ² = id in 3+1D. Concretely: the configuration space
C_2(R^3) has π_1 = Z/2; transport around the non-contractible loop defines the sign.
Deliverable: a category-theoretic restatement of the standard topological proof of
the ±1 dichotomy (Fadell-Neuwirth / Leinaas-Myrheim) in the language of the mark.

## 3. Dimension quantization of s

TASK T3: show that in the braided setting, spin s is the twist phase θ_X =
quantum-trace(c_{X,X})/d_X; dimension enters only through the allowed braided
structures (symmetric category in d≥3 → s ∈ Z or Z+1/2; braid group in d=2 → s ∈ R/Z).
Deliverable: the table

| d | motion group | braided structure | allowed s | statistics |
|---|---|---|---|---|
| 2 | B_n | ribbon (non-symmetric) | R/Z | anyons |
| ≥3 | S_n | symmetric | Z, Z+1/2 | bosons/fermions |

## 4. F2 falsifiability protocol

- If T1-T3 can be completed with no postulate beyond Calling/Crossing + compact
  closure → F2 succeeds → C3 gains [NOT YET EVIDENCE]→[EVIDENCE-lite] status.
- If the derivation requires importing microcausality or Lorentz structure as an
  additional axiom → the treatise claim is graded [CONTESTED] and the paper states
  the minimal extra structure needed (this is the honest outcome either way).

## 5. Calibration register (placeholder — populate at P4 closeout)

[CHECK: 2027-06] F2 derivation status: SUCCEEDED / FAILED / PARTIAL.
[CHECK: 2027-06] External citation rate of the invariant formulation (R = e^{2πis}).

## 6. Open risks

R1 (KIF-60): C1 is [RETRODICTION] — no predictive credit claimed.
R2: the exterior-algebra reading of `!` may break digling/dereliction in DiLL — T1
must be checked against DiLL axiomatics (Faggian-Hyland, Ehrhard-Regnier).
R3: MAP-TERRITORY — every identity claim carries a falsifiability condition (F1/F2).

## 7. Next actions

1. T1 formalization notebook (DiLL axioms, graded braiding) — artifacts/notebooks/t1.md
2. T2 configuration-space restatement — artifacts/notebooks/t2.md
3. T3 dimension table with ribbon-category proofs — artifacts/notebooks/t3.md
4. P4 closeout: full derivation or impossibility argument + calibration register.
