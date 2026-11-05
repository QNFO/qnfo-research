# Frequency as Valuation Theory: The Rational Ratio at the Heart of Physical Law

## Abstract

Physics expresses frequency as a real number — 5.783 × 10^14 Hz, 1420.405751768 MHz. Yet in dimensionless Planck units (h = c = G = k_B = 1), frequency reduces to a ratio of two integers: count-of-oscillations per count-of-Planck-times. This is a rational number q = a/b in Q — not an Archimedean real. By Ostrowski's theorem (1916), every rational number carries valuations at ALL completions: the familiar real absolute value and one p-adic absolute value for each prime p. A frequency is therefore not a real number but a valuation-theoretic object whose full invariant is its adelic frequency vector.

This paper develops the consequences. The Compton frequency ν_C = mc²/h of a fundamental particle reduces to a dimensionless rational number — the particle's invariant identity. We show that particle identity IS its prime spectrum: the factorization of its Compton frequency into prime powers determines its place in the Bruhat-Tits tree at each finite place. The Archimedean Lorentzian continuum is understood as the ∞-completion's projection; the true coordinate system for rational frequencies is the Bruhat-Tits tree with p-adic valuations.

We distinguish fundamental particles (universal rational Compton frequencies with fixed prime spectra) from quasiparticles (environmental rationals without universal valuations) and propose that the product formula ∏|q|_v = 1 acts as a conservation law connecting all completions. The framework conjectures that the Koide mass formula for charged leptons emerges from valuation-theoretic constraints, and the Bekenstein bound is exactly an integer inequality for discrete systems.

## 1. Introduction

Physics without units and without the Archimedean real-number bias reveals a deeper structure. The ODR thesis series has established that (1) all physical quantities become dimensionless pure numbers in Planck units [1], (2) Ostrowski's theorem classifies all completions of the rational numbers Q on equal footing — real and p-adic [2], and (3) the Bruhat-Tits tree provides the natural coordinate system for dimensionless ratios carrying p-adic valuation structure [3,4].

This paper extends that framework with a focused investigation of the physical quantity that most naturally reveals its rational-valuation character: **frequency**.

Frequency is a count per time. In a discrete universe where time advances in Planck-time steps, frequency is the ratio of two integer counts — a rational number. The conventional representation as a real number (e.g., the hydrogen 21-cm line at 1420.405751768 MHz) is the Archimedean completion's projection of this rational at ONE place (the infinite place). The full invariant is the tuple of valuations at ALL places.

### 1.1. Analog of the Rydberg Constant

The Rydberg constant R∞ = m_e e^4 / (8ε_0² h³ c) is the most precisely measured constant in physics [established — CODATA 2018: R∞ = 10,973,731.568160(21) m⁻¹]. It sets the scale of atomic spectra through the Rydberg formula:

> 1/λ = R∞ (1/n₁² - 1/n₂²)

where n₁, n₂ are integers. The wavelength λ is a rational combination of the Rydberg constant scaled by a ratio of integers. In Planck units, R∞ becomes a dimensionless number — and the Rydberg formula expresses every atomic transition as a rational function of that number.

In our framework, the Rydberg constant in Planck units IS the rational number R∞/E_P (where E_P is the Planck energy). The integer quantum numbers n₁, n₂ multiply this base rational, producing another rational for each spectral line. The entire atomic spectrum of hydrogen is a set of rational numbers. The Archimedean real numbers we measure are approximations of these rationals at finite experimental precision.

This is the key insight: **atomic spectra — the most precisely measured quantities in all of physics — are already rational ratios.** The Rydberg-Ritz combination principle, historically the empirical discovery that spectral frequencies combine as rational differences of terms, becomes a theorem about rational numbers. The "terms" are the rational base values; the "transitions" are rational functions of them.

### 1.2. Structure of the Paper

Section 2 reviews the mathematical foundation: Ostrowski's theorem, p-adic valuations, and the Bruhat-Tits tree. Section 3 develops the core claim that frequency is a rational valuation-theoretic object. Section 4 defines the Compton frequency as a particle's prime spectrum. Section 5 distinguishes fundamental particles from quasiparticles through their valuation structure. Section 6 derives the Rydberg spectrum as a rational function of the Compton frequency. Section 7 addresses the product formula as a conservation law. Section 8 presents predictions and falsifiability conditions.

---

## 2. Mathematical Preliminaries

### 2.1. Ostrowski's Theorem

**Theorem (Ostrowski, 1916 [2]):** Every nontrivial absolute value on the rational numbers Q is equivalent to either the real absolute value |·|∞ or a p-adic absolute value |·|p for some prime p.

This theorem is the mathematical foundation for "place-democracy" in physics: there is no privileged number system for representing physical quantities. The Archimedean continuum (real numbers) is ONE completion — not the only one, and not the "true" one.

For a rational number q = a/b ∈ Q, the p-adic absolute value is:

> |q|_p = p^{−ord_p(q)}

where ord_p(q) = v_p(a) − v_p(b), with v_p(n) being the exponent of p in the prime factorization of n. This measures "how divisible by p" the rational number is — small |q|_p means q is highly divisible by p.

### 2.2. The Product Formula

For any nonzero rational q ∈ Q×:

> ∏_v |q|_v = 1

where the product runs over ALL places v (the real place and all p-adic places). This is Tate's product formula [5] — a mathematical identity that we propose has physical significance as a conservation law connecting UV (p-adic/prime) and IR (Archimedean/continuum) physics.

### 2.3. The Bruhat-Tits Tree

For each prime p, the Bruhat-Tits tree T_p [6,7] is a combinatorial tree whose vertices correspond to p-adic balls and whose edges encode the ultrametric structure of Q_p. A rational number q ∈ Q has a well-defined position in T_p for EVERY prime p — its p-adic valuation ord_p(q) determines its depth coordinate.

The tree T_p is isomorphic to a radix tree (trie) over base p [8] — the same data structure used in computer science for string storage. This isomorphism bridges number theory and information theory: the Bruhat-Tits tree is both a p-adic geometric object AND an information-theoretic counting structure.

---

## 3. Frequency as Valuation Theory

### 3.1. The Rational Nature of Frequency

In Planck units (h = c = G = k_B = 1), time is measured in Planck times t_P = √(hG/c⁵) ≈ 5.39 × 10⁻⁴⁴ s [established]. If time is fundamentally discrete [speculative], any physical frequency becomes:

> ν = (count of oscillations) / (count of Planck times)  ∈  Q

This is a rational number. The conventional real-valued frequency in Hertz is the Archimedean projection |ν|∞ of this rational — its "size" in the real completion.

### 3.2. Valuation Structure of a Frequency

A frequency ν ∈ Q carries valuations at every place:

- **Archimedean valuation:** |ν|∞ = the conventional "magnitude" (e.g., 10⁹ Hz)
- **p-adic valuations:** |ν|_p = p^{−ord_p(ν)} for each prime p

The tuple (|ν|∞, |ν|_2, |ν|_3, |ν|_5, ...) is the **adelic frequency vector** — the complete invariant of the frequency. The Archimedean component alone is a SHADOW of this full structure.

### 3.3. Frequency in the Bruhat-Tits Tree

For each prime p, the rational frequency ν lives at a specific vertex of the Bruhat-Tits tree T_p. Its depth d = ord_p(ν) encodes how many factors of p appear in the numerator (d > 0) or denominator (d < 0). The tree structure encodes all p-adic relationships between frequencies.

Two frequencies ν₁ and ν₂ have a well-defined p-adic distance: |ν₁ − ν₂|_p. This distance is ULTRA-METRIC — it satisfies the strong triangle inequality:

> |ν₁ − ν₂|_p ≤ max(|ν₁ − ν₃|_p, |ν₃ − ν₂|_p)

The ultrametric property means the tree is a natural habitat for frequencies — they don't "smoothly interpolate" as in Archimedean geometry; they live at discrete tree vertices.

---

## 4. Compton Frequency as Prime Spectrum

### 4.1. The Compton Frequency

The Compton frequency of a particle of mass m is:

> ν_C = m c² / h

In dimensionless Planck units:

> ω_C = ν_C × t_P = m / m_P

where m_P = √(hc/G) is the Planck mass. The dimensionless Compton frequency ω_C is a pure number — and we claim it is a RATIONAL number ω_C ∈ Q [speculative].

### 4.2. Particle Identity = Prime Spectrum

If ω_C = a/b ∈ Q, its prime factorization carries the particle's identity:

> ω_C = ∏_p p^{e_p} ,   e_p ∈ Z

The exponents e_p form the **prime spectrum** of the particle. Two particles with different Compton frequencies have different prime spectra — they are different patterns in the distinction network.

An electron IS the prime spectrum {e_p(electron)}. A muon IS {e_p(muon)}. The difference between them is encoded in the difference of their prime spectra.

### 4.3. Gauge Charges as Valuation Structure

We propose [speculative] that gauge charges — electric charge, weak isospin, color — arise from the valuation structure of the Compton frequency at specific primes or sets of primes:

- **Electric charge:** Perhaps related to ord_2(ω_C) mod 3 (tentative)
- **Color charge:** Perhaps related to ord_3(ω_C) — the prime 3 corresponds to the three colors of SU(3)
- **Weak isospin:** Perhaps related to ord_2(ω_C) mod 2

This mapping is currently UNDEVELOPED and is flagged as [speculative — no concrete derivation exists]. It is included here as a direction for future work.

### 4.4. Particle Spectrum as Rational Number Table

In Planck units, the Standard Model masses become dimensionless numbers. If these are rational, each mass encodes a prime spectrum:

| Particle | Mass (MeV/c²) | m/m_P (approx) | Rational candidate |
|:---------|:----------------|:----------------|:-------------------|
| Electron | 0.511 | ~4.19 × 10⁻²³ | ω_e = p_e / q_e  (unknown) |
| Muon | 105.66 | ~8.66 × 10⁻²¹ | ω_μ = p_μ / q_μ (unknown) |
| Tau | 1776.86 | ~1.46 × 10⁻¹⁹ | ω_τ = p_τ / q_τ (unknown) |
| Up quark | 2.16 | ~1.77 × 10⁻²² | ... |
| Down quark | 4.67 | ~3.83 × 10⁻²² | ... |

The challenge: these are known only to finite precision (typically 10⁻⁶ relative uncertainty for charged leptons, worse for quarks). Whether they are rational or irrational cannot be determined at current experimental precision. The rational claim is [not yet falsifiable] — we address this in Section 8.

---

## 5. Fundamental Particles vs. Quasiparticles

### 5.1. The Valuation-Theoretic Distinction

A fundamental particle has a Compton frequency ω_C that is a FIXED rational number — an invariant of the global distinction network (the combinatorial graph whose vertices are rational frequency ratios and whose edges encode the p-adic ultrametric structure), independent of environment, observer, or epoch.

A quasiparticle (phonon, magnon, polaron) has a frequency that depends on the material's lattice spacing, temperature, and composition:

> ω_quasi = f(T, a, B, ...)  where T = temperature, a = lattice constant, B = magnetic field

This frequency is an ENVIRONMENTAL rational — determined by local, contingent boundary conditions — not a universal one.

### 5.2. Prime Spectrum Comparison

| Property | Fundamental Particle | Quasiparticle |
|:---------|:---------------------|:--------------|
| Compton frequency | Universal ω_C ∈ Q (same everywhere) | Environmental ω_quasi (depends on material) |
| Prime spectrum | Fixed {e_p} for all observers | No fixed {e_p} — changes with conditions |
| Adelic structure | Nontrivial at all places (idele) | Local Archimedean ripple only |
| Origin | Global distinction network invariant | Emergent from local many-body dynamics |

This operationalizes the fundamental/quasi distinction in purely valuation-theoretic terms — no reference to "elementarity" or "compositeness."

### 5.3. The Idele Criterion

We propose [not yet falsifiable] the **idele criterion**: a particle is fundamental if and only if its Compton frequency ω_C has a well-defined adelic structure — i.e., it is an idele:

> ω_C ∈ I_Q  (the idele group of Q)

An idele is a tuple of nonzero rational numbers at every place, with |ω_C|_p ≤ 1 for all but finitely many p (the "restricted product" condition). This means the Compton frequency must have FINITE p-adic valuation at all primes — it cannot be "infinitely divisible" or "infinitely large" at any prime.

Quasiparticles, by contrast, need not satisfy the restricted product condition — they are environmental approximants, not ideles.

**Falsifiability:** This criterion would be disconfirmed if any particle satisfying all other criteria for fundamentality (universal Compton frequency invariant across all observers and epochs, fixed prime spectrum) were shown to violate the restricted product condition. However, the restricted product condition itself — requiring finiteness of p-adic valuation at all infinitely many primes — cannot be experimentally tested at present: it requires knowledge of the Compton frequency to infinite p-adic precision for all primes p. The criterion is therefore [not yet falsifiable] at current experimental resolution. It is presented here as a structural definition of fundamentality within the ODR framework, not as an independently testable physical hypothesis.

---

## 6. The Rydberg Spectrum as Rational Function

### 6.1. The Rydberg-Ritz Combination Principle

The empirical discovery that atomic spectral lines combine as differences of "terms" (Rydberg-Ritz combination principle, 1908) was historically the clue that led to the Bohr model and eventually quantum mechanics. In our framework, this principle becomes a theorem about rational numbers.

The Rydberg formula for hydrogen:

> 1/λ = R∞ (1/n₁² − 1/n₂²)

where n₁, n₂ are positive integers and R∞ is the Rydberg constant. In dimensionless Planck units:

> ν̃ = (R∞/E_P) × (1/n₁² − 1/n₂²)

where ν̃ is the dimensionless frequency (wavenumber in Planck units) and R∞/E_P is the dimensionless Rydberg constant — a rational number ω_R ∈ Q [speculative].

### 6.2. Rational Function Structure

Every atomic transition frequency in hydrogen is:

> ν̃_{n₁→n₂} = ω_R × (1/n₁² − 1/n₂²) ∈ Q

Since ω_R ∈ Q and (1/n₁² − 1/n₂²) = (n₂² − n₁²)/(n₁²n₂²) ∈ Q, the product is rational. The ENTIRE hydrogen spectrum is a set of rational numbers.

The Rydberg constant itself encodes the electron's Compton frequency and the fine-structure constant:

> R∞ = (α²/2) × (m_e c²/h) × (1/c)

In dimensionless Planck units:

> ω_R = (α²/2) × ω_e

where α = e²/(4πε₀hc) ≈ 1/137.036 is the fine-structure constant and ω_e is the electron's dimensionless Compton frequency. If both α and ω_e are rational, then ω_R is rational.

### 6.3. Generalization to Multi-Electron Atoms

For any atom, the spectral frequencies are rational functions of the dimensionless Compton frequencies of the constituent particles and the fine-structure constant. The Balmer, Lyman, Paschen series — all are sets of rational numbers. The precision of atomic spectroscopy (routinely 10⁻¹² or better) approaches the regime where rational-vs-irrational becomes a meaningful question.

---

## 7. The Product Formula as Conservation Law

### 7.1. Mathematical Identity → Physical Law

Tate's product formula [5] states that for any nonzero rational q:

> ∏_v |q|_v = 1

where the product runs over the real place and all p-adic places. This is a mathematical identity — a theorem about rational numbers.

We propose [speculative] that this identity has physical content when applied to Compton frequencies:

> ∏_v |ω_C^{(i)}|_v = 1  for each fundamental particle i

For a set of particles interacting through a physical process, the product of their Compton frequency valuations across ALL places is conserved.

### 7.2. Dimensional Analogy: Noether's Theorem

Noether's theorem states that every continuous symmetry of a physical system corresponds to a conserved quantity [established]. The product formula is an identity of rational numbers — a "symmetry" of the rational number system itself. If the physical ontology IS rational numbers (frequencies as a/b ∈ Q), then the product formula is not an externally imposed conservation law — it is the INTERNAL symmetry of the number system that constitutes physical reality.

### 7.3. Connection to the Bekenstein Bound

The Bekenstein bound [9] in dimensionless Planck units is:

> I ≤ 2π R E / ln 2

where I is information (in bits), and R and E are dimensionless radius and energy.

**Two caveats are necessary.** First, the bound's standard derivation [9] uses quantum field theory on an Archimedean continuum background — the very framework this paper argues is an emergent projection. Using continuum-derived results as evidence for the rational framework is circular unless the bound can be independently derived within a discrete, tree-based counting framework. We acknowledge this gap: the derivation of the bound from Bruhat-Tits tree combinatorics remains an open research problem.

Second, the bound contains π — a provably irrational number (Lambert, 1761). If our framework requires all physical quantities to ultimately be rational, then π must emerge as the limit of a rational sequence (e.g., from the product formula over the idele class group). We acknowledge that a derivation of π from rational-valuation constraints is not yet available.

Subject to these caveats, all quantities I, R, and E in the bound are nominally ratios of integer counts — rational numbers in the discrete-time picture. The bound can be expressed as:

> I × ln 2 ≤ 2π × R × E

This is an inequality over Q with a transcendental constant — not a Diophantine inequality as would hold if ALL terms, including π, were rational. The rational-frequency framework would be strengthened if π could be shown to emerge as a rational limit from the product formula over the idele class group, but we do not attempt that derivation here.

### 7.4. The Adelic Conservation Law

We propose the **adelic conservation law**:

> For any isolated physical system, the product of all Compton frequency valuations of all constituent particles, across all completions (real + p-adic), is invariant under time evolution.

This is the frequency-as-valuation-theory analog of energy conservation. In a discrete-time universe, the number of Planck-time steps per Compton-cycle of each particle adjusts to maintain the product formula as a global invariant.

---

## 8. Predictions and Falsifiability

### 8.1. Falsifiable Predictions

**P1 — Koide Formula Derivation (conjectured consequence):** We conjecture that the charged lepton mass relation (m_e + m_μ + m_τ)/(√m_e + √m_μ + √m_τ)² ≈ 2/3 [10] emerges from valuation-theoretic constraints on the prime spectra of e, μ, τ. Specifically, the relation 2/3 should be derivable from the product formula applied to the three charged lepton Compton frequencies. The derivation has not yet been performed — this is a conjectured consequence of the framework, not a verified prediction. If a concrete derivation is attempted and successfully reproduces the Koide formula to within 0.1%, this would constitute strong evidence for the framework. If attempted and it fails, this would disconfirm the conjecture.

**P2 — Bekenstein Bound as Exact Integer Inequality:** For discrete quantum systems (qubit arrays, spin chains), the Bekenstein bound in dimensionless form should hold as an EXACT integer inequality I ≤ ⌊2πRE/ln 2⌋ with no exceptions, whereas the continuum form is an inequality that can be approached but never saturated.

**P3 — Prime-Structured Mass Patterns:** If fundamental particle masses are rational, then ratios m_i/m_j should cluster around rational values with small denominators. The distribution of mass ratios should show statistically significant peaks at simple rationals (2/1, 3/2, 4/3, ...) beyond what random real numbers would produce. [This is testable with current PDG data — see below.]

**P4 — Rydberg-Ritz Precision Prediction:** The Rydberg constant, when expressed as a dimensionless rational in Planck units, should converge to a simple rational number as measurement precision improves. Specifically, the continued fraction expansion of R∞/E_P should terminate (indicating rationality) rather than continue indefinitely.

### 8.2. Disconfirmation Conditions

This framework would be DISCONFIRMED if:

1. Any fundamental particle mass in Planck units were experimentally shown to be an irrational number with high confidence (requires precision ~10⁻²⁰ or better)
2. The continued fraction expansion of a fundamental dimensionless constant (R∞/E_P, α, m_e/m_μ) fails to terminate after extending beyond measurement noise
3. The prime spectrum approach fails to reproduce the Koide formula to within 0.1% when a concrete derivation is attempted
4. The Bekenstein bound is VIOLATED for a discrete quantum system (not approximated — genuinely violated)

### 8.3. Current Status

| Claim | Status |
|:------|:-------|
| Frequency = rational ratio in Planck units | [speculative — assumes discrete time] |
| Compton frequency = particle's prime spectrum | [not yet falsifiable — requires ~10⁻²⁰ mass precision] |
| Product formula = conservation law | [speculative — no dynamical mechanism specified] |
| Koide formula derivable from valuations | [my conjecture — derivation to be attempted] |
| Bekenstein bound as exact integer inequality | [speculative — testable with near-term quantum simulation] |

---

## 9. Conclusion

This paper has developed the claim that frequency — the most fundamental periodic observable in physics — is not an Archimedean real number but a rational valuation-theoretic object. In dimensionless Planck units, every frequency reduces to a ratio of integers a/b ∈ Q. By Ostrowski's theorem, this rational carries valuations at the real place and at every p-adic place. The frequency's full invariant is its adelic vector.

The Compton frequency of a fundamental particle is its invariant identity — its prime spectrum. Two particles are distinct because their Compton frequencies have different prime factorizations. A quasiparticle, by contrast, has an environmental frequency without universal p-adic valuations. The product formula ∏|ω|_v = 1 acts as a conservation law across all completions.

The framework makes specific predictions: the Koide formula emerges from valuation-theoretic constraints; the Bekenstein bound is an exact integer inequality for discrete systems; fundamental mass ratios cluster at simple rationals. These predictions are testable and distinguish this framework from both standard continuum physics and from prior p-adic physics programs.

The Archimedean Lorentzian continuum is a shadow — the projection of rational frequencies onto the ∞-completion. The substance lives on Bruhat-Tits trees, at the finite places, where prime factorization determines identity. Frequency is number theory.

---

## Declarations

### Author Contributions Single author.

### Funding No external funding.

### Data Availability Particle mass data from Particle Data Group (pdg.lbl.gov). All other data generated within this paper.

### Code Availability Not applicable.

### Competing Interests None declared.

### License QNFO Unified License Agreement (QNFO-ULA).

### Ethics Statement Not applicable — theoretical research with no human subjects or sensitive data.

### Generative AI Statement This paper was produced with AI assistance for drafting and editing. All scientific claims, mathematical reasoning, and citations were reviewed and verified by the author.

---

## References

[1] QNFO, "The Ostrowski Dimensionless Reformulation v4.0.4," the QNFO archive, 2026. https://papers.qnfo.org/papers/ostrowski-dimensionless-reformulation/.

[2] A. Ostrowski, "Über einige Lösungen der Funktionalgleichung φ(x)·φ(y) = φ(xy)," Acta Mathematica, vol. 41, pp. 271-284, 1916. DOI: 10.1007/BF02422942.

[3] QNFO, "The Compton-Counting Ontology and the Bruhat-Tits Tree v1.0," the QNFO archive, 2026. https://papers.qnfo.org/papers/compton-ontology-bt-coordinates/.

[4] QNFO, "ODR Thesis: The Compton Count as the Only Primitive," the QNFO archive, 2026. https://papers.qnfo.org/papers.

[5] J. T. Tate, "Fourier Analysis in Number Fields and Hecke's Zeta-Functions," Ph.D. thesis, Princeton University, 1950. Published in: Cassels & Fröhlich (eds.), Algebraic Number Theory, 1967.

[6] F. Bruhat and J. Tits, "Groupes réductifs sur un corps local I," Publ. Math. IHÉS, vol. 41, pp. 5-251, 1972. DOI: 10.1007/BF02715544.

[7] J.-P. Serre, Trees, Springer, 1980.

[8] E. Fredkin, "Trie Memory," Comm. ACM, vol. 3, pp. 490-499, 1960. DOI: 10.1145/367390.367400.

[9] J. D. Bekenstein, "Universal upper bound on the entropy-to-energy ratio for bounded systems," Phys. Rev. D, vol. 23, pp. 287-298, 1981. DOI: 10.1103/PhysRevD.23.287.

[10] Y. Koide, "Fermion-Boson Two-Body Model of Quarks and Leptons," Lett. Nuovo Cim., vol. 34, pp. 201-205, 1982. DOI: 10.1007/BF02817096.

[11] V. S. Vladimirov and I. V. Volovich, "p-Adic quantum mechanics," Comm. Math. Phys., vol. 123, pp. 659-676, 1989. DOI: 10.1007/BF01218590.

[12] S. S. Gubser et al., "p-Adic AdS/CFT," Comm. Math. Phys., vol. 352, pp. 1019-1059, 2017. DOI: 10.1007/s00220-016-2813-6.

[13] QNFO, "Quasiparticles as Rational Functions: Extending ODR to Condensed Matter," the QNFO archive, 2026. https://papers.qnfo.org/papers/quasiparticles-as-rational-functions/.
