# KIF-29 Consilience Gate — QNFO.RES.028 (Phase 1b, 2026-08-27)

## Cross-Domain Lexicon (domains selected from Phase 1 due-diligence evidence)

1. **Number Theory (NT)** — chosen because the adjudicated object is arithmetic: the Dirichlet family ζ(s)/ζ((m+1)s), roots of unity, characters. Evidence: RES.027 (10.5281/zenodo.22123068), p-adic anyon fusion/braiding (10.5281/zenodo.21208491).
2. **Quantum Statistics / Thermodynamics (QS)** — the target structures: Fermi-Dirac, Bose-Einstein, maximum entropy. Evidence: RES.027 §2, Self-Referential Scalar Family (10.5281/zenodo.22035210).
3. **Condensed Matter / Topological Order (CM)** — the anyon observable side: Haldane exclusion statistics, Laughlin phases, Fibonacci braiding, quantum Hall. Evidence: Ye-Marchetti-Su-Yu 1512.01783, Chen-Ng 9411008, Heiblum et al. 2209.15461, Rosenow-Halperin 2510.04319; corpus: pattern-particle-unification (10.5281/zenodo.22024856), operationalizing-generalized-symmetries (10.5281/zenodo.18199396).
4. **Information Theory (IT)** — the selection principle: exponential-family max-entropy, Fisher geometry. Evidence: RES.027 §2.3/§4, Adelic Shannon Theory (10.5281/zenodo.22024240).
5. **Computer Science / Quantum Computation (CS)** — the practitioner layer: braid-group gates, topological quantum computation, quantum-group substrates. Evidence: ultrametric-quantum-computation-langlands (10.5281/zenodo.20036379), zbw-anyon-braiding (10.5281/zenodo.21336087).

## Minimum-Viable-Finding per domain (each checked, non-trivial)

- **NT ↔ QS:** the Euler factor (1 + p^{-s} + … + p^{-ms}) is the single-mode partition function of an m-capped occupation mode; the m-family is the partition function of Gentile intermediate statistics (Gentile 1940). Computed (Phase 4, G1/G2).
- **CM ↔ QS:** the exclusion-constraint ↔ braid-phase relation is regime-restricted (HES holds for incompressible Hall liquids with edge only — Ye et al. 2015); the m-family (Gentile) is NOT Haldane exclusion statistics: the occupation curves agree only at the endpoints. Computed (Phase 4, G4).
- **CM ↔ NT:** the standard anyon models sit on the root-of-unity locus — Laughlin ν = 1/m gives e^{iπ/m} (a 2m-th root of unity); Fibonacci braid eigenvalues are q⁴ and −q² at q = e^{iπ/5}; the TL loop parameter |δ(q)| = 2cos(π/5) = φ at the same point. Computed (Phase 4, C1–C4).
- **IT ↔ QS:** the geometric/Bernoulli family is the unique constrained max-entropy distribution on {0..m} and {0,1}; the capped mode's canonical derivative yields the golden occupations (verified in RES.027; re-checked Phase 4, G2).
- **CS ↔ CM:** braid-group gates as the computational substrate of TQC; the in-corpus quantum-group records parameterize them at roots of unity (named-input consistency, not independent evidence).

## Silo Cost Table

| Domain | Structure name | Earliest | Connected | Silo cost | Key reference |
|:-------|:---------------|:---------|:----------|:----------|:--------------|
| Number Theory | ζ(s)/ζ((m+1)s) m-th-power-free series | 1737 (Euler product era) | 2026 (explicit m-family = Gentile partition function, RES.027/RES.028) | ~289 yr (identity age); 86 yr (Gentile connection) | Euler 1737; RES.027 22123068 |
| Physics | Gentile intermediate statistics (m-cap) | 1940 | 1991 (Haldane exclusion statistics); explicit m-family identification 2026 | 51 yr / 86 yr | Gentile 1940; Haldane 1991 |
| Physics | Haldane fractional exclusion statistics | 1991 | 1994–2015 (braid-statistics relation, regime-restricted) | 24 yr | Haldane 1991; Chen-Ng 1994; Ye et al. 2015 |
| Physics | Anyons (fractional exchange phase) | 1977/1982 | 1997–2003 (TQC braid gates) | ~20 yr | Leinaas-Myrheim 1977; Wilczek 1982; Kitaev 2003 |
| Mathematics | Quantum groups / TL at roots of unity | 1971–1986 | 1997–2003 (anyon braiding data) | ~17 yr | Temperley-Lieb 1971; Drinfeld-Jimbo 1985; Kitaev 2003 |
| Physics | Spin-statistics connection | 1940 | — (conceded boundary, RES.011) | — | Pauli 1940; Duck-Sudarshan 1998 |
| Math-Physics | Primon/Riemann gas | 1990 | 2026 (p-adic/adelic statistics, RES.020/027) | 36 yr | Julia 1990; Spector 1990; RES.020 22035210 |

**Flag:** `[SILO-FAILURE: >50yr gap]` on the Gentile-intermediate-statistics line — the m-capped occupation family was known to physics since 1940 and its partition-function form is a classical arithmetic identity, yet the explicit identification "bounded-occupation family = Gentile statistics" only appears in this program (2026). This synthesis rectifies an 86-year fragmentation; the adjudication in this project (that the family carries counting, not phase) is the rectification's substance.

## Synthesis Consilience

**Meta-principle:** statistics are set by the algebra of local constraints (occupation caps — a counting datum on a real generating function), while exchange phases are set by the topology of exchange (braid/character data — a phase datum on configuration space); the two layers are independent in exactly the way the m-family's phase-blindness exhibits, and the bridge between them is character-theoretic: multiplicative characters evaluated at roots of unity, the same parameterization the in-corpus quantum-group records use.

**Frontier question:** what is the minimal structure that generates a phase rather than a cap — i.e., when does an arithmetic object acquire a braid representation beyond its abelianization? (The non-abelian extension of C2; successor direction to this project.)

## Bayesian Evidential Weight (KIF-60)

- m-family = Gentile partition function: identity check — `[RETRODICTION — not evidence]` for evidential-weight purposes (its value here is the explicit adjudication, not a discovery).
- Root-of-unity reproduction of Laughlin/Fibonacci phases: identity checks of established data — `[RETRODICTION]`; C2's weight is the characterization, not a prediction.
- Prime-gap specific-heat deviation (H2): the only forward computation in the set — graded `[PREDICTION]`, internal to the Riemann-gas model, pending independent scrutiny.

## Symmetric Audit (incumbent frameworks)

The incumbents that grade this program are: configuration-space topology (CST — braid/symmetric group derivation), the spin-statistics theorem, and QFT. Audited symmetrically: CST imports five silent scaffolds (named in RES.011) and concedes it cannot supply the spin-statistics connection without Lorentz symmetry; the spin-statistics theorem holds as the boundary both frameworks respect. The incumbent claim "exclusion-type constraints are the right language for anyonic statistics" is precisely what the HES↔braid literature restricts to special regimes — the same kill-standard applied to the program's own m-family claim. The audit is symmetric: this project disconfirms its own correspondence candidate (C1) with the same rigor it applies to the incumbent identification.
