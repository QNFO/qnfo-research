# KIF-29 Cross-Domain Consilience Gate — QNFO.RES.009

**Date:** 2026-08-14 · **WBS:** QNFO.RES.009.P1b · **Slug:** spin-statistics-distinction
**Scope:** scaled to project size (Genre A structural-analysis paper).

## 1. Cross-Domain Lexicon (dynamic selection, evidence-based)

Domains selected from Phase 1 due-diligence evidence (each chosen because the same
structure appears there, independently):

| Domain | Lexicon term | QNFO/External evidence |
|---|---|---|
| Physics — relativistic QFT | spin, statistics, commutation/anticommutation, exchange phase | Pauli 1940 (via Duck-Sudarshan 10.1119/1.18860); Verch 10.1007/s002200100526 |
| Condensed matter | anyons, braiding phase, fractional spin, FQH quasiparticles | Leinaas cond-mat/9903329; Nardin 2211.07788; Trung 2208.13786 |
| Topology / TQFT | spin structure, fermion sign, 360° rotation | Johnson-Freyd 1507.06297 |
| Mathematics — tensor categories | braiding c_{X,Y}, twist θ_X, ribbon structure, modular data | Bruillard 10.1007/s00220-009-0908-z; Kong-Wen 1405.5858; Oeckl hep-th/0008072 |
| Foundations — Laws of Form / linear logic | mark, distinction, parity, ! modality, symmetric vs exterior algebra | Spencer-Brown 1969; treatise 10.5281/zenodo.21908818; STC 10.5281/zenodo.19547736 |
| Philosophy of physics | map/territory, structural realism, invariant vs convention | Bain (Weinberg's proof) 10.1016/s1355-2198(03)00066-2 |

## 2. Minimum-Viable-Finding (one non-trivial structural isomorphism per domain)

1. **QFT:** exchange phase of identical particles = 2π-rotation phase of the field: R = e^{2πis} (Pauli; Kuckert quant-ph/0208151 gives necessary+sufficient condition).
2. **Condensed matter:** FQH quasiparticles carry a *measurable fractional spin* that satisfies the same relation R = e^{2πis} (Comparin 2112.02901; Nardin 2211.07788; Trung 2208.13786 — proven from wavefunctions alone).
3. **Topology/TQFT:** reflection-positivity + spin structure forces the spin-statistics sign — a *topological version* of the theorem (Johnson-Freyd 1507.06297).
4. **Tensor categories:** ribbon condition θ_X = quantum-trace(c_{X,X})/d_X reduces to R = e^{2πis} for abelian anyons — the relation is a theorem about braided categories, not about 3+1D (Bruillard; Oeckl hep-th/0008072: SST ≡ unification of symmetries).
5. **Laws of Form / mark calculus:** mark parity (Z/2) is the same algebraic structure as the (-1)^{2s} grading — currently only an *asserted correspondence* in the treatise (its Appendix A silently imports the symmetric algebra for !); deriving it is this paper's F2 claim (NOT yet established).
6. **Philosophy:** the invariance under "changing the base" (dimension, frame, formalism) isolates R = e^{2πis} as the structural invariant; the boson/fermion binary is a 3+1D shadow (Anastopoulos quant-ph/0110169: "any distinction of identical particles comes solely from the choice of coordinates").

**Gate check:** ≥1 non-trivial isomorphism per domain — satisfied (items 1-6).

## 3. Silo Cost Table

| Domain | Structure name | Earliest | Connected | Silo cost | Key paper |
|---|---|---|---|---|---|
| QFT | spin-statistics theorem | 1940 (Pauli) | categorical/TQFT version 2015 (Johnson-Freyd) | **75 yr** | Pauli 1940; 1507.06297 |
| Condensed matter | anyons / fractional statistics | 1977 (Leinaas-Myrheim) | spin-statistics for anyons proven 2008 (Mund 0801.3621); measurable fractional spin 2021-22 | **31 yr** | cond-mat/9903329; 2208.13786; 2211.07788 |
| Tensor categories | braided/ribbon categories | 1986-93 (Joyal-Street) | SST as braided-category statement ~2000 (Oeckl) | **~14 yr** | Oeckl hep-th/0008072 |
| Laws of Form | Z/2 parity of the mark | 1969 (Spencer-Brown) | **NEVER** connected to exchange statistics (treatise 2026 asserts correspondence without derivation) | **57+ yr and counting** | Spencer-Brown 1969; treatise 10.5281/zenodo.21908818 |
| Geometric quantisation | exchange = symmetry transformation | 2001 (Anastopoulos) | independently reproduces SST without QFT | — | quant-ph/0110169 |

**Flag:** `[SILO-FAILURE: >50yr gap — this synthesis rectifies multi-generational knowledge fragmentation]` — the Laws of Form → exchange statistics gap (57+ yr, still open) is precisely this paper's F2 niche. Independence of the converging lines is satisfied: QFT (Pauli/Streater-Wightman), condensed matter (Leinaas-Myrheim, FQH experiments), category theory (Joyal-Street), and Laws of Form (Spencer-Brown) developed with no communication.

## 4. Synthesis Consilience

- **Meta-principle (invariant across all translations):** "Exchange phase = topological spin" (R = e^{2πis}); dimension, locality, and Lorentz invariance only *restrict which braided structures are realized* (symmetric in ≥3+1D → bosons/fermions; braid group in 2+1D → anyons).
- **Frontier Question:** Can the calculus of re-entrant distinctions *construct* the braiding of two marks (in a compact closed category) and derive the trivial-vs-sign representations of S_n from mark parity alone — making exchange statistics a theorem of distinction rather than a postulate? (F2.)

## 5. Symmetric Audit of Incumbents (user injunction 2026-08-04)

The spin-statistics theorem is itself audited with the same kill-criteria: it is dimension-dependent (fails in 2+1D), proof-dependent (nonperturbative generality not unconditionally proven — noted in the 2026-08-14 corpus), and scaffolded on microcausality/positive-energy assumptions. No pro-incumbent bias: the theorem is graded [ESTABLISHED IN 3+1D QFT], not [UNIVERSAL NECESSITY].

## 6. Gate Output

This file satisfies the Phase 1b HARD GATE: lexicon (6 domains, evidence-cited), minimum-viable-findings (6), silo cost table (5 rows + >50yr flag), synthesis consilience (1 meta-principle + 1 frontier question). KIF-60 sub-gate in `artifacts/bayesian-evidential-weight.md`.
