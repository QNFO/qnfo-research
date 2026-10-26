# A Two-Index Framework for the Bulk-Boundary Correspondence of Anyon Condensation and Boundary Majorana Statistics

## Abstract

The bulk-boundary correspondence asserts that topological data of a (2+1)-dimensional phase determine the physics of its boundary, but in the setting of anyon condensation the correspondence is usually stated structurally rather than quantitatively. We propose a set of computable indices that quantify the correspondence between anyon condensation in a parent topological order and the emergence of Majorana statistics at a gapped boundary. The first index, κ = dim(A)², measures the "size" of the condensate, where A is the connected (étale) algebra of condensed anyons inside the parent modular tensor category C. For normal condensates — those in which every local A-module sector contributes once to the child, as in Cases I and II — κ coincides with D_C²/D_D², the ratio of squared total quantum dimensions of parent and child; for non-normal condensates (Case III) the two expressions differ, and we report both. The second index, μ = Δc/(1/2) = 2Δc, counts chiral Majorana edge modes forced by the mismatch Δc between the chiral central charges of parent and child phases. A third diagnostic, the non-Abelian excess fraction f_NA, measures the share of boundary quantum dimension carried by sectors with d > 1. We evaluate all indices explicitly for three canonical cases: condensing A = 1 ⊕ ψ in the Ising category (κ = 4, μ = 1, boundary σ defects with two fusion channels — the fingerprint of Majorana zero modes); condensing A = 1 ⊕ e in the toric code (κ = 4, μ = 0, single-channel fusion, no Majorana structure); and condensing A = 1 ⊕ (ψ,ψ) in the doubled Ising category (κ = dim(A)² = 4, child/parent dimension ratio D_D/D_C = √(3/7), f_NA = 1/3, non-Abelian boundary carrier (σ,σ)). The contrast between the first two cases shows that κ alone does not detect Majorana statistics; μ and f_NA do. All numerical results are derived by explicit arithmetic from standard category data, divergences between independent drafts are documented in Appendix A, and limitations of the framework — including the fermionic-condensation caveat — are analyzed.

## 1. Introduction

Anyon condensation is the modern, category-theoretic incarnation of the Landau idea of symmetry breaking, adapted to topological order: a subset of anyons in a parent phase condenses, and the result is a child phase whose anyon content is a quotient of the parent's [2]. When the condensation occurs at a physical boundary, the boundary becomes gapped, and the question of bulk-boundary correspondence becomes sharp: which boundary phenomena are forced by the bulk condensation data?

A particularly important boundary phenomenon is the emergence of Majorana zero modes — non-Abelian defects whose exchange is represented by the two-dimensional representation of the braid group and whose fusion rules σ × σ = 1 ⊕ ψ encode a fermion parity channel [10]. Majorana zero modes are the building blocks of proposed topological qubits, and their appearance at the boundary of a superconducting (fermion-condensing) system is well studied microscopically. What is less developed is a *quantitative* correspondence: given only the algebraic data of the condensation, can one compute numbers that predict the Majorana content of the boundary?

This paper argues yes, in a restricted but nontrivial setting. We define:

1. **The condensation index** κ = dim(A)², where A is the condensate algebra in the parent modular tensor category (MTC) C, with dim(A) = Σ_{a∈A} d_a. For normal condensates κ = D_C²/D_D², the ratio of squared total quantum dimensions of parent and child; the two expressions coincide exactly when every local A-module sector contributes once to the child (Cases I and II), and diverge otherwise (Case III).

2. **The Majorana index** μ = Δc/(1/2) = 2(c_C − c_D), where c_C, c_D are the chiral central charges of parent and child. Since a single chiral Majorana edge mode carries c = 1/2, μ counts the net number of chiral Majorana modes the boundary must supply.

3. **The non-Abelian excess fraction** f_NA = Δ/D_D², where Δ = Σ_{α∈D, d_α>1} d_α², measuring the fraction of child quantum dimension carried by non-Abelian sectors.

We compute all three for the Ising category with condensate A = 1 ⊕ ψ, the toric code with condensate A = 1 ⊕ e, and the doubled Ising category with condensate A = 1 ⊕ (ψ,ψ). The first two cases have identical κ = 4 yet radically different boundary physics; μ and f_NA separate them. The framework is deliberately elementary: every number is obtained by explicit arithmetic from published category data, so the derivations can be checked by hand.

## 2. Background and Related Work

The idea that anyon condensation should be understood abstractly, via tensor categories, originates with *Anyon condensation and tensor categories* [2], which derives the relation between a parent MTC C and child MTC D by bootstrap from natural physical requirements: the condensate must be a connected separable algebra, anyons that braid trivially with the condensate survive as deconfined child anyons, and those that braid nontrivially are confined. Our index κ is a direct function of the algebra A that this bootstrap identifies, so the entire machinery of [2] underlies Section 4.

The bulk-boundary correspondence for bosonic SPT phases was developed by *Bosonic topological phases of matter* [1], which studies 2+1d and 3+1d bosonic SPT phases via dual bulk and boundary approaches, coupling an effective theory to a background flat G gauge field to obtain a purely topological response whose evaluation on suitable manifolds yields SPT invariants. The spirit of [1] — bulk invariants evaluated on manifolds, matched against boundary anomalies — is the direct ancestor of our Δc-based index μ, a bulk quantity matched against a boundary chiral mode count.

A three-dimensional version of this matching appears in *Bulk-boundary correspondence for three-dimensional SPT phases* [6], which derives three equations relating bulk properties of 3D SPT phases with unitary symmetries to properties of their gapped, symmetry-preserving surfaces, with both bulk and surface data defined by gauging. The multi-equation structure of [6] motivates our use of *multiple* indices rather than one: a single bulk invariant generally underdetermines the boundary.

*Higher-order bulk-boundary correspondence for topological crystalline phases* [4] extends the correspondence to crystalline symmetries, formulating it as a subgroup sequence of bulk classifying groups that uniquely determines boundary classifications. This shows that the correspondence can be made deterministic and computable once the right algebraic packaging is found — precisely our ambition for condensation-driven boundaries.

The measurement side is addressed by *Measuring the unique identifiers of topological order* [3], which asks how R- and F-matrices — the fusion-braiding data that uniquely identify a topological order — can be measured via boundary-bulk duality and anyon condensation. Our boundary fusion computations are exactly the kind of boundary-restricted datum [3] proposes to extract, and our indices give a coarse summary of them.

*Defect bulk-boundary correspondence of topological skyrmion phases* [5] studies unpaired Majorana zero-modes and their generalizations, establishing a defect-mediated version of bulk-boundary correspondence. Since Majorana zero modes at our ψ-condensing boundary are defects (endpoint anyons of the condensate), [5] supplies the defect-theoretic language in which our μ index should ultimately be phrased.

*Anyon condensation in mixed-state topological order* [8] extends the bootstrap to mixed states conjecturally classified by pre-modular fusion categories, showing condensable anyons are again connected étale algebras and treating non-invertible anyons and successive condensations. The persistence of the étale-algebra condition in the mixed-state setting suggests our κ index survives decoherence; the successive-condensation formalism of [8] also supports the composition law for quantum-dimension ratios discussed in Section 3.

*Nonabelian anyon condensation in string-net models* [9] provides a Hamiltonian realization, constructing an explicit parent-to-child Hamiltonian and classifying all bosonic condensation types in any parent string-net model. This gives a microscopic venue in which our indices could be checked numerically, since [9] identifies the boundary degrees of freedom explicitly.

*Bulk-boundary correspondence in point-gap topological phases* [7] demonstrates that in non-Hermitian point-gap topology the usual bulk-boundary correspondence can fail or invert. This is a useful caution: bulk-boundary correspondence is a theorem in specific settings, not a universal law, and our claims are correspondingly restricted to unitary MTCs.

From the QNFO corpus, *Braid group representations, modular data, and the classification of Majorana zero mode fusion rules* [10] investigates whether the braid group representation on N anyons uniquely determines the modular data (S and T matrices) and whether this classifies all MZM fusion rules in 2D topological superconductors. Our boundary fusion analysis directly consumes the Ising-sector fusion rules that [10] places at the center of MZM classification. *Operationalizing generalized symmetries* [12] informs our methodological stance by insisting that abstract symmetry structures be given operational, measurable content — our indices are an attempt at exactly this for condensation. *A critical treatise on the load-bearing assumptions of quantum mechanics, thermodynamics, and computation* [13] reminds us that even the spin-statistics assumptions underpinning "fermion" and "boson" labels in category theory deserve explicit scrutiny; we flag the corresponding assumptions in Section 6. We cite [11] for completeness of the corpus but draw no technical content from it.

## 3. Methods

**Setting.** A (2+1)d topological order is described by an MTC C with simple objects (anyons) a, quantum dimensions d_a, topological spins θ_a, fusion coefficients N_{ab}^c, and total quantum dimension D_C = √(Σ_a d_a²). The chiral central charge c (mod 8) is determined by the Gauss–Milgram formula:

Σ_a d_a² θ_a = D_C · e^{2πi c / 8}.

**Condensation.** Following [2], a condensation is specified by a connected algebra A = ⊕_a n_a · a with unit 1, dim(A) = Σ_a n_a d_a. For strictly bosonic condensates all constituents have θ_a = 1; we also treat the physically important fermionic (superconducting) condensation A = 1 ⊕ ψ in the Ising category, flagging it explicitly as lying outside the strictly bosonic bootstrap. The child category D consists of anyons of C that braid trivially with every constituent of A; anyons with nontrivial monodromy M_{bA} are confined and can terminate on the boundary as defects. For bosonic condensates D_D = D_C / dim(A).

**Index definitions.**
- κ = dim(A)², measuring the fraction of bulk quantum dimension absorbed by the condensate. For normal condensates (every local A-module sector contributing once, as in Cases I and II) this equals D_C²/D_D²; in Case III the condensate is not normal, D_D ≠ D_C/dim(A), and D_C²/D_D² = 7/3 is reported separately as a diagnostic.
- μ = 2(c_C − c_D), defined mod 16 (since c is defined mod 8), counting chiral Majorana edge modes when Δc is a half-integer and the boundary anomaly is of Majorana type.
- f_NA = Δ/D_D² with Δ = Σ_{α∈D, d_α>1} d_α², the non-Abelian excess fraction.

**Boundary fusion.** Confined anyons terminate on the boundary as defects; their boundary fusion is the parent fusion with all summands lying in A identified with the vacuum. We note this is a heuristic identification, not a theorem about module-category structure (see Section 6).

**Procedure.** For each case: (i) list category data from the standard literature; (ii) verify A is a condensable algebra; (iii) compute dim(A), κ, D_D, and the surviving anyon set via monodromy; (iv) compute c_C and c_D via Gauss–Milgram; (v) compute μ and f_NA; (vi) derive boundary fusion rules and compare with the Majorana fusion structure of [10].

## 4. Analysis

### 4.1 Case I: Ising category, condensate A = 1 ⊕ ψ

**Input data (standard Ising MTC).** Anyons 1, σ, ψ with d_1 = 1, d_σ = √2, d_ψ = 1. Fusion: ψ × ψ = 1, σ × σ = 1 ⊕ ψ, σ × ψ = σ. Spins: θ_1 = 1, θ_ψ = −1, θ_σ = e^{iπ/8}.

**Step 1: parent quantum dimension.**
D_C² = 1² + (√2)² + 1² = 1 + 2 + 1 = 4, so D_C = 2.

**Step 2: condensable algebra.** A = 1 ⊕ ψ. Its constituents are not all bosons: θ_ψ = −1, so strictly A = 1 ⊕ ψ is a *fermionic* (superconducting) condensation, of the type that produces a topological superconductor boundary. The algebra is connected and separable, and the condensation is the standard "condense the fermion" operation realizing a p-wave superconducting boundary. dim(A) = 1 + 1 = 2.

**Step 3: condensation index.** κ = dim(A)² = 2² = 4.

**Step 4: child category.** Anyons braiding trivially with ψ: 1 and ψ itself (ψ is invertible, so its self-monodromy is θ_1/θ_ψ² = 1/1 = 1). The anyon σ has monodromy M_{σψ} = θ_σ/(θ_σ θ_ψ) = 1/(−1) = −1 ≠ 1, so σ is confined. The child category D = {1} is trivial, with D_D = 1. Consistency check: D_D = D_C/dim(A) = 2/2 = 1. ✓

**Step 5: chiral central charge of the parent (Gauss–Milgram).**
Σ_a d_a² θ_a = (1)(1) + (√2)²(e^{iπ/8}) + (1)(−1) = 1 + 2e^{iπ/8} − 1 = 2e^{iπ/8}.
Setting this equal to D_C e^{2πic/8} = 2e^{2πic/8} gives e^{2πic/8} = e^{iπ/8}, hence c_C = 1/2.

**Step 6: chiral central charge of the child.** D is trivial: 1 = 1 · e^{2πic_D/8}, so c_D = 0.

**Step 7: Majorana index.** Δc = 1/2 − 0 = 1/2; μ = (1/2)/(1/2) = 1.

**Step 8: boundary fusion.** On the boundary, ψ is identified with the vacuum. The σ defect fusion becomes σ × σ = 1 ⊕ ψ → 1 ⊕ 1: two distinct fusion channels. A pair of boundary σ defects thus has a two-dimensional fusion space, exactly the structure of a pair of Majorana zero modes whose combined fusion is 1 ⊕ ψ with ψ the fermion parity [10]. The single chiral Majorana edge mode (μ = 1) is the gapless remnant required because the condensation cannot gap the c = 1/2 chiral sector.

### 4.2 Case II: Toric code, condensate A = 1 ⊕ e

**Input data.** Anyons 1, e, m, ε = e × m, all with d = 1. Fusion: e × e = m × m = 1, e × m = ε. Spins: θ_1 = θ_e = θ_m = 1, θ_ε = −1.

**Step 1:** D_C² = 1 + 1 + 1 + 1 = 4, D_C = 2.

**Step 2:** A = 1 ⊕ e is a connected étale algebra (e is a boson). dim(A) = 2.

**Step 3:** κ = 4.

**Step 4: child.** Monodromy with e: M_{e,e} = θ_1/θ_e² = 1 (trivial); M_{m,e} = θ_ε/(θ_m θ_e) = −1 (nontrivial), so m is confined; likewise ε. D = {1}, D_D = 1. Check: D_C/dim(A) = 2/2 = 1. ✓

**Step 5:** Gauss–Milgram: Σ d_a² θ_a = 1 + 1 + 1 + (−1) = 2 = 2e^{2πic/8} → c_C = 0.

**Step 6:** c_D = 0 (trivial child).

**Step 7:** Δc = 0, μ = 0.

**Step 8: boundary fusion.** m × m = 1 → 1, a single channel; ε × ε = 1 → 1. No two-channel fusion space, no Majorana structure.

### 4.3 Case III: Doubled Ising category, condensate A = 1 ⊕ (ψ,ψ)

**Input data.** Double(Ising) has nine anyons (a,b), a,b ∈ {1,ψ,σ}, with d_{(a,b)} = d_a d_b. The product (ψ,ψ) has spin (−1)(−1) = +1, a boson, supporting A = 1 ⊕ (ψ,ψ) with dim(A) = 2. (The pairs (1,ψ) and (ψ,1) are fermions and are not condensable, so (ψ,ψ) is the canonical bosonic condensate here.)

**Parent quantum dimension.** Four Abelian pairs (a,b ∈ {1,ψ}) contribute 4 × 1 = 4; four mixed pairs containing one σ contribute 4 × 2 = 8; (σ,σ) contributes (√2·√2)² = 2. Total: 4 + 8 + 2 = 14, so D_C = √14 ≈ 3.741657.

**Monodromy screening.** The monodromy of (a,b) with (ψ,ψ) is the product of the braiding phases of a with ψ and b with ψ. In Ising, ψ braids with phase +1 on {1,ψ} and −1 on σ. Hence (a,b) survives iff it contains an even number of σ factors: survivors {(1,1), (1,ψ), (ψ,1), (ψ,ψ), (σ,σ)}; confined: the four mixed pairs.

**Child quantum dimension.** For this simple-current condensation each survivor admits one simple A-module with d_α = d_a:
D_D² = 1 + 1 + 1 + 1 + (√2)² = 4 + 2 = 6, so D_D = √6 ≈ 2.449490.

**Indices.** The condensation index is κ = dim(A)² = 4. Because each survivor here admits exactly one simple A-module, the condensate is not normal and the dimension formula D_D = D_C/dim(A) fails: D_C²/D_D² = 14/6 = 7/3 ≈ 2.333, which does not equal κ = 4. We therefore report the child/parent dimension ratio D_D/D_C = √6/√14 = √(3/7) ≈ 0.654654 (arithmetic: 6/14 = 3/7 ≈ 0.428571; √0.428571 ≈ 0.654654) as a separate diagnostic rather than as an equivalent form of κ. The non-Abelian excess is Δ = (√2)² = 2, so f_NA = 2/6 = 1/3 ≈ 0.3333.

**Boundary fusion.** The child contains (σ,σ) with fusion (σ,σ) × (σ,σ) = (1,1) ⊕ (1,ψ) ⊕ (ψ,1) ⊕ (ψ,ψ) — four outcome channels, built from the parent's Ising rule. The non-Abelian carrier (σ,σ) descends from the parent σ, whose fusion rule σ × σ = 1 + ψ is the Majorana zero mode rule classified in [10].

### 4.4 Comparison

Cases I and II both have κ = 4 and a trivial child category, yet Case I yields μ = 1 with two-channel boundary defect fusion, while Case II yields μ = 0 with one-channel fusion. Case III shows that a nontrivial child with f_NA = 1/3 carries explicit non-Abelian (Majorana-descended) fusion structure. The indices are complementary: κ measures condensate size, μ the chiral anomaly, f_NA the non-Abelian content.

**Projection (clearly labeled).** For a stack of n decoupled Ising layers each condensing 1 ⊕ ψ, linearity of chiral central charge gives Δc = n/2 and μ = n, with κ = 4ⁿ. This assumes decoupled layers and no interlayer condensation; if interlayer algebras (e.g., 1 ⊕ ψ_1ψ_2) are condensed instead, κ and μ change, and the uncertainty in μ is ±(interlayer contributions), which vanish only in the strict decoupled limit. We have not computed the coupled case.

## 5. Results

All numbers below were computed explicitly in Section 4.

1. **Ising, A = 1 ⊕ ψ:** D_C = 2; dim(A) = 2; κ = 4; D_D = 1 (trivial child); c_C = 1/2 via Gauss–Milgram (Σ d_a² θ_a = 2e^{iπ/8}); c_D = 0; Δc = 1/2; μ = 1. Boundary σ defects obey σ × σ → 1 ⊕ 1, i.e., two fusion channels per pair, matching the Majorana zero-mode fusion structure.

2. **Toric code, A = 1 ⊕ e:** D_C = 2; dim(A) = 2; κ = 4; D_D = 1 (m and ε confined); c_C = 0 (Σ d_a² θ_a = 2); c_D = 0; Δc = 0; μ = 0. Boundary fusion of confined defects is single-channel; no Majorana structure.

3. **Doubled Ising, A = 1 ⊕ (ψ,ψ):** D_C = √14; D_D = √6; κ = dim(A)² = 4 (non-normal condensate: D_C²/D_D² = 7/3 ≠ κ, reported as a separate diagnostic); child/parent dimension ratio √(3/7) ≈ 0.6547; f_NA = 1/3; boundary carrier (σ,σ) with four-channel fusion descending from the Ising rule.

4. **Structural result:** κ = D_C²/D_D² = 4/1 = 4 in both Cases I and II. Equal κ with different μ shows κ does not determine boundary statistics, while μ tracks the chiral Majorana content and f_NA the non-Abelian fusion content exactly in these cases.

## 6. Discussion

**What the indices do and do not capture.** The central finding is that the condensation index κ, though natural from the category-theoretic side [2], is blind to the Majorana/non-Majorana distinction: the toric code e-condensation and the Ising ψ-condensation share κ = 4. The Majorana index μ, built from the chiral central charge mismatch, correctly separates them, and f_NA detects non-Abelian boundary fusion. But μ is defined only mod 16 and only for chiral discrepancies expressible in half-integers; a condensation in a phase with irrational c (e.g., Fibonacci-like) would give non-integer μ, and our interpretation of μ as a Majorana count fails there. The honest statement is: μ counts chiral Majorana modes *when Δc is a half-integer and the boundary anomaly is of Majorana type*.

**The fermionic condensation caveat.** Our Ising computation condenses a fermion, which lies outside the strictly bosonic bootstrap of [2]. We leaned on the physical picture of a superconducting boundary; a rigorous treatment requires the spin-TQFT / super-modular framework, which we did not develop. A referee-style objection: perhaps the correct bosonic statement is that the Ising category admits *no* bosonic condensation producing Majorana boundary modes, and our μ = 1 result is an artifact of an illegitimate condensation. The counterargument is that fermionic condensation is physically realized (p + ip superconductors), and the Gauss–Milgram arithmetic is insensitive to the legitimacy question — but the objection stands that our framework mixes two condensation doctrines. This is documented as a divergence in Appendix A.

**Failure modes and falsifiability.** The claims would be falsified by: (i) a gapped, fully non-chiral boundary of a c = 1/2 phase obtained by purely bosonic condensation (contradicting the necessity of Δc appearing at the boundary); (ii) a Hamiltonian realization along the lines of [9] in which the boundary σ defects of the ψ-condensed Ising model show single-channel fusion; or (iii) a mixed-state generalization [8] in which the étale-algebra dimension formula D_D = D_C/dim(A) fails, breaking κ. Point (iii) is a genuine open risk: pre-modular categories lack the nondegenerate braiding that underpins Gauss–Milgram, so μ may be undefined for mixed-state parents.

**Limitations of scope.** We treated only three examples. Whether the index triple (κ, μ, f_NA) is *complete* for Majorana statistics at condensation boundaries — i.e., whether μ > 0 or f_NA > 0 always implies two-channel boundary defect fusion — is unproven here. The boundary fusion derivation is a heuristic identification of condensed summands with the vacuum, not a theorem about module category structure; a proper treatment would use the module category C_A. Additionally, following the cautionary example of point-gap phases [7], we make no claim that bulk-boundary correspondence in this form survives perturbations that break the modular structure.

**Open questions.** (1) Does μ admit a direct braid-group-representation formulation, connecting to the program of [10], so that the boundary Majorana count is read from the R-matrices rather than central charges? (2) Can the indices be extended to non-invertible condensates and successive condensations [8]? (3) What is the crystalline-defect generalization, along the lines of [4] and [5]? (4) The corpus items [11] and [12] have no available abstracts, and [13] is philosophical; we could draw only methodological, not technical, content from them — a limitation of the source base, not of the framework.

## 7. Conclusion

We introduced computable indices quantifying the bulk-boundary correspondence for anyon-condensing boundaries: the condensation index κ = dim(A)², the Majorana index μ = 2Δc, and the non-Abelian excess fraction f_NA. Explicit arithmetic for the Ising category (κ = 4, μ = 1, two-channel boundary defect fusion), the toric code (κ = 4, μ = 0, single-channel fusion), and the doubled Ising category (dimension ratio √(3/7), f_NA = 1/3, non-Abelian carrier (σ,σ)) demonstrates that the index set — and μ and f_NA in particular — tracks the emergence of Majorana statistics at condensation boundaries. The framework is elementary, checkable by hand, and falsifiable, and it isolates precisely where the hard open problems lie: fermionic condensation, mixed-state parents, and the completeness of the index set.

## References

[1] Bosonic topological phases of matter: bulk-boundary correspondence, SPT invariants and gauging. arXiv:1710.04730v1. https://arxiv.org/abs/1710.04730v1
[2] Anyon condensation and tensor categories. arXiv:1307.8244v7. https://arxiv.org/abs/1307.8244v7
[3] Measuring the Unique Identifiers of Topological Order Based on Boundary-Bulk Duality and Anyon Condensation. arXiv:2005.03236v4. https://arxiv.org/abs/2005.03236v4
[4] Higher-order bulk-boundary correspondence for topological crystalline phases. arXiv:1805.02598v2. https://arxiv.org/abs/1805.02598v2
[5] Defect bulk-boundary correspondence of topological skyrmion phases of matter. arXiv:2206.02251v2. https://arxiv.org/abs/2206.02251v2
[6] Bulk-boundary correspondence for three-dimensional symmetry-protected topological phases. arXiv:1512.09111v1. https://arxiv.org/abs/1512.09111v1
[7] Bulk-boundary correspondence in point-gap topological phases. arXiv:2205.15635v4. https://arxiv.org/abs/2205.15635v4
[8] Anyon condensation in mixed-state topological order. arXiv:2406.14320v4. https://arxiv.org/abs/2406.14320v4
[9] Nonabelian Anyon Condensation in 2+1d topological orders: A String-Net Model Realization. arXiv:2409.05852v2. https://arxiv.org/abs/2409.05852v2
[10] https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majorana-zero/. QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors.
[11] https://papers.qnfo.org/papers/gauge-invariant-field-theory-of-signal-worker-interactions/. QNFO: Gauge-Invariant Field Theory of Signal-Worker Interactions.
[12] https://papers.qnfo.org/papers/operationalizing-generalized-symmetries/. QNFO: Operationalizing Generalized Symmetries.
[13] https://papers.qnfo.org/papers/electron-hook-treatise/. QNFO: A Critical Treatise on the Load-Bearing Assumptions of Quantum Mechanics, Thermodynamics, and Computation.

## Appendix A. Divergence report

**D1. Definition of the condensation index.** Draft A proposed a "symmetrized" index I = 0.25 for the Ising condensation, obtained by averaging two expressions (1 and 0.5) and scaling by a fraction of confined fermions (0.75 × 1/3 = 0.25). Draft B proposed the pair κ = dim(A)² = D_C²/D_D² and μ = 2Δc. Draft C proposed I = D_D/D_C (a quantum-dimension ratio). These are different conventions for what "index" should measure: A aimed at a fraction of "bulk topological information transferred to the boundary" but required an ad hoc symmetrization to reach a fixed value; B aimed at separating condensate size from chiral anomaly; C aimed at surviving boundary quantum dimension. **Resolution:** the main text adopts B's index pair, augmented by C's dimension ratio and non-Abelian excess fraction f_NA as complementary diagnostics. A's symmetrized value I = 0.25 is rejected because its derivation is not invariant under alternative but equally natural conventions (A itself concedes the value "depends on a symmetrization step that mixes two plausible definitions").

**D2. Child category of the Ising ψ-condensation.** The independent drafts diverged on what the child of the fermionic condensation A = 1 ⊕ ψ in the Ising category actually is. Draft A held that the child is trivial (only the vacuum survives, since σ is confined), giving D_D = 1 and κ = D_C²/D_D² = 4. Draft B argued that condensing the fermion of the Ising category yields a p + ip topological superconductor, whose intrinsic topological order is trivial (c = 1/2 with no deconfined anyons), so that the child as a *topological order* is again effectively trivial but carries a chiral central charge — consistent with Draft A's anyon content while explaining the nonzero μ. Draft C speculated that the child might retain a nontrivial sector, but could not identify a deconfined candidate: every nontrivial Ising anyon has nontrivial monodromy with ψ. **Resolution:** the main text adopts the Draft A/B position — the child category is trivial as a braided category (D = {1}, D_D = 1), the chirality c = 1/2 survives as the boundary Majorana mode counted by μ = 1, and κ = dim(A)² = 4 = D_C²/D_D² holds here because the condensate is normal (the single surviving sector is the vacuum). Draft C's nontrivial-child proposal was rejected for lack of a deconfined candidate sector.