---
title: "The Distinction-Based Ultrametric: A Hierarchy Distance Without Primes, and the Statistical Test of Arithmetic Structure in Physical Spectra"
author: "Rowan Brad Quni-Gudzinas"
affiliation: "QNFO"
orcid: "0009-0002-4317-5604"
date: "2026-08-28"
license: "CC BY 4.0"
status: "published"
version: "1.0"
doi: ""
concept_doi: "https://papers.qnfo.org/papers"
wbs: "QNFO.UMP.014"
slug: "distinction-based-ultrametric"
abstract: |
  Quantum mechanics is written in one completion of the rational numbers, the real
  line, though Ostrowski's theorem gives one completion for every prime. A line of
  work reads physical structure through those other places, but its empirical tests
  of prime-specific geometry in physical systems have repeatedly returned null
  results. This paper separates what survives from what does not. The surviving
  object is not any prime-specific arithmetic but a finite hierarchy distance: the
  number of distinctions required to separate two states. We state that formula,
  show it is an ultrametric on any finite hierarchy and independent of the
  realization chosen (p-adic valuation, formal Laurent series, or plain nested
  partitions), and verify both claims in deposited, deterministic computation. The
  empirical question then becomes statistical rather than geometric: do physical
  spectra carry arithmetic information beyond universal random-matrix statistics?
  We implement the five observables that test this, validate them on known answers
  (including a computational confirmation of the Montgomery-Odlyzko pair
  correlation for the Riemann zeros), and apply them to two real molecular spectra.
  The first real-data result is negative for arithmetic structure in the
  pair-correlation channel: neither molecule is GUE-like. The machinery and the
  pre-registerable null models are deposited, so the question can be asked of
  larger spectra as they become available. The premises end where a physical length
  is identified at a p-adic place; everything below that line is computation.
---

# The Distinction-Based Ultrametric: A Hierarchy Distance Without Primes, and the Statistical Test of Arithmetic Structure in Physical Spectra

## Abstract

Quantum mechanics is written in one completion of the rational numbers, the real line, though Ostrowski's theorem gives one completion for every prime. A line of work reads physical structure through those other places, but its empirical tests of prime-specific geometry in physical systems have repeatedly returned null results. This paper separates what survives from what does not. The surviving object is not any prime-specific arithmetic but a finite hierarchy distance: the number of distinctions required to separate two states. We state that formula, show it is an ultrametric on any finite hierarchy and independent of the realization chosen (p-adic valuation, formal Laurent series, or plain nested partitions), and verify both claims in deposited, deterministic computation. The empirical question then becomes statistical rather than geometric: do physical spectra carry arithmetic information beyond universal random-matrix statistics? We implement the five observables that test this, validate them on known answers (including a computational confirmation of the Montgomery-Odlyzko pair correlation for the Riemann zeros), and apply them to two real molecular spectra. The first real-data result is negative for arithmetic structure in the pair-correlation channel: neither molecule is GUE-like. The machinery and the pre-registerable null models are deposited, so the question can be asked of larger spectra as they become available. The premises end where a physical length is identified at a p-adic place; everything below that line is computation.

## 1. The Archimedean shadow

Quantum mechanics is written in the Archimedean completion of the rational
numbers. The complex Hilbert space of the standard formalism is built on the real
line, and the real line is one completion among all of them: Ostrowski's theorem
classifies the completions of the rational numbers as the real line and one
p-adic field per prime [@quni2026ump004]. The primes are the other places. Their
structure is multiplicative — unique factorization — never additive.

A research line reads physical structure through those places. Its strongest
published results are isomorphisms of mathematical structure: the unrestricted
exponent rule on an integer lattice gives the Riemann zeta function and
Bose-Einstein occupation, the squarefree rule gives a ratio of zeta values and
Fermi-Dirac occupation, and the bounded-occupation family between them carries no
exchange phase [@quni2026stats; @quni2026anyons; @quni2026res023]. Those results
are exact and computationally verified. But the empirical claim that physical
systems exhibit the prime-specific geometry has, in the tests run so far, come
back null (Section 3).

Why a reader should care. Two reasons. First, the failure pattern is itself a
finding: the tests that failed were all geometric — they asked whether a finite
physical matrix is exactly ultrametric, or whether a spectrum shows exact
log-periodicity. The tests that have not been run are statistical — whether the
distribution of a large spectrum carries arithmetic information beyond what
universal random-matrix theory predicts. The distinction between these two kinds
of test is the load-bearing correction this paper makes. Second, the surviving
object — the distinction-based distance — is finite, prime-free, and constructible
on any hierarchy, which makes it usable in a way the prime-specific arithmetic is
not. The map-territory statement is explicit: arithmetic provides structural
insight; physics reveals statistical distributions.

## 2. The distinction-based ultrametric formula

A finite-resolution world distinguishes states rather than positioning them. Two
states are either distinct or not at a given resolution, and the natural distance
is the number of distinctions required to separate them:

$$d(a,b) = \min\left\{\text{number of distinctions required to separate } a \text{ and } b\right\}.$$

On a finite rooted tree whose leaves are the states, this is the depth of the
lowest common ancestor, measured from the leaves. If the leaves sit at depth $k$
and the lowest common ancestor of $a$ and $b$ is at depth $\ell$, then
$d(a,b) = k - \ell$. This is the cophenetic distance of classical taxonomy
[@sokal1962; @jardine1971; @johnson1967].

Two facts are exact and were verified in code (Section 5). First, the induced
distance satisfies the ultrametric inequality

$$d(a,c) \le \max(d(a,b), d(b,c)),$$

which follows because among any three leaves, the two largest lowest-common-ancestor
depths coincide. Second, the "min" is fixed on a tree — the path is unique — but
the qualification matters: on a directed acyclic graph with multiple paths, the
minimum over paths need not equal the tree value. The formula requires the tree,
and a deposited computation exhibits the counterexample. The distinction, the
counting of distinctions, and finite resolution are unanalyzable primitives here;
this is the premise boundary stated verbatim in [@quni2026res021].

The formula is realization-independent. A stated digit-tree embedding assigns
each leaf a base-$p$ digit string; the reversed string is an integer (p-adic
realization) and a coefficient vector (formal Laurent realization). With the rule
$d = (k-1) - v(x_a - x_b)$, where $v$ is the valuation of the difference, the three
distance matrices — partition, p-adic, Laurent — are identical. The
prime-specific arithmetic is one realization; the hierarchy is the invariant, as
stated in [@quni2026res023]. The distinction-based distance needs no primes.

## 3. What has been tested, and what has not

The empirical tests of prime-specific structure in physical systems are a ledger
of nulls, and they should be read by channel, not lumped together.

The geometric channel has been tested and nullified. The CMB shows no
log-periodic oscillations (a certified radix-agnostic null at $p = 0.89$ on Planck
2018 data [@quni2026cmbnull]) and only upper bounds in the bispectrum
[@quni2026cmbbis]. The Fenna-Matthews-Olson coupling matrix is anti-ultrametric
(cophenetic correlation 0.426, $p = 0.984$), and its exact-clustering test returns
$p = 0.598$ [@quni2026register]. A generic clock-rest coupling violates Parisi
ultrametricity in 29-35% of simulated instances [@quni2026register]. The
ultrametric-QEC independent-error threshold is $2.0\times10^{-4}$, roughly fifty-five
times below the surface-code threshold [@quni2026register]. A pre-registered search
for adelic structure in the Standard Model mass spectrum found one weak hint in
fifteen tests and did not reject the null [@quni2026compton]. An anharmonic mass
ladder was falsified by its pre-registered null [@quni2026particle].

The statistical channel has not been tested. The specific-heat deviation of the
primon gas — the observable that separates the arithmetic spectrum from a smooth
ideal gas [@quni2026anyons] — is a statistical, not a geometric, signature, and no
physical realization of it has been measured. The distinction-based formula
itself is definitional: it makes no empirical claim, so it is outside the
falsified class entirely.

The methodological point follows directly from the ledger. The Fenna-Matthews-Olson
complex has seven sites; seven levels cannot support a correlation function. The
tests that failed were small and geometric. The tests that could succeed are
large and statistical — pair correlations, form factors, number variances — which
is where the number-theoretic signal, if it exists, is known to live
[@montgomery1973; @odlyzko1987; @bogomolny1995].

## 4. The surviving empirical claim

The surviving empirical claim is H1 of [@quni2026res023]: ultrametric structure is
an effective compression and clustering prior, and, in the spectral form this
paper adopts, physical spectra may carry arithmetic information beyond universal
random-matrix statistics. It is tested with five observables, each with a null
model.

1. **Pair correlation.** After unfolding, $R_2(s) = 1 - (\sin\pi s / \pi s)^2$ for
   the Gaussian unitary ensemble, with arithmetic corrections beyond it
   [@montgomery1973; @bogomolny1995]. Null: pure GUE.
2. **Spectral form factor.** The ramp-versus-plateau structure distinguishes
   correlated from uncorrelated spectra [@berry1985]. Null: pure GUE ramp.
3. **Number variance and rigidity.** GUE grows as $(1/\pi^2)\log L$, Poisson as
   $L$ [@berry1985]. Null: pure GUE.
4. **Partition-function thermodynamics.** The Bost-Connes system has partition
   function $Z(\beta) = \prod_p (1-p^{-\beta})^{-1} = \zeta(\beta)$, with a phase
   transition at $\beta = 1$ [@bostconnes1995]. Null: smooth ideal-gas specific heat.
5. **Log-periodic corrections.** Subleading corrections to scaling of the form
   $f(x) = x^\alpha (1 + \epsilon\cos(2\pi\log x/\log\lambda))$; the robust
   quantity is the period, not the amplitude.

The disconfirmation criterion is stated in advance. If a large-N physical
spectrum shows pure GUE statistics with no arithmetic corrections, the claim of a
physics-relevant arithmetic substrate is falsified at the distribution level, not
merely at the level of finite geometric approximation. This is the H1 leg of the
2028 decision point of [@quni2026res023].

## 5. Computational verification

Every quantitative statement in this paper is reproduced by a deposited,
deterministic script (seed 20260828, Python 3.12, NumPy 2.4.4, SciPy 1.17.1),
with outputs in the record's verification directory.

The formula is verified in `sim-distinction-ultrametric-verification.py`: the
golden taxonomy distances satisfy the ordering $d(\text{Dog},\text{Wolf})=1 <
d(\text{Dog},\text{Cat})=2 < d(\text{Dog},\text{Human})=3 <
d(\text{Dog},\text{Snake})=4$; the ultrametric inequality holds on thirty seeded
random trees; and the three realizations give identical distance matrices on
8/9/16-leaf trees.

The estimators are verified in `sim-statistical-signatures-full.py` (eight checks)
and `sim-statistical-signatures-smoke.py` (seven checks). The smoke suite recovers
the Bost-Connes critical behavior — the pole amplitude $C_V(1.06) = 316.3$ against
the predicted $\beta^2/(\beta-1)^2 = 312.1$ — and the log-periodic detector recovers
a known period. The full suite recovers the Poisson flat pair correlation, the
GUE curve, the primes' twin-gap hard core (the first bin is exactly zero because
the minimum prime gap of 2 maps to a minimum unfolded spacing of $2/\ln p$), and
the Dyson number-variance formula.

The Montgomery-Odlyzko law is verified in `sim-riemann-zeros-fast.py`: the first
three thousand Riemann zeros, unfolded by the Riemann-von Mangoldt smooth count,
give a pair correlation matching the GUE curve with mean absolute deviation
$0.061$, a repulsion $R_2(0) = 0.030$, and a Dyson number variance $1.044$ against
the predicted $0.525$. The zeros — not the primes — are the arithmetic object whose
pair correlation matches GUE; the primes themselves are Poisson-like beyond the
hard core, per [@gallagher1985].

## 6. Real data

Real data was acquired and run through the machinery (`sim-benchmark-real.py`),
with provenance from the ExoMol molecular line-list repository.

The NaH Rivlin line list (3,339 levels) rejects both nulls: its pair correlation
deviates from the Poisson curve by 0.135 and from the GUE curve by 0.356, with
empirical p-values of 0 against both (Bonferroni-Holm corrected). It is neither
Poisson nor GUE — quasi-regular, its own class, as a molecule with rotational
ladders is expected to be.

The H2O POKAZATEL line list (200,000 states, 199,866 unique) is Poisson-like: its
pair correlation deviates from the Poisson curve by only 0.028 (p = 1.000) while
rejecting GUE at p = 0.000. Its number variance grows linearly, as the Poisson null
predicts.

The first real-data result in the pair-correlation channel is negative for
arithmetic structure: neither molecule is GUE-like, and one is Poisson-like. This
is a result, not a silence — it is the first statistical-channel data point,
consistent with the geometric-channel nulls, and it calibrates the machinery on
real spectra for the larger datasets to come. The null models (Poisson and GOE
Monte Carlo at $n=2000$, matched through the same unfolding) were themselves
calibrated against controls, which pass.

## 7. What a practitioner can do

A metrologist or spectroscopist gets a machine, not a conclusion. The deposited
scripts unfold any level sequence by a smoothed staircase, compute the five
observables, and return an empirical p-value against the GUE and Poisson nulls
with a multiple-comparison correction. A hierarchy-detection toolbox — the
distinction-based distance plus an ultrametricity test — classifies a dataset as
hierarchical or not; the auditable-attention proof of concept [@quni2026attention]
is the same distance applied to a transformer. The crosswalk is short: the
number of distinctions is the cophenetic distance; a p-adic valuation is one
realization of it; a place is a measurement basis; a prime gap is a spectral
irregularity; the Bruhat-Tits tree is the regular-tree specialization of a finite
hierarchy.

## 8. Where the premises end

The claim is as deep as its premises. The distinction, the counting of
distinctions, and finite resolution are unanalyzable primitives (L0). The
ultrametric inequality is definitional (L1). The lowest-common-ancestor
construction is derived and exact (L2). Realization independence is structural
and computationally verified (L3). The empirical hypothesis H1 — that physical
spectra carry arithmetic information — is L4, and it is where the risk sits. The
premises end where a physical length is identified at a p-adic place; nothing in
this paper asserts such an identification.

## 9. Related work

The distinction-based distance is the cophenetic distance of numerical taxonomy
[@sokal1962; @jardine1971; @johnson1967] and the object of modern hierarchical
clustering theory [@carlsson2010]. Ultrametric fitting has an active
algorithmic literature [@chierchia2019; @contreras2011], and cophenetic metrics
appear in topological data analysis [@guzel2020]. The statistical treatment of
ultrametricity in networks [@fang2023] and the fairness of hierarchical clustering
[@maity2026] are contemporaneous. The number-theoretic spectral statistics are
Montgomery-Odlyzko [@montgomery1973; @odlyzko1987], Gallagher's Poisson statistics
for the primes [@gallagher1985], and the Bogomolny-Keating corrections
[@bogomolny1995]; the program's own spectral-rigidity reading of the Riemann
hypothesis is [@quni2026spectral]. Within the program, the formula is the graded distinguishability
map of [@quni2026ump004], the finite-distinction geometry of [@quni2026res021],
and the hierarchy invariant of [@quni2026res023]; the arithmetic realization it
demotes is the statistics line [@quni2026stats; @quni2026anyons] and the
re-entrant calculus [@quni2026reentrant].

## 10. Limitations

The null Monte Carlo runs at $n=2000$ while the real spectra run at $n \approx 200{,}000$;
the test statistic's dependence on $n$ is weak but not zero. The H2O window is the
first 200,000 states, the low-energy region. Both real spectra are molecular, one
data class. The zeros arm uses three thousand zeros; convergence to the asymptotic
pair correlation is expected to be at the few-percent level at this height. The
GUE null is realized by a GOE ensemble, whose bulk pair correlation is identical
to GUE; the ensemble difference enters only at the arithmetic-correction order,
which this test does not probe. The geometric-channel nulls are summarized from
the register [@quni2026register]; the reader is directed there for the full
statistics.

## 11. Conclusion

The distinction-based ultrametric — the number of distinctions required to
separate two states — is a finite, prime-free hierarchy distance, an ultrametric
on any finite hierarchy, and independent of the realization chosen. It is exact
and it is verified. The empirical question it carries is statistical, not
geometric: whether physical spectra hold arithmetic information beyond universal
random-matrix statistics. The machinery to ask that question is implemented,
validated on known answers, and applied to two real molecular spectra, with a
first negative result in the pair-correlation channel. The question is now posed,
with null models and a disconfirmation criterion, for the larger spectra that
will decide it.

## References
