---
title: "The Corrected Primon-Gas Dictionary: Zeta Partition Functions and the Discipline of Arithmetic Interpretations"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-29"
abstract: |
  The primon gas — a free quantum gas whose single-particle modes are
  indexed by the primes, with energies equal to the logarithms of the primes
  — has connected quantum statistical mechanics with multiplicative number
  theory since the early 1990s and remains in active use in high-energy
  theory. This paper consolidates the correspondence into a single audited
  reference: a term-by-term dictionary in which every entry is corrected and
  every formula is verified by deposited deterministic computations, a
  five-level ladder that separates mathematical isomorphism from physical
  realization claims, and a negative list stating what the correspondence
  does not license. The dictionary is exact and model-specific. The premises
  end where a physical temperature would be identified at a p-adic place,
  and no such identification is asserted.
keywords: [primon gas, zeta function, partition function, quantum statistics,
  Riemann zeros, Gentile statistics, spectral statistics]
---

## 1. Introduction

The primon gas is a free quantum gas whose single-particle modes are
labelled by the primes: mode $p$ carries energy $\varepsilon_p = \ln p$, the
many-body states are labelled by the integers $n = \prod_p p^{a_p}$, and the
Hamiltonian is multiplication by $\ln n$. Its grand canonical partition
function is the Riemann zeta function, and its statistics — unrestricted,
squarefree, or bounded occupation — generate a small family of exact
identities between thermodynamic quantities and multiplicative number
theory. The construction goes back to the statistical reading of the zeta
function [@julia1990], the supersymmetric reformulation of the Möbius
inversion [@spector1990], and the study of arithmetic gases [@bakas1991];
its deepest version is the Bost–Connes system, where the symmetry-breaking
phase transition at inverse temperature one carries the arithmetic of the
maximal abelian extension of the rationals [@bostconnes1995]. The
correspondence is not dormant: it is currently used in cosmology, where
modular-invariant states near a spacelike singularity define dual primon
gases [@hartnoll2025] and complex primon gases built from the Gaussian and
Eisenstein integers [@declerck2025], and in the statistical mechanics of
mean-field spin glasses, where the gas acquires a kernel representation
[@franchini2024].

This paper does not claim the correspondence as new. Its contribution is a
consolidation with discipline: a corrected, audited dictionary in which
every entry is stated exactly and every formula is verified by deposited
deterministic computations; a five-level ladder that separates what the
correspondence is (an exact mathematical isomorphism) from what it is not (a
physical realization claim); a ledger of corrections to errors that have
circulated in informal drafts of the dictionary; and a negative list stating
what the correspondence does not imply. Earlier work in the same research
program established the squarefree origin of the Fermi–Dirac/Bose–Einstein
distinction [@adelicquantumstatistics2026], the bounded-occupation family
with its absent exchange phase [@arithmeticanyons2026], the consolidated map
with its practitioner crosswalk [@adelicquantumarithmetic2026], the
computational discrimination of the arithmetic cut from matched-density
nulls [@arithmeticcutdiscrimination2026], and the realization-independent
hierarchy distance that underlies the whole construction
[@distinctionbasedultrametric2026].

## 2. The Correspondence

*Setup.* Single-particle modes are labelled by primes $p$ with energies
$\varepsilon_p = \ln p$; many-body states are labelled by integers
$n = \prod_p p^{a_p}$ with occupation exponents $a_p$; the Hamiltonian acts
by $(\hat H f)(n) = (\ln n)\, f(n)$. The inverse temperature $\beta$ is a
formal parameter; its identification with the complex variable $s$ of the
zeta function is a choice on the real section, flagged throughout as
formal.

*Partition functions.* The grand canonical partition functions are exact:

$$Z_B(\beta) = \prod_p \left(1 - p^{-\beta}\right)^{-1} = \zeta(\beta),$$

for unrestricted occupation ($a_p \in \mathbb N_0$);

$$Z_F(\beta) = \prod_p \left(1 + p^{-\beta}\right) = \frac{\zeta(\beta)}{\zeta(2\beta)},$$

for squarefree occupation ($a_p \in \{0,1\}$); and

$$\ln Z_{MB}(\beta) = \sum_p p^{-\beta} = P(\beta),$$

for the distinguishable gas, where $P$ is the prime zeta function. The
bounded-occupation (Gentile) family interpolates:

$$Z_m(\beta) = \prod_p \frac{1 - p^{-(m+1)\beta}}{1 - p^{-\beta}},$$

with $m = 1$ reproducing the Fermi gas and $m \to \infty$ the Bose gas.
No exchange phase appears anywhere in the family: an occupation cap is not a
braid phase, and the phases that standard anyon models carry are
multiplicative characters at roots of unity — a different arithmetic object
[@arithmeticanyons2026]. The three free-gas statistics are transforms of the
prime zeta function:

$$\ln Z_B = \sum_{k \ge 1} \frac{P(k\beta)}{k}, \qquad
\ln Z_F = \sum_{k \ge 1} \frac{(-1)^{k+1} P(k\beta)}{k}, \qquad
\ln Z_{MB} = P(\beta).$$

A chemical potential, i.e. a fugacity $z = e^{\beta\mu}$, deforms the Bose
product to

$$Z_\mu(\beta) = \prod_p \left(1 - z\, p^{-\beta}\right)^{-1}
= \sum_n z^{\Omega(n)} n^{-\beta},$$

where $\Omega(n)$ counts prime factors with multiplicity. This is the
$z$-weighted generating function of the integers, *not* a Dirichlet
$L$-function: a Dirichlet character twists each Euler factor as
$\prod_p (1 - \chi(p) p^{-s})^{-1} = L(s, \chi)$, a multiplicative
phase filter, which is a different object from a chemical potential.

*Thermodynamic observables.* With $U = -\partial_\beta \ln Z$,

$$U_B = \sum_p \frac{\ln p}{p^\beta - 1}, \qquad
U_F = \sum_p \frac{\ln p}{p^\beta + 1},$$

and the specific heat carries the full derivative factor:

$$C_V = -\beta^2\, \partial_\beta U, \qquad
C_V^B = \beta^2 \sum_p \frac{(\ln p)^2\, p^{-\beta}}{(1 - p^{-\beta})^2}, \qquad
C_V^F = \beta^2 \sum_p \frac{(\ln p)^2\, p^{-\beta}}{(1 + p^{-\beta})^2}.$$

The entropy is $S = \ln Z + \beta U$, which for the Bose gas reads

$$S = \sum_p \left[-\ln(1 - x_p) + \beta\,(\ln p)\,\frac{x_p}{1 - x_p}\right],
\qquad x_p = p^{-\beta}.$$

*Zeros as fluctuations, not definitions.* The level-count function
$\psi(x) = \sum_{n \le x} \Lambda(n)$ obeys the explicit formula

$$\psi_0(x) = x - \sum_{\rho} \frac{x^\rho}{\rho} - \ln(2\pi)
- \frac12 \ln\!\left(1 - x^{-2}\right),$$

so the nontrivial zeros of the zeta function enter as subleading oscillatory
corrections to the smooth count. They do not define the statistics and they
do not define the leading thermodynamics. The zeros themselves follow the
GUE two-point law $R_2(s) = 1 - (\sin \pi s / \pi s)^2$
[@montgomery1973; @odlyzko1987]; the primes are Poisson-like beyond a hard
core [@gallagher1976]: consecutive primes differ by at least two (for primes
at least three), which is a minimum unfolded spacing of $2/\ln p$ — a first
bin of the spacing histogram that is exactly empty below that width. The
sharp small-spacing exclusions that discriminate the prime spectrum from
random sets therefore test the primes, not the zeros.

*Operators and phase structure.* The Hamiltonian is the multiplication
operator by $\ln n$, with $\operatorname{Tr} e^{-\beta \hat H} = \zeta(\beta)$;
the von Mangoldt function is a *coefficient*, entering through
$-\zeta'(s)/\zeta(s) = \sum_n \Lambda(n) n^{-s}$, not an operator of the
model. The power $\zeta^k$ corresponds to $k$ independent copies of the gas,
not to $k$-body interactions. The pole of $\zeta(\beta)$ at $\beta = 1$ is
the infinite-mode limit of the free gas, realized in the Bost–Connes system
as a genuine symmetry-breaking transition [@bostconnes1995]; at any finite
prime cutoff there is no singularity, only a smooth crossover, and a
numerical evaluation point such as $\beta = 1.06$ is a probe near the
would-be pole, not a phase-transition temperature of any finite system.

## 3. The Correction Ledger

The following corrections repair errors that circulated in an informal
draft dictionary of the correspondence. Each row states the erroneous form
and the corrected form; every corrected formula is verified in code (Section
6).

(a) *Modes and states.* The draft wrote $\varepsilon_i \equiv \ln n_i$,
conflating levels with states. The single-particle modes are the primes with
energies $\ln p$; the many-body states are the integers $n = \prod_p p^{a_p}$
with energies $\ln n$. The many-body level count up to energy $E$ is
$\lfloor e^E \rfloor$ (integers), while the single-particle mode count is
the prime-counting function; the two are different objects.

(b) *Chemical potential versus character.* The draft mapped
$e^{\beta\mu}$ to a Dirichlet character. The fugacity gives the
$z$-weighted generating function of Section 2; a character is a twist of the
Euler factors. They are not the same object.

(c) *The Maxwell–Boltzmann row.* The draft wrote a Boltzmann row with a
labelling factor inconsistent with the unification rule. The consistent
statement is $\ln Z_{MB} = P(\beta)$.

(d) *Specific heat.* The draft defined $C_V = \partial_\beta U$. The correct
definition is $C_V = -\beta^2\, \partial_\beta U$; the missing factor and
sign are restored in the formulas above.

(e) *Entropy.* The draft's entropy had a wrong sign on the first term and a
dimensionally wrong second term. The correct form carries $\beta \ln p$ in
the second term, as above.

(f) *The small-spacing exclusion.* The draft attributed the sharp
small-spacing exclusion of the prime spectrum to GUE repulsion of the zeros.
The exclusion tests the primes (twin-gap hard core); the zeros' GUE
behaviour is a separate statement.

(g) *Phase transitions and continuation.* The draft read the pole of the
zeta function as a physical transition of a finite system and analytic
continuation as the thermodynamic limit. The pole is the infinite-mode
limit; continuation extends the function and corresponds to no finite
system's partition function.

(h) *Eigenstates.* The draft called the primes "energy eigenstates." The
eigenstates of $\hat H$ are the integers.

(i) *The Hamiltonian.* The draft identified the Hamiltonian with an
arithmetic derivative. It is multiplication by $\ln n$; the von Mangoldt
function enters as a coefficient of $-\zeta'/\zeta$.

(j) *Interactions.* The draft read Dirichlet convolution as an interaction
and $\zeta^k$ as $k$-body interactions. Convolution is a generating-function
parallel, not a Hamiltonian term, and $\zeta^k$ is $k$ independent species.

(k) *Observables.* The draft's "Theorem 2" bundled the specific-heat
signature with the small-spacing exclusion. They are different observables
with different nulls: the specific heat is thermodynamic, the exclusion is a
two-point statistic of the prime spectrum [@arithmeticcutdiscrimination2026].

## 4. The Five-Level Interpretive Ladder

Claims of the form "arithmetic structure appears in physics" are not one
claim. They stratify into five levels.

- **L0 — distinction.** The marking of an inside against an outside. A
  methodological primitive: the framework treats it as unanalysable, which
  is a choice of starting point, not an ontic commitment; the re-entrant
  calculus developed this primitive into a formal system
  [@reentrantdistinctions2026].
- **L1 — hierarchy.** The distinction-based ultrametric: the number of
  distinctions required to separate two states. Definitional and
  realization-independent; arithmetic enters only when a hierarchy is
  dressed in prime or $p$-adic clothing [@distinctionbasedultrametric2026;
  @ultrametricprogram2026]. The counting construction that turns
  distinctions into quantities — quantity as broken idempotence — is prior
  work [@idempotentcore2026], and is credited rather than re-derived here.
- **L2 — isomorphism.** Euler products, zeta identities, and the
  bounded-occupation family. An exact mathematical isomorphism; the content
  of Section 2 lives here.
- **L3 — statistical hypothesis.** Physical spectra carry arithmetic
  correlations beyond universal random-matrix statistics. A falsifiable
  distributional claim, requiring a pre-registered null.
- **L4 — physical instantiation.** A specified system realizes the
  arithmetic partition function. A claim about a laboratory system, held to
  the same protocol discipline that the finite-distinction reading of
  quantum mechanics applies to its own claims [@finitedistinctionqm2026].

The ladder carries three inference rules. First, *L2 cannot imply L4*: the
fact that a formal partition function equals the zeta function does not
place any physical system at L4. Second, *L3 is the only admissible
bridge*: a physical claim must be stated as a distributional prediction with
a pre-registered null. Third, *L4 requires a protocol*: a specified
spectrum, a specified counting rule, a pre-registered null, and a
pre-registered test.

Two honest statements about these rules. The rules are methodological
discipline, not a discovery: the L2-to-L4 inference they forbid is an
inference that informal drafts of this very correspondence made, so the
rules are non-vacuous as self-correction, and as external guidance they are
a pre-commitment — "admissible inference" is defined by the protocol above,
and the ladder's falsifiability is precisely that an exhibited admissible
L2-to-L4 inference would break its central rule. And the ladder is a
classificatory device, not a theory: it cannot be falsified by data, only
outperformed or abandoned. This paper's empirical content is inherited, not
new: the discrimination results on which the L3 statements rest are
published elsewhere, including a confirmed separation of the arithmetic cut
from matched-density nulls and a disconfirmed specific-heat-only
separation, adjudicated as pre-registered [@arithmeticcutdiscrimination2026].

## 5. What the Correspondence Licenses, and What It Does Not

*The negative list.* The exactness of the dictionary does not license: a
derivation of spin–statistics from the Euler product; a universe made of
primes; an identification of Riemann zeros with measured energy levels; or
evidence for the Hilbert–Pólya programme. The zeros enter through the
explicit formula as fluctuations; they define neither the statistics nor the
leading thermodynamics. Where the informal draft preamble spoke of "the
physical universe and the mathematical universe as two dialects of the same
statistical language," the precise statement is narrower: a free quantum gas
on a prime-logarithmic spectrum is combinatorially and analytically
isomorphic to multiplicative number theory — the primes provide the modes,
the integers provide the many-body states, the zeta function provides the
partition function — and that isomorphism is exact in the toy model and
silent beyond it.

*What a practitioner can do.* Two concrete artifacts follow from the
dictionary. First, a specification for an engineered log-prime spectrum: a
device (superconducting registers, optical lattices, or photonic arrays)
whose mode frequencies are proportional to $\ln p$, whose occupation caps
implement the Gentile family of Section 2, and whose readout follows the
corrected thermodynamic formulas; every formula needed for the readout is
verified rather than asserted (Section 6). Second, a scope statement that
decides, *before* an experiment, what a realization claim may consist of:
by the ladder's rules, a claim that a device realizes the arithmetic
partition function must state the spectrum, the counting rule, the null
model, and the test in advance — an engineering-relevant discipline that
separates a physical signature from a simulation.

## 6. Verification

Every quantitative statement in Sections 2 and 3 is verified by two
deposited, deterministic computation suites (52 checks in total, all
passing, released with this paper).

The first suite verifies the dictionary identities at $\beta = 2$: the three
partition functions against $\zeta(2) = \pi^2/6$, $\zeta(2)/\zeta(4)$ and
the prime zeta value $P(2) = 0.45224742\ldots$, with explicit
truncation-tail corrections (the tail at prime cutoff $10^6$ is computed
with the three-term expansion of the exponential integral, not the
one-term form, which errs by several percent); the unification expansions to
$k = 30$; the Gentile limits $m = 1 \to$ Fermi and $m \to \infty \to$ Bose;
the specific-heat definition against a finite-difference computation of
$-\beta^2\, \partial_\beta U$; the entropy against $\ln Z + \beta U$; and
the fugacity identity $Z_\mu = \sum_n z^{\Omega(n)} n^{-\beta}$ against a
direct sum over integers.

The second suite verifies the spectral and analytic statements: the explicit
formula $\psi_0(x)$ at $x = 20$ and $x = 30$ against the exact summatory von
Mangoldt function, using 120 exact zero ordinates (residuals 0.018 and
0.020); a seeded Monte Carlo of the Gaussian unitary ensemble (120 matrices
of size 150, semicircle unfolding — no rank unfolding), whose two-point
correlation matches $1 - (\sin \pi s / \pi s)^2$ in the bulk with maximum
deviation 0.036 and whose number variance at window lengths 5, 10 and 20
matches the exact two-point reduction $\Sigma^2(L) = L - 2\int_0^L (L-s)(\sin \pi s/\pi s)^2\, ds$
to within the stated tolerance (the Monte Carlo windows are centred on a
grid of arbitrary positions; counting around data points instead would
measure the Palm count, whose mean is $2\int_0^{L/2} R_2(t)\, dt$, not $L$ —
a subtlety the deposited code documents and avoids); the number variance at
$L = 20$ and $L = 3400$ against the Dyson asymptotic
$(1/\pi^2)\left[\ln(2\pi L) + 1 + \gamma - \pi^2/8\right]$, which converges
from below with a relative deficit of 20–33% over $L \le 50$; the exact
logarithmic-integral unfolding $\operatorname{Li}(x) = \operatorname{Ei}(\ln x)$
against the known values $\operatorname{Li}(2) = 1.0451637801\ldots$ and
$\operatorname{Li}(10^6) = 78627.54916\ldots$, together with a demonstration
that the asymptotic series for $\operatorname{Li}$ is unusable at small
argument; the Fermi observables against finite differences; the identity
$\operatorname{Tr} e^{-\beta \hat H} = \zeta(2)$ with tail correction; the
von Mangoldt convolution $\Lambda = \log * \mu$; $\zeta^k$ as $k$ independent
species; and the twin-gap hard core as a *computed* bin count — among
78,496 unfolded spacings of primes below $10^6$, the first bin is empty
while a continuous Poisson null expects several thousand, a hard-core
deficit of $z = -86.4$.

The anchors of the published lineage are recovered with attribution:
$\beta^2/(\beta - 1)^2 = 312.111$ at $\beta = 1.06$ is the analytic
pole-amplitude value; the exact recomputed specific heat at $\beta = 1.06$
is $\approx 311.9$ (finite sum to prime cutoff $10^7$ plus analytic tail);
and the value $316.3$ that circulated earlier is *not* the exact value — it
is a finite-difference artifact of a coarse computation, and is treated as
an adjudication target only.

Two data notes follow from the re-computation. First, a zero-ordinate cache
deposited with an earlier study of this program [@arithmeticcutdiscrimination2026]
was found, on re-computation against independent exact values, to be a
coarse approximation with maximum error $\approx 0.38$; the suites here use
exact values instead, and downstream users of that cache should re-derive
the zeros rather than reuse it. Second, the prime-spacing distribution at
mid-range shows a large deviation from a continuous Poisson reference
($z = +27.5$ in one bin): prime gaps are even and alternate modulo six, so a
continuous Poisson process is the wrong reference there; the correct nulls
are the matched-level-density ensembles of the discrimination study, which
are out of scope here and declared as such.

*Reproducibility statement.* The suites are deterministic; the seeded Monte
Carlo uses seeds 20260829 and 777. Runtime: Python 3.12.10, NumPy 2.4.4,
SciPy 1.17.1, mpmath (exact zero ordinates), on Windows x64; wall-clock for
the full second suite is minutes on a laptop. The scripts and their outputs
are deposited with this paper; every number in this section is produced by
running them.

## 7. Premise Boundaries

Where the premises end, stated plainly. The identification $\beta = s$ is a
formal choice, flagged throughout; nothing here identifies a physical
temperature at any $p$-adic place. The completeness of the correction ledger
is an audit-level statement, not a proof: a twelfth error found by an
independent reader would be a corrigendum, not a collapse, and that status
is asserted rather than concealed. The empirical content is inherited from
the discrimination study and is not re-claimed here. And the central
honesty of the ladder, stated once: the correspondence is verified-exact at
L2, and nothing in that exactness moves the L3/L4 needle.

## 8. Term Crosswalk

For the reader arriving from either side, the correspondence in one table.

| Quantum statistics | Multiplicative number theory |
|---|---|
| Single-particle mode $p$, energy $\ln p$ | Prime $p$ |
| Many-body state, energy $\ln n$ | Integer $n = \prod_p p^{a_p}$ |
| Occupation exponent $a_p$ | Prime exponent in the factorization |
| Bose gas (unrestricted occupation) | All integers; $\zeta(\beta)$ |
| Fermi gas (squarefree occupation) | Squarefree integers; $\zeta(\beta)/\zeta(2\beta)$ |
| Boltzmann gas | Prime zeta function $P(\beta)$ |
| Gentile family (occupation cap $m$) | Exponents bounded by $m$ |
| Fugacity $z = e^{\beta\mu}$ | Weight $z^{\Omega(n)}$; not a character |
| Specific heat $C_V = -\beta^2\, \partial_\beta U$ | Prime-weighted variance of $\ln p$ |
| Level-count oscillations | Explicit formula; zeta zeros as corrections |
| Small-spacing exclusion | Twin-gap hard core of the primes |
