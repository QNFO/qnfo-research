# OUTLINE — QNFO.RES.027 (working, P2→P3)

- **Title (working):** Quantum Statistics from the Adelic Product Formula: The Squarefree Origin of the Fermi–Dirac/Bose–Einstein Distinction
- **Slug:** adelic-quantum-statistics · **Branch:** res/paper/adelic-quantum-statistics · **Phase:** P2 close → P3 draft

## Abstract (skeleton)

The two quantum statistics are the maximum-entropy occupation distributions of a multiplicity-constrained lattice: the unrestricted integer lattice carries the Bose–Einstein occupation distribution, and the squarefree restriction — one prime factor per constituent, at most — carries the Fermi–Dirac distribution, with the product formula ∏_v|x|_v = 1 as the audit invariant. Per-place identifications at fugacity z = 1/p (β_p = ln p) are established prior art [RES.020]; this paper supplies the tiers those records leave open: the global lattice identities, the per-distinction rate γ = 1/N from bath degeneracy, the symplectic structure as the sign-normalized generator selected by exclusion, the Möbius-parity dictionary of composite statistics, and the bounded-occupancy interpolation family that anyonic statistics must contact. Epistemic register: no physical particle is implied; the claims are isomorphisms of mathematical structure; the physical labels attach at the statistical-distribution level.

## 1. Introduction

1.1 The question: why two statistics — and only two in d ≥ 3 — as a multiplicity fact, not a particle-type fact.
1.2 The sequence: Paper 1 (Landauer floor, QNFO.JPC.003), Paper 2 (finite-adele numeracy, QNFO.RES.024), Paper 3 (completeness senses, QNFO.RES.025); this paper is the fourth tier.
1.3 The framing (user directive, verbatim status): isomorphism of mathematical structure; no particle ontology; labels statistical.
1.4 Prior art scoped (F4): the primon-gas canon (Julia 1990; Spector 1990; Bakas–Bowick 1991; Hartnoll–Yang 2025) carries the per-place identifications; RES.020 v1.3.0 publishes them within the corpus (R1/R2/R3). The delta is stated precisely and executably (artifacts/external-search/f4-differential-primon-gas-audit.py).

## 2. The lattice dichotomy (T1)

2.1 Global identities: Σ_{n squarefree} n^{−s} = ζ(s)/ζ(2s); Σ_n n^{−s} = ζ(s) — the Euler factors as mode partition functions (occupation 0/1 vs unbounded). Verification: verify_stats.py F1a/F1b/F1c.
2.2 Golden occupations: ⟨n⟩_F = 1/(e^{β(ε−μ)}+1), ⟨n⟩_B = 1/(e^{β(ε−μ)}−1), recovered from the canonical derivative at arbitrary (β, μ, p). Verification: F1d (Richardson-extrapolated finite differences).
2.3 The per-place identifications at z = 1/p, β_p = ln p: cited from RES.020 (R1/R2), with its 37-entry verification run and its one FAIL entry (born_degeneracy) flagged, never inherited.
2.4 Maximum entropy: the golden distributions are the unique maximum-entropy solutions under their constraints (first-order exponential-family condition + strict concavity). Verification: verify_maxent.py (S9).
2.5 The direction-symmetry guard (Q4 inversion): the squarefree↔Fermi assignment is falsifiable, not symmetric (S1).

## 3. The rate: γ = 1/N (T2)

3.1 The degeneracy-cancellation mechanism: one unit of total activity over N indistinguishable alternatives → mixing operator T = Id − (1/N)(Id − P̄), non-uniform eigenvalue 1 − 1/N → per-distinction rate γ = 1/N.
3.2 Seeded Monte Carlo of the one-distinction chain (initial-state autocorrelation, raw-mean comparison).
3.3 The S2 guard (Q3 seam): heterogeneity breaks the result — per-alternative rates κ_i replace 1/N; the result is a property of the uniform degeneracy, demonstrated not assumed.
3.4 Verification: verify_rate_gamma.py (F2, 15/15).

## 4. The symplectic tier (T3)

4.1 Fisher geometry on the simplex: g = δ/p_i + 1/p_N (the negative of the entropy Hessian; sign-convention note — the seed note's stated "g = ∂²S" carries a sign slip, the metric it uses is the correct positive one).
4.2 The skew generator L = (shift − shift⁻¹)/2: skew w.r.t. g; ω = gL antisymmetric; Fourier eigenvalues ±i sin(2πk/N).
4.3 Finite-N honesty: J² = −sin²(2πk/N) — NOT −1; the complex structure is the sign-normalized generator (discrete Hilbert transform), H² = −1 on mean-zero modes exactly at every N.
4.4 The Fermi/Bose contrast: the symmetric (diffusive) generator has real cos² eigenvalues ≥ 0 — no complex structure without exclusion.
4.5 Large-N honesty: at fixed θ, J²(θ) = −sin²θ, bounded away from −1 — only the sign-normalized structure converges.
4.6 Verification: verify_symplectic.py (F3, 34/34).

## 5. Composite statistics and Möbius parity (F5 — dictionary)

5.1 The composite rule (even/odd fermion count → boson/fermion) as Möbius parity μ(n) = (−1)^{#prime factors} of the squarefree lattice.
5.2 The three-leg falsifier: canonical parity table (Cooper pair, exciton, pion, baryon, He-4, He-3, electron, vacuum); the μ = 0 sector as the exclusion-forbidden sector; the Dirichlet pair 1/ζ(s) = Σ μ(n)/nˢ vs ζ(s).
5.3 Labeled an IDENTIFICATION (dictionary), not a derivation (Q9 discipline).

## 6. Intermediate statistics: the anyon program (F6 — predictive card)

6.1 The bounded-occupancy interpolation: Σ_{v_p ≤ m ∀p} n^{−s} = ζ(s)/ζ((m+1)s); m = 1 recovers Fermi, m → ∞ recovers Bose. Verification: verify_parastats.py (16/16).
6.2 The observable targets: F6a abelian anyons (θ = π/m, Laughlin, ν = 1/m); F6b non-abelian (Ising/Majorana — MZMs, σ² = 1 braiding, 4π-Josephson; Fibonacci ν = 12/5); F6c parastatistics beyond 2D (Wang–Hazzard 2308.05203, 1D/2D constructed models).
6.3 The dimensionality bridge: d ≥ 3 → S_N → ±1; d = 2 → B_N → anyons; BKT quasi-condensation.
6.4 The open correspondence: occupancy bound ↔ braid phase — stated not verified; the falsifier F6.

## 7. Crosswalk / translations (CROSSWALK-TRANSLATION-1)

7.1 The term table (number theory ↔ quantum statistics ↔ stochastic thermodynamics ↔ information theory ↔ QEC engineering), incl. the composite-statistics row.
7.2 The adjacent-domain bridges: ADL.001 (adelic Shannon — β_p = ln p); INM (signal-worker ontology and its composite-boson failure); UMP (RSB ultrametricity as the occupation-count analog); SLB (the statistics lineage: tyranny → spin-statistics → exchange phase); JPC (the γ input closure).

## 8. Practitioner section

8.1 The regime classifier: multiplicity structure → statistics → per-distinction cost (closes JPC.003's assumed rate).
8.2 The audit: product-formula checksum for occupation counting in classical simulators.
8.3 The control reading: statistics = occupation regime → manipulating statistics = engineering the multiplicity bound; the correspondence to braiding/filling/MZM control surfaces as the F6 target.

## 9. Premise depth and boundaries

9.1 L0 primitives: integers + unique factorization; the product formula (imported theorem); the maximum-entropy principle (imported postulate); Euler's distinct-part identity (named).
9.2 L1 derived: the squarefree/unrestricted dichotomy; the degeneracy cancellation; the large-N limit calculus.
9.3 L2 named imports: RES.021 (finite-distinction machinery); JPC.003 (Landauer floor); RES.024 (finite-adele encoding); RES.025 (completeness senses); RES.020 (R1/R2/R3 — the published per-place identifications); the composite-statistics rule (standard QM).
9.4 The RES.009 boundary, verbatim: the spin-statistics CONNECTION requires Lorentz and locality input this paper does not supply; the decisive test already run there (abelian-pair postulate ASSUMED; involutivity a target-category condition) is what this paper's route does not claim to outrun.
9.5 Where premises end: the mapping hypothesis is a named input tested by reproduction (F1–F3), earning predictive status only via the F6 program.

## 10. Verification appendix (COMPUTATIONAL-VERIFICATION-1)

10.1 The six scripts and the 163-check fleet: verify_stats.py 65; verify_product_formula.py 17; verify_parastats.py 16; verify_rate_gamma.py 15; verify_symplectic.py 34; verify_maxent.py 16.
10.2 Reproducibility statement: stdlib-only, seeded (20260827), runtimes ~seconds; run logs + results JSONs deposited with the paper.
10.3 The F4 scoping artifact (artifacts/external-search/f4-differential-primon-gas-audit.py) and the evidence files (external-verify-2026-08-27.txt).

## 11. Falsifier register (locked with the claim)

F1 (golden occupations), F2 (γ ∝ 1/N + mechanism guard), F3 (symplectic Fermi-only + finite-N honesty), F4 (executable prior-art delta), F5 (three-leg parity), F6 (anyon contact). Each maps to its script (§2–§6) and its verification status (all green, 2026-08-27).

## References (skeleton — full citation-audited bib at P5)

Corpus: RES.020 10.5281/zenodo.22035210; RES.021 10.5281/zenodo.22046458; JPC.003 10.5281/zenodo.22117282; RES.024 10.5281/zenodo.22114495; RES.025 10.5281/zenodo.22109455; RES.009 10.5281/zenodo.21964598; RES.010 10.5281/zenodo.21964104; RES.011 10.5281/zenodo.21962450; pattern-particle-unification 10.5281/zenodo.22024856; tyranny-of-the-plus-minus-one (concept 10.5281/zenodo.21939595); from-distinction-to-dissipation 10.5281/zenodo.21940822; zbw-majorana-tqc-p5-adelic-qec 10.5281/zenodo.21336099; zbw-p5-capstone 10.5281/zenodo.21609223; adelic-shannon-theory 10.5281/zenodo.22024240; operationalizing-generalized-symmetries 10.5281/zenodo.18199397; continuum-trilogy-02-padic-spin 10.5281/zenodo.21672990; consilience-physics-numtheory 10.5281/zenodo.21590155. External: Julia 1990; Spector 1990; Bakas–Bowick 1991; Leinaas–Myrheim 1977; Wilczek 1982; Kitaev 2003/2006; Nayak et al. 2008; DHR 1971; Pauli 1940; Duck–Sudarshan 1998; arXiv 2502.02661, 2602.11927, 2505.17361, 1106.1166, 0903.2664, 2306.05919, 0708.2567, 2308.05203, hep-th/0308095, 1201.6541.

## Publication gates (at P5)

Title-visible bridge (TERMINOLOGY-SILO-LESSONS-1): the title names both domains. Plain scholarly prose (PUBLICATION-PROSE-GATE-1 / ANTI-TELEGRAPH-1): no internal shorthand, no brand language. Rendering gates (CURRENCY-DOLLAR-ESCAPE-1, FRONTMATTER-DUPLICATION-1, FFFD-RAW-FALSE-POSITIVE-1, LICENSE/README-CLOBBER-1). Deposit integrity (PUBLICATION-SOURCE-COMPLETENESS-1, REFERENCE-TITLE-FIDELITY-1, METADATA-RELATIONS-ASSERT-1, DEPOSIT-LAYOUT-VERIFY-1, POST-PUBLISH-FRONTMATTER-ASSERT-1).
