# Deep Research — QNFO.RES.009 (P4 status: derivation sketches complete)

**WBS:** QNFO.RES.009.P4 · **Date:** 2026-08-14 · **Status:** T1-T3 DERIVATION SKETCHES COMMITTED

## 1. Summary of results

| Task | Deliverable | Status | Key content |
|---|---|---|---|
| T1 | Two modal exponentials | DERIVATION SKETCH | $P_{\mathrm{sym}}/P_{\mathrm{antisym}}$ idempotent projectors of exchange; Sym(A) = Λ(A) for odd A; $!_S$/$!_{\Lambda}$ are grading components; the two 1D characters of $S_n$ identified |
| T2 | Braiding of two marks | DERIVATION SKETCH | $\sigma_{M,M} = \eta\,\mathrm{id}$, ribbon identity forces $\eta = \theta_M$; symmetric category $\Rightarrow \eta = \pm 1$; $\eta = -1$ identified with Crossing ($e^{i\pi} = -1$), $\eta = +1$ with Calling |
| T3 | Dimension quantization | DERIVATION SKETCH | d=2: $s \in \mathbb{R}/\mathbb{Z}$ (anyons); d≥3: $s \in \{0,1/2\}$ (bosons/fermions); Lorentz input boundary documented |

Notebooks: `artifacts/notebooks/t1.md`, `t2.md`, `t3.md`.

## 2. Honest boundary (stated in paper §5)

The mark calculus forces the *two eigenvalues* of exchange (statistics) from distinction + compact closure + involutive braiding. The *spin–statistics connection* (which eigenvalue ↔ which spin) requires the Lorentz/positivity input external to the mark. The paper does not claim a full derivation.

## 3. KIF-60 status after P4

- C1 (invariant R = e^{2πis}): [RETRODICTION — not evidence] — unchanged, correctly labeled.
- C2 (monograph silent symmetric algebra): textual finding, verified against the monograph's Appendix A.
- C3 (mark-calculus derivation): [NOT YET EVIDENCE] — T1-T3 are sketches; full DiLL axiomatic check + n-particle character derivation pending next iteration.

## 4. Calibration register

| ID | Prediction | Window | Status |
|---|---|---|---|
| C-01 | The symmetric/exterior split of the exchange operator on the odd mark reproduces the two 1D characters of S_n | P4 closeout | [IN PROGRESS] — T1 sketch confirms for n=2, general n pending |
| C-02 | The ribbon identity (twist = braiding trace) is the categorical form of the spin-statistics relation | P5 publication | [CONFIRMED BY LITERATURE] — Oeckl 2000, Johnson-Freyd 2015, Bruillard 2009 |
| C-03 | No published derivation of exchange statistics from the mark calculus exists (silo claim) | P1/P2 sweeps | [CONFIRMED] — 989-record corpus + Zenodo/arXiv sweeps found none |

## 5. Next actions

1. T1 extension: full digling/dereliction/promotion check for $!_S$/$!_{\Lambda}$ in DiLL; n-particle character derivation.
2. T2 extension: explicit cup-cap construction for the self-dual mark.
3. P5: paper draft (committed), PDF build (CDP pipeline), Zenodo deposit.
