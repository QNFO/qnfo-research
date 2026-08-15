---
title: "The Exchange Phase as a Logical Scalar: R = e^{2πis} from the Re-Entrant Calculus"
author: "Rowan Brad Quni-Gudzinas"
affiliation: "QNFO"
ORCID: "0009-0002-4317-5604"
date: "2026-08-14"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: "10.5281/zenodo.21941238"
status: "published"
---

## Abstract

The boson/fermion dichotomy is conventionally presented as a primitive classification of nature. Recent work established that the underlying invariant is the relation between the exchange phase of identical particles and their topological spin, R = e^{2πis}, with the dichotomy as its shadow in three spatial dimensions where the involutive braiding quantizes the spin parameter. This paper examines whether a calculus whose only primitive is the act of drawing a distinction can generate this invariant rather than importing it as an axiom. The re-entrant mark of the calculus of indications, disciplined by linearity, already generates the constants e and π as logical scalars: e as the fixed point of the differential equation D f = f, and π as the trace of the identity on the circle type. The central observation of this paper is that the exchange phase is the (2s)-fold half-turn of the re-entrant mark: R = (e^{iπ})^{2s} = e^{2πis} = (−1)^{2s}, so that the boson/fermion dichotomy is the parity of 2s. The arithmetic identity is established; the identification of the exchange monodromy with a power of the mark's half-turn is a model of the re-entrant phase; the claim that the calculus derives the invariant as a logical scalar within a single formal system is stated as a conjecture with explicit falsifiability conditions. The framework is distinguished from the nearest prior work deriving a Z₂ exchange phase from self-referential scattering, which lacks both the power structure for arbitrary spin and the unification of e, π, and R as a single scalar family.

**Keywords:** exchange phase; spin-statistics; topological spin; laws of form; re-entrant mark; logical scalar; anyons

## 1. Introduction

The spin-statistics theorem is among the most robust laws of physics: integer-spin particles obey Bose–Einstein statistics and half-integer-spin particles obey Fermi–Dirac statistics [Pauli 1940]. The QNFO research program has pursued the structural reading of this law. In [Quni-Gudzinas 2026b] it was established that the primitive content is not the dichotomy itself but the relation

$$R = e^{2\pi i s} \quad [\text{ESTABLISHED}]$$

between the exchange phase of identical particles and their topological spin, where the boson/fermion binary is a dimension-dependent shadow of this relation in three spatial dimensions [ESTABLISHED]. The same work identified a derivation target: a distinction-based foundation of physics must derive exchange statistics from the primitive act of drawing a boundary, rather than importing the relation as an axiom. The required construction was formalized — two modal exponentials, the braiding of two marks in a compact closed category, and the ribbon condition — yielding η = ±1 in the symmetric case, with η = −1 identified with the treatise's half-turn phase e^{iπ} = −1.

This paper closes the remaining gap with one structural observation: **the exchange phase is the (2s)-fold half-turn of the re-entrant mark**. The constants e and π have already been shown to arise as logical scalars of the re-entrant calculus — values the type theory computes rather than axioms it imports [Quni-Gudzinas 2026a]. This paper extends the scalar family to the exchange phase R = (e^{iπ})^{2s}, and states precisely what is established, what is a model, and what is conjectural about that identification.

## 2. Background: the invariant and the machinery

### 2.1 The invariant R = e^{2πis}

The exchange of two identical particles is a loop in their configuration space. The phase acquired is a representation of the fundamental group of that space: π₁ = ℤ₂ in dimension d ≥ 3, and π₁ = B₂ ≅ ℤ in dimension d = 2 [Leinaas and Myrheim 1977]. The spin-statistics relation states which phase is realized: η = (−1)^{2s}, where s is the spin [Pauli 1940; Duck and Sudarshan 1998]. In dimension d ≥ 3 the involutive braiding forces 2s ∈ ℤ, so the exchange phase is ±1 and particles are bosons or fermions; in dimension d = 2 the quantization collapses to continuity, and arbitrary exchange phases e^{2πis} describe anyons [Wilczek 1982; Kitaev 2006]. [ESTABLISHED]

### 2.2 The re-entrant calculus

The calculus of indications [Spencer-Brown 1969] takes the drawing of a distinction as primitive. The re-entrant form f = f̄ oscillates, generating a discrete clock of period 2: f(n) = (−1)^n f(0) [ESTABLISHED — elementary consequence]. Under linear discipline [Quni-Gudzinas 2026a]:

- **e** arises as the logical scalar of the differential fixed point: D f = f, f(0) = 1, with unique solution f(x) = e^x and e = Σ 1/n! [established analysis];
- **π** arises as the trace of the identity on the circle type: π = Tr(id_{S¹}) = C/d in the analytic realization, where the circle carries its geometric structure and the trace is computed by the Gaussian-integral construction [established geometry; logical derivation: [my conjecture]];
- **the half-turn** of the circle carries the marked state to the unmarked state: e^{iπ} = −1, the geometric root of the Euler identity [ESTABLISHED — Euler's formula].

The exchange of two marks in a compact closed category was constructed in [Quni-Gudzinas 2026b, notebook T2]: the exchange map σ_{M,M} = η·id for the self-dual mark, the ribbon identity η = θ_M, and the symmetric-category constraint η = ±1, with η = −1 identified with Crossing (e^{iπ} = −1) and η = +1 with Calling.

### 2.3 The gap

The parent works establish η = ±1 (symmetric case) and identify the single sign η = −1 with the treatise's half-turn, but never write the power structure R = (e^{iπ})^{2s} that covers arbitrary spin s and the 2+1-dimensional anyon generalization. The leap from "the mark has a half-turn phase" to "two marks anticommute" is asserted, not derived [Quni-Gudzinas 2026b]. This paper supplies the missing composite reading.

## 3. Core claim

> **The exchange phase R = e^{2πis} is the (2s)-fold half-turn of the re-entrant mark:**
> $$R = (e^{i\pi})^{2s} = e^{2\pi i s} = (-1)^{2s},$$
> **with the boson/fermion dichotomy the parity of 2s.**

**Formally:**
- s ∈ ℤ: 2s even → R = +1 → Bose–Einstein statistics (symmetric exchange, Calling);
- s ∈ ℤ + ½: 2s odd → R = −1 → Fermi–Dirac statistics (antisymmetric exchange, Crossing);
- 3+1-dimensional involutive braiding quantizes s to {0, 1/2, 1, 3/2, …} → the dichotomy [ESTABLISHED, Quni-Gudzinas 2026b];
- 2+1 dimensions allow any real s → anyon phases e^{2πis} [ESTABLISHED, Leinaas and Myrheim 1977].

**Scope note on the equality chain.** The final equality (−1)^{2s} = ±1 holds only in the quantized case 2s ∈ ℤ. For arbitrary real s the general form is R = e^{2πis} = cos 2πs + i sin 2πs (e.g., s = 1/4 gives R = i). The specific reading advanced here is the middle form: R as a power of the treatise's half-turn, (e^{iπ})^{2s} — the monodromy of the exchange loop as the (2s)-fold iteration of the half-turn e^{iπ} = −1.

## 4. The derivation

**Step 1 — the exchange map exists in the compact closed structure.** [established — construction] The exchange σ_{M,M}: M⊗M → M⊗M is the braiding of the self-dual mark. In a symmetric braided category σ² = id, so σ has eigenvalues ±1 with idempotent projectors P_sym = ½(1+σ) and P_antisym = ½(1−σ).

**Step 2 — the half-turn as the basic monodromy.** [established — treatise §12.1] The half-turn of the circle carries the marked state to the unmarked state: e^{iπ} = −1 = Crossing. This is the single-mark monodromy under rotation by π.

**Step 3 — exchange phase as a power of the half-turn.** [MAP — model of the re-entrant phase] The exchange of two particles is a loop in their configuration space. The loop winds the relative coordinate; the phase acquired is the monodromy of that loop. The reading advanced here is that the exchange monodromy is the (2s)-fold iteration of the mark's half-turn: R = (e^{iπ})^{2s} = e^{2πis} = (−1)^{2s}. The arithmetic identity is [established]; the identification of the exchange monodromy with a power of the mark's half-turn is [MAP — model].

**Step 4 — parity of 2s → the dichotomy.** [established arithmetic + Quni-Gudzinas 2026b §1] The dichotomy is exactly the parity of 2s.

**Step 5 — dimension quantization.** [established — Quni-Gudzinas 2026b §3] In d ≥ 3 the involutive braiding forces 2s ∈ ℤ → R = ±1; in d = 2 the braid group allows continuous s → anyon phases e^{2πis}.

**Step 6 — unification with e and π.** [my conjecture — the scalar family] e (the fixed point of D f = f), π (the trace of the identity on S¹), and R (the monodromy power of the half-turn) form one family of logical scalars of the re-entrant mark under linear discipline: fixed point, trace, monodromy power.

## 5. Status ladder

| Component | Status |
|---|---|
| Exchange map σ_{M,M}; projectors P_sym/P_antisym | [established — Quni-Gudzinas 2026b, notebooks T1/T2] |
| Half-turn e^{iπ} = −1 | [established — treatise §12.1] |
| η = −1 ↔ Crossing; η = +1 ↔ Calling | [established — Quni-Gudzinas 2026b, notebook T2] |
| (e^{iπ})^{2s} = (−1)^{2s} = ±1 for 2s ∈ ℤ | [established — elementary arithmetic] |
| Exchange monodromy = (2s)-fold half-turn | [MAP — model of the re-entrant phase] |
| e/π/R scalar-family unification | [my conjecture] |
| Formal derivation in the traced differential cohesive linear type theory | [my conjecture — F1 target] |
| Physical realization (which sign, in 3+1D) | [established physics; external Lorentz/microcausality input] |

## 6. Falsifiability conditions

- **F1 (formal).** The claim that the re-entrant calculus *generates* R = (e^{iπ})^{2s} as a logical scalar is falsified if no derivation exists within the traced differential cohesive linear type theory of the treatise (Part VIII) without importing the relation as an axiom. This is a concrete, checkable claim about a formal system. [my conjecture]
- **F2 (empirical, inherited).** If a stable, local, relativistic excitation in 3+1 dimensions is observed with exchange phase η ≠ e^{2πis} (e.g., a spin-1/2 particle obeying Bose–Einstein statistics), the invariant claim is disconfirmed. No such particle is known in the Standard Model. Evasion strategies in the literature (e.g., mass-dimension-three-half spinors [Ahluwalia and Lee 2022]) target the standard theorem statement rather than the invariant relation itself. [established — restated from Quni-Gudzinas 2026b F1]
- **F3 (scope).** The arithmetic identity R = (e^{iπ})^{2s} = (−1)^{2s} is [established] elementary arithmetic; the identification of the exchange phase with the (2s)-fold half-turn in the geometric model is [MAP — model]; the claim that this identification is a logical derivation within a single formal system is [my conjecture].

**Disconfirmation summary.** The invariant claim is disconfirmed if: (a) a formal derivation in the Part VIII system is shown impossible without importing the relation as an axiom (F1); or (b) an empirical excitation with exchange phase η ≠ e^{2πis} is observed in 3+1 dimensions (F2). Neither condition is currently met.

## 7. Relation to prior work

**Quni-Gudzinas 2026b (parent).** Establishes the invariant R = e^{2πis} and the η = ±1 symmetric construction; explicitly documents that the leap from the half-turn phase to anticommuting marks is not derived. This paper supplies the (e^{iπ})^{2s} composite reading absent there.

**Kauffman 2022.** Reviews Majorana fermions through the laws of form, connecting the mark calculus to fermionic structure. It addresses the representation of fermions, not the exchange-phase invariant, and contains no (2s)-fold half-turn power structure. The present claim is distinct and complementary.

**Ma and Zhang 2025.** Derive a Z₂ exchange phase from self-referential scattering via Riccati square roots and the spinor double cover in a quantum field theory framework. Their primitive is self-referential scattering in QFT; the primitive here is the re-entrant mark of the calculus of indications. Their result is confined to the Z₂ (boson/fermion) case; the (e^{iπ})^{2s} power structure for arbitrary s (anyons) and the e/π/R scalar-family unification are absent. The present claim is distinct: the derivation target is the re-entrant mark under linear discipline, not bare self-reference.

**Berry and Robbins 2017.** The geometric-phase construction of spin-statistics: exchange of two particles acquires the Berry phase, connecting statistics to geometry. The monodromy-power reading advanced here is conceptually adjacent (both trace the exchange phase to a geometric monodromy) but is formulated natively in the calculus of indications rather than in Hilbert-space geometry.

**Ahluwalia and Lee 2022.** Propose mass-dimension-three-half spinors as an evasion of the standard spin-statistics theorem. This is relevant to F2: the evasion targets the standard theorem statement, not the invariant R itself; the empirical falsifier above covers the general evasion class.

## 8. Conclusions

The exchange phase R = e^{2πis} is the (2s)-fold half-turn of the re-entrant mark: R = (e^{iπ})^{2s} = (−1)^{2s}. The boson/fermion dichotomy is the parity of 2s. The claim is scoped with an explicit status ladder: the arithmetic is established, the identification is a model, and the full logical derivation within the traced differential cohesive linear type theory of the treatise is a conjecture with concrete falsifiability conditions. If the derivation succeeds, e, π, and R form a single family of logical scalars of the re-entrant mark — fixed point, trace, and monodromy power — and the spin-statistics connection is the arithmetic of the half-turn. If it fails, the failure mode is precisely specified: the calculus cannot generate the exchange phase without importing it as an axiom.

## 9. Declarations

- **Funding:** This research received no external funding.
- **Conflicts of interest:** The author declares no conflicts of interest.
- **Data availability:** All source files, gate artifacts, and external-search evidence are deposited with this record and mirrored in the project repository (see provenance link).
- **Code availability:** The derivation is analytical; the arithmetic verification and citation-audit scripts are deposited as artifacts.
- **Ethics approval:** Not applicable.
- **Consent for publication:** Not applicable.
- **Author contributions:** R.B.Q.-G. conceived, derived, and wrote the paper.
- **Preprint policy:** This is a self-archived working paper; it has not been submitted for peer review.
- **Reproducibility:** Every numerical claim is independently recomputable from the stated elementary formulas; the citation audit re-verifies every bibliographic entry against live registries.

## References

- Ahluwalia, D. V., and C.-Y. Lee (2022). Spin-half bosons with mass dimension three-half: Evading the spin-statistics theorem. *Europhysics Letters*, 10.1209/0295-5075/ac97bd (+ erratum 10.1209/0295-5075/acabe2).
- Berry, M. V., and J. M. Robbins (2017). Indistinguishability for quantum particles: spin, statistics and the geometric phase. *A Half-Century of Physical Asymptotics and Other Diversions*, 10.1142/9789813221215_0008.
- Duck, I., and E. C. G. Sudarshan (1998). Toward an understanding of the spin-statistics theorem. *American Journal of Physics* 66(4), 284–303, 10.1119/1.18860.
- Kauffman, L. H. (2022). A Review of Majorana fermions and the laws of form. *Journal of Physics: Conference Series* 2197, 012001, 10.1088/1742-6596/2197/1/012001.
- Kitaev, A. (2006). Anyons in an exactly solved model and beyond. *Annals of Physics* 321(1), 2–111, 10.1016/j.aop.2005.10.005.
- Leinaas, J. M., and J. Myrheim (1977). On the theory of identical particles. *Il Nuovo Cimento B* 37, 1–23, 10.1007/BF02727953.
- Ma, H., and W. Zhang (2025). Self-Referential Scattering and the Birth of Fermions: Riccati Square Roots, Spinor Double Cover, and a Z₂ Exchange Phase. Zenodo, 10.5281/zenodo.17706898.
- Pauli, W. (1940). The Connection Between Spin and Statistics. *Physical Review* 58, 716, 10.1103/PhysRev.58.716.
- Quni-Gudzinas, R. B. (2026a). The Calculus of Re-Entrant Distinctions: A Unified Treatise on the Loop, the Tree, and the Constants of Self-Reference. Zenodo, 10.5281/zenodo.21908818.
- Quni-Gudzinas, R. B. (2026b). The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant. Zenodo, 10.5281/zenodo.21938971.
- Spencer-Brown, G. (1969). *Laws of Form*. George Allen and Unwin.
- Wilczek, F. (1982). Magnetic Flux, Angular Momentum, and Statistics. *Physical Review Letters* 48, 1144, 10.1103/PhysRevLett.48.1144.
- Joyal, A., R. Street, and D. Verity (1996). Traced monoidal categories. *Mathematical Proceedings of the Cambridge Philosophical Society* 119, 447–468, 10.1017/S0305004100074338.
