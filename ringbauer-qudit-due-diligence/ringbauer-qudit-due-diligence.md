---
title: "Trapped-Ion Qudit Quantum Computing: Due-Diligence Assessment of the Ringbauer Program"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-10"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: "10.5281/zenodo.21879122"
status: "published"
keywords:
  - qudit
  - trapped ions
  - quantum computing
  - light-shift gate
  - quantum simulation
  - entanglement
  - lattice gauge theory
  - due diligence
abstract: >
  This note documents a due-diligence assessment of the trapped-ion qudit quantum
  computing program led by Martin Ringbauer at the University of Innsbruck. Three
  publications anchor the assessment: the universal qudit processor demonstration
  (2022), the native qudit entanglement gate based on a generalized light-shift
  mechanism (2023), and a lattice gauge theory simulation with ion qudits (2024).
  All bibliographic metadata, author lists, DOIs, and experimental figures cited
  here were verified against live Crossref records and the published article body.
  The note records the measured light-shift gate fidelities by dimension, the
  quadratic scaling of gate error with qudit dimension, and the relevance of this
  empirical curve to the dimensional-advantage crossover parameter in qudit
  benchmarking.
---

## 1 Purpose and Scope

This note records a structured due-diligence assessment of the trapped-ion qudit
quantum computing research program centered at the University of Innsbruck and
associated with Martin Ringbauer. The assessment was conducted against the
following primary sources, each verified live during the assessment session:

| Source | Identifier | Verification |
|:-------|:-----------|:-------------|
| Universal qudit processor (2022) | DOI `10.1038/s41567-022-01658-0` | Crossref + arXiv API |
| Native qudit entanglement gate (2023) | DOI `10.1038/s41467-023-37375-2` | Crossref + full article body |
| Lattice gauge theory simulation (2024) | DOI `10.1103/PRXQuantum.5.040309` | Crossref (title + author list) |

The scope is limited to (a) verifying the bibliographic record, (b) extracting the
experimental gate-performance data, and (c) assessing the relevance of that data to
qudit benchmarking questions. It is not a review of the full qudit literature.

## 2 Bibliographic Record

### 2.1 Universal Qudit Processor (2022)

- **Title:** A universal qudit quantum processor with trapped ions
- **Authors:** Martin Ringbauer, Michael Meth, Lukas Postler, Roman Stricker,
  Rainer Blatt, Philipp Schindler, Thomas Monz
- **Venue:** Nature Physics, volume 18, article 1053 (2022)
- **DOI:** `10.1038/s41567-022-01658-0`
- **arXiv:** `2109.06903` (submitted 2021-09-14)

The work demonstrates a universal qudit quantum processor with a local Hilbert
space dimension of up to 7, using calcium-40 ions in a surface Paul trap. The
authors report performance comparable to qubit-based processors while enabling
native simulation of high-dimensional quantum systems and more efficient
implementation of qubit-based algorithms. [established — abstract, arXiv API]

### 2.2 Native Qudit Entanglement Gate (2023)

- **Title:** Native qudit entanglement in a trapped ion quantum processor
- **Authors:** Pavel Hrmo, Benjamin Wilhelm, Lukas Gerster, Martin W. van Mourik,
  Marcus Huber, Rainer Blatt, Philipp Schindler, Thomas Monz, Martin Ringbauer
  (Hrmo and Wilhelm contributed equally)
- **Venue:** Nature Communications, volume 14, article 2242 (2023)
- **DOI:** `10.1038/s41467-023-37375-2`
- **Funding:** ERC Starting Grant QUDITS (101039522); ERC Consolidator Grant
  Cocoquest (101043705); EU H2020 MSCA 840450; EU Quantum Flagship AQTION
  (820495) and MILLENION; FWF SFB BeyondC (F7109); FWF START (Y879-N27);
  FFG 872766; US Army Research Office W911NF-21-1-0007 and W911NF-16-1-0070;
  ODNI/IARPA. [established — acknowledgements section of the article body]

### 2.3 Lattice Gauge Theory Simulation (2024)

- **Title:** Digital Quantum Simulation of a (1+1)D SU(2) Lattice Gauge Theory
  with Ion Qudits
- **Authors:** Giuseppe Calajó, Giuseppe Magnifico, Claire Edmunds, Martin
  Ringbauer, Simone Montangero, Pietro Silvi
- **Venue:** PRX Quantum, volume 5, article 040309 (2024)
- **DOI:** `10.1103/PRXQuantum.5.040309`

The 2024 work is a digital quantum simulation of a (1+1)-dimensional SU(2)
lattice gauge theory using ion qudits. It is an original simulation study, not a
review article. This classification is recorded explicitly because the work is
occasionally miscited as a review of the qudit field. [established — Crossref
title and author-list verification]

## 3 Experimental Gate Data

### 3.1 Encoding and Gate Mechanism

The qudit encoding uses the calcium-40 ion: the $|0\rangle$ state is the
$S_{1/2}$, $m_j = -1/2$ ground level, and the states $|i\rangle$ with
$i \in \{1, 2, 3, 4\}$ are Zeeman sub-levels of the $D_{5/2}$ manifold. Coherent
operations between sub-levels use 729 nm laser light; 401 nm light generates the
light shift for the state-dependent force. [established — article body]

The entangling gate is a generalized light-shift (LS) gate. The gate action is
symmetric on all excited qudit states, which implies the same gate mechanism can
be used irrespective of qudit dimension, and that the calibration overhead does
not increase with dimension. The composite gate is constructed from $d$
applications of the light-shift pulse $U_{\mathrm{LS}}(t_g)$ interleaved with
cyclic permutation operators $X_d$:

$$G = (X_d \, U_{\mathrm{LS}}(t_g))^d$$

Up to a global phase, the gate acts as:

$$G(\theta): |jj\rangle \to |jj\rangle, \qquad |jk\rangle \to e^{i\theta}|jk\rangle \text{ if } j \neq k$$

This action directly generates genuine qudit entanglement, as opposed to
embedding qubit-level entanglement in a larger Hilbert space. [established —
article body]

### 3.2 Measured Fidelities

The gate fidelity was extracted from exponential decay fits over repeated gate
applications (up to 9 applications between state preparation and reversed
preparation). The measured state fidelities for dimensions $d = 2$ through
$d = 5$ are:

| Dimension $d$ | Measured fidelity |
|:--------------|:------------------|
| 2 | $99.6(1)\%$ |
| 3 | $98.7(2)\%$ |
| 4 | $97.0(3)\%$ |
| 5 | $93.7(3)\%$ |

[established — article body, Figure 4 and main text]

The measured gate performance degrades quadratically with dimension. The paper's
numeric error model reproduces the data with good agreement and attributes the
dominant errors at higher dimension to Rabi frequency noise and slow frequency
noise causing dephasing of local operations; at $d = 2$ the fidelity is limited
by motional coherence time and gate-laser frequency noise. [established — article
body]

### 3.3 Entanglement Properties

The entanglement of the states generated by a single gate application was
evaluated using the Schmidt number, concurrence, and entanglement of formation.
For all dimensions tested, the Schmidt number is maximal (equal to $d$), which
certifies genuine qudit entanglement up to $d = 5$. For $d > 2$, the concurrence
significantly exceeds the maximal possible value for any qubit state.
[established — article body]

## 4 Relevance to Qudit Benchmarking

The dimensional-advantage crossover parameter $d^{*}$ is the minimum qudit
dimension at which the encoding-density benefit of a qudit (which carries
$\log_2 d$ bits per physical system) overcomes the per-gate fidelity penalty.
The measured fidelity staircase above provides an empirical anchor for this
parameter: the per-gate error grows approximately quadratically in $d$ while the
encoding density grows only logarithmically. At the demonstrated operating point
($d = 3$ with $98.7\%$ gate fidelity), the encoding-density gain is $\log_2 3
\approx 1.58$ bits per system, which offsets the reduced per-gate fidelity
relative to qubits only if the algorithmic depth is correspondingly reduced or
the encoding overhead is otherwise exploited. The 2024 lattice gauge theory
simulation is a concrete demonstration of the reduced circuit-depth argument:
qudit encoding directly compresses the simulation register for a non-abelian
gauge theory.

No quantitative claim about a specific crossover value is made in this note; the
purpose of Section 4 is to record the empirical fidelity curve as a benchmark
input. [my conjecture — the framing of $d^{*}$ as a benchmark input]

## 5 Verification Statement

All bibliographic metadata (titles, author lists, DOIs, venues, volumes) and all
experimental figures (fidelities, Schmidt number, gate mechanism, funding
acknowledgements) were verified during the assessment session against at least
one live source: Crossref API, arXiv API, or the full published article body.
No citation in this note is drawn from unverified memory of the literature.

## 6 Limitations

- The assessment covers only the three primary sources listed in Section 1.
- The PRX Quantum (2024) record was verified via Crossref metadata (title and
  author list) but the article body was not read in full during this assessment.
- The fidelity extraction methodology is summarized from the article; the
  numeric error model is cited but not independently recomputed here.
- This note does not review competing qudit platforms (photonic, superconducting,
  neutral-atom) or the broader qudit error-correction literature.
