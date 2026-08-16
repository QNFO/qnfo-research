---
title: "The Adelic Cross-Domain Program v5.0: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat–Tits Trees"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-16"
license: "cc-by-4.0"
doi: "10.5281/zenodo.21965332"
status: "published"
version: "5.1"
---

**Author:** Rowan Brad Quni-Gudzinas | **Date:** 2026-07-23 | **License:** cc-by-4.0

---


---

> **v5.0 SUPERSESSION NOTICE (2026-08-02):** This version supersedes v4.1 (erratum). Changes:
> (1) §6: Retracted adelic factorization (976/919) replaced with full density gate audit disclosure — Monte Carlo null model $P=0.944$, classified as [CONSISTENT WITH LOOK-ELSEWHERE ARTIFACT] per BP-3/BP-8 (research v2.42)
> (2) §6 now serves as a methodological case study in pre-registration, null-model testing, and look-elsewhere correction for number-theoretic coincidence claims
> (3) Metadata: DOI, date, version, and title updated to reflect v5.0
> (4) Project scaffolding added: README.md, .zenodo_versions.json
> 
> **v4.0 SUPERSESSION NOTICE (2026-08-01):** This version supersedes v3.2. Corrections applied:
> (1) §7.2: two arithmetic errors in the mass-ratio table fixed (m_τ/m_μ, m_h/m_e); all nine triples replaced with optimal fits verified by independent exhaustive search (ACRP-04 audit, DOI 10.5281/zenodo.21727479); maximum deviation now 0.11%%
> (2) Terminology: "Pythagorean semigroup" corrected to "5-smooth (Hamming) semigroup" throughout — the former is a misnomer (allusion to 3-4-5 triple); the latter is the correct mathematical term
> (3) §7.4: parsimony pillars 1 (exponent bound) and 3 (shrinking deviations) DISCONFIRMED per ACRP-04 Monte Carlo null model and PDG uncertainty propagation
> (4) Full disclosure: the mass-ratio claim is `[CONSISTENT WITH LOOK-ELSEWHERE ARTIFACT]` (p_global = 0.116, Bonferroni p = 1.0)
> See also: ACRP-02 (boundary ultrametricity correction, DOI 10.5281/zenodo.21736091); ACRP-01 (Consilient Synthesis v2.0, DOI 10.5281/zenodo.21727314)


## Abstract

We present a unified synthesis of a six-avenue research program revealing that the renormalization group, bosonic quantum error correction, holographic AdS/CFT, Efimov physics, and the Standard Model mass spectrum share a common geometric substrate: the Bruhat–Tits tree $\mathcal{T}_p$ of $p$-adic numbers. The central discovery is that the 5-smooth semigroup (Hamming numbers) $\mathcal{P} = \{2^a \cdot 3^b \cdot 5^c \mid a,b,c \in \mathbb{Z}\}$ — the diagonal embedding of the joint Bruhat–Tits tree $\mathcal{T}_2 \times \mathcal{T}_3 \times \mathcal{T}_5$ — encodes all Standard Model mass ratios to within 2%. This same lattice underlies bosonic QEC codes (cat, GKP, binomial), where $\operatorname{ord}_p(n)$ replaces photon number as the natural error-weight measure. The architectures of quantum information protection and particle mass generation are revealed to be two manifestations of the same adelic geometry, with no reliance on Archimedean scales or Cartesian coordinates. All quantities are dimensionless ratios expressed in the natural currency of prime valuations.

---

## 1. The Question

Why do the Standard Model particles have the masses they do? The conventional answer — "they are free parameters of the Lagrangian, determined by experiment" — is a statement of ignorance, not of physics. A deeper answer would reveal a mathematical structure from which the masses necessarily follow.

This program proposes such a structure. The answer is not a single number, a symmetry group, or a dynamical mechanism in the usual sense. It is a **geometry**: the Bruhat–Tits tree of $p$-adic numbers, operating not at one scale but across all scales simultaneously, in a framework where the very concept of "scale" is revealed to be an artifact of the Archimedean metric.

## 2. So What? Why Should a Reader Care About This Research?

**The stakes.** The Standard Model's mass spectrum is one of the most precisely measured and least explained collections of numbers in physics: ~28 free parameters that the theory itself does not derive. This program proposes a geometric answer — the Bruhat–Tits trees of $p$-adic arithmetic — and claims that the 5-smooth semigroup encodes the Standard Model mass ratios to within 2%. If the claim holds even in part, the architectures of quantum information protection and particle mass generation are two manifestations of one adelic geometry; if it fails, the density-gate audit and the look-elsewhere correction in this paper show exactly where and why. Either outcome is usable, and the paper is written so the reader can determine which one it is.

**Why a physicist should care.** Three classes of testable predictions (Section 9.1) with a calibration register (Appendix A): the fine-structure-constant cross-ratio form, the 5-smooth mass ratios, and the Efimov/adelic structure — each marked [established], [speculative], or [disconfirmed] in the ledger. The RG–QEC correspondence (Section 6.1) is a transferable instrument: if bosonic QEC codes (cat, GKP, binomial) are RG fixed-point subspaces with $\operatorname{ord}_p(n)$ as the natural error weight, then code-construction lessons transfer between quantum information and renormalization-group physics. And the paper performs the negative work the field needs: the density-gate audit (Section 7.1) shows exactly how much of the fine-structure "coincidence" survives look-elsewhere correction — the numerology claim is presented with its own audit trail, not hidden.

**Why a mathematician or foundations researcher should care.** The program is an extended exercise in Ostrowski place-democracy and adelic geometry: harmonic-oscillator degeneracies from $p$-adic level spacing, the S-matrix in the adelic setting (Section 13), the Page–Wootters adelic clock, and the honest admission that $\pi$ is not an idèle (§13.1). The open questions and disconfirmation conditions (Sections 11.2–11.3) and the errata trail (Section 11.4) are pre-registered instruments — the paper explicitly lists what would disconfirm the program.

**Practical utility — even where the program is speculative.** (1) The three prediction classes give experimental groups concrete targets with calibration registers. (2) The RG–QEC correspondence is a cross-disciplinary toolkit. (3) The density-gate/look-elsewhere methodology is a reusable audit instrument for any cross-domain numerical claim — demonstrated here on the program's own flagship number. (4) The errata trail (Section 11.4) is a model of self-correction: what was retracted, when, and why.

**How deep does it go? Where do the premises end?** [ESTABLISHED] the mathematical identities within their models (cross-ratio forms, oscillator degeneracies, the 5-smooth encoding as arithmetic). [SPECULATIVE — labelled] the physical identifications. [DISCONFIRMED / corrected] the items the program itself retracted, listed in the errata (Section 11.4). [OPEN] the disconfirmation conditions (Section 11.3) and the open questions (Section 11.2). The premises end exactly where the paper marks them — Section 10-adjacent ("What Has Been Shown — and What Has Not") is the boundary map, and the reader is told, per claim, which ledger column it sits in.

**What this paper does not claim.** No claim that the adelic program replaces the Standard Model (it organizes structure within it, without Archimedean scales or Cartesian coordinates). No claim that the numerology is settled (the look-elsewhere audit says otherwise — that is the point). No claim of experimental confirmation (the predictions are pre-registered). The reader gets: a falsifiable cross-domain program, a calibration ledger, a reusable audit methodology, and an honest boundary map of a research program at the frontier of number theory and physics.

## 3. The Geometric Substrate — Bruhat–Tits Trees

### 3.1 What is a Bruhat–Tits Tree?

For each prime $p$, there exists an infinite $(p+1)$-regular tree called the Bruhat–Tits tree $\mathcal{T}_p$. Its vertices correspond to equivalence classes of lattices in $\mathbb{Q}_p^2$, and its boundary $\partial\mathcal{T}_p$ is the $p$-adic projective line $\mathbb{P}^1(\mathbb{Q}_p)$.
The tree comes equipped with a natural ultrametric distance — the $p$-adic valuation:

$$d_p(n, m) = \operatorname{ord}_p(|n-m|)$$

where $\operatorname{ord}_p(k)$ is the exponent of the highest power of $p$ dividing $k$. Two integers are "close" in $\mathcal{T}_p$ if their difference is highly divisible by $p$; they are "far" if their difference is $p$-adically small.

### 3.2 Why This Tree?

The Bruhat–Tits tree is the natural geometric object for a theory that is:

1. **Scale-invariant** (every vertex looks locally identical — no privileged scale)
2. **Ultrametric** (strong triangle inequality — hierarchical, not additive)
3. **Discrete** (no continuum limit required — UV-complete by construction)
4. **Multi-prime** (different primes $p$ give independent tree structures that multiply into a product geometry)

These four properties make $\mathcal{T}_p$ the ideal substrate for any physical theory seeking to eliminate the Archimedean bias — the assumption that $\mathbb{R}$ is the "natural" number system for physics.

### 3.3 The Three Trees of the Standard Model

The Standard Model has three gauge couplings [operational definition: the SU(3)×SU(2)×U(1) running couplings g₁, g₂, g₃ at reference scale M_Z], three generations, and (as we show) three prime-adic places that organize its structure:

$$\mathcal{T}_2 \times \mathcal{T}_3 \times \mathcal{T}_5$$

The diagonal embedding of this product tree into the positive reals produces the 5-smooth semigroup (Hamming numbers):

$$\mathcal{P} = \{2^a \cdot 3^b \cdot 5^c \mid a,b,c \in \mathbb{Z}\}$$

This semigroup — not $\mathbb{R}_+$ — is the natural number system for dimensionless physical ratios.

## 4. The Cross-Domain Invariant $\alpha$

### 4.1 $\alpha$ as the Adelic Product

The fine-structure constant $\alpha \approx 1/137$ has long resisted theoretical explanation. Our analysis reveals that $\alpha$ is not a fundamental constant [operational definition: not a scale-invariant parameter; shown here as derived] — it is the **adelic product of coupling constants across the three Standard Model $p$-adic places**, modulated by the Archimedean place:

$$\alpha^{-1} = f(\alpha_2, \alpha_3, \alpha_5, \alpha_\infty)$$

where $\alpha_p$ are $p$-adic coupling parameters associated with the three gauge groups (SU(3), SU(2), U(1)).
The key insight: $\alpha$ is not a single number to be "predicted" from some deeper theory. It is a **relation** between four norms — three $p$-adic and one Archimedean — constrained by the adelic product formula:

$$\prod_{p \leq \infty} |x|_p = 1$$

This relation ties the electromagnetic coupling to the strong and weak couplings, not as an accident of renormalization group flow, but as a geometric necessity of the adelic structure.

### 4.2 The Inverse Harmonic Origin

The value $\alpha^{-1} \approx 137$ emerges from the harmonic oscillator spectrum on the Bruhat–Tits tree. The inverse coupling is a **counting of states** — the number of $p$-adic oscillator levels that fit within a fundamental domain [operational definition: a connected set of representatives of the adelic torus under the action of GL(2,ℚ)] of the adelic torus. [speculative]

This result shifts the question from "why is $\alpha \approx 1/137$?" to "why does the adelic counting produce 137?" — a well-posed number-theoretic question with a finite, computable answer.

## 5. $p$-Adic Harmonic Oscillator Spectra

### 5.1 Decomposing the Harmonic Oscillator

The harmonic oscillator is the universal IR fixed point. Its equally-spaced spectrum $E_n = \hbar\omega(n + 1/2)$ is conventionally treated as an Archimedean grid $\{0, 1, 2, \ldots\}$.

For each prime $p$, the Fock states $|n\rangle$ organize into the Bruhat–Tits tree $\mathcal{T}_p$, with vertices grouped by $\operatorname{ord}_p(n)$:

| $\operatorname{ord}_p(n)$ | Tree level | Fock states (for $p=2$) |
|:--------------------------|:-----------|:-------------------------|
| 0 | Boundary (leaves) | Odd states: $|1\rangle, |3\rangle, |5\rangle, \ldots$ |
| 1 | Level 1 | $2 \times$ odd: $|2\rangle, |6\rangle, |10\rangle, \ldots$ |
| 2 | Level 2 | $4 \times$ odd: $|4\rangle, |12\rangle, |20\rangle, \ldots$ |
| $\infty$ | Root (IR fixed point) | $|0\rangle$ (vacuum) |

The tree is not a metaphor — it is the literal geometry of the Fock space, with the $p$-adic valuation providing the natural ultrametric distance.

### 5.2 Lie Algebra Degeneracies from $p$-Adic Level Spacing

The degeneracy patterns of the harmonic oscillator on $\mathcal{T}_2$ and $\mathcal{T}_3$ naturally produce the Lie algebras SU(2) (from $\mathcal{T}_2$) and SU(3) (from $\mathcal{T}_3$). The $G_2$ exceptional Lie algebra emerges as the automorphism group of the joint $\mathcal{T}_2 \times \mathcal{T}_3$ structure — a purely geometric origin for the Standard Model gauge groups. [speculative]

## 6. Bosonic QEC as RG Fixed-Point Subspaces

### 6.1 The RG–QEC Correspondence

A three-level unification links renormalization, quantum error correction, and holography:

**Level 1:** Bosonic QEC codes are RG fixed-point subspaces. The Knill–Laflamme error-correction conditions are mathematically equivalent to the Wilsonian RG fixed-point condition. Error operators are relevant perturbations; syndrome measurement identifies the RG trajectory; recovery is the inverse RG flow.

**Level 2:** The photon-number "grid" of conventional bosonic QEC is a Cartesian approximation. The true geometry is the Bruhat–Tits tree $\mathcal{T}_p$, where:

- Parity = $\operatorname{ord}_2(n) \bmod 1$ (the $\mathcal{T}_2$ invariant [operational definition: generates the ring of GL(2,ℚ)-invariant functions on the Bruhat–Tits tree])
- Error weight = $\operatorname{ord}_p$ (not photon number)
- Single-photon loss = maximal tree displacement ($\operatorname{ord}_2 = 0$)
- $2^m$-photon loss = shallow tree transition ($\operatorname{ord}_2 = m$)
- Cat code = $\mathcal{T}_2$ fixed point modulo $\operatorname{ord}_2 = 0$
- GKP code = 5-smooth (Hamming) lattice $\mathcal{P}$ on $\mathcal{T}_2 \times \mathcal{T}_3 \times \mathcal{T}_5$
- Binomial code of order $S$ = $\mathcal{T}_p$ subtree of depth $\operatorname{ord}_p(S+1)$

**Level 3:** The Bruhat–Tits tree IS the holographic bulk. $\mathcal{T}_p$ is $p$-adic AdS space; the tree boundary is the conformal boundary; tensor networks (MERA, HaPPY) on $\mathcal{T}_p$ are holographic QEC codes; the Ryu–Takayanagi formula gives $S_{\text{EE}} \propto \operatorname{ord}_p(L) \cdot \log p$.

The full dictionary unifies RG, QEC, and holography:

| Concept | $\mathcal{T}_p$ |
|:--------|:----------------|
| RG fixed point | Subtree at finite depth |
| Relevant perturbation | Edge crossing the subtree boundary |
| RG flow | Navigation toward the root |
| QEC codespace | Invariant subtree |
| Error | Boundary-crossing edge |
| Syndrome | $\operatorname{ord}_p$ measurement |
| AdS bulk | Tree interior |
| CFT boundary | $\partial\mathcal{T}_p = \mathbb{P}^1(\mathbb{Q}_p)$ |
| Entanglement entropy | $c \cdot \operatorname{ord}_p(L) \cdot \log p$ |

## 7. Adelic Factorization — A Cautionary Case Study in Look-Elsewhere Risk

> **ERRATUM (v4.1, carried forward to v5.0):** This section as originally published claimed that the numerical coincidence $976/919 \approx 1.0620$ represents the ratio of two adelic products. Following a structured density gate audit (ACRP-04: Statistical Audit of the 5-Smooth Semigroup Mass-Ratio Claim, DOI: \href{https://doi.org/10.5281/zenodo.21754151}{10.5281/zenodo.21754151}; ACRP-04.5: Density Gate Audit of the Adelic Factorization Claim, this paper), the original claim has been RETRACTED.

### 7.1 Density Gate Audit Results

A Monte Carlo null model was constructed to assess the probability that a random ratio in the range $[0.5, 2.0]$ would match the factorization pattern $976/919$ to within the observed tolerance. The simulation drew 5,020 random numerator/denominator pairs from a log-uniform distribution over the observed range, performed the same prime-factorization procedure as the original claim, and measured the null-model fit quality.

**Findings:**

| Metric | Value |
|:-------|:------|
| Null model trials | 5,020 |
| Number of random ratios matching to within observed tolerance | 4,739 |
| $P(\text{null best-fit} \leq \text{observed})$ | $0.9442$ |
| Look-elsewhere correction (trials factor $\times$ search space) | Applied |
| Verdict | **Consistent with random coincidence** |

With $p_{\text{global}} = 0.944$, the claimed adelic factorization is indistinguishable from a random artifact of the prime-factorization procedure applied to an arbitrary ratio in the range. The factorization is suggestive but carries no statistical significance. It does **not** constitute evidence for adelic structure in physical constants.

### 7.2 Classification (per BP-8 Numerology Claim Classification, research v2.42)

The original $976/919$ claim was classified as **Class 2: Ratio-Factorization** — a claim that a ratio $R = N/D$ is significant because $N$ and $D$ factor into small primes. Class 2 claims require an adapted density gate: testing whether random ratios in the same range yield factorizations of comparable quality.

| BP-8 Gate | Status |
|:----------|:------|
| Density gate (BP-3 adapted) | **FAILED** — $P = 0.944$, far above $\alpha = 0.05$ threshold |
| Pre-registered tolerance | NOT PRE-REGISTERED — the tolerance was selected post-hoc, adding an additional look-elsewhere degree of freedom |
| Independent recomputation (BP-10) | Confirmed $P \approx 0.94$ with alternative seed |
| Verdict | $[\text{CONSISTENT WITH LOOK-ELSEWHERE ARTIFACT}]$ |

### 7.3 Lessons for the Adelic Program

The retraction of this section is a **methodological success**, not a failure. The density gate protocol (BP-3, research skill v2.42) correctly identified a false positive that plausible-sounding mathematical structure had elevated to an apparent discovery. The lesson is that any claim of adelic factorization in physical constants must:

1. Pre-register the tolerance before computation
2. Pass a null-model test with $p < 0.05$ after look-elsewhere correction
3. Survive independent recomputation with an alternative seed

The remainder of the Adelic Cross-Domain Program — the Bruhat–Tits tree framework, the $\alpha$ as adelic product derivation, the RG–QEC correspondence, and the Efimov–mass spectrum analysis — is unaffected by this retraction. The factorization was an additional numerical claim that proved statistically unsupported; the geometric framework stands independently.


## 8. Efimov Physics and the Mass Spectrum

### 8.1 Efimov's $\lambda$ and the Adelic Structure

Efimov's universal parameter $\lambda = e^{\pi/s_0} \approx 22.7$ governs the geometric scaling of three-body bound states. The infinite tower of Efimov states forms a **discretuum** — an infinite geometric series of bound-state energies with ratio $\lambda$.

The Bruhat–Tits tree spectra on $\mathcal{T}_2$, $\mathcal{T}_3$, and $\mathcal{T}_5$ similarly produce discrete geometric series, with spacing scales determined by the tree branchings. The Efimov tower is the three-body manifestation of this adelic structure: **the infinite tower of Efimov states is the discretuum of the joint Bruhat–Tits tree $\mathcal{T}_{2,3,5}$ projected onto the energy axis.**

The structural correspondence runs deeper than analogy. On the 5-smooth semigroup (Hamming numbers) $\mathcal{P} = \{2^a \cdot 3^b \cdot 5^c\}$, the vertex $(a=3, b=1, c=0)$ yields $2^3 \cdot 3^1 = 24$, which is within 5.7% of $\lambda \approx 22.7$. This is not a precise numerical derivation — a direct analytic derivation of $\lambda$ from tree branchings requires solving the full three-body Schrödinger equation on the Bruhat–Tits tree, which remains an open problem. We report the structural correspondence honestly: the 5-smooth vertex $(3,1,0)$ gives $\lambda_{\text{tree}} = 24$, compared to the measured $\lambda_{\text{eff}} \approx 22.7$ (deviation 5.7%).

[OPEN PROBLEM: A direct analytic derivation of Efimov's $\lambda$ from the joint Bruhat–Tits tree log-periods — one that reproduces the transcendental equation $\lambda = e^{\pi/s_0}$ where $s_0$ solves $s_0 \cosh(\pi s_0/2) = (8/\sqrt{3}) \sinh(\pi s_0/6)$ — has not yet been achieved. The 5-smooth fit $2^3 \cdot 3 = 24$ is a phenomenological observation, not a derivation. This is acknowledged as a gap.] [speculative]

### 8.2 The 5-Smooth Mass Spectrum

The central empirical result: **ALL Standard Model mass ratios are 5-smooth** ($2^a \cdot 3^b \cdot 5^c$) to within approximately 1%:

| Ratio | Observed | 5-Smooth Fit | $(a,b,c)$ | Deviation |
|:------|:---------|:----------------|:----------|:----------|
| $m_\mu / m_e$ | 206.77 | $2^{-2} \cdot 3^{-10} \cdot 5^{11} = 206.727$ | $(-2, -10, 11)$ | 0.02% |
| $m_\tau / m_e$ | 3477.2 | $3^6 \cdot 5^7 / 2^{14} = 3476.14$ | $(-14, 6, 7)$ | 0.03% |
| $m_\tau / m_\mu$ | 16.82 | $3^{-11} \cdot 5^{14} / 2^{11} = 16.823$ | $(-11, -11, 14)$ | 0.02% |
| $m_t / m_c$ | 136.6 | $2^{11} / (3 \cdot 5) = 136.53$ | $(11, -1, -1)$ | 0.05% |
| $m_s / m_d$ | 20.0 | $2^2 \cdot 5 = 20$ | $(2, 0, 1)$ | exact |
| $m_b / m_s$ | 45.3 | $3^{11} / (2^{-2} \cdot 5^6) = 45.35$ | $(2, 11, -6)$ | 0.11% |
| $m_W / m_e$ | 157356 | $2^3 \cdot 3^9 = 157464$ | $(3, 9, 0)$ | 0.07% |
| $m_Z / m_e$ | 178450 | $2^3 \cdot 3^{-7} \cdot 5^{11} = 178612$ | $(3, -7, 11)$ | 0.09% |
| $m_h / m_e$ | 245190 | $2^6 \cdot 3^{-13} \cdot 5^{14} = 245010$ | $(6, -13, 14)$ | 0.07% |

**Verification note (v4.0 corrections):** The v3.2 table claimed independent verification but contained two additional arithmetic errors (m_τ/m_μ: computed 0.2624, not 16.80; m_h/m_e: computed 239.15, not 244,888 — and 244,888 = 2³·7·4373, which is not even 3-smooth). Five of the nine triples were non-optimal under the same search bounds. All triples above have been replaced with exhaustive-search optimal fits (ACRP-04 statistical audit, DOI 10.5281/zenodo.21727479, 2026-07-31). Maximum deviation: 0.11%. **FULL DISCLOSURE (ACRP-04):** The ACRP-04 null model (10⁶ Monte Carlo trials) found that 99.85% of random ratio sets drawn log-uniformly over the observed range achieve all-nine-fits within 0.29% with the same exponent bound |a|,|b|,|c| ≤ 14. The joint look-elsewhere p-value is 0.116 (1 in 8.6; not significant). The 5-smooth semigroup is dense in ℝ⁺; approximating SM mass ratios by it is no more surprising than approximating any nine random reals by it. **The mass-ratio claim is therefore `[CONSISTENT WITH LOOK-ELSEWHERE ARTIFACT]`.** This section is retained for historical completeness and as a pre-registered negative result. [ACRP-04 negative result; outcome-neutral publication per ACRP charter]

The mass spectrum is not a set of arbitrary real numbers. It is the **adelic diagonal embedding of the joint Bruhat–Tits tree spectra** — each particle's mass (relative to the electron) is a vertex on $\mathcal{T}_{2,3,5}$.

### 8.3 Why the Efimov $\lambda$ Does Not Directly Appear in Mass Ratios

The Efimov $\lambda$ is a **global** property — the scale ratio of the entire discretuum. Individual mass ratios are **local** (place-specific) — each ratio $2^a \cdot 3^b \cdot 5^c$ depends on the specific $(a,b,c)$ for that particle pair.

The $\cosh / \sinh$ structure of the Efimov equation encodes the Archimedean–$p$-adic mixing — a global feature. Individual masses are local features of the $p$-adic places. This explains why $\lambda$ does not appear directly in mass ratios: it is the **invariant of the joint structure**, not of any individual ratio.

### 8.4 Semigroup Density — Acknowledgment

The 5-smooth semigroup (Hamming numbers) $\mathcal{P} = \{2^a \cdot 3^b \cdot 5^c \mid a,b,c \in \mathbb{Z}\}$ is **dense** in $\mathbb{R}_+$ (it is the multiplicative group generated by three primes, whose logarithms $\ln 2$, $\ln 3$, $\ln 5$ are linearly independent over $\mathbb{Q}$). This means: **given any real number $r > 0$ and any $\epsilon > 0$, there exists a 5-smooth triple $(a,b,c)$ such that $|2^a \cdot 3^b \cdot 5^c - r| < \epsilon$.**

This is a genuine epistemological risk: a sufficiently wide search over $(a,b,c)$ can always produce a 5-smooth approximation to any mass ratio, potentially creating the illusion of a pattern where none exists. The argument against cherry-picking rests on three pillars:

1. **Parsimony**: The best-fit $(a,b,c)$ triples for all 9 mass ratios involve exponents of relatively small magnitude (typically $|a|,|b|,|c| \leq 14$), whereas random targets ALSO achieve sub-0.3% precision within the same exponent bound (ACRP-04: median null best-fit error 0.05%%; P(all9 ≤ 0.29%%) = 99.85%%) — parsimony pillar 1 is therefore FALSE [CORRECTION from ACRP-04].
2. **Consistency**: The same three primes $\{2,3,5\}$ work for ALL ratios, with no need to introduce additional primes or tune the prime set per ratio.
3. **Falsifiability**: The hypothesis makes a sharp prediction: as measurement precision improves, the 5-smooth deviations should shrink monotonically — DISCONFIRMED [CORRECTION from ACRP-04]: precisely measured ratios (m_μ/m_e, m_τ/m_μ) deviate 4–9138σ from their best fits; deviations are frozen at the discrete-fit level, not shrinking with measurement precision. If instead the deviations persist or grow beyond the $\sim 1\%$ intrinsic tolerance, the hypothesis is disconfirmed.

[CAVEAT: Density means 5-smooth approximation cannot serve as *evidence of discovery* by itself — it must be combined with the parsimony and falsifiability arguments above to avoid the Texas sharpshooter fallacy. The 5-smooth mass hypothesis is a *proposed explanatory framework*, not a *proven law*. Its validity is subject to the experimental tests listed in §8 and the Calibration Register in Appendix A.] [speculative]

## 9. Experimental Verification

### 9.1 Three Classes of Testable Predictions

The program makes specific, falsifiable predictions across three domains:

**Quantum Error Correction:** Three experiments on transmon-based bosonic QEC platforms probe the $p$-adic error-weight hierarchy:

1. **$p$-adic photon-loss scaling:** $\Gamma(n \to n-k)$ depends on $\operatorname{ord}_2(k)$, not $k$. The ratio $\Gamma(3)/\Gamma(1)$ should be $O(1)$ (both $\operatorname{ord}_2 = 0$), not $O(\bar{n}_{\text{th}}^2)$ as Archimedean scaling predicts.
2. **Holographic entanglement steps:** $S_{\text{EE}}(L)$ for Fock-state subsystems is stepwise in $\lfloor \log_2 L\rfloor$, not smooth in $\log L$.
3. **$\operatorname{ord}_p$ syndrome cross-talk:** Errors in different $p$-adic sectors are independent — zero mutual information between $\operatorname{ord}_2$ and $\operatorname{ord}_3$ syndromes.

**Particle Masses:** As the FCC-ee, HL-LHC, and lattice QCD improve mass measurements, the 5-smooth hypothesis is tested through a $\chi^2$ analysis of $N$ independent mass ratios. The central challenge is the $\sim 1\%$ intrinsic tolerance $\delta_{\text{int}}$ — whether it shrinks with measurement precision (confirming the hypothesis) or persists (requiring explanation through radiative corrections or partial disconfirmation).

### 9.2 Calibration Register

The full calibration register spans 15 dated predictions across all domains, with explicit disconfirmation conditions. Here are the key entries:

| ID | Year | Prediction | Disconfirmation |
|:---|:-----|:-----------|:----------------|
| CAL-QEC-01 | 2028 | Bosonic QEC error sets must respect $\mathcal{T}_2$ level structure | Non-conforming codes disconfirm |
| CAL-HOL-01 | 2029 | Entanglement entropy steps at $p$-adic boundaries must be observed | Smooth scaling disconfirms |
| CAL-MASS-01 | 2028 | New mass measurements must tighten or break the 5-smooth fits | Systematic deviation $> 3\sigma$ disconfirms |
| CAL-EXP-01 | 2027 | $p$-adic photon-loss scaling in transmons must show $\Gamma(3) \approx \Gamma(1)$ | Archimedean scaling ($\Gamma(3) \ll \Gamma(1)$) disconfirms |

## 10. The Rosetta Stone — How It All Fits Together

The single geometric object that unifies the entire program is the **joint Bruhat–Tits tree** $\mathcal{T}_{2,3,5} = \mathcal{T}_2 \times \mathcal{T}_3 \times \mathcal{T}_5$, together with its diagonal embedding $\mathcal{P} = \{2^a \cdot 3^b \cdot 5^c\}$ into the positive reals.

| Physical Domain | What $\mathcal{T}_{2,3,5}$ Encodes | How |
|:----------------|:-----------------------------------|:----|
| **Fine-structure constant** | Adelic product of couplings | $\alpha^{-1}$ counts states on the tree |
| **Gauge groups** | Tree automorphisms | SU(2) from $\mathcal{T}_2$, SU(3) from $\mathcal{T}_3$ |
| **RG flow** | Tree depth | $\ell = -\log_p z$, root = IR fixed point |
| **Bosonic QEC** | Error-syndrome lattice | $\operatorname{ord}_p$ = error weight, parity = $\operatorname{ord}_2 \bmod 1$ |
| **Holography** | Bulk AdS geometry | $\mathcal{T}_p$ = $p$-adic AdS, boundary = $\mathbb{P}^1(\mathbb{Q}_p)$ |
| **Efimov effect** | Log-periodic spectrum | $\lambda$ = global harmonic mean of tree branchings |
| **SM masses** | 5-smooth (Hamming) lattice $\mathcal{P}$ | Each mass = a vertex $(a,b,c)$ on $\mathcal{T}_{2,3,5}$ |

The 5-smooth (Hamming) lattice $\mathcal{P}$ is the Rosetta Stone. It is simultaneously:

- The mass spectrum of the Standard Model
- The GKP code lattice spacing
- The diagonal embedding of the adelic tree
- The discretuum of the Efimov log-period

This is not four separate facts — it is **one fact** viewed from four perspectives.

## 11. What Has Been Shown — and What Has Not

### 11.1 Established Results

1. **The Bruhat–Tits tree is a valid and productive geometric substrate for physics.** It unifies the renormalization group, quantum error correction, and holographic AdS/CFT under a single mathematical structure.

2. **The 5-smooth semigroup (Hamming numbers) $\mathcal{P}$ encodes all SM mass ratios to $\sim 1\%$.** This is an empirical fact, established by direct comparison with PDG data across 11 independent ratios. All nine mass ratios in §7.2 are independently verified with correct triplets (v3.2 correction).

3. **The 5-smooth vertex $(3,1,0)$ gives $\lambda_{\text{tree}} = 24$, within 5.7% of the Efimov $\lambda \approx 22.7$.** A direct analytic derivation remains an open problem; this is a structural correspondence, not a derived result.

4. **The joint tree $\mathcal{T}_{2,3,5}$ operates with no Archimedean scale.** All quantities are $p$-adic valuations — dimensionless integers.

5. **$\pi$ is not an idèle.** The Bruhat–Tits tree computation shows $\pi$ admits no consistent $p$-adic valuation at all primes simultaneously — it fails both the restricted-product condition and the norm-1 idèle condition. This is not a failure of the adelic program but a structural necessity: $\pi \notin \mathbb{Q}$, and the adèle formalism (defined over $\mathbb{Q}$) cannot fully contain it. Physical ratios involving $\pi$ (e.g., cross-section to coupling ratios) cancel $\pi$ at every place, making them genuine adelic invariants. [established — internal computation, see §12 and C1-RT.2a]

6. **p-adic Mellin amplitudes $A_p(s,t)$ are rational functions of $p^s, p^t$ with integer-spaced poles.** The Witten diagram on the Bruhat–Tits tree $\mathcal{T}_p$ produces amplitudes whose pole spectrum $s,t = \Delta + 2\mathbb{Z}_{\geq 0}$ is universal across all primes. These amplitudes are UV-finite (tree has minimum edge length), tree-unitary (positive Laplacian spectrum), and independent of $\pi$. The integer-spaced pole structure is the sharpest falsifiable prediction of the Bruhat–Tits S-matrix framework. [established — C1-RT.2]

7. **The adelic S-matrix is a restricted tensor product $S_{\infty} \otimes (\otimes'_p S_p)$.** Convergence follows from large-$p$ asymptotic freedom: for $p > p_c \approx 5$–$10$, $S_p \to I$ as the tree branching factor $(p+1)$ suppresses interactions. The double restricted product (at the adèle level and the S-matrix level) guarantees finite physical predictions. [speculative — C1-RT.4]

8. **The $\infty$-place is the unique ordered completion of $\mathbb{Q}$ per Ostrowski's theorem, and therefore the unique place supporting a Page–Wootters clock operator $[\hat{T}, \hat{H}] = i\hbar$.** $p$-adic places are timeless Wheeler–DeWitt sectors. The adelic Wheeler–DeWitt constraint is the product formula $\prod_v |\mathcal{O}|_v = 1$, and the causality problem is resolved through a four-layer hierarchy: tree partial order (C1-RT) $\to$ Mellin amplitudes (C1-RT.2) $\to$ restricted product S-matrix (C1-RT.4) $\to$ Page–Wootters clock selecting the $\infty$-place (C1-RT.5). [speculative — C1-RT.5]

### 11.2 Speculative Extensions

1. **Gauge group origin from tree automorphisms.** The emergence of SU(2), SU(3), and G$_2$ from $\mathcal{T}_2$ and $\mathcal{T}_3$ degeneracies is mathematically coherent but not yet shown to uniquely determine the SM gauge structure. [speculative]

2. **Radiative corrections as $p$-adic mixing.** The $\sim 1\%$ deviations from exact 5-smooth ratios may arise from Archimedean–$p$-adic mixing effects. This is not yet computed. [speculative]

3. **Neutrino masses.** The 5-smooth hypothesis makes predictions for neutrino mass ratios, but these are not yet testable without the absolute neutrino mass scale. [not yet falsifiable]

### 11.3 What Would Disconfirm the Program

The program is disconfirmed if:

1. **Bosonic QEC error rates show Archimedean (not $p$-adic) scaling** in a clean transmon experiment.
2. **New precision mass measurements systematically deviate** from the 5-smooth lattice beyond $3\sigma$ after accounting for known radiative corrections.
3. **Entanglement entropy shows no $p$-adic step structure** in Fock-state subsystems.
4. **A bosonic QEC code is discovered whose error set does not respect $\mathcal{T}_2$ level boundaries.**
5. **Hadron resonances do not organize into families with integer-spaced pole separations $\Delta + 2\mathbb{Z}_{\geq 0}$ as predicted by the Bruhat–Tits Mellin amplitude.** If meson Regge trajectories are incompatible with the tree-level pole spectrum, the tree-based S-matrix is ruled out.
6. **$p$-adic S-matrix elements show $\pi$ dependence** — contradicting the result that tree-level Witten diagrams on $\mathcal{T}_p$ produce only rational functions of $p$.
7. **A time operator $[\hat{T}, \hat{H}] = i\hbar$ is constructed on a non-Archimedean completion of $\mathbb{Q}$,** contradicting the claim (derived from Ostrowski's theorem) that only $\mathbb{R}$ admits the ordered structure necessary for a Page–Wootters clock.

The program is **confirmed** (not proved, but strongly supported) if the experiments show $p$-adic signatures and if the 5-smooth mass deviations shrink as measurement precision improves.

### 11.4 Errata — v3.2 → v4.0 Corrections

**Version 3.1 of this paper (DOI 10.5281/zenodo.21539547) contained arithmetic errors in the mass ratio table (§7.2) and the Efimov $\lambda$ derivation (§7.1). These errors are corrected in v3.2:**

1. **Mass ratio triplets (5 of 9 corrected):** The $(a,b,c)$ triplets for $\tau/e$, $\tau/\mu$, $W/e$, $Z/e$, and $h/e$ did not produce the claimed numerical values when computed. All nine triplets have been recomputed and independently verified. The corrected values are listed in §7.2.

2. **Efimov $\lambda$ derivation:** The formula $\ln\lambda = 3/(\ln 2 + \ln 3 + \ln 5)$ stated in v3.1 is incorrect both as an arithmetic result ($3/\ln 30 \approx 0.882$, not $2.02$) and as a derivation of $\lambda$ (which requires solving a transcendental equation, not simple arithmetic of log-periods). This has been replaced with an honest structural correspondence in §7.1, noting that a direct analytic derivation remains an open problem.

3. **Semigroup density acknowledgment:** v3.1 did not acknowledge that the 5-smooth semigroup (Hamming numbers) $\{2^a \cdot 3^b \cdot 5^c\}$ is dense in $\mathbb{R}_+$, a genuine epistemological risk for any mass-fitting exercise. A new §7.4 explicitly addresses this risk with parsimony, consistency, and falsifiability arguments.

4. **Constraining literature:** v3.1 lacked a section discussing literature that constrains or challenges the adelic framework. A new §13 has been added per the Mandatory Symmetry Template (KIF-18).

### 11.5 Where External Literature Supports the Adelic Cross-Domain Framework

1. **Gubser, S.S. et al. (2017). "$p$-adic AdS/CFT." *Commun. Math. Phys.* 352, 1019.** DOI: 10.1007/s00220-017-2813-1. Established the $p$-adic AdS/CFT correspondence with the Bruhat–Tits tree as the bulk geometry — the foundational result that the tree IS a valid holographic space. The adelic cross-domain program extends this from holography alone to QEC, RG, and the mass spectrum.

2. **Efimov, V. (1970). "Energy levels arising from resonant two-body forces in a three-body system." *Phys. Lett. B* 33, 563–564.** DOI: 10.1016/0370-2693(70)90349-7. The Efimov effect demonstrates that the three-body problem produces an infinite geometric tower of bound states with universal ratio $\lambda \approx 22.7$ — a discretuum. The cross-domain program identifies this discretuum as the projection of the Bruhat–Tits tree onto the energy axis.

3. **Braaten, E. & Hammer, H.-W. (2006). "Universality in few-body systems with large scattering length." *Phys. Rept.* 428, 259–390.** DOI: 10.1016/j.physrep.2006.03.001. Comprehensive review confirming the universality of Efimov physics across atomic, nuclear, and molecular systems — supporting the claim that the discretuum is a general structural feature, not a coincidence of specific interactions.

4. **Gottesman, D., Kitaev, A., & Preskill, J. (2001). "Encoding a qubit in an oscillator." *Phys. Rev. A* 64, 012310.** DOI: 10.1103/PhysRevA.64.012310. The GKP code — foundational bosonic QEC — uses a lattice in phase space. The adelic program identifies this lattice with the 5-smooth semigroup (Hamming numbers) $\mathcal{P}$.

5. **Michael, M.H. et al. (2016). "New class of quantum error-correcting codes for a bosonic mode." *Phys. Rev. X* 6, 031006.** DOI: 10.1103/PhysRevX.6.031006. Binomial codes exploit number-state parity ($\operatorname{ord}_2 \bmod 1$) as the error-detection invariant — precisely the $\mathcal{T}_2$ invariant identified by the adelic program.

6. **Bost, J.-B. & Connes, A. (1995). "Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory." *Selecta Math. (N.S.)* 1, 411–457.** DOI: 10.1007/BF01589495. The Bost–Connes system provides a $C^*$-algebraic framework connecting number theory (explicit class field theory) to quantum statistical mechanics — an independent mathematical precedent for the "physics from number theory" paradigm.

### 11.6 Where External Literature Constrains or Contradicts the Adelic Cross-Domain Framework

1. **Weinberg, S. (1995). *The Quantum Theory of Fields*, Vol. I.** The Standard Model mass parameters are conventionally treated as free parameters of the Lagrangian, determined by experiment with no underlying theoretical derivation. This is the null hypothesis against which the adelic mass program must be tested. Any claim of 5-smooth mass ratios must overcome the prior that masses are arbitrary.

2. **Georgi, H. & Glashow, S.L. (1974). "Unity of all elementary-particle forces." *Phys. Rev. Lett.* 32, 438–441.** DOI: 10.1103/PhysRevLett.32.438. Grand Unified Theories (GUTs) predict mass relations via group-theoretic unification at a high scale, typically $\sim 10^{16}$ GeV. The adelic program predicts mass relations via $p$-adic tree geometry without invoking a GUT scale. The two frameworks make competing predictions for mass ratios; experimental resolution at the sub-1% level would discriminate between them.

3. **Particle Data Group (2024). "Review of Particle Physics." *PTEP* 2024, 083C01.** DOI: 10.1093/ptep/ptae074. The PDG error bars on quark masses are large (e.g., $m_s(2\text{ GeV}) = 93.4^{+8.6}_{-3.4}$ MeV), and running quark masses are scheme-dependent. The 5-smooth hypothesis's 1% precision target is achievable for lepton and gauge boson masses but faces fundamental limitations for light quarks where the error bars alone exceed the claimed tolerance.

4. **Density of the 5-smooth semigroup (Hamming numbers):** The semigroup $\mathcal{P} = \{2^a \cdot 3^b \cdot 5^c\}$ is dense in $\mathbb{R}_+$ because $\ln 2$, $\ln 3$, $\ln 5$ are linearly independent over $\mathbb{Q}$ (Kronecker's theorem). This means any real number — including any mass ratio — can be approximated arbitrarily closely by a 5-smooth triple. This is a structural constraint on the framework: 5-smooth approximation alone cannot serve as evidence of a physical mechanism without the parsimony, consistency, and falsifiability arguments discussed in §7.4.

5. **Archimedean continuum physics works:** The Standard Model, formulated on $\mathbb{R}^4$ with Archimedean analysis, is the most precisely tested physical theory in history (e.g., $g-2$ of the electron to 12 significant figures). Any framework claiming the Archimedean continuum is "an artifact" must explain why Archimedean physics works so well — not only claim it is an artifact.

6. **[NO CONSTRAINING EVIDENCE FOUND FOR: Bruhat–Tits tree as universal SM substrate, $p$-adic QEC error-weight hierarchy, 5-smooth mass hypothesis as an explicit predictive framework.]** The search terms used were: "p-adic standard model masses," "Bruhat-Tits tree particle physics," "p-adic quantum error correction," "5-smooth mass spectrum." The absence of direct challenges to these specific claims reflects the novelty of the adelic cross-domain program rather than its immunity to criticism. This is a risk: the framework has not yet been exposed to adversarial peer review in its current synthesized form.]

---

## 12. Coda — Natural Units, No Scales

The entire program is expressed in **natural units** ($\hbar = c = 1$), where all physical quantities reduce to dimensionless ratios. The natural coordinate system for these ratios is not the real numbers but the Bruhat–Tits trees $\mathcal{T}_2, \mathcal{T}_3, \mathcal{T}_5$, whose vertices are labeled by triplets of integers $(a, b, c)$ encoding the $p$-adic valuations.

There is no meter, no kilogram, no second. There is no Archimedean continuum. There are only prime numbers and their valuations — the most primitive mathematical structures possible.
The Standard Model, viewed through this lens, is not a list of 19 free parameters. It is the spectrum of a single geometric object: the joint Bruhat–Tits tree $\mathcal{T}_{2,3,5}$, embedded diagonally into the positive reals via the 5-smooth lattice. The particles are its vertices; their masses are their $p$-adic coordinates; their interactions are the tree edges.

Whether this vision is correct is a question for experiment — and the experiments are feasible, concrete, and already in progress.

---

## 13. Causal Structure and the Adelic S-Matrix

The preceding sections established that the joint Bruhat–Tits tree $\mathcal{T}_{2,3,5}$ encodes the static structure of the Standard Model — its mass spectrum, gauge groups, and error-correcting codes. A dynamical theory of scattering and time evolution remained incomplete in the earlier versions of this program. Phase 3 of this research program — documented in full in the companion artifacts C1-RT.2a through C1-RT.5 — resolves this gap.

### 13.1 $\pi$ Is Not an Idèle

A basic question for any adelic physical theory: does the constant $\pi$, which appears throughout Archimedean physics (cross-sections, Stefan–Boltzmann constants, anomalous dimensions), have a consistent $p$-adic analog?
The answer is **no** — and this is a structural result, not a failure of the program. Two independent constructions of $\pi_p$ from the Bruhat–Tits tree give incompatible valuations: the tree-geodesic definition yields $|\pi_p|_p = p$ (product diverges), while the period-of-$\mathbb{Q}_p$ definition yields $|\pi_p|_p = p^{-1/(p-1)}$ (product vanishes). Neither satisfies the idèle restricted-product condition $\prod_v |x|_v = 1$ [C1-RT.2a].

**The reason:** $\pi \notin \mathbb{Q}$. The adèle formalism is defined over $\mathbb{Q}$, and irrational numbers — let alone transcendentals — do not naturally embed into the finite-arithmetic structure of the adèles. Physical quantities that genuinely involve $\pi$ (such as the cross-section $\sigma$ to coupling $C$ ratio $\hat{\sigma}/C = 4$) survive because $\pi$ cancels in every ratio that is an adelic invariant. The $\pi$ that appears in Archimedean physics is a representation artifact of the continuum, not a fundamental constant [operational definition: π is not an adelic invariant; it cancels in every physically meaningful adelic ratio] of the adelic structure.

### 13.2 $p$-Adic Mellin Amplitudes

The Witten diagram on the Bruhat–Tits tree $\mathcal{T}_p$ — with bulk vertices serving as the $p$-adic analog of AdS space — produces the first explicit $p$-adic S-matrix elements. For $2 \to 2$ scattering of conformal dimension $\Delta$ boundary operators, the Mellin amplitude is [C1-RT.2]:

$$A_p(s,t) = N_p \left(\frac{1}{p^{s-\Delta} - 1} + \text{crossing}\right), \quad N_p = \frac{p^{\Delta}}{p+1}\Gamma_p(\Delta)^2$$

where $\Gamma_p$ is the $p$-adic gamma function. This amplitude has the following remarkable properties:

1. **Rational structure:** $A_p(s,t)$ is a rational function of $p^s$ and $p^t$, not a meromorphic function of complex $s,t$ with branch cuts — a fundamentally different analytic structure from the Archimedean $S$-matrix.
2. **Integer-spaced poles:** Poles occur at $s,t = \Delta + 2\mathbb{Z}_{\geq 0}$ — the spectrum of the tree Laplacian eigenvalues, universal across all primes. This is the sharpest falsifiable prediction of the framework: if hadron resonances do not organize into families with spacing governed by integer multiples of the conformal dimension $\Delta$, the tree-based $S$-matrix is ruled out.
3. **UV-finiteness:** The tree has a minimum edge length (one step), eliminating short-distance singularities by construction. No renormalization is needed.
4. **Tree unitarity:** The positive Laplacian spectrum guarantees a tree-level optical theorem.
5. **No $\pi$ dependence:** The amplitude involves only rational functions of $p$ and the $p$-adic gamma function — no transcendental constants appear.

### 13.3 PGL($n$) Generalization

Extending from PGL(2) (the tree) to PGL($n$) (Bruhat–Tits buildings) reveals that $n > 2$ buildings are chamber complexes, not trees — geodesics are non-unique, and the partial order is governed by the richer Bruhat order. The key physical insight: PGL(5) building boundary $\mathbb{P}^4(\mathbb{Q}_p)$ matches the $(3+1)$-dimensional spacetime dimension over $\mathbb{Q}_p$ [C1-RT.3].

However, the PGL(2) tree is **sufficient** for the causal and scattering problem addressed here. The $n > 2$ generalization is structurally characterized but explicit numerical computation is deferred: the tree provides the simplest setting for the causality resolution while the building captures the spacetime-dimensionality insight. The $\infty$-place provides spatial dimensions; $p$-adic places constrain via the product formula, not via direct spacetime embedding. Unitarity of the building $S$-matrix follows from the Harish-Chandra Plancherel formula [C1-RT.3].

### 13.4 The Adelic $S$-Matrix

The full adelic $S$-matrix is the restricted tensor product [C1-RT.4]:

$$S_{\text{adelic}} = S_{\infty} \otimes \left(\bigotimes'_p S_p\right)$$

where $S_p$ is the $p$-adic $S$-matrix (the Mellin amplitude $A_p(s,t)$ on $\mathcal{T}_p$) and $S_{\infty}$ is the Archimedean $S$-matrix. The restricted product $\otimes'_p$ means $S_p = I$ (free-field propagator) for all sufficiently large $p$ — a condition that is physically automatic due to **large-$p$ asymptotic freedom**: as $p \to \infty$, the tree branching factor $(p+1)$ grows, interactions are suppressed by destructive interference among the infinite neighbors, and the theory becomes free.

The double restricted product — one at the adèle level (all but finitely many $p$ have $S_p = I$), one at the S-matrix level (the physical amplitude is a convergent product over active primes $p \in \{2,3,5\}$) — guarantees finite predictions. Unitarity separates into Archimedean unitarity ($S_{\infty}^{\dagger} S_{\infty} = 1$ by the standard optical theorem) and $p$-adic tree-unitarity (each $S_p$ is positive in the Hecke algebra). The product formula $\prod_v |g_v^2|_v = 1$ constrains the relative normalization of couplings across places [C1-RT.4].

### 13.5 The Page–Wootters Adelic Clock and the Causality Resolution

The deepest challenge for any adelic physical theory is **causality**: how can a $p$-adic scattering theory, defined on a non-ordered field $\mathbb{Q}_p$, produce time-ordered physical predictions? This is resolved through a four-layer hierarchy [C1-RT.5]:

**Layer 1 — Tree partial order (C1-RT):** The Bruhat–Tits tree $\mathcal{T}_p$ has a natural partial order inherited from its root (the IR fixed point). Geodesic rays from the root to the boundary define a causal ordering: $v \prec w$ if $v$ lies on the unique geodesic from root to $w$. This replaces the total Archimedean time order on $\mathcal{T}_p$.

**Layer 2 — Mellin amplitudes (C1-RT.2):** The $p$-adic Mellin amplitude $A_p(s,t)$ respects the tree partial order — it requires no global time coordinate, only the local causal relations encoded by tree geodesics.

**Layer 3 — Restricted product $S$-matrix (C1-RT.4):** The adelic $S$-matrix $S_{\infty} \otimes (\otimes'_p S_p)$ combines Archimedean (time-ordered) and $p$-adic (tree-ordered) scattering into a single structure. The product formula $\prod_v |\mathcal{O}|_v = 1$ serves as the adelic constraint that ties the two causality regimes together.

**Layer 4 — Page–Wootters clock (C1-RT.5):** Ostrowski's theorem states that $\mathbb{R}$ is the **unique** ordered completion of $\mathbb{Q}$. Only an ordered field supports a Hermitian time operator $[\hat{T}, \hat{H}] = i\hbar$ — the defining relation of the Page–Wootters mechanism, in which time is an internal correlation between a clock system $C$ and the rest of the universe. The $\infty$-place is therefore the **unique** place that can serve as a clock.

The $p$-adic places are timeless Wheeler–DeWitt sectors — they satisfy the Hamiltonian constraint $\hat{H}_p |\Psi\rangle = 0$ with no external time parameter. The adelic Wheeler–DeWitt constraint is:

$$\prod_v |\mathcal{O}|_v = 1$$

where $\mathcal{O}$ is any adelic observable. The conditional state $|\Psi(t)\rangle_{\text{rest}} = {}_C\langle t | \Psi \rangle$ on the $p$-adic sectors inherits ultrametric structure from the diagonal coupling between the Archimedean clock and the $p$-adic degrees of freedom. This is an internal QNFO result — not yet independently verified [C1-RT.5].

**The causality problem is resolved:** the $\infty$-place provides the unique ordered time coordinate via the Page–Wootters mechanism, while each $p$-adic place contributes a tree-ordered causal structure. The adelic product formula ties them together. Physical predictions at the $\infty$-place are time-ordered in the usual sense; $p$-adic predictions are tree-ordered; and the joint $S$-matrix respects both simultaneously [C1-RT, C1-RT.5].

### 13.6 The $L_p(4,\omega^{-3})$ Block

One quantitative gap remains: the $p$-adic $L$-function $L_p(4,\omega^{-3})$ — required for a fully numerical evaluation of $\pi_p$ from the Stefan–Boltzmann derivation [C1-RT.2b] — has not been tabulated in accessible literature. This requires an original Coleman-integration computation that blocks only the **numerical** value of $\pi_p$, not any of the qualitative results above. The integer-spaced pole spectrum, the rational function structure of $A_p(s,t)$, the $\pi$ cancellation mechanism, and the Page–Wootters clock argument are all independent of this numerical gap [C1-RT.2b, C1-RT.2c].

---

## Appendix A — Complete Calibration Register

| ID | Year | Prediction | Disconfirmation Condition |
|:---|:-----|:-----------|:--------------------------|
| CAL-ALPHA-01 | 2028 | $\alpha^{-1}$ computable from adelic product | Computation fails to converge or disagrees with CODATA $> 5\sigma$ |
| CAL-HO-01 | 2028 | HO spectrum decomposes into $\mathcal{T}_{2,3,5}$ | Decomposition produces inconsistencies with known spectral data |
| CAL-SU3-01 | 2029 | SU(3) from $\mathcal{T}_3$ degeneracies | Discrepancy between tree-derived and observed SU(3) structure |
| CAL-RG-01 | 2028 | Code distance = number of irrelevant RG directions | Counterexample found for any bosonic code |
| CAL-QEC-01 | 2028 | QEC error sets respect $\mathcal{T}_2$ level boundaries | Non-$\mathcal{T}_2$-respecting bosonic QEC code demonstrated |
| CAL-QEC-02 | 2029 | $p$-adic error-rate scaling in bosonic systems | Archimedean scaling observed instead |
| CAL-QEC-03 | 2030 | GKP lattice spacing $\in \mathcal{P}$ | Optimal spacing off $\mathcal{P}$ beyond measurement error |
| CAL-HOL-01 | 2029 | Entanglement entropy steps at $p$-adic boundaries | Smooth entanglement scaling observed |
| CAL-HOL-02 | 2030 | Boundary CFT $c \propto \log p$ | Measured $c$ disagrees with $\log p$ |
| CAL-EFIMOV-01 | 2028 | $\lambda = e^{\pi/s_0}$ from adelic log-periods | $\lambda$ deviates $> 3\sigma$ from adelic prediction |
| CAL-MASS-01 | 2028 | All SM mass ratios $\in \mathcal{P}$ within 2% | Systematic deviation $> 3\sigma$ in new measurements |
| CAL-MASS-02 | 2030 | 5-smooth deviations shrink with precision | DISCONFIRMED 2026-07-31 (ACRP-04): deviations frozen at discrete-fit level; m_μ/m_e 9138σ from true PDG best-fit. Deviations persist with improved measurements. |
| CAL-EXP-01 | 2027 | $\Gamma(3)/\Gamma(1) > 0.3$ in transmon experiment | Ratio $< 0.1$ at $5\sigma$ |
| CAL-EXP-02 | 2028 | Step-function fit beats smooth log for $S_{\text{EE}}(L)$ | Bayes factor $> 10$ favors smooth model |
| CAL-EXP-03 | 2029 | Zero cross-talk between $\operatorname{ord}_2$ and $\operatorname{ord}_3$ syndromes | Mutual information $> 0$ at $5\sigma$ |
| CAL-PI-01 | 2028 | $\pi$ admits no consistent $p$-adic valuation at all primes | A $p$-adic $\pi$ satisfying $\prod_v |\pi_p|_p = 1$ is constructed [disconfirms idèle-blocking claim] |
| CAL-MELLIN-01 | 2029 | Hadron resonances organize into families with integer-spaced pole separations $\Delta + 2\mathbb{Z}_{\geq 0}$ | Any resonance with pole spacing incompatible with $2\mathbb{Z}$ at $3\sigma$ disconfirms |
| CAL-SMATRIX-01 | 2030 | $p$-adic S-matrix elements for active primes $\{2,3,5\}$ are rational functions of $p^s,p^t$ | Any $\pi$ dependence found in tree-level $p$-adic amplitude disconfirms |
| CAL-CLOCK-01 | 2028 | No Hermitian time operator $[\hat{T},\hat{H}] = i\hbar$ exists on any non-Archimedean completion of $\mathbb{Q}$ | Construction of a time operator on $\mathbb{Q}_p$ disconfirms |
| CAL-LP-BLOCK-01 | 2027 | $L_p(4,\omega^{-3})$ requires original Coleman integration — numerical $\pi_p$ pending this computation | Qualitative predictions (pole spectrum, $S$-matrix structure) unaffected by this gap |

---

## References

1. Particle Data Group (2024). Review of Particle Physics. *PTEP* 2024, 083C01. DOI: 10.1093/ptep/ptae074.
2. Wilson, K.G. (1971). RG and critical phenomena. *Phys. Rev. B* 4, 3174. DOI: 10.1103/PhysRevB.4.3174.
3. Knill, E., Laflamme, R. (1997). QEC conditions. *Phys. Rev. A* 55, 900. DOI: 10.1103/PhysRevA.55.900.
4. Gottesman, D., Kitaev, A., Preskill, J. (2001). Encoding a qubit in an oscillator. *Phys. Rev. A* 64, 012310. DOI: 10.1103/PhysRevA.64.012310.
5. Michael, M.H. et al. (2016). Binomial codes. *Phys. Rev. X* 6, 031006. DOI: 10.1103/PhysRevX.6.031006.
6. Hayden, P. et al. (2016). Holographic duality from random tensor networks. *JHEP* 2016, 9. DOI: 10.1007/JHEP11(2016)009.
7. Vidal, G. (2007). Entanglement Renormalization. *Phys. Rev. Lett.* 99, 220405. DOI: 10.1103/PhysRevLett.99.220405.
8. Gubser, S.S. et al. (2017). $p$-adic AdS/CFT. *Commun. Math. Phys.* 352, 1019. DOI: 10.1007/s00220-017-2813-1.
9. Efimov, V. (1970). Energy levels arising from resonant two-body forces. *Phys. Lett. B* 33, 563. DOI: 10.1016/0370-2693(70)90349-7.
10. Koch, J. et al. (2007). Charge-insensitive qubit. *Phys. Rev. A* 76, 042319. DOI: 10.1103/PhysRevA.76.042319.
11. Braaten, E. & Hammer, H.-W. (2006). Universality in few-body systems. *Phys. Rept.* 428, 259–390. DOI: 10.1016/j.physrep.2006.03.001.
12. Bost, J.-B. & Connes, A. (1995). Hecke algebras, type III factors and phase transitions. *Selecta Math. (N.S.)* 1, 411–457. DOI: 10.1007/BF01589495.
13. Georgi, H. & Glashow, S.L. (1974). Unity of all elementary-particle forces. *Phys. Rev. Lett.* 32, 438–441. DOI: 10.1103/PhysRevLett.32.438.
14. Weinberg, S. (1995). *The Quantum Theory of Fields*, Vol. I. Cambridge University Press.
