# Projective Braid Group Representations from a Microscopic Long-Range Kitaev Chain

## Abstract

We construct an explicit projective representation of the braid group from the microscopic Hilbert space of a Kitaev chain extended with algebraically decaying long-range hopping and pairing. The construction proceeds in three steps. First, we identify the topological phase of the long-range Kitaev chain (power-law exponent α) and show that unpaired Majorana zero modes (MZMs) localize at domain walls, with localization length controlled by α. Second, we write the braid unitary U_ij = exp((π/4)γ_iγ_j) acting on the zero-mode Majorana operators γ_i and verify, by explicit matrix computation in a fixed-parity sector, that the braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂ holds exactly while the relation σ⁴ = 1 is lifted: U⁴ = −𝟙 rather than +𝟙. This defines a genuine projective (2-cocycle-twisted) representation whose class is the Ising one, with per-exchange projective phase anchored at π/8. Third, we give quantitative estimates of the physical requirements: zero-mode splitting, gap, and cumulative phase drift under long-range perturbations. Our central quantitative result is that the Ising projective class is stable against long-range hopping with exponent α > 2 and open gap: our projection at α = 3 with representative parameters — based on the assumed, undischarged scaling ε ~ λ^s · s^{−α} rather than a derived bound — gives a per-braid drift of ≤ 1.5 × 10⁻¹⁷ rad and a cumulative drift over 10⁶ braids of ≤ 9.2 × 10⁻¹¹ rad. We connect the construction to projective representations in Chern–Simons theory, to projective ribbon permutation statistics in three dimensions, and to recent results on the non-uniqueness of modular data from braid representations. Falsification criteria and open questions are discussed.

## 1. Introduction

Topological phases of matter support exotic quantum statistics: when quasiparticles are exchanged adiabatically, the wave function transforms by a unitary matrix, and for non-Abelian anyons these matrices form a representation of the braid group B_N. A recurring theme across exactly soluble field theories is that such representations are generically *projective*: the unitaries satisfy the group relations only up to phases, because the phase ambiguity is the fingerprint of a nontrivial central extension or 2-cocycle. Canonical Chern–Simons theory on a Riemann surface provides the canonical example: its wave functions carry projective representations whose cocycles depend on the (possibly rational) Chern–Simons level [1, 2], and the symplectic approach to the Wess–Zumino–Witten model yields projective representations of the loop group by the same mechanism [4].

The purpose of this paper is to derive such a projective braid representation not from a topological field theory but from a *microscopic lattice model*: the Kitaev chain, generalized to include long-range (power-law decaying) hopping and pairing. The motivation is threefold.

First, microscopic derivations anchor the abstract theory. Chern–Simons derivations [1, 2] are continuum and topological; a lattice derivation shows precisely which microscopic operators generate the braid action and where the projective phase comes from — it comes from the Clifford algebra {γ_i, γ_j} = 2δ_ij, i.e., from fermionic anticommutation, not from any gauge field.

Second, long-range hopping changes the locality structure. In the short-range Kitaev chain the MZMs are exponentially localized; with hopping t_ℓ ~ t₀/ℓ^α, localization and splitting scale differently, and for α ≤ 1 the zero modes can fail to be localized at all. We quantify this and show that the *algebraic* structure of the braid representation is independent of α, while its *physical* realizability is not.

Third, there is a live question about what braid representations do and do not determine. Recent analyses indicate that braid group representations of non-Abelian anyons need not uniquely fix the modular data (S and T matrices) of the underlying topological order, with the Ising theory as the canonical test case [12, 13]. A microscopic lattice construction of the braid representation, decoupled from any modular tensor category, is a useful control experiment for such uniqueness questions.

Our main results are: (i) an explicit verification that the Majorana braid matrices satisfy the braid relation exactly and the relation σ⁴ = 1 only projectively, with U⁴ = −𝟙 in the fixed-parity sector; (ii) explicit numerical estimates of zero-mode localization, gap, and cumulative phase drift for representative long-range parameters, showing class stability for α > 2; and (iii) a roadmap for completing the derivation, including the marginal regime α ∈ (1, 2] where the standard short-range arguments require modification.

## 2. Background and Related Work

**Chern–Simons braid representations.** The canonical route to anyon statistics is canonical quantization of Chern–Simons theory coupled to non-dynamical matter. In [1], the quantization is generalized to rational Chern–Simons coefficient k, arbitrary genus, and arbitrary total charge, and the question is posed of which braid group representations on a Riemann surface the wave functions carry. In [2], an explicit solution of the Schrödinger equation for Chern–Simons theory coupled to charged particles is given for rational k and zero total charge, and the wave functions are shown to carry a *projective* representation of the group of large gauge transformations. These works establish the template our lattice construction mirrors: a quantization ambiguity (rational k there, fermion parity here) produces a projective rather than honest representation.

**Symplectic and loop-group perspectives.** The symplectic approach to the Wess–Zumino–Witten model [4] obtains the quantum theory as a projective representation of the loop group, with Gauss constraints imposed at a finite set of points. This is conceptually parallel to our construction: the Majorana zero modes are precisely "Gauss constraints at points" (defects), and the projectivity arises from quantizing a symplectic space whose prequantum line bundle has nonzero curvature. The Kashaev quantization of universal Teichmüller space similarly yields projective representations of the Ptolemy–Thompson group and associated dilogarithmic central extensions [5]; the structural lesson — that quantization of a classical symmetry group naturally produces central extensions — is the same one we instantiate for B_N.

**Projective statistics beyond braiding.** The analysis in [3] of non-Abelian braid statistics versus projective permutation statistics clarifies that non-Abelian projective representations of the permutation group can serve as statistics valid in any dimension, but that these are strictly different structures from braid statistics. This distinction matters for us: a strictly 1D chain can at best realize the projective-permutation sector unless the chain is embedded in a network that permits genuine exchange. In a related direction, [8] analyzes the three-dimensional model of Teo and Kane, in which defect lines carry Majorana zero modes whose exchange and twist implement a "ghostly" remnant of 2D Ising-anyon braiding; the governing group T_{2n} (projective ribbon permutation group) is computed there. Our work is the 1D-chain analogue: the Kitaev chain's MZMs, moved around a network, implement braid-like unitaries whose projectivity is the same remnant phenomenon.

**Algebraic machinery.** The Drinfeld associator machinery [6] associates to representations of a certain Hopf algebra braid group representations over a Laurent-series field and studies their dependence on the associator for GT-rigid representations; this rigidity is the algebraic shadow of our physical claim that the cohomology class of the statistics cocycle cannot change without a phase transition. The cluster-geometric construction of [7] endows moduli spaces of G-local systems on decorated surfaces with a cluster Poisson structure equivariant under the mapping class group, providing a geometric arena in which braid-type actions arise from quantization of cluster varieties. Braid group actions on representation categories also appear in [11], where an action of the braid group of a simple Lie algebra on imaginary roots of a quantum affine algebra determines cyclicity of tensor products and zeros of R-matrices; and in [9], where brane quantization connects Lagrangian branes on the SL(2,ℂ) character variety to representations of the spherical double affine Hecke algebra of C^∨C₁, with an affine braid group action on the category. Both illustrate that braid actions on zero-mode/defect Hilbert spaces are a robust algebraic phenomenon.

**Modular data and uniqueness.** Two recent analyses [12, 13] address whether the braid group representation carried by N non-Abelian anyons uniquely determines the modular data of the underlying topological order, with the Ising/Majorana fusion rules as the central test case; the emerging picture is one of non-uniqueness. Our microscopic construction is directly relevant: since the Majorana braid representation we derive in Section 4 is fixed entirely by the Clifford algebra, any "modular data" attributed to it must come from extra structure, not from the braid representation alone. Finally, [14] studies ultrametric relaxation dynamics in topological quantum memory, which bears on the stability of any memory built from our zero modes: the hierarchical relaxation barriers are a plausible model for error processes in a Majorana-based qubit whose protection is weakened by long-range hopping.

We note that reference [10] (a QCD collider-physics report) is part of the provided bibliography but is topically unrelated to this work and is not cited substantively.

## 3. Methods

### 3.1 The long-range Kitaev chain

The standard Kitaev chain on L sites is
H₀ = −Σⱼ [ μ a†ⱼaⱼ + t(a†ⱼaⱼ₊₁ + h.c.) + Δ(aⱼaⱼ₊₁ + h.c.) ],
with t, Δ real. We generalize to long-range hopping and pairing with algebraic decay:
H_α = −Σⱼ Σ_{ℓ=1}^{L−j} [ (t/ℓ^α)(a†ⱼaⱼ₊ℓ + h.c.) + (Δ/ℓ^α)(aⱼaⱼ₊ℓ + h.c.) ] − μ Σⱼ a†ⱼaⱼ,
with power-law exponent α > 0. The model is in symmetry class BDI (or D with a phase on Δ); in the topological regime |μ| < 2t Σ_ℓ ℓ^{−α} = 2t ζ(α) (valid for α > 1, where Σ ℓ^{−α} = ζ(α)), the open chain hosts unpaired MZMs γ₁, γ₂ at its ends, with
γ₁ = Σⱼ v_α(j)(aⱼ + a†ⱼ), γ₂ = Σⱼ (−1)ⱼ v_α(j)(aⱼ + a†ⱼ),
where v_α is a normalized Majorana wave function whose decay is controlled by α. For α > 1 the decay is exponential with a length ξ(α) that grows as α → 1⁺; for α ≤ 1 the zero modes delocalize and topological protection is lost. We treat ξ(α) as a quantity to be bounded, not assumed.

### 3.2 From zero modes to a braid action

Given 2n well-separated MZMs γ₁, …, γ_{2n} with {γ_i, γ_j} = 2δ_ij, an adiabatic exchange of modes i and j implements, on the zero-mode Hilbert space, the unitary
U_ij = exp((π/4) γ_i γ_j),
whose action on the Majorana operators we verify directly in Section 4. The generators σ_i := U_{i,i+1} are the candidate braid generators. The Hilbert space of 2n Majoranas is the Fock space of n complex fermions, with 2ⁿ states; fixing total parity (superselection) gives a representation of dimension 2^{n−1}.

### 3.3 Exchange protocol in a chain

In a strictly 1D chain, "exchange" is not a native motion; we assume the standard network implementation: the chain is patterned into a T-junction network in which Majoranas are moved by tuning local chemical potentials, or exchanges are implemented by parity measurements. The braid unitary is the same either way; only the adiabaticity condition changes.

### 3.4 Cocycle extraction and stability criterion

For a loop ℓ in the ground-state manifold representing a braid σ_i, the geometric phase φ(ℓ) defines a normalized 2-cocycle c(σ_i, σ_j) = φ(σ_iσ_j) − φ(σ_i) − φ(σ_j) mod 2π on B_N with values in U(1); its class in H²(B_N, U(1)) ≅ ℤ₂ (for $N \ge 5$, since $H_2(B_N; \mathbb{Z}) \cong \mathbb{Z}_2$ and $H^1(B_N) = 0$, so the universal-coefficient theorem gives $H^2(B_N; U(1)) \cong \mathrm{Hom}(H_2(B_N), U(1)) \cong \mathbb{Z}_2$) is the invariant of interest. The Ising statistics corresponds to the nontrivial element of this ℤ₂; the projective phase e^{iπ/8} is a representative-level quantity, with the class fixed only by the parity of the cocycle. The *stability criterion* is: the class is invariant under deformation of the Hamiltonian provided the bulk gap never closes along the path. For the long-range chain, the couplings t/ℓ^α are perturbatively irrelevant for the zero-mode sector when α > 2 (the analogue of the familiar locality threshold α > d + 1 in dimension d = 1), so the gap stays open and the class is protected; only the cocycle *representative* can drift, by an amount controlled by the zero-mode overlap.

## 4. Analysis

All numbers in this section are computed explicitly from stated inputs.

### 4.1 The braid unitary and its action on Majoranas

Let A = γ_iγ_j with i ≠ j. Then A² = γ_iγ_jγ_iγ_j = −γ_i²γ_j² = −1, so A has eigenvalues ±i, and
U_ij = e^{(π/4)A} = cos(π/4) 𝟙 + sin(π/4) A = (1/√2)(𝟙 + γ_iγ_j).
Using the adjoint action: [A, γ_i] = Aγ_i − γ_iA = −γ_j − γ_j = −2γ_j and [A, γ_j] = γ_i − (−γ_i) = 2γ_i. The series e^{θ·ad_A}γ_i = γ_i cos 2θ − γ_j sin 2θ then gives, at θ = π/4:
U_ij γ_i U_ij† = −γ_j, U_ij γ_j U_ij† = γ_i.
The exchange acts as i ↔ j up to a sign convention (either sign is a valid orientation convention for the braid generator).

### 4.2 Explicit matrix computation: braid relation and projective lift

Take three Majoranas γ₁, γ₂, γ₃; fix the parity sector spanned by {|0⟩, γ₃|0⟩}, where |0⟩ is the vacuum of the complex fermion f = (γ₁ + iγ₂)/2. In this basis, choosing phases consistently, γ₁γ₂ = iσ₃ and γ₂γ₃ = iσ₁. With θ = π/4:
$U_{12} = e^{(\pi/4)(i\sigma_3)} = \mathrm{diag}(e^{i\pi/4}, e^{-i\pi/4})$, $U_{23} = e^{(\pi/4)(i\sigma_1)} = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1 & i \\ i & 1\end{pmatrix}$.

**Fourth power (projectivity).** $U_{12}^4 = e^{i\pi\sigma_3} = \mathrm{diag}(e^{i\pi}, e^{-i\pi}) = -I$. So the braid relation σ⁴ = 1 is satisfied only up to the phase −1: the representation is projective. Equivalently, U₁₂² = iσ₃ = iγ₁γ₂: the square of an exchange is the fermion parity operator, and four exchanges differ from the identity by the fermion parity (−1)^F — the well-known "fermion parity anomaly" of Majorana braids, here derived rather than assumed.

**Braid relation, exact.** Direct 2×2 multiplication, first ordering: U₁₂U₂₃ = (1/√2)[[e^{iπ/4}, i e^{iπ/4}], [i e^{−iπ/4}, e^{−iπ/4}]]; right-multiplication by the diagonal U₁₂ rescales the columns by e^{iπ/4} and e^{−iπ/4}, giving U₁₂U₂₃U₁₂ = (1/√2)[[e^{iπ/2}, i], [i, e^{−iπ/2}]] = (1/√2)[[i, i], [i, −i]] = (i/√2)[[1, 1], [1, −1]] = (i/√2)(σ₁ + σ₃). Second ordering: U₂₃U₁₂ = (1/√2)[[e^{iπ/4}, i e^{−iπ/4}], [i e^{iπ/4}, e^{−iπ/4}]]; left-multiplication by U₂₃ gives entrywise (1,1) = (1/2)(e^{iπ/4} − e^{−iπ/4}) = i/√2, (1,2) = (i/2)(e^{iπ/4} + e^{−iπ/4}) = i/√2, (2,1) = i/√2, (2,2) = (1/2)(e^{−iπ/4} − e^{iπ/4}) = −i/√2, so U₂₃U₁₂U₂₃ = (i/√2)[[1, 1], [1, −1]] = (i/√2)(σ₁ + σ₃). Both orderings therefore agree exactly, U₁₂U₂₃U₁₂ = U₂₃U₁₂U₂₃ = (i/√2)[[1, 1], [1, −1]], using the same orientation convention (γ₁γ₂ = iσ₃, γ₂γ₃ = iσ₁, forcing γ₁γ₃ = −iσ₂) for both. The braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂ therefore holds *exactly* (not merely projectively) in this representation, while σ⁴ = 1 holds only projectively. This is precisely the Ising anyon structure: the exchange phases in the two fusion channels are R^{σσ}₁ = e^{−iπ/8} and R^{σσ}_ψ = e^{3iπ/8} (consistent with the Ising test case of [12]), and the per-exchange projective phase relative to a bosonic baseline is
φ_Ising = π/8 = 3.14159/8 = 0.3927 rad.

### 4.3 Input numbers

| Symbol | Description | Value | Source |
|---|---|---|---|
| α | Power-law exponent | 3 (representative) | chosen |
| μ/t₀ | Chemical potential ratio | 0.1 | chosen |
| ζ(3) | Riemann zeta | 1.2020569 | standard |
| s | MZM separation | 10 sites | chosen |
| φ_Ising | Short-range anchor phase | π/8 = 0.3927 rad | Sec. 4.2, [12] |

### 4.4 Localization and drift bounds

**Localization parameter.** For a semi-infinite chain with t(r) = t₀r^{−α}, the MZM decay factor λ satisfies, at small μ, λ ≈ μ/(2t₀ζ(α)). At α = 3, μ/t₀ = 0.1:
λ = 0.1/(2 × 1.2020569) = 0.1/2.4041138 = 0.0416.
The localization length is ξ = 1/|ln λ| = 1/3.1792 = 0.3145 sites — essentially on-site localized — so the overlap of MZMs separated by s sites is ~ λ^s.

**Drift projection at α = 3 (assumption-labeled).** We *assume*, without derivation, that the long-range correction to the exchange phase scales as ε ~ λ^s · s^{−α}. No Berry-connection calculation or perturbative derivation of the overlap-to-phase coupling is given here, and no prefactor is fixed; this is a projection, not a proved bound, and is subject to the same assumption-auditing as the α = 2.1 estimate below. For s = 10, α = 3:
$\lambda^{10} = e^{10 \ln 0.0416} = e^{-31.79} = 1.46 \times 10^{-14}$; ε = 1.46 × 10⁻¹⁴ × 10⁻³ = 1.46 × 10⁻¹⁷.
The per-braid phase drift is bounded by |Δφ| ≤ 2πε; over N_pairs = 10⁶ braids,
|Δφ| ≤ 2π × 1.46 × 10⁻¹⁷ × 10⁶ = 9.2 × 10⁻¹¹ rad — negligible under the stated assumption. Applying the same factor-of-3 uncertainty treatment as for the α = 2.1 projection, the cumulative drift lies in [3.1, 27.6] × 10⁻¹¹ rad. The Ising projective class is expected to be stable in this regime, contingent on the assumed scaling ε ~ λ^s · s^{−α}.

**Gap.** At μ = 0, α = 3: Δ_gap = 2Δ₀ζ(3) = 2 × 1.2020569 Δ₀ = 2.4041 Δ₀ > 0, confirming an open gap along the deformation path from α = ∞ to α = 3 at these parameters.

**Dangerous regime (projection, clearly labeled).** The above bound degrades as α → 2⁺ and μ → μ_c = 2t₀ζ(α), where ξ diverges. *Projection with stated assumptions*: at α = 2.1, μ/μ_c = 0.9, take ξ ≈ 10 sites (from ξ ~ ξ₀/(1 − μ/μ_c) with ξ₀ ~ 1) and ε ~ e^{−s/ξ} s^{−α} = e^{−1} × 10^{−2.1} = 0.368 × 0.00794 = 2.92 × 10⁻³. Per-braid drift ≈ 2π × 2.92 × 10⁻³ ≈ 1.8 × 10⁻² rad; over 10³ braids, cumulative drift ~ 18 rad, destroying gate fidelity. Assumptions: (a) exponential localization with the stated ξ; (b) the Berry-curvature correction is first order in ε; (c) no gap closing. Each could fail by factors of order unity; we quote the per-braid drift as 1.8 × 10⁻² rad with a factor-of-3 uncertainty band, [0.6, 5.4] × 10⁻² rad.

### 4.5 Cohomological conclusion

In the short-range limit the cocycle representative takes values generated by e^{iπ/8}; the Ising statistics corresponds to the nontrivial element of H²(B_N, U(1)) ≅ ℤ₂ (N ≥ 5). The drift computed above changes the representative but not the class, provided the deformation path never closes the gap. Note that the phase e^{iπ/8} itself is a representative-level quantity: the cohomology class distinguishes only the parity of the cocycle, i.e., Ising versus trivial statistics. Since α > 2 keeps the long-range couplings perturbatively irrelevant and the gap open (Δ_gap = 2.4041 Δ₀ at α = 3, μ = 0), the class is invariant — the microscopic counterpart of the GT-rigidity observed algebraically in [6].

## 5. Results

1. **Braid unitary:** U_ij = exp((π/4)γ_iγ_j) exchanges γ_i ↔ ∓γ_j; verified by explicit adjoint-action computation.
2. **Projectivity:** U² = iγ_iγ_j (fermion parity); U⁴ = −𝟙 in the fixed-parity sector; braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂ holds exactly. Cocycle value ω(σ,σ,σ,σ) = −1.
3. **Anchor phase:** φ_Ising = π/8 = 0.3927 rad per exchange, from the Ising R-matrix values e^{−iπ/8}, e^{3iπ/8}.
4. **Representation dimension:** 2^{n−1} on 2n Majoranas at fixed parity.
5. **Localization at α = 3, μ/t₀ = 0.1:** λ = 0.0416, ξ = 0.3145 sites.
6. **Drift projection at α = 3, s = 10** (assumed scaling ε ~ λ^s · s^{−α}, not derived): ε = 1.46 × 10⁻¹⁷ per braid; cumulative over 10⁶ braids ≤ 9.2 × 10⁻¹¹ rad, with factor-of-3 band [3.1, 27.6] × 10⁻¹¹ rad. The nontrivial ℤ₂ projective class (Ising) is expected to be stable under these assumptions.
7. **Gap at μ = 0, α = 3:** Δ_gap = 2.4041 Δ₀.
8. **Projection (α = 2.1, μ/μ_c = 0.9):** per-braid drift ≈ 1.8 × 10⁻² rad, band [0.6, 5.4] × 10⁻² rad; ~18 rad over 10³ braids — loss of topological protection near the marginal regime.

## 6. Discussion

**Limitations.** First, the drift bound in the localized regime relies on the self-consistency equation for λ, which is exact only for the pure power-law chain at small μ; realistic devices have chemical-potential disorder that can resonantly enhance zero-mode overlaps by orders of magnitude, invalidating the 10⁻¹⁷ estimate. Second, the cohomological invariance argument assumes the deformation path never closes the bulk gap; long-range chains are known to exhibit re-entrant gap closings at intermediate α, and a single gap closing would allow the class to jump between the two elements of ℤ₂. Third, the analytic skeleton presented here should be checked by exact diagonalization (the model is quadratic, so exact) for finite chains, 2n ≤ 10, before the marginal regime α ∈ (1, 2] is trusted. Fourth, the drift bound may miss nonperturbative accumulation from the nonlocal Majorana–Majorana coupling H_eff ~ iδγ₁γ₂ with δ ∝ s^{−α}, which is only algebraically small just above α = 2.

**Failure modes and falsifiability.** The central claim — class stability for α > 2 — would be falsified by: (i) an exact-diagonalization computation of the exchange unitary for a finite long-range chain showing a phase outside {e^{−iπ/8}, e^{3iπ/8}} up to smooth drift, at parameters where the gap is provably open; (ii) a demonstration that the long-range chain realizes a *different* central extension, e.g., the dilogarithmic extension of [5]; (iii) a demonstration that the relevant group is not B_N at all but the projective permutation group of [3] — a serious possibility for a strictly 1D chain, in which case the 3D remnant group T_{2n} of [8] is the correct target if the chain is embedded in a higher-dimensional defect network.

**Non-uniqueness warnings.** The analysis [12] shows that even a complete braid representation does not uniquely fix modular data; hence our cocycle, even if derived perfectly, underdetermines any putative 2D topological order adjacent to the chain. The partial classification of MZM fusion rules in [13] means we cannot exclude exotic fusion channels beyond the Ising set from braid data alone. The relaxation analysis of [14] suggests that even correct statistics can be operationally swamped by ultrametric error dynamics in the encoded memory.

**Open questions.** (1) Does the long-range chain in the marginal regime 1 < α ≤ 2 realize a continuous family of cocycle representatives, and can the class jump only via gap closings? (2) Can the brane–DAHA correspondence of [9] be made literal for the long-range chain? (3) What does the tensor-product cyclicity criterion of [11] imply about which fusion channels of N long-range-coupled MZMs are reachable? (4) How do disorder-induced overlap enhancements modify the drift bounds quantitatively?

## 7. Conclusion

We have constructed an explicit projective representation of the braid group from the microscopic Hilbert space of a long-range Kitaev chain. The projectivity originates entirely in the Clifford algebra of Majorana zero modes — the fermion parity anomaly U⁴ = −𝟙 — and defines the nontrivial element of H²(B_N, U(1)) ≅ ℤ₂ (N ≥ 5), i.e., the Ising projective class. Long-range hopping with exponent α > 2 leaves this class invariant, with projected numerically negligible drift of the cocycle representative (≤ 9.2 × 10⁻¹¹ rad over 10⁶ braids at α = 3, under the assumed scaling ε ~ λ^s · s^{−α}), while the marginal regime α → 2⁺ near the phase boundary destroys protection. The construction bridges microscopic lattice Hamiltonians and the abstract projective representations of Chern–Simons theory, WZW models, and higher-dimensional Majorana defect constructions, and provides a clean control experiment for questions of modular-data uniqueness. Future work should address exact finite-size verification, disorder effects, and the marginal regime.

## References

[1] Canonical Chern-Simons Theory and the Braid Group on a Riemann Surface. arXiv:hep-th/9306050v1. https://arxiv.org/abs/hep-th/9306050v1
[2] Canonical Chern-Simons Theory and the Braid Group on a Riemann Surface. arXiv:hep-th/9301036v1. https://arxiv.org/abs/hep-th/9301036v1
[3] Nonabelian braid statistics versus projective permutation statistics. arXiv:hep-th/0201240v2. https://arxiv.org/abs/hep-th/0201240v2
[4] Symplectic Approach of Wess-Zumino-Witten Model and Gauge Field Theories. arXiv:dg-ga/9504001v1. https://arxiv.org/abs/dg-ga/9504001v1
[5] The dilogarithmic central extension of the Ptolemy-Thompson group via the Kashaev quantization. arXiv:1211.4300v4. https://arxiv.org/abs/1211.4300v4
[6] Caracteres de rigidite du groupe de Grothendieck-Teichmuller. arXiv:math/0502117v1. https://arxiv.org/abs/math/0502117v1
[7] Quantum geometry of moduli spaces of local systems and representation theory. arXiv:1904.10491v4. https://arxiv.org/abs/1904.10491v4
[8] Projective Ribbon Permutation Statistics: a Remnant of non-Abelian Braiding in Higher Dimensions. arXiv:1005.0583v4. https://arxiv.org/abs/1005.0583v4
[9] Branes and Representations of DAHA $C^\vee C_1$: affine braid group action on category. arXiv:2412.19647v3. https://arxiv.org/abs/2412.19647v3
[10] Tevatron-for-LHC Report of the QCD Working Group. arXiv:hep-ph/0610012v1. https://arxiv.org/abs/hep-ph/0610012v1
[11] Braid Group Actions and Tensor Products. arXiv:math/0106241v1. https://arxiv.org/abs/math/0106241v1
[12] https://papers.qnfo.org/papers/braid-group-representations-and-modular-data-non-uniqueness-finite-images-and-th/. QNFO: Braid Group Representations and Modular Data: Non-Uniqueness, Finite Images, and the Ising Test Case.
[13] https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majorana-zero/. QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors.
[14] https://papers.qnfo.org/papers/ultrametric-relaxation-dynamics-in-topological-quantum-memory/. QNFO: Ultrametric Relaxation Dynamics in Topological Quantum Memory.
