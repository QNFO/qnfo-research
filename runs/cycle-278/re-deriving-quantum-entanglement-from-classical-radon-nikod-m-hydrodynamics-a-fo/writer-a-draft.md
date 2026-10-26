# Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis

## Abstract

The Hydrodynamic Stability Hypothesis (HSH) conjectures that standard quantum mechanics, including multipartite entangled states such as the Greenberger–Horne–Zeilinger (GHZ) state, can be axiomatically re‑grounded in classical measure theory: wavefunctions are interpreted as Radon–Nikodým densities that relax into basins of attraction of classical probability measures under a local hydrodynamic transport, restoring local realism without superdeterminism. We formalize HSH as four explicit axioms (classical probability space, local state variables, local continuous transport, free measurement settings) and attempt an explicit derivation of the GHZ state and its Bell‑type correlations purely from those axioms. By showing with full arithmetic that the pointwise product constraint $P_{1}P_{2}P_{3}P_{4}=+1$ follows from the axioms, while the quantum predictions require the product $-1$, we obtain a Mermin‑type violation factor of $2$ and a CHSH violation factor of $\sqrt{2}\approx1.414214$. The strong form of HSH is therefore falsified: reproducing GHZ statistics forces either non‑local variables or contradiction. As a clearly labeled projection, we compute the sub‑femtosecond propagation timescales that any simulation of the proposed hydrodynamic transport must resolve, and we discuss which weakened versions of the hypothesis could survive.

## 1. Introduction

Quantum networks and distributed quantum information processing rely on multipartite entanglement as a resource that enables tasks such as secret sharing, distributed sensing, and fault‑tolerant computation. Engineers designing quantum repeaters, protocol designers optimizing entanglement distribution, and theorists assessing the foundations of quantum mechanics all face the practical problem that the presence of Bell‑violating correlations imposes stringent constraints on any underlying local‑realist description. If the Hydrodynamic Stability Hypothesis (HSH) were correct, it would provide a local‑realist, classical‑measure‑theoretic foundation for these resources, eliminating the need for non‑local explanations and potentially simplifying the design of quantum‑network protocols. However, the hypothesis must reproduce the GHZ‑type correlations that are experimentally verified and essential for network‑level advantages. 

We therefore ask: can the axioms of HSH generate the GHZ stabilizer statistics without invoking non‑local influences? Our contributions are:

1. Formalization of HSH as four minimal axioms (Section 3.1).  
2. Derivation of the classical pointwise product constraint $P_{1}P_{2}P_{3}P_{4}=+1$ from the axioms (Section 4.2).  
3. Computation of the quantum GHZ stabilizer values and the resulting contradiction (Section 4.1).  
4. Quantitative Mermin and CHSH violation analysis (Sections 4.3–4.4).  
5. Projection of the temporal resolution required for the sub‑femtosecond particle‑tracking simulations proposed by HSH (Section 4.6).  

## 2. Background and Related Work

**Entanglement as a dynamical and statistical resource.** Reference [1] articulates a philosophy drawn from statistical mechanics and random‑matrix theory: individual instances of complex quantum circuits are intractable to simulate, but the statistical properties of random ensembles obey simple universal laws. This is directly relevant to HSH because a Radon–Nikodým measure is an ensemble object, not a single‑trajectory object, so any classical hydrodynamic re‑grounding must live at exactly the ensemble‑statistical level emphasized by [1]. Our axiom set in Section 3 is therefore phrased at the ensemble level.

**Multipartite entanglement in networks.** Reference [2] states that a quantum internet aims at distributing bipartite entanglement between distant nodes, but that multipartite entanglement between nodes may empower the quantum internet for additional or better applications in communications, sensing, and computation, and presents an algorithm for generating multipartite entanglement between distributed nodes. Reference [6] introduces hybrid entangled states—entanglement between different degrees of freedom—as enabling various quantum computational and communication tasks with fewer resources, and aims to exploit this advantage in communication over quantum networks. Together, [2] and [6] establish that multipartite entanglement of exactly the GHZ type we analyze is an operational, technologically targeted resource, not a mathematical curiosity; any re‑grounding of quantum mechanics must reproduce it.

**The classical–quantum boundary.** Reference [3] states that 75 years after the term “entanglement” was coined, the connection between quantum and classical mechanics remains an open problem, and discusses, drawing on results in semiclassical systems, the fate of entanglement in a closed system as Planck’s constant becomes vanishingly small. Reference [5] identifies three classical, pre‑quantum paradigms for describing particles—the material point, the test‑particle, and the diluted particle (droplet model)—as limit cases of a quantum regime in which pairs of particles interact without getting entangled, an entanglement‑free regime that the (truncated) summary connects to decoherence‑related descriptions. These two works frame the exact question HSH answers in the opposite direction: [3] and [5] study how classicality emerges from quantum mechanics, whereas HSH claims the reverse reduction. Our falsification result is consistent with the framing of [3], in which the quantum–classical connection is treated as an open problem rather than a solved reduction.

**GHZ dynamics under classical environments.** Reference [4] addresses the dynamics of entanglement and coherence for three non‑interacting qubits initially prepared as a maximally entangled GHZ‑like state coupled with independent classical environments, considering two different Gaussian environment models. This is the closest antecedent to HSH’s program, since it couples a GHZ state to explicitly classical environments.

**Classical–quantum unification and interpolation programs.** Reference [8] states the goal of overcoming the two separate languages of classical and quantum systems and creating a smooth, common procedure providing a continuous passage between the strictly classical and the strictly quantized state, with path integration among the tools mentioned. Reference [7] shows that the scaling of the $\alpha$‑QPE family of phase‑estimation algorithms can be naturally and succinctly derived within a classical–quantum framework using quantum singular‑value transformations. Both [7] and [8] represent interpolation strategies between fixed classical and fixed quantum formalisms; HSH is more radical, claiming the quantum formalism is derivable from the classical one. Our result marks the precise point where such a derivation, if local, must fail.

**Internal program context.** The QNFO corpus entry [10] describes an archive of a research record investigating the Post‑Quantum Synthesis (PQS) framework. Reference [9] is the Hydrodynamic Stability Hypothesis itself, taken here as the conjecture under test as restated in the grounding material. References [11] and [12] provide no further detail beyond their titles, so we make no claims about their content; the title of [11] suggests a finite, real‑number‑free measurement formalism that would be a natural axiomatic substrate for a measure‑theoretic re‑derivation, but this cannot be verified from the supplied material.

## 3. Methods

### 3.1 Axiomatization of the hypothesis

We formalize the strong form of HSH as four axioms, chosen to be generous: each is the weakest assumption the hypothesis’s own description requires. Let $(\Lambda,\mathcal{F},\mu)$ be a classical probability space, with $\Lambda$ a configuration space of hidden classical states $\lambda\in\Lambda$.

- **(A1) Classical measure grounding.** Every quantum state corresponds to a measure $\mu_{\psi}\ll\mu$ with Radon–Nikodým derivative $\rho_{\psi}= \frac{d\mu_{\psi}}{d\mu}$, such that all quantum predictions are recoverable as functionals of $\rho_{\psi}$.
- **(A2) Local state variables.** For $N$ spatially separated parties, the configuration decomposes as $\lambda=(\lambda_{1},\ldots,\lambda_{N})$ with $\lambda_{i}\in\Lambda_{i}$, and each party’s outcome is a local function $A_{i}=f_{i}(\lambda_{i},s_{i})$ of its own variable and its own setting $s_{i}$.
- **(A3) Local continuous transport.** The time evolution $\mu_{t}= (\Phi_{t})_{*}\mu_{0}$ is generated by a local flow $\Phi_{t}$ on $\Lambda$ propagating information at finite speed $v_{\max}$, so that no influence connects spacelike‑separated events; preparation and measurement correspond to relaxation into basins of attraction $\mathcal{B}_{k}\subset\Lambda$ of stable measures, the observed outcome indexing the basin.
- **(A4) Free settings.** The distribution of measurement settings is statistically independent of $\lambda$ (no superdeterminism).

The strong claim of HSH is that A1–A4 suffice to derive the quantum formalism, including entangled states.

### 3.2 Falsification protocol

Given A1–A4, we ask whether the model can reproduce the quantum joint statistics of the GHZ state

$$|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl(|000\rangle + |111\rangle\bigr)$$

under local Pauli measurements $X$ and $Y$ on each of the three qubits. The protocol is: (i) derive the classical constraint that A1–A4 impose on the four relevant triple correlations, (ii) compute the quantum values of those same correlations from the GHZ state, and (iii) compare. Any mismatch falsifies the strong form, because the hypothesis claims to re‑derive the quantum statistics from the classical axioms. This is a derivation‑and‑contradiction analysis, not a numerical simulation; the complementary simulation target is specified as a projection in Section 4.6.

### 3.3 Simulation projection protocol

The complementary test proposed by the hypothesis is sub‑femtosecond particle tracking of the hydrodynamic transport $\Phi_{t}$, to check whether apparent instantaneous state changes across spatial barriers are accompanied by continuous local wave propagation. We compute, as labeled projections with stated assumptions, the propagation timescales such a simulation must resolve for the hypothesis’s locality claim to be checked.

## 4. Analysis

### 4.1 Quantum correlations of the GHZ state (inputs and derivation)

**Input 1 (explicit assumption, not sourced).** We take the GHZ state to be $|\mathrm{GHZ}\rangle = (|000\rangle + |111\rangle)/\sqrt{2}$.

**Input 2 (explicit assumption, not sourced).** We assume the Pauli operators $X$ and $Y$ each have eigenvalues $\pm1$.

**Step 1: action of Pauli strings on GHZ.** Using $X|0\rangle=|1\rangle$, $X|1\rangle=|0\rangle$, $Y|0\rangle=i|1\rangle$, $Y|1\rangle=-i|0\rangle$:

$$XXX\,|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl(|111\rangle + |000\rangle\bigr)=+|\mathrm{GHZ}\rangle,$$

$$XYY\,|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl(i\,i\,|011\rangle + (-i)(-i)\,|100\rangle\bigr)= -|\mathrm{GHZ}\rangle,$$

and identically for $YXY$ and $YYX$ by symmetry.

**Step 2: quantum triple products.** Since $XXX|\mathrm{GHZ}\rangle = |\mathrm{GHZ}\rangle$, the product of the three outcomes for settings $(X,X,X)$ is deterministically

$$\langle XXX\rangle_{Q}=+1.$$

Since $XYY$, $YXY$, $YYX$ each act as $-1$ on $|\mathrm{GHZ}\rangle$,

$$\langle XYY\rangle_{Q}= \langle YXY\rangle_{Q}= \langle YYX\rangle_{Q}= -1.$$

These four stabilizer eigenvalues are the quantum predictions any successful re‑derivation must reproduce.

### 4.2 The classical constraint from axioms A1–A4

Under A1–A4, each party $i\in\{1,2,3\}$ carries a local variable $\lambda_{i}$ and predetermined outcomes $A_{i}(\lambda_{i},s_{i})\in\{-1,+1\}$ for settings $s_{i}\in\{X,Y\}$. Define the four triple products:

$$P_{1}=A_{1}^{X}A_{2}^{X}A_{3}^{X},\quad
P_{2}=A_{1}^{X}A_{2}^{Y}A_{3}^{Y},\quad
P_{3}=A_{1}^{Y}A_{2}^{X}A_{3}^{Y},\quad
P_{4}=A_{1}^{Y}A_{2}^{Y}A_{3}^{X}.$$

Each $P_{k}\in\{-1,+1\}$ pointwise. Their product, computed pointwise for every fixed $\lambda$:

\[
\begin{aligned}
P_{1}P_{2}P_{3}P_{4}
&=(A_{1}^{X})^{2}(A_{1}^{Y})^{2}(A_{2}^{X})^{2}(A_{2}^{Y})^{2}(A_{3}^{X})^{2}(A_{3}^{Y})^{2}\\
&=(+1)^{6}=+1,
\end{aligned}
\]

since each local outcome appears exactly twice and squares to $+1$. Taking expectations and using that the pointwise identity holds $\mu$‑almost everywhere (A1):

$$\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1.$$

But the quantum values require $\langle P_{1}\rangle_{Q}=+1$ and $\langle P_{2}\rangle_{Q}= \langle P_{3}\rangle_{Q}= \langle P_{4}\rangle_{Q}= -1$, so the quantum product of the four correlations is

$$(+1)\times(-1)\times(-1)\times(-1) = -1\neq+1.$$

The contradiction is complete: the classical axioms force the pointwise product $+1$; the quantum stabilizer values require $-1$.

### 4.3 Mermin bound and violation factor

For any model satisfying A1–A4,

$$\bigl|\langle P_{1}\rangle - \langle P_{2}\rangle - \langle P_{3}\rangle - \langle P_{4}\rangle\bigr|\le 2,$$

because the pointwise expression $|P_{1}-P_{2}-P_{3}-P_{4}|=2$ whenever $P_{1}P_{2}P_{3}P_{4}=+1$. The quantum values give

\[
\begin{aligned}
\bigl|\langle P_{1}\rangle_{Q} - \langle P_{2}\rangle_{Q} - \langle P_{3}\rangle_{Q} - \langle P_{4}\rangle_{Q}\bigr|
&=|(+1)-(-1)-(-1)-(-1)|\\
&=|1+1+1+1|\\
&=4.
\end{aligned}
\]

Thus the classical bound is $M_{\mathrm{LHV}}=2$, the quantum value is $M_{\mathrm{Q}}=4$, the gap $\Delta M = 2$, and the violation factor $M_{\mathrm{Q}}/M_{\mathrm{LHV}} = 2$.

### 4.4 CHSH cross‑check

For two parties, the CHSH combination is

$$S = E(a,b) + E(a,b') + E(a',b) - E(a',b'),$$

with each $E\in[-1,1]$ classically, giving the bound $|S|\le2$. The quantum maximum for singlet‑type correlations is $S_{\max}=2\sqrt{2}$. Using $\sqrt{2}\approx1.414214$ (since $1.414214^{2}=2.0000006\approx2$),

$$2\sqrt{2}\approx2\times1.414214 = 2.828427.$$

The violation factor over the classical bound is $\sqrt{2}\approx1.414214$.

### 4.5 The fork and the falsification verdict

The derivation forces exactly two options:

- **Option (i).** Abandon A2 and allow $A_{i}$ to depend on all settings (non‑local response functions). Then the pointwise product constraint fails and the quantum values become reproducible, but the hypothesis’s locality claim is lost.
- **Option (ii).** Keep A2 and accept that the model fails to reproduce the quantum stabilizer values, i.e. it contradicts the quantum predictions it was supposed to re‑derive.

Either way, the strong form of HSH—local classical measure theory reproducing GHZ statistics—is falsified.

### 4.6 Simulation timescale projection (explicitly labeled projection)

**Assumptions (stated).**  
(P1) The hydrodynamic transport propagates influence at most at $v_{\max}=c=3.0\times10^{8}\ \mathrm{m\,s^{-1}}$ (the most generous choice).  
(P2) The spatial barrier separating two parties has width $L=1.0\times10^{-3}\ \mathrm{m}$ (typical laboratory scale).  
(P3) The simulation timestep must be at most one‑tenth of the propagation time to resolve the signal (Nyquist‑type requirement).

**Derivation.** Minimum propagation time:

\[
t_{\min}= \frac{L}{v_{\max}} = \frac{1.0\times10^{-3}\ \mathrm{m}}{3.0\times10^{8}\ \mathrm{m\,s^{-1}}}
= 3.333333\times10^{-12}\ \mathrm{s}\approx3.33\ \mathrm{ps}.
\]

Required timestep:

\[
\Delta t \le \frac{t_{\min}}{10}=3.333333\times10^{-13}\ \mathrm{s}\approx333\ \mathrm{fs}.
\]

Number of timesteps to cover one propagation across the barrier:

\[
N_{\mathrm{steps}} = \frac{t_{\min}}{\Delta t}=10.
\]

For a macroscopic barrier $L=1.0\ \mathrm{m}$:

\[
t_{\min}= \frac{1.0}{3.0\times10^{8}} = 3.333333\times10^{-9}\ \mathrm{s}\approx3.33\ \mathrm{ns},
\qquad
N_{\mathrm{steps}} = \frac{3.33\times10^{-9}}{3.33\times10^{-13}} = 1.0\times10^{4}.
\]

These are projections conditional on P1–P3. They establish the temporal resolution the tracking program must achieve, but they cannot rescue the strong form of the hypothesis: the GHZ contradiction is kinematic, not dynamical.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

1. **GHZ quantum correlations** (Section 4.1): $\langle XXX\rangle_{Q}=+1$; $\langle XYY\rangle_{Q}= \langle YXY\rangle_{Q}= \langle YYX\rangle_{Q}= -1$.
2. **Classical pointwise constraint** (Section 4.2): $P_{1}P_{2}P_{3}P_{4}=+1$ for every $\lambda$, hence $\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1$, which conflicts with the quantum product $-1$.
3. **Mermin bound and violation** (Section 4.3): classical $M_{\mathrm{LHV}}=2$; quantum $M_{\mathrm{Q}}=4$; gap $\Delta M=2$; violation factor $2$.
4. **CHSH cross‑check** (Section 4.4): classical bound $2$; quantum maximum $2\sqrt{2}\approx2.828427$; violation factor $\sqrt{2}\approx1.414214$.
5. **Falsification verdict** (Section 4.5): the strong form of HSH is falsified; any classical measure‑theoretic model reproducing GHZ statistics must violate axiom A2 or contradict the quantum predictions.
6. **Simulation timescale projections** (Section 4.6): for $L=1.0\times10^{-3}\ \mathrm{m}$, $t_{\min}=3.333333\times10^{-12}\ \mathrm{s}$, $\Delta t\le3.333333\times10^{-13}\ \mathrm{s}$, $N_{\mathrm{steps}}=10$; for $L=1.0\ \mathrm{m}$, $t_{\min}=3.333333\times10^{-9}\ \mathrm{s}$, $N_{\mathrm{steps}}=1.0\times10^{4}$.

## 6. Discussion

**What the falsification does and does not show.** The derivation in Sections 4.2–4.5 falsifies the *strong* claim: that GHZ‑type Bell‑violating correlations follow from classical measure theory plus local hydrodynamic transport plus freedom of settings. It does not falsify weaker versions. In particular, a version of HSH that drops A2—allowing the Radon–Nikodým measure to be non‑local on $\Lambda$—or that reinterprets “locality” at the level of the flow rather than the response functions, escapes the argument. This is the most likely retreat position, and it matches mainstream non‑local interpretations; the value of the derivation is that it shows HSH cannot simultaneously keep locality, measurement freedom, and the GHZ correlations.

**Against ourselves: possible escapes we cannot exclude.** First, our formalization A1–A4 is our own; the source record [9] supplies no summary text, so the hypothesis’s author might formalize “stability” or “locality” differently in ways that evade our axioms. Second, we assumed deterministic response functions $A_{i}\in\{\pm1\}$; stochastic local response functions change the bookkeeping but not the underlying pointwise product constraint, because the algebraic identity $P_{1}P_{2}P_{3}P_{4}=+1$ holds pointwise regardless of randomness. A fully rigorous stochastic treatment is beyond the scope of this paper. Third, the connection between “basins of attraction” (A3) and Born‑rule statistics is not derived here; even if the correlation structure were classically reproducible, the probabilities would need a separate derivation, and the category‑theoretic program of [11] (which provides no detail beyond its title) might be the intended substrate—this cannot be verified from the supplied material.

**Limitations of the quantitative work.** The timescale projections of Section 4.6 depend entirely on the assumed barrier width $L$ and the generous speed choice $v_{\max}=c$; the dimensional requirement of the hydrodynamic model is itself an unspecified parameter of HSH [9], so the projections bound only the temporal resolution, not the full computational cost, which grows with phase‑space dimensionality and was not computed here. The Mermin and CHSH bounds are standard results re‑derived within our axiom system, not novel theorems; their novelty lies only in their application to the HSH axiom set.

**Failure modes.** If defenders respond by weakening A2 while retaining the word “local” for the transport $\Phi_{t}$, the falsification loses its target; the paper’s contribution then becomes a clarification of which notion of locality is incompatible with GHZ statistics. If a regularised (non‑singular) family of classical measures could be shown to approximate the GHZ correlations while keeping A2, our use of deterministic pointwise assignments would be the vulnerable point—but the product constraint $P_{1}P_{2}P_{3}P_{4}=+1$ holds for any local assignment, deterministic or stochastic, so this escape route is closed in the deterministic case and, we argue, in the stochastic case by the same algebra.

**What would falsify our falsification.** A single explicit construction of local response functions $A_{i}(\lambda_{i},s_{i})$ satisfying A1–A4 that reproduces all four stabilizer values $\langle P_{1}\rangle=+1$, $\langle P_{2}\rangle=\langle P_{3}\rangle=\langle P_{4}\rangle=-1$ would falsify our falsification, because it would contradict the pointwise product constraint derived in Section 4.2. Similarly, an experimental or theoretical demonstration that the GHZ stabilizer values admit a local stochastic measure‑theoretic model with $\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=-1$ would break the argument at its pointwise step.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Researchers in quantum foundations, designers of quantum‑network protocols, and theorists exploring classical‑quantum unification will use the result to assess whether a local‑realist, measure‑theoretic foundation can underpin multipartite entanglement resources. If the result holds, any design that assumes a purely local classical underpinning for GHZ‑type correlations must be revised; network‑level performance analyses that rely on such an assumption will need to incorporate non‑local or hybrid models.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA Technology Readiness Level definitions, it resides at TRL 1–2 (basic principles observed and reported). Analytical work of this nature never exceeds TRL 3.

**(c) Smallest next experiment or prototype.** The minimal de‑risking test is a constructive proof‑of‑principle: devise explicit local deterministic (or stochastic) response functions $A_{i}(\lambda_{i},s_{i})$ that satisfy A1–A4 and reproduce the four GHZ stabilizer values. Measuring the triple‑product correlations in a simulated or tabletop setting and finding a violation of the pointwise product $+1$ would falsify our falsification. Conversely, failure to construct such functions supports the present verdict.

**(d) Engineering constraints.** The projection in Section 4.6 identifies the primary constraints for any simulation that attempts to verify the locality claim: (i) a maximum signal speed $v_{\max}$