# Phase 0.2 — Independent Bin Table Re-Derivation

**Date:** 2026-07-18  
**Status:** Working notes — not final  
**Source:** Derived from Doc E cross-audit, re-argued independently against primary literature categories

---

## Methodology

For each sub-hypothesis, we independently re-derive the bin assignment by asking:

1. Is there a way to state this claim that generates a specific, lockable prediction with fewer free parameters than facts to explain?
2. If yes — what is the minimum theory-building step needed?
3. If no — is the obstacle contingent (theory not yet developed) or structural (the claim as stated is not operationalizable)?

The Doc E assignments serve as starting points but must be re-argued here.

---

## H1 — Helical Electron Internal Structure

**Claim:** The electron has internal helical structure at the Compton scale; Zitterbewegung is a real classical trajectory; electron = knotted photon.

**Disaggregation:** H1 actually contains three nested claims of increasing strength:
- H1a: Zitterbewegung is a real physical oscillation at frequency 2mc²/ħ (not just an operator artifact). `[Est]` — this is derivable from the Dirac equation and contributes to g=2.
- H1b: This oscillation corresponds to a classical helical trajectory in 3D space. `[Open]` — the Hestenes spacetime-algebra interpretation makes this claim; it is mathematically isomorphic to the Dirac equation but makes different ontological commitments. Not falsified, not established.
- H1c: The electron IS a knotted photon — the helix is a self-trapped photonic configuration, and 3D space is not fundamental. `[Blocked]` — spin-statistics theorem prohibits fermions from bosonic fields in 3+1D without additional structure.

**Bin assignment:** H1a is bin A (already tested — g-2 confirms Dirac structure). H1b is bin B (could be tested with a Compton-scale scattering prediction, but no such prediction exists yet). H1c is bin C (blocked by spin-statistics theorem — requires theorem-circumvention justification).

**Final bin for H1 as stated:** **B** — the most charitable interpretation (H1b) requires theory first. The strongest interpretation (H1c) is blocked. Neither is bin A.

**Path to bin A:** Produce an explicit Lagrangian for the "knotted photon" model; derive spin-1/2 statistics (not postulate); compute g-2 correction with no free parameters; lock prediction before comparing to CODATA.

---

## H2a — Photonic Vortex Solitons → Fermion Behavior

**Claim:** Photonic bound states in engineered media can exhibit fermion-like behavior (spin-1/2 statistics, exclusion-like effects).

**Assessment:** This is the strongest scientific claim in the entire cluster. Unlike H1c, it doesn't claim photons ARE fermions — it claims photonic systems can BEHAVE LIKE fermions under specific engineered conditions. This is a standard physics claim: "system X can simulate behavior of system Y in regime Z." Photonic quantum simulation is a real, active field.

**Falsifiable prediction:** A photonic vortex soliton transported around a closed loop in a synthetic-gauge-field lattice will accumulate a Berry phase of π (not 2π) if fermionic behavior is achieved. This is parameter-free. The experimental methodology exists (polariton interferometry, photonic lattice transport).

**Bin assignment:** **A** — claim is specific, testable, and the methodology exists. The prediction (Berry phase π vs 2π) is lockable before measurement.

**Caveat:** No demonstration of fermionic statistics in photonic systems currently exists in the literature. This is an open frontier — the test could fail, and the null result would be informative either way.

---

## H2b — Knot Invariants → Lepton Mass Ratios

**Claim:** The muon/electron and tau/electron mass ratios (~207 and ~3477) are predicted by knot invariants of the photonic configurations corresponding to each lepton generation.

**Assessment:** This fails the pre-registration rule on structural grounds. The model has: choice of knot family (a discrete parameter), choice of which invariant to map to mass (another discrete parameter), and any coupling constants in the energy functional (continuous parameters). Minimum degrees of freedom: ≥3. Facts to explain: 2 (m_μ/m_e, m_τ/m_e). Since DoF ≥ facts, agreement is guaranteed by construction.

**Could this escape bin C?** Only if a specific mapping is fixed by a principle independent of the masses — e.g., "energy is proportional to crossing number with no fitted coefficients; electron = trefoil (3 crossings), muon = knot with N crossings, tau = knot with M crossings; predict ratios as 3:N:M." This is specific enough to lock and test. But no such construction exists in the literature, and preliminary analysis suggests any simple crossing-number-to-mass mapping would produce integer ratios (3:5:7, 3:4:6, etc.) that don't match the observed non-integer ratios ~207 and ~3477.

**Bin assignment:** **C** — not falsifiable as posed. The "could this escape" scenario is noted but not yet realized.

---

## H3 — COTT/Invertible-Zero Arithmetic Advantage

**Claim:** A non-destructive algebra with an invertible zero (COTT/wheel theory) enables computation with energy dissipation below the Landauer limit or new algorithmic primitives.

**Assessment:** This decomposes into two sub-claims:

- H3a (dissipation): COTT circuits dissipate less energy than standard reversible logic.
- H3b (complexity): COTT enables new algorithmic primitives (e.g., factoring speedup).

**H3a analysis:** Standard reversible computing (Bennett, Toffoli, Fredkin) already approaches the Landauer limit in the adiabatic limit — this is established physics [Est]. COTT's "invertible zero" extends the algebra to include ∞ as an element. But standard reversible logic never encounters division by zero because its domain excludes it. The question is: does adding ∞ as a represented value change anything physical? The most likely answer is no — representing ∞ as a bit pattern doesn't change the thermodynamics of computation, which depend on physical state-space volume, not algebraic representation. The claimed "advantage" reduces to: "we represent 1/0 as ∞ rather than excluding it from the domain." But standard reversible logic already excludes undefined operations without thermodynamic cost (it's logically reversible, so it never needs to "erase" an undefined result — it just never generates one). This is most likely a category error [CE].

**H3b analysis:** Complexity classes are defined relative to specific computational models. Changing the algebra doesn't change the model unless it changes which operations are elementary. No peer-reviewed result demonstrates that wheel-theoretic arithmetic changes any complexity class boundary. This is most likely a category error [CE].

**Bin assignment:** **C** for the "advantage" claim. The underlying mathematics (wheel theory) is legitimate [Est], but the claimed physical/computational advantage over standard reversible logic is [Unsup] and likely [CE]. Resolve analytically per Doc D Phase 1.5.3.

---

## H4a — Ultrametric Signatures in Rydberg Spectra

**Claim:** Ultrametric/p-adic structure at the fundamental level would leave detectable signatures in the nearest-neighbor spacing distribution of highly-excited Rydberg atomic spectra.

**Assessment:** This claim conflates two independent questions:

- Q1: Do Rydberg atoms exhibit exotic spectral statistics? This is testable with existing methodology. Bin A.
- Q2: If exotic statistics are found, do they indicate ultrametric/p-adic pre-geometry? This requires a quantitative bridge from Planck-scale (~10¹⁹ GeV) effects to Rydberg-scale (~10⁻⁵ eV) observables — a 40-order-of-magnitude gap. No such bridge exists.

**Reframed test:** H4a can be run as "search for exotic spectral statistics in Rydberg atoms, agnostic about origin." Any deviation from Poisson/Wigner–Dyson would be interesting regardless of its source. This is bin A. But interpreting such a deviation as evidence for ultrametric pre-geometry is bin C — the bridge principle is absent.

**Bin assignment:** **A for the spectroscopy; C for the ultrametric interpretation.** The audit report must clearly separate the measurement from the interpretation.

**H4a scale estimate (to be computed in Phase 1.6):** If ultrametric structure exists at Planck length l_P ≈ 1.6×10⁻³⁵ m, the characteristic energy scale is E_P ≈ 1.2×10¹⁹ GeV. Rydberg atoms probe energy differences of ~10⁻⁵ eV (for n~100). The ratio is ~10⁴⁰. For Planck-scale discreteness to produce structure at eV scales, an amplification mechanism spanning 40 orders of magnitude is required. Candidate mechanisms: fractal/self-similar scaling, conformal fixed points, or scale-invariant critical phenomena — but none are specified by the claim. Until one is, the interpretation is unwarranted.

---

## H4b — Adelic Product Formula for α

**Claim:** α = ∏_p p^(−v_p) with valuations v_p determined by an independent principle (not fitted to α).

**Assessment:** "With one free valuation v_p per prime" is the problem. There are infinitely many primes. Matching α to 12 significant digits costs ≤12 valuations (using primes ≤37). This is equivalent to fitting 12 free parameters to 12 observable digits — the "test" cannot fail because the model has enough freedom to match any target.

**What the adelic product formula actually is (number theory context):** For any nonzero rational x, ∏_v |x|_v = 1, where the product runs over all places (real and p-adic). This is a theorem about the absolute values of rational numbers. It does not generate physical constants; it relates the values a number takes at different places. The idea that α might be an adelic norm is mathematically legitimate (any real number is), but has no predictive content unless the valuations are fixed independently.

**Could this escape bin C?** Only if v_p are fixed by an independent principle — e.g., "v_2 = 2 (from the quadratic Casimir of SU(2)), v_3 = 3 (from SU(3)), v_5 = 5 (from SO(10))..." or something similarly principled. No such construction exists in the surveyed literature (Volovich, Vladimirov, Freund–Olson).

**Bin assignment:** **C** — not falsifiable as posed.

---

## H5 — Reversible Logic at Landauer Limit

**Claim:** A reversible logic chain can approach kT ln 2 energy dissipation per logically irreversible bit.

**Assessment:** This is established physics [Est]. Bennett (1973) proved it theoretically. Bérut et al. (Nature 2012) confirmed it experimentally. Multiple adiabatic CMOS and superconducting demonstrations exist.

**Relationship to core claim:** H5 is independent of the photon-as-substrate hypothesis. It doesn't test any of the other sub-hypotheses. It validates that reversible computing works — which is good science, but doesn't distinguish the project's core claim from standard thermodynamics.

**Bin assignment:** **A** — already tested. A literature-verification task suffices; no new experiment needed.

---

## Summary Bin Table (Independently Re-Derived)

| # | Claim | Bin | Reasoning |
|---|---|---|---|
| H1 | Helical electron internal structure | **B** | H1a [Est], H1b [Open/B], H1c [Blocked]. Most charitable interpretation (H1b) requires theory. |
| H2a | Photonic solitons → fermion behavior | **A** | Specific, parameter-free prediction (Berry phase π vs 2π). Methodology exists. No demonstration yet. |
| H2b | Knot invariants → mass ratios | **C** | DoF ≥ facts. No parameter-free mapping exists. Curve-fitting fallacy. |
| H3 | COTT advantage claim | **C** | [CE] — algebraic extension doesn't change computational thermodynamics without physical mechanism. |
| H4a | Rydberg spectral statistics | **A*/C** | Spectroscopy: bin A. Ultrametric interpretation: bin C (no bridge principle spanning 40 orders of magnitude). |
| H4b | Adelic formula for α | **C** | One free valuation per prime. Any constant can be matched. Not falsifiable. |
| H5 | Reversible logic at Landauer limit | **A** | [Est] — already confirmed experimentally. Independent of core claim. |

---

## Agreement with Doc E

This independent re-derivation confirms the Doc E bin assignments for all seven claims. No revision needed. The assignments are:

- **H1: B** (confirmed — Doc E had B)
- **H2a: A** (confirmed)
- **H2b: C** (confirmed)
- **H3: C** (confirmed)
- **H4a: A/C** (confirmed — Doc E flagged the scale problem)
- **H4b: C** (confirmed)
- **H5: A** (confirmed)

**Conclusion:** Bin table is stable. Proceed to audit rubric (0.3) and seed bibliography (0.4).
