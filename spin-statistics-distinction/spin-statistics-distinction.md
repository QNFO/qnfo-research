---
title: "The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant"
author: "Rowan Brad Quni-Gudzinas"
affiliation: "QNFO"
ORCID: "0009-0002-4317-5604"
date: "2026-08-16"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: "10.5281/zenodo.21962904"
status: "published"
---

## Abstract

The textbook dichotomy between bosons and fermions is commonly presented as a primitive classification of nature, with the spin-statistics theorem as its iron law. This paper argues that the dichotomy is a derived, dimension-dependent shadow of a single structural relation: the exchange phase of identical particles equals their topological spin, $R = e^{2\pi i s}$. [ESTABLISHED] The relation holds across relativistic quantum field theory, topological field theory, and condensed-matter anyon systems; dimension enters only by quantizing the allowed values of $s$. [RETRODICTION — not evidence] Stating this as a single invariant is a unification of established results, not a new prediction. After stating the invariant and its dimensional quantization, the paper addresses a foundational question: whether a calculus whose primitive is the distinction — rather than the particle or the field — can derive exchange statistics from the act of distinction itself. A recent monograph in this tradition (Quni-Gudzinas, 2026a) exhibits the gap [textual finding]: the model of its exponential modality silently adopts the symmetric algebra, which corresponds to bosonic statistics, without deriving that choice from the primitive. The paper formalizes the required construction — two modal exponentials (symmetric and
exterior), the braiding of two marks in a compact closed category (with the abelian-pair
postulate made explicit), and the ribbon condition linking twist to exchange — and
states the falsifiability conditions under which the derivation program succeeds or
fails. [NOT YET EVIDENCE] The derivation is pre-registered here; it is not yet executed.

## 1. Introduction

Two identical particles can be exchanged. In quantum mechanics, the state of the pair carries a phase under exchange: $\psi(x_2, x_1) = \eta\,\psi(x_1, x_2)$. In three or more spatial dimensions, exchanging twice is topologically trivial, so $\eta^2 = 1$ and $\eta \in \{+1, -1\}$: the two possibilities are bosons (symmetric, $\eta = +1$) and fermions (antisymmetric, $\eta = -1$). The spin-statistics theorem states which sign is realized: $\eta = (-1)^{2s}$, where $s$ is the spin (Pauli, 1940; Duck and Sudarshan, 1998). [ESTABLISHED]

This paper makes two claims. First, the structural invariant is not the dichotomy itself but the relation $R = e^{2\pi i s}$ between exchange phase and topological spin; the binary is a shadow of that relation in three spatial dimensions. Second, a distinction-based foundation of physics — a calculus whose only primitive is the act of drawing a boundary — must, to claim the spin-statistics connection, derive exchange statistics from the primitive; the current state of that program contains a silent assumption that this paper identifies and replaces with a concrete derivation target.

## 2. The invariant: exchange phase equals topological spin

The exchange of two identical particles is a loop in their configuration space. The phase acquired is a representation of the fundamental group of that space (Leinaas and Myrheim, 1977; Laidlaw and DeWitt, 1971). [ESTABLISHED] The rotation of a single particle by $2\pi$ is the twist. In a ribbon braided tensor category — the mathematical home of particle-like excitations in topological order — the two are linked by the ribbon identity:

$$\theta_X = \frac{\mathrm{Tr}_q(c_{X,X})}{d_X},$$

where $\theta_X$ is the twist (topological spin), $c_{X,X}$ the braiding, $d_X$ the quantum dimension, and $\mathrm{Tr}_q$ the quantum trace (Joyal and Street, 1993; Kitaev, 2006; Bakalov and Kirillov, 2001). [ESTABLISHED] For an abelian object, $d_X = 1$ and the identity reduces to

$$R = e^{2\pi i s},$$

the universal spin-statistics relation. This relation has been proven directly from wavefunctions for fractional quantum Hall quasiparticles (Trung et al., 2022; Nardin et al., 2022) and is realized experimentally as measurable fractional spin (Comparin et al., 2021). [ESTABLISHED]

## 2.1 The 3+1D shadow

In three or more spatial dimensions the braiding is symmetric (involutive): $c_{Y,X} \circ c_{X,Y} = \mathrm{id}$. Then $\theta_X^2 = 1$, so $e^{2\pi i s} = \pm 1$, forcing $s \in \{0, \tfrac{1}{2}\} \bmod 1$. Integer spin gives the trivial representation (bosons); half-integer spin gives the sign representation (fermions) (Pauli, 1940; Streater and Wightman, 1964). [ESTABLISHED]

## 2.2 The 2+1D generalization

In two spatial dimensions the braiding is not involutive: the exchange group is the braid group, and $\theta_X = e^{2\pi i s}$ can be any phase. Particles with fractional statistics — anyons — realize the continuous range of $s \in \mathbb{R}/\mathbb{Z}$ (Leinaas and Myrheim, 1977; Wilczek, 1982; Haldane, 1991; Mund, 2008). [ESTABLISHED]

## 2.3 What is invariant

Across both regimes, the invariant content is unchanged: superselection sectors, fusion rules, and braiding data, with the relation $R = e^{2\pi i s}$ (Wang and Wen, 2014; Johnson-Freyd, 2015). [ESTABLISHED] Dimension enters only through which braided structures are realizable. The binary dichotomy is therefore not the invariant; the relation is.

## 3. Dimension quantization: bosons and fermions as a 3+1D shadow

| Spatial dimension | Motion group | Braided structure | Allowed $s$ | Statistics |
|---|---|---|---|---|
| 2 | Braid group $B_n$ | Ribbon, non-symmetric | $s \in \mathbb{R}/\mathbb{Z}$ | Anyons, $R = e^{2\pi i s}$ |
| $\geq 3$ | Permutation group $S_n$ | Symmetric, involutive | $s \in \{0, \tfrac{1}{2}\} \bmod 1$ | Bosons ($\eta = +1$), fermions ($\eta = -1$) |

[ESTABLISHED] The table is the dimensional quantization of the spin parameter: in $d \geq 3$ the involutive braiding forces $2s \in \mathbb{Z}$; in $d = 2$ the quantization collapses to continuity. In $3{+}1$ dimensions a further input — microcausality and positive energy in a local relativistic theory — identifies which sign corresponds to which spin (Pauli, 1940; Duck and Sudarshan, 1998; Verch, 2001). [ESTABLISHED] That input is external to any purely algebraic derivation; the boundary is stated explicitly in Section 5.

## 4. The calculus of distinctions and its silent assumption

A distinction-based calculus begins with a mark: a boundary separating an inside from an outside. Its two primitive laws are Calling (idempotence: a mark repeated is the mark) and Crossing (involution: a boundary crossed twice returns to the unmarked state) (Spencer-Brown, 1969). A recent monograph develops this calculus toward physics, including a treatment of the half-turn phase $e^{i\pi} = -1$ and a claim that parity is the ancestor of physical spin-statistics (Quni-Gudzinas, 2026a, Section 2.3). [textual finding]

The monograph's Appendix A models its exponential modality with the symmetric algebra:

$$!A = \bigoplus_{n=0}^{\infty} S^n(A),$$

where $S^n(A)$ is the $n$-th symmetric power. The symmetric algebra is exactly the bosonic Fock construction: many-body states totally symmetric under exchange. [ESTABLISHED — the symmetric algebra realizes Bose statistics.] The monograph therefore *silently chooses bosonic statistics* as the semantic realization of its exponential, without deriving the choice from the act of distinction. [textual finding — verifiable against Quni-Gudzinas (2026a), Appendix A.]

The gap is structural, not cosmetic. The spin-statistics theorem is about the symmetry of the joint state of two identical marks under exchange; the calculus provides a phase for a single mark under rotation, but never constructs the exchange of two marks. The leap from "the mark has a half-turn phase" to "two marks anticommute" is asserted, not derived. (This assessment was reached independently in the deep-inquiry analysis of 2026-08-14; it is stated here as a checkable textual claim about the monograph.)

## 5. A derivation program

The program has three tasks, pre-registered with falsifiability conditions (Section 6).

**T1 — Two modal exponentials.** In a $\mathbb{Z}/2$-graded symmetric monoidal category with the graded braiding $\sigma_{A,B}(a \otimes b) = (-1)^{\lvert a \rvert \lvert b \rvert} b \otimes a$, the exchange operator $P = \sigma_{A,A}$ on $A \otimes A$ splits into two idempotent projectors,

$$P_{\mathrm{sym}} = \tfrac{1}{2}(1 + P), \qquad P_{\mathrm{antisym}} = \tfrac{1}{2}(1 - P),$$

whose eigenspaces are the symmetric and antisymmetric subspaces. [ESTABLISHED — elementary super-algebra.] For a mark of odd parity, the graded symmetric algebra coincides with the exterior algebra, so the symmetric and exterior exponentials,

$$!_S(A) = \bigoplus_{n} S^n(A), \qquad !_{\Lambda}(A) = \bigoplus_{n} \Lambda^n(A),$$

are the two grading components of one construction. The two statistics are the two eigenvalues of exchange. [DERIVATION SKETCH — P4 notebook T1.]

**T2 — The braiding of two marks.** In a compact closed category with a self-dual mark $M$, the exchange map $\sigma_{M,M}$ is a scalar $\eta \cdot \mathrm{id}$, and the ribbon identity forces $\eta = \theta_M$. In a symmetric category $\theta_M^2 = 1$, so $\eta = \pm 1$: the two eigenvalues of exchange are the boson and fermion signs. The sign $\eta = -1$ is the same $-1$ as the treatise's half-turn phase $e^{i\pi} = -1$. [DERIVATION SKETCH — P4 notebook T2.] The identification of $\eta = +1$ with Calling and $\eta = -1$ with Crossing is the mark-calculus reading of the two one-dimensional representations of the symmetric group.

**T3 — Dimension quantization.** The table in Section 3, with dimension entering only through the allowed braided structures. [DERIVATION SKETCH — P4 notebook T3.]

**The boundary of the program.** The program can show that statistics is forced by distinction, compact closure, an involutive braiding, and the abelian-pair postulate (the pair of marks has a unique joint state up to phase, so that the braiding acts by a scalar). The last postulate is the categorical counterpart of the exclusion of parastatistics: without it, mixed-symmetry (parastatistics-class) sectors are not excluded by the algebraic machinery alone; in algebraic quantum field theory the exclusion follows from locality (Doplicher, Haag, and Roberts, 1971, 1974; Doplicher and Roberts, 1990; Greenberg and Messiah, 1965). The program therefore must either adopt the postulate or derive a DHR-style exclusion — which again lands on locality. [2026 note — two external developments qualify this boundary. First, a model-independent, quantum-information-theoretic exclusion of parastatistics has been given that does not route through locality at all: complete invariance under quantum permutations forces Bosons or Fermions (Mekonnen, Galley, and Mueller, 2025). Second, the classical equivalence theorems (Greenberg and Messiah, 1965; Doplicher, Haag, and Roberts) do not exhaust the possibilities: R-parastatistics — parastatistics inequivalent to bosons or fermions, consistently defined in any dimension — has been shown to emerge as observable quasiparticle statistics in condensed-matter systems (Wang and Hazzard, 2023, 2024, 2026). The abelian-pair postulate's status is thereby sharpened: its exclusion of parastatistics-class sectors is neither a purely algebraic consequence nor exclusively a locality theorem — it is a substantive physical assumption whose justification the new literature can either strengthen (quantum-permutation invariance) or qualify (emergent paraparticles).] It cannot, from the mark alone, show *which* eigenvalue corresponds to *which* spin: the spin–statistics *connection* requires the additional postulate that the twist equals the $2\pi$ rotation of a Lorentz representation, with microcausality and positive energy (Pauli, 1940; Duck and Sudarshan, 1998). The paper states this boundary explicitly; it does not claim a full derivation of the spin-statistics theorem from distinction. [CONTESTED — the sufficiency of the minimal postulates is open.]

## 6. Falsifiability conditions

**F1 (empirical).** If a stable, local, relativistic excitation in $3{+}1$ dimensions is observed with exchange phase $\eta \neq e^{2\pi i s}$ — for example, a spin-$\tfrac{1}{2}$ particle obeying Bose-Einstein statistics, or a spin-$0$ particle obeying Fermi-Dirac statistics — the claim that $R = e^{2\pi i s}$ is the universal invariant is disconfirmed. No such particle is known in the Standard Model. [ESTABLISHED — the absence of violations is a strong constraint, not a proof.]

**F2 (formal).** If the mark calculus cannot reproduce the two one-dimensional representations of $S_n$ (trivial and sign) from the primitive distinction, compact closure, an involutive braiding, and the abelian-pair postulate alone — without importing microcausality, Lorentz structure, or any other physical postulate — the derivation program is disconfirmed, and the monograph's spin-statistics claim stands as an asserted correspondence. (The abelian-pair postulate is a structural condition on the joint state of the pair, not a physical input; it is the minimal admission needed to exclude parastatistics-class sectors. Yang–Baxter alone forces the exchange phase to be uniform across pairs — see `artifacts/notebooks/t1-t2-dill-full-check.md` §3.)

**F2′ (2026-08-16, updated after the T2 rigor pass).** F2 as written above is *disconfirmed in its strong form* and is restated as follows. The category-theoretic rigor pass (companion notes `res009-gap6-t2-rigor-pass-2026-08-16.md` and `res009-gap6-t2-f-construction-2026-08-16.md`, live-verified 2026-08-16) established three results. (i) The exchange σ_{M,M} is scalar *iff* M⊗M is simple: abelianity (d_M = 1) is presupposed, not delivered, by the calculus. (ii) The interpretation functor F exists *iff* the target braiding is involutive (symmetric categories, or the Temperley–Lieb regime at A⁴ = 1): involutivity is a condition on the target, not a theorem of the calculus. (iii) The calculus's syntactic signature is the Lawvere theory of Boolean algebras: crossing is unary, and the binary exchange is added target structure. Consequently the mark calculus supplies the *syntax* of the involutive quotient (S_n = B_n/⟨σᵢ² = 1⟩, verified quantitatively in the Temperley–Lieb algebra: σᵢ² = A²I + (1 − A⁻⁴)Uᵢ), while the *selection* of the involutive quotient remains external kinematical input (π₁ of the configuration space: S_N for d ≥ 3, B_N for d = 2). **F2′ (surviving condition):** the derivability claim is restricted to the syntax of the two exchange channels — the two one-dimensional characters of the involutive quotient are realized as the idempotent projectors P± = (id ± σ)/2 (Calling's idempotence law), with the abelian-pair postulate retained as an explicit channel-count postulate tied to the locality-based exclusion of parastatistics (DHR 1971/1974). F2′ is not disconfirmed by the rigor pass; F2 as originally written is. [NOT YET EVIDENCE — the surviving claim is the pre-registered channel-count program]

**Surprise accounting (KIF-60 discipline).** The existence of anyons in $2{+}1$ dimensions is established and does not count as predictive evidence for this paper: anyonic statistics is expected under the null hypothesis of braid-group representations. Only F1's precision constraint and F2's derivability constraint carry evidential weight. The invariant formulation itself is [RETRODICTION — not evidence]: it restates established results in a unified language. The paper claims credit only for the derivation program (F2) and for the identification of the monograph's silent assumption (a textual finding).

## 7. Relation to existing programs

The derivation program sits between three established lines of work. First, the algebraic quantum field theory tradition proves the spin-statistics connection from locality and positivity (Streater and Wightman, 1964; Verch, 2001), and extends it to anyons in $2{+}1$ dimensions (Mund, 2008; Kuckert, 2002; Kuckert and Mund, 2004). Second, the topological and categorical tradition states the connection as a theorem about braided tensor categories (Joyal and Street, 1993; Bakalov and Kirillov, 2001; Johnson-Freyd, 2015; Oeckl, 2000), and condensed-matter physics realizes it for fractional quantum Hall quasiparticles (Comparin et al., 2021; Nardin et al., 2022; Trung et al., 2022). Third, the distinction-based tradition derives physical structure from the mark (Spencer-Brown, 1969; Quni-Gudzinas, 2026a, 2026b, 2026c). The present paper is the first, to the author's knowledge, to state the derivation target explicitly for the third tradition: the exchange of two marks, constructed in a compact closed category, whose eigenvalues are the two statistics. Adjacent internal work on p-adic anyon braiding (Quni-Gudzinas, 2026d) and on the topological distinction between Dirac and Majorana fermions (Quni-Gudzinas, 2026e) provides a compatible categorical language.

## 8. Conclusions

The boson/fermion dichotomy is not the primitive content of the spin-statistics theorem; the relation $R = e^{2\pi i s}$ between exchange phase and topological spin is. [ESTABLISHED] The dichotomy is its shadow in three spatial dimensions, where the involutive braiding quantizes $s$ to integers and half-integers. [ESTABLISHED] A distinction-based calculus that aims to ground quantum statistics must construct the exchange of two marks and derive the two eigenvalues of exchange from the primitive; the current monograph in that tradition silently assumes the symmetric (bosonic) algebra instead. [textual finding] This paper pre-registers the derivation program (T1-T3) and its falsifiability conditions (F1, F2), and states the boundary of the program: the spin-statistics *connection* requires Lorentz and locality input that the mark alone cannot supply. [NOT YET EVIDENCE]

## 9. The Parsimony Ledger (2026-08-16 update)

A ledger counts every primitive, labels each as DERIVED or ASSUMED, and states the standing debt — it prevents the Occam objection from being answered by relocation. *Counting convention:* one primitive = one named structural input not derived within the system.

| System | Primitives | Derives | Status |
|---|---|---|---|
| Standard QFT | 3D spacetime + locality, positivity, Lorentz | ±1 exchange **and** the spin–statistics connection | COMPLETE (Streater–Wightman 1964) |
| Mark calculus | mark + compact closure + involutive braiding + abelian-pair postulate + external Lorentz/locality input | the two exchange eigenvalues (±1) — the *syntax* of the involutive quotient | PRE-REGISTERED (F2′); NOT YET EVIDENCE |

**Row-by-row debt (definitive outcome of the T2 rigor pass, 2026-08-16).**
1. **Abelian-pair postulate** — **ASSUMED (definitive).** The demotion attempt failed honestly: scalar exchange follows *from* abelianity (M⊗M simple, d_M = 1); the calculus does not deliver it (rigor-pass Lemma 3; DD HARD-1 stands). The postulate is retained as an explicit channel-count postulate, tied to the locality-based parastatistics exclusion (DHR 1971/1974).
2. **Involutive braiding (σ² = 1)** — **ASSUMED (definitive).** The inheritance claim is resolved: F exists iff the target braiding is involutive — involutivity is a condition on the target (symmetric categories, TL at A⁴ = 1), not a theorem of the calculus (f-construction note). The calculus supplies the syntax of the quotient S_n = B_n/⟨σᵢ² = 1⟩; the selection remains external (d ≥ 3 kinematical input).
3. **Compact closure** — ASSUMED (structural input, never disputed).
4. **External Lorentz/locality input** — CONCEDED as boundary (paper §5). The spin–statistics *connection* requires the twist to equal the 2π rotation of a Lorentz representation; not derivable from the mark alone.
5. **The mark itself** — primitive (the program's single claimed primitive). Its primitiveness is itself a quotient-claim (UIA Q15: "what are the braid group, the mark, and SO(3) all quotients of?") and remains audited next.

**Quotient-direction neutrality (reviewer DESIGN-1/3).** S_n ≅ B_n / ⟨σᵢ² = 1⟩ (Artin) is neutral evidence: parsimony favors S_n as the exchange-statistics object until the mark calculus demonstrably *needs* B_n for 3D physics. The functorial form (f-construction): B_n is not a model of the calculus's signature; the calculus realizes the S_n reading natively.

**Verdict.** The mark calculus supplies the syntax of the involutive quotient; the selection of the involutive target is external kinematical input. F2 as originally written is disconfirmed; F2′ (channel-count postulate retained, tied to DHR locality) is the surviving pre-registered condition. This is the paper's §5 boundary, now stated as a ledger outcome rather than a concession.

## Declarations

**Funding.** No external funding.
**Conflicts of interest.** The author declares no conflicts of interest.
**Data availability.** No experimental data were generated. All external claims are documented in the evidence files accompanying the source repository.
**Code availability.** No code was required for the arguments presented; derivation notebooks are planned for the program's formal phase.
**Author contributions.** Sole author.
**Ethics approval.** Not applicable.
**Consent for publication.** Not applicable.
**Acknowledgments.** The author thanks the reviewers of the companion monograph for the discussion that sharpened Section 4.
**Correspondence.** rowan.quni@outlook.com

## References

Bakalov, B., and Kirillov, A. (2001). *Lectures on Tensor Categories and Modular Functors*. American Mathematical Society.

Comparin, T., Opler, A., Macaluso, E., Biella, A., Polychronakos, A. P., and Mazza, L. (2021). Measurable fractional spin for quantum Hall quasiparticles on the disk. arXiv:2112.02901.

Duck, I., and Sudarshan, E. C. G. (1998). Toward an understanding of the spin-statistics connection. *American Journal of Physics*, 66, 284. doi:10.1119/1.18860.

Doplicher, S., Haag, R., and Roberts, J. E. (1971). Local observables and particle statistics I. *Communications in Mathematical Physics*, 23, 199-230. doi:10.1007/BF01877742.

Doplicher, S., Haag, R., and Roberts, J. E. (1974). Local observables and particle statistics II. *Communications in Mathematical Physics*, 35, 49-85. doi:10.1007/BF01646454.

Doplicher, S., and Roberts, J. E. (1990). Why there is a field algebra with a compact gauge group describing the superselection structure in particle physics. *Communications in Mathematical Physics*, 131, 51-107.

Greenberg, O. W., and Messiah, A. M. L. (1965). Selection rules for parafields and the absence of para particles in nature. *Physical Review*, 138, B1155. doi:10.1103/PhysRev.138.B1155.

Haldane, F. D. M. (1991). "Fractional statistics" in arbitrary dimensions: A generalization of the Pauli principle. *Physical Review Letters*, 67, 937. doi:10.1103/PhysRevLett.67.937.

Johnson-Freyd, T. (2015). Spin, statistics, orientations, unitarity. arXiv:1507.06297.

Joyal, A., and Street, R. (1993). Braided tensor categories. *Advances in Mathematics*, 102, 20-78.

Kitaev, A. (2006). Anyons in an exactly solved model and beyond. *Annals of Physics*, 321, 2-111.

Kuckert, B. (2002). Spin & statistics in nonrelativistic quantum mechanics, I. arXiv:quant-ph/0208151.

Kuckert, B., and Mund, J. (2004). Spin & statistics in nonrelativistic quantum mechanics, II. arXiv:quant-ph/0411197.

Laidlaw, M. G. G., and DeWitt, C. M. (1971). Feynman functional integrals for systems of indistinguishable particles. *Physical Review D*, 3, 1375. doi:10.1103/PhysRevD.3.1375.

Leinaas, J. M., and Myrheim, J. (1977). On the theory of identical particles. *Nuovo Cimento B*, 37, 1-23.

Mekonnen, M., Galley, T. D., and Mueller, M. P. (2025). Invariance under quantum permutations rules out parastatistics. arXiv:2502.17576.

Mund, J. (2008). The spin-statistics theorem for anyons and plektons in d=2+1. arXiv:0801.3621.

Nardin, A., Ardonne, E., and Mazza, L. (2022). Spin-statistics relation for quantum Hall states. arXiv:2211.07788.

Oeckl, R. (2000). The quantum geometry of spin and statistics. arXiv:hep-th/0008072.

Pauli, W. (1940). The connection between spin and statistics. *Physical Review*, 58, 716.

Quni-Gudzinas, R. B. (2026a). The Calculus of Re-Entrant Distinctions: A Unified Treatise on the Loop, the Tree, and the Constants of Self-Reference. Zenodo. doi:10.5281/zenodo.21908818.

Quni-Gudzinas, R. B. (2026b). Syntactic Token Calculus: From the Logic of Distinction to the Coordinate-Free Cosmos. Zenodo. doi:10.5281/zenodo.19547736.

Quni-Gudzinas, R. B. (2026c). P-adic Spin, Information, and Ultrametric Internal Quantum Numbers. Zenodo. doi:10.5281/zenodo.21672990.

Quni-Gudzinas, R. B. (2026d). p-Adic Anyon Fusion and Braiding: Quantum Groups at Roots of Unity. Zenodo. doi:10.5281/zenodo.21208491.

Quni-Gudzinas, R. B. (2026e). Vanishing ZBW Signal: The ZBW-Majorana Hypothesis as a Unified Framework for Topological Fermion Distinction. Zenodo. doi:10.5281/zenodo.21574555.

Spencer-Brown, G. (1969). *Laws of Form*. George Allen and Unwin.

Streater, R. F., and Wightman, A. S. (1964). *PCT, Spin and Statistics, and All That*. Benjamin.

Trung, H. Q., Wang, Y., and Yang, B. (2022). Spin-statistics relation and the Abelian braiding phase for anyons in fractional quantum Hall effect. arXiv:2208.13786.

Verch, R. (2001). A spin-statistics theorem for quantum fields on curved spacetime manifolds in a generally covariant framework. *Communications in Mathematical Physics*, 223, 261. doi:10.1007/s002200100526.

Wang, J., and Wen, X.-G. (2014). Non-Abelian string and particle braiding in topological order. arXiv:1404.7854.

Wang, Z., and Hazzard, K. R. A. (2023). Particle exchange statistics beyond fermions and bosons. arXiv:2308.05203.

Wang, Z., and Hazzard, K. R. A. (2024). Parastatistics and a secret communication challenge. arXiv:2412.13360.

Wang, Z., and Hazzard, K. R. A. (2026). On R-parastatistics I: Foundation. arXiv:2607.26351.

Wilczek, F. (1982). Quantum mechanics of fractional-spin particles. *Physical Review Letters*, 49, 957.
