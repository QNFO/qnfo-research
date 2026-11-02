---
title: "Manifesto for Honest Computation"
author: "Rowan Brad Quni-Gudzinas"
date: 2026-07-08
series: "The Qubit Delusion --- Phase VI (Final Synthesis)"
abstract: >
 Five papers have traced an arc from diagnosis to prescription. The qubit is a
 scaffold, not an invariant. Alternative paradigms exist. Physical limits are real.
 A diversified portfolio is rational. Institutions must be reformed. This final
 paper --- the Manifesto --- synthesizes these findings into principles for honest
 computation and a call to action for investors, researchers, policymakers, and
 the public. We propose five principles: (1) the substrate IS the algorithm; (2)
 correlation over particle; (3) joules per solution as the universal metric; (4)
 falsifiability as a condition of funding; and (5) institutional independence of
 verification. We propose a specific resource reallocation --- from the ~60% currently
 consumed by gate-model quantum computing toward thermodynamic, optical, neuromorphic,
 and analog quantum simulation --- and a Falsification Pledge by which institutions
 commit to pre-registering computational claims with time-bound success criteria.
 Computation is too important to be left to narrative production. The future of
 computing is honest, or it is nothing.
keywords:
 - manifesto
 - honest computation
 - post-classical computing
 - quantum computing reform
 - computational principles
 - research ethics
---

# Preamble

Computation is the most important technology of the twenty-first century.
It determines what we can know, what we can build, what we can cure, and
what we can defend against. The future of computation is, in a very real
sense, the future of human capability.

For the past two decades, a significant fraction of the world's
computational R&D expenditure --- roughly $35 billion --- has been directed
toward one specific computational paradigm: the fault-tolerant universal
gate-model quantum computer. This investment was made on the basis of
extraordinary claims: exponential speedups for problems of commercial
importance, revolutionary new industries, a transformation of the
computational landscape comparable to the invention of the transistor.

Those claims have not been realized. Not one commercially viable quantum
computer exists. Not one problem of genuine economic value has been solved
faster, cheaper, or more accurately by a quantum computer than by a
classical alternative. The roadmaps have been revised outward, repeatedly,
from "five years" to "ten years" to "the 2030s" --- and those timelines
assume flawless execution of error-correction protocols that currently
consume thousands of physical qubits per logical qubit.

This is not a temporary setback. It is not a matter of insufficient
funding, insufficient talent, or insufficient time. The failure is
structural. It is embedded in the institutional incentive systems that
fund computational research, in the ontological confusion that treats
qubits as particles rather than relational properties, in the neglect of
fundamental thermodynamic limits, and in the absence of independent
verification with enforcement mechanisms.

Five papers have mapped this terrain. This final paper --- the Manifesto --- 
synthesizes their findings into actionable principles and a call to
action. We do not merely diagnose. We prescribe. We do not merely
critique. We construct. The future of honest computation depends on it.

# 1. What We Have Learned

## 1.1 The Diagnosis (Phase I)

The qubit-gate-circuit model is an epistemic failure. It projects particle
ontology onto a relational, field-theoretic reality. The qubit is not a
thing; it is a relation. The gate is not an operation on an object; it is a
correlation between measurement contexts. Decoherence is not an enemy to be
suppressed; it is the physical process by which quantum systems become
classical --- and it can be harnessed as a computational resource.

The $35 billion quantum computing industry has optimized for narrative
production, not computational output, because the institutional incentive
structure rewards ambitious claims with prestigious publications, media
coverage, and capital inflows, while the correction --- independent
verification, qualification, and refutation --- operates on a timescale
too slow to affect capital allocation.

## 1.2 The Alternatives (Phase II)

Measurement-based quantum computing (MBQC), continuous-variable quantum
computing (CV-QC), topological quantum computing (TQC), field-theoretic
computation, analog quantum simulation, thermodynamic computing,
neuromorphic computing, and optical computing --- these are not minor
variations on the qubit model. They represent genuinely different
ontological commitments, with different scaling properties, different
manufacturability constraints, and different problem-class affinities.

The photonic platform (PsiQuantum, Xanadu) offers room-temperature
operation and leverages existing semiconductor manufacturing infrastructure,
making it the strongest commercial case in quantum computing. Neutral atom
arrays (QuEra, Atom Computing) offer the most promising path for near-term
scientific impact through analog quantum simulation. Ising machines and
thermodynamic solvers are already commercially deployed for optimization.
Neuromorphic processors already achieve ~10³× energy advantage over GPUs
for inference workloads.

## 1.3 The Limits (Phase III)

The Landauer bound does not privilege quantum over classical computation.
The Margolus-Levitin theorem imposes a fundamental quantum speed limit within
a factor of ~30-200 of current practice. The error-correction overhead --- 
10² to 10³ physical operations per logical operation --- multiplies the
thermodynamic cost of quantum computation beyond what any polynomial
algorithmic speedup can overcome.

Only exponential speedups --- Shor's algorithm for factoring, and possibly
quantum simulation at sufficient scale --- can overcome the energy penalty.
For everything else, the joules-per-solution comparison favors specialized
classical hardware: Ising machines for optimization, optical processors for
linear algebra, neuromorphic processors for inference, reversible classical
processors for general-purpose computation.

## 1.4 The Portfolio (Phase IV)

The rational investment response to these findings is a diversified
portfolio across physical substrates, allocated in proportion to the
evidence for each substrate-problem pair. Approximately 45% thermodynamic
and analog (Ising machines, p-bit networks, analog quantum simulators),
25% optical (integrated photonic matrix processors), 20% neuromorphic,
and only 5-10% fault-tolerant quantum --- a near-inversion of the current
allocation where gate-model QC absorbs roughly 60% of advanced computing
investment.

## 1.5 The Institutions (Phase V)

The current institutional structure --- venture capital with 10-year fund
horizons, government agencies without post-award evaluation mechanisms,
academic publishing with prestige cascades, and a regulatory vacuum --- is
configured to produce narrative assets, not computational ones. The $35
billion outcome is the equilibrium of this game.

Five reforms are necessary: an Advanced Computing Projects Agency (ACPA)
modeled on DARPA; mandatory independent verification for computational
claims above a materiality threshold; structural separation of quantum
hardware and software; joules-per-solution procurement for all government
computational contracts; and a public registry of computational claims
with time-bound falsification criteria.

# 2. The Five Principles of Honest Computation

From this synthesis, we distill five principles. They are not merely
guidelines. They are conditions that any computational research program
must satisfy to be considered honest.

## Principle 1: The Substrate IS the Algorithm

Computation is a physical process. The physical substrate --- its Hamiltonian,
its degrees of freedom, its natural dynamics, its coupling to the
environment --- determines what can be computed and at what cost. The choice
of computational scaffold (qubit vs. qumode, gate vs. measurement, digital
vs. analog) is never ontologically neutral. It encodes assumptions about
what computation IS, and those assumptions have consequences for what can
be computed efficiently.

The honest approach: match the problem class to the physical substrate
whose natural dynamics solve it most efficiently. Do not force all problems
into a single scaffold. Do not optimize a scaffold that is misaligned with
the physics. Let the physics do the computing.

## Principle 2: Correlation Over Particle

The fundamental computational resource in quantum systems is not the state
of individual qubits but the correlation structure --- entanglement, phase
coherence, collective modes --- that connects them. A quantum computer is a
machine for steering correlations, not for manipulating particles.

The honest approach: design computational architectures where correlation
is the primitive --- not the qubit, not the gate, not the circuit depth. In
MBQC, the cluster state IS the computation. In CV-QC, Gaussian entanglement
IS the resource. In TQC, braiding correlations IS the algorithm. In
thermodynamic computing, the free energy landscape IS the solver.

## Principle 3: Joules Per Solution, Not Quantum Volume

The universal metric for computational advantage is total energy consumed
to deliver a verified, correct answer to a specified problem at specified
scale. "Joules per solution" --- measured at the wall plug, including all
overhead --- is the only metric that is invariant under scaffold variation,
platform choice, and algorithmic approach.

"Quantum volume," "quantum utility," "quantum supremacy" --- these are
scaffold-specific metrics that privilege the qubit-gate-circuit model.
They do not measure what users care about: does this machine solve my
problem faster, cheaper, or more accurately than alternatives?

The honest approach: publish joules-per-solution numbers for commercially
relevant problems, compared against the best available classical
implementation. If the joules-per-solution number is not available, the
claim is not yet an investment proposition.

## Principle 4: Falsifiability as a Condition of Funding

No computational research program should receive public funding without
pre-registered, time-bound, falsifiable milestones. "We will demonstrate
X joules-per-solution advantage on problem Y of commercially relevant
scale Z by date W." If the milestone is not met by the stated date, funding
is terminated. No extensions. No rebranding. No milestone creep.

Falsifiability is not an optional feature of honest science. It is the
defining feature. A research program that cannot state what would count as
failure is not a research program; it is a faith-based initiative. Faith-
based initiatives have their place --- in religion, in art, in speculative
philosophy --- but they should not be funded with public money or marketed
to investors as technology investments.

## Principle 5: Institutional Independence of Verification

Evaluation of computational claims must be performed by institutions that
are structurally independent of the claimants. The academic community
cannot verify its own claims, because the prestige cascade ensures that
ambitious claims are rewarded before they are verified. Venture capitalists
cannot verify the claims of their portfolio companies, because the
information asymmetry is unbridgeable and the incentive is to mark up,
not to verify. Government agencies cannot verify claims from programs they
have funded, because program managers have career incentives to report
success.

Independent verification requires independent institutions: an ACPA with
DARPA's structure, a public registry with enforcement mechanisms, an
independent verification corps funded by a levy on computational research
expenditure. The principle is separation of powers: those who make claims
must not be the ones who verify them. Those who fund claims must not be
the ones who evaluate them. Those who benefit from claims must not be the
ones who adjudicate them.

# 3. The Honest Portfolio: A Concrete Reallocation

The principles above imply a specific reallocation of computational R&D
capital. We present it as a concrete recommendation, not as a theoretical
exercise.

## 3.1 Near-Term (1-3 Years): Deploy What Works

| Allocation | Substrate | Problem Class | Status |
|:----------:|:----------|:--------------|:-------|
| 25% | Ising machines / thermodynamic solvers | Combinatorial optimization | Commercially available |
| 20% | Optical matrix processors | Linear algebra (inference) | Research prototypes |
| 20% | Neuromorphic processors | Probabilistic inference, edge AI | Commercially available |
| 15% | p-bit probabilistic networks | Sampling, optimization | Research prototypes |
| 10% | Analog quantum simulators | Quantum many-body physics | Research demonstrations |
| 10% | Conventional CMOS + algorithms | General-purpose | Dominant incumbent |

**What to STOP funding at near-term scale:** Universal fault-tolerant
gate-model QC on superconducting or trapped-ion platforms. The thermodynamic
arithmetic does not work for commercially relevant problem sizes within
VC-relevant timeframes. These platforms should be maintained as fundamental
research programs at ~5% of current funding levels, not as commercial
ventures at ~60%.

## 3.2 Medium-Term (3-7 Years): Scale What Shows Promise

| Allocation | Substrate | What Success Looks Like |
|:----------:|:----------|:------------------------|
| 30% | Analog quantum simulation | 10,000-atom simulators; catalyst/pathway design |
| 25% | Optical processors | 1,000×1,000 photonic circuits in production |
| 20% | Neuromorphic + memristive | Memristive crossbar at commercial scale |
| 15% | Reversible/adiabatic CMOS | Processor at 1% Landauer limit |
| 10% | Photonic quantum (room-temp) | Logical qubit with error rate <10⁻⁶ |

## 3.3 Long-Term (7-15+ Years): Invest in the Physics

| Allocation | Substrate | Rationale |
|:----------:|:----------|:----------|
| 30% | Reversible classical computing | Path to Landauer-limit general-purpose computation |
| 25% | Photonic quantum (MBQC, CV) | Room-temperature; avoids cryogenic penalty |
| 20% | Analog quantum simulation at scale | Pharmaceutical and materials discovery |
| 15% | Fault-tolerant QC (crypto only) | Only path for factoring; government security interest |
| 10% | Field-theoretic computation | Speculative; fundamental research only |

# 4. A Call to Action

The principles and portfolio above are not self-executing. They require
action by specific actors.

## 4.1 To Investors (Venture Capital, Institutional, Retail)

- **Demand joules-per-solution numbers.** If a quantum computing company
 cannot state --- in writing --- the problem class, scale, joules-per-solution,
 classical competitor, and falsifiable milestone with timeframe, do not
 invest. Period.

- **Diversify across substrates.** The optimal portfolio is not a bet on
 one quantum computing company. It is a diversified allocation across the
 Problem-Substrate Mapping. If you must invest in quantum computing,
 allocate no more than 10% of your advanced computing exposure to
 gate-model QC.

- **Shorten your evaluation cycle.** The Narrative Production Function
 operates on a timescale of months. Independent verification operates on
 years. Close the gap: require independent verification BEFORE capital
 deployment, not after. Your limited partners will thank you.

## 4.2 To Researchers (Academic and Industrial)

- **Pre-register your claims.** Before announcing a result, register the
 claim, the falsification criteria, and the independent verification
 protocol in the Public Registry of Computational Claims. If the registry
 does not yet exist, publish these on your institutional repository.

- **Celebrate negative results.** A well-designed experiment that falsifies
 a hypothesis is as valuable as one that confirms it. The institutional
 incentive structure currently penalizes negative results by making them
 harder to publish and less prestigious. Change this: submit negative
 results to journals, cite them, and reward colleagues who publish them.

- **Reject scaffold-specific benchmarks.** Do not report "quantum volume"
 or "quantum supremacy" without also reporting joules-per-solution on a
 commercially relevant problem. If the commercially relevant problem is
 not yet solvable, state when it will be --- with a specific date --- and
 hold yourself to that date.

## 4.3 To Policymakers and Funding Agencies

- **Establish an Advanced Computing Projects Agency.** Model it on DARPA.
 Fund it at $500 million per year. Staff it with active researchers on
 3-5 year terms. Give it the authority to terminate programs that miss
 milestones. Require it to publish all results --- positive and negative --- 
 within six months.

- **Mandate independent verification.** Any claim of computational
 advantage above a $10 million funding threshold must be independently
 verified within 12 months. Make independent verification a condition of
 continued funding. Fund the verification infrastructure through a 0.5%
 levy on computational research expenditure.

- **Reform procurement.** All government computational procurement above
 $1 million must evaluate bids on a joules-per-solution basis. No more
 buying "access" to quantum computers that solve no commercially relevant
 problems.

- **Establish a Public Registry of Computational Claims.** Fund it. Staff
 it. Give it the authority to flag unverified claims. Make compliance a
 condition of government funding and a factor in government procurement.

## 4.4 To the Public

- **Demand evidence.** When a company announces "quantum supremacy" or
 "quantum advantage," ask: on what problem? Compared to what classical
 alternative? At what joules-per-solution? What is the falsification
 criterion? What is the deadline?

- **Follow the joules, not the narrative.** The quantum computing industry
 has produced an extraordinary volume of press releases, TED talks, and
 *Nature* covers. It has produced zero commercially viable computational
 output. These two facts are not unrelated. The narrative production
 function consumes resources that could be directed toward actual
 computation.

- **Support institutional reform.** Write to your representatives. Demand
 that public funds for computational research be allocated on the basis of
 evidence, not narrative. The $35 billion already spent came, in
 significant part, from taxes. The next $35 billion should be spent
 differently.

# 5. The Falsification Pledge

We, the authors of this Manifesto and the five papers that precede it,
commit to the following:

1. **Every claim we make about computational advantage will be accompanied
 by a specific joules-per-solution number compared against the best
 available classical implementation.**

2. **Every prediction we make about future computational capability will
 be accompanied by a specific deadline and a specific falsification
 criterion. If the deadline passes without the criterion being met, we
 will publicly acknowledge the failure.**

3. **We will not report "quantum volume," "quantum utility," or any other
 scaffold-specific metric without also reporting the joules-per-solution
 on the most commercially relevant problem accessible at the reported
 scale.**

4. **We will submit all our computational claims to independent
 verification --- and we will publish the verification reports, whether
 they confirm, qualify, or refute our claims.**

5. **We will celebrate negative results. A falsified hypothesis is a
 contribution to knowledge. A perpetually unfalsifiable research program
 is a drain on knowledge.**

We invite --- we *challenge* --- every institution, company, research group,
and individual working in post-classical computing to adopt this pledge.
Make it public. Link to it from your website. Include it in your grant
proposals and your investor pitch decks.

If you cannot adopt the Falsification Pledge, ask yourself why. What are
you protecting? Who benefits from the ambiguity? What would happen to your
funding, your valuation, your prestige, if your claims were subjected to
rigorous, independent, time-bound verification?

The answer to that question is the answer to the question this entire
series has been asking: is quantum computing a scientific enterprise or a
financial one? Is it seeking truth, or seeking capital?

# 6. Conclusion: Honest, or Nothing

The first five papers in this series have made the case. The qubit is a
scaffold, not an invariant. Alternative paradigms exist. Physical limits
are real and binding. A diversified portfolio is the rational investment
response. Institutional reform is necessary and possible.

This Manifesto adds the final element: a set of principles and a call to
action. Computation can be honest, or it can be nothing. A computational
paradigm that substitutes narrative for evidence, prestige for verification,
and fundraising for falsification is not a scientific enterprise. It is a
machine for converting capital into press releases.

The laws of physics do not negotiate. The Landauer bound applies equally to
classical and quantum computation. The Margolus-Levitin theorem limits the
speed of any quantum evolution. The error-correction overhead multiplies
the thermodynamic cost of fault-tolerant quantum computation beyond what
any polynomial algorithmic speedup can overcome. These are facts. They are
not subject to revision by press release, by TED talk, or by Series D
funding round.

The future of honest computation is not a single device. It is an ecosystem:
thermodynamic optimizers for combinatorial problems, optical processors for
linear algebra, neuromorphic processors for probabilistic inference, analog
quantum simulators for quantum many-body physics, reversible classical
processors for general-purpose computation, and --- if and when the physics
permits --- fault-tolerant quantum processors for cryptography and other
problems requiring exponential speedups at scale.

This ecosystem will not emerge from the incumbent quantum computing
industry, whose institutional incentives reward the opposite of honesty.
It will emerge from new institutions --- an ACPA, an independent verification
corps, a public registry of claims --- and from the courage of individual
researchers, investors, and policymakers who insist on evidence over
narrative.

The choice is ours. Honest computation, or nothing.

---

*This Manifesto is the sixth and final paper in the "Qubit Delusion" series.*
*All papers are available under CC-BY-4.0 at papers.qnfo.org via the concept DOI*
*https://papers.qnfo.org/papers. The Falsification Pledge can be adopted by any*
*institution, company, or individual. Attribution requested, not required.*

---

**Series References**

- Phase I: "The Qubit Delusion" --- https://papers.qnfo.org/papers/paper-the-qubit-delusion/
- Phase II: "Beyond the Qubit" --- https://papers.qnfo.org/papers
- Phase III: "The Physics of Computation" --- https://papers.qnfo.org/papers
- Phase IV: "The Problem-Substrate Mapping" --- https://papers.qnfo.org/papers
- Phase V: "Institutional Reform" --- https://papers.qnfo.org/papers/paper-institutional-reform/
- Phase VI: "Manifesto for Honest Computation" --- this paper
