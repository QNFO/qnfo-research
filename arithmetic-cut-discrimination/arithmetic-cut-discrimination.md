---
title: "Discriminating the Arithmetic Cut: Matched-Level-Density Null Models for the Primon-Gas Specific Heat and Spectral Correlations"
author: "Rowan Brad Quni-Gudzinas"
affiliation: "QNFO"
orcid: "0009-0002-4317-5604"
date: "2026-08-29"
license: "CC BY 4.0"
status: "preprint"
version: "1.0"
wbs: "QNFO.RES.030"
slug: "arithmetic-cut-discrimination"
abstract: |
  The arithmetic-statistics program reads the two exchange statistics of
  identical particles as two multiplicity rules on one integer lattice, and
  its published observable is the specific heat of the primon gas: a
  computable deviation from the smooth ideal gas at every sampled temperature.
  The program's own red team raised the decisive objection: any irregular
  spectrum with the same level density might reproduce that deviation, making
  the observable level-density content rather than arithmetic content. This
  paper adjudicates the objection computationally. It constructs three
  matched-level-density non-arithmetic null ensembles, realizes each under the
  same statistics as the cut, and computes the specific heat and the unfolded
  two-point statistics of the cut against them. The specific heat separates
  from the fixed-count nulls at every tested cutoff (z-scores from 5 to 100)
  and from the Poisson-type nulls beyond a computable minimum cutoff; a
  focused test of the small-spacing exclusion separates at 34 sigma. The
  full two-point curve does not separate under a uniform distance measure at
  any tested cutoff, which locates the arithmetic information in the
  small-spacing hard core. The paper also adjudicates two published numbers
  in the program: the reported Dyson number-variance pair mixes two window
  lengths and uses an asymptotic formula outside its validity range, and the
  Bost-Connes specific heat at inverse temperature 1.06 is a finite-cutoff
  crossover whose approach to the pole is power-law in the cutoff. The
  premises end where a physical temperature is identified at a p-adic place;
  nothing in this paper crosses that boundary.
---

## 1. The objection this paper answers

A line of work reads the two exchange statistics of identical particles as
the two multiplicity rules of one integer lattice. Unrestricted exponents give
the Riemann zeta function and Bose-Einstein occupation; the squarefree
restriction gives a ratio of zeta values and Fermi-Dirac occupation
[@quni2026stats; @quni2026adelic], and a
bounded-occupation family interpolates between them without carrying an
exchange phase [@quni2026anyons]. The published observable of that
identification is thermodynamic: the specific heat of the primon gas deviates
from a smooth-density ideal gas at every sampled temperature, by up to roughly
three quarters at low temperature [@quni2026anyons].

That observable was never tested against the null it must defeat. An
experimentalist who engineers a spectrum of prime-logarithmic mode energies
and measures a specific-heat deviation has no way, from the published record
alone, to tell the deviation of an arithmetic spectrum from the deviation of
any irregular spectrum with the same level density. This paper builds that
test. It constructs the matched-density non-arithmetic null ensembles, runs
the arithmetic cut against them under the same statistics, and reports the
separation thresholds in the cutoff and the observable.

## 2. The arithmetic cut and its thermodynamics

Fix a cutoff $P$ and let the modes be the primes $p \le P$ with energies
$\varepsilon_p = \ln p$ and inverse temperature $\beta$. Three statistics
are realized by three occupation rules, each with an exact closed form for
the specific heat:

Bose (unrestricted): $C_V^{(B)} = \beta^2 \sum_p (\ln p)^2 p^{-\beta}
(1-p^{-\beta})^{-2}$.

Fermi (squarefree): $C_V^{(F)} = \beta^2 \sum_p (\ln p)^2 p^{-\beta}
(1+p^{-\beta})^{-2}$.

Maxwell-Boltzmann: $C_V^{(MB)} = \beta^2 \sum_p (\ln p)^2 p^{-\beta}$, whose
logarithmic partition function is the prime zeta function $P(\beta) =
\sum_p p^{-\beta}$. The primon gas and its arithmetic-gas variants are
thirty-year-old objects of the statistical theory of numbers
[@julia1990statistical; @bakas1991curiosities], and the bounded-occupation
family studied here extends them in the program's register
[@quni2026adelic].

Two limits are exact. At high temperature every Bose mode contributes one
unit of specific heat (equipartition over $\pi(P)$ modes) while the Fermi and
Boltzmann modes decay to zero. At low temperature all three statistics
collapse to $\beta^2 (\ln 2)^2 2^{-\beta}$, the freeze-out of the lowest mode.
All of this is verified in the deposited scripts, which reproduce the
equipartition limit to $10^{-6}$ and the collapse exactly.

The ideal-gas baseline used by the published claim is $\pi(P)$ units of
specific heat, flat in temperature. The relative deviation
$D(\beta) = 1 - C_V^{(B)}(\beta)/\pi(P)$ is monotone: it reaches three
quarters at $\beta \approx 0.42$ (about 2.4 ideal-gas temperatures) and
approaches 100 percent at low temperature. The phrase "up to roughly three
quarters at low temperature" is therefore window-dependent: the deviation
exceeds three quarters for all lower temperatures and tends to full
freeze-out, so the figure in the published abstract is correct only for a
specific, previously unstated temperature window.

## 3. The matched-density null ensembles

Three null families share the arithmetic cut's level count $N = \pi(P)$ and
range $[\ln 2, \ln P]$ but carry no prime structure:

- **Smooth log-spaced.** Levels evenly spaced in log-energy. Deterministic;
  the fluctuation-free comparator.
- **Fixed-count random.** $N$ independent uniform points on the log range,
  sorted. Matched count and range, irregular, no arithmetic structure.
- **Poisson-on-log-scale.** A Poisson number of points with the same mean
  density. Matched mean density with count fluctuations.

Fairness is enforced at two levels. First, every null is realized under the
same statistics as the cut: the null levels play the role of the modes in the
closed forms of Section 2. Second, the two-point observables use each
family's own smooth staircase (the exact log-prime count for the cut, the
linear-in-log count for the nulls), the same binning, the same window, and
matched sample counts. Without these two rules, a spacing artifact is
mistaken for arithmetic content; with them, the comparison isolates the
arithmetic structure itself.

## 4. Validation of the machinery

Before any discrimination result, the estimators must recover known answers.
The deposited suite validates:

- **The GUE pair correlation** from Monte Carlo samples of the Hermitian
  Gaussian ensemble, matched to the analytic bulk curve to within 0.07 mean
  absolute deviation, and the estimator passes exact sanity checks (a uniform
  grid gives number variance exactly zero; an exact Poisson sample gives
  $10.63 \pm 0.1$ against the expected 10 at window 10).
- **Montgomery-Odlyzko.** The first 3000 Riemann zeros, unfolded by the
  Riemann-von Mangoldt smooth count, match the GUE pair correlation to 0.11
  mean absolute deviation with the expected repulsion at small spacing
  [@montgomery1973pair; @odlyzko1987distribution].
- **The twin-gap hard core.** The minimum unfolded prime spacing is exactly
  $2/\ln P$ (the minimum prime gap is 2; beyond the hard core the primes are
  Poisson-like [@gallagher1976distribution]): measured $0.206128$ against the
  predicted $0.206099$ at $P = 2^{14}$, with zero spacings below the
  threshold.
- **A positive control.** A planted log-periodic modulation of the level
  density is recovered by the spectral form factor at the planted frequency
  to $8 \times 10^{-5}$ relative error.

## 5. Discrimination results

For each cutoff $P \in \{2^8, 2^{12}, 2^{16}\}$, each statistics, and each
null family, the cut's specific-heat curve and two-point curve are compared
to the null family's own self-distance distribution (30 realizations), and
separation is reported in units of its standard deviation.

**Specific heat.** The cut separates at or above two sigma in every statistics
against the fixed-count nulls from the smallest tested cutoff onward
(z-scores from 4.9 at $P = 2^8$ to 102 at $P = 2^{16}$). Against the
Poisson-type nulls the separation is not significant at the smallest cutoff
(0.28 for Bose), becomes significant at $P = 2^{12}$ (4.1), and grows to 63
at $P = 2^{16}$. The minimum cutoff for a two-sigma specific-heat verdict is
therefore $P \approx 2^8$ against fixed-count nulls and $P \approx 2^{12}$
against Poisson-type nulls, for all three statistics. The disconfirmation
criterion this machine serves is pre-registered for the program's estimation
record [@quni2026hd3; @quni2026ump014].

**Two-point statistics.** Under a uniform distance measure over the unfolded
pair-correlation curve, the cut does not separate from the nulls at any
tested cutoff (z-scores near minus one). This is expected physics: beyond
the hard core the primes are asymptotically Poisson
[@gallagher1976distribution], so the full curve carries little beyond the
level density. The arithmetic information is concentrated in the
small-spacing exclusion: the fraction of nearest-neighbor spacings below
$2/\ln P$ is exactly zero for the cut and $0.1656 \pm 0.0049$ for the
fixed-count nulls, a separation of 34 sigma at $P = 2^{16}$. Any two-point
verdict must report both numbers; the uniform measure alone would understate
the channel.

The three null families overlap at the smallest cutoff (their shared mean
density forces it) and separate from each other as the cutoff grows — a
consistency check, not a claim.

## 6. Two published numbers adjudicated

**The Dyson number-variance pair.** The program's estimation paper reports
"a Dyson number variance 1.044 against the predicted 0.525" [@quni2026ump014].
Both numbers are values of the Dyson asymptotic formula
$(1/\pi^2)[\ln(2\pi L) + 1 + \gamma - \pi^2/8]$ at different window lengths:
1.0449 at $L = 3400$ and 0.5246 at $L = 20$. The sentence compares two
different windows. Independently of that mismatch, the asymptotic formula
itself is not accurate at these lengths: the exact two-point reduction
$\Sigma^2(L) = L - 2\int_0^L (L-s)(\sin \pi s / \pi s)^2 ds$
[@dyson1962statistical; @mehta2004random] gives 0.65 at $L = 20$ against the
asymptotic 0.52, a 24 percent underestimate, and the GUE Monte Carlo samples
match the exact reduction within 8-13 percent. At the low height of the first
3000 zeros the measured values exceed the exact reduction by 1.2-2.8 times,
growing with the window; that residual is the known height-dependent
unfolding error of the Riemann-von Mangoldt count [@odlyzko1987distribution].

**The Bost-Connes specific heat.** The estimation paper reports a
Bost-Connes critical specific heat of 316.3 at $\beta = 1.06$ against a
predicted pole amplitude 312.1 [@quni2026ump014]. The pole amplitude is
recovered exactly by the deposited computation, but the truncated-product
specific heat at $\beta = 1.06$ is 33.1 at $P = 10^4$, 47.5 at $10^5$, and
62.7 at $10^6$: the tail $\sum_{p > P} p^{-\beta}$ decays only as
$P^{-(\beta-1)}$, which is about 0.44 even at $P = 10^6$, so the published
316.3 cannot come from a direct truncated-product computation at any feasible
cutoff [@bost1995hecke]. The honest observable is the finite-cutoff
crossover table reported here; the pole language is reserved for the infinite
limit. Ensemble averaging over Hamiltonians, as in the randomized Riemann
gas, is known to wash out the pole entirely [@duenas2014thermodynamics], so
no such averaging is applied to the thermodynamic observable.

## 7. What a practitioner can do

A spectroscopist or metrologist considering an engineered prime-logarithmic
spectrum gets a discrimination machine rather than a conclusion. The
deposited scripts accept any level sequence and a cutoff, generate the three
matched-density null families under the chosen statistics, and return: the
separation z-scores per observable, the minimum cutoff at which a two-sigma
specific-heat verdict is available, and the small-spacing exclusion test.
The same machine converts the published specific-heat deviation into a
threshold table usable as an engineering specification: a qudit register or
optical lattice with $P \approx 2^{12}$ or more modes is sufficient to
discriminate the arithmetic cut from matched non-arithmetic spectra in the
thermodynamic channel, and the hard-core test decides the two-point channel.
The protocol is blind to the origin of the spectrum, so it applies to any
candidate arithmetic system.

## 8. Limitations

The cutoffs tested run to $P = 2^{16}$ (6542 modes); larger cutoffs and noise
models (temperature stability, resolution) are extensions, not claims. The
molecular data applications discussed elsewhere in the program require
desymmetrization by species and per-species unfolding before any of these
tests apply [@quni2026ump014]; the machine here is validated on the cut and on
controlled ensembles. The low-height number-variance residual of Section 6 is
quantified empirically and attributed to the known unfolding error; its exact
decomposition is left open. The finite-p-base primon gas has an independent
kernel-theoretic treatment [@franchini2024padic], and the conformal primon
gas of the Belinski-Khalatnikov-Lifshitz setting generalizes the partition
functions studied here [@hartnoll2025conformal]; neither changes the null
construction of this paper. The statistical-class claims are about
mathematical structure: no physical realization is asserted, and the premises
end where a physical temperature is identified at a p-adic place.

## 9. Reproducibility

Every quantitative statement in this paper is reproduced by a deposited,
deterministic script (seed 20260829, Python 3.12.10, NumPy 2.4.4, SciPy
1.17.1), with the outputs in the record's verification directory: the
estimator suite (pair correlation, number variance against the exact
two-point reduction, form factor, GUE samples, planted control) and the
discrimination suite (thermodynamics, null ensembles, separation tables,
hard-core test). The Riemann zeros are computed by a vectorized
Riemann-Siegel method. The exact-theory integral is evaluated numerically at
each reported window length.

## References
