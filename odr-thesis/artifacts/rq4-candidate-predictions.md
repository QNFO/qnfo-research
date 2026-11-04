# RQ4 Candidate Predictions

**Project:** odr-thesis | **Date:** 2026-08-03 | **Source:** Phase 4 + red-team v1 COM-2 remediation
**Purpose:** Concrete falsifiable predictions for the most under-researched RQ

---

## Summary

RQ4 ("Does this framework generate a testable Planck-scale prediction?") is the thesis's enabling constraint. Without at least one prediction that differs from standard QFT AND is testable with current/near-future experiments, RQ1-3 remain Philosophy, not Physics.

Five candidates ranked by testability (time to experimental confirmation):

| # | Name | Testability | Timeline | Prior Work |
|:--|:-----|:-----------|:---------|:-----------|
| P2 | Lorentz-violation dispersion from tree discreteness | **HIGH** | 2-5 yr (Fermi-LAT data exists) | Amelino-Camelia DSR, LIV |
| P1 | Compton-count quantization in UHECR GZK cutoff | **MEDIUM** | 5-10 yr (Auger) | GZK (1966), UHECR anomaly |
| P5 | Quasiparticle m* invariance null test | **MEDIUM** | 1-2 yr (PDG data exists) | Landau, quasiparticle extension |
| P3 | BT-tree scattering using Romanov-Rudin formalism | **LOW** | 10+ yr (requires new calculation) | Romanov-Rudin 1995 |
| P4 | Feynman = tensor network contraction on BT tree | **LOW** | 10+ yr (requires theory development) | p-adic AdS/CFT tensor networks |

---

## P2: Lorentz-Violation Dispersion from Tree Discreteness (★ HIGH)

### Claim
The BT tree's ultrametric distance breaks continuous Lorentz symmetry at Planck scale. The tree is (p+1)-valent, not isotropic — Poincaré invariance is an emergent symmetry in the Archimedean (IR) limit, not a fundamental one. This predicts a modified dispersion relation for particles:

\[ E^2 = p^2 c^2 + m^2 c^4 + \xi \cdot \frac{E^3}{m_P} \]

where ξ is a dimensionless O(1) parameter related to the tree's branching factor p.

### Test
Gamma-ray burst (GRB) photons of different energies arrive at different times due to the energy-dependent speed of light:
\[ v(E) \approx c \left( 1 - \xi \frac{E}{m_P} \right) \]

Fermi-LAT has already detected ~10⁴ GRBs with photon energies up to ~100 GeV. The Δt between high-energy and low-energy photons from the same burst constrains ξ:
- Current bound: ξ < O(10⁻²¹) from Fermi-LAT (GRB 090510, 31 GeV photon)
- If ξ ~ 10⁻²⁰ to 10⁻¹⁸: detectable with improved GRB timing or next-generation telescopes (CTA)

### Falsifiability
**This would be disconfirmed if** future GRB observations push the bound below ξ < 10⁻²² without detecting a signal — this would put the tree-discreteness prediction at a scale too fine for tree geometry to matter.

### Known Constraints
Amelino-Camelia's doubly-special relativity (DSR) and the LIV literature already constrain energy-dependent speed of light at O(10⁻²¹). The ODR prediction must distinguish itself from generic LIV: the tree-discreteness prediction is NOT a smooth power law — it has a threshold structure at p-adic prime boundaries (e.g., ξ(2) ≠ ξ(3) for 2-adic vs 3-adic tree). If the signal shows prime-dependent structure, it's tree-geometry, not generic LIV.

---

## P1: Compton-Count Quantization in UHECR GZK Cutoff (★ MEDIUM)

### Claim
The Greisen-Zatsepin-Kuzmin (GZK) cutoff is the energy at which ultra-high-energy cosmic rays (UHECR) interact with CMB photons to produce pions: E_GZK ~ 5×10¹⁹ eV. In the ODR framework, this energy is NOT a continuous threshold — it's a rational Compton count ratio between the proton mass and the CMB photon temperature. Sub-leading quantum corrections produce a set of preferred UHECR energies corresponding to small-denominator rational Compton-count ratios.

### Test
Analyze the UHECR energy spectrum from Pierre Auger Observatory for preferential clustering of events at predicted Compton-count rational energy multiples. The null hypothesis (continuous GZK) predicts a smooth cutoff; ODR predicts clustered structure at rational energy steps.

### Falsifiability
**This would be disconfirmed if** Auger data (with full statistics, ~10⁵ events) shows a smooth GZK cutoff with zero significant clustering at the predicted rational energy steps.

### Known Constraints
The GZK cutoff is observed but the transition region is noisy. The "ankle" feature in the cosmic ray spectrum (~5×10¹⁸ eV) might already be a structure signal — alternative models attribute it to galactic-extragalactic transition. An ODR analysis of the ankle as a Compton-count transition between two rational prime-factorization regimes is testable with existing Auger public data.

---

## P5: Quasiparticle m* Invariance Null Test (★ MEDIUM)

### Claim
Per the quasiparticle extension paper (qnfo2026quasiparticle, pending Zenodo DOI): "This characterization would be disconfirmed if a quasiparticle were found to have an invariant Compton count independent of the host material — i.e., if the effective mass m* were shown to be an invariant constant rather than a context-dependent parameter."

### Test
Systematic review of PDG, solid-state databases, and 2D materials literature: identify all reported quasiparticle effective masses. If ANY quasiparticle (phonon, magnon, electron hole, exciton, Cooper pair) is found to have m* that is IDENTICAL across ≥2 host materials with different lattice constants and compositions, the claim is disconfirmed.

### Status
- Known: electron m* in GaAs = 0.067×m_e; in Si = 0.19×m_e — different. [established]
- Known: All known quasiparticles have host-dependent m*. This is a NULL test that has held for ~90 years (since Landau 1930s). [established]
- Frontier: 2D materials (graphene, TMDs) and topological insulators may have exotic quasiparticles with near-universal m* — these are the target for disconfirmation.

### Falsifiability
**This would be disconfirmed if** a quasiparticle is found in a 2D material or topological phase whose effective mass is identical (±1%) between two chemically different host lattices. This is NOT a "never" prediction — it is testable and could be falsified by a single materials discovery.

---

## P3: BT-Tree Scattering Amplitude Using Romanov-Rudin (★ LOW)

### Claim
Romanov & Rudin (1995, "Scattering on the Bruhat-Tits tree. I," Phys Lett A, DOI 10.1016/0375-9601(94)00997-4) developed a scattering formalism on the BT tree for 1D problems. Extended to particle scattering with Compton-count vertex labels, this formalism would produce a Planck-scale correction to standard QFT scattering amplitudes: σ_BT = σ_QFT × (1 + δ_BT), where δ_BT ~ O(m/m_P) is the tree-geometry correction.

### Test
Compute Bhabha scattering (e⁺e⁻ → e⁺e⁻) on the BT tree using Romanov-Rudin formalism with Compton-count-labeled vertices. The predicted correction δ_BT distinguishes tree-geometry from standard radiative corrections.

### Dependency
This candidate DEPENDS_ON theoretical development that has not been done. The Romanov-Rudin formalism is for 1D problems; extending to 4D QFT is a substantial research program. This is a 10+ year candidate, not a 2-5 year one.

---

## P4: Feynman = Tensor Network Contraction on BT Tree (★ LOW)

### Claim
The Consilience Gate frontier question: "Can the Feynman diagram be reinterpreted as a tensor network contraction on the BT tree?" In the p-adic AdS/CFT program, the BT tree IS a tensor network — correlation functions are computed by contracting tensors at tree vertices. If Compton counts label the vertices (particle identities) and Feynman propagators correspond to tensor contractions along tree edges, every Feynman diagram is a tensor network.

### What This Would Predict
The structure of vertex corrections at a given order in perturbation theory would be constrained by the tree's branching geometry. Vertex functions at a p-adic prime p would have structure determined by the (p+1)-valency of the tree at that prime. This is NOT a numerically falsifiable prediction currently — it's a theoretical framework for deriving predictions from the tree.

### Status
Theory-development stage. The p-adic AdS/CFT tensor network formalism (Bhattacharyya et al. 2018-2021) provides the computational machinery; the Compton-count labelling of vertices is the ODR contribution. No concrete calculation exists yet.

---

## Priority Recommendation

For the thesis paper, present P2 (Lorentz-violation dispersion) as the PRIMARY candidate — it's the most testable, it has existing constraining data (Fermi-LAT), and it distinguishes ODR from both standard QFT (no LIV) and generic LIV (no prime-structured threshold effects).

P5 (quasiparticle null test) is the SECONDARY candidate — it's immediately testable from PDG data and provides a concrete falsifiability condition for RQ1.

P1, P3, and P4 are TERTIARY candidates — they need more development, but they demonstrate the framework's predictive scope beyond the core paper.
