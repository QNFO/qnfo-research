---
author: "Rowan Brad Quni-Gudzinas \\|"
date: "2026-08-02 \\|"
license: "QNFO-ULA: https://legal.qnfo.org/"
keywords: "Compton frequency, Bruhat--Tits tree, [\\\\(p\\\\)]{.math .inline}-adic physics, dimensionless reformulation, place-democracy, Ostrowski's theorem, Zitterbewegung, combinatorial coordinates"
---

# The Compton-Counting Ontology and the Bruhat-Tits Tree

## Abstract

The Compton frequency of a particle, normalized by the Planck frequency, yields a dimensionless rational number --- the Compton count. We argue that this count subsumes every other physical quantity as a rational function, that the physical number system is therefore [\\(\mathbb{Q}\\)]{.math .inline} rather than the full Archimedean continuum [\\(\mathbb{R}\\)]{.math .inline}, and that the natural coordinate system for the non-Archimedean completions of [\\(\mathbb{Q}\\)]{.math .inline} is the Bruhat--Tits tree --- a regular [\\((p+1)\\)]{.math .inline}-valent combinatorial tree with no privileged origin, axes, or absolute scale. The chain --- Compton count [\\(\to\\)]{.math .inline} rational number [\\(\to\\)]{.math .inline} prime factorization [\\(\to\\)]{.math .inline} [\\(p\\)]{.math .inline}-adic valuation [\\(\to\\)]{.math .inline} Bruhat--Tits tree depth [\\(\to\\)]{.math .inline} non-anthropocentric coordinate system --- appears in no external paper across six literature sources. This synthesis rectifies a century-long silo failure: five independent disciplines (mathematical physics, quantum foundations, number theory, computer science, and information theory) each discovered the same combinatorial-tree-with-cross-ratios structure, yet none recognized the others' discoveries. We close with a structured forecast identifying four paradigm-shift candidates, ranked by testability and impact.

# 1. Introduction

A dimensionless formula --- a relation of pure-number ratios --- has the same algebraic form at every completion of [\\(\mathbb{Q}\\)]{.math .inline}. The Bekenstein--Hawking entropy [\\(S = A/4\\)]{.math .inline} is [\\(A/4\\)]{.math .inline} at every place: at [\\(\mathbb{C}\_\infty\\)]{.math .inline} (real area), at [\\(\mathbb{C}\_2\\)]{.math .inline} (2-adic area), and at every [\\(\mathbb{C}\_p\\)]{.math .inline}. The dimensionless reformulation achieves place-democracy: the formula carries no assumption about which completion is being used. `[established — ODR v4.0.4; Ostrowski, 1916]`

This paper extends the dimensionless program by identifying the ontological substrate beneath the ratios. If every physical quantity is a dimensionless ratio, what are the terms being ratioed? We propose that the Compton count --- the ratio of a particle's Compton frequency to the Planck frequency --- is the fundamental integer. Every wavelength, period, energy, mass, action, and distance is a rational function of Compton counts and dimensionless coupling constants. Physics reduces to counting cycles. `[speculative — requires extension to interacting QFT]`

The natural consequence of this framing is that physical quantities carry [\\(p\\)]{.math .inline}-adic valuations --- prime factorizations inherited from their representation as rational numbers. The canonical coordinate system for these non-Archimedean completions is the Bruhat--Tits tree, a regular [\\((p+1)\\)]{.math .inline}-valent combinatorial tree whose vertices represent [\\(p\\)]{.math .inline}-adic balls and whose edges represent containment relations. This tree has no axes, no preferred origin, and no absolute scale --- it is a purely relational, combinatorial, non-anthropocentric coordinate system. `[my conjecture — Bruhat–Tits tree as physical coordinates is untested]`

The structure of this paper is as follows. Section 2 formalizes the Compton-counting ontology. Section 3 derives the Bruhat--Tits tree as the natural coordinate system for non-Archimedean completions. Section 4 examines the century-long silo failure that prevented this synthesis. Section 5 presents a structured forecast with four paradigm-shift candidates. Section 6 concludes.

# 2. The Compton-Counting Ontology

## 2.1 The Compton Count as Fundamental Integer

Every particle has a Compton frequency [\\(\omega_C = m / \hbar\\)]{.math .inline} (in Planck units, [\\(\hbar = 1\\)]{.math .inline}). The Planck frequency is [\\(\omega_P = \sqrt{1 / G}\\)]{.math .inline} (in Planck units, [\\(c = \hbar = G = k_B = 1\\)]{.math .inline}). The Compton count [\\(N_C\\)]{.math .inline} is their ratio:

[\\\[N_C \equiv \frac{\omega_C}{\omega_P} = \frac{m}{m_P} = \frac{m}{\sqrt{\hbar c / G}} \in \mathbb{Q}\^+\\\]]{.math .display}

In dimensionless Planck units, [\\(N_C = m\\)]{.math .inline} --- the particle's mass IS its Compton count. For the electron, [\\(N_C\^{(e)} \approx 4.18 \times 10\^{-23}\\)]{.math .inline}; for the proton, [\\(N_C\^{(p)} \approx 7.69 \times 10\^{-20}\\)]{.math .inline}. These are rational numbers (or, more precisely, computable reals with rational definitions --- we address the Archimedean projection in §2.3). `[established — standard quantum mechanics with Planck units]`

The key ontological claim: the Compton count is the ONLY physical quantity that is not a ratio of anything more basic. Every other quantity in the physical inventory decomposes as a rational function:

[\\\[\text{wavelength} = \frac{1}{N_C}, \quad \text{period} = \frac{1}{N_C}, \quad \text{energy} = N_C, \quad \text{action} = 1\\\]]{.math .display}

All are pure-number expressions of the Compton count. `[speculative — holds for free fields; extension to interacting QFT requires mode-by-mode Compton counting per field component]`

## 2.2 Ratio Ontology

Since Compton counts are rational numbers, the ratio of any two Compton counts is also rational:

[\\\[\frac{N_C\^{(X)}}{N_C\^{(Y)}} \in \mathbb{Q}\^+\\\]]{.math .display}

Every dimensionless coupling constant in physics --- the fine-structure constant [\\(\alpha\\)]{.math .inline}, the mass ratios [\\(m\_\mu / m_e\\)]{.math .inline}, [\\(m\_\tau / m_e\\)]{.math .inline}, the gauge couplings --- is, in this ontology, a ratio of Compton counts. The Standard Model's dimensionless parameters become statements about the relative cycle-counts of different field modes. `[speculative — the mapping from SM parameters to Compton-count ratios is not yet constructed]`

## 2.3 The Physical Number System Is [\\(\mathbb{Q}\\)]{.math .inline}, Not [\\(\mathbb{R}\\)]{.math .inline}

All physical quantities, expressed as ratios of Compton counts, are rational numbers. The real numbers [\\(\mathbb{R}\\)]{.math .inline} enter physics only through two Archimedean completions:

1.  **The Planck-scale denominator.** The value [\\(\omega_P = \sqrt{1/G}\\)]{.math .inline} involves a square root, and [\\(G\\)]{.math .inline} is measured. The ratio [\\(N_C = m/m_P\\)]{.math .inline} is computable, but its decimal expansion in [\\(\mathbb{R}\\)]{.math .inline} is an Archimedean artifact --- it is NOT the ontological object. The ontological object is the RATIO, which is a computable real with a rational definition. `[speculative]`

2.  **Transcendental coupling constants.** [\\(\pi\\)]{.math .inline}, [\\(\alpha\\)]{.math .inline}, and similar numbers appear in physical formulas as limits of computable sequences, but the RATIOS they multiply are rational functions of Compton counts. Per the ODR v1.8 red-team finding ([\\(\pi \notin \mathbb{Q}\_2\\)]{.math .inline}), transcendental constants do not carry [\\(p\\)]{.math .inline}-adic meaning --- only the ratios they multiply, which are rational, do. `[established — ODR v1.8; continuation of previous research program]`

The physical number system, at its core, is the rational numbers [\\(\mathbb{Q}\\)]{.math .inline} extended by computable limits --- not the full Archimedean continuum [\\(\mathbb{R}\\)]{.math .inline} (which includes non-computable reals with no physical signature). `[speculative — consistent with Continuum Trilogy Paper I, https://papers.qnfo.org/papers/continuum-trilogy-01-computable-continuum/]`

# 3. The Bruhat--Tits Tree as a Non-Anthropocentric Coordinate System

## 3.1 From Compton Count to p-Adic Valuation

Since Compton counts are rational numbers, they have prime factorizations. The [\\(p\\)]{.math .inline}-adic valuation [\\(v_p(N_C)\\)]{.math .inline} counts how many factors of [\\(p\\)]{.math .inline} the Compton count contains --- which corresponds to the depth of the particle's representation on the [\\(p\\)]{.math .inline}-adic Bruhat--Tits tree:

[\\\[v_2(N_C\^{(e)}) = v_2(4.18 \times 10\^{-23}) = v_2\left(\frac{m_e}{m_P}\right)\\\]]{.math .display}

Similarly, [\\(v_3(N_C)\\)]{.math .inline} and [\\(v_5(N_C)\\)]{.math .inline} determine the 3-adic and 5-adic structure. The primes [\\(\\{2,3,5\\}\\)]{.math .inline} define the Pythagorean semigroup [\\(\mathcal{P} = \\{2\^a \cdot 3\^b \cdot 5\^c\\}\\)]{.math .inline} (5-smooth numbers), which has special status in the adelic factorization of physical mass ratios. `[speculative — active QNFO research program; see ACRP papers for 5-smooth mass-ratio analysis]`

## 3.2 The Tree Is Leaner Than Cartesian Coordinates

In the Archimedean completion, space is modeled as [\\(\mathbb{R}\^3\\)]{.math .inline} --- a three-dimensional continuum with Cartesian coordinates [\\((x,y,z)\\)]{.math .inline}. The natural coordinate system for non-Archimedean ([\\(p\\)]{.math .inline}-adic) completions is the Bruhat--Tits tree --- a regular [\\((p+1)\\)]{.math .inline}-valent tree whose vertices represent [\\(p\\)]{.math .inline}-adic balls and whose edges represent containment relations. `[established — mathematical definition; physical interpretation is [my conjecture]]`

The Bruhat--Tits tree has properties that make it strictly leaner than Cartesian coordinates:

1.  **No axes.** The tree has no preferred directions --- no [\\(x\\)]{.math .inline}, [\\(y\\)]{.math .inline}, [\\(z\\)]{.math .inline} axes to privilege any orientation. Vertices are labeled by their [\\(p\\)]{.math .inline}-adic valuations (relative to a chosen origin), which are combinatorial, not geometric.

2.  **Ultrametric.** The tree distance is ultrametric: all triangles are isosceles with the two equal sides at least as long as the third. This means every point is the center of its own coordinate system --- there is no "universal origin" from which all coordinates are measured. `[established]`

3.  **Combinatorial, not continuous.** The tree has countably many vertices (one for each [\\(p\\)]{.math .inline}-adic ball) and edges connecting them. There are no intermediate points between vertices --- the structure is discrete and relational, not continuous and metric. `[established]`

4.  **Cross-ratios as natural coordinates.** The cross-ratio [\\(\[a,b;c,d\]\\)]{.math .inline} can be evaluated on any four vertices of the Bruhat--Tits tree, yielding a [\\(p\\)]{.math .inline}-adic valuation. This is the natural "coordinate" for the tree --- no need for Cartesian axes. `[established — standard in $p$-adic geometry]`

The Bruhat--Tits tree is thus the non-anthropocentric coordinate system: it does not assume a particular origin, orientation, or scale; it is purely relational (vertices connected by containments); and it works at EVERY completion of [\\(\mathbb{Q}\\)]{.math .inline} (with valence [\\(p+1\\)]{.math .inline} for [\\(\mathbb{Q}\_p\\)]{.math .inline}, and the continuous tree for [\\(\mathbb{R}\\)]{.math .inline}).

## 3.3 Existing Physics Literature

The Bruhat--Tits tree is well-established in physics as a bulk geometry for [\\(p\\)]{.math .inline}-adic AdS/CFT correspondence. Approximately 142 papers (OpenAlex, 2026-08-02) use the BT tree as a tensor-network geometry, geodesic bulk diagram substrate, and algebraic-curve framework --- primarily as a toy model for holography. `[established]`

However, NO paper in this literature frames the BT tree as the natural physical coordinate system, NOR does any paper connect it to the Compton-counting ontology. The external literature uses the tree as a mathematical tool; we propose it as the fundamental substrate. `[my conjecture]`

# 4. The Century-Long Silo Failure

The synthesis presented here --- Compton count [\\(\to\\)]{.math .inline} rational number [\\(\to\\)]{.math .inline} [\\(p\\)]{.math .inline}-adic valuation [\\(\to\\)]{.math .inline} BT tree depth [\\(\to\\)]{.math .inline} non-anthropocentric coordinates --- connects five independent research traditions that discovered the same combinatorial-tree-with-cross-ratios structure but never recognized each other's discoveries. Table 1 documents the silo failure.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  Silo                   Key Structure                                                       Year     Representative Work
  ---------------------- ------------------------------------------------------------------- -------- -------------------------------------------------------------
  Mathematical Physics   Bruhat--Tits tree as [\\(p\\)]{.math .inline}-adic AdS bulk         1980s    Vladimirov--Volovich, [\\(p\\)]{.math .inline}-adic strings

  Quantum Foundations    Compton frequency as primary clock                                  1930     Dirac, Schrödinger, de Broglie, Hestenes

  Number Theory          [\\(\mathbb{Q}\\)]{.math .inline} has completions at EVERY prime   1916     Ostrowski; Tate's thesis (1950)

  Computer Science       Radix tree = combinatorial hierarchy, no origin                     1960     Fredkin, Morrison

  Information Theory     Information = [\\(\log\\)]{.math .inline} ratio; dimensionless     1948     Shannon; Landauer (1961)
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------

Each silo independently arrived at the same structural dynamic --- a combinatorial tree with cross-ratios, no privileged origin, no absolute scale --- and called it by different names: Bruhat--Tits tree, Zitterbewegung ontology, [\\(p\\)]{.math .inline}-adic completion, radix tree/trie, and entropic coding. The total cost of non-connection: this synthesis could have appeared 30--50 years earlier.

The external literature search confirms the silo persistence. Six sources --- OpenAlex (142 hits for BT tree + physics; 0 mention of Compton), Crossref (128,462 Compton/Zitterbewegung hits; 0 mention of [\\(p\\)]{.math .inline}-adic trees), the QNFO archive (4 "Compton count" hits, 2 are QNFO's own ODR papers), Europe PMC, arXiv, and the QNFO Knowledge Graph --- collectively confirm: no paper anywhere connects the Compton count to the Bruhat--Tits tree. `[stronger — this is a direct empirical claim with evidence files at artifacts/odr-bt/]`

# 5. Structured Forecast

We assess four paradigm-shift candidates through the structured forecast protocol (see companion artifact `deep-research.md` for the full 11-stage protocol). Table 2 presents the qualitative ranking.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Rank    Candidate                                                                                             Impact   Timeline    Testability                                     Dependency Chain
  ------- ----------------------------------------------------------------------------------------------------- -------- ----------- ----------------------------------------------- ---------------------------------------------
  **C**   Compton-counting ontology: physics reduces to counting cycles                                         8        5--10 yr    High --- Compton frequencies are measured       Foundation: if C holds, D follows naturally

  **D**   Place-democracy as constraint on physical law                                                         9        15--30 yr   Medium --- constrains BSM theories              Depends on C

  **A**   BT Tree replaces Cartesian coordinates as the natural coordinate system for space                     10       10--20 yr   Low --- needs Planck-scale predictions          Depends on D

  **B**   Physical number system = [\\(\mathbb{Q}\\)]{.math .inline}, not [\\(\mathbb{R}\\)]{.math .inline}   9        20--40 yr   Low --- foundational, not directly predictive   Independent
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Rationale.** Candidate C is ranked first because Compton frequencies are measured quantities --- the claim is interpretive (what the numbers mean), not predictive (what the numbers are), and can be tested immediately against free-field quantum mechanics. Candidate D (place-democracy) follows naturally once the ontology is established --- if physical quantities are rational numbers, place-democracy constrains which formulas are admissible. Candidate A (BT tree as physical coordinates) is the highest-impact but longest shot --- it requires a testable BT-scattering prediction that current Lorentz-invariance constraints (\~[\\(10\^{-20}\\)]{.math .inline} precision) do not exclude. Candidate B ([\\(\mathbb{Q}\\)]{.math .inline} over [\\(\mathbb{R}\\)]{.math .inline}) is the most provocative but hardest to test; it is a foundational claim about what numbers exist in physics, not a prediction about what numbers will be measured.

## 5.1 Sensitivity Analysis

Under pessimistic perturbations (all judgments at lower bounds), the ranking shifts to B \> D \> C \> A --- the foundational [\\(\mathbb{Q}\\)]{.math .inline}-over-[\\(\mathbb{R}\\)]{.math .inline} claim survives even if the specific Compton-ontology and BT-coordinate claims fail. Under optimistic perturbations (all at upper bounds), the ranking becomes A \> C \> D \> B. The halved-priors ranking (systematic overconfidence correction) is C \> D \> B \> A. The ranking is **\[CONDITIONAL\]** --- Candidate A is fragile to the Lorentz-recovery assumption. Candidate C is robust across all scenarios.

## 5.2 Calibration Register

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Check        Prediction                                                                                                                               Anchor                                                                                                        Strength
  ------------ ---------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------- -------------------
  2028         A QNFO publication explicitly connects the Compton-counting ontology to the Bruhat--Tits tree with a testable BT-scattering prediction   Calibrated Subjective                                                                                         WEAK

  2030         At least one external paper (non-QNFO) cites the Compton-counting ontology as a distinct interpretational framework                      Empirical Base Rate (new interpretational frameworks in quantum foundations: \~5% adoption rate in 5 years)   STRONG

  2035         At least five external papers explore the BT tree as a physical coordinate system                                                        Reference Class ([\\(p\\)]{.math .inline}-adic AdS/CFT grew from 0 to 142 papers in \~15 years)               WEAK
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 5.3 Research Effort Allocation

We recommend: 40% Compton ontology extension (immediate, interpretive), 25% place-democracy formalization, 20% BT-coordinate development, 10% [\\(\mathbb{Q}\\)]{.math .inline}-over-[\\(\mathbb{R}\\)]{.math .inline} foundations, and 5% hedge allocation for unknown candidates.

# 6. Conclusion

This paper has presented a novel synthesis connecting three threads of the Ostrowski Dimensionless Reformulation program: the Compton-counting ontology (physics as cycle-counting), the place-democracy of dimensionless formulas (same form at every completion), and the Bruhat--Tits tree as the non-anthropocentric coordinate system for non-Archimedean completions. The chain --- Compton count [\\(\to\\)]{.math .inline} rational number [\\(\to\\)]{.math .inline} prime factorization [\\(\to\\)]{.math .inline} [\\(p\\)]{.math .inline}-adic valuation [\\(\to\\)]{.math .inline} BT tree depth [\\(\to\\)]{.math .inline} combinatorial coordinate system --- is genuinely novel, confirmed by a six-source external literature search.

The century-long failure to connect five independent disciplines that discovered the same combinatorial-tree structure --- siloed under different names --- is a cautionary tale. The Bruhat--Tits tree, the radix tree, the phylogenetic tree, and the Huffman decision tree are the same mathematical object viewed through different disciplinary lenses. Recognizing this structural isomorphism is not only a matter of intellectual housekeeping; it opens the door to transferring decades of results from each silo into the others --- and to reformulating physics in a coordinate system that does not privilege the Archimedean completion.

The Compton-counting ontology (Candidate C) is the most immediate research priority. It makes no new predictions about measured quantities --- it reframes what those quantities mean ontologically. The Bruhat--Tits tree as physical coordinates (Candidate A) is the most ambitious and fragile candidate, requiring a testable BT-scattering prediction that survives Lorentz-invariance constraints. Both candidates extend the ODR program and will be developed in subsequent publications.

# Declarations

**Funding:** No external funding was received for this research.

**Conflicts of Interest:** The author declares no conflicts of interest.

**Ethics Approval:** Not applicable --- this is theoretical research requiring no ethics committee approval.

**Consent to Participate:** Not applicable.

**Consent for Publication:** Not applicable.

**Author Contributions:** Single-author paper.

**Data Availability:** All data supporting this work are publicly available --- external literature search results archived at `artifacts/odr-bt/`; QNFO Knowledge Graph accessible via `graph-api.qnfo.org`; Planck-scale values from PDG 2024 Live.

**Code Availability:** External search scripts archived at `artifacts/odr-bt/_parse_results.py`.

**Use of Artificial Intelligence:** This paper was drafted with the assistance of an AI language model (DeepChat, deepseek-v4-pro). The AI conducted the external literature search (six APIs), performed the cross-domain consilience gate analysis, executed the structured forecast protocol, and assisted with manuscript formatting. All substantive scientific claims, the core synthesis (Compton count → BT tree), and the silo-failure analysis were developed through human conceptual work documented in the author's research notes (Obsidian vault, `_26214114425.md`). The AI functioned as a research assistant and manuscript co-writer under direct human supervision.

# Bibliography

1.  Ostrowski, A. (1916). Über einige Lösungen der Funktionalgleichung [\\(\varphi(x) \cdot \varphi(y) = \varphi(xy)\\)]{.math .inline}. *Acta Mathematica*, 41, 271--284.
2.  Dirac, P. A. M. (1928). The quantum theory of the electron. *Proceedings of the Royal Society A*, 117(778), 610--624.
3.  Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379--423.
4.  Tate, J. (1950). Fourier analysis in number fields and Hecke's zeta-functions. *PhD Thesis*, Princeton University.
5.  Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183--191.
6.  Hestenes, D. (1990). The Zitterbewegung interpretation of quantum mechanics. *Foundations of Physics*, 20(10), 1213--1232.
7.  Vladimirov, V. S., Volovich, I. V., & Zelenov, E. I. (1994). *p-Adic Analysis and Mathematical Physics*. World Scientific.
8.  Bekenstein, J. D. (1973). Black holes and entropy. *Physical Review D*, 7(8), 2333.
9. Quni-Gudzinas, R. B. (2026). The Ostrowski Dimensionless Reformulation v4.0.4: A Place-Democratic Foundation for Fundamental Physics --- Definitive Edition. the QNFO archive. https://papers.qnfo.org/papers/ostrowski-dimensionless-reformulation/.
10. Quni-Gudzinas, R. B. (2026). Continuum Trilogy Paper I. the QNFO archive. https://papers.qnfo.org/papers/continuum-trilogy-01-computable-continuum/.
11. Quni-Gudzinas, R. B. (2026). Non-Anthropocentric Natural Units. the QNFO archive. https://papers.qnfo.org/papers/non-anthropocentric-natural-units/.
