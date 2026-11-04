---
modified: 2026-07-18T14:10:00Z
status: draft
parent-docs:
  - _26199153842.md  # Doc A: Vision
  - _26199155230.md  # Doc B: v1 Research Program
  - _26199155335.md  # Doc C: Experimental Tests
  - _26199155940.md  # Doc D: v2 Research Program
---

# Photonic Substrate Hypotheses for Emergent Spacetime: A Technical Audit Report

**Version:** Final (synthesized from Docs A–D and cross-audit)
**Date:** 2026-07-18
**Status:** Draft — human review pending

---

## Abstract

A cluster of informal claims — linking the photon's bosonic statistics to the non-fundamentality of 3D space, the electron's internal structure to knotted electromagnetic configurations, non-destructive (COTT) arithmetic to thermodynamic advantages over standard reversible computing, and ultrametric/adelic number-theoretic structure to low-energy electron physics — was advanced in a visionary essay (Doc A) and subsequently subjected to two methodological passes: a proposed literature-audit research program (Docs B/D) and a set of experimental test designs (Doc C). An independent cross-audit (this report) found that Doc A's **master claim** — "photons don't obey Pauli exclusion, therefore the primacy of 3D space is falsified" — is a logical non-sequitur. The master claim has been reformulated (endorsed by the project's author) as:

> The informational properties of quantum fields suggest that geometric spacetime is emergent, not fundamental — and photons, as the only freely-propagating massless boson with a natural two-state (qubit) polarization structure, are the natural elementary carriers in such an informational substrate.

Under this reformulated framing, this report audits five sub-hypotheses (H1–H5) against the existing peer-reviewed literature, classified using a bin system (A: testable now, B: needs theory first, C: not falsifiable as posed) and a pre-registration rule requiring parameter-sparse, locked predictions before any claim is treated as tested. The central finding is that **no strong ontological claim survives audit**: the representational/toy-model versions of several sub-claims have real, citable support within explicit domains of validity, but the upgrade from "this math can describe electron-like behavior in some regime" to "this is what an electron actually is, more fundamental than space" is not supported by any derivation surveyed, and in the case of H1 (spin-1/2 from spin-1 fields) is blocked by the spin-statistics theorem unless the model specifies which theorem assumption it circumvents.

---

## 1. The Reformulated Core Claim

### 1.1 What was wrong with the original

Doc A's master argument was:

> P1: Photons are bosons → they don't obey Pauli exclusion.
> P2: Therefore they don't exclusively occupy 3D physical space.
> C: Therefore the primacy of 3D physical space is falsified in favor of a pre-geometric, information-theoretic foundation.

This is a non-sequitur. Bosons exist in standard 3+1D quantum field theory; the fact that multiple bosons can occupy the same quantum state does not mean space is emergent — it means the concept of "occupying space" applies differently to bosons than to fermions. Pauli exclusion is a property of fermionic wavefunctions under antisymmetrization, not a definition of what space *is*. The original argument conflates "space as a principle of exclusive occupancy" (a macroscopic intuition) with "space as a physical entity" (a structure in general relativity and quantum field theory). Falsifying the *intuition* does not falsify the *entity*.

### 1.2 The corrected formulation

> The informational properties of quantum fields suggest that geometric spacetime may be emergent in some quantum gravity frameworks — and photons, as the only freely-propagating massless boson with a natural two-state (qubit) polarization structure, are the natural elementary information carriers in such a substrate.

This formulation is:

- **Logically valid:** It asserts a hypothesis ("photons are natural carriers *if* spacetime is emergent"), not a deduction. It does not claim that bosonic statistics prove emergence.
- **Connected to real physics:** The entanglement-entropy/geometry connection (Ryu–Takayanagi), holographic tensor-network models, and "it from bit" programs are all legitimate research frontiers that motivate the question.
- **Falsifiable in principle:** If emergent-spacetime frameworks consistently fail to give photons a privileged role (e.g., if emergent geometry treats all fields symmetrically), the "natural carriers" claim is weakened.
- **Nuanced about "only":** Gluons are also massless spin-1 bosons with two polarization states, but they are confined below the QCD scale (~200 MeV). At low energies, photons are the *only freely-propagating* massless boson. This nuance matters: if confinement is an essential feature of non-abelian gauge fields, then the photon's freedom is itself information-theoretically significant. The reformulation uses "freely-propagating" to capture this.

### 1.3 What this report audits

The reformulated claim decomposes into five sub-hypotheses (H1–H5), four inherited from Docs B/D and one added. This report audits each against:

- The peer-reviewed literature (as known to this audit)
- The spin-statistics theorem and other theorem-level constraints
- The pre-registration rule (see §2)
- The bin classification system (see §2)

---

## 2. Methodology

### 2.1 Bin classification

Every claim is assigned one of three bins, following Doc D:

| Bin | Definition |
|---|---|
| **A** | Genuinely testable *now*: a parameter-sparse (or parameter-free) prediction can be derived and locked before comparison to data. |
| **B** | Requires prior theoretical work: the methodology for testing is sound, but no lockable prediction currently exists. |
| **C** | Not falsifiable as posed: the comparison procedure has enough tunable freedom to match virtually any target. Claims in this bin are *excluded* from the "tests" section of this report and reported as open problems. |

### 2.2 Pre-registration rule

Following Doc D, no comparison between a model's output and data counts as a test unless:

1. The exact functional form or algorithm producing the prediction is fixed *before* comparison, with no free parameters left to be chosen after seeing the target value.
2. The number of free parameters is **smaller** than the number of independent facts it must explain.
3. The locked prediction is timestamped before comparison.

### 2.3 Evidence tags

Within each audit, claims are tagged:

| Tag | Meaning |
|---|---|
| `[Est]` | Established in the peer-reviewed literature, with citation. |
| `[Open]` | Known open problem; state of the art quantified. |
| `[Unsup]` | Not supported by existing derivations or evidence. |
| `[Blocked]` | Inconsistent with or blocked by a known theorem, unless model specifies which assumption is circumvented. |
| `[CE]` | Category error: the claim conflates concepts from different domains in a way that invalidates the argument. |

---

## 3. H1 — Helical Electron Internal Structure

### 3.1 The claim

The electron has internal structure at the Compton scale (λ_c ≈ 2.4×10⁻¹² m), characterized by a helical null curve — the Zitterbewegung — with a pitch-to-circumference ratio equal to α ≈ 1/137. This internal motion is a "self-trapped photon," and the electron's mass, charge, and magnetic moment emerge from this helical geometry.

### 3.2 What is established

1. **Zitterbewegung is a real feature of the Dirac equation** `[Est]`. The velocity operator in the Dirac theory has eigenvalues ±c, and the expectation value of the position operator precesses at frequency ω = 2mc²/ħ. This was derived by Schrödinger in 1930 and is a standard result in relativistic quantum mechanics (Sakurai, *Advanced QM*, §3.3). However, the "motion" is a quantum interference effect between positive- and negative-energy states — it occurs in the algebra of operators, not as a classical trajectory in 3D space. The Compton wavelength is the amplitude of this operator oscillation. This is physically real (it contributes to the electron's magnetic moment) but it is not a *classical helix*.

2. **Classical EM knot solitons exist** `[Est]`. Rañada (1989) and Trueba & Rañada (1996) constructed Hopf-fibration solutions to Maxwell's equations in vacuum that carry topological charge — linked electric and magnetic field lines. These are exact solutions of the source-free Maxwell equations and propagate at c. Bouwmeester, Irvine, et al. (later extended) demonstrated that knotted EM fields can be realized experimentally at microwave frequencies. However, these are *massless* configurations — they propagate at c, have no rest frame, and carry integer topological charge (linking number), not spin-1/2.

3. **Spinning soliton models of the electron exist** `[Est]`. The Kerr–Newman solution of Einstein–Maxwell theory has the same mass, charge, and angular momentum as the electron when parameters are set to e, m_e, and ħ/2. Burinskii (2000–present) has extensively studied the Kerr–Newman geometry as a "spinning soliton" model of the electron, showing that its gyromagnetic ratio g=2 matches the Dirac value. The Kerr–Newman solution has a ring singularity that can be interpreted as a closed null curve — geometrically, a "helix" at the speed of light. This is the closest thing in the literature to the "helical electron" of Doc A.

### 3.3 The gap: spin-statistics

The spin-statistics theorem (Pauli 1940, Lüders & Zumino 1958, extended by Weinberg) states: **in any 3+1D relativistic quantum field theory satisfying locality, Lorentz invariance, and positivity of energy, integer-spin fields must obey Bose statistics and half-integer-spin fields must obey Fermi statistics.**

This is a **theorem**, not an empirical observation. It means:

- Any model that claims to derive a spin-1/2 electron from a spin-1 photonic field **must specify which assumption of the spin-statistics theorem it violates**.
- The Kerr–Newman soliton model doesn't do this — it starts with a *classical* solution (where spin-statistics doesn't apply), and the "spin" comes from the intrinsic angular momentum of the Kerr geometry, which is a classical parameter. Quantizing this object to get fermionic statistics is the hard part, and no derivation surveyed closes this gap.
- Models that successfully produce fermions from bosons in other contexts (e.g., skyrmions in 2+1D, anyons, or fermionization of bosons in 1+1D) all work in *different spacetime dimensions* where the spin-statistics theorem has different content. The 3+1D case is uniquely restrictive.

**Verdict:** The representational claim — "the electron can be modeled as a spinning soliton with a closed null-curve geometry" — has real literature support (Burinskii's Kerr–Newman program). The ontological claim — "the electron *is* a knotted photon" — is `[Blocked]` by the spin-statistics theorem unless the model specifies which assumption is circumvented. No such specification exists in the surveyed literature.

### 3.4 What would be required to move H1 from bin B to bin A

- An explicit Lagrangian (or Hamiltonian) for the "knotted photon" field, with a demonstrated topological sector that:
  - Has charge ±e, mass m_e, spin-1/2 under the Lorentz group.
  - Obeys Fermi statistics (anticommutation relations) — derived, not postulated.
  - Reduces to the Dirac equation in the low-energy limit.
- From this Lagrangian, derive a numeric prediction for g-2 with no free parameters beyond those already fixed by e, m_e, ħ.
- Lock the prediction before comparing to the CODATA g-2 value.

**Current status:** No such Lagrangian exists. Bin B.

### 3.5 The g-2 test is sound methodology, but premature

The experimental sensitivity for electron g-2 is extraordinary: the measured value agrees with Standard Model QED to ~10⁻¹³ (Hanneke et al., 2008; Fan et al., 2023). Any helical correction to the vertex function must produce a deviation at or below this level to be consistent with existing data. This means:

- The helical model must produce a number at ~10⁻¹³ precision.
- If it produces a correction *larger* than 10⁻¹³, it's already falsified by existing data (unless the correction has been hidden by an unlikely cancellation).
- If it produces a correction *smaller*, it's currently untestable.

Without an explicit Lagrangian, we can't evaluate which case applies. The g-2 test is well-posed but waits on theory.

---

## 4. H2 — Photons as the Substrate of Matter

### 4.1 H2a: Photonic vortex solitons with fermion-like behavior `[Bin A]`

**Claim:** It should be possible to create matter-like behavior from purely photonic systems in the laboratory, without invoking fermions.

**Literature status:**

- Photon-photon interactions in nonlinear media are a real, active experimental field `[Est]`. Rydberg-EIT media (Peyronel et al., *Nature* 2012) produce effective photon-photon interactions strong enough to observe photon blockade — the optical analog of Coulomb blockade, where one photon prevents a second from entering a medium. Polariton Bose–Einstein condensates (Kasprzak et al., *Nature* 2006) demonstrate collective quantum behavior in photonic systems.
- Synthetic gauge fields for photons are experimentally realized `[Est]`. Topological photonic lattices (Ozawa et al., *Rev. Mod. Phys.* 2019; Hafezi et al.) exhibit protected edge states and effective magnetic fields for light. However, these produce *bosonic* topological phases — the underlying particles remain bosons.
- **No demonstration of fermionic statistics from photonic systems exists** `[Open]`. The claim requires two steps: (a) create a self-trapped photonic soliton (demonstrated in some regimes), and (b) demonstrate that this soliton exhibits spin-1/2 behavior under exchange (not demonstrated). Step (b) is the hard part: Bose-Fermi duality is known in 1+1D (bosonization) and in certain 2+1D systems (flux attachment), but not in 3+1D for fundamental fields.

**Test design (per Doc C, refined):**

A polariton or photonic-lattice experiment could measure a quantized Berry phase or spin-locking ratio under adiabatic transport of a photonic vortex soliton. The prediction: a Berry phase of π (sign change under 2π rotation, as for a spin-1/2 object) rather than 2π (as for a spin-1 object). This prediction is parameter-free. It can be locked before measurement.

**Expected outcome:** Based on existing literature, the null result (no fermionic Berry phase) is more likely than discovery. But the experiment is genuinely runnable and would be informative either way. Bin A.

### 4.2 H2b: Knot invariants predict lepton mass ratios `[Bin C]`

**Claim:** If electrons, muons, and taus are topologically distinct knots in the photon field, the model must predict m_μ/m_e ≈ 207 and m_τ/m_e ≈ 3477 from knot invariants.

**Why bin C:** This fails the pre-registration rule on multiple counts:

1. **Degrees of freedom exceed facts to explain.** Two numbers must be predicted. The "model" has: choice of knot family (trefoil, figure-eight, etc.), choice of which knot invariant to use (Alexander, Jones, HOMFLY-PT polynomials), choice of energy functional, and any coupling constants in that functional. That is at minimum 3–4 degrees of freedom to fit 2 numbers. Agreement is guaranteed by construction, not evidence.

2. **Historical precedent is discouraging.** The idea that particle masses are determined by knot topology dates to Kelvin's vortex-atom theory (1867) and has been periodically revived (Jehle 1971, Finkelstein's knot-theoretic preon models, Bilson-Thompson's braided ribbon model 2005). None of these programs have produced parameter-free predictions for the lepton mass ratios that matched observation without post-hoc fitting.

3. **Even if a parameter-free mapping were found, it wouldn't distinguish "electrons are knots" from "knot invariants happen to produce these ratios."** The Pauli exclusion principle, spin, charge quantization, and coupling to the weak interaction are all unexplained by knot topology alone — they require additional structure beyond "this is a knot."

**What would count as a test:** Fix *before* comparison:
- A specific knot diagram for each lepton generation, chosen by a principle independent of the masses.
- An energy functional with zero free coefficients — e.g., energy proportional to crossing number.
- A prediction for m_μ/m_e and m_τ/m_e from this locked setup.

No such construction exists. Bin C until one does.

---

## 5. H3 — COTT / Invertible-Zero Arithmetic

### 5.1 The claim

A "non-destructive, total algebra" with an invertible zero (a wheel algebra, per Carlström 2004; COTT as a specific instance) can perform useful computation with energy dissipation below the Landauer limit and may enable new algorithmic primitives (e.g., factoring).

### 5.2 What is established

1. **Reversible computing is physically real** `[Est]`. Bennett (1973) showed that any computation can be performed reversibly, with energy dissipation arbitrarily close to zero in the adiabatic limit. The Landauer limit (kT ln 2 per bit erased) has been experimentally confirmed (Bérut et al., *Nature* 2012). This is standard thermodynamics of computation.

2. **Wheel theory / projective arithmetic is legitimate mathematics** `[Est]`. Extending a ring with an inverse for zero produces a wheel (Carlström 2004; also related to earlier projective-line constructions). This is rigorous. But mathematical existence ≠ physical relevance.

### 5.3 The gap: what does COTT add?

Standard reversible logic (Bennett, Toffoli, Fredkin, Fredkin–Toffoli gates) already provides total, lossless operations on finite bitstrings. Division by zero *never occurs* in standard reversible circuits because the domain of each gate is always well-defined — a Toffoli gate maps {0,1}³ → {0,1}³, and there is no "zero" to divide by. COTT extends this algebra to include ∞ as an element via the invertible zero construction. But the question is: **does this extension enable any operation that standard reversible logic cannot express?**

This is an **analytical question**, not an experimental one. Doc D's Phase 1.5.3 correctly identifies it: "show an operation COTT permits that standard reversible arithmetic does not."

**Probable resolution:** Standard reversible arithmetic is already total on its domain, and its domain already excludes undefined operations (like 1/0). COTT's innovation is to *include* 1/0 = ∞ as a defined value, but standard reversible logic achieves totality by never generating the offending expression in the first place. The claimed "advantage" is likely a category error `[CE]`: it conflates "having a defined value for 1/0" (an algebraic property) with "enabling new physical operations" (a computational property). Unless a specific, physically realizable gate is described that uses the invertible zero to do something Bennett-style gates cannot, the advantage claim is vacuous.

### 5.4 The complexity-class claim

The suggestion that COTT might enable "new algorithmic primitives" (e.g., for factoring) is almost certainly a category error `[CE]`. Complexity classes (P, NP, BQP) are defined relative to standard models of computation. Introducing a new algebra doesn't change what's computable unless it changes which operations count as elementary — and even then, the Church–Turing thesis limits what's physically computable regardless of algebraic representation. No peer-reviewed result shows that wheel-theoretic arithmetic changes any complexity class boundary.

**Verdict:** The mathematical structure (wheel algebra) is legitimate `[Est]`. The claimed physical/computational advantage over standard reversible computing is `[Unsup]` and likely `[CE]`. H3 resolves to bin C for the advantage claim. H5 (see §7) captures the genuine physics (standard reversible computing, which is independent of COTT).

---

## 6. H4 — Ultrametric / Adelic Signatures

### 6.1 H4a: Rydberg spectral statistics `[Bin A for spectroscopy; Bin C for ultrametric connection]`

**Claim:** Ultrametric or p-adic structure at the fundamental level would leave detectable traces in the spacing statistics of highly excited Rydberg atomic spectra.

**Literature status:**

- Rydberg atoms are a well-developed experimental platform `[Est]`. Spectroscopy of Rydberg states reaches resolution sufficient for quantum-chaos studies (e.g., the diamagnetic Kepler problem in strong magnetic fields, where the transition from regular to chaotic spectral statistics is observed — Wintgen & Friedrich, *Phys. Rev. Lett.* 1986).
- Spectral statistics (nearest-neighbor spacing distributions) distinguish integrable systems (Poisson) from chaotic systems (Wigner–Dyson from random matrix theory) from intermediate cases (Brody distribution). This methodology is standard and model-independent `[Est]`.

**The scale problem:**

If ultrametric/p-adic structure exists at the Planck scale (~10¹⁹ GeV), the energy scale is ~40 orders of magnitude above Rydberg energies (~10⁻⁵ eV). For Planck-scale discreteness to produce detectable signatures in atomic spectra, an amplification mechanism spanning 40 orders of magnitude is required. No such mechanism is proposed in Doc A, C, or D. Without one, H4a is **not testing ultrametricity at the Planck scale** — it is testing whether Rydberg atoms exhibit any exotic spectral statistics at all, which is a legitimate but different question.

**Reframed test:** H4a can be run as "measure Rydberg spectral statistics and compare to known quantum-chaos predictions." Any deviation from Poisson/Wigner–Dyson would be interesting regardless of origin. But the *interpretation* of such a deviation as evidence for ultrametric/adelic pre-geometry is unwarranted without a quantitative model linking Planck-scale effects to eV-scale spectra. The test itself is bin A; the interpretation is bin C.

### 6.2 H4b: Adelic product formula for α `[Bin C]`

**Claim:** The fine-structure constant α can be expressed as an adelic product α = ∏_p p^(−v_p) with valuations v_p determined by an independent principle.

**Why bin C:** As Doc D correctly identifies, with one free valuation v_p per prime, any real constant can be represented to arbitrary precision. There are infinitely many primes; matching α to 12 digits costs at most 12 valuations. This is equivalent to fitting 12 free parameters to 12 digits — agreement is guaranteed, not evidence. The pre-registration rule requires that v_p be fixed by an independent principle *before* comparing to α. No such principle exists in the surveyed literature.

**What the adelic product formula actually is:** In number theory, the adelic product formula states ∏_v |x|_v = 1 for any nonzero rational x, where the product runs over all places (real and p-adic). This is a theorem about rational numbers and their absolute values — it doesn't *generate* physical constants. The idea that α = 1/137.035... might be expressed as an adelic norm is mathematically legitimate (any real number can be), but it has no predictive content unless the valuations are fixed independently.

**Verdict:** Interesting mathematical speculation, no physical content. Bin C.

---

## 7. H5 — Reversible Logic at the Landauer Limit `[Bin A, independent of core claim]`

### 7.1 The claim

A reversible logic chain can perform computation with energy dissipation approaching kT ln 2 per logically irreversible bit.

### 7.2 Literature status

This is **already established** `[Est]`:

- Landauer (1961) derived the thermodynamic cost of erasure: kT ln 2 per bit.
- Bennett (1973, 1982) proved that computation can be performed reversibly, avoiding this cost.
- Bérut et al. (*Nature* 2012) experimentally confirmed the Landauer limit using a colloidal particle in a double-well potential.
- Adiabatic CMOS and superconducting reversible logic (e.g., Younis & Knight, Frank, DeBenedictis) have demonstrated energy-per-operation near the thermal limit.

This is well-established physics, independent of COTT, independent of the photon-as-substrate hypothesis, and independent of any claim about emergent spacetime. It is bin A but doesn't test any of the other sub-hypotheses.

**Verdict:** `[Est]`. No new experiment needed. A literature-verification task (per Doc D) suffices.

---

## 8. Cross-Cutting Issues

### 8.1 The spin-statistics theorem barrier (affects H1, H2)

The spin-statistics theorem in 3+1D imposes a hard constraint: integer-spin fields → bosons; half-integer-spin fields → fermions. Any model claiming to derive a fermionic electron from a bosonic photon field must specify which theorem assumption it circumvents:

- **Locality?** If the "knot" is non-local (e.g., topological), the theorem may not apply. But then the model must explain why locality is violated at the Compton scale without contradicting existing tests of QED locality.
- **Lorentz invariance?** Possible but highly constrained — Lorentz violation bounds are at the ~10⁻²⁰ level from astrophysical tests.
- **3+1D?** If extra dimensions are invoked, the theorem may have different content. But then the model must explain why the effective 3+1D theory inherits spin-1/2.
- **Commutation relations?** If the field algebra is deformed (e.g., non-commutative geometry), the theorem's assumptions may not hold. The model must specify the deformation.

**Audit finding:** No peer-reviewed work surveyed specifies which assumption is circumvented for the specific case of a photonic-knot electron. The Kerr–Newman soliton literature (Burinskii) works in the *classical* regime where the theorem doesn't apply, and the quantization step that would confront the spin-statistics constraint is not performed in a way that yields fermionic statistics.

### 8.2 The H4a scale problem (affects H4a)

Planck-scale effects → Rydberg spectra requires 40 orders of magnitude of amplification. No mechanism proposed. Without one, H4a is "exotic spectral statistics search" but not "test of ultrametric pre-geometry." This should be stated explicitly in any report claiming to test H4a.

### 8.3 The gluon nuance (affects reformulated core claim)

The reformulated claim says photons are "the only massless boson with two-state polarization structure." This is technically incorrect: gluons are also massless spin-1 bosons with two polarization states. The correction is crucial:
- Gluons *are* massless in the unconfined theory.
- They have two polarization states like photons.
- But they are **confined** — below ~200 MeV, they exist only in color-neutral bound states.

The correct formulation: "photons are the only *freely-propagating* massless boson with two polarization states in the low-energy universe." Confinement may itself be information-theoretically significant: if non-abelian gauge fields inevitably self-confine while abelian ones don't, the photon's freedom is a structural fact about the universe, not an accident. This refinement *strengthens* the reformulated claim rather than weakening it.

### 8.4 The psychological/epistemological claim (independent of physics)

Doc A's argument that human spatial intuition is "fermion-biased" — that we model space as exclusive occupancy because our bodies are made of fermionic matter — is the most original claim in Doc A and the only one that doesn't require breaking the spin-statistics theorem. It is not physics; it is cognitive science / philosophy of perception. It is independently testable through:
- Cross-species comparisons (do organisms with different dominant sensory modalities model space differently?).
- Developmental psychology (at what age do children acquire "exclusive occupancy" as a spatial primitive?).
- Cross-cultural spatial cognition (do all human cultures converge on 3D exclusive-occupancy space as the default?).

This claim falls outside the scope of a physics audit but is flagged here as independently interesting and worthy of pursuit in a separate project.

---

## 9. Curve-Fitting Audit Appendix

Per Doc D's requirement, this appendix documents every place in the prior documents where a test was proposed that fails the pre-registration rule.

### E1. H2b — Knot invariants → lepton mass ratios (Doc C, §2)

**Problem:** The "test" says: take a knot-to-mass mapping, compute m_μ/m_e and m_τ/m_e, see if they match 207 and 3477. But:
- The knot family is unspecified.
- The energy functional and its coupling constants are unspecified.
- With ≥2 free parameters to fit 2 numbers, this procedure always "succeeds."

**Resolution:** Reclassified bin C. Report states plainly: no parameter-free mapping exists.

### E2. H4b — Adelic product formula for α (Doc C, §4)

**Problem:** α = ∏_p p^(−v_p) with valuations v_p — one free parameter per prime. Matching α to 12 digits is guaranteed with ≤12 primes. The "test" can't fail.

**Resolution:** Reclassified bin C. Report states plainly: no independent principle fixing valuations exists.

### E3. H1 g-2 "test" (Doc C, §1)

**Problem:** Doc C says "compute corrections to the QED vertex from helical geometry and compare to measured g-2." But no Lagrangian, no vertex function, no computation exists. This is a task description, not a prediction. It "tests" a theory that hasn't been specified — it can neither pass nor fail because there's nothing to compare.

**Resolution:** Retained as a sound *methodology* (g-2 is a good test target) but classified as bin B — requires theory first. Not run in this audit.

---

## 10. Final Verdict Table

| # | Claim | Bin | Verdict | Key constraint |
|---|---|---|---|---|
| **Core** | Photons are natural information carriers in emergent-spacetime frameworks | — | `[Open]` — plausible hypothesis, logically valid under reformulation | Requires emergent-spacetime framework to be specified |
| **H1** | Electron has helical internal structure at Compton scale | **B** | `[Est]` — Zitterbewegung is real. `[Blocked]` for ontological "knotted photon" claim | Spin-statistics theorem |
| **H2a** | Photonic vortex solitons can exhibit fermion-like behavior | **A** | `[Open]` — real experimental frontier; no fermionic behavior demonstrated yet | Requires quantized Berry phase π prediction, locked before measurement |
| **H2b** | Knot invariants predict lepton mass ratios | **C** | `[Unsup]` — no parameter-free mapping exists; curve-fitting fallacy | Pre-registration rule: fewer parameters than facts required |
| **H3** | COTT arithmetic beats standard reversible computing | **C** | `[Unsup]` / `[CE]` — advantage over Bennett-style reversible logic not demonstrated; complexity-class claim likely category error | Analytical resolution needed before any hardware |
| **H4a** | Ultrametric signatures in Rydberg spectra | **A** (spectroscopy) / **C** (ultrametric connection) | `[Open]` — spectroscopy is runnable; ultrametric interpretation unquantified | 40-order magnitude scale gap without amplification mechanism |
| **H4b** | Adelic product formula reproduces α | **C** | `[Unsup]` — valuations are free parameters; curve-fitting fallacy | Requires independent principle fixing valuations |
| **H5** | Reversible logic approaches Landauer limit | **A** | `[Est]` — experimentally confirmed; independent of core claim | Literature verification sufficient |

---

## 11. What Would Need to Be True

For any of the strong ontological claims to survive a rigorous audit, the following conditions would need to be met:

### For H1 (helical electron as literal description):
1. A Lagrangian exists for a spin-1 field with a topological soliton sector.
2. The soliton has spin-1/2 under the Lorentz group **and** obeys Fermi statistics — derived, not postulated.
3. This requires specifying which assumption of the spin-statistics theorem is circumvented (locality, Lorentz invariance, field algebra, or 3+1D spacetime dimension).
4. The effective low-energy theory matches the Dirac equation with the observed e, m_e, and g-2 to current precision (~10⁻¹³).
5. The same Lagrangian, in different topological sectors, reproduces the muon and tau with the correct mass ratios.

**Status:** None of these conditions are met in the surveyed literature.

### For H2b (mass ratios from knot invariants):
1. A specific knot family and energy functional is fixed by a principle independent of the target masses.
2. The energy functional has zero free parameters.
3. The computed mass ratios match observation.

**Status:** No such construction exists.

### For H3 (COTT advantage over standard reversible logic):
1. A specific gate-level operation is described that uses the invertible zero.
2. This operation cannot be expressed in Bennett-style reversible logic.
3. The operation is physically realizable (maps to real hardware).

**Status:** No such operation has been demonstrated.

---

## 12. Summary

This audit finds a consistent pattern across all five sub-hypotheses:

| What the evidence supports | What the evidence does not support |
|---|---|
| "Zitterbewegung is a real feature of the Dirac electron" | "The electron IS a knotted photon — falsifying the primacy of space" |
| "Classical EM knot solitons exist and can be realized experimentally" | "These solitons explain spin-1/2, charge quantization, or lepton generations" |
| "Photonic platforms exhibit rich many-body physics (blockade, condensation, topology)" | "Purely photonic systems can reproduce fermionic statistics in 3+1D" |
| "Reversible computing approaches the Landauer limit, confirming Bennett's theory" | "COTT's invertible zero enables operations beyond standard reversible logic" |
| "p-adic and adelic mathematics are rigorous formalisms" | "Adelic structures are physically present in low-energy electron observables" |
| "The fine-structure constant α remains a deep puzzle in physics" | "α is computable from an adelic product formula without free parameters" |

**The reformulated core claim — "photons are natural information carriers in emergent-spacetime frameworks" — is a legitimate, interesting hypothesis that motivates genuine research questions.** It correctly identifies photons' unique properties and connects them to active research programs (holography, entanglement-geometry, it-from-bit). The upgrade from "motivating hypothesis" to "established fact" or "falsification of space" is where the original documents overreached, and this audit has mapped precisely where.

The value of this audit is not in debunking the vision — much of which is connected to real, interesting physics — but in producing a defensible map of what is established, what is open, and what is rhetorical extrapolation. That map, in the form of the verdict table above, is the deliverable.

---

## References (Primary sources audited)

- Bennett, C.H. (1973). "Logical reversibility of computation." *IBM J. Res. Dev.*
- Bennett, C.H. (1982). "The thermodynamics of computation — a review." *Int. J. Theor. Phys.*
- Bérut, A. et al. (2012). "Experimental verification of Landauer's principle." *Nature* 483, 187–189.
- Burinskii, A. (2000–2023). Series on Kerr–Newman geometry as electron model. *Phys. Rev. D*, *Grav. Cosmol.*, *J. Phys. A*.
- Carlström, J. (2004). "Wheels — on division by zero." *Math. Structures Comput. Sci.*
- Hestenes, D. (1990). "The Zitterbewegung interpretation of quantum mechanics." *Found. Phys.*
- Irvine, W.T.M. & Bouwmeester, D. (2008). "Linked and knotted beams of light." *Nature Phys.*
- Landauer, R. (1961). "Irreversibility and heat generation in the computing process." *IBM J. Res. Dev.*
- Ozawa, T. et al. (2019). "Topological photonics." *Rev. Mod. Phys.* 91, 015006.
- Pauli, W. (1940). "The connection between spin and statistics." *Phys. Rev.* 58, 716.
- Rañada, A.F. (1989). "A topological theory of the electromagnetic field." *Lett. Math. Phys.*
- Ryu, S. & Takayanagi, T. (2006). "Holographic derivation of entanglement entropy." *Phys. Rev. Lett.*
- Trueba, J.L. & Rañada, A.F. (1996). "The electromagnetic helicoid." *Eur. J. Phys.*
- Vladimirov, V.S., Volovich, I.V., & Zelenov, E.I. (1994). *p-Adic Analysis and Mathematical Physics.*
- Weinberg, S. (1995). *The Quantum Theory of Fields*, Vol. I, §5.7 (spin-statistics theorem).
