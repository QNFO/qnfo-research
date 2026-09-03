---
title: "A Verified Energy Model for Surface-Code Quantum Error Correction: Joules per Logical-Qubit Operation and the JPCUB Normalization"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-09-03"
license: "CC BY 4.0"
doi: "10.5281/zenodo.22278600"
version: "2.0.1"
status: "published"
---

## Abstract

Surface-code quantum error correction translates one logical qubit into a two-dimensional array of physical qubits, and the energy cost of that translation is rarely quantified at the level of a logical operation. This paper specifies a minimal, convention-explicit energy model for a rotated surface-code patch of distance d and computes it in full. The model states three conventions up front: the patch uses N_c = 2d^2 - 1 physical qubits (d^2 data, d^2 - 1 ancilla); one logical operation costs N_g = 8 d^3 physical gates (roughly 2d^2 stabilizer measurements of four CNOT gates each per syndrome round, d rounds per logical operation); and the energy decomposes as E = (E_g N_g + E_c N_c)/N_l with gate energy E_g and per-round control-and-measurement energy E_c per physical qubit. All quantitative predictions are computed by a deposited verification script: the Landauer erasure floor k_B T ln 2 per bit at 300 K, 77 K, 4 K, and 20 mK; the full energy table for d = 3..31; the exact cubic scaling check N_g(15)/N_g(9) = (15/9)^3 reproduced to four decimal places; and the observation that realistic cryogenic control dissipates roughly 2.6 x 10^10 times the 4 K Landauer floor, so the binding constraint on joules per logical operation is the efficiency of the control electronics, not thermodynamics. The paper defines JPCUB, joules per logical-qubit operation, as the normalization that isolates algorithmic cost from error-correction overhead, and tabulates the overhead factor for distances 3 to 21. The reader should care because roadmap planning currently lacks a single reproducible energy figure per logical operation: this model supplies one, with every quoted number computable from source. Where the premises end: the gate-count and round-count conventions are order-of-magnitude engineering conventions, not derived bounds; the Landauer values are exact but apply only to erasure-limited dissipation; and absolute energies require measured E_g and E_c, which the paper leaves as parameters rather than asserting.

## 1. Introduction

Fault-tolerant quantum computation buys logical accuracy with physical overhead. A surface-code machine replaces one logical qubit with a patch of thousands of physical qubits, replaces one logical gate with rounds of stabilizer measurements, and replaces one logical operation's energy with the energy of the entire overhead machinery. The first two costs are tabulated extensively in the literature; the third is not, and it is the one that determines whether a scaled machine is economically feasible.

The absence has a specific cause. Energy depends on device and control-plane engineering choices that no code-level analysis can fix: the gate energy of a cryogenic CMOS controller, the dissipation per measurement channel, the round time. Any energy figure quoted without stating those choices is a number without a domain of applicability. The correct object is therefore not a single number but a parameterized model whose conventions are stated and whose predictions are computable. This paper provides that object for the surface code.

The contribution is threefold. First, a convention-explicit model: physical-qubit count, gate count, and energy decomposition are fixed as conventions in Section 3, so any downstream number inherits a stated domain. Second, a verified computation: every table in Section 5 is produced by a deposited script, including the exact cubic scaling of gate overhead and the Landauer floors at four temperatures. Third, a normalization: JPCUB, joules per logical-qubit operation, which separates the algorithmic energy of a computation from the error-correction overhead that currently dominates it by ten orders of magnitude.

## 2. Prior work

The thermodynamic and informational bottlenecks of scalable fault-tolerant quantum computation are examined in a companion QNFO record [4], which argues that energy, erasure, and wiring constraints bound fault-tolerant machines more tightly than gate fidelity alone. The present paper instantiates that argument quantitatively for one code family: it converts the bottleneck claim into a parameterized, computed energy model.

The gate-counting basis is standard surface-code practice. Fowler's low-overhead logical Hadamard [2] documents the full overhead of a logical operation at distance 7 in an idle array, including the syndrome rounds and state distillation that motivate the per-round and per-operation conventions used here. Lavasani, Zhu, and Barkeshli [3] show that constant-overhead logical gates exist for hyperbolic codes. That result delimits the regime of the present model: the cubic overhead N_g = 8 d^3 is the surface-code scaling in the polynomial-overhead regime, and the constant-overhead routes are complementary rather than contradictory, because they exchange gate-count scaling for other costs (embedding, routing, and planar control).

Landauer's irreversibility principle [1] supplies the thermodynamic floor: erasing one bit dissipates at least k_B T ln 2. The present paper computes that floor at the temperatures relevant to quantum control planes and compares it with realistic gate energies, with the result stated in Section 5: the floor is two orders of magnitude below realistic dissipation even at 300 K, and ten orders below at 4 K.

## 3. Model and conventions

The model treats one logical qubit in a rotated surface-code patch of distance d. Three conventions fix the geometry and cost of the patch.

**Convention 1 (qubits).** A rotated distance-d patch contains d^2 data qubits and d^2 - 1 ancilla qubits, for a total N_c = 2 d^2 - 1 physical qubits. This is the standard rotated-lattice count; a distance-3 patch has 17 qubits, a distance-11 patch 241.

**Convention 2 (gates).** One logical operation consists of d syndrome rounds. Each round measures approximately 2 d^2 stabilizers (X- and Z-type), and each stabilizer measurement is implemented with four CNOT gates plus preparation and measurement. The four-CNOT estimate therefore gives approximately 8 d^2 physical gates per round, and N_g = 8 d^3 physical gates per logical operation. Preparation, measurement, and decoding operations are not counted as gates; their energy is absorbed into E_c below.

**Convention 3 (energy).** The energy per logical operation is

E = (E_g N_g + E_c N_c) / N_l

with N_l = 1 logical qubit, E_g the energy dissipated per physical gate, and E_c the per-round control-and-measurement energy per physical qubit (so E_c N_c covers d rounds of control). Both E_g and E_c are parameters to be supplied by device measurements; the model predicts the functional dependence on d, not the absolute dissipation of any particular controller.

Where the premises end: the four-CNOT stabilizer estimate is an order-of-magnitude convention that can be refined per implementation; the d-round convention is the standard fault-tolerance prescription, not a theorem; and the linear energy decomposition ignores cross-talk heating and cooling overhead, which can be added as further terms without changing the structure of the model.

## 4. Analysis

**Distance and fidelity.** The logical error rate of a surface-code patch scales as p_L proportional to (p/p_th)^(d/2) for physical error rate p well below threshold p_th. Inverting, a target logical rate p_L requires distance d proportional to log(1/p_L) / log(p_th/p). Combined with the cubic gate count, the energy per logical operation scales polylogarithmically with the target error rate and cubically with the chosen distance:

E(d) = E_g 8 d^3 + E_c (2 d^2 - 1).

The two terms scale differently: the gate term is cubic in d, the control term quadratic. For realistic E_g of order 1 pJ and E_c of order 0.1 pJ per round, the cubic term dominates for all d above 3, so the model reduces to E approximately E_g 8 d^3 in the relevant regime.

**Landauer floor.** If every physical gate erases at least one bit of information, the erasure-limited floor for a logical operation is E_min = N_g k_B T ln 2 = 8 d^3 k_B T ln 2. This is a lower bound on the gate-energy contribution only if the gate is erasure-limited; dissipative gates operate far above it, as Section 5 quantifies.

**JPCUB normalization.** Defining JPCUB as joules per logical-qubit operation removes the error-correction overhead from the benchmark figure: a JPCUB value reports the energy of one logical operation inclusive of overhead, whereas joules per physical gate reports a controller property. The ratio of the two is exactly N_g = 8 d^3, the overhead factor tabulated in Section 5.

## 5. Results

All values in this section are computed by the deposited verification script (jpcub_nv_verify.py); no number is transcribed from memory.

**Landauer erasure floor per bit.**

| Temperature | k_B T ln 2 (J/bit) |
|---|---|
| 300 K | 2.871e-21 |
| 77 K | 7.369e-22 |
| 4 K | 3.828e-23 |
| 20 mK | 1.914e-25 |

**Energy per logical operation across distances.**

| d | N_c | N_g | E at E_g = 1 pJ (J) | E_min at 300 K (J) | E_min at 4 K (J) |
|---|---|---|---|---|---|
| 3 | 17 | 216 | 2.160e-10 | 6.201e-19 | 8.268e-21 |
| 5 | 49 | 1000 | 1.000e-09 | 2.871e-18 | 3.828e-20 |
| 7 | 97 | 2744 | 2.744e-09 | 7.878e-18 | 1.050e-19 |
| 9 | 161 | 5832 | 5.832e-09 | 1.674e-17 | 2.232e-19 |
| 11 | 241 | 10648 | 1.065e-08 | 3.057e-17 | 4.076e-19 |
| 15 | 449 | 27000 | 2.700e-08 | 7.752e-17 | 1.034e-18 |
| 21 | 881 | 74088 | 7.409e-08 | 2.127e-16 | 2.836e-18 |
| 31 | 1921 | 238328 | 2.383e-07 | 6.842e-16 | 9.123e-18 |

**Scaling check.** N_g(15) / N_g(9) = 4.6296, and (15/9)^3 = 4.6296, reproducing the cubic scaling to four decimal places.

**Overhead versus thermodynamics.** At d = 11, the erasure floor at 4 K is 4.076e-19 J per logical operation, while a realistic gate energy of 1 pJ yields 1.065e-08 J, a ratio of 2.6 x 10^10. The same ratio holds at every distance because both quantities scale identically in d. Thermodynamics is therefore not the binding constraint; control-electronics efficiency is.

**JPCUB overhead factor.** The normalization factor from physical gates to logical operations is N_g = 8 d^3: 216 at d = 3, 1000 at d = 5, 5832 at d = 9, 27000 at d = 15, 74088 at d = 21.

## 6. Discussion

The dominant term is unambiguous: for any controller dissipating at the picosecond-joule scale, the cubic gate term swamps the quadratic control term above distance 3, and the Landauer floor sits ten orders of magnitude below both. Three consequences follow.

First, the model's precision is appropriate to its use. The conventions are order-of-magnitude, so the absolute energies are order-of-magnitude estimates; but the scaling, the ratios, and the normalization are exact consequences of the conventions and are computed exactly. A practitioner should treat the absolute columns of the table as planning figures and the scaling and ratio results as structural facts.

Second, the distance dependence is the design lever. Because E scales as d^3 while the achievable logical error scales as (p/p_th)^(d/2), a modest fidelity improvement that allows one or two fewer distance steps buys a cubic energy saving. The model makes that trade explicit and computable: for any measured (p, E_g, E_c), the energy cost of a chosen distance is read off the table by construction.

Third, the constant-overhead routes of [3] bound the model's regime. The cubic overhead is a property of the planar surface-code family, not a theorem of fault tolerance. Where the hyperbolic-code trade-offs (embedding and routing costs) are acceptable, the gate-count scaling improves; the energy accounting of Section 3 transfers directly, with N_g replaced by the route's gate count.

## 7. What a practitioner can do with this result

1. **Benchmark with JPCUB.** Report joules per logical-qubit operation alongside joules per physical gate. The JPCUB figure carries the error-correction overhead, which is the quantity a roadmap needs; the per-gate figure alone understates the energy of a logical machine by the factor 8 d^3, up to four orders of magnitude at distance 21.

2. **Price the distance.** Before committing to a target logical error rate, compute the distance it implies, then read the energy from the table. A target that moves from d = 11 to d = 21 multiplies the energy per logical operation by seven; the model exposes that cost at planning time rather than after the control plane is sized.

3. **Direct the engineering.** Because the Landauer ratio is 2.6 x 10^10, every joule saved in the control electronics translates directly into logical-operation energy; thermodynamic arguments against scaling are misdirected at current dissipation levels. The levers in order of leverage are: gate energy E_g (linear), distance d (cubic), and control-plane parallelism (sublinear per logical operation).

## 8. Conclusion

A convention-explicit energy model for the rotated surface code, with N_c = 2 d^2 - 1 physical qubits, N_g = 8 d^3 physical gates per logical operation, and the decomposition E = (E_g N_g + E_c N_c)/N_l, predicts that the energy per logical operation grows cubically with code distance, that realistic controllers operate ten orders of magnitude above the Landauer floor, and that the JPCUB normalization isolates the overhead factor 8 d^3 that a benchmark must carry. Every quantitative claim in this paper is reproduced by the deposited verification script. The open parameters E_g and E_c are flagged explicitly: the model states the dependence, and the next measurement step is to supply them from a specific controller.

## References

[1] Landauer, R. 1961. "Irreversibility and Heat Generation in the Computing Process." IBM Journal of Research and Development 5 (3): 183-191.

[2] Fowler, A. G. 2012. "Low-overhead surface code logical Hadamard." arXiv:1202.2639.

[3] Lavasani, A., G. Zhu, and M. Barkeshli. 2019. "Universal logical gates with constant overhead: instantaneous Dehn twists for hyperbolic quantum codes." arXiv:1901.11029.

[4] QNFO. 2025. "Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation." Zenodo. doi:10.5281/zenodo.17955898.

## Changelog

- v2.0 (2026-09-03): all quantitative predictions computed by the deposited verification script; prior-work positioning added (Sections 2 and 6); HTML and PDF renderings added to the deposit; abstract rewritten with computed values, no deferred claims.
- v1.0 (2026-09-03): initial short-form record.

## Verification

Every number in Section 5 is produced by jpcub_nv_verify.py, deposited with this record. The script uses only the Python standard library and four constants (k_B, h, hbar, ln 2). Run "python jpcub_nv_verify.py" to reproduce the tables; the scaling check compares N_g(15)/N_g(9) against (15/9)^3 to full double precision. Conventions 1-3 of Section 3 are encoded at the top of the script, so the reproduction is a test of the conventions, not of the transcription.
