---
title: "Arithmetic Anyons: The Bounded-Occupation Family, Gentile Statistics, and the Roots of Unity That Carry Braid Phases"
author: "Rowan Brad Quni-Gudzinas"
affiliation: "QNFO"
ORCID: "0009-0002-4317-5604"
date: "2026-08-27"
license: "cc-by-4.0"
status: "published"
version: "1.0.0"
doi: "10.5281/zenodo.22124744"
concept_doi: "10.5281/zenodo.22124743"
abstract: |
  Three spatial dimensions admit exactly two exchange statistics for identical particles, and a recent record reads the two occupation distributions as maximum-entropy occupations of one integer lattice under two multiplicity rules, closing with an open correspondence: the bounded-occupation family interpolates between the fermionic and bosonic cases and is proposed as the arithmetic object that intermediate (anyonic) statistics must contact. This paper settles the correspondence computationally. The family is the partition function of Gentile intermediate statistics — an occupation cap per mode — and it carries no exchange phase for any cap: permuting occupation labels yields only the signs $\pm 1$, every observable is invariant under any inserted phase, and the canonical symmetric reading assigns the phase $+1$ for every cap, including the cap that reproduces Fermi counting, where fermions carry $-1$. The correspondence with Fermi counting is therefore a counting isomorphism, not an exchange-phase isomorphism. The arithmetic objects that carry the phases realized in the standard anyon models are multiplicative characters at roots of unity: the Laughlin exchange phase at filling $1/m$ is a primitive $2m$-th root of unity, and the Fibonacci braid eigenvalues are powers of $e^{i\pi/5}$. The prime-gap structure supplies a computable distinguishing observable: the specific heat of the primon gas deviates from the smooth-density-of-states ideal gas at every sampled temperature, by up to roughly three quarters at low temperature, in both statistics. The claims are isomorphisms of mathematical structure; the spin-statistics boundary is respected; every quantitative statement is reproduced by the deposited verification scripts.
keywords:
  - anyons
  - Gentile statistics
  - Haldane exclusion statistics
  - roots of unity
  - Riemann gas
  - Bose-Einstein statistics
  - Fermi-Dirac statistics
  - bounded occupation
  - zeta function
bibliography: "references.bib"
---

## 1. Introduction

A system of identical particles in three or more spatial dimensions admits exactly two exchange statistics. In two dimensions the configuration-space argument yields the braid group and a continuum of fractional phases — the anyons realized in the fractional quantum Hall regime [@leinaas1977; @wilczek1982] and measured in anyon colliders [@heiblum2022]. Two readings of the two-statistics binary meet in a recent record: the occupation distributions are read as maximum-entropy occupations of the integer lattice, the unrestricted lattice giving the Riemann zeta function and the squarefree lattice the ratio of two zeta values [@zenodo22123068]. That record closes with an open correspondence: the bounded-occupation family

$$\sum_{v_p(n) \le m} n^{-s} \;=\; \prod_p \left(1 + p^{-s} + \dots + p^{-ms}\right) \;=\; \frac{\zeta(s)}{\zeta((m+1)s)}$$

interpolates from the fermionic case at $m = 1$ to the bosonic case as $m \to \infty$, and is proposed as the arithmetic object that intermediate (anyonic) statistics must contact. Whether any intermediate $m$ reproduces any known anyonic observable is left unproven there.

This paper settles the correspondence computationally, in three steps. First, the family is identified: it is the partition function of Gentile intermediate statistics, an occupation cap of $m$ particles per mode introduced in 1940 [@gentile1940] — and it carries no exchange phase for any $m$. Occupation caps count; braid phases act on trajectories. The computation shows the cap fixes no phase at all, so no member of the family reproduces the Laughlin exchange phase, and the correspondence with Fermi counting is a counting isomorphism rather than an exchange-phase isomorphism. Second, the arithmetic objects that do carry the phases realized in the standard anyon models are multiplicative characters at roots of unity: the Laughlin exchange phase at filling $1/m$ is a primitive $2m$-th root of unity, and the Fibonacci braid eigenvalues are powers of $e^{i\pi/5}$, the same parameterization as the quantum-group records at roots of unity already in the corpus [@zenodo21208491; @zenodo22024856]. Third, the prime-gap structure of the integer lattice supplies a computable thermodynamic observable — a specific-heat deviation from the smooth-density-of-states ideal gas — that separates the arithmetic construction from the standard derivation and is quantified at every sampled temperature.

The practical consequence is a design rule: a device architecture that proposes to control exchange statistics by constraining register occupation changes the accessible counting, not the exchange phase; the phase lives in character-theoretic (root-of-unity) structure. Section 8 states the rule and the adjudication table. The spin-statistics connection is a boundary this paper respects, not a target; the boundary is the one drawn in the configuration-space record [@zenodo21962450].

## 2. The bounded-occupation family

Let $\zeta(s)$ be the Riemann zeta function. The two Dirichlet identities at the center of the family are

$$\sum_{n \text{ squarefree}} n^{-s} = \prod_p (1 + p^{-s}) = \frac{\zeta(s)}{\zeta(2s)}, \qquad \sum_{n \ge 1} n^{-s} = \prod_p (1 - p^{-s})^{-1} = \zeta(s).$$

The first counts integers whose prime exponents obey $a_p \in \{0,1\}$; the second counts every exponent. The Euler factors are single-mode partition functions: $(1 + p^{-s})$ is the partition function of a two-state mode, $(1 - p^{-s})^{-1}$ that of an unbounded mode, when $s$ is read as an inverse temperature multiplying the mode energy $\ln p$. The identification of these generating structures with the two quantum statistics has a long history in the Riemann-gas literature [@julia1990; @spector1990; @bakas1991; @hartnoll2025; @makhaldiani2018], and its per-place form was established in this program at fixed fugacity [@zenodo22035210].

The bounded-occupation family caps the exponent at $m$:

$$\sum_{v_p(n) \le m} n^{-s} \;=\; \prod_p \left(1 + p^{-s} + \dots + p^{-ms}\right) \;=\; \frac{\zeta(s)}{\zeta((m+1)s)}.$$

The sum runs over $m$-th-power-free integers. At $m = 1$ the family is the squarefree (fermionic-counting) series; as $m \to \infty$ it approaches the unrestricted (bosonic-counting) series. This exact object is not new to physics: it is the partition function of Gentile intermediate statistics, in which no mode holds more than $m$ particles, and which Gentile introduced in 1940 as the natural intermediate between the two standard statistics [@gentile1940]. The identification "bounded-occupation family = Gentile partition function" is elementary, but it was not stated in the earlier record, and it matters for the adjudication below: Gentile statistics is a known, named object with a literature, distinct from Haldane exclusion statistics.

The occupation numbers of the capped mode follow from the canonical derivative. With weight $x = z p^{-\beta}$ the capped-mode occupation is

$$\langle a \rangle_m = \frac{\sum_{a=0}^{m} a\, x^a}{\sum_{a=0}^{m} x^a},$$

which at $m = 1$ gives the Fermi value $x/(1+x)$, equal to $1/3$ at $x = 1/2$, increases monotonically in $m$, and tends to the Bose value $x/(1-x)$, equal to $1$ at $x = 1/2$. The verification script `verify_m_anyon.py` checks the family identity by direct sieved sums against $\zeta(s)/\zeta((m+1)s)$ for $m \in \{1,2,3,5\}$ and $s \in \{2.5, 3.0, 4.0\}$ (maximal error $5.9 \times 10^{-8}$ at $s = 2.5$ over the first $5 \times 10^{4}$ integers), and checks the golden occupation values.

## 3. The family carries no exchange phase

Exchange statistics is a datum of the multi-particle state space: a representation of the braid group (two dimensions) or the symmetric group (three and more dimensions) on the states of identical particles. The bounded-occupation family is a generating function of counting: a real-valued Dirichlet series whose coefficients are the number of configurations. The two layers — counting and phase — are distinct, and the computation shows the family contains only the first.

**Occupation-label exchange.** Take two distinguishable modes $p$ and $q$ and the two-particle sector of the capped Fock space: states $|a_p, a_q\rangle$ with $a_p + a_q = 2$, namely $(2,0)$, $(1,1)$, $(0,2)$ for any cap $m \ge 2$, and $(1,1)$ alone at $m = 1$. Particle exchange maps $|a_p, a_q\rangle \mapsto |a_q, a_p\rangle$. This is a permutation of the sector: a swap of $(2,0)$ with $(0,2)$ and a fixed point at $(1,1)$. Its eigenvalues are $\{1, 1, -1\}$ for every $m \ge 2$, and $\{1\}$ at $m = 1$. Permuting occupation labels produces only the signs $\pm 1$; no fractional phase $e^{i\theta}$ with $\theta \notin \{0, \pi\}$ is available, for any $m$.

**Phase insertion leaves every observable fixed.** The stronger statement is that the cap does not determine any phase. Attach an arbitrary exchange phase $e^{i\theta f(a)}$ to the mode weights, so the weight of occupancy $a$ becomes $w_a = x^a e^{i\theta f(a)}$. The occupation probabilities are $p_a = |w_a|^2 / \sum |w|^2 = x^{2a} / \sum x^{2a}$, independent of $\theta$ exactly: every observable built from the probabilities — occupations, entropy, thermodynamic potentials — is invariant under any inserted phase. The phase is a free datum the cap does not fix.

**Consequences.** For $m \ge 2$ the Laughlin exchange phase at filling $1/m$ is $e^{i\pi/m}$: the values $i$, $e^{i\pi/3}$, $e^{i\pi/5}$ are all different from $1$. No member of the family reproduces any of them, because the family carries no phase to compare. At $m = 1$ the canonical symmetric reading assigns $+1$, where fermions carry $-1$: even the Fermi correspondence is a counting correspondence, not a phase correspondence. The "must contact" wording of the earlier record therefore overstates the relation: contact with anyonic statistics would require a phase datum, and the family contains none. What the family supplies is a counting interpolation between the two statistics — and counting interpolations are blind to phases. This is the structural reason, and the computation confirms it rather than assuming it.

## 4. Gentile statistics is not Haldane exclusion statistics

The exclusion-type constraint that the condensed-matter literature has actually related to braid phases is Haldane's fractional exclusion statistics [@haldane1991; @speliotopoulos1995]. In the g-form, a mode whose occupation is $n$ leaves $g$ fewer states for the next particle, and the occupation at fugacity parameter $x$ solves

$$w^{g} (1 + w)^{1-g} = 1/x, \qquad n_g = \frac{1}{w + g},$$

with $g = 1$ the Fermi case and $g = 0$ the Bose case. The relation between Haldane statistics and braid statistics is known to be regime-restricted: it holds perturbatively for the Chern-Simons anyon model only when the anyon-anti-anyon statistical interaction is included [@chenng1994], and non-perturbatively only for the incompressible anyon liquid with a Hall edge [@ye2015]. Outside those regimes the two notions of statistics do not coincide.

The bounded-occupation family is a different object from Haldane statistics, and the computation quantifies the difference. Table 1 compares the capped-mode occupation with the Haldane occupation under the two natural interpolations $g = 1/m$ and $g = 1/(m+1)$, on the grid $x \in \{0.1, 0.3, 0.5, 0.7, 0.9\}$.

| $m$ | max deviation, $g = 1/m$ | max deviation, $g = 1/(m+1)$ |
|:---:|:---:|:---:|
| 2 | 0.109 | 0.187 |
| 3 | 0.252 | 0.090 |
| 5 | 0.578 | 0.360 |

Table 1: Maximum absolute difference between the capped-mode (Gentile) occupation and the Haldane occupation, across the grid.

The curves agree only at the endpoints — $m = 1$ with $g = 1$ reproduces Fermi exactly, and $m \to \infty$ with $g \to 0$ reproduces Bose — and deviate at every finite $m \ge 2$ under both mappings. The m-family is Gentile statistics; it is not Haldane exclusion statistics, and it inherits none of the special-regime braid-phase relations that the Haldane object enjoys in the literature.

## 5. The phase carriers: characters at roots of unity

If truncation does not carry phase, the next question is what does. The braid group $B_N$ on $N$ strands has one-dimensional representations $\rho_\theta(\sigma_i) = e^{i\pi\theta}$ for every $\theta$: its characters reproduce every abelian exchange phase. The verification checks the braid relation $\sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2$ and the distant commutation for $\theta \in \{1/3, 2/5, 1/2\}$. The arithmetic content enters at the level of which phases are realized: the phases realized in the standard models sit on the roots of unity.

**Laughlin phases.** At filling $\nu = 1/m$ the Laughlin quasiparticle carries the exchange phase $e^{i\pi/m}$. The computation evaluates the order of each phase, the smallest positive power equal to $1$:

| $m$ | phase $e^{i\pi/m}$ | order |
|:---:|:---:|:---:|
| 1 | $-1$ | 2 |
| 2 | $i$ | 4 |
| 3 | $e^{i\pi/3}$ | 6 |
| 5 | $e^{i\pi/5}$ | 10 |
| 7 | $e^{i\pi/7}$ | 14 |

Table 2: The Laughlin exchange phases are primitive $2m$-th roots of unity.

Each phase is a primitive $2m$-th root of unity: the exchange phase of the standard abelian anyon is cyclotomic data, not a truncation datum.

**Fibonacci braiding.** The non-abelian Fibonacci model supplies the second test. Set $q = e^{i\pi/5}$, a tenth root of unity. The two standard Fibonacci braid eigenvalues are $q^4 = e^{4\pi i/5}$ and $-q^2 = -e^{2\pi i/5}$, of orders $5$ and $10$; the Temperley-Lieb loop parameter at the same point is $|q + q^{-1}| = 2\cos(\pi/5) = \varphi$, the golden ratio. The whole family of Temperley-Lieb categories with $\delta_k = 2\cos(\pi/(k+2))$ — $\sqrt{2}$ for the Ising category at $k = 2$, $\varphi$ for Fibonacci at $k = 3$, $\sqrt{3}$ at $k = 4$ — sits on the root-of-unity locus $q_k = e^{i\pi/(k+2)}$. All of these identities are checked exactly by the deposited script `verify_braid_characters.py`.

The same parameterization — quantum groups at roots of unity — is the stated setting of the in-corpus p-adic anyon braiding records [@zenodo21208491], and the root-of-unity phases on ramified branches are the named input of the pattern-particle table [@zenodo22024856]. The consistency is a named-input consistency: this paper does not derive those records' constructions, it verifies that the phases they carry are exactly the root-of-unity data that the character model reproduces and the occupation family cannot.

## 6. A distinguishing observable: the prime-gap specific heat

The remaining question is whether the arithmetic origin of the two statistics is observationally distinguishable from the standard derivation, beyond reproducing the same distributions. The sharpest computable quantity is the thermodynamics of the primon gas: modes at energies $\ln p$ over the primes, with bosonic occupation $n_B(p) = 1/(p^{\beta} - 1)$ and fermionic occupation $n_F(p) = 1/(p^{\beta} + 1)$ at inverse temperature $\beta$. Thermodynamic studies of the Riemann gas exist in the classical randomized form [@duenas2014] and the conformal form [@hartnoll2025]; the quantity computed here is the prime-gap deviation from the smooth baseline, which neither supplies. The specific heat follows from the exact second moment of energy fluctuations,

$$C_V(\beta) = \beta^2 \sum_{p \le P} (\ln p)^2 \, n(1 \pm n),$$

with the plus sign for bosons and the minus sign for fermions. The bosonic sum diverges as $\beta \to 1^+$: the partial sums $\sum_{p \le x} 1/p$ track Mertens' law $\ln \ln x + B$ and grow without bound, so the Hagedorn-type point of the model sits at $\beta = 1$, in the neighborhood of the Bost-Connes phase-transition point [@bostconnes1995]. All computations run at $\beta \ge 1.1$.

The baseline is the smooth-density-of-states ideal gas with the same mode count and the same asymptotics: mode $k$ at energy $\ln x_k$, where $x_k$ solves $Li_2(x) = k$ exactly for every $k$ (the prime-number-theorem staircase, computed by Newton inversion to machine precision, strictly increasing). The deviation $\Delta C_V = C_V(\text{primes}) - C_V(\text{smooth})$ isolates the prime-gap imprint. Table 3 reports it.

| $\beta$ | $\Delta C_V$ bosonic | relative | $\Delta C_V$ fermionic | relative |
|:---:|:---:|:---:|:---:|:---:|
| 1.1 | $-1.386$ | 2.9 % | $-1.629$ | 3.6 % |
| 1.25 | $-0.874$ | 4.1 % | $-1.221$ | 6.4 % |
| 1.5 | $-0.358$ | 4.2 % | $-0.786$ | 11.2 % |
| 2.0 | $+0.139$ | 3.9 % | $-0.289$ | 10.9 % |
| 3.0 | $+0.429$ | 27.6 % | $+0.173$ | 14.4 % |
| 4.0 | $+0.428$ | 47.7 % | $+0.312$ | 40.8 % |
| 6.0 | $+0.255$ | 73.7 % | $+0.238$ | 72.5 % |

Table 3: Specific-heat deviation of the primon gas from the smooth staircase, $P = 10^6$ (78,498 modes), both statistics.

The deviation is nonzero at every sampled temperature in both statistics. It is negative at high temperature, where the smooth baseline overcounts the bottom of the spectrum — its first mode sits at $Li_2^{-1}(1) \approx 2.87$, above the first prime $2$, so the primes are denser in the first few modes — and it changes sign near $\beta \approx 2.5$. At low temperature the prime-gap structure dominates: at $\beta = 6$ the deviation is roughly three quarters of the specific heat itself in both statistics. The observable is internal to the Riemann-gas model; it is the minimal quantity that separates the arithmetic construction from the smooth ideal gas, not a laboratory prediction.

## 7. Crosswalk of terminology

The correspondence between the three vocabularies in play — number theory, quantum statistics, and condensed-matter/topological order — is as follows.

| Number theory | Quantum statistics | Condensed matter / topological order |
|:---|:---|:---|
| squarefree integers | occupation in $\{0,1\}$, Fermi counting | Pauli exclusion |
| unrestricted exponents | occupation in $\mathbb{N}_0$, Bose counting | mode sharing, condensation |
| $m$-th-power-free integers | bounded occupation, cap $m$ | Gentile intermediate statistics (no known braid datum) |
| prime modes, energy $\ln p$ | primon gas, partition function $\zeta(s)$ | conformal primon gas [@hartnoll2025] |
| Dirichlet character | abelian exchange phase $e^{i\pi\theta}$ | Laughlin quasiparticle phase at $1/m$ |
| roots of unity, cyclotomic data | fractional phases | quantum-group braid eigenvalues (Temperley-Lieb at $q$ a root of unity) |
| adelic product formula | normalization invariant | audit checksum for lattice-layer simulations |
| Möbius parity $\mu(n)$ | composite-statistics rule | composite-fermion / composite-boson parity |

The rows that matter for the adjudication are the third and the sixth: the truncation vocabulary (row three) names a counting object with no phase content, and the cyclotomic vocabulary (row six) names the phase objects. A reader working in any one of the three vocabularies can translate the result: occupation caps are not braid phases; characters are.

## 8. What a practitioner can do

The adjudication is directly usable as a design rule for any architecture that proposes to control exchange statistics through arithmetic or register-level constraints.

**Design rule 1.** Constraining the occupation bound of a register — a cap $m$ per mode — changes the accessible counting statistics (Fermi-like, intermediate, Bose-like) and nothing about exchange phases. An m-cap register is not an anyon. Architectures claiming anyonic behavior from bounded-occupation registers need a separate source for the phase.

**Design rule 2.** The arithmetic carrier of abelian exchange phases is the character group. A register parameterized by roots of unity reproduces the Laughlin phase at filling $1/m$ with the primitive $2m$-th root of unity; the non-abelian models correspond to the Temperley-Lieb family at $\delta_k = 2\cos(\pi/(k+2))$. Engineering the phase means engineering the root-of-unity structure, not the truncation.

**Adjudication table.** For a given target observable, the table states which carrier holds it:

| Target | m-family (occupation cap) | Character / root-of-unity model |
|:---|:---|:---|
| Fermi/Bose occupation distributions | reproduces (counting) | reproduces |
| Exchange phase $e^{i\pi/m}$ | absent (no phase datum) | primitive $2m$-th root of unity |
| Fibonacci braid eigenvalues | absent | $q^4$, $-q^2$ at $q = e^{i\pi/5}$ |
| Prime-gap thermodynamic imprint | carries (the lattice itself) | not applicable |

**Instruments.** The three verification programs are deposited with this paper and run anywhere with Python and mpmath: `verify_m_anyon.py` (family identity, golden occupations, phase-blindness, Gentile-versus-Haldane), `verify_braid_characters.py` (braid characters, Laughlin orders, Fibonacci and Temperley-Lieb data), `verify_prime_gap_thermo.py` (Mertens boundary, exact staircase baseline, specific-heat deviations). They are deterministic, take minutes on a laptop, and their outputs are machine-readable. The product-formula checksum of the earlier record [@zenodo22123068] remains the audit instrument for the lattice layer; the scripts here audit the phase layer.

## 9. Premise depth and boundaries

The premises end at three named levels.

**L0 — unanalyzable primitives.** The integers with unique factorization; the braid group and its standard representations; the maximum-entropy principle as a selection rule; the canonical ensemble.

**L1 — named imported inputs.** The classical identity for the m-th-power-free series; Gentile's intermediate statistics [@gentile1940]; Haldane's exclusion statistics and its g-form [@haldane1991]; the established regime-restricted relation between Haldane statistics and braid statistics [@chenng1994; @ye2015]; the in-corpus roots-of-unity braiding records [@zenodo21208491; @zenodo22024856]; the per-place identifications at fixed fugacity [@zenodo22035210].

**L2 — derived in this paper.** The no-phase statement for the bounded-occupation family (computed, Section 3); the Gentile-versus-Haldane separation (computed, Section 4); the character reproduction of the standard phases (computed, Section 5); the prime-gap specific-heat deviation (computed, Section 6).

The claims are as deep as L2. Nothing here derives braid phases from arithmetic; the content locates which arithmetic objects carry which phases, and shows the truncation object carries none. The spin-statistics connection [@ducksudarshan1998] — exchange phase tied to spin through Lorentz symmetry, microcausality, and positive energy — is not engaged; it remains the boundary drawn in the configuration-space record [@zenodo21962450] and the structural invariant stated in the boson-fermion record [@zenodo21964598].

## 10. Verification and reproducibility

Every quantitative statement in this paper is reproduced by the three deposited scripts, whose check inventory is: `verify_m_anyon.py` — the Dirichlet identity for the m-family (sieved sums against the zeta ratio, error below $6 \times 10^{-8}$), the golden occupation values (Fermi $1/3$ and Bose $1$ at $x = 1/2$), the permutation eigenvalues $\{1,1,-1\}$ and the exact phase-invariance of observables, and the Gentile-versus-Haldane deviation grid; `verify_braid_characters.py` — the braid relations of the one-dimensional characters, the Laughlin phase orders, the Fibonacci eigenvalues at $q = e^{i\pi/5}$, and the Temperley-Lieb family values; `verify_prime_gap_thermo.py` — the Mertens-law divergence boundary, the exact staircase baseline (78,498 Newton inversions to machine precision), and the specific-heat deviations of Table 3.

The runtime environment is Python 3.12 with mpmath 1.3.0; the scripts use the standard library and mpmath only, are deterministic (no random numbers), and need no network access. The scripts run from the deposited directory with `python verify_m_anyon.py`, `python verify_braid_characters.py`, and `python verify_prime_gap_thermo.py`; each prints a per-check report and writes a machine-readable JSON result. Golden values: bosonic and fermionic specific heats of the primon gas at $\beta = 3$ are $1.5505264$ and $1.2045416$ (arbitrary units, $P = 10^6$).
