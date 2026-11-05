# The Universe Category: A Single Functor Encoding Quantization, Stability, and Factorization

## Abstract

This paper proposes a single categorical object — a functor from the divisibility
category of the positive integers to the category of smooth compact manifolds — and
investigates whether its image simultaneously encodes three structures that have
historically been treated as separate: quantization (integer-valued topological
invariants), stability (ultrametric hierarchy), and prime factorization (homology
rank). The functor $F: \mathcal{P} \to \mathcal{M}$ sends an integer $n$ to the
product of spheres $\prod_{p \mid \mathrm{rad}(n)} S^{p-1}$, where
$\mathrm{rad}(n)$ is the square-free kernel. By the Künneth formula the total
homology rank of the image is $2^{\omega(n)}$, where $\omega(n)$ is the number of
distinct prime factors. We verify this property computationally for all
$n \leq 100{,}000$ and verify the associated prime-power criterion: $n$ is a prime
power if and only if the homology rank of its image is exactly 2. The synthesis
claim — that quantization, stability, and factorization are three faces of one
categorical structure — is stated as a pre-registered conjecture with explicit
disconfirmation conditions. Consistent with the evidential-weight standards applied
throughout this research program, all structural correspondences identified here
are labeled [RETRODICTION — not evidence]: post-hoc syntheses carrying zero
independent evidential weight until novel predictions accrue.

## 1. Introduction

The deepest unresolved question at the interface of number theory, geometry, and
physics is not a single equation but a structural one: are the recurring patterns
that appear across these fields — quantized spectra, ultrametric hierarchies,
prime distributions — independent coincidences, or manifestations of a common
underlying object? This paper addresses that question through a concrete
categorical construction.

The starting point is a functor first defined in prior work on prime numbers as
optimization primitives [1]. That work showed that the property of being prime can
be reformulated as a topological invariant: an integer is a prime power if and only
if a canonically associated manifold has total homology rank 2. This paper extends
that construction in one direction: rather than asking what a single integer
encodes, we ask what the whole functor encodes. If the image of the functor can be
shown to carry quantization and stability structures alongside factorization, then
the functor constitutes a "universe category" — a single categorical object whose
image exhibits the three fundamental organizing principles of physical reality.

The project is explicitly framed as a pre-registered conjecture. The disconfirmation
conditions are stated in Section 6 before any observational or computational results
are presented, and the computational verification in Section 4 is a test of the
conjecture's most concrete leg.

## 2. Background

Three bodies of prior work motivate the construction.

**Topological invariants and quantization.** The Strange Loop program [2] derives
quantization from the necessity of integer-valued topological invariants as
stability mechanisms against continuous perturbation. The Lefschetz number
$L(R) = 2$ and winding number $w(R) = 1$ of a self-referential map on a compact
space are proposed as the blueprint of a self-stabilizing system. Whether these
invariants can be realized as invariants of a functor's image is a central question
of the present work.

**Ultrametric hierarchy and stability.** The Alpha Pi program [3] argues that the
continuous Archimedean geometry of the real numbers is the root of instability in
quantum systems, and that the ultrametric geometry of p-adic numbers — governed by
the strong triangle inequality $|x + y|_p \leq \max(|x|_p, |y|_p)$ — provides
intrinsic fault tolerance. The Bruhat-Tits tree $T_q$ replaces the Bloch sphere as
quantum state space, and particles emerge as topological defects in a cosmic syntax
tree [3]. Recent work on anomalous diffusion on p-adic fractals [4] has quantified
the spectral consequences of this geometry, finding effective transient dimensions
$d_{\mathrm{eff}} \approx 6.2$ for $p = 2$ and $d_{\mathrm{eff}} \approx 7.9$ for
$p = 3$ on Bruhat-Tits trees, while cautioning that pure ultrametricity yields a
degenerate Laplacian spectrum distinct from the Gaussian unitary ensemble (GUE)
statistics of the Riemann zeros — a constraint this paper carries forward in
Section 6.

**Factorization as geometry.** The geometric approach to integer factorization [5]
and the helical-coordinate program [6] treat factorization hardness as a
representational artifact of coordinate choice. The Morse-theoretic framing used
here is compatible with this view: primality becomes a property of the critical
point structure of a manifold rather than an arithmetic search problem.

## 3. The Construction

### 3.1 The Categories

Let $\mathcal{P}$ be the category whose objects are the integers $n > 1$ and whose
morphisms are divisibility: there is a unique morphism $m \to n$ if and only if
$m \mid n$. This is a preorder category encoding the divisibility poset.

Let $\mathcal{M}$ be the category of smooth, compact, connected manifolds with
smooth embeddings as morphisms.

### 3.2 The Functor

Define the square-free kernel $\mathrm{rad}(n) = \prod_{p \mid n} p$. Define the
functor

$$F: \mathcal{P} \to \mathcal{M}, \qquad F(n) = \prod_{p \mid \mathrm{rad}(n)} S^{p-1}.$$

On a morphism $m \mid n$, the functor acts as the natural inclusion
$F(m) \hookrightarrow F(n)$. The functor does not distinguish between a prime and
its powers: $F(p^a) = F(p) = S^{p-1}$ for any $a \geq 1$. This property is
examined critically in Section 5.

### 3.3 The Homology-Rank Property

By the Künneth formula, the total homology rank of a product of spaces multiplies
across factors. Each sphere $S^{d}$ has total homology rank 2 (one generator in
degree 0 and one in degree $d$). Therefore:

$$\mathrm{rank}\, H_*(F(n)) = 2^{\omega(n)}$$

where $\omega(n)$ is the number of distinct prime factors of $n$.

**Prime-power criterion.** $n$ is a prime power if and only if
$\mathrm{rank}\, H_*(F(n)) = 2$.

**Morse-theoretic interpretation.** Under a standard height function, each sphere
$S^{p-1}$ has exactly two critical points (a minimum and a maximum). A Morse
function on the product, obtained as the sum of the pulled-back height functions,
has critical points in bijection with the Cartesian product of the per-sphere
critical sets. Hence the number of critical points of $F(n)$ is also
$2^{\omega(n)}$: the arithmetic complexity of $n$ is mirrored by the topological
complexity of its image.

## 4. Computational Verification

The D1 disconfirmation condition — the most concrete leg of the conjecture — was
tested directly. For every integer $n$ in $[2, 100{,}000]$, we computed:

1. the homology rank of $F(n)$ via the Künneth formula,
2. the Morse critical-point count of $F(n)$ under the product height function,
3. the prime-power criterion (rank = 2 if and only if $n$ is a prime power).

**Result: all 99,999 integers passed all three checks.** The homology rank equals
$2^{\omega(n)}$ for every $n \leq 100{,}000$; the Morse critical-point count agrees;
and the prime-power criterion holds without exception.

Representative values:

| $n$ | prime factors | image | rank |
|:----|:--------------|:------|:-----|
| 2 | $\{2\}$ | $S^1$ | 2 |
| 6 | $\{2, 3\}$ | $S^1 \times S^2$ | 4 |
| 30 | $\{2, 3, 5\}$ | $S^1 \times S^2 \times S^4$ | 8 |
| 210 | $\{2, 3, 5, 7\}$ | $S^1 \times S^2 \times S^4 \times S^6$ | 16 |

This verification is reproducible from the repository notebook
(`notebooks/functor_formalization.py`, pure Python standard library).

## 5. The Synthesis Conjecture

The central claim of this paper is the following pre-registered conjecture.

**Conjecture (Universe Category).** *There exists a single functor
$F: \mathcal{P} \to \mathcal{M}$ whose image simultaneously encodes (i) quantization
as integer-valued topological invariants, (ii) stability as ultrametric hierarchy,
and (iii) prime factorization as homology rank. The three are not coincidences but
faces of one categorical structure.*

### 5.1 The Evidence Available

The three legs have independent support:

- **Factorization leg:** the homology-rank property is verified computationally
  (Section 4) and is a theorem of the construction.
- **Stability leg:** the ultrametric hierarchy of the primes — the strong triangle
  inequality organizing p-adic space — is structurally mirrored by the
  prime-indexed product structure of $F(n)$. Prior work [3][4][7] establishes the
  ultrametric hierarchy as a stability mechanism in physics.
- **Quantization leg:** integer-valued topological invariants of the type that
  appear in the image of $F$ are proposed in [2] as the blueprint of quantization.

### 5.2 Honest Labeling

Consistent with the Bayesian evidential-weight standards applied throughout this
research program, all correspondences identified in Section 5.1 are
**[RETRODICTION — not evidence]**. They were constructed post-hoc: the functor was
designed so that factorization becomes a topological invariant, and the stability
and quantization legs were then mapped onto the same structure. No prediction was
pre-registered before the correspondence was observed. Each correspondence carries
zero independent evidential weight until a novel, pre-registered prediction derived
from the synthesis is confirmed by independent observation.

### 5.3 The Open Obstructions

**Obstruction 1 (multiplicity).** The functor is blind to multiplicity:
$F(8) = F(2) = S^1$. A "universe category" that cannot distinguish $2^3$ from $2^1$
may be too coarse to encode physical content, since particles are distinguished by
multiplicity. Whether multiplicity is genuinely irrelevant (only the square-free
kernel matters) or whether the functor must be enriched to carry multiplicity is an
open problem.

**Obstruction 2 (dynamical content).** Homology is a static invariant. Quantization
and stability are dynamical phenomena. Bridging this gap requires extending the
construction to $\infty$-categories or homotopy-type theory — a formalization not
yet written.

**Obstruction 3 (spectral realism).** The p-adic diffusion results [4] show that
pure ultrametricity does not reproduce GUE statistics without broken symmetry.
Any claim that the stability leg alone accounts for the Riemann spectrum is
constrained by this result.

## 6. Pre-Registered Disconfirmation Conditions

The following conditions were committed to the project repository (git commit
`84527e3`, 2026-08-10) before the computational results of Section 4 were obtained:

- **D1:** If the homology rank of $F(n)$ for a square-free composite with $k$
  distinct prime factors is ever found not to equal $2^k$, the framework is wrong.
  *Status: tested and not falsified for $n \leq 100{,}000$ (Section 4).*
- **D2:** If a physical system engineered with the modular-curve topology
  ($L = 2$, $w = 1$) fails to exhibit quantized behavior at the predicted scale,
  the quantization leg is falsified. *Status: untested (instrument frontier).*
- **D3:** If the ultrametric-error-suppression bound
  $|x + y|_p \leq \max(|x|_p, |y|_p)$ is violated by a realized Bruhat-Tits-tree
  quantum state space, the stability leg is falsified. *Status: untested
  (instrument frontier).*

## 7. Discussion

The value of the construction is twofold. First, it makes a previously abstract
correspondence concrete and computationally testable: the equivalence between
arithmetic structure and topological structure is verified for every integer up to
$10^5$. Second, it isolates precisely where the harder claims lie — the synthesis
conjecture, the multiplicity obstruction, and the dynamical gap — so that future
work can target them directly rather than gesturing at the correspondence.

The paper does not claim that the universe is a category in any literal or
decorative sense. It claims only that a specific, well-defined categorical
construction exhibits three structures that have historically been treated as
unrelated, and that this coincidence is worth investigating under the discipline of
pre-registered falsification.

## 8. Conclusion

A functor from the divisibility category of the integers to the category of smooth
manifolds has been defined, and its most concrete property — homology rank equals
$2^{\omega(n)}$ — has been verified for all integers up to $100{,}000$. The
synthesis conjecture that this functor simultaneously encodes quantization,
stability, and factorization is stated with explicit disconfirmation conditions and
honest [RETRODICTION] labeling. Three open obstructions — multiplicity blindness,
the static-dynamical gap, and spectral realism — delimit the conjecture's scope.
The construction is offered as a falsifiable hypothesis about the unity of
mathematical structure, not as a demonstrated theorem.

## Declarations

**Funding:** No specific funding was received for this work.

**Competing interests:** The author declares no competing interests.

**Data availability:** The computational verification is fully reproducible from
the repository notebook (`notebooks/functor_formalization.py`); the output for
$n \leq 100{,}000$ is reported in Section 4.

**Author contributions:** The author conceived, formalized, and verified the entire
construction.

**Ethics approval:** Not applicable.

**Consent for publication:** The author consents.

**Pre-registration:** The core claim and disconfirmation conditions D1-D3 were
committed to the project repository (git commit `84527e3`, 2026-08-10) before the
computational results were obtained. A living research continuity registry tracks
the conjecture and its calibration schedule.

## References

[1] Quni-Gudzinas, R. B. Prime Numbers as Universal Optimization Primitives.
the QNFO archive, 2025. https://papers.qnfo.org/papers.

[2] Quni-Gudzinas, R. B. The Strange Loop Theory of Physical Quantization.
the QNFO archive, 2025. https://papers.qnfo.org/papers.

[3] Quni-Gudzinas, R. B. Alpha Pi Project: From Cardiac Rhythms to Cosmic Fractals.
the QNFO archive, 2026. https://papers.qnfo.org/papers.

[4] Quni-Gudzinas, R. B. Spectral Analysis of Anomalous Diffusion on p-Adic
Fractals: Reconciling Riemannian Geometry with Discrete Arithmetic via Geometric
Resonances. the QNFO archive, 2026. https://papers.qnfo.org/papers.

[5] Khomovsky, D. I. A geometric approach to integer factorization. arXiv, 2018.
arXiv:1802.03658.

[6] Quni-Gudzinas, R. B. Geometric Factorization via Natural Coordinate Systems.
the QNFO archive, 2025. https://papers.qnfo.org/papers.

[7] Quni-Gudzinas, R. B. Number-Theoretic Ultrametric Foundations: A Unified p-adic
Framework for Error-Correcting Code Classification. the QNFO archive, 2025.

[8] Heydeman, M., Marcolli, M., Saberi, I. Tensor networks, p-adic fields, and
algebraic curves: arithmetic and the AdS3/CFT2 correspondence. Advances in
Theoretical and Mathematical Physics, 2018. DOI: 10.4310/atmp.2018.v22.n1.a4.

[9] Aizenbud, A., Zapolsky, F. Functoriality in Morse theory on closed manifolds.
arXiv, 2008. arXiv:0805.2131.

[10] Hung, L.-Y., Li, W., Melby-Thompson, C. M. p-adic CFT is a holographic tensor
network. Journal of High Energy Physics, 2019. DOI: 10.1007/jhep04(2019)170.
