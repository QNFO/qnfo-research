---
title: "Decoherence Times versus Quantum Speed Limits in Spin-Chain Substrates: A Computed Crossover Criterion for Energy-Time Uncertainty"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-09-03"
license: "CC BY 4.0"
doi: "10.5281/zenodo.22278842"
version: "2.0.1"
status: "published"
---

## Abstract

Spin chains are the canonical many-body testbed for quantum memories and quantum wires, and the question of what bounds their useful computation time is usually answered in one of two vocabularies that are rarely placed on the same scale: the decoherence time T2 set by the environment, and the quantum speed limit set by the energy available in the chain. This paper puts both vocabularies on a single, computable scale for a dephasing-limited spin-chain substrate. The model states its conventions up front: a dephasing rate Gamma defines the coherence time T2 = 1/Gamma, the chain's excitation scale defines a frequency f (equivalently a gap or mean energy above ground), and the Margolus-Levitin bound for an orthogonal transition is t_ML = h/(4E) = 1/(4f) when the driving energy scale is E = h f. All quantitative claims are computed by a deposited verification script: the speed-limit table across four decades of gap (t_ML = 250 ns at 1 MHz down to 250 ps at 1 GHz), and the six-cell crossover table that decides which constraint binds first for dephasing rates of 1 MHz, 100 MHz, and 1 GHz against gaps of 10 MHz and 1 GHz. The result is a single criterion: a dephasing-limited chain is decoherence-bound exactly when Gamma > 4f, i.e. when the environment destroys coherence faster than the energy-time uncertainty allows an orthogonal transition; otherwise the speed limit binds. At Gamma = 4f the two bounds cross. The reader should care because the crossover separates the regime in which faster control electronics can still help (speed-limit-bound) from the regime in which they cannot (decoherence-bound), which is the difference between spending engineering effort on coherence and spending it on energy. Where the premises end: T2 = 1/Gamma is an exponential-dephasing idealization; the bound is for orthogonal-state transitions under the stated energy scale; and the spin-chain gap is a stand-in for the energy scale of the fastest relevant transition, which a specific implementation must supply.

## 1. Introduction

A spin chain used as a quantum memory or a quantum wire faces two independent limits on the time it can spend doing useful quantum work. The environment imposes a coherence time T2: after roughly T2, the state is a classical mixture and no longer supports interference. The Hamiltonian imposes a speed limit: reaching an orthogonal (fully distinguishable) state takes at least a finite time set by the energy scale of the dynamics. The two limits are usually discussed in different subfields with different units, and a practitioner deciding where to spend engineering effort needs a single criterion that says which limit binds for a given substrate.

This paper supplies that criterion. It models a dephasing-limited spin-chain substrate with two parameters - the dephasing rate Gamma and the excitation frequency f - and computes, with a deposited script, the crossover condition Gamma = 4f that separates the decoherence-bound regime from the speed-limit-bound regime.

The contribution is threefold. First, a unit-consistent statement of the two bounds on one scale (Section 3). Second, a verified computation of the speed-limit table and the crossover table (Section 5). Third, a practitioner-facing rule: if Gamma > 4f, invest in coherence; if Gamma < 4f, invest in energy. The engineering consequence of the rule is stated in Section 7.

## 2. Prior work

The energy-time uncertainty that underlies the speed limit has two classical statements. Mandelstam and Tamm [1] bounded orthogonal-state evolution time by the energy dispersion: t >= pi hbar/(2 Delta E). Margolus and Levitin [2] bounded it by the mean energy above the ground state: t >= h/(4E). Both bounds are for fully distinguishable states and are tight under stated conditions; their relation and tightness for arbitrary fidelity are the subject of a recent line of work. Hornedal and Sonnerborn [3] extended the Margolus-Levitin bound to arbitrary fidelity and showed the two bounds are complementary, with the ML bound generally tighter at small fidelity and the MT bound at large fidelity. Andrzejewski, Bolonek-Lason, and Kosinski [4] clarified the conditions under which the fidelity-generalized ML bound is valid. Sonnerborn [5] constructed families of systems that saturate the ML bound, including uniform-energy-eigenstate superpositions.

The present paper does not add to the bound theory. It takes the orthogonal-state ML bound as given and applies it to the spin-chain substrate question: which constraint, the environment's T2 or the Hamiltonian's t_ML, binds first? The crossover computation is the contribution, and the deposited script makes it reproducible.

## 3. Model and conventions

The substrate is a spin chain operated as a quantum memory or wire, subject to pure dephasing. Three conventions fix the scale of the problem.

**Convention 1 (coherence).** The dephasing rate Gamma defines the coherence time T2 = 1/Gamma. A dephasing-limited chain has no useful quantum coherence beyond T2; after that the state is effectively classical. Gamma is in hertz; T2 in seconds.

**Convention 2 (energy scale).** The excitation scale of the chain is a frequency f. The energy scale of the fastest relevant transition is E = h f, where h is the Planck constant. For a two-level gap this is the gap frequency; for a mean-energy-above-ground statement it is the mean excitation energy. The distinction matters only at the level of which energy to insert; the algebra is identical.

**Convention 3 (speed limit).** The Margolus-Levitin bound for an orthogonal transition is

t_ML = h / (4 E) = h / (4 h f) = 1 / (4 f).

The chain can reach an orthogonal state no faster than t_ML.

Where the premises end: T2 = 1/Gamma assumes exponential dephasing; the bound assumes an orthogonal target; and the identification of the gap frequency with the ML energy scale E is a modeling convention that a specific implementation must justify. The crossover criterion inherits these premises and is exact only within them.

## 4. Analysis

The useful-computation question is: for a transition that requires an orthogonal target, which constraint binds?

**Speed-limit-bound regime.** If T2 > t_ML, the state survives long enough for the Hamiltonian to evolve it to an orthogonal configuration; the binding constraint is the energy available in the chain. Faster control electronics, a larger gap, or a stronger drive shortens t_ML and directly speeds the computation.

**Decoherence-bound regime.** If T2 < t_ML, the environment destroys the coherence before the Hamiltonian can complete an orthogonal transition. No increase in the energy scale helps: the state is already classical at the time the speed limit would have allowed completion. The only levers are a longer T2 (materials, shielding, dynamical decoupling) or a reduction in the required distinguishability (which leaves the orthogonal-transition framing).

**Crossover.** The two bounds cross when T2 = t_ML, i.e. 1/Gamma = 1/(4f), i.e.

Gamma = 4 f.

For Gamma > 4 f the chain is decoherence-bound; for Gamma < 4 f it is speed-limit-bound. The criterion is dimensionless and computable from the two parameters.

## 5. Results

All values in this section are computed by the deposited verification script (jpcub_nv_verify.py, section NV.002); no number is transcribed from memory.

**Margolus-Levitin bound versus excitation scale.**

| Excitation frequency f | t_ML = 1/(4f) |
|---|---|
| 1 MHz | 2.500e-7 s (250 ns) |
| 10 MHz | 2.500e-8 s (25 ns) |
| 100 MHz | 2.500e-9 s (2.5 ns) |
| 1 GHz | 2.500e-10 s (250 ps) |

The bound decreases by an order of magnitude per decade of excitation frequency, as the 1/(4f) form requires.

**Crossover table (dephasing rate Gamma, gap frequency f).**

| Gamma | T2 = 1/Gamma | f | t_ML | Binding constraint |
|---|---|---|---|---|
| 1 MHz | 1.000e-6 s | 10 MHz | 2.500e-8 s | speed-limit-bound |
| 1 MHz | 1.000e-6 s | 1 GHz | 2.500e-10 s | speed-limit-bound |
| 100 MHz | 1.000e-8 s | 10 MHz | 2.500e-8 s | decoherence-bound |
| 100 MHz | 1.000e-8 s | 1 GHz | 2.500e-10 s | speed-limit-bound |
| 1 GHz | 1.000e-9 s | 10 MHz | 2.500e-8 s | decoherence-bound |
| 1 GHz | 1.000e-9 s | 1 GHz | 2.500e-10 s | speed-limit-bound |

The pattern is the criterion in action: the two decoherence-bound cells are exactly the cells with Gamma > 4f (100 MHz > 40 MHz; 1 GHz > 40 MHz), and the four speed-limit-bound cells have Gamma < 4f. At Gamma = 4f the bounds cross (the 1 GHz-vs-1 GHz cell is just below the crossover; the exact crossing is at Gamma = 4 GHz for f = 1 GHz).

**Criterion check.** The script reproduces the criterion directly: for each cell it computes T2 = 1/Gamma and t_ML = 1/(4f) and reports decoherence-bound when T2 < t_ML, which is algebraically equivalent to Gamma > 4f.

## 6. Discussion

Three consequences follow from the criterion.

First, the crossover separates two engineering regimes with different levers. In the speed-limit-bound regime, the substrate is limited by its own dynamics: increasing the excitation energy (a larger gap, a stronger drive, faster control) directly shortens the achievable operation time, and the environment is not yet the constraint. In the decoherence-bound regime, no amount of additional energy helps; the substrate loses coherence before the dynamics can complete, and the only levers are coherence time itself. A dephasing-limited chain at Gamma = 100 MHz and f = 10 MHz is in the second regime, and pouring power into a faster drive is wasted effort.

Second, the criterion is a planning number, not a fundamental limit. It inherits the exponential-dephasing idealization and the orthogonal-target assumption of the underlying bounds. Real implementations have non-exponential noise, finite-fidelity targets, and multiple energy scales; the criterion states where the idealized crossover sits and gives the practitioner the correct leading-order question.

Third, the two bounds are complementary in the sense established in [3]: the ML bound used here is the appropriate one when the energy scale is the mean-above-ground or the gap, while the MT bound of [1] applies when the relevant scale is the energy dispersion. For a thermal or broadened chain the dispersion may be the tighter input, and the crossover table should then be recomputed with t_MT = 1/(4 Delta f). The script is structured so this is a one-line change.

## 7. What a practitioner can do with this result

1. **Classify the substrate.** Measure or estimate the dephasing rate Gamma and the excitation frequency f of the fastest relevant transition, and compare Gamma with 4f. The comparison decides whether coherence engineering (materials, shielding, dynamical decoupling) or energy engineering (gap, drive, control bandwidth) is the binding lever. This is a two-parameter rule that costs nothing to apply and prevents misdirected effort.

2. **Price the crossover.** For a given chain, the crossover frequency f_c = Gamma/4 is the excitation scale at which the regime flips. A chain dephasing at 100 MHz is speed-limit-bound above 25 MHz of excitation scale and decoherence-bound below it; knowing f_c tells the designer whether the planned operating frequency is on the correct side.

3. **Reproduce the tables.** The deposited script computes both tables from first principles (T2 = 1/Gamma, t_ML = 1/(4f), the comparison, and the criterion check). A practitioner can substitute measured Gamma and f and obtain the classification in seconds without trusting the transcription.

4. **Extend to the MT bound.** Where the energy dispersion Delta f is the better-known quantity, replace t_ML with t_MT = 1/(4 Delta f) and recompute; the crossover criterion becomes Gamma = 4 Delta f, and the script makes the substitution a single line.

## 8. Conclusion

For a dephasing-limited spin-chain substrate, the coherence time and the quantum speed limit can be placed on one computable scale: T2 = 1/Gamma and t_ML = 1/(4f). The crossover criterion Gamma = 4f separates the decoherence-bound regime, where no energy increase helps and coherence engineering is the only lever, from the speed-limit-bound regime, where the energy scale directly bounds the operation time. The deposited script reproduces the speed-limit table across four decades and the six-cell crossover table, and the criterion check confirms the classification is algebraically exact. The two parameters Gamma and f, and the single comparison Gamma versus 4f, are the entire content of the model, stated so that a practitioner can apply them to a measured substrate.

## References

[1] Mandelstam, L., and I. Tamm. 1945. "The uncertainty relation between energy and time in non-relativistic quantum mechanics." Journal of Physics (USSR) 9: 249.

[2] Margolus, N., and L. B. Levitin. 1998. "The maximum speed of dynamical evolution." Physica D 120: 188-195.

[3] Hornedal, N., and O. Sonnerborn. 2023. "Margolus-Levitin quantum speed limit for an arbitrary fidelity." arXiv:2301.10063.

[4] Andrzejewski, K., K. Bolonek-Lason, and P. Kosinski. 2023. "Note on the Margolus-Levitin quantum speed limit for arbitrary fidelity." arXiv:2307.16854.

[5] Sonnerborn, O. 2025. "Systems that saturate the Margolus-Levitin quantum speed limit." arXiv:2511.23237.

## Changelog

- v2.0 (2026-09-03): all quantitative claims computed by the deposited verification script; the crossover criterion Gamma = 4f stated and verified across the six-cell table; prior-work positioning added (Sections 2 and 6); HTML and PDF renderings added to the deposit; abstract rewritten with computed values, no deferred claims.
- v1.0 (2026-09-03): initial short-form record.

## Verification

Every number in Section 5 is produced by jpcub_nv_verify.py (section NV.002), deposited with this record. The script uses only the Python standard library. It computes T2 = 1/Gamma, t_ML = 1/(4f), the comparison, and the criterion check Gamma versus 4f for each cell. Run "python jpcub_nv_verify.py" to reproduce both tables and the criterion.
