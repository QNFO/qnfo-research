---
title: "The Landauer Floor of Cryogenic Quantum Control: Computed Energy Bounds and the JPCUB Normalization"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-09-03"
license: "CC BY 4.0"
doi: "10.5281/zenodo.22279728"
version: "2.0.1"
status: "published"
---

## Abstract

Cryogenic quantum control electronics dissipate energy many orders of magnitude above the thermodynamic minimum implied by Landauer's principle, and the gap matters for the joules-per-compute economics of fault-tolerant machines. This paper computes the Landauer floor for a rotated surface-code control plane and compares it with the realistic dissipation of cryo-CMOS electronics. The model states its conventions up front: erasing one bit costs at least k_B T ln 2; one logical operation of a distance-d surface-code patch requires N_g = 8 d^3 physical gates (the counting convention of a companion record); and a realistic gate energy is taken to be of order 1 pJ, which is between ten and eleven orders of magnitude above the 4 K Landauer floor. All quantitative claims are computed by a deposited verification script: the floor k_B T ln 2 per bit at 300 K (2.871e-21 J), 77 K (7.369e-22 J), 4 K (3.828e-23 J), and 20 mK (1.914e-25 J); the per-logical-operation floor at distance 7 (1.050e-19 J at 4 K) and distance 11 (4.076e-19 J at 4 K); and the ratio of realistic gate dissipation to the 4 K floor, 2.6 x 10^10 at every distance, because both quantities scale identically in d. The central consequence is that thermodynamics is not the binding constraint on cryogenic control: the floor is so far below realistic dissipation that no plausible improvement in thermodynamic efficiency moves the joules-per-logical-operation figure; the binding constraint is the efficiency of the control electronics themselves. The paper defines the JPCUB normalization - joules per logical-qubit operation - as the benchmark unit that carries the overhead, and reports the overhead factor 8 d^3 for the working distances. The reader should care because roadmap cost models that cite the Landauer bound as a floor for quantum control are off by ten orders of magnitude in the wrong direction: the floor is real but irrelevant at current dissipation levels, and the useful planning number is the gap between realistic gate energy and the floor, not the floor itself. Where the premises end: the 1 pJ gate energy is an order-of-magnitude engineering convention, not a measured value; the gate count inherits the rotated-surface-code convention; and Landauer's bound applies to erasure-limited dissipation, which real gates exceed by many orders of magnitude.

## 1. Introduction

Every claim that quantum computing will be energy-efficient at scale must eventually confront the control plane: the classical electronics that generate, route, and measure the signals that operate the quantum processors. For superconducting and spin qubits, that control plane operates at cryogenic temperatures, and its dissipation is a standing question for scaled machines. Two numbers frame the discussion: the thermodynamic minimum set by Landauer's principle, and the actual dissipation of cryo-CMOS electronics. The two are rarely placed on the same scale, and when they are, the gap is usually stated qualitatively.

This paper states the gap quantitatively and computes it. The Landauer floor for a surface-code control plane is computed at four temperatures, the per-logical-operation floor is computed at two working distances, and the ratio to a realistic gate energy is computed exactly. The result is that the floor sits ten orders of magnitude below realistic dissipation, and the engineering implication is that thermodynamic efficiency is not the lever.

The contribution is threefold: a unit-consistent statement of the Landauer floor for a surface-code control plane (Section 3); a verified computation of the floor, the per-operation floor, and the ratio (Section 5); and a benchmark normalization - JPCUB, joules per logical-qubit operation - that carries the error-correction overhead in a single figure (Sections 4 and 7).

## 2. Prior work

Landauer's principle [1] states that erasing one bit of information dissipates at least k_B T ln 2. It is the standard thermodynamic floor for any irreversible computation, and it is the floor adopted here.

The gate-counting basis for the surface-code overhead is the rotated-lattice convention used in [2], which documents the full overhead of a logical operation including syndrome rounds. The companion QNFO record on thermodynamic bottlenecks of fault-tolerant computation [4] argues that energy, erasure, and wiring constrain scaled machines more tightly than gate fidelity; the present paper computes the energy side of that argument for one control plane. Lavasani, Zhu, and Barkeshli [3] provide the constant-overhead counterpoint: for hyperbolic codes the gate-count scaling improves, which changes the prefactor but not the structure of the floor-vs-dissipation comparison made here.

Cryo-CMOS control electronics are an active engineering field whose per-gate dissipation is device- and process-dependent. This paper does not cite a specific measurement; it adopts an order-of-magnitude gate energy of 1 pJ as an explicit convention and computes the consequences, leaving the substitution of a measured value to the practitioner.

## 3. Model and conventions

The model computes the thermodynamic floor of a cryogenic surface-code control plane. Three conventions fix the scale.

**Convention 1 (Landauer floor).** Erasing one bit of information dissipates at least

E_land(T) = k_B T ln 2.

The floor is per erased bit, per gate, and depends only on temperature. Its values at the four temperatures of interest are computed in Section 5.

**Convention 2 (gate count).** A distance-d rotated surface-code patch performs N_g = 8 d^3 physical gates per logical operation, following the counting convention of the companion energy model: roughly 2 d^2 stabilizer measurements of four CNOT gates per syndrome round, and d rounds per logical operation. The floor for one logical operation is therefore

E_min(d, T) = N_g k_B T ln 2 = 8 d^3 k_B T ln 2.

**Convention 3 (realistic gate energy).** A realistic cryogenic gate energy is taken to be E_g = 1 pJ, an order-of-magnitude engineering convention for cryo-CMOS control electronics. The ratio

R = E_g / E_land(T)

quantifies how far real dissipation sits above the thermodynamic floor. The convention is explicit so that a measured gate energy can be substituted without changing the structure of the model.

Where the premises end: the gate count inherits the rotated-surface-code convention and is an order-of-magnitude engineering figure; the 1 pJ gate energy is a stated assumption, not a measurement; and the Landauer bound applies to erasure-limited dissipation, which real control electronics exceed by orders of magnitude - exactly the gap this paper quantifies.

## 4. Analysis

The analysis has three steps.

**The floor.** E_land(T) = k_B T ln 2 decreases linearly with temperature. Moving the control plane from room temperature to 4 K reduces the floor by a factor of 75; to 20 mK by another factor of 200. The floor is the only part of the problem that thermodynamics fixes.

**The ratio.** Because E_min(d, T) and the realistic per-operation energy E_g N_g both scale identically with d (both proportional to N_g = 8 d^3), the ratio R = E_g / E_land(T) is independent of distance. It is a property of the control-electronics efficiency and the operating temperature alone. This is the structural fact that makes the comparison clean: whatever the distance, the realistic dissipation sits R times above the floor.

**The normalization.** Defining JPCUB as joules per logical-qubit operation, E_JPCUB = E_g N_g = E_g 8 d^3, removes the error-correction overhead from the benchmark figure: the per-logical-operation energy carries the overhead, the per-gate energy does not, and the ratio of the two is exactly N_g = 8 d^3. A roadmap figure stated in JPCUB therefore contains the overhead factor that a per-gate figure hides.

## 5. Results

All values in this section are computed by the deposited verification script (jpcub_nv_verify.py, section NV.003); no number is transcribed from memory.

**Landauer floor per erased bit.**

| Temperature | k_B T ln 2 (J/bit) |
|---|---|
| 300 K | 2.871e-21 |
| 77 K | 7.369e-22 |
| 4 K | 3.828e-23 |
| 20 mK | 1.914e-25 |

**Per-logical-operation floor and the ratio at realistic gate energy.**

| d | N_g | E_min at 4 K (J) | E at E_g = 1 pJ (J) | Ratio E_g/E_land(4 K) |
|---|---|---|---|---|
| 7 | 2744 | 1.050e-19 | 2.744e-09 | 2.6e+10 |
| 11 | 10648 | 4.076e-19 | 1.065e-08 | 2.6e+10 |

**Ratio invariance.** The ratio is 2.6 x 10^10 at both distances, confirming the structural claim of Section 4: the gap between realistic dissipation and the Landauer floor is independent of code distance because both quantities scale as N_g. At 300 K the ratio is 3.5 x 10^8; at 4 K it is 2.6 x 10^10; at 20 mK it would be 5.2 x 10^12 if the electronics operated at that temperature.

**JPCUB overhead factor.** The normalization factor from physical gates to logical operations is N_g = 8 d^3: 216 at d = 3, 1000 at d = 5, 5832 at d = 9, 27000 at d = 15, 74088 at d = 21.

## 6. Discussion

Three consequences follow.

First, the Landauer floor is not a useful planning bound for cryogenic control at current dissipation levels. The floor at 4 K is 3.828e-23 J per bit; a realistic gate dissipates 1 pJ, which is 2.6 x 10^10 times larger. Thermodynamics is not the binding constraint, and arguments that the Landauer bound will limit quantum control are premature by ten orders of magnitude. The useful planning number is the ratio R, which measures the efficiency gap of the control electronics.

Second, the ratio is a control-electronics property, not a code property. Because it is independent of distance, improving the code (better fidelity, smaller d) does not close the gap to the floor; only improving the control electronics does. The design levers are therefore separated cleanly: code improvements move the per-logical-operation energy through the cubic gate count, while control-electronics improvements move the prefactor E_g, and the two should be budgeted separately.

Third, the JPCUB normalization is the correct benchmark unit because it carries the overhead. A per-gate figure understates the energy of a logical machine by the factor 8 d^3, which is four orders of magnitude at distance 21. Reporting joules per logical-qubit operation makes the overhead explicit and the comparison across codes meaningful.

## 7. What a practitioner can do with this result

1. **Benchmark in JPCUB.** Report joules per logical-qubit operation, not joules per physical gate. The JPCUB figure carries the 8 d^3 overhead; the per-gate figure hides it. This is a reporting change with a four-order-of-magnitude effect on the stated energy of a logical machine at large distance.

2. **Ignore the Landauer floor as a design target.** The gap of 2.6 x 10^10 at 4 K means thermodynamic efficiency is not the lever for cryogenic control. Direct engineering effort at the control electronics' actual dissipation per gate (the prefactor E_g), which is where the ten orders of magnitude live, not at recovering the last fraction toward the floor.

3. **Price the code-distance lever.** Because per-logical-operation energy scales as d^3, a fidelity improvement that reduces the required distance by one step buys a cubic energy saving. The floor-vs-dissipation ratio is unchanged by the code; the energy per logical operation is what changes.

4. **Substitute measured values.** The 1 pJ convention is explicit. A measured per-gate energy from a specific cryo-CMOS process replaces E_g and the tables recompute in one line (the script encodes the substitution).

## 8. Conclusion

The Landauer floor of a cryogenic surface-code control plane is real, computable, and irrelevant at current dissipation levels. The floor per bit at 4 K is 3.828e-23 J; a realistic gate energy of order 1 pJ sits 2.6 x 10^10 times above it at every code distance. The ratio is a control-electronics property, independent of the code, and the binding constraint on joules per logical operation is the efficiency of the control electronics, not thermodynamics. The JPCUB normalization - joules per logical-qubit operation - carries the 8 d^3 overhead that a per-gate benchmark hides, and the deposited script reproduces every number in this paper.

## References

[1] Landauer, R. 1961. "Irreversibility and Heat Generation in the Computing Process." IBM Journal of Research and Development 5 (3): 183-191.

[2] Fowler, A. G. 2012. "Low-overhead surface code logical Hadamard." arXiv:1202.2639.

[3] Lavasani, A., G. Zhu, and M. Barkeshli. 2019. "Universal logical gates with constant overhead: instantaneous Dehn twists for hyperbolic quantum codes." arXiv:1901.11029.

[4] QNFO. 2025. "Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation." Zenodo. doi:10.5281/zenodo.17955898.

## Changelog

- v2.0 (2026-09-03): all quantitative claims computed by the deposited verification script; the ratio invariance (2.6 x 10^10 at every distance) is derived and verified; prior-work positioning added (Sections 2 and 6); HTML and PDF renderings added to the deposit; abstract rewritten with computed values, no deferred claims.
- v1.0 (2026-09-03): initial short-form record.

## Verification

Every number in Section 5 is produced by jpcub_nv_verify.py (section NV.003), deposited with this record. The script uses only the Python standard library and computes the Landauer floor at four temperatures, the per-logical-operation floor at d = 7 and d = 11, and the ratio E_g/E_land(4 K) with the 1 pJ convention, confirming the ratio is independent of distance. Run "python jpcub_nv_verify.py" to reproduce the tables.
