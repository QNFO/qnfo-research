---
title: "The Qubit Delusion: How Particle Ontology Sabotaged Quantum Computing"
author: "Rowan Brad Quni-Gudzinas"
date: 2026-07-08
abstract: |
  The quantum computing industry has absorbed approximately $35 billion in global investment
  over two decades while delivering zero commercially viable machines. This paper argues
  that the failure is not merely an engineering delay but an epistemic crisis: the dominant
  qubit-gate-circuit model of quantum computation imports a particle ontology that is
  inconsistent with quantum field theory, relational quantum mechanics, and the physics of
  continuous, correlated systems. Through systematic deconstruction of the scaffolds
  underlying quantum computing -- qubit-as-particle, gate-as-discrete-operation,
  decoherence-as-enemy, error-correction-as-classical-coding -- we identify the invariants
  that survive scaffold removal (superposition, entanglement, correlation structure, phase
  coherence) and examine alternative computational paradigms (measurement-based,
  continuous-variable, topological, and field-theoretic) that are more faithful to quantum
  reality. We combine ontological analysis with empirical forensics -- a reproducibility
  scorecard of twenty major milestone claims, a comparative bubble-morphology analysis
  situating the quantum computing capital structure alongside historical technology bubbles,
  and a press-release-versus-preprint claim-gap analysis -- to assess whether the field is
  producing science or narrative assets. The evidence suggests a systematic map-territory
  confusion operating at industrial scale, sustained by institutional incentives that reward
  optimism over falsification. We conclude with a constructive research agenda grounded in
  field-theoretic and relational quantum computation.
---

# 1. Introduction

In October 2019, Google announced "quantum supremacy" --- a 53-qubit processor,
Sycamore, had performed a random circuit sampling task in 200 seconds that
would, Google claimed, take the world's largest supercomputer 10,000 years to
reproduce [@Arute2019]. Sundar Pichai compared the achievement to the Wright
brothers' first flight. The announcement triggered a wave of media coverage,
venture capital inflows, and national quantum strategies across the G20.

Four years later, IBM's Head of Quantum, Jay Gambetta, reframed the field's
ambitions. Gone was "supremacy." The new watchword was "quantum utility" --- a
more modest claim that quantum computers might someday solve problems of
practical interest. IBM's Eagle processor, with 127 qubits, had simulated the
Ising model on a scale that strained classical methods [@Kim2023]. Yet no
commercially valuable computation had been performed that could not, with some
effort, be accomplished on classical hardware.

This pattern --- spectacular announcement followed by qualification, followed by
a new, more distant milestone --- has repeated with metronomic regularity
throughout quantum computing's commercial history. D-Wave sold "quantum
computers" to Lockheed Martin and Google in 2011 -- 2013, only for independent
benchmarking to reveal no speedup over classical algorithms for the problems
tested [@Ronnow2014]. Rigetti went public via SPAC at a $1.5 billion valuation
in 2022; by 2024 its stock had declined over 90%. IonQ, the first pure-play
quantum computing company to IPO, has oscillated between hype-driven rallies and
reality-driven corrections.

By 2026, the global quantum computing industry has absorbed an estimated $35
billion in combined public and private investment. No commercially viable
quantum computer exists. Not one. The roadmaps project fault-tolerant machines
in the 2030s, which would mean a roughly forty-year interval between Shor's
algorithm (1994) --- the field's foundational existence proof --- and a working
product. Even those timelines assume flawless execution of error-correction
protocols that currently require thousands of physical qubits to encode a single
logical qubit.

The standard narrative attributes this protracted timeline to engineering
difficulty: qubits are fragile, decoherence is relentless, error correction is
expensive, and scaling is hard. This is undoubtedly true. But it may also be
*insufficient* --- a proximate explanation that obscures a deeper, structural
problem.

This paper proposes a different diagnosis. **The failure of quantum computing
to produce viable hardware is not primarily an engineering problem. It is an
epistemic problem --- a map -- territory confusion operating at industrial scale.**
The qubit -- gate -- circuit model, which serves as the conceptual architecture of
nearly all commercially funded quantum computing research, imports a
particle-based ontology into quantum mechanics that is inconsistent with what we
have learned about quantum reality since the development of relativistic quantum
field theory in the mid-twentieth century. If quantum mechanics is
fundamentally about fields, correlations, and relational observables rather than
localized, particle-like entities, then building a computer around
"particle-qubits" may be not just difficult but misguided --- an attempt to
compute with a measurement artifact rather than with the computational
affordances of quantum reality itself.

This paper develops this thesis in five parts. **Section 2** provides a
philosophical and physical deconstruction of the qubit -- gate -- circuit scaffold,
identifying what is arbitrary convention (scaffold) and what is invariant across
representations. **Section 3** presents empirical forensics: a reproducibility
scorecard for twenty major quantum computing milestone claims, a
bubble-morphology analysis comparing the quantum computing capital structure to
historical technology bubbles, and a press-release-versus-preprint claim-gap
analysis across five leading institutions. **Section 4** surveys alternative
quantum computational paradigms --- measurement-based, continuous-variable,
topological, and field-theoretic --- that move away from particle-qubit ontology
and may be more faithful to quantum reality. **Section 5** examines the
sociology and institutional economics of the quantum computing ecosystem,
analyzing how career incentives, venture capital structures, and corporate
branding imperatives sustain the qubit-gate model even in the face of mounting
negative evidence. **Section 6** proposes a constructive research agenda
grounded in field-theoretic and relational approaches to quantum computation.
**Section 7** concludes.

A note on method: this paper is produced by the QNFO autonomous research
pipeline under the LLM Research Automation Protocol (LRAP). All empirical
claims are sourced from publicly available literature, press archives, preprint
servers, and financial disclosures. The ontological analysis draws on the
Deconstruction Spiral v4.0 methodology, which systematically separates
human-imposed scaffolds from structural invariants. The empirical forensics
employ standard meta-scientific tools adapted from the reproducibility
movements in psychology and biomedicine. No proprietary data or human-subject
research is involved. The conclusions are falsifiable: Section 3 specifies the
observations that would refute the central thesis.

---

# 2. Ontological Deconstruction of the Qubit -- Gate -- Circuit Model

## 2.1 The Scaffold -- Invariant Distinction

Every scientific model deploys *scaffolds*: arbitrary human conventions --- 
choice of basis, coordinate system, unit, epoch, gate set, qubit encoding --- that
enable representation but do not inhere in the phenomenon represented. The
ability to distinguish scaffold from invariant is the mark of episte