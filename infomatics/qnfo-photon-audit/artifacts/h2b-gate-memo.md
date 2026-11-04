# H2b Gate Memo: Knot-to-Mass Mapping

**Project:** qnfo-photon-audit — Task 1.5.2  
**Date:** 2026-07-21  
**Status:** Phase 1.5 Pre-Registration Gate  
**Gate:** Attempt parameter-free knot→mass mapping; expected: no such mapping exists → bin C confirmed

---

## 1. Gate Question

Does the knotted-photon literature provide or imply a parameter-free mapping from knot topology to fermion masses? Expected outcome (per Phase 0 bin table): no such mapping exists; bin C confirmed.

---

## 2. Lit Review Finding

The H2 literature review (`artifacts/lit-review-h2.md`, 24 external + 5 QNFO-internal sources) found zero papers that map knotted field topology to fermion masses without free parameters.

The H1 literature review (`artifacts/lit-review-h1.md`, 12 core + 5 background sources) surveyed the knotted-EM soliton literature including Rañada (1989, 1990), Trueba & Rañada (1996), Irvine & Bouwmeester (2008), Kedia et al. (2013), Arrayás et al. (2017), Burinskii (2000, 2015, 2023), Chernitskii (1999), and Hestenes (1990, 2010). None of these works produces a parameter-free mapping from knot topology to fermion masses.

---

## 3. Analytic Resolution

### 3a. What a knot-to-mass mapping would require

To claim that knot topology determines fermion masses without free parameters, a theory must:

1. **Assign a specific knot (or knot invariant) to each fermion flavor** (electron, muon, tau, up quark, down quark, etc.) — 6 leptons + 6 quarks = 12 assignments
2. **Derive the mass of each fermion from its knot invariant** using a well-defined formula with ZERO free parameters (or at most parameters already fixed by other known physics, e.g., the Planck mass or α)
3. **Reproduce the known mass spectrum** to within experimental uncertainty

### 3b. Known knot invariants

The standard knot invariants are:
- **Jones polynomial:** V(t) — 1-variable polynomial, Laurent in t^{½}
- **Alexander polynomial:** Δ(t) — 1-variable polynomial
- **HOMFLY-PT polynomial:** P(a,z) — 2-variable polynomial
- **Knot genus, crossing number, unknotting number** — integer invariants

Key constraint: there are infinitely many distinct knots. Even if each fermion mass corresponds to a specific knot, this is a post-hoc assignment — the mapping is not predicted, only fit.

### 3c. Chernitskii (1999) — Closest approach

Chernitskii's "solitons as particles" program (1999, hep-th/9901128) constructs topological solitons from nonlinear electrodynamics and associates their Hopf invariants with quantum numbers. However, Chernitskii's mapping is qualitative:

- Hopf invariant H → electric charge (integer quantization)
- Knot linking number → possibly other quantum numbers

This is an integer-to-integer mapping (topological invariant → quantum number), NOT a real-number-to-real-number mapping (topological invariant → mass in MeV). Mass values are continuous real numbers; knot invariants are typically integers or polynomial coefficients. There is a fundamental mismatch between the codomains.

### 3d. Burinskii (2000, 2015, 2023) — Kerr-Newman route

Burinskii's Kerr-Newman electron model produces the Dirac gyromagnetic ratio g=2 (classical value from Kerr geometry), and the KN solution has a mass parameter M that is NOT derived from topology — it is one of the free parameters of the Kerr-Newman solution (together with angular momentum a and charge e).

### 3e. Why this is a fundamental problem

The Standard Model fermion masses span 6 orders of magnitude:
- Electron neutrino: < 1 eV (possibly much lower)
- Electron: 0.511 MeV
- Top quark: 173 GeV

Any theory that derives these from knot topology must explain why certain knots correspond to vastly different masses. The knot invariants (crossing number, genus, polynomial coefficients) are small integers — typically O(1) to O(100). Mapping these to masses spanning 10^6 requires either:
- An amplification mechanism (e.g., exponential dependence on invariant)
- Free parameters (tuning the coupling between topology and mass)

No paper in the surveyed literature provides either.

---

## 4. Verdict

**H2b gate: CONFIRMED BIN C.**

**No parameter-free mapping from knot topology to fermion masses exists in the published literature.** The mapping found in the closest approaches (Chernitskii, Burinskii) is either qualitative (Hopf invariant → charge, which is integer-to-integer) or dependent on free parameters (mass M is a free parameter of the Kerr-Newman solution, not derived from topology).

### Falsifiability

The H2b claim would be SUPPORTED if: a derived formula M(knot_invariant) reproduces at least 3 known fermion masses to within experimental uncertainty with ZERO free parameters (or parameters only from known physics like α, m_P). It would be DISCONFIRMED if: it is proven that knot invariants, being finite integer sets, cannot span the continuous real-valued mass spectrum without introducing free parameters that effectively become the mass values themselves.

---

## 5. Recommendation for Gate Summary (Task 1.5.5)

- **H2b → Bin C (confirmed):** Log as formally unsupported. The mapping has not been constructed in any peer-reviewed work. Recommend no Phase 2 test for knot-to-mass predictions. Standard Model Yukawa parameters remain the experimentally validated mass-generation mechanism.
