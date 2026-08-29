# Corrected Dictionary of Arithmetic Quantum Thermodynamics — QNFO.RES.031 (M2, Phase 2)

- **Date:** 2026-08-29 · **Status:** Phase 2 draft (every C3 row carries a computable fix; full code verification at P3)
- **Object:** the primon gas — single-particle modes indexed by primes p with energies ε_p = ln p; many-body states indexed by integers n = ∏_p p^{a_p}; Hamiltonian = multiplication by ln n; inverse temperature β (formal; the identification β = s is a choice, flagged as such).
- **Preamble (corrected).** This is a term-by-term mapping between the quantum-statistical formalism of the primon gas and multiplicative number theory. It is **exact and model-specific** — a combinatorial/analytic isomorphism, not an analogy, and not a statement that "the physical universe and the mathematical universe are two dialects of the same statistical language." That preamble phrase (seed Dictionary) is withdrawn: it re-erects the L2→L4 slide that C4 forbids. The mapping is exact in the toy model and disciplined at the physical boundary.
- **C3 ledger cross-reference:** each corrected row is tagged `C3(a)`–`C3(k)` against the Phase-0-locked correction ledger.

## I. Fundamental Variables (corrected)

| Concept | Seed draft (error) | Corrected | Tag |
|---|---|---|---|
| Single-particle modes | `{ε_i} ↔ {ln n}` ("ε_i ≡ ln n_i") | Single-particle modes = **primes p**, energies ε_p = ln p. Many-body states = **integers** n = ∏ p^{a_p}, energies ln n. The two levels are different objects. | C3(a) |
| State count | N(Λ) = #{n ≤ e^Λ} | Many-body level count = ⌊e^Λ⌋ (integers); single-particle mode count up to Λ = π(e^Λ) (primes). The draft's row mixed them. | C3(a) |
| Inverse temperature | β ≡ s | β = s is a **formal identification** on the real section; no physical temperature is asserted anywhere (premise-boundary). | — |
| Chemical potential / fugacity | "e^{βμ} ↦ χ(p) in the Euler product" | Fugacity z = e^{βμ} gives Z_μ = ∏_p (1 − z p^{−β})^{−1} = Σ_n z^{Ω(n)} n^{−β} — **not** a Dirichlet series of a character. A character χ twists each Euler factor as ∏_p (1 − χ(p) p^{−s})^{−1} = L(s,χ): a multiplicative phase/parity filter, not a chemical potential. | C3(b) |
| Occupation | {n_p} ↔ ∏ p^{n_p} | Correct as stated; occupation exponents a_p of n = ∏ p^{a_p}. | — |

## II. Partition Functions (corrected)

| Object | Formula | Tag |
|---|---|---|
| Bose (unrestricted, a_p ∈ ℕ₀) | Z_B(β) = ∏_p (1 − p^{−β})^{−1} = **ζ(β)** | C1 |
| Fermi (squarefree, a_p ∈ {0,1}) | Z_F(β) = ∏_p (1 + p^{−β}) = **ζ(β)/ζ(2β)** | C1 |
| Maxwell–Boltzmann (distinguishable, correct) | ln Z_MB(β) = Σ_p p^{−β} = **P(β)** (prime zeta); Z_MB = exp P(β). The seed table's MB row "∏(1+x_p) with an extra N! factor" contradicts the unification rule and is withdrawn. | C3(c) |
| Gentile family (a_p ∈ {0,…,m}) | Z_m(β) = ∏_p (1 − p^{−(m+1)β})/(1 − p^{−β}); m = 1 → Z_F, m → ∞ → Z_B; **no exchange phase anywhere in the family** (occupation caps do not braid; anyons are braid phases, a different object — RES.028). | C1, C4 |
| Unification rule (prime-zeta expansions) | ln Z_B = Σ_{k≥1} P(kβ)/k; ln Z_F = Σ_{k≥1} (−1)^{k+1} P(kβ)/k; ln Z_MB = P(β). | C1 |

## III. Exchange Statistics as Arithmetic Filters (corrected)

Statistics = exponent rules on one integer lattice: Bose a_p ∈ ℕ₀; Fermi a_p ∈ {0,1}; Gentile a_p ≤ m. The generating functions are §II. The three free-gas statistics are inclusion-exclusion transforms of P(β) (§II unification rule) — **the transform acts on log Z, not on the statistics themselves** (seed "Theorem 1" wording corrected).

## IV. Thermodynamic Observables (corrected; β formal)

| Observable | Seed draft (error) | Corrected | Tag |
|---|---|---|---|
| Internal energy | U = −∂_β ln Z ✓ | U_B = Σ_p (ln p) p^{−β}/(1 − p^{−β}) = Σ_p ln p/(p^β − 1); U_F = Σ_p ln p/(p^β + 1) | — |
| Specific heat | "C_V = ∂_β U" (missing −β² factor, sign inconsistent with its own formula) | **C_V = −β² ∂_β U**; C_V^B = β² Σ_p (ln p)² p^{−β}/(1 − p^{−β})²; C_V^F = β² Σ_p (ln p)² p^{−β}/(1 + p^{−β})² | C3(d) |
| Entropy | "S_arith = Σ_p [ln(1−x_p) + x_p/(1−x_p)]" (wrong sign on the log term; second term dimensionally wrong — missing β ln p) | S = ln Z + βU = Σ_p [−ln(1−x_p) + β (ln p) x_p/(1−x_p)], x_p = p^{−β} | C3(e) |
| Pressure (formal) | pV = (1/β) ln Z | pV/k_BT ≡ ln ζ(β) for Bose (formal; no volume is defined in the model) | — |
| Free energy | −βF ≡ Σ_p −ln(1−p^{−β}) ✓ | F = −(1/β) ln Z | — |

## V. Spectral Statistics (corrected; SPECTRAL-ESTIMATOR-CONSTRUCTION-1 compliant)

- **Level density.** Single-particle: ρ_1(E) = Σ_p δ(E − ln p). Many-body: N(E) = #{n : ln n ≤ E} = ⌊e^E⌋. The seed's "ρ(ln x) ∝ dπ/dx" conflated prime counting with integer level density — withdrawn (C3(a)).
- **Explicit formula (zeros = fluctuations, not definitions).** ψ_0(x) = x − Σ_ρ x^ρ/ρ − ln(2π) − ½ ln(1 − x^{−2}), ψ(x) = Σ_{n≤x} Λ(n). The zeta zeros enter as subleading oscillatory corrections to the smooth level count. (Seed draft truncated the last term — corrected.)
- **Zeros vs primes (the permanent distinction).** The Riemann **zeros are GUE-like** (Montgomery 1973, Odlyzko 1987); the **primes are Poisson-like beyond the hard core** (Gallagher 1976) with the twin-gap hard core: minimum gap 2 for primes ≥ 3 (the pair (2,3) is the unique gap-1 exception) ⇒ minimum unfolded spacing 2/ln p ⇒ **first bin exactly zero** under a bin width below that. The 34σ focused small-spacing exclusion tests the **primes**, not the zeros; the seed's "proves primes' zeros repel like GUE" is wrong in both halves (C3(f)).
- **Estimator constructions (six-bug checklist).**
  1. Pair correlation = k-th-neighbor decomposition with per-order normalization (NOT the spacing distribution).
  2. Unfolding: exact Li(x) via scipy.special.expi(log x) (the asymptotic series diverges for small arguments).
  3. Number variance: exact two-point reduction Σ²(L) = L − 2∫₀^L (L−s)(sin πs/πs)² ds is the reference; the Dyson asymptotic (1/π²)[log(2πL)+1+γ−π²/8] converges from below (mis-fit 20–33% at L ≤ 50, defined as (exact − Dyson)/Dyson; the inverse convention gives 17–25% — RES.030 R-1). Both formulas recorded; the asymptotic never used at small L.
  4. No rank unfolding (tautology — it is the smoothed staircase).
  5. Montgomery–Odlyzko on **zeros**; Gallagher + twin-gap hard core on **primes**.
  6. Form factor: single-realization K(τ) is **report-only at fixed τ** (non-self-averaging: Var(K/N) ~ O(1)); the ramp needs ensemble or τ-window averaging.
- **GUE two-point function.** R2(s) = 1 − (sin πs/πs)²; the spectral form factor is its Fourier dual — the seed's "K(τ) ↔ 1 − (sin πτ/πτ)²" conflated the two (corrected).

## VI. Operators (corrected)

| Seed row | Corrected | Tag |
|---|---|---|
| "Ĥ ↔ arithmetic derivative / von Mangoldt operator" | **H is the multiplication operator** (Ĥf)(n) = (ln n) f(n); eigenvalues ln n; Tr e^{−βĤ} = ζ(β). The von Mangoldt function Λ is a **coefficient**, entering via −ζ′/ζ = Σ_n Λ(n) n^{−s} — not eigenvalues. The arithmetic derivative is not an operator of this model. | C3(i) |
| "[A,B] ↔ distinction-based ultrametric" | **No correspondence claimed.** Commutators are operator algebra; the ultrametric is a metric on a hierarchy (UMP.014). Withdrawn. | — |
| "Interactions ↔ Dirichlet convolution" | Dirichlet convolution is multiplication of arithmetic functions (generating-function level). **Formal parallel only** — it is not an interaction term in any Hamiltonian. | C3(j) |
| "RG flow ↔ Möbius inversion" | Formal analogy only. | — |

## VII. Phase Transitions (corrected)

| Seed row | Corrected | Tag |
|---|---|---|
| "BEC ↔ pole at s=1"; β=1.06 as critical behavior | The pole at β = 1 is the **infinite-mode limit** (Bost–Connes: KMS-state symmetry breaking in the full system). A finite prime cutoff gives a smooth crossover, no singularity. **β = 1.06 is a numerical evaluation point near the pole — not a phase-transition temperature of any finite system.** | C3(g) |
| "Thermodynamic limit ↔ analytic continuation of ζ" | The mode-count limit is P_max → ∞ (giving ζ(β) on Re β > 1). **Analytic continuation is a mathematical extension of the function — it is not the thermodynamic limit** and corresponds to no finite system's partition function. | C3(g) |
| "Higher-order poles ζ^k ↔ k-body interactions" | ζ^k = ∏_p (1−p^{−β})^{−k} = **k independent copies (species)** of the gas — not k-body interactions. | C3(j) |

## VIII. Operational Theorems (corrected)

- **T1 (transform).** ln Z_B, ln Z_F, ln Z_MB are the three inclusion-exclusion transforms of P(β) (§II unification rule). Correct as stated; the transform acts on log Z.
- **T2 (observables are distinct).** The specific heat C_V(β) (thermodynamic channel; RES.030 D1 CONFIRMED separation at ≥2σ beyond computable P_max) and the 34σ focused small-spacing exclusion (two-point statistic on the prime spectrum's hard core; RES.030: focused z ≈ 33.8σ, uniform z ≈ −0.8) are **different observables with different nulls**. The seed's Theorem 2 conflated them — withdrawn. | C3(k)
- **T3 (map–territory).** The correspondence is structural (L2). No physical realization is asserted (L4 open; the negative list C4 is the correct statement of what is NOT claimed).

## IX. Meta-Lemma (corrected)

- Primes = **single-particle modes**. Integers = **many-body eigenstates** of H = ln n (the Fock-space basis). Riemann zeros = **subleading oscillatory corrections** to the level count via the explicit formula. The seed's "prime numbers are energy eigenstates" is withdrawn (C3(h)); "Riemann zeros are excited state fluctuations measured by thermodynamic observables" is withdrawn (C3(f),(k)) — zeros enter the count, not the leading thermodynamics.

## X. Verification plan (P3)

Coverage status: every C3 row above carries a computable **fix** (M2 requirement, red-team-verified 11/11 with seed antecedents). The P2 smoke suite (`artifacts/verification/verify-dictionary-p2.py`, 18/18 PASS, exit 0, re-run independently by two red-team slots) already verifies: the three partition-function identities at β = 2 (truncated products vs ζ(2), ζ(2)/ζ(4), P(2), tail-corrected via the 3-term E₁ expansion); the prime-zeta expansions to k = 30; Gentile limits (m = 1 → Fermi, m = 40 → Bose); the thermodynamic fixes (C_V formula vs finite-difference −β²∂_βU; S formula vs ln Z + βU); the anchor values (β²/(β−1)² = 312.1 analytic, exact total ≈ 311.9, and the adjudication that the legacy 316.3 is NOT the exact value — it is a finite-difference artifact of the published lineage); the twin-gap hard core (min gap 2 for primes ≥ 3); and the fugacity ≠ character distinction (Z_μ product vs Σ_n z^{Ω(n)} n^{−β}). The full P3 suite adds the declared coverage gaps: explicit-formula ψ_0, GUE R2(s), Σ²(L)/Dyson comparison, exact-Li unfolding, Fermi observables (U_F, C_V^F, S^F), level-count rows C3(a), operator attributions C3(h)/(i), ζ^k = k-species C3(j), the observables-distinct row C3(k), and the first-bin-zero statement as a computed bin count (not INFO-only).
