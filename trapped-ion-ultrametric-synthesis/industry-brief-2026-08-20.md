# Why Measure Error Correlations Before Choosing a Code

**A one-page brief for quantum-hardware teams and funders.**
Source record: *The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for
Testing p-Adic Structure in Quantum Dynamics*, v1.4 — DOI 10.5281/zenodo.22025544
(concept 10.5281/zenodo.22013263). All numbers cited below are published in the
record and its source archive.

---

## The problem: threshold theorems are theorems about noise models, not hardware

Every error-correction threshold — the surface code's ~1.1×10⁻² included — is proven
under an error model. That model is overwhelmingly *independent, Markovian, additive*
noise: the Archimedean geometry of the error channel. Real devices violate it:
cosmic-ray multi-qubit events, crosstalk, two-level-system defects, leakage,
non-Markovian baths, and thermal correlations grow *with scale*. If correlated
structure dominates at the scales where fault tolerance must actually run, the
threshold that matters is not the textbook one — it is the threshold under the
**measured** noise, and that number is not yet on anyone's datasheet.

## The honest disclosure first (the number that hurts)

Under independent errors, the ultrametric qudit code path shows a threshold near
2.0×10⁻⁴ — **approximately 55× worse than surface codes** (published in the
program's own QEC record, 10.5281/zenodo.21046993; recomputed from its own numbers).
We publish this number because it is the crux: **if independent errors dominate at
scale, the ultrametric path is dead, and the industry is right to ignore it.** The
same discipline published the program's own nulls: no CMB log-periodic signal
(10.5281/zenodo.21902891), an anti-ultrametric biological counterexample
(10.5281/zenodo.21651892), and a QEC-Darwinism no-go theorem whose proof chain
assumes Archimedean geometry (Maity et al., arXiv:2608.03944).

## The one bet everything rests on

> **At scale, error structure is not independent.**

That is a falsifiable statement about hardware, not a philosophical preference. The
case for taking it seriously: (1) the industry's own correlated-error pain
(cosmic-ray events, crosstalk, TLS defects); (2) the QEC-Darwinism theorem — QEC and
emergent classical objectivity cannot coexist above F_L > 0.874 *under the
Archimedean assumption*, which is exactly the assumption correlated/hierarchical
noise violates; (3) the thermal/energy argument — active correction pays an energy
tax that grows with distance, while structure-suppressing (passive) designs do not.

## The ask: a rounding error of R&D budget, spent on measurement

We are **not** asking anyone to abandon surface codes. We are asking teams to spend a
small fraction of their error-characterization budget on **measuring the correlation
structure of errors at scale** — because that measurement improves *any* code choice,
ultrametric or not:

1. **R1 — Page–Wootters ultrametricity probe** (8 weeks on existing trapped-ion
   apparatus; predicted UVR split 0% diagonal vs 29–35% nondiagonal; kill-condition
   pre-registered).
2. **R3 — laptop benchmark** (effective transient dimension on p-regular trees;
   code deposited with the source record).
3. **Artifact 4 — energy-audit template** (joules-per-solution methodology, applied
   to any platform).
4. **Artifact 5 — QEC-Darwinism constraint checker** (audit any candidate
   architecture against the F_L > 0.874 no-go; check which Archimedean assumptions
   the proof uses — if an advantage survives only by violating a named assumption,
   the geometry is doing real work).

The **correlated-error benchmark spec** (companion document) turns the bet into a
pre-registered protocol: pairwise correlation functions, spatiotemporal clustering,
non-Markovian memory, event-burst statistics, and decision rules that settle the
question either way — **including the rule that kills the ultrametric path if
independent errors dominate.**

## What we promise in return

If the measurement says independent errors dominate: the ultrametric path is dead,
and we will have published the result — the program's ledger already includes its own
nulls. If it says correlated structure dominates: the 55× comparison was the wrong
comparison, the geometry of the error structure *is* the code, and the teams that
measured first own the transition.

**One measurement, pre-registered, cheap, valuable either way. That is the entire
ask.**

---

*Companion: `correlated-error-benchmark-spec-2026-08-20.md` (pre-registered protocol
and decision rules). Full register: 10.5281/zenodo.22025544. This brief is an
engagement artifact, not a claim of hardware advantage.*
