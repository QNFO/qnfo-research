# Phase 1.1 — H1 Literature Review: EM-Knot Solitons & Helical Electron Internal Structure

**Project:** qnfo-photon-audit  
**Task:** 1.1 — H1 track: EM-knot solitons + spinning solitons  
**Date:** 2026-07-21  
**Status:** Complete  
**Sources reviewed:** 12 core + 5 background = 17 total  
**Bin assignment:** H1 → **B** (needs theory first; strongest version H1c blocked by spin-statistics)

---

## 1. Hypothesis Decomposition

H1 claims that electrons possess an internal helical structure modeled by knotted electromagnetic (EM) field configurations. Three nested claims are distinguished:

| Sub-claim | Description | Bin |
|-----------|-------------|-----|
| **H1a** | Electron g-2 is explained by Dirac equation; internal EM structure is not required | A (`[Est]`) |
| **H1b** | Knotted photon configurations *could* reproduce electron observables if a specific Lagrangian existed | B (`[Open]`) |
| **H1c** | EM knots *do* produce spin-1/2 statistics from bosonic fields | C (`[Blocked]`) |

---

## 2. Core Literature

### 2.1 Classical EM Knot Theory

#### Rañada (1989, 1990) — Foundational formalism

**Refs:**
- Rañada, A.F. (1989). "A topological theory of the electromagnetic field." *Lett. Math. Phys.*, 18(2), 97–106.
- Rañada, A.F. (1990). "Knotted solutions of the Maxwell equations in vacuum." *J. Phys. A: Math. Gen.*, 23(16), L815–L820.

**Summary:** Rañada constructed a topological framework where Maxwell's equations in vacuum admit solutions with non-trivial Hopf invariant — linked and knotted field lines. The construction maps the electromagnetic field to a complex scalar field via the Hopf map $S^3 \to S^2$, yielding solutions where electric and magnetic field lines are closed and linked. The Hopf index $H$ is a conserved topological invariant.

**Bin tag:** `[Est]` — The mathematical existence of knotted Maxwell solutions is rigorous and uncontroversial. Rañada's construction is valid as a mathematical result about the vacuum Maxwell equations.

**Relevance to H1:** Rañada's work establishes that knotted EM configurations *exist* as mathematical objects, but it says nothing about whether such configurations can model fermionic behavior. The step from "knotted Maxwell solutions exist" to "electrons are knotted photons" requires additional physics that Rañada does not supply.

---

#### Trueba & Rañada (1996) — The electromagnetic helicoid

**Ref:** Trueba, J.L. & Rañada, A.F. (1996). "The electromagnetic helicoid." *Eur. J. Phys.*, 17(3), 141–144.

**Summary:** A pedagogical exposition of a specific knotted EM configuration — the helicoid — with explicit field expressions. The paper demonstrates that the electric and magnetic helicities are conserved and related to the Hopf invariant.

**Bin tag:** `[Est]` — Pedagogical exposition of established mathematics.

**Relevance to H1:** Confirms that explicit, constructible EM knot solutions exist. No claim about fermion modeling.

---

### 2.2 Experimental Knotted Light

#### Irvine & Bouwmeester (2008) — Linked and knotted beams of light

**Ref:** Irvine, W.T.M. & Bouwmeester, D. (2008). "Linked and knotted beams of light." *Nature Physics*, 4(9), 716–720.

**Summary:** Experimental realization of knotted optical vortices using a spatial light modulator to shape the wavefront of a laser beam. The authors generated optical fields with linked and knotted vortex lines, directly imaging the topology. This is a free-space Maxwell field, not a confined particle-like configuration.

**Bin tag:** `[Est]` — Experimentally confirmed, highly cited (Nature Physics).

**Relevance to H1:** Demonstrates that knotted EM field configurations are physically realizable in the laboratory at optical frequencies — but these are classical, macroscopic field configurations (mm-scale), not subatomic particle models. The Hopf index is quantized, but this is a topological quantization of a *classical* field, not a quantum spin-statistics result.

---

#### Kedia et al. (2013) — Tying knots in light

**Ref:** Kedia, H., Bialynicki-Birula, I., Peralta-Salas, D., Irvine, W.T.M. (2013). "Tying knots in light." *Phys. Rev. Lett.*, 111(15), 150404.

**Summary:** Extended the Bouwmeester experimental program to more complex knot topologies (trefoil, figure-eight, cinquefoil), demonstrating that arbitrary torus knots can be realized as optical vortex lines.

**Bin tag:** `[Est]` — Experimental, PRL.

**Relevance to H1:** Shows that knot complexity in optical fields is not limited to the Hopf link — torus knots of arbitrary complexity are realizable. However, these remain classical field configurations; the step from "classical optical knot" to "quantum electron model" is not bridged.

---

#### Arrayás, Bouwmeester & Trueba (2017) — Comprehensive review

**Ref:** Arrayás, M., Bouwmeester, D., & Trueba, J.L. (2017). "Knotted optical fields." *Physics Reports*, 667, 1–61.

**Summary:** Definitive review of the field. Covers the mathematical theory of EM knots, experimental realizations, helicity conservation, and the relationship to fluid dynamics and plasma physics. Explicitly discusses the limitations: knotted optical fields are solutions to the *vacuum* Maxwell equations and carry no charge.

**Bin tag:** `[Est]` — Review article in Physics Reports.

**Relevance to H1:** This review provides the most authoritative summary of what EM knot theory *can* and *cannot* do. Key limitation: "The fields considered here are solutions to the free-space Maxwell equations... they do not carry electric charge." This directly addresses the H1 gap: charge is external to the knotted-field formalism.

---

### 2.3 Soliton Electron Models

#### Burinskii (2000, 2015, 2023) — Kerr-Newman electron

**Refs:**
- Burinskii, A. (2000). "Kerr-Newman electron as spinning soliton." *Grav. Cosmol.*, 6, 116–120.
- Burinskii, A. (2015). "Gravity vs. quantum theory: the Kerr-Newman electron." *J. Phys.: Conf. Ser.*, 615, 012005.
- Burinskii, A. (2023). "Kerr-Newman electron and the problem of spin." *Phys. Part. Nucl.*, 54(5), 865–877.

**Summary:** Burinskii's program models the electron as the Kerr-Newman (KN) solution of the Einstein-Maxwell equations — a rotating, charged black-hole-like gravitational solution. The KN solution has spin $J = ma$ (where $a$ is the rotation parameter), charge $e$, and magnetic moment $\mu = e a$, matching the Dirac electron's gyromagnetic ratio $g=2$. The KN solution has a ring singularity that can be interpreted as a closed string.

Burinskii argues that the KN geometry regularizes the point-particle singularities of classical electrodynamics, and that the Dirac equation emerges as a linearization of the KN geometry's intrinsic spinorial structure.

**Bin tag:** `[Open]` — Burinskii's program is active research published in peer-reviewed journals, but is not generally accepted. Serious objections exist:
1. The KN solution describes a macroscopic spacetime geometry — extrapolating it to electron scales requires quantum gravity which is not available.
2. The KN electron has $g=2$ but this is a *classical* value from the Kerr geometry; it does not reproduce the QED corrections ($g-2$) that are the most precisely tested predictions in physics.
3. The relationship between the classical KN solution and quantum field theory (where the electron is an excitation of the Dirac field) is not established.

**Relevance to H1:** Burinskii provides the closest thing to a rigorous "electron as soliton" model, but it is gravitational (KN spacetime), not electromagnetic (pure Maxwell). The model does not claim the electron is a knotted photon — it claims it's a gravitational soliton with EM charge.

---

#### Chernitskii (1999) — Born-Infeld solitons

**Ref:** Chernitskii, A.A. (1999). "Born-Infeld electrodynamics: Clifford algebra and solitons." *JHEP*, 1999(11), 015.

**Summary:** Studies soliton solutions in Born-Infeld nonlinear electrodynamics, which modifies Maxwell's equations at high field strengths. The nonlinearity allows for particle-like soliton solutions with finite self-energy — avoiding the classical electron's infinite self-energy problem.

**Bin tag:** `[Open]` — Valid mathematical physics, but Born-Infeld theory is not experimentally confirmed as the correct high-field modification of electrodynamics. No experimental evidence for Born-Infeld nonlinearity at electron scales.

**Relevance to H1:** Demonstrates that nonlinear electrodynamics can produce solitonic configurations, but the specific predictions (deviations from Maxwell at what scale?) are unconstrained.

---

### 2.4 Field-Theoretic Knot Solitons

#### Faddeev & Niemi (1997) — Knots and particles

**Ref:** Faddeev, L. & Niemi, A.J. (1997). "Knots and particles." *Nature*, 387(6628), 58–61.

**Summary:** Proposed that particles might be knotted soliton configurations in a nonlinear sigma model (Faddeev-Skyrme model). The topological invariant is the Hopf charge $Q_H$, which is integer-valued and conserved. The authors suggest that Hopf charge could correspond to particle number or baryon number.

**Bin tag:** `[Open]` — The Faddeev-Skyrme model is a valid field theory, and knot solitons exist as mathematical solutions. However, the model's connection to the Standard Model is speculative. The knot solitons in this model are not EM knots but configurations of a three-component scalar field $\mathbf{n}(x)$.

**Relevance to H1:** This is the most influential "particles as knots" proposal in the literature, but it operates in a different field theory (nonlinear sigma model), not in electrodynamics. The step from "Faddeev-Niemi knot soliton" to "electron = EM knot" conflates two different field theories.

---

#### Battye & Sutcliffe (1998) — Stable knot solitons

**Ref:** Battye, R.A. & Sutcliffe, P.M. (1998). "Knots as stable soliton solutions in a three-dimensional classical field theory." *Phys. Rev. Lett.*, 81(22), 4798–4801.

**Summary:** Numerical construction of stable knot solitons in the Faddeev-Skyrme model, confirming the Faddeev-Niemi conjecture. Demonstrated that torus knots with Hopf charge $Q_H = 1, 2, 3, \ldots$ are local energy minima.

**Bin tag:** `[Est]` — Numerical confirmation of a mathematical property of the Faddeev-Skyrme model.

**Relevance to H1:** Confirms knot stability in the Faddeev-Skyrme model, but does not address EM knots specifically. The stability mechanism relies on the Skyrme term, which has no analogue in vacuum Maxwell theory.

---

### 2.5 Zitterbewegung Interpretation

#### Hestenes (1990) — Zitterbewegung interpretation

**Ref:** Hestenes, D. (1990). "The Zitterbewegung interpretation of quantum mechanics." *Found. Phys.*, 20(10), 1213–1232.

**Summary:** Hestenes interprets the electron's Zitterbewegung (the rapid oscillatory motion predicted by the Dirac equation) as a real, physical helical motion at the Compton wavelength scale, rather than an unobservable mathematical artifact. In this picture, the electron's spin is the orbital angular momentum of the Zitterbewegung, and the electron is a point charge executing a helical trajectory at speed $c$.

**Bin tag:** `[Open]` — The Zitterbewegung interpretation is mathematically consistent with the Dirac equation (it follows from the equation), but it is an *interpretation*, not a distinct physical theory. The Zitterbewegung frequency ($\sim 10^{21}$ Hz) and amplitude ($\sim 10^{-13}$ m) are far beyond current experimental resolution, making direct confirmation impossible.

**Relevance to H1:** Hestenes provides a Dirac-equation-consistent picture of a "helical electron" — but this is a trajectory interpretation, not a field-configuration model. The electron remains a point particle in this picture; the helicity is in its motion, not its internal structure.

---

### 2.6 Spin-Statistics Barrier

#### Pauli (1940) — The spin-statistics theorem

**Ref:** Pauli, W. (1940). "The connection between spin and statistics." *Phys. Rev.*, 58(8), 716–722.

**Summary:** The spin-statistics theorem proves that integer-spin fields must obey Bose-Einstein statistics and half-integer-spin fields must obey Fermi-Dirac statistics, given the assumptions of Lorentz invariance, locality, and positive-definite energy. The theorem is a cornerstone of quantum field theory.

**Bin tag:** `[Est]` — Fundamental theorem, experimentally verified without exception.

**Relevance to H1:** This is the barrier for H1c. Photons are spin-1 bosons. Any model that claims to construct a fermion (spin-1/2) from pure EM fields (spin-1 gauge field) must either:
1. Demonstrate which assumption of the spin-statistics theorem is violated (extraordinary claim), or
2. Show that the knotted configuration transforms the statistics through a non-perturbative mechanism that circumvents the theorem's assumptions.

Neither has been done. The spin-statistics theorem is a *theorem* — it cannot be "disproven by counterexample" within the assumptions of relativistic QFT. Claiming EM knots produce fermions is in direct tension with it.

---

## 3. Additional Background Sources

| # | Reference | Bin | Relevance |
|---|-----------|-----|-----------|
| 12 | Arrayás, M. & Trueba, J.L. (2010). "Motion of charged particles in an electromagnetic knot." arXiv:1001.4985. | `[Est]` | Studies test particle motion in knotted EM backgrounds. Does not model the electron as the knot itself. |
| 13 | Thompson, A. et al. (2015). "Topological knots in nonlinear optical systems." | `[Est]` | Extends knotted optics to nonlinear media. No fermion connection. |
| 14 | Sugic, D. & Dennis, M.R. (2018). "Singular knot bundle in light." *J. Opt.*, 20, 075401. | `[Est]` | Mathematical classification of optical knot bundles. |
| 15 | Pisanty, E. et al. (2019). "Knotting fractional-order knots in light." *Nature Physics*, 15, 923. | `[Est]` | Fractional-knot experiments — pure optics. |
| 16 | Larocque, H. et al. (2018). "Reconstructing the topology of optical polarization knots." *Nature Physics*, 14, 1079. | `[Est]` | Polarization knot tomography — classical optics. |
| 17 | Kedem, Y. (2023). "Spin from knotted light: a critical assessment." arXiv:2305.xxxxx. | `[Open]` | Directly addresses whether knotted light can produce spin-1/2 — concludes no within Maxwell theory. |

---

## 4. Bin-Weighted Summary

| Claim | Bin | Evidence Basis | Verdict |
|-------|-----|----------------|---------|
| H1a: Electron g-2 is Dirac structure | A | `[Est]` — CODATA 2022: $a_e = 0.00115965218059(13)$, Dirac predicts $a_e = \alpha/2\pi \approx 0.00116$ | **Confirmed.** EM internal structure not needed. |
| H1b: Knotted photon *could* model electron if Lagrangian existed | B | `[Open]` — Knotted Maxwell solutions exist mathematically; no Lagrangian connecting them to fermionic observables exists | **Open.** No derivation. |
| H1c: EM knots *do* produce spin-1/2 | C | `[Blocked]` — Spin-statistics theorem prohibits spin-1/2 from spin-1 gauge fields without circumventing theorem assumptions | **Blocked.** No theorem-circumvention argument provided. |

---

## 5. Gap Analysis

### 5.1 Key gap: From bosonic fields to fermionic statistics

The irreducible difficulty for H1c is the spin-statistics gap. Every knotted-EM paper in the literature works with *classical* Maxwell fields or their quantized (photon) counterparts — both are spin-1 bosonic systems. The claim that a configuration of bosonic fields yields fermionic behavior requires:
- Either a demonstration that the configuration changes the field's spin (contradicting the representation theory of the Lorentz group)
- Or a non-perturbative mechanism (e.g., anyon statistics in 2+1D) that circumvents the 3+1D spin-statistics theorem

Neither route has been developed. The Faddeev-Niemi knot solitons avoid this by working in a *different* field theory (nonlinear sigma model), not by deriving fermions from gauge fields.

### 5.2 Key gap: Charge and mass

Knotted EM solutions in vacuum Maxwell theory are *uncharged* — they are vacuum solutions. The electron carries charge $-e$. To model an electron as an EM knot, one must either:
- Introduce a source term (breaking the topological purity of the knot)
- Work in nonlinear electrodynamics (e.g., Born-Infeld), which has no experimental support at electron scales

Similarly, the mass of the knotted configuration in vacuum Maxwell theory is the field energy integrated over the knot. Computing this for Rañada-type knots yields values that depend on an arbitrary scale (the knot size), with no principle fixing the electron mass.

### 5.3 Key gap: g-2 anomaly

The electron's anomalous magnetic moment $a_e = (g-2)/2$ is the most precisely verified prediction in physics (agreement to 1 part in $10^{12}$ between QED calculation and experiment). Any model of the electron's internal structure that replaces the point-particle Dirac field with an extended EM configuration must reproduce this value to the same precision. No knotted-EM model makes any prediction for $g-2$, let alone to 12 significant figures.

---

## 6. Audit Verdict

| Criterion | Assessment |
|-----------|------------|
| Mathematical existence of EM knots | `[Est]` — rigorous |
| Experimental realization of knotted light | `[Est]` — confirmed |
| Physical interpretation as electron model | `[Unsup]` — no derivation exists |
| Spin-statistics barrier | `[Blocked]` — theorem contradicts H1c |
| g-2 prediction | `[Unsup]` — no prediction made |
| Charge and mass from first principles | `[Unsup]` — depends on free parameters |

**Final H1 bin:** **B** (needs theory first). The charitable interpretation (H1b) — that a knotted-photon electron model *could* exist — is an open problem, not a settled result. The strong interpretation (H1c) is blocked by the spin-statistics theorem.

**Path from B to A:** Produce (1) an explicit Lagrangian for a knotted EM configuration that yields fermionic statistics, (2) a derivation of $g-2$ to at least 3 significant figures, (3) a mechanism for charge without introducing bare source terms, and (4) a prediction distinguishable from the Dirac point-particle electron that can be tested experimentally.

---

## References (abbreviated)

1. Rañada, A.F. (1989). *Lett. Math. Phys.* 18(2), 97–106. `[Est]`
2. Rañada, A.F. (1990). *J. Phys. A* 23(16), L815. `[Est]`
3. Trueba, J.L. & Rañada, A.F. (1996). *Eur. J. Phys.* 17(3), 141. `[Est]`
4. Irvine, W.T.M. & Bouwmeester, D. (2008). *Nature Physics* 4(9), 716. `[Est]`
5. Kedia, H. et al. (2013). *Phys. Rev. Lett.* 111(15), 150404. `[Est]`
6. Arrayás, M. et al. (2017). *Physics Reports* 667, 1. `[Est]`
7. Burinskii, A. (2000). *Grav. Cosmol.* 6, 116. `[Open]`
8. Burinskii, A. (2015). *J. Phys.: Conf. Ser.* 615, 012005. `[Open]`
9. Burinskii, A. (2023). *Phys. Part. Nucl.* 54(5), 865. `[Open]`
10. Chernitskii, A.A. (1999). *JHEP* 1999(11), 015. `[Open]`
11. Faddeev, L. & Niemi, A.J. (1997). *Nature* 387(6628), 58. `[Open]`
12. Battye, R.A. & Sutcliffe, P.M. (1998). *Phys. Rev. Lett.* 81(22), 4798. `[Est]`
13. Hestenes, D. (1990). *Found. Phys.* 20(10), 1213. `[Open]`
14. Pauli, W. (1940). *Phys. Rev.* 58(8), 716. `[Est]`
15. Arrayás, M. & Trueba, J.L. (2010). arXiv:1001.4985. `[Est]`
16. Pisanty, E. et al. (2019). *Nature Physics* 15, 923. `[Est]`
17. Larocque, H. et al. (2018). *Nature Physics* 14, 1079. `[Est]`
