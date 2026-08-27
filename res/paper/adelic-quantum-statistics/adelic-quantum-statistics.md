---
title: "Quantum Statistics from the Adelic Product Formula: The Squarefree Origin of the Fermi–Dirac/Bose–Einstein Distinction"
author: "Rowan Brad Quni-Gudzinas"
affiliation: "QNFO"
ORCID: "0009-0002-4317-5604"
date: "2026-08-27"
license: "cc-by-4.0"
status: "draft"
version: "v0.1-draft"
doi: ""
keywords:
  - Bose-Einstein statistics
  - Fermi-Dirac statistics
  - squarefree integers
  - adelic product formula
  - maximum entropy
  - Möbius function
  - anyons
  - bounded occupation
---

## Abstract

Why are there two quantum statistics, and only two, in three spatial dimensions? This paper reads the Bose–Einstein and Fermi–Dirac occupation distributions as the maximum-entropy solutions of one lattice with two multiplicity rules. On the unrestricted integer lattice the Euler factor at each prime place is the mode partition function of an unbounded occupation number, and the resulting Dirichlet series is the Riemann zeta function; on the squarefree restriction — each prime divides at most once — the Euler factor becomes the mode partition function of an occupation number in $\{0,1\}$, and the series becomes $\zeta(s)/\zeta(2s)$. The two golden occupation numbers $1/(e^{\beta(\varepsilon-\mu)} \pm 1)$ follow from the canonical derivative of these mode factors at arbitrary inverse temperature and chemical potential, and both are the unique maximum-entropy distributions under their stated constraints. The per-place identifications at fugacity $z = 1/p$, inverse temperature $\beta_p = \ln p$, were established elsewhere; what the earlier records leave open is supplied here: the per-distinction transition rate $\gamma = 1/N$ as a consequence of bath degeneracy, the complex structure of the large-$N$ limit as the sign-normalized generator selected by exclusion, the Möbius-parity reading of composite statistics, and the bounded-occupation family $\zeta(s)/\zeta((m+1)s)$ that interpolates between the two statistics and that anyonic exchange statistics must contact. The register is structural throughout: no physical particle is implied; the claims are isomorphisms of mathematical structure, and the physical labels attach at the level of statistical distributions. Every quantitative statement is reproduced by the deposited verification scripts.

## 1. Introduction

A system of identical particles in three or more spatial dimensions admits exactly two exchange statistics. This binary is usually presented as a primitive classification of nature, with the spin-statistics theorem connecting it to spin. The question asked here is narrower and arithmetic: can the two statistics be recovered as the maximum-entropy occupation distributions of a single lattice under two multiplicity constraints, with the adelic product formula as the invariant that ties the places together?

The answer turns out to be nearly classical. Write an integer as $n = \prod_p p^{a_p}$. If every exponent is unrestricted, $a_p \in \mathbb{N}_0$, the Euler factor at the prime $p$ in the Dirichlet series $\sum n^{-s} = \zeta(s)$ is $(1 - p^{-s})^{-1}$, which is the mode partition function of an occupation number taking every value $0,1,2,\dots$ — the bosonic counting. If every exponent is restricted to $a_p \in \{0,1\}$, the integer is squarefree, and the Dirichlet series is $\zeta(s)/\zeta(2s)$, whose Euler factor $(1 + p^{-s})$ is the mode partition function of an occupation number in $\{0,1\}$ — the fermionic counting. The identification of these generating structures with the two quantum statistics has a long history in the Riemann-gas literature [Julia 1990; Spector 1990; Bakas–Bowick 1991], and its per-place form was established within this research program for the fixed fugacity $z = 1/p$ [10.5281/zenodo.22035210]. This paper does not re-derive those identifications; it supplies the tiers they leave open, and it states the precise boundary of each claim.

Three results are the substance of the paper.

First, the golden occupation numbers are recovered from the canonical derivative of the mode partition functions at arbitrary inverse temperature $\beta$ and chemical potential $\mu$, not only at the special point $z = 1/p$, and the maximum-entropy property that selects them is verified directly.

Second, the per-distinction transition rate $\gamma = 1/N$ — an input assumed by the finite-distinction formulation of unitary evolution [10.5281/zenodo.22046458] — is shown to follow from bath degeneracy: one unit of total activity distributed uniformly over $N$ indistinguishable alternatives produces a mixing operator whose non-uniform eigenvalues are $1 - 1/N$.

Third, the complex structure of the large-$N$ limit is identified precisely. The reversible generator on the simplex is skew with respect to the Fisher metric, but its squared eigenvalues are $-\sin^2(2\pi k/N)$, not $-1$. The complex structure is the sign-normalized generator — the discrete Hilbert transform — whose square is $-1$ on mean-zero modes exactly at every $N$. This normalization is selected on the fermionic side alone: the symmetric (diffusive) generator has real squared eigenvalues $\cos^2(2\pi k/N) \geq 0$ and admits no complex structure.

Two further structures complete the paper: the Möbius-parity dictionary, in which the composite-statistics rule of quantum mechanics (an even number of fermionic constituents gives a composite boson, an odd number a composite fermion) is exactly the parity of the prime-factor count on the squarefree lattice; and the bounded-occupation family $\sum_{v_p \le m} n^{-s} = \zeta(s)/\zeta((m+1)s)$, which interpolates from the fermionic case at $m = 1$ to the bosonic case as $m \to \infty$ and provides the arithmetic object that intermediate (anyonic) statistics must contact.

The remainder of the paper is organized as follows. Section 2 states the lattice dichotomy and its verification. Section 3 derives the rate $\gamma = 1/N$. Section 4 treats the symplectic tier. Section 5 is the Möbius-parity dictionary. Section 6 is the anyon program. Section 7 gives the crosswalk of terminology. Section 8 states what a practitioner can do with the result. Section 9 states the premise depth and the boundaries, including the precise relation to the spin-statistics connection. Section 10 is the verification appendix.

## 2. The lattice dichotomy

### 2.1 Global identities

Let $\zeta(s)$ denote the Riemann zeta function. The two Dirichlet identities central to this paper are

$$\sum_{n \text{ squarefree}} n^{-s} = \prod_p (1 + p^{-s}) = \frac{\zeta(s)}{\zeta(2s)}, \qquad \sum_{n \geq 1} n^{-s} = \prod_p (1 - p^{-s})^{-1} = \zeta(s).$$

The first is the generating function of integers whose prime exponents obey $a_p \in \{0,1\}$; the second counts every exponent. The Euler factors are the single-mode partition functions: $(1 + p^{-s})$ is $\sum_{a=0}^{1} e^{-a s \ln p}$, the partition function of a two-state mode, and $(1 - p^{-s})^{-1}$ is $\sum_{a \geq 0} e^{-a s \ln p}$, the partition function of an unbounded mode, when $s$ is read as an inverse temperature multiplying the mode energy $\ln p$. The verification script `verify_stats.py` checks both identities against direct sieved sums: at $s = 2.5, 3.0, 4.0$ the squarefree sum over the first $10^5$ integers matches $\zeta(s)/\zeta(2s)$ to at most $1.3 \times 10^{-8}$, and the unrestricted sum matches $\zeta(s)$ to $2.1 \times 10^{-8}$ (checks F1a, F1b). The Euler-product forms match the closed forms to machine-independent truncation error (F1c).

### 2.2 Golden occupation numbers

At inverse temperature $\beta$ and chemical potential $\mu$, with $z = e^{\beta\mu}$, the two single-mode partition functions are

$$Z_F = 1 + z p^{-\beta}, \qquad Z_B = (1 - z p^{-\beta})^{-1},$$

where the mode energy is $\ln p$. The mean occupation number is the canonical derivative,

$$\langle n \rangle = -\frac{1}{\beta}\frac{\partial}{\partial \ln p}\ln Z,$$

which evaluates to

$$\langle n \rangle_F = \frac{z p^{-\beta}}{1 + z p^{-\beta}} = \frac{1}{e^{\beta(\ln p - \mu)} + 1}, \qquad \langle n \rangle_B = \frac{z p^{-\beta}}{1 - z p^{-\beta}} = \frac{1}{e^{\beta(\ln p - \mu)} - 1}.$$

These are the Fermi–Dirac and Bose–Einstein occupation numbers with the mode energy $\varepsilon = \ln p$. The verification (check F1d) computes the canonical derivative by finite differences with Richardson extrapolation at $p \in \{2,3,5\}$, $\beta \in \{0.5, 1, 2\}$, $z \in \{0.5, 1, 2\}$ (Bose cases restricted to $z p^{-\beta} < 1$ for convergence) and matches the golden forms to within $10^{-9}$. The special point $z = 1/p$, $\beta_p = \ln p$, of the per-place identifications [10.5281/zenodo.22035210] is the case $\beta = 1$, $\mu = 0$ of this family.

### 2.3 The maximum-entropy property

The golden distributions are not merely the derivatives of the partition functions; they are the unique maximum-entropy distributions under the stated constraints. For the geometric distribution $q_n = (1-q)q^n$ on $n \geq 0$ (the bosonic occupation distribution), the entropy gradient $-( \ln q_n + 1 )$ is affine in the state label $n$, hence orthogonal to every direction that preserves both the normalization and the mean — the first-order condition of a constrained maximum — and the entropy Hessian is strictly negative. For the two-state occupation (fermionic), the two constraints (normalization and fixed mean) determine the distribution uniquely. The verification script `verify_maxent.py` checks the first-order condition against randomly sampled constraint directions (residual below $10^{-14}$ after projection), strict concavity, and uniqueness (16 checks).

### 2.4 The direction of the assignment

The identification of squarefree with fermionic and unrestricted with bosonic is a direction, and a direction must be falsifiable. The two golden values differ at every non-degenerate point — at $z p^{-\beta} = \tfrac12$ the Fermi value is $\tfrac13$ and the Bose value is $1$ — so the assignment is not symmetric under interchange; the verification records this as a guard check (S1).

## 3. The rate $\gamma = 1/N$

The finite-distinction formulation of unitary evolution treats a system as $N$ finite alternatives with a per-distinction transition rate $\gamma$, and obtains the large-$N$ unitary limit from the entropy-Hessian gradient flow [10.5281/zenodo.22046458]. That paper assumes $\gamma = 1/N$. The seed derivation of this value is as follows. Suppose the environment consists of $N$ indistinguishable alternatives, and that one distinction is processed per unit of total activity. The mixing operator is

$$T = \mathrm{Id} - \frac{1}{N}\left(\mathrm{Id} - \bar P\right), \qquad \bar P_{ij} = \frac{1}{N},$$

the operator that leaves the uniform distribution fixed and contracts every mean-zero mode by $1 - 1/N$. The continuous-time rate of the non-uniform modes is therefore $\gamma = 1/N$ exactly: the individual rate $1$ (one unit of activity) is divided by the degeneracy $N$ of the bath. The verification script `verify_rate_gamma.py` checks the eigenvalue structure exactly for $N \in \{2,4,8,16,32,64\}$ (F2a), simulates the discrete chain — one randomly chosen alternative replaced per step — and matches the occupation autocorrelation to the closed form $q^2 + q(1-q)(1-q)^t$ with $q = 1/N$ in seeded Monte Carlo (F2b), and confirms the log-log slope of $\gamma(N)$ against $N$ is $-1$ (F2d).

Two qualifications are stated rather than absorbed. First, the result is a property of the uniform degeneracy: if the alternatives carry individual rates $\kappa_i$ with $\sum \kappa_i = 1$, the occupation of alternative $i$ relaxes at its own rate $\kappa_i$, not at $1/N$ — the verification records this as a guard (F2c). Second, the input that the bath supplies one unit of total activity per distinction is a model assumption; the derivation concerns the degeneracy-cancellation mechanics on top of that input, and the seam between distinct and indistinguishable alternatives is where the assumption lives.

## 4. The symplectic tier

### 4.1 Fisher geometry on the simplex

The state space of $N$ alternatives is the $(N-1)$-simplex. The entropy $S(p) = -\sum_i p_i \ln p_i$ has Hessian

$$\frac{\partial^2 S}{\partial p_i \partial p_j} = -\frac{\delta_{ij}}{p_i} - \frac{1}{p_N}, \qquad i,j < N,$$

with $p_N = 1 - \sum_{i<N} p_i$; the Fisher metric is its negative,

$$g_{ij} = \frac{\delta_{ij}}{p_i} + \frac{1}{p_N},$$

positive definite on the simplex, and $g = N(I + \mathbf{1}\mathbf{1}^\top)$ at the uniform point. (The seed derivation writes the metric as the Hessian of $S$; the sign of the defining equation is the other way round. The metric used throughout the derivation is the positive one; only the displayed equation carries the slip.)

### 4.2 The reversible generator

Let $L = \frac12(\text{shift} - \text{shift}^{-1})$ be the cyclic discrete derivative. On Fourier modes $e^{2\pi i k i/N}$ it acts by multiplication with $i\sin(2\pi k/N)$; it is skew with respect to $g$, and $\omega = gL$ is antisymmetric. The complex structure defined by $\omega(u,v) = g(Ju,v)$ is, at the uniform point, $J = L$ itself.

### 4.3 What $J^2$ actually is

The squared generator has Fourier eigenvalues $J^2_k = -\sin^2(2\pi k/N)$. This is $-1$ only at the single mode $k = N/4$; at fixed $\theta = 2\pi k/N$ the value $-\sin^2\theta$ stays bounded away from $-1$ as $N$ grows. The complex structure proper is the sign-normalized generator: the operator $H$ with Fourier multiplier $-i\,\mathrm{sgn}(\sin(2\pi k/N))$ is the discrete Hilbert transform, and $H^2 = -1$ on mean-zero modes exactly at every $N$. The large-$N$ identification is therefore: the generator carries the Hilbert phase at every $N$, and the Hilbert magnitude only after sign normalization.

### 4.4 The Fermi/Bose contrast

The symmetric counterpart $L_B = \frac12(\text{shift} + \text{shift}^{-1})$ is self-adjoint with respect to $g$, and its square has real Fourier eigenvalues $\cos^2(2\pi k/N) \geq 0$. No complex structure can arise on this side: the exclusion (skew, oriented) generator is what selects it. All of this is verified numerically in `verify_symplectic.py` (34 checks): the Fisher Hessian against the signed closed form at random interior points and at the uniform point, skewness and antisymmetry to $10^{-15}$, the eigenvalue identities, the finite-$N$ behavior of $J^2$, $H^2 = -1$ on mean-zero modes, and the Bose-side contrast.

## 5. Composite statistics and Möbius parity

The composite-statistics rule of quantum mechanics states that a bound state of an even number of fermions behaves as a boson and of an odd number as a fermion: the Cooper pair (two electrons) condenses, the exciton (electron and hole) is bosonic, helium-4 (six fermions) condenses while helium-3 (five fermions) does not. On the squarefree lattice the exchange sign of a composite is the parity of its prime-factor count: for squarefree $n$, the Möbius function is $\mu(n) = (-1)^{k}$ where $k$ is the number of prime factors. The dictionary is therefore

$$\text{exchange sign} = \mu(n), \qquad \text{on the squarefree lattice},$$

with the parity table verified entry by entry (check F-HCP): Cooper pair, exciton, and pion carry $\mu = +1$ (bosonic); baryon, helium-3, and the electron carry $\mu = -1$ (fermionic); the vacuum carries $\mu(1) = +1$. The Dirichlet series of the Möbius function, $1/\zeta(s) = \sum_n \mu(n) n^{-s}$, is the Fermi-side generating-function continuation against the Bose-side $\zeta(s)$.

This dictionary is an identification, not a derivation: it states that the sign structure of composite statistics and the parity structure of the squarefree lattice are the same mathematical object. The non-squarefree sector, $\mu(n) = 0$, is the exclusion-forbidden sector — a repeated prime factor is a repeated constituent, which the exclusion principle forbids. The claim carries three disconfirmation conditions: a contradiction anywhere in the parity table; a failure of the $\mu = 0$ sector to coincide with the exclusion-forbidden sector; or the demonstration that the identification is merely coincidental rather than structural.

## 6. Intermediate statistics: the anyon program

### 6.1 The interpolation family

Between the fermionic bound $a_p \le 1$ and the bosonic bound $a_p \to \infty$ lies the one-parameter family of bounded-occupation lattices $a_p \le m$. Its generating function closes exactly:

$$\sum_{n :\, v_p(n) \le m \; \forall p} n^{-s} = \prod_p \left(1 + p^{-s} + \cdots + p^{-ms}\right) = \frac{\zeta(s)}{\zeta((m+1)s)}.$$

At $m = 1$ this is the squarefree (Fermi) identity $\zeta(s)/\zeta(2s)$; as $m \to \infty$ it approaches $\zeta(s)$ (Bose). The verification script `verify_parastats.py` checks the sieved sums against the closed form for $m \in \{1,2,3\}$ at $s = 3,4$, the single-mode means against the analytic form, and both endpoint limits (16 checks).

### 6.2 The known targets

The interpolation family is proposed as the arithmetic object that intermediate (anyonic and parastatistical) exchange statistics must contact. The known observable targets are: abelian anyons with fractional exchange phases $e^{i\theta}$, $\theta = \pi/m$ (Laughlin quasiparticles at fractional quantum Hall fillings $\nu = 1/m$); non-abelian anyons — Ising/Majorana (Majorana zero modes in semiconductor–superconductor hybrids and Kitaev chains, with $\sigma^2 = 1$ braiding and the $4\pi$-periodic fractional Josephson effect) and Fibonacci (filling $\nu = 12/5$, universal for topological quantum computation); and parastatistics beyond two dimensions in the generalized-exclusion formulation [arXiv:2308.05203], whose constructed models are one- and two-dimensional.

### 6.3 The open correspondence

Whether an intermediate occupation bound reproduces any of these observables in the same maximum-entropy framework is an open question, and it is the disconfirmation condition of this section: if no intermediate bound reproduces a known anyonic or parastatistical observable, the arithmetic family remains a dictionary without contact. The dimensionality bridge is named for the same reason: in $d \geq 3$ the exchange group is the symmetric group and the phases are exactly $\pm 1$; in $d = 2$ it is the braid group and the phases can be fractional — the relaxation of the dichotomy in two dimensions is the phenomenon the interpolation family would have to mirror. The two-dimensional Bose gas, which condenses only quasi-long-range (Berezinskii–Kosterlitz–Thouless), marks the other place where the dichotomy softens.

## 7. Crosswalk of terminology

| This paper | Number theory | Quantum statistics | Stochastic thermodynamics | Information theory | QEC engineering |
|---|---|---|---|---|---|
| product formula | $\prod_v \lvert x \rvert_v = 1$ | normalization of occupations | global audit invariant | normalization constraint | checksum on readout/decoder arithmetic |
| squarefree restriction | distinct-part partitions | Fermi–Dirac (occupation 0/1) | exclusion regime | one-bit occupation per state | physical-qubit exclusivity |
| unrestricted lattice | unrestricted partitions | Bose–Einstein | sharing regime | unbounded occupation | mode sharing (cat/oscillator) |
| $\gamma = 1/N$ | degeneracy factor | per-state rate | bath degeneracy cancellation | uniform prior over alternatives | per-round syndrome rate |
| composite statistics | even/odd fermion count | Möbius parity $\mu(n)$ | exchange sign $\pm 1$ | constituent-count rule | Cooper pairs, excitons, He-4/He-3 |

Adjacent-domain bridges: the per-place identifications rest on the adelic information measure $H_p = \mathbb{E}[v_p]$ [10.5281/zenodo.22024240]; the signal-worker ontology of information physics, which reads boson as delocalized signal and fermion as localized worker, is known to fail exactly on composite bosons [10.5281/zenodo.21974194] — the failure the Möbius dictionary repairs; the replica-symmetry-breaking structure of spin glasses carries the same occupation-count question in the ultrametric setting; and the logical-scalar lineage [10.5281/zenodo.21964598; 10.5281/zenodo.21964104; 10.5281/zenodo.21962450] supplies the exchange-phase reading this paper does not claim to replace.

## 8. What a practitioner can do

A practitioner reads the statistics of a reservoir off its multiplicity structure. Given the occupation bound of a physical register — exclusive ($a_p \le 1$), shared (unbounded), or intermediate ($a_p \le m$) — the occupation distribution and the per-distinction cost follow, and the rate that the thermodynamic-floor analysis had to assume becomes a derived quantity [10.5281/zenodo.22117282].

The product formula provides an implementable audit. The checksum demonstrated for exact rational arithmetic across places [10.5281/zenodo.22114495] extends one tier up: occupation counts in a classical simulator of quantum statistics can be validated place-by-place, with a deviation from $\prod_v \lvert x \rvert_v = 1$ localizing the failing place. The verification records this as a completeness property: every proper subset of places deviates, and only the full place set normalizes to 1 (check H3b, all 1023 proper subsets tested).

The control reading follows from the same identification. If statistics are the occupation regime, then controlling statistics is controlling the multiplicity structure. In the laboratory the exchange phase is manipulated by braiding worldlines, by filling-factor engineering in the fractional quantum Hall effect, and by moving Majorana zero modes (T-junction and measurement-only braiding). The arithmetic counterpart — changing the occupation bound $m$ — is the design variable the same physical content takes in a classical stochastic system. The correspondence between these two control surfaces, the braid phase on one side and the occupation bound on the other, is the open target of Section 6, not an established result.

## 9. Premise depth and boundaries

The primitives are the integers with unique factorization, the adelic product formula (an imported theorem), the maximum-entropy principle (an imported postulate), and Euler's distinct-part partition identity $\prod(1+q^n)$, which is the engine of Section 2. Derived are the squarefree/unrestricted dichotomy and its occupation consequences, the degeneracy cancellation behind $\gamma = 1/N$, and the large-$N$ limit calculus. Named imported inputs are the finite-distinction formulation of unitary evolution [10.5281/zenodo.22046458], the thermodynamic floor of error correction [10.5281/zenodo.22117282], finite-adele encoding [10.5281/zenodo.22114495], the completeness senses of ordered fields [10.5281/zenodo.22109455], the per-place identifications at $\beta_p = \ln p$ [10.5281/zenodo.22035210], and the composite-statistics rule of standard quantum mechanics.

Where the premises end: the claim that the occupation-number distributions of quantum statistics are the maximum-entropy distributions of a multiplicity-constrained lattice is a mapping hypothesis — an isomorphism of mathematical structure — tested here by reproduction, and it asserts nothing about what particles are. It earns predictive status only through the anyon program of Section 6.

The boundary to the spin-statistics connection is stated in the words of the record that established it [10.5281/zenodo.21964598]: the connection between exchange phase and spin requires Lorentz symmetry, microcausality, and positive energy, and no arithmetic or topological argument supplies those. This paper derives the two statistical distributions and their rate structure from multiplicities; it does not claim to replace the spin-statistics connection, and it inherits its boundary verbatim.

## 10. Verification

Every quantitative statement in this paper is reproduced by one of six deposited scripts, all standard-library Python, seeded, and deterministic, with run logs and results files shipped alongside:

| Script | Content | Checks |
|---|---|---|
| `verify_stats.py` | squarefree/unrestricted identities, Euler-factor correspondence, golden occupations, direction guard, Möbius parity table | 65 |
| `verify_product_formula.py` | exact product formula, checksum completeness, occupation-constraint link | 17 |
| `verify_parastats.py` | bounded-occupation interpolation family | 16 |
| `verify_rate_gamma.py` | eigenvalue structure of the mixing operator, seeded Monte Carlo, heterogeneity guard, log-log slope | 15 |
| `verify_symplectic.py` | Fisher Hessian, skewness, Fourier eigenvalues, $J^2$ finite-$N$ behavior, Hilbert normalization, Bose-side contrast | 34 |
| `verify_maxent.py` | first-order maximum-entropy condition, strict concavity, uniqueness, golden edge cases | 16 |

Total: 163 checks, all passing at the time of writing. The F4 scoping artifact (`f4-differential-primon-gas-audit.py`) reproduces the published primon-gas canon side by side with the quantities introduced here and prints the differential table; no quantity introduced here reproduces a published one. Reproducibility: run each script from the deposited directory; no dependencies beyond the standard library; runtimes are on the order of seconds.

## References

- Julia, B. L. (1990). Statistical theory of numbers. In *Number Theory and Physics*.
- Spector, D. (1990). Supersymmetry and the Möbius inversion function. *Communications in Mathematical Physics*.
- Bakas, I., & Bowick, M. J. (1991). Curiosities of arithmetic gases. *Journal of Mathematical Physics*.
- Leinaas, J. M., & Myrheim, J. (1977). On the theory of identical particles. *Il Nuovo Cimento B*.
- Wilczek, F. (1982). Quantum mechanics of fractional-spin particles. *Physical Review Letters*.
- Kitaev, A. (2003). Fault-tolerant quantum computation by anyons. *Annals of Physics*.
- Kitaev, A. (2006). Anyons in an exactly solved model and beyond. *Annals of Physics*.
- Nayak, C., Simon, S. H., Stern, A., Freedman, M., & Das Sarma, S. (2008). Non-Abelian anyons and topological quantum computation. *Reviews of Modern Physics*.
- Doplicher, S., Haag, R., & Roberts, J. E. (1971). Local observables and particle statistics I, II. *Communications in Mathematical Physics*.
- Pauli, W. (1940). The connection between spin and statistics. *Physical Review*.
- Duck, I., & Sudarshan, E. C. G. (1998). *Pauli and the Spin-Statistics Theorem*. World Scientific.
- Wang, Z., & Hazzard, K. R. A. (2023). Particle exchange statistics beyond fermions and bosons. arXiv:2308.05203.
- Hartnoll, S. A., & Yang, M. (2025). The Conformal Primon Gas at the End of Time. arXiv:2502.02661.
- Zhou, C.-C., Chen, S. A., Chen, Y.-Z., Shen, Y., Zhang, F.-L., & Dai, W.-S. (2025). Quantum statistics forbids particle exchange statistics beyond bosons and fermions in 3D. arXiv:2505.17361.
- Medina Sánchez, N., & Dakić, B. (2023). Reconstruction of quantum particle statistics: bosons, fermions, and transtatistics. arXiv:2306.05919.
- Program records: 10.5281/zenodo.22035210; 10.5281/zenodo.22046458; 10.5281/zenodo.22117282; 10.5281/zenodo.22114495; 10.5281/zenodo.22109455; 10.5281/zenodo.21964598; 10.5281/zenodo.21964104; 10.5281/zenodo.21962450; 10.5281/zenodo.22024856; 10.5281/zenodo.22024240; 10.5281/zenodo.21974194; 10.5281/zenodo.21940822; 10.5281/zenodo.21336099; 10.5281/zenodo.21609223; 10.5281/zenodo.18199397; 10.5281/zenodo.21672990; 10.5281/zenodo.21590155.
