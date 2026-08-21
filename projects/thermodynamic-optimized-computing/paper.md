---
title: "What Does a Correct Quantum Answer Cost? Thermodynamic Optimization and the Choice Between Correcting Qubits and Protecting Them"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-21"
subtitle: "A platform scorecard and a protection-correction crossover"
abstract: >
  The quantum-computing roadmap is measured in qubit counts, gate fidelities, and
  logical error rates. None of these quantities answers the question an engineering
  or investment decision actually needs: what does a correct answer cost, in energy,
  end to end? This paper proposes ranking candidate platforms by energy per correct
  solution and uses that criterion to examine the field's central architectural
  choice -- correcting fragile qubits with active error correction, or protecting
  qubits in hardware. We compile published platform parameters, calibrate a
  correction-overhead model on a measured below-threshold surface-code memory, and
  compute the crossover between the two strategies as a function of protection gap,
  temperature, and decoder efficiency. The result is a trade-off surface, not a
  slogan: hardware protection dominates only where the protection gap exceeds the
  thermal scale by a large factor; active correction is robust wherever it has been
  demonstrated; and the decisive unknown is the control-electronics overhead common
  to both strategies. Predictions are stated in advance, and all computations are
  deposited with the paper.
---

## 1. The question the roadmap does not answer

Quantum computing is the only major computing technology whose progress is reported in units that do not include energy. Processor roadmaps report qubit counts, two-qubit gate fidelities, and logical error rates; a buyer cannot read off any of them what a finished computation will cost in joules, because the correction overhead, the cooling plant, and the control electronics are counted separately, if at all. Classical computing learned decades ago that energy per operation is the constraint that selects architectures. The same question, asked of quantum platforms, is the subject of this paper: **what does a correct quantum answer cost, end to end?**

A correct answer is the right object, not a bare operation. A computation that fails and must be rerun has cost its full energy budget for nothing. The natural figure of merit is therefore the energy spent per completed, correct solution of a fixed benchmark task. This quantity was formalized elsewhere as the joules-per-solution criterion, together with a measurement protocol [@jpcub2025]. The present paper does not re-derive that criterion; it applies it to the one question the field has not yet answered with numbers: which protection strategy — and which platform — is cheapest.

## 2. Two strategies, one physics

Classical silicon needs no active error correction. A bit is carried collectively by thousands to millions of electrons; transistors restore and amplify; a few errant charges change nothing. Quantum information enjoys none of these conveniences. An unknown qubit state cannot be copied (the no-cloning theorem), cannot be amplified without being measured, and decays continuously rather than by discrete flips. Some protection is therefore mandatory; the only question is where it lives.

**Active correction** puts the protection in software and circuit overhead: a logical qubit is spread over many physical qubits, syndromes are measured continuously, and a decoder reconstructs what the hardware lost. The strategy has the decisive virtue that it has been demonstrated: a 101-qubit distance-7 surface-code memory now operates below threshold, suppresses its logical error per cycle to $0.143\%$ with a measured suppression factor of $\Lambda = 2.14$ per two units of code distance, and outperforms its best physical qubit's lifetime by a factor of $2.4$ [@willow2024]. The strategy has a corresponding cost: the overhead factor in qubits (and in the classical electronics that run the decoder) multiplies the thermodynamic cost of every logical operation. The classical lineage of thermodynamic computing — from Landauer's principle through reversible and generalized-reversible machines — analyzed exactly this trade for classical logic, where the overhead question is simpler because bits can be copied [@vitanyi2005; @frank2018]; separate analyses have extended the same accounting to fault-tolerant quantum architectures [@bottlenecks2025].

**Hardware protection** puts the protection in the material: a qubit stored in a topologically ordered system, or more generally in a system with an energy gap $\Delta$ separating the computational subspace from its errors, suppresses local errors by a factor that scales as $\exp(-\Delta / k_B T)$ — exponential in the ratio of the protection gap to the thermal scale, not absolute. The strategy's cost is equally clear: no protected qubit has yet been demonstrated, and the field's recent history contains results in which non-topological states mimicked the expected topological signatures closely enough to fool careful measurements [@yu2020]. Theoretical analyses also warn that thermally excited anyons erode the protection at any nonzero temperature, however slowly [@foundations2026], and that ultrametric encodings proposed as alternatives sit at thresholds roughly two orders of magnitude worse than surface codes under independent errors — confining their advantage to the correlated-failure regime in which they were designed [@quditqec2026; @adelicqec2026]. The honest status of hardware protection is therefore: strong theory, hard gaps measured in the relevant materials [@gul2017; @gao2023; @kong2021], no qubit — with engineered high-temperature platforms such as twisted cuprate structures proposed but undemonstrated [@twistronics2025].

The thesis examined in this paper is the tempting one: that hardware protection is the quantum analogue of the silicon noise margin, and that a "quantum semiconductor" — a protected qubit needing little or no active correction — is the architecture that wins on energy. The paper's job is not to defend that thesis but to compute, from published numbers, where it is right and where it is not.

## 3. The trade-off surface

Fix a benchmark computation of $N$ logical operations. For each strategy, the energy per correct solution is

$$ E_{\text{solution}} = \frac{E_{\text{op}} \times \text{overhead} \times N}{P_{\text{correct}}} , $$

where $E_{\text{op}}$ is the energy of one elementary operation, the overhead is $1$ for a protected qubit and the physical-qubits-per-logical-qubit factor for an actively corrected one, and $P_{\text{correct}}$ is the probability the whole computation completes correctly.

For **active correction** we calibrate on the measured surface-code memory: logical error per cycle $L_7 = 1.43 \times 10^{-3}$ at distance $7$, suppressed by $\Lambda = 2.14$ for every increase of the distance by two. A computation of $N = 10^{6}$ logical operations needs $L \lesssim 10^{-7}$, which this calibration reaches at distance $33$ with an overhead of $(2d-1)^2 = 4225$ physical qubits per logical qubit. For **hardware protection** we take the thermal-activation law $L = \exp(-\Delta/k_B T)$ with no correction block.

The crossover is the surface in (gap, temperature, physical error rate, decoder efficiency) space where the two energies are equal. It is computed numerically rather than guessed; the computation is deposited with this paper and described in Section 7. Its qualitative content, visible in the results below, is that protection wins when $\Delta/k_B T$ is large and loses when it is not: the computed boundary sits between roughly 7 and 15, while the gap sizes measured in real materials sit at 100 and above, deep inside the protection regime. That is a physical statement about thermal activation, not a marketing statement about materials.

## 4. A first scorecard

Table 1 reports the quantum-level energy per correct solution for the benchmark ($N = 10^{6}$ logical operations, target logical error $10^{-7}$ per operation). The superconductor entry uses a per-gate anchor of $8.2 \times 10^{-25}$ J at 15 mK, recomputed in the deposited verification from the thermodynamic translation formula $k_B T \ln(1/\alpha_r)$ with a $1.9\%$ amplitude-resolution rate; trapped-ion and spin entries use order-of-magnitude quantum-level estimates whose derivation is stated in the deposited data file; the protected entries assume a per-operation energy equal to the transmon anchor, which is generous to the comparison in the only way that matters, since no protected qubit exists to measure. Platform fidelities behind the rows: trapped-ion two-qubit gates at $99.9\%$ [@ballance2015]; silicon two-qubit gates demonstrated in semiconductor quantum dots [@veldhorst2014; @zhang2023]; photonic component loss follows standard figures with no single canonical source, flagged as an estimate in the data file.

| Platform | Strategy | p (physical) | Distance d | Overhead | P(correct) | E per correct solution (quantum level) |
|---|---|---|---|---|---|---|
| Superconducting transmon | active | $1.5 \times 10^{-3}$ | 33 | 4225 | 0.93 | $3.5 \times 10^{-15}$ J |
| Trapped ion | active | $1.0 \times 10^{-3}$ | 33 | 4225 | 0.93 | $4.2 \times 10^{-8}$ J (est. $E_{op}$) |
| Silicon spin | active | $1.0 \times 10^{-3}$ | 33 | 4225 | 0.93 | $4.2 \times 10^{-9}$ J (est. $E_{op}$) |
| Photonic (fusion) | active | $1.0 \times 10^{-2}$ | 33 | 4225 | 0.93 | $4.2 \times 10^{-3}$ J (est. $E_{op}$) |
| Majorana, InSb/NbTiN ($\Delta \approx 200$ µeV) | hardware | — | — | 1 | $\approx 1$ | $8.2 \times 10^{-19}$ J (assumed $E_{op}$) |
| Majorana, PbTe/Pb ($\Delta \approx 1$ meV) | hardware | — | — | 1 | $\approx 1$ | $8.2 \times 10^{-19}$ J (assumed $E_{op}$) |

**Reading the table honestly.** On the quantum-level comparison, hardware protection wins by three to four orders of magnitude — if the protected qubit exists with comparable per-operation energy. The table does not claim it does. Every active-correction entry assumes the measured Willow scaling transfers to the platform; every protected entry assumes an unmeasured qubit. The photonic row applies the surface-code calibration to a platform that in practice uses lattice codes, and is the least reliable row for that reason. The table is a ranking of the physics, not a ranking of today's hardware.

**The control-electronics caveat.** Full-stack analyses show the classical control and cooling electronics dominate the energy budget of every platform, by orders of magnitude, over the quantum-level gate energy [@fellous2022; @ramos2026; @aufferves2021]. Applied uniformly (a multiplier of $10^{4}$–$10^{6}$), this overhead does not change the ranking — it changes the absolute numbers, and it is the quantity the field measures least well. The paper's second-order recommendation follows: publish control-electronics power per platform with the same discipline as gate fidelities.

## 5. Predictions, stated in advance

Three predictions were written down before the scorecard computation was completed, and they are reported here with the outcomes the computation produced.

1. **At 15–20 mK with a protection gap of order $10^{-22}$ J or larger, hardware protection beats active correction on the quantum-level comparison; at 1 K and above, active correction wins at every physical error rate below threshold.** The computed crossover sweep confirms both halves: protection dominates wherever $\Delta/k_B T$ exceeds roughly 15 (the boundary sits between 7 and 15 in the sweep), and thermal activation hands the advantage to correction above roughly 0.1 K for the gap sizes measured in the literature. **Outcome: consistent.**
2. **Better decoders move the crossover in correction's favor.** The sweep with decoder efficiency improved by a factor of two halves the correction energy at every point. Constant-overhead fault tolerance under general noise, proved for low-density parity-check codes, bounds this trend from below [@christandl2025]. **Outcome: consistent.**
3. **The quantum-semiconductor claim fails as stated if no protected platform demonstrates a logical error rate below the best corrected platform's rate at equal measured energy.** No protected qubit has been demonstrated, so this prediction is unresolved — and it is the one that decides the thesis. **Outcome: unresolved, with the failure condition explicit.**

## 6. Where the premises end

It is worth stating plainly which parts of the argument are derived here and which are taken on trust, because the two strategies have different trust profiles and the difference matters.

Four things are imported without re-derivation: the second law in its information-theoretic form (Landauer's bound), the quantum speed limit, the no-cloning theorem, and the definition of the joules-per-solution criterion with its measurement protocol. These are standard. Two things are imported from the experimental literature rather than proved here: the measured surface-code calibration (a demonstrated fact), and the claim that topological protection suppresses local errors exponentially in gap over temperature (a well-supported theoretical claim with no demonstrated qubit behind it). Everything the paper adds — the criterion applied as a platform ranking, the crossover computation, the predictions and their outcomes — is derived from those six ingredients by arithmetic and simulation, and every step is deposited.

The theory is therefore exactly as deep as its two experimental imports. A reader who trusts the hard-gap measurements but not the topological-protection claim will still find the scorecard useful for the actively corrected platforms, where the calibration is measured. A reader who trusts neither will still find the framing question — energy per correct solution — usable tomorrow against whatever hardware exists. That is the intended epistemic load: the paper's usefulness does not depend on the quantum semiconductor existing.

## 7. Verification and reproducibility

All quantitative claims in Sections 3–5 are computed by three deposited scripts using only the Python standard library: `thermo_bounds.py` (the thermodynamic constants and program anchor), `crossover_model.py` (the 32-scenario crossover sweep and the seeded 1000-sample Monte Carlo of the flagship point), and `scorecard_calc.py` (Table 1). Seeds, runtimes, and re-run instructions are in the deposited reproducibility statement. The scripts and their outputs accompany the paper so that every number in the scorecard can be regenerated or disputed by anyone.

## References
