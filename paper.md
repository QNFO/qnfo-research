---
title: "Error Correction Is a Landauer Machine: The Thermodynamic Floor of Quantum Error-Correction Overhead"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-26"
license: "CC BY 4.0"
doi: ""
status: "draft-v0.4"
---

# Error Correction Is a Landauer Machine: The Thermodynamic Floor of Quantum Error-Correction Overhead

## Abstract

Quantum error correction is priced almost exclusively in combinatorial currency: rate, distance, threshold. The physical bill — the energy paid for performing the correction itself — goes unpriced by the field's headline metrics. This paper prices it. Every cycle of active (measurement-based) error correction is an erasure engine: syndrome extraction, majority voting, and ancilla re-initialization each destroy the redundancy they read, and Landauer's principle charges at least kT·ln2 per bit erased. The consequence is a limit that is thermodynamic rather than combinatorial: correction overhead does not converge to zero as codes improve; it converges to a positive floor, whose height per logical qubit per round is (n−k)/k · kT·ln2 for an [[n,k]] code. The floor's scaling law is computed and verified across code families — linear in n for repetition codes, quadratic in distance for surface codes, and constant for constant-rate families. The same analysis transfers to classical storage, where a two-level nested (tree-structured) code is compared against flat Hamming codes of equal rate on a clustered NAND-like error channel: hierarchical decoding reduces per-round erasure count by a factor of 1.6 to 3, while the naive construction pays a residual-error penalty — an honest partial result that reframes, rather than proves, the structural-protection hypothesis. Finally, biological systems that run robust quantum processes with no correction scaffold (photosynthetic energy transfer; radical-pair magnetoreception) show that the floor is an architecture choice — structure prepays in capital energy what correction pays in operating erasures — and autonomous/dissipative correction is identified as the boundary of the claim.

**Where the premises end:** the paper imports Landauer's principle, the JPCUB metric definition, and the anatomy of standard QEC cycles as named inputs; it derives the erasure-count decomposition and the floor inequality; the biological claims are empirical citations; and the classical test results are simulation-level, not industrial measurements. The claim is deliberately bounded to active correction — it says nothing about autonomous or dissipative schemes, which escape the erasure bill.

## 1. Introduction

The cost of quantum error correction (QEC) is normally counted in qubits. A surface code of distance d uses on the order of d² physical qubits to hold one logical qubit; constant-rate quantum LDPC families reduce the multiplicative overhead but are counted the same way — in redundancy. The energy bill for performing correction is different in kind: every syndrome extraction records error information that must then be discarded, and discarding information is a physical act with a price.

That the price exists is old news. Vedral cast error correction as a Maxwell's-demon problem and applied Landauer's principle to both classical and quantum correction in 1999 [3]. Korepin and Terilla gave a thermodynamic interpretation of the quantum error-correction criterion in 2002 [4]. Landi, Oliveira, and Buksman carried out a complete thermodynamic assessment of operator-based error-correcting codes treated as Otto-cycle engines, showing that the work cost of the correction gate is directly tied to the heat injected by the error, and that the encoding/decoding work is always positive [6]. This paper does not claim novelty for the principle. It claims three things the prior work does not provide: (i) a per-family decomposition of the erasure bill — the (n−k)/k · kT·ln2 floor per logical qubit per round, computed and verified across code families; (ii) an explicit architecture-choice reading of that floor, bounded to active correction and witnessed by biological systems; and (iii) a classical, near-term, falsifiable test of the structural-protection hypothesis that requires no quantum hardware.

The motivation is the JPCUB program: joules per correct answer, counted at system level [16]. Where the JPCUB metric ranks computing platforms, this paper ranks correction architectures. Where JPCUB has been applied to platform scorecards [27, 28], this paper applies it to the correction cycle itself.

## 2. The Erasure Anatomy of a QEC Cycle

An active QEC cycle contains at least three erasure operations:

1. **Syndrome extraction.** Ancilla qubits are entangled with the data, measured, and — critically — reset for the next round. The measurement outcome (the syndrome) must be irreversibly recorded; the ancilla state must be re-initialized. Each reset erases the syndrome register.
2. **Majority voting / decoding.** The decoder maps the syndrome to a correction. In classical decoding hardware this is an irreversible computation; in the quantum register the logical correction itself may be unitary, but the bookkeeping that selects it is not.
3. **Ancilla re-initialization.** Fresh ancillae must be prepared; used ancillae must be discarded or reset. Every prepared-and-discarded ancilla is an erasure of its previous state.

Landauer's principle prices each irreversible erasure of one bit at no less than kT·ln2, where T is the temperature of the bath into which the heat is rejected [1]. Reversible operations are free; erasures are not [2]. Correction cycles are erasure-heavy by construction: they exist to convert error information into a reset state.

For an [[n,k]] stabilizer code, each round of syndrome extraction measures at least n−k independent stabilizer generators, producing n−k syndrome bits that must be reset. The per-round erasure budget is therefore at least n−k bits, and per logical qubit per round:

  E_floor(n,k,T) = (n−k)/k · kT·ln2 .    (1)

This is the claim's core arithmetic. It is a floor for measurement-based correction; nothing in this section assumes a particular decoder or platform.

## 3. The Floor: Computation and Scaling Laws

Equation (1) was evaluated in code (verification_floor.py, this deposit) at five temperatures and seven code families. Golden values: kT·ln2 = 2.871×10⁻²¹ J (300 K), 3.828×10⁻²³ J (4 K), 1.435×10⁻²⁵ J (15 mK).

| Family | n | k | (n−k)/k | E_floor at 300 K (J) | E_floor at 4 K (J) |
|---|---|---|---|---|---|
| Repetition [3,1] | 3 | 1 | 2.000 | 5.742×10⁻²¹ | 7.656×10⁻²³ |
| Repetition [7,1] | 7 | 1 | 6.000 | 1.723×10⁻²⁰ | 2.297×10⁻²² |
| Hamming [7,4] | 7 | 4 | 0.750 | 2.153×10⁻²¹ | 2.871×10⁻²³ |
| Surface code d=3 (rotated, 17q) | 17 | 1 | 16.000 | 4.594×10⁻²⁰ | 6.125×10⁻²² |
| Surface code d=21 (rotated, 881q) | 881 | 1 | 880.000 | 2.526×10⁻¹⁸ | 3.369×10⁻²⁰ |
| qLDPC [[144,12,12]] | 144 | 12 | 11.000 | 3.158×10⁻²⁰ | 4.211×10⁻²² |
| Constant-rate tree code r=1/2 | 2 | 1 | 1.000 | 2.871×10⁻²¹ | 3.828×10⁻²³ |

Three scaling laws follow, each verified numerically in the accompanying script:

1. **Repetition codes scale linearly.** For [n,1], (n−k)/k = n−1. Better repetition is linearly more expensive per logical qubit.
2. **Surface codes scale quadratically.** For the rotated surface code holding one logical qubit at distance d, n ≈ 2d²−1 and (n−k)/k ≈ 2d²−2. From d=3 to d=21 the per-logical-qubit floor grows from 16 to 880 — a 55× increase for a 7× distance gain.
3. **Constant-rate families have a constant floor.** For a family with rate r = k/n, (n−k)/k = (1−r)/r, independent of n. A rate-1/2 code pays exactly one kT·ln2 per logical qubit per round at any block length.

Two observations follow. First, the floor never reaches zero for any code with n > k: the combinatorial story ("overhead falls as codes improve") and the energy story ("the erasure bill persists per round") are both true, and Equation (1) shows they coexist — better codes move from the linear/quadratic regime to the constant-rate regime, where the floor stops falling. Second, the JPCUB ranking of families by Equation (1) differs from the rate ranking: surface codes at d=21 pay 880 kT·ln2 per logical qubit per round while a constant-rate tree code pays 1.

**The relevance caveat, stated plainly.** At 15 mK the qLDPC floor is 1.579×10⁻²⁴ J per logical qubit per round. A cryo-CMOS decoder consumes on the order of 1 pJ per decoded bit. The gap is eleven orders of magnitude. The floor is not today's cost driver; it is the asymptote that architectures approach as everything else is optimized. A paper that ignores this gap overclaims; a paper that prices the floor honestly tells engineers where the curve ends.

## 4. JPCUB Ranking of Correction Architectures

The JPCUB metric defines advantage as the ratio of total system energy consumed to produce a correct answer at a given correctness threshold, with anti-gaming rules that count everything — control electronics, reset pulses, ancilla preparation, cooling amortization — and never decode energy alone [16]. Applied to correction, the measured quantity is joules per correct logical operation:

  E_cor = E_round / (1 − p_fail_adjusted) ,   (2)

where E_round is the per-round system energy and the denominator carries the failure rate's retry amplification. Under this metric the constant-rate families dominate, surface codes at large distance are the most expensive, and the erasure count of the decoder (not just the register) enters E_round. The quantitative consequence of this ranking for fault-tolerance roadmaps is left to the practitioner section.

## 5. The Architecture Choice: Nature's Witness and the Prepaid Bill

Biological systems run robust quantum processes without correction cycles. Photosynthetic light-harvesting complexes exhibit long-lived electronic coherence that survives the thermal environment [5]; radical-pair magnetoreception depends on coherent spin dynamics in a noisy protein environment [7]. Neither system measures syndromes; neither resets ancillae. Their robustness is structural — energy landscapes, chromophore geometry, spin chemistry — rather than corrective.

The economic reading is a capital/operating split. An antenna complex is expensive infrastructure: its scaffold is metabolically maintained continuously. Active correction pays a different bill: a per-round operating cost of erasures. The crosswalk between the two communities is:

| QEC engineering | Adjacent-domain equivalent | Fidelity |
|---|---|---|
| Syndrome reset / ancilla re-init | Bit erasure; reset-to-reference | Exact |
| Correction work | Heat rejected to the bath (engine language, [6]) | Exact |
| Structural protection | Passive stability; energy landscape | Good |
| Scaffold maintenance cost | Capital depreciation / housekeeping metabolism | Metaphor, flagged |
| JPCUB (joules per correct answer) | Energy-per-corrected-bit; P/E amortization (NAND industry) | Exact for classical storage |
| Overhead (qubit ratio) | Redundancy rate (coding theory) | Exact |

The thesis this paper adds to the JPCUB program is that the floor's existence does not force the correction paradigm. Nature's witness shows the floor is a choice: pay per round for erasures, or pay once for structure. The interesting engineering question is where the crossover lies — the same crossover JPC.002 computes for platforms, specialized to correction.

## 6. The Boundary: Autonomous and Dissipative Correction

The claim is bounded to active, measurement-based correction. Autonomous correction — continuously driven stabilization, engineered dissipation, cat-qubit confinement, GKP stabilization [19, 21, 22] — does not perform discrete syndrome resets, and therefore does not pay Equation (1)'s bill in the same form. It pays instead the continuous cost of driving and dissipation. This is not a loophole against the physics; it is a different ledger entry. The paper's floor claim says nothing against autonomous schemes, and the presence of working autonomous demonstrations [19] is precisely why the claim must carry its scope statement explicitly.

## 7. The Classical Test: Flash Memory as the Falsifiable Proxy

The structural-protection hypothesis has a classical, near-term, hardware-free testbed: NAND flash. Flash controllers already pay a correction bill — LDPC/BCH decoders burn controller energy on every read, and P/E endurance is a physical budget consumed by every write. The hypothesis: a nested (tree-structured) code exploiting error clustering uses fewer erasures per round than a flat code of equal rate, and its total energy-per-corrected-bit (including endurance amortization) matches or beats the flat baseline.

**Pre-registered protocol.** Page = fixed data block; equal rate for both codes; channel = clustered error model (uniform background plus contiguous bursts); metrics = (a) per-round erasure count (Landauer-relevant energy proxy), (b) post-decode residual data-bit error rate, (c) failure-adjusted energy per corrected page. Baseline = flat Hamming; test code = two-level nested structure with hierarchical decoding.

**Simulation results (this deposit, verification_h2.py, seed 20260826, 4,000 trials per regime).** Page = 64 data bits, rate 4/7 for both codes. Flat: 16 × Hamming[7,4], full-pass decoding, 48 erasures per round. Tree: level-1 single-parity detection per 4-bit group (16 bits), level-2 bitwise-XOR reconstruction parity per two-group super-group (32 bits), correcting one flagged group per super-group; only triggered super-groups measure level-2 parity.

| Regime | Erasures flat | Erasures tree | Energy ratio | Residual bits flat | Residual bits tree |
|---|---|---|---|---|---|
| zero-error | 48.0 | 16.0 | 3.00 | 0.000 | 0.000 |
| uniform p=0.005 | 48.0 | 17.2 | 2.79 | 0.003 | 0.006 |
| uniform p=0.02 | 48.0 | 20.6 | 2.33 | 0.065 | 0.150 |
| burst c=1 L=8 | 48.0 | 21.2 | 2.27 | 1.323 | 2.124 |
| burst c=2 L=8 | 48.0 | 24.3 | 1.98 | 2.772 | 4.318 |
| heavy burst c=2 L=16 | 48.0 | 29.3 | 1.64 | 12.795 | 17.401 |

**Reading the result honestly.** The hierarchical structure delivers its mechanism: the erasure bill adapts to the error regime (16 erasures when clean, 29 under heavy bursts), a 1.64–3.0× reduction against the flat decoder's constant 48. But this naive construction loses on correctness in every non-trivial regime — the single-parity level-1 detector misses even-count errors, and one reconstruction per super-group is too little redundancy for burst regimes. The hypothesis card is therefore revised, not confirmed: the adaptive-erasure mechanism is demonstrated; the energy-per-corrected-bit advantage of tree codes over LDPC baselines on real NAND workloads remains open, and requires constructions with stronger per-group detection (two parity bits per group) or true product/tree LDPC families. The protocol above is the test those constructions should run. A null on the full industrial test would not touch the floor claim — Equation (1) is independent of whether tree codes win — which is why the two hypotheses are carried as separate cards.

## 8. What This Paper Does Not Claim

- It does not claim novelty for Landauer's principle in correction (Vedral [3], Korepin–Terilla [4], Landi et al. [6] precede it).
- It does not challenge threshold theorems or constant-rate quantum LDPC results [14]. The floor is about energy, not rate; both stories are true.
- It does not assert that the floor is the dominant cost of today's machines — the eleven-order gap says the opposite.
- It does not produce a new industrial-strength code construction. The tree code here is a toy whose failure modes are part of the result.
- It does not claim autonomous correction pays the same bill; it names autonomous schemes as the boundary.
- It does not rehearse ontology. Whether the continuum is real is a different program's question.

**Future research topics opened by this work** are collected in the companion note `artifacts/future-research-topics.md` in this deposit. The principal ones: (i) the industrial flash test with real tree/LDPC constructions; (ii) the energy dimension of the QEC-Darwinism tradeoff [24]; (iii) the capital/operating crossover curve for structural protection (extending JPC.002's crossover to correction); (iv) a p-adic entropy treatment of the non-Archimedean erasure hierarchy; (v) the epistemological reading — "reality is a syndrome; we probe it, never read it" — as the map-territory structure of stabilizer measurement.

## Verification Appendix

All numbers in §3 and §7 are computed by scripts in `artifacts/verification/` (Python 3, stdlib only): `verification_floor.py` (golden values, floor table, six structural checks) and `verification_h2.py` (seeded Monte Carlo, six structural checks). Reproduce with `python verification_floor.py` and `python verification_h2.py` from that directory; outputs are `verification_floor.json` and `h2_results.json`, with runs recorded in `run_out.txt` and `h2_run_out.txt`. Seed: 20260826. Environment: CPython 3.x, no external dependencies.

## References

[1] R. Landauer, "Irreversibility and Heat Generation in the Computing Process," IBM J. Res. Dev. 5, 183 (1961).
[2] C. H. Bennett, "The Thermodynamics of Computation — a Review," Int. J. Theor. Phys. 21, 905 (1982).
[3] V. Vedral, "Landauer's erasure, error correction and entanglement," arXiv:quant-ph/9903049 (1999).
[4] V. Korepin, J. Terilla, "Thermodynamic interpretation of quantum error correcting criterion," arXiv:quant-ph/0202054 (2002).
[5] G. S. Engel et al., "Evidence for wavelike energy transfer through quantum coherence in photosynthetic systems," Nature 446, 782 (2007).
[6] G. T. Landi, A. L. Fonseca de Oliveira, E. Buksman, "Thermodynamic analysis of quantum error correcting engines," arXiv:1911.06354 (2019).
[7] P. J. Hore, H. Mouritsen, "The Radical-Pair Mechanism of Magnetoreception," Annu. Rev. Biophys. 45, 299 (2016).
[8] D. Bedingham, O. Maroney, "The thermodynamic cost of quantum operations," arXiv:1604.03749 (2016).
[9] P. Taranto et al., "Landauer vs. Nernst: What is the True Cost of Cooling a Quantum System?" arXiv:2106.05151 (2021).
[10] Y.-H. Ma, J.-F. Chen, C. P. Sun, H. Dong, "Minimal Energy Cost to Initialize a Quantum Bit with Tolerable Error," arXiv:2112.07311 (2021).
[11] P. Chattopadhyay, A. Misra, T. Pandit, G. Paul, "Landauer Principle and Thermodynamics of Computation," arXiv:2506.10876 (2025).
[12] N. Ishida, Y. Hasegawa, "Thermodynamic Recycling of Algorithmic Failure Branches: Quantum-Computer Demonstration with Quantum Error Correction," arXiv:2601.07522 (2026).
[13] M. A. Nielsen, I. L. Chuang, Quantum Computation and Quantum Information, 10th ann. ed., ch. 10 (2010).
[14] P. Panteleev, G. Kalachev, "Asymptotically good quantum and locally testable classical LDPC codes," STOC 2022.
[15] C. Gidney, M. Ekerå, "How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits," Quantum 5, 433 (2021).
[16] R. B. Quni-Gudzinas, "The Joules-per-Solution Metric: Definition, Measurement Protocol, and Anti-Gaming Provisions," QNFO.JPC.002 (2026).
[17] R. B. Quni-Gudzinas, "Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation," 10.5281/zenodo.17955898 (2025).
[18] R. B. Quni-Gudzinas, "Thermodynamic and Quantum Constraints on Scalable Quantum Computing," 10.5281/zenodo.17937531 (2025).
[19] R. B. Quni-Gudzinas, "Autonomous Dissipative Quantum Processing," QNFO (2025).
[20] R. B. Quni-Gudzinas, "Thermodynamics of Structural Persistence (Topological Memory)," QNFO (2025).
[21] R. B. Quni-Gudzinas, "Resonant Kerr-Cancellation Dynamics in Dissipative Bosonic Stabilization," QNFO (2025).
[22] R. B. Quni-Gudzinas, "Stabilization of Gottesman-Kitaev-Preskill States," QNFO (2025).
[23] R. B. Quni-Gudzinas, "The Qubit Delusion" series (2026).
[24] R. B. Quni-Gudzinas, "Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces," 10.5281/zenodo.21964674 (2026).
[25] R. B. Quni-Gudzinas, "Passive Error Resilience Through Ultrametric Geometry: A Proposal for p-Adic Quantum Metrology," QNFO (2025).
[26] R. B. Quni-Gudzinas, "The Physics of Computation: Fundamental Limits and the Honest Boundaries of Post-Classical Computing," QNFO (2025).
[27] R. B. Quni-Gudzinas, "JPCUB Competitive Landscape v2.0," QNFO (2026).
[28] R. B. Quni-Gudzinas, "The Qudit Advantage: System-Level Joules-per-Solution Comparison," QNFO (2026).
[29] R. B. Quni-Gudzinas, "The Universal Ignorance Audit," 10.5281/zenodo.21901984 (2026) — method used in the planning phase of this work.
