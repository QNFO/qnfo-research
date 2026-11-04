# Phase 2: Literature Classification & KIF-18 Symmetry Template

**Project:** odr-thesis | **Date:** 2026-08-03 | **Phase:** 2 Complete

---

## Classification Matrix

28 papers classified across Source + Type + Tier + Falsifiability + RQ.

### Core (7 papers — directly address RQ, must cite)

| # | Title | Authors | Year | Source | DOI | RQ |
|:--|:------|:--------|:-----|:-------|:----|:---|
| C1 | Ontological Distribution of Reality v3.0 | QNFO | 2026 | Zenodo | 10.5281/zenodo.21755425 | 1,2,3 |
| C2 | Continuum Trilogy Paper I | QNFO | 2026 | Zenodo | 10.5281/zenodo.21672990 | 2,3 |
| C3 | Quasiparticles as Rational Functions (ODR extension) | QNFO | 2026 | Zenodo (PENDING) | TBD | 1 |
| C4 | Tensor network and (p-adic) AdS/CFT | Bhattacharyya et al. | 2018 | JHEP | 10.1007/jhep01(2018)139 | 3 |
| C5 | p-adic CFT is a holographic tensor network | Hung, Li, Melby-Thompson | 2019 | JHEP | 10.1007/jhep04(2019)170 | 3 |
| C6 | Emergent Einstein Equation in p-adic CFT Tensor Networks | Chen, Liu, Hung | 2021 | PRL | 10.1103/physrevlett.127.221602 | 3,4 |
| C7 | Über einige Lösungen der Funktionalgleichung... (Ostrowski's theorem) | Ostrowski, A. | 1916 | Acta Mathematica | — | 2 |

### Supporting (12 papers — adjacent work, cite where relevant)

| # | Title | Authors | Year | Source | DOI | RQ |
|:--|:------|:--------|:-----|:-------|:----|:---|
| S1 | Tensor networks, p-adic fields, and algebraic curves | Heydeman et al. | 2016 | arXiv/JHEP | — | 3 |
| S2 | Bending the Bruhat-Tits tree Part II (BTZ analogue) | Chen, Liu, Hung | 2021 | JHEP | 10.1007/jhep09(2021)097 | 3 |
| S3 | p-adic AdS/CFT | Gubser et al. | 2017 | CMP | 10.1007/s00220-016-2813-6 | 3 |
| S3b | Scattering on the Bruhat-Tits tree. I | Romanov, Rudin | 1995 | Phys Lett A | 10.1016/0375-9601(94)00997-4 | 4 |
| S4 | p-Adic Analysis and Mathematical Physics | Vladimirov, Volovich, Zelenov | 1994 | Book | — | 2,3 |
| S5 | More Is Different | Anderson, P.W. | 1972 | Science | — | 1 |
| S6 | Foundations of Perturbative QCD | Collins | 2011 | CUP | 10.1017/cbo9780511975592 | 1 |
| S7 | Bruhat–Tits Theory: A New Approach | Kaletha & Prasad | 2023 | CUP | 10.1017/9781108933049 | 3 |
| S8 | The Self-Simulation Hypothesis Interpretation of QM | Irwin et al. | 2020 | Entropy | 10.3390/e22020247 | 1 |
| S9 | Landau Fermi Liquid Theory | Landau, L.D. | 1957 | JETP | — | 1 |
| S10 | The Lamb Shift | Bethe, H.A. | 1947 | PR | — | 1 |
| S11 | PDG: Review of Particle Physics | PDG | 2024 | PRD | 10.1103/physrevd.110.030001 | 1,4 |
| S12 | A Theory of Everything | Laughlin & Pines | 2000 | PNAS | — | 1 |

### Background (7 papers — context/foundations, cite selectively)

| # | Title | Authors | Year | Source | DOI | RQ |
|:--|:------|:--------|:-----|:-------|:----|:---|
| B1 | Quantum Field Theory in a Nutshell | Zee, A. | 2010 | Book | — | 1 |
| B2 | Solid State Physics | Kittel, C. | 2005 | Book | — | 1 |
| B3 | Many-Particle Physics | Mahan, G.D. | 2000 | Book | — | 1 |
| B4 | Principles of Physical Cosmology | Peebles, P.J.E. | 1993 | Book | — | 1 |
| B5 | Introduction to p-adic Numbers and p-adic Analysis | Gouvêa | 2003 | Book | — | 2 |
| B6 | Advanced Quantum Mechanics | Dick, R. | 2012 | Book | — | 1 |
| B7 | Bruhat–Tits Theory (Summary Chapter) | Kaletha & Prasad | 2023 | CUP | 10.1017/9781108933049.007 | 3 |

### Reject (2 papers — false positive/irrelevant)

| # | Title | Reason |
|:--|:------|:-------|
| R1 | The rotatory power of tartaric acid (G. Bruhat, 1914) | "Bruhat" is the physicist, not the Bruhat–Tits tree |
| R2 | QuasiX: GW/BSE implementation (2025) | Software tool — keyword match on "quasiparticle" only |

---

## RQ Cross-Reference

| RQ | Core | Supporting | Background | Total |
|:---|:-----|:-----------|:-----------|:------|
| RQ1 (Compton ontology) | 3 | 8 | 4 | 15 |
| RQ2 (ℚ vs ℝ) | 2 | 2 | 1 | 5 |
| RQ3 (BT coordinates) | 5 | 6 | 1 | 12 |
| RQ4 (Predictions) | 1 | 1 | 0 | 2 |
| RQ5 (Silo failure) | All | All | All | 28 |

**Assessment:** RQ1 (15 papers), RQ3 (12 papers), and RQ5 (28 papers) are well-supported. RQ2 (5 papers) is thin — mostly mathematical foundations without explicit physics claims. RQ4 (2 papers) is severely under-researched — this is the thesis's hardest section and will require significant original work.

---

## KIF-18 Mandatory Symmetry Template (HARD — MUST NOT be empty)

### Where External Literature Supports the ODR Thesis (by RQ)

#### RQ1: Compton Count Ontology
- **QFT:** PDG [S11] defines particle masses as Compton wavelengths; the relation ω_C = mc²/ħ is textbook material. This supports the thesis that the Compton frequency is the central link between mass and quantum identity. [established]
- **Condensed Matter:** Landau [S9] established that quasiparticles have effective mass m* ≠ m_bare, demonstrating that mass is context-dependent. ODR's "quasiparticle = rational function of background Compton counts" maps directly to this well-established physics. [established]
- **Renormalization:** Bethe [S10] showed the electron mass receives radiative corrections — mass is not a fixed constant even in QFT. This supports ODR's claim that only the Compton count N_C = m/m_P is invariant across completions. [established]
- **Emergentism:** Anderson [S5] argued emergent phenomena are as real as fundamental ones; Laughlin & Pines [S12] proposed a "Theory of Everything" based on emergence. ODR provides the geometric criterion (BT-tree vertex invariance) that these frameworks lack. [established]

#### RQ2: ℚ as Primitive Number System
- **Ostrowski's Theorem:** [C7] proves that the only non-trivial completions of ℚ are ℝ (Archimedean) and ℚ_p (p-adic). This is the mathematical foundation — but NO external physics paper uses this theorem to argue that ℚ (not ℝ) is the primitive. This is the thesis's original claim. [established — mathematics; speculative — physics application]
- **p-adic Physics Program:** Vladimirov & Volovich [S4] developed p-adic quantum mechanics, demonstrating that p-adic completions are viable for physics. This supports the "place-democracy" argument but does not assert ℚ-primacy. [established]

#### RQ3: BT Tree as Coordinate System
- **p-adic AdS/CFT (strongest external support):** Five papers in JHEP and PRL [C4, C5, C6, S1, S2] independently developed the BT tree as a physical geometry for holography. This is the strongest external validation: the same mathematical object (the Bruhat–Tits tree) WORKS as a physical coordinate system. Each paper confirms that the tree supports:
  - Tensor network contractions (C4, C5) — spatial geometry from entanglement
  - Black hole analogues (S2) — curvature analogues from combinatorial structure
  - Einstein equations (C6) — gravity emerges from the tree's combinatorics
  - **None of these papers use the tree for particle ontology** — this is ODR's novel application
- **Kaletha & Prasad [S7, B7]:** Definitive mathematical reference establishing BT tree as a (p+1)-valent combinatorial graph with ultrametric distance. [established — mathematics]

#### RQ4: Testable Predictions
- **Emergent Einstein Equations (C6):** Chen, Liu, Hung (2021 PRL) derive Einstein equations from p-adic CFT tensor networks — this is the closest example of a "testable prediction from BT tree geometry." It demonstrates that the tree CAN produce falsifiable physical predictions (in this case, gravitational dynamics).
- **BT-tree scattering theory EXISTS:** Romanov & Rudin (1995, Phys Lett A, 10.1016/0375-9601(94)00997-4) developed "Scattering on the Bruhat-Tits tree. I" — a concrete scattering formalism on the tree. This is prior art that the thesis's RQ4 must engage: the claim is not "no BT scattering exists" but "no BT scattering has been connected to Compton-count particle ontology, and no prediction distinguishing ODR from standard QFT has been derived." This is a HARD constraint on the RQ4 narrative (corrected during red-team v1, 2026-08-03).
- **Overwhelmingly negative (for the specific ODR claim):** No external paper proposes a Planck-scale prediction specifically from the BT-tree / Compton-count / particle-identity framework. This is the thesis's hardest gap — a novel prediction must be developed.
- **Lorentz violation:** The p-adic breaking of Lorentz invariance is well-known [S4, S2]. Any BT-tree-based prediction will likely involve a Lorentz-violation signature at Planck scale — this constrains the search space.

#### RQ5: Silo Failure Diagnosis
- **Five independent discoveries of the same combinatorial tree:**
  1. Ostrowski [C7], 1916 — completions of ℚ (number theory)
  2. Dirac, 1928 — Zitterbewegung frequency (quantum foundations)
  3. Fredkin, 1960 — radix trie (computer science)
  4. Vladimirov–Volovich, 1980s-1994 — BT tree (mathematical physics)
  5. Heydeman et al., 2016 — holographic tensor network (quantum gravity)
- Each domain called the same structure a different name; none connected it to particle ontology. [established — historical]
- **Silo costs:** 110yr (Ostrowski → ODR), 98yr (Dirac → ODR), 66yr (Fredkin → ODR). The p-adic AdS/CFT program reduced the math-physics-to-holography gap to ~30yr, but the Compton-count-to-BT-tree connection remains undiscovered by external authors.

### Where External Literature Constrains or Contradicts the Thesis (by RQ)

#### RQ1: Compton Count Ontology
- **QFT dressing:** The Compton frequency ω_C is treated as a PROPERTY of a particle in QFT, not as its IDENTITY. QFT textbooks (Zee [B1], Collins [S6]) describe particles as field excitations with quantum numbers; the mass is one of those quantum numbers, not the defining one. The thesis inverts this — the particle IS the Compton count; everything else follows. This ontological inversion has NO external precedent and will be seen as a radical philosophical claim, not a physics derivation. [PHILOSOPHY]
- **Renormalization group:** The Compton frequency at IR (m_e c²/ħ) is not the same as at UV — running masses change the Compton count with scale. The thesis must address whether N_C is scale-dependent (in which case it fails the "invariant vertex" claim) or whether the bare Lagrangian N_C is the true primitive (in which case the dressed mass is a rational function, consistent with the quasiparticle extension).

#### RQ2: ℚ as Primitive Number System
- **No external support for the specific claim:** Zero external physics papers state "physics runs on ℚ, not ℝ." The thesis is making an unprecedented claim. This is the RQ with the highest novelty-to-evidence ratio — the paper must present it as a speculative hypothesis, not an established finding.
- **Irrational constants in physics:** π, e, √2 appear in physical laws. The thesis must explain how these are "rational approximations" or "Archimedean projections" without dismissing the operational fact that physicists use them.
- **Computable reals:** The Continuum Trilogy's "ℝ_c × ∏ ℚ_p^c" model (computable reals only) is more defensible than "pure ℚ" at first glance. The thesis should acknowledge this nuance: the number system is computable-rational-with-p-adic-completions, not naively ℚ.

#### RQ3: BT Tree Coordinates
- **The p-adic AdS/CFT program uses the BT tree for holography, not particle coordinates:** The tree is a bulk dual of a 1D CFT boundary — a very different application from "coordinate system for particle identity." The thesis must clearly distinguish these two uses and explain why the tree is applicable to BOTH (consilience) without conflating them.
- **Lorentz invariance is broken on the BT tree:** The p-adic norm is ultrametric, not isotropic — Lorentz symmetry does not hold naturally on the tree. The paper must state this explicitly and propose a recovery mechanism (e.g., "Lorentz invariance is an Archimedean emergent symmetry at large separation scales").
- **No external paper has used the BT tree to replace ℝ³:** This is the most speculative of the 5 RQs.

#### RQ4: Testable Predictions
- **Critical gap — no existing testable prediction from BT tree particle ontology:** This is the weakest dimension of the thesis.
- **Lorentz-violation signatures from quantum gravity:** Amelino-Camelia's doubly-special relativity and the LIV (Lorentz Invariance Violation) literature already constrain possible Planck-scale effects. Any ODR prediction that predicts Lorentz violation must fit within existing experimental bounds (e.g., from IceCube, Fermi-LAT, AGILE).
- **False-precision risk:** The thesis must avoid the trap of proposing a "prediction" that is effectively untestable or differs from existing QFT predictions only at O(10⁻³⁰) where no experiment can reach.
- **[PHILOSOPHY] Falsifiability:** Per qnfo-core §0.0: "This would be disconfirmed if..." — RQ4 MUST include at least one concrete falsifiability condition.

#### RQ5: Silo Failure
- **The p-adic AdS/CFT program has already partially closed the silo:** The math-physics-to-holography gap is now ~10yr (2016-2026), not 110yr. This weakens the "complete silo failure" framing — the thesis must acknowledge that the BT tree IS being used in physics, just not for particle ontology.
- **Convergent discovery is not proof:** The fact that five disciplines discovered the same tree independently is circumstantial evidence, not proof that the tree is the "true" coordinate system of nature. The thesis must present this as suggestive consilience, not as a logical deduction.
- **[NO CONTRADICTING EVIDENCE FOUND]** — no external paper has argued AGAINST using the BT tree for particle ontology. The critique is of absence, not of contradiction.
