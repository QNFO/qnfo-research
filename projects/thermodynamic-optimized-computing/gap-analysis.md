# Gap Analysis: Energy as the Selection Criterion for Quantum Computing Platforms

**Project:** Thermodynamically Optimized (Topological/Quantum) Computing
**Date:** 2026-08-21 · Working document for the paper body (Sections 1–2 draft material)

---

## 1. What already exists

**Inside the research program.** The program has published the criterion itself: the joules-per-solution metric, with a measurement protocol and anti-gaming provisions (10.5281/zenodo.21637028). It has analyzed the thermodynamic and informational bottlenecks of scalable fault-tolerant quantum computation (10.5281/zenodo.17955898). Its Problem-Substrate Mapping work concludes that quantum error correction multiplies the thermodynamic cost of a computation by roughly 10²–10³, and that only exponential algorithmic speedups can overcome that penalty. Its thermodynamics-of-translation analysis derived a concrete per-gate anchor: roughly 8.2×10⁻²⁵ joules per transmon gate at 15 mK with a 1.9% approximation rate. It has published whole-system energy accounting for a fault-tolerant machine and a resource-commensurable comparison of bosonic encodings. None of these, however, applies the criterion to the question this paper asks: *which physical platform wins?*

**Outside the program.** Two external literatures border the question and neither occupies it. Classical thermodynamic computing — the Landauer–Bennett line, generalized reversible computing, and the time-space-energy surveys of reversible machines — owns the thermodynamic analysis of classical logic but has no quantum-platform scorecard. Fault-tolerant quantum computation theory owns the error-correction side but ranks codes by threshold and overhead, not by energy per correct solution. The 2025 result on constant-overhead fault tolerance under general noise (QLDPC codes, arXiv:2512.02760) matters here: it caps the worst-case error-correction tax from below, which means the naive "error correction is unavoidably 10²–10³ times more expensive" premise needs to be stated as a decoder- and code-dependent claim.

**What is missing.** No published work scores superconducting, trapped-ion, spin, photonic, and protected (topological) platforms against one another on a common energy-per-correct-solution scale computed from published data, and none draws the crossover curve between active correction and hardware protection with explicit temperature and decoder-efficiency axes. That is the gap.

## 2. Why the gap matters

Quantum computing investment is currently steered by qubit counts, gate fidelities, and logical error rates — quantities that do not answer the question a buyer or an investor actually asks: what does a correct answer cost? If a material-science dollar spent on protected substrates buys more correct solutions per joule than a decoder-engineering dollar spent on fragile qubits, the field's roadmap metric is the wrong selection criterion and the industry is misallocating effort. Conversely, if active correction wins at every plausible protection level, that is equally worth knowing and equally publishable. Either way, the missing object is a quantitative, falsifiable comparison. This paper builds it.

## 3. How this project fills it

Three deliverables, in plain terms:

1. **A platform scorecard.** A table scoring candidate platforms on a joules-per-correct-solution proxy built from published per-gate energies, error rates, cooling overhead, and correction overhead. Every number either carries a primary-literature source or is marked as unresolved.
2. **A crossover curve.** A model of the trade-off surface between active correction and hardware protection, with temperature and decoder efficiency as explicit axes, showing where each strategy is energetically cheaper for a fixed benchmark computation.
3. **Pre-registered predictions.** Quantitative conditions under which the claim fails, stated before the comparison is completed, so that the outcome — whichever way it falls — is informative.

## 4. Where the premises end

This section states, in plain prose, which parts of the argument are derived and which are assumed.

The argument takes four things as given and does not re-derive them: the second law and its information-theoretic form (the Landauer bound), the quantum speed limit (Margolus–Levitin), the no-cloning theorem, and the definition of the joules-per-solution criterion from the metric paper. These are imported primitives. It also takes two things as given from the literature rather than proving them here: that topological protection suppresses local errors exponentially in the ratio of an energy gap to temperature (standard in the anyon literature, experimentally unestablished at scale), and that error-correction overhead depends on code and decoder choices (now bounded from below by the constant-overhead results).

From those premises, two facts are derived by ordinary argument. First, classical semiconductor logic needs no active correction because a bit is carried collectively with gain restoration, while quantum logic cannot copy or amplify an unknown state — so some protection strategy, material or corrective, is mandatory. Second, whatever the strategy, the energy cost is a product of per-operation energy, overhead, and the probability of a correct run.

Everything beyond that — the claim that platforms should be ranked by joules per correct solution, the claim that a protected "quantum semiconductor" regime may exist where active correction becomes minimal, and the crossover predictions — is the paper's own contribution and is presented as hypothesis, not theorem. A reader who rejects the two literature imports will still find the scorecard useful; a reader who accepts them will find the predictions falsifiable.

## 5. Known tensions the paper must carry

The program's own results complicate the thesis and are disclosed rather than hidden. First, its foundational ultrametric-computation paper concludes that topological quantum computing fails at nonzero temperature through thermal anyon proliferation — protection is exponential in gap over temperature, not absolute. Second, the program's own tree-code thresholds sit roughly 55× worse than surface-code thresholds under independent errors, which confines the passive-protection advantage to correlated-failure regimes. Third, the high-temperature superconductor pathway has no experimental validation at the coherence timescales computation requires. The paper states these facts and builds its predictions on the trade-off surface they define, rather than on the stronger claim a reader might expect from the title.
