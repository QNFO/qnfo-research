---
title: "Adelic Quantum Arithmetic: Particles as Prime Factors"
author: "Rowan Brad Quni-Gudzinas"
affiliation: "QNFO"
ORCID: "0009-0002-4317-5604"
date: "2026-08-27"
license: "cc-by-4.0"
status: "published"
version: "1.0.0"
doi: "10.5281/zenodo.22133707"
bibliography: "references.bib"
abstract: |
  Standard quantum mechanics is written in the Archimedean completion of the rational numbers: Hilbert space over the complex numbers uses only the real place, one among all completions classified by Ostrowski's theorem. The primes are the other places, and their structure is multiplicative — unique factorization — never additive. Two published results show that the statistics binary is the multiplicative readout of a single integer lattice: the unrestricted exponent rule gives the Riemann zeta function and Bose–Einstein occupation; the squarefree rule, each prime dividing at most once, gives a ratio of two zeta values and Fermi–Dirac occupation. A third record settles the continuation: the bounded-occupation family interpolates between the two statistics but carries no exchange phase for any occupation cap; the phases realized in the standard anyon models are multiplicative characters at roots of unity, and the prime-gap structure supplies a computable distinguishing observable in the primon-gas specific heat. This paper renders the line as one readable map — the thesis, the proofs, the adjudicated continuation — and adds what the individual records do not carry: a practitioner-facing crosswalk that reads particle species as prime factors, and a separation of what is proved, what is conjectured, and what is disconfirmed. The claims are isomorphisms of mathematical structure; no physical particle is implied; and the premises end where the identification of a physical temperature at the p-adic place begins.
keywords:
  - Bose-Einstein statistics
  - Fermi-Dirac statistics
  - adelic quantum mechanics
  - p-adic places
  - unique factorization
  - squarefree integers
  - Gentile statistics
  - practitioner crosswalk
---

## 1. The Archimedean shadow

Quantum mechanics is written in one completion of the rational numbers. The complex Hilbert space of the standard formalism is built on the real numbers, and the real numbers are the Archimedean completion of $\mathbb{Q}$: they fill in the limits, the continuity, the dynamics. Ostrowski's theorem says that $\mathbb{Q}$ has other completions — one for every prime $p$, the $p$-adic fields $\mathbb{Q}_p$, where a number is measured by how divisible it is by $p$ rather than by its size. The real completion is one place among all of them.

Nothing forces the choice of that place. Macroscopic measurement is Archimedean — rulers, clocks, and detectors read real-valued outputs — so the real place is the convenient one, the anthropocentric one. The primes are the other places: non-Archimedean, tree-structured, and tied together with the real place by the product formula

$$\prod_v |x|_v = 1 ,$$

the statement that for every nonzero rational the product of all absolute values over all places is exactly one. The Archimedean magnitude and the prime valuations are not independent data; they are one constraint.

The primes are multiplicative by construction. Every positive integer factors uniquely into primes, $n = \prod_p p^{a_p}$, and this factorization — not any additive structure — is what generates the integers as a semigroup. If physics is read through the places of $\mathbb{Q}$, then whatever enters physics through the primes enters multiplicatively. Three published records make this precise for the most basic classification in quantum theory: the split between Bose–Einstein and Fermi–Dirac statistics [@quni2026stats; @quni2026anyons; @quni2026scalar].

## 2. Statistics from the product formula

The two statistics are read in [@quni2026stats] as the maximum-entropy occupations of a single lattice under two multiplicity rules. Write an integer as a product of prime powers. If every exponent is unrestricted, the Euler factor at the prime $p$ in the Dirichlet series over integers is the mode partition function of an unbounded occupation number, and the series is the Riemann zeta function,

$$\zeta(s) = \prod_p (1 - p^{-s})^{-1} .$$

If instead each prime divides at most once — the squarefree restriction, $a_p \in \{0,1\}$ — the Euler factor becomes the mode partition function of an occupation number restricted to zero or one, and the series becomes a ratio of two zeta values,

$$\frac{\zeta(s)}{\zeta(2s)} .$$

The two mode factors are exactly the Bose–Einstein and Fermi–Dirac mode partition functions, and both occupation distributions are the unique maximum-entropy distributions under their stated constraints. The golden occupation numbers follow from the canonical derivative of the mode factors. The register is explicit: these are isomorphisms of mathematical structure, and no physical particle is implied by any step.

The per-place identification was established earlier, in [@quni2026scalar]: the $p$-adic maximum-entropy distribution — the geometric distribution on the valuation — is the Bose–Einstein occupation distribution at fugacity $z = 1/p$ — inverse temperature $\ln p$ at the $p$-adic place — and the squarefree restriction is its Fermi–Dirac counterpart with occupation probability $1/(p+1)$ at the same temperature. The same record ties the exchange phase to the scalar family generated by a half-turn, a line continued from the distinction calculus in [@quni2026exchange].

What [@quni2026stats] left open was the interpolation between the two statistics. The bounded-occupation family — an occupation cap of $m$ per mode, with the Dirichlet series $\zeta(s)/\zeta((m+1)s)$ — passes through the bosonic case at unbounded $m$ and the fermionic case at $m = 1$, and it was proposed there as the arithmetic object that intermediate, anyonic statistics must contact. That correspondence is settled, computationally, in [@quni2026anyons].

## 3. The anyonic continuation, adjudicated

The bounded-occupation family is the partition function of Gentile intermediate statistics: a cap on occupation per mode, nothing more. The adjudication in [@quni2026anyons] is sharp. The family carries no exchange phase for any cap: permuting occupation labels yields only the signs $+1$ and $-1$, every observable is invariant under any inserted phase, and the canonical symmetric reading assigns the phase $+1$ for every cap — including the cap that reproduces Fermi counting, where fermions carry $-1$. The correspondence with Fermi counting is therefore a counting isomorphism, not an exchange-phase isomorphism. A cap on occupation is arithmetic; it is not a braid.

The arithmetic objects that do carry the phases realized in the standard anyon models are multiplicative characters at roots of unity: the Laughlin exchange phase at filling $1/m$ is a primitive $2m$-th root of unity, and the Fibonacci braid eigenvalues are powers of $e^{i\pi/5}$ [@quni2026anyons]. The division of labor is clean: the primes give the counting and the statistics; the roots of unity give the phases.

The same record supplies the observable that separates the arithmetic structure from a smooth continuum. The prime-gap structure of the primon gas — particles labeled by primes with energies $\ln p$ — makes its specific heat deviate from the smooth-density-of-states ideal gas at every sampled temperature, by up to roughly three quarters at low temperature, in both statistics [@quni2026anyons]. This is a computable signature, and it is the bridge to practitioners in §5.

## 4. The crosswalk: particles as prime factors

The three records [@quni2026stats; @quni2026anyons; @quni2026scalar] state their results in the language of Dirichlet series and valuation theory. The dictionary below translates each arithmetic object into the language a statistical-mechanics or quantum-engineering reader already uses. Nothing in the dictionary adds physics; it restates the published isomorphisms in adjacent terms.

| Arithmetic object | Physical / engineering reading |
|---|---|
| place / valuation | a way of measuring size |
| prime | an independent multiplicative quantum number; a species label |
| squarefreeness | Pauli exclusion: a mode is occupied at most once |
| unrestricted exponents | Bose aggregation: a mode is occupied without bound |
| product formula | the constraint linking all scales |
| adele ring | all measurement scales in one object |
| idele characters | conserved multiplicative quantum numbers |
| Möbius parity | the bookkeeping that organizes composite, intermediate statistics |
| Bruhat–Tits tree | a hierarchical, tree-structured state space |
| $p$-adic norm inequality | passive error protection: errors add without amplification |
| re-entrant mark / half-turn | the generator of the exchange phase (via [@quni2026exchange]) |

The central row is the second: a particle species label behaves like a prime factor. Species labels multiply — a state of two distinguishable subsystems carries a product of labels — and they do not add, exactly as primes multiply into integers and never add. The squarefree restriction says a prime divides at most once, and the Pauli principle says a mode is occupied at most once; the same $\{0,1\}$ constraint appears on both sides. Read this way, the Fermi–Dirac exclusion is squarefreeness, and the Bose–Einstein aggregation is the unrestricted lattice [@quni2026stats].

## 5. What a practitioner can do

Four concrete uses follow from the records, in order of increasing commitment.

**The partition recipe with a built-in signature.** Any system whose mode labels carry unique factorization — engineered spectra, qudit registers indexed by prime-like labels, synthetic lattices — admits the two readings of §2 directly: unrestricted occupation gives the zeta-function partition function, the squarefree restriction gives the ratio. The prime-gap structure then supplies a computable distinguishing observable: the specific heat deviates from the smooth-density-of-states ideal gas at every sampled temperature, by up to roughly three quarters at low temperature, in both statistics [@quni2026anyons]. An experimentalist who engineers the spectrum of a candidate "arithmetic" system gets a number to look for.

**Passive protection through the non-Archimedean triangle inequality.** The $p$-adic norm satisfies $\lVert x + y \rVert_p \le \max(\lVert x \rVert_p, \lVert y \rVert_p)$: adding two states never increases the size measure beyond the larger of the two. Read through the dictionary, the inequality reads as passive error protection: errors accumulate without amplification. The relaxation architecture of [@quni2026relaxation] turns the same ultrametric structure into a mechanism: passive topological relaxation freezes a system into a protected sector without active correction cycles, targeting the thermodynamic wall that active error correction hits at scale. The architecture of [@quni2026relaxation] is limited to abelian topological sectors — a memory, not a universal processor. Both readings point in the direction the energy benchmark of [@quni2026joules] prices: what a correct quantum answer costs in energy. A hardware architect gets a design principle — protect by geometry, correct by readout — and a metric to judge it against.

**Engineered intermediate statistics, correctly placed.** The bounded-occupation family interpolates between the two statistics, and per [@quni2026anyons] it carries no exchange phase for any cap. A platform that implements Gentile-like occupation caps is engineering a counting interpolant, not a braid. If the platform's physics involves exchange phases, those phases live at roots of unity — Laughlin-like fillings give primitive roots, Fibonacci-like braiding gives powers of $e^{i\pi/5}$ [@quni2026anyons] — and the correct arithmetic objects to model them are multiplicative characters, not occupation caps. This distinction prevents a class of design errors in anyonic platforms.

**A translation layer between communities.** The dictionary of §4 lets number-theoretic results and statistical-mechanics results be checked against each other mechanically. A theorem about zeta ratios is a statement about occupation distributions; a measurement of a specific-heat deviation is a statement about prime gaps. Each side gains the other's tooling.

## 6. Proved, conjectured, disconfirmed

The program's results separate into three classes, and the separation is the point.

**Proved.** The two statistics as maximum-entropy occupations of one lattice under two multiplicity rules [@quni2026stats]; the per-place identification at fugacity $1/p$ [@quni2026scalar]; the no-exchange-phase-for-any-cap adjudication of the bounded-occupation family [@quni2026anyons]; the roots-of-unity carriers of the anyonic phases [@quni2026anyons]; the prime-gap specific-heat deviation [@quni2026anyons]. Each carries deposited verification scripts.

**Conjectured.** The Adelic Representation Theorem — that a system realizing a sufficiently rich hierarchy of distinctions is computationally equivalent to an adelic quantum computer — remains a conjecture with no formal proof, and it is labeled as such wherever it appears. It is not load-bearing for anything in this paper.

**Disconfirmed.** Findings on record that constrain the program rather than support it: the Fenna–Matthews–Olson coupling data are anti-ultrametric (cophenetic correlation 0.426, p = 0.984); a strict-ultrametricity spectrum hypothesis for the Wheeler–DeWitt setting was falsified — no finite-dimensional energy spectrum produces strict ultrametricity; the cosmic microwave background shows no log-periodic oscillations above 0.3% amplitude; exact FMO clustering is null (p = 0.598); and a diagonal refinement in four dimensions is insufficient without a tree-structured clock spectrum. These nulls travel with the program and are cited with it. The record [@quni2026umbrella] states the falsifiable-test framework under which these findings were produced.

The map-territory discipline is stated once: the arithmetic identifications are claims about mathematical structure, and the physical labels attach at the level of statistical distributions. Where the records claim an identity of structure, they claim an identity of structure; where they propose a physical dictionary, they say so and write the falsification conditions.

## 7. Where the premises end

The argument rests on a short chain, and each link is labeled.

The given: $\mathbb{Q}$, Ostrowski's classification of places, and unique factorization — textbook mathematics. The machinery: maximum-entropy reasoning on a lattice of modes, the standard method of statistical mechanics. The proved links: the identifications of §2 and the adjudication of §3, exact and computationally verified [@quni2026stats; @quni2026anyons; @quni2026scalar]. The proposed link: attaching physical labels to the distributions — the identification of a physical temperature at the $p$-adic place, the reading of species as primes. This is where the premises end. The algebra is exact; the dictionary is proposed; and the falsification conditions are written: the dictionary fails if it requires auxiliary assumptions beyond the published isomorphisms to reach any practitioner-measurable quantity, and the specific-heat signature of §5 is a concrete place to test it.

One named import remains: the spin-statistics theorem [@pauli1940], which this line treats as the physical target to be recovered, not as something derived here.

## 8. Related work

Non-Archimedean and adelic quantum mechanics is an established program in the literature. Dragovich formulated $p$-adic and adelic quantum mechanics and the adelic harmonic oscillator, unifying ordinary and $p$-adic quantum mechanics on equal footing [@dragovich2003; @dragovich2004]. Zúñiga-Galindo and collaborators developed the modern $p$-adic Schrödinger equation and its two-slit experiment [@zuniga2023slit], the $p$-adic Dirac equation with Planck-scale Lorentz violation [@zuniga2023dirac], and $p$-adic potential-well and quantum-walk models [@zuniga2024wells]. Mathematical foundations for $p$-adic states, trace-class operators, and the symplectic and Heisenberg groups were supplied by Aniello, Mancini, Parisi and by Hu and Hu [@aniello2022; @hu2015].

The primon gas — particles labeled by primes with energies $\ln p$ — is a live subject in high-energy theory, where it appears in the quantization of near-singularity gravitational dynamics and in conformal primon gases at the end of time [@hartnoll2025; @declerck2025]. This line of work differs from those in emphasis: it does not study a $p$-adic or adelic theory as an alternative dynamics, but reads the standard statistics themselves as the multiplicative structure of the integers, with the product formula as the invariant linking the places.

Within this line of work, the Archimedean-shadow reading was developed in [@quni2026tate; @quni2026consilience; @quni2026units]; the umbrella thesis across seven domains is [@quni2026umbrella]; the exchange phase as a logical scalar of the distinction calculus is [@quni2026exchange]; and an earlier record reads the primes as places (archived without a DOI). The present record consolidates the line and adds the crosswalk of §4 and the separation of §6.

## 9. Limitations

The dictionary of §4 is proposed, not derived: everything to its left is proved, everything to its right is a translation. No claim is made that any $p$-adic place couples to measurement beyond what is on record, and the null findings of §6 bound the empirical content squarely. The paper claims no new physics; it maps, translates, and disciplines. The energy-benchmark connection of §5 is directional — the design principle and the metric are stated, but no energy saving is quantified here. The prime-gap signature is computed in [@quni2026anyons] for the ideal primon gas; its realization in an engineered system is open.

## 10. Reproducibility

Every quantitative statement asserted in this record is reproduced by the verification suite deposited alongside it: `sim-adelic-quantum-arithmetic-verification.py` (Python 3, standard library only, deterministic — no random seeds; runtime 1.77 s on a consumer laptop, sieving two million primes and two million integers). The suite runs eighteen checks, all passing: the Euler-product expansion of the zeta function against pi^2/6 (relative error 3.2e-8); the squarefree Dirichlet series against zeta(2)/zeta(4) = 15/pi^2 (relative error 2.0e-7); the squarefree density against 6/pi^2, approximately 0.607927 (absolute error 1.1e-5, inside the expected N^(-1/2) sampling bound); the Moebius inversion against 1/zeta(2) (relative error 8.5e-11); the occupation golden values 1/(p-1) and 1/(p+1) in exact rational arithmetic at fugacity 1/p for p = 2, 3, 5, 7; the Gentile cap-m Euler factors against their finite geometric sums; the bounded-occupation factor at m = 1 against the fermionic mode factor; and the roots-of-unity phase bookkeeping — the Laughlin phase at filling 1/m as a primitive 2m-th root of unity and the Fibonacci eigenvalues as tenth roots. The output file `verification-output.json` carries every check, value, expected value, and tolerance. The reference list is rendered from `references.bib`; every entry was verified against DataCite, the Zenodo records API, Crossref, or the arXiv API on 2026-08-27 (see `citation-audit.md`).
