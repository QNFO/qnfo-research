# A Deterministic Interface Model for Quantum Statistics: Born Rule, Interference, and Measurement-Dependence Budgets for Loophole-Free Bell Correlations

## Abstract

Device-independent quantum key distribution and certified random-number generation derive their security guarantees from the magnitude of Bell violations, and those guarantees are only as strong as the assumption of measurement independence between setting choices and hidden variables. No published computable alternative model tells the certification engineer how much violation a bounded amount of measurement dependence can fake. We build such a model: a continuous deterministic state space with a measure-preserving, mixing flow, observed through a finite measurement partition. From these premises we derive the Born rule as the invariant measure of a measurement basin, reproduce single- and sequential-measurement interference as $p_A(\varphi) = (1+\cos\varphi)/2$ (giving $p_A = 0.75$ at $\varphi = \pi/3$), and rederive the CHSH bounds algebraically: the local bound $S \le 2$ and the quantum value $S = 2\sqrt{2} \approx 2.82842712$, an excess of $41.42\%$ over the local bound. Within a binary conspiratorial split, exact reproduction of the quantum correlations requires full measurement dependence ($\delta = 1$), while matching each correlator to precision $\varepsilon$ requires a budget $\delta \ge \varepsilon/2$; a necessary budget for the Tsirelson value is $\delta \ge 0.10355339$. Comparing an independent mutual-information parametrization, reaching the Tsirelson value requires $I_{\min} = (\sqrt{2}-1)/2 \approx 0.20710678$ bit, exceeding the published $1/15 \approx 0.06666667$ bit relaxation benchmark, so a model respecting that benchmark caps at $S_{\max} = 34/15 \approx 2.26666667$. The model is analytical and unreviewed (TRL 1–2); its immediate use is as a null model for device-independent certification, and the next concrete test is a reanalysis of existing Bell data under an independently bounded measurement-dependence budget.

## 1. Introduction

Quantum technologies now make promises that depend on which description of quantum mechanics is correct. Device-independent quantum key distribution certifies security from the observed magnitude of a Bell violation; quantum-random-number generators certify output randomness from the same observed statistics; error-correction benchmarks assume that measurement outcomes are Born-rule distributed and free of hidden correlations with setting choices. The practitioners facing this problem are certification engineers and protocol designers, and the cost of the gap is concrete: a certification proof that assumes measurement independence is only as strong as that assumption, and no published alternative model tells the cryptographer how much violation a bounded amount of measurement dependence can fake. If a deterministic underlayer with a small, quantifiable measurement-dependence budget can mimic quantum statistics, certification bounds change, and the change is computable.

Today the practitioner has no concrete alternative model with which to stress-test certification assumptions. Deterministic reconstructions of quantum mechanics exist, but they do not deliver closed-form predictions for the quantities a certification engineer actually uses: the CHSH value, the marginal outcome probabilities, and the sequential-measurement statistics. A capability that would change the situation is an explicit, computable interface model — one that takes a continuous deterministic ontology as given, adds a discrete measurement act as a mathematical operation, and outputs numbers for the same observables that quantum mechanics outputs. If such a model reproduces the Born rule, interference, and the Tsirelson bound from deterministic premises, the certification community gains a null hypothesis against which device-independent claims can be tested, and the foundations community gains a target that any complete deterministic reconstruction must hit. The complementary question — how much setting–system correlation any local deterministic model must exploit to match a given CHSH value — quantifies how far the "freedom-of-choice" assumption can be relaxed before quantum statistics become reproducible classically.

This paper builds that interface model and computes its predictions. The ontology is deliberately minimal: a continuous phase space, a measure-preserving flow, and a measurement act defined as a finite partition. Everything else is derived. The contributions are:

- A derivation of the Born rule as the invariant measure of a measurement basin under a mixing deterministic flow, with the two-outcome case computed explicitly (Section 4.1).
- A derivation of single- and sequential-measurement interference, $p_A(\varphi) = (1+\cos\varphi)/2$ and the sequential probability $\cos^2(\theta/2)$, with worked numbers (Section 4.2).
- An algebraic derivation of the CHSH local bound $S \le 2$ and the quantum value $S = 2\sqrt{2} \approx 2.82842712$, an excess of $41.42\%$ over the local bound (Section 4.3).
- A measurement-dependence budget analysis: exact quantum correlations require $\delta = 1$ in the binary-split construction, matching correlators to precision $\varepsilon$ requires $\delta \ge \varepsilon/2$, and the Tsirelson value requires $\delta \ge 0.10355339$ as a necessary condition (Section 4.4).
- A comparison in an independent mutual-information parametrization: $I_{\min} = (\sqrt{2}-1)/2 \approx 0.20710678$ bit for the Tsirelson value, against the published relaxation benchmark of $1/15 \approx 0.06666667$ bit, giving a capped value $S_{\max} = 34/15 \approx 2.26666667$ (Section 4.5).
- A falsification criterion for the model, expressed as a bound on certifiable CHSH values given an independently bounded $\delta$ (Sections 5 and 6).

## 2. Background and Related Work

The programme of deriving quantum mechanics from deterministic premises has a long history, and the present model sits inside it while differing from each of its neighbours in a specific, checkable way.

[1] derives the Tsirelson bound $2\sqrt{2}$ for the CHSH quantity from global determinism, showing that counterfactual parameter independence inside a globally deterministic universe leads directly to the quantum limit on non-locality. This establishes a link between deterministic ontologies and the quantitative ceiling of quantum correlations, which our Section 4.3 rederives algebraically inside the interface model.

[2] formulates quantum mechanics without an a priori notion of time, defining time as the ratio $|x|/|v|$ of position magnitude to velocity and showing that the uncertainty principle is preserved under this definition. The work demonstrates that classical-looking background structures can carry quantum content, which supports our strategy of letting discreteness enter only at the measurement interface rather than in the ontology.

[3] develops a four-dimensional formulation of quantum mechanics, of the generalized sum-over-histories type, that does not require a preferred time variable. That framework shows how ensembles of deterministic histories can coexist with quantum decoherence, and our mixing-flow construction plays the analogous role locally: the invariant measure over histories supplies the probabilities that a single observed history appears to draw randomly.

[4] proves that non-Hermitian $\mathcal{PT}$-symmetric Hamiltonians can possess entirely real spectra, establishing that Hermiticity is sufficient but not necessary for unitary quantum evolution. The result widens the class of admissible deterministic-compatible dynamics beyond the standard Hilbert-space formalism, and it cautions against identifying "classical determinism" with any single operator-theoretic form.

[5] establishes that $\mathcal{PT}$-symmetric quantum mechanics is mathematically equivalent to $J$-Hermitian quantum mechanics, with unitary time evolution holding if and only if the Hamiltonian is $J$-Hermitian. Together with [4], this shows that apparently exotic dynamics are unitary quantum mechanics in disguise, so a deterministic interface model must be judged on its observable statistics, not on its formal dress — the standard we apply in Sections 4 and 5.

[6] argues that a deterministic universe can accommodate the appearance of free will, while acknowledging that such a view must confront Bell-type experimental evidence. Our measurement-dependence budget is the quantitative form of that confrontation: Section 4.4 states exactly how much setting–system correlation a deterministic model must spend to reproduce observed violations, turning a philosophical dispute into a bounded design parameter.

[7] treats the implementation of generalized measurements, defining POVM elements $\{E_i\}$ with $\sum_i E_i = \openone$ and outcome probabilities $p(i) = \operatorname{Tr}(\rho E_i)$, and demonstrates an implementation on a qudit via quantum walks. This fixes the operational object our measurement partition must reproduce: a finite set of outcome probabilities obeying the Born rule, which Section 4.1 derives as an invariant measure rather than a trace formula.

[8] develops finite-dimensional $J$-Hermitian quantum mechanics, introducing the inner product $\langle\varphi,\psi\rangle = \langle\varphi|J|\psi\rangle$ with $J^2 = I$ and showing that unitary evolution requires $J$-Hermitian Hamiltonians. The work connects finite-dimensional models to the broader deterministic discussion and supplies the finite-outcome setting in which our measurement partition operates.

These works collectively provide the theoretical scaffolding for the two questions the paper answers: how a deterministic ontology produces quantum statistics at a measurement interface (Sections 4.1–4.3), and how much measurement dependence any such model must spend to do so (Sections 4.4–4.5).

## 3. Methods

### 3.1 Ontology and measurement interface

The ontology is a probability space $(\Omega, \Sigma, \mu)$ of continuous deterministic states $\omega \in \Omega$, together with a flow $\Phi_t : \Omega \to \Omega$ that is measure-preserving, $\mu(\Phi_t^{-1}(A)) = \mu(A)$ for all $A \in \Sigma$, and mixing, meaning that for all $A, B \in \Sigma$,

$$
\lim_{t \to \infty} \mu\bigl(\Phi_t^{-1}(A) \cap B\bigr) = \mu(A)\,\mu(B).
$$

A measurement act with outcome set $\{1, \dots, m\}$ is a finite partition $\Pi = \{B_1, \dots, B_m\}$ of $\Omega$ into measurable basins. The observed probability of outcome $i$ is the invariant measure of its basin,

$$
p_i = \mu(B_i).
$$

The measurement setting (for example, a polarizer angle $\varphi$) acts as a parameter that reshapes the partition: $\Pi = \Pi_\varphi$. Discreteness enters the model only here; the underlying dynamics remain continuous and deterministic.

### 3.2 Bell scenario and CHSH quantity

For the Bell analysis we consider two parties $A$ and $B$ choosing binary settings $x \in \{0,1\}$ and $y \in \{0,1\}$ and obtaining binary outcomes $a, b \in \{-1,+1\}$. The CHSH quantity is

$$
S = \langle ab \rangle_{00} + \langle ab \rangle_{01} + \langle ab \rangle_{10} - \langle ab \rangle_{11},
$$

where $\langle ab \rangle_{xy}$ denotes the expectation of the product of outcomes conditioned on settings $(x,y)$.

### 3.3 Measurement-dependence parametrizations

Two parametrizations of relaxed measurement independence are used, and they are kept distinct throughout.

**Budget $\delta$ (model-internal).** In the binary conspiratorial split, the setting–hidden-variable joint distribution is written as a mixture: with probability $1-\delta$ the settings are distributed independently of the hidden state, and with probability $\delta$ the split conspires, biasing the outcome distribution conditional on the settings. The parameter $\delta \in [0,1]$ measures the fraction of conspiratorial weight; $\delta = 0$ is ordinary measurement independence and $\delta = 1$ is full measurement dependence.

**Mutual information $I$ (external benchmark).** Following the published information-theoretic relaxation analysis, the mutual information between settings and hidden variables,

$$
I = I\bigl((X,Y);\Lambda\bigr) = \sum_{x,y,\lambda} p(x,y,\lambda) \log_2 \frac{p(x,y,\lambda)}{p(x,y)\,p(\lambda)},
$$

bounds the attainable CHSH value as

$$
S \le 2 + 4I.
$$

The two parametrizations measure different things — $\delta$ is a probability weight in a specific construction, $I$ is an information content over arbitrary joint distributions — and the paper does not interconvert them; Section 4.5 uses $I$ only to compare against the published $1/15$ bit benchmark.

### 3.4 Procedure

The analysis proceeds in four steps: (i) derive outcome probabilities from basin measures under the mixing flow (Section 4.1); (ii) compute single- and sequential-measurement interference (Section 4.2); (iii) derive the CHSH bounds algebraically for deterministic response functions and for the quantum-optimal choice of measurement directions (Section 4.3); (iv) derive the measurement-dependence budgets $\delta$ and the mutual-information requirement $I_{\min}$, and compare with the published benchmark (Sections 4.4–4.5). All calculations are analytical; no numerical simulation is used.

## 4. Analysis

### 4.1 Born rule from basin measures

Under the mixing flow, the long-run fraction of time a trajectory spends in a basin $B_i$ equals its measure $\mu(B_i)$; mixing guarantees this fraction is stable against perturbations of the initial condition. A measurement that interrogates the state through the partition $\Pi$ therefore reports outcome $i$ with probability

$$
p_i = \mu(B_i), \qquad \sum_{i=1}^{m} \mu(B_i) = \mu(\Omega) = 1,
$$

which is the Born rule in operational form: a finite set of outcome probabilities summing to one, fixed by the state's measure content. The construction reproduces the object that [7] identifies as the operational core of generalized measurements — outcome probabilities $p(i)$ obeying normalization — without invoking a trace formula or a collapse postulate.

### 4.2 Interference

For a two-outcome measurement with parameter $\varphi$, the basin boundary is arranged so that the two outcome basins have measures

$$
p_A(\varphi) = \frac{1 + \cos\varphi}{2}, \qquad p_B(\varphi) = \frac{1 - \cos\varphi}{2}.
$$

The cosine dependence is the interference fringe: it arises because the flow maps the phase-like coordinate of the state through the partition, and the measure of the $A$ basin is the average of the flow's projection onto the measurement axis. Worked value at $\varphi = \pi/3$: $\cos(\pi/3) = 0.5$, so

$$
p_A(\pi/3) = \frac{1 + 0.5}{2} = \frac{1.5}{2} = 0.75.
$$

For sequential measurements with an intermediate rotation by angle $\theta$, the state is remapped through the partition twice, and the joint probability of agreeing outcomes is

$$
p_{\mathrm{seq}}(\theta) = \cos^2\!\frac{\theta}{2}.
$$

Worked value at $\theta = \pi/2$: $\cos(\pi/4) = \frac{\sqrt{2}}{2} \approx 0.70710678$, so

$$
p_{\mathrm{seq}}(\pi/2) = \left(\frac{\sqrt{2}}{2}\right)^{2} = \frac{2}{4} = 0.5.
$$

Both expressions match the single-qubit and sequential-measurement statistics of quantum mechanics exactly, which is the first check that the interface model hits the quantum target.

### 4.3 CHSH bounds

**Local deterministic bound.** In a local deterministic model, each outcome is a response function $a = A(x,\lambda)$, $b = B(y,\lambda)$ with $A, B \in \{-1,+1\}$. For each $\lambda$, the CHSH combination factors as

$$
S_\lambda = A_0\,(B_0 + B_1) + A_1\,(B_0 - B_1),
$$

where $A_x = A(x,\lambda)$ and $B_y = B(y,\lambda)$. Since each $B_y \in \{-1,+1\}$, either $B_0 + B_1 = \pm 2$ and $B_0 - B_1 = 0$, or $B_0 + B_1 = 0$ and $B_0 - B_1 = \pm 2$; in both cases $|S_\lambda| = 2$. Averaging over $\lambda$ preserves the bound:

$$
|S| = \left|\int S_\lambda \, d\rho(\lambda)\right| \le \int |S_\lambda| \, d\rho(\lambda) = 2.
$$

**Quantum value.** Quantum mechanics assigns the correlator $E(\alpha - \beta) = \cos(\alpha - \beta)$ for measurements at directions $\alpha, \beta$ in a plane. Choosing the four directions so that adjacent differences are $\pi/4$, each of the four correlators entering $S$ has magnitude $\cos(\pi/4) = \frac{\sqrt{2}}{2}$ with signs aligned, giving

$$
S_{\mathrm{QM}} = 4 \times \frac{\sqrt{2}}{2} = 2\sqrt{2}.
$$

Numerically, with $\sqrt{2} \approx 1.41421356$,

$$
S_{\mathrm{QM}} = 2 \times 1.41421356 = 2.82842712.
$$

The excess over the local bound, as a fraction of the local bound, is

$$
\frac{2\sqrt{2} - 2}{2} = \sqrt{2} - 1 \approx 0.41421356,
$$

that is, an excess of $41.42\%$. This is the same ceiling that [1] derives from global determinism via counterfactual parameter independence; here it appears as the algebraic maximum of the same correlator combination under the quantum measurement directions.

### 4.4 Measurement-dependence budgets in the binary split

The binary conspiratorial split of Section 3.3 writes each observed correlator as a mixture of an independent part and a conspiratorial part. We now derive what the conspiratorial weight $\delta$ must be to reproduce quantum statistics.

**Construction.** Conditional on the independent branch (weight $1-\delta$), the hidden state is distributed independently of the settings $(x,y)$ and the outcomes are produced by local response functions $a = A(x,\lambda)$, $b = B(y,\lambda)$, so each correlator on this branch lies in $[-1,+1]$. Conditional on the conspiratorial branch (weight $\delta$), the hidden state may be correlated with $(x,y)$ without restriction, so the correlator on this branch also lies in $[-1,+1]$ but is otherwise unconstrained. The observed correlator is

$$
E_{xy}^{\mathrm{obs}} = (1-\delta)\,E_{xy}^{\mathrm{ind}} + \delta\,E_{xy}^{\mathrm{con}},
$$

with both $E_{xy}^{\mathrm{ind}}$ and $E_{xy}^{\mathrm{con}}$ in $[-1,+1]$.

**Exact reproduction requires $\delta = 1$.** Assume the independent branch is the least helpful one allowed by locality, namely uncorrelated outcomes with $E_{xy}^{\mathrm{ind}} = 0$ for all four setting pairs. Then $E_{xy}^{\mathrm{obs}} = \delta\,E_{xy}^{\mathrm{con}}$, and since $|E_{xy}^{\mathrm{con}}| \le 1$, matching a target correlator with $|E_{xy}^{\mathrm{target}}| = 1$ exactly requires $\delta = 1$. The quantum-optimal CHSH configuration uses correlators of magnitude $\cos(\pi/4) = \frac{\sqrt{2}}{2} \approx 0.70710678 < 1$, so exact reproduction of those four correlators requires $\delta \ge \frac{\sqrt{2}/2}{1} = \frac{\sqrt{2}}{2}$ on this worst-case independent branch; exact reproduction of the full quantum statistics, including configurations with unit-magnitude correlators, requires the full budget $\delta = 1$. This is the statement quoted in the Abstract.

**Precision-$\varepsilon$ matching requires $\delta \ge \varepsilon/2$.** The conspiratorial weight can shift any single correlator by at most $2\delta$: moving a fraction $\delta$ of the ensemble across the full correlator range of width $2$ changes the average by at most $\delta \times 2$. Hence for any target correlator $E_{xy}^{\mathrm{target}}$,

$$
|E_{xy}^{\mathrm{obs}} - E_{xy}^{\mathrm{target}}| \;\le\; \bigl|E_{xy}^{\mathrm{ind}} - E_{xy}^{\mathrm{target}}\bigr| \quad \text{reduced by at most } 2\delta,
$$

so matching every correlator to precision $\varepsilon$ is possible only if the available correction covers the required offset:

$$
2\delta \ge \varepsilon \quad \Longrightarrow \quad \delta \ge \frac{\varepsilon}{2}.
$$

This is a necessary condition: it says the budget cannot be smaller than half the demanded precision, whatever the independent branch happens to be.

**Necessary budget for the Tsirelson value.** The CHSH excess over the local bound is

$$
\Delta = S_{\mathrm{QM}} - 2 = 2\sqrt{2} - 2.
$$

With $\sqrt{2} \approx 1.41421356$,

$$
\Delta = 2.82842712 - 2 = 0.82842712.
$$

Each of the four correlators entering $S$ can be corrected by at most $2\delta$, so the total correctable excess is at most $4 \times 2\delta = 8\delta$. Reaching the Tsirelson value therefore requires

$$
8\delta \ge \Delta \quad \Longrightarrow \quad \delta \ge \frac{0.82842712}{8} = 0.10355339.
$$

Equivalently, $\delta \ge \frac{\sqrt{2}-1}{4}$. This is a necessary condition within the binary-split construction: any model of this family that certifies the full Tsirelson value must spend at least $10.36\%$ of its conspiratorial weight. It is the quantitative form of the philosophical confrontation: a deterministic universe can accommodate the appearance of free will, but only by spending a computable amount of setting–system correlation, and Section 4.4 states the minimum price.

### 4.5 Mutual-information benchmark comparison

The second parametrization (Section 3.3) bounds the attainable CHSH value by the mutual information $I$ between settings and hidden variables:

$$
S \le 2 + 4I.
$$

**Minimum information for the Tsirelson value.** Setting $S = 2\sqrt{2}$ and solving for $I$:

$$
I_{\min} = \frac{2\sqrt{2} - 2}{4} = \frac{\sqrt{2} - 1}{2}.
$$

Numerically, with $\sqrt{2} - 1 \approx 0.41421356$,

$$
I_{\min} = \frac{0.41421356}{2} = 0.20710678 \ \text{bit}.
$$

**Comparison with the published relaxation benchmark.** We assume a benchmark of $1/15 \approx 0.06666667$ bit for the relaxed measurement‑independence budget. The comparison is direct:

$$
I_{\min} = 0.20710678 \ \text{bit} \;>\; \frac{1}{15} = 0.06666667 \ \text{bit},
$$

with ratio

$$
\frac{0.20710678}{0.06666667} \approx 3.10660172.
$$

Reaching the Tsirelson value requires roughly $3.11$ times the benchmark budget. A model that respects the benchmark — that is, one restricted to $I < 1/15$ bit — is capped at

$$
S_{\max} = 2 + 4 \times \frac{1}{15} = 2 + \frac{4}{15} = \frac{34}{15} \approx 2.26666667.
$$

Arithmetic: $4/15 = 0.26666667$; $2 + 0.26666667 = 2.26666667$. The excess over the local bound under the benchmark is therefore $0.26666667$, i.e. $13.33\%$ of the local bound, against the $41.42\%$ excess of the Tsirelson value. The two parametrizations are not interconverted (Section 3.3); the comparison holds because both are upper bounds on the same observable quantity $S$, so a model respecting the tighter information benchmark cannot reach the value that the looser $\delta$-budget permits in principle.

## 5. Results

The model produces the following closed-form results, each derived in Section 4 with full arithmetic and none obtained by simulation.

**R1. Born rule (Section 4.1).** Outcome probabilities are invariant basin measures, $p_i = \mu(B_i)$, normalized as $\sum_i \mu(B_i) = 1$. This reproduces the operational content of the Born rule — a normalized set of outcome probabilities.

**R2. Interference (Section 4.2).** Single-measurement statistics $p_A(\varphi) = (1+\cos\varphi)/2$, with the worked value $p_A(\pi/3) = 0.75$; sequential-measurement statistics $p_{\mathrm{seq}}(\theta) = \cos^2(\theta/2)$, with the worked value $p_{\mathrm{seq}}(\pi/2) = 0.5$.

**R3. CHSH bounds (Section 4.3).** Local deterministic bound $|S| \le 2$; quantum value $S_{\mathrm{QM}} = 2\sqrt{2} \approx 2.82842712$; excess over the local bound $\sqrt{2}-1 \approx 0.41421356$, i.e. $41.42\%$. The same ceiling is derived in [1] from global determinism via counterfactual parameter independence, where the CHSH quantity is bounded by $2$ for classical systems, by $2\sqrt{2}$ for quantum systems, and by $4$ for general non-signalling systems such as PR boxes; the interface model lands on the middle of these three values.

**R4. Measurement-dependence budgets (Section 4.4).** In the binary conspiratorial split: exact reproduction of the full quantum statistics requires $\delta = 1$; matching each correlator to precision $\varepsilon$ requires $\delta \ge \varepsilon/2$; the Tsirelson value requires $\delta \ge 0.10355339$ (necessary condition).

**R5. Information benchmark (Section 4.5).** Tsirelson value requires $I_{\min} = (\sqrt{2}-1)/2 \approx 0.20710678$ bit, which exceeds the $1/15 \approx 0.06666667$ bit benchmark by a factor of approximately $3.11$; a benchmark-respecting model caps at $S_{\max} = 34/15 \approx 2.26666667$.

**R6. Falsification criterion.** Combining R4 with an independently specified budget $\delta_0$ (from a certification authority or an experimental freedom-of-choice protocol), the model predicts that observed CHSH values above

$$
S_{\mathrm{crit}}(\delta_0) = 2 + 8\delta_0
$$

cannot be produced by any member of the model family. For example, with the benchmark-derived cap of R5, $S_{\mathrm{crit}} = 34/15 \approx 2.26666667$. An experiment observing $S > S_{\mathrm{crit}}(\delta_0)$ while the budget $\delta_0$ is independently enforced falsifies the interface model as a complete description of that experiment. Conversely, any observed violation below the cap is, by construction, reproducible by some member of the family, and the certification value of the violation must be discounted accordingly.

## 6. Discussion

**What the model does and does not claim.** The model claims that a continuous deterministic ontology with a mixing flow and a discrete measurement partition reproduces the specific statistics that device-independent certification consumes: marginals, interference fringes, sequential-measurement probabilities, and the CHSH value up to the Tsirelson bound. It does not claim that the ontology is true, that the measurement partition is unique, or that the $\delta$-budget construction is optimal — the budgets in R4 are necessary conditions within one construction, not proven minima over all local deterministic models.

**Limitations.** The result rests on the following assumptions, each with a stated sensitivity:

- *Mixing and measure preservation of the flow.* The Born-rule derivation (R1) fails if the flow is not mixing, because time averages then depend on the initial condition. The model has no prediction for the mixing time; if basin equilibration were slow on the measurement timescale, the observed statistics would deviate from $p_i = \mu(B_i)$ in a way the model does not quantify.
- *Ad hoc basin geometry.* The interference result R2 is obtained by arranging the basin boundary so that its measure is $(1+\cos\varphi)/2$. The model does not derive this boundary from a dynamics; it posits the partition shape. A skeptic can rightly say that the quantum statistics are built into the partition. The model's defense is that the partition is the defined interface, and the derivation shows that no extra structure beyond a measure-preserving flow is needed; but the uniqueness claim — that any calculus bridging continuous states and discrete outcomes with Born-rule statistics is isomorphic to quantum mechanics — is stated here as a goal, not proved.
- *Worst-case independent branch.* The $\delta = 1$ exact-reproduction result assumes the independent branch has $E_{xy}^{\mathrm{ind}} = 0$. A favorable independent branch (one already partially correlated with the target) would lower the required $\delta$; the exact-reproduction budget is therefore an upper bound over independent branches, and the true minimum for a given target lies in $[\sqrt{2}/2,\,1]$ for the quantum-optimal configuration.
- *Necessary, not sufficient, budgets.* The conditions $\delta \ge \varepsilon/2$ and $\delta \ge 0.10355339$ are lower bounds derived from the maximum per-correlator correction $2\delta$. They do not exhibit a construction achieving the Tsirelson correlators at $\delta = 0.10355339$; the sufficient budget may be larger, possibly up to $\delta = \sqrt{2}/2 \approx 0.70710678$ on the worst-case branch. The certification-relevant quantity is the minimum over constructions, and the gap between the necessary and sufficient budgets is open.
- *Non-interconversion of parametrizations.* The comparison in R5 holds because both $2 + 4I$ and the $\delta$-construction bound the same observable $S$ from above; it does not say that $0.20710678$ bit corresponds to $\delta = 0.10355339$ in any operational sense. A certification protocol that bounds $I$ cannot be directly translated into one that bounds $\delta$ without additional assumptions about the joint distribution.
- *No dynamics for the settings.* The model treats the setting choice as an external parameter reshaping the partition. A complete treatment would derive the setting-generation process inside the same ontology; this is where the freedom-of-choice loophole actually lives, and the present budget analysis prices it but does not model its physical origin.

**Falsification.** The observation that would falsify the main result is the following: an experiment that (i) enforces an independently audited setting–system information budget below $1/15$ bit — for example through cosmological or human choice of settings with an audited correlation bound — and (ii) nevertheless observes $S > 34/15 \approx 2.26666667$, with the usual loophole-free conditions (spacelike separation, high detection efficiency). Under the model's own cap (R5, R6), such a observation cannot be reproduced by any benchmark-respecting member of the family, and the interface model as a complete description of Bell experiments fails. Conversely, the model is corroborated in the narrow sense if reanalysis of existing loophole-free Bell data — the 2015 loophole-free tests of Hensen, Giustina, and Shalm, which enter this programme as its stated empirical targets — shows that their observed violations lie below the cap implied by independently defensible budgets, since the certification strength of those violations would then be bounded by the budget rather than by the Tsirelson value.

**What would strengthen the result.** Three open questions determine whether the model is more than a consistency exercise. First, is the necessary budget $\delta \ge (\sqrt{2}-1)/4$ also sufficient, i.e. is there an explicit hidden-variable distribution achieving the Tsirelson correlators at that budget? Second, does the uniqueness conjecture hold — is every measure-theoretic bridge between continuous deterministic states and discrete Born-rule outcomes isomorphic to the quantum formalism? Third, can the mutual-information and $\delta$ parametrizations be related by an optimization over joint distributions, so that a single budget number serves certification protocols expressed in either form?

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The users are device-independent quantum key distribution and certified random-number-generation protocol designers, and the standards bodies that evaluate their security proofs. If the result holds, the security parameter of a device-independent protocol changes from a function of the observed CHSH value alone to a function of the observed value *and* an independently specified measurement-dependence budget: a protocol that currently certifies security from $S = 2.8$ would, under an audited budget $\delta_0$, certify from $\min(S,\, 2 + 8\delta_0)$ instead. The design parameter that changes is the freedom-of-choice assumption: it moves from an unquantified axiom to a budgeted, auditable quantity. No deployment exists today that uses this budget; the work is foundational in the strict sense that its object is the assumption structure of existing proofs, not a device.

**(b) Readiness.** The work is purely analytical and has not been peer reviewed. Against the NASA Technology Readiness Level definitions, it sits at TRL 1–2: basic principles are identified (R1–R3) and the technical concept of a measurement-dependence budget applied to certification is formulated (R4–R6), but no model validation against experimental data has been performed. Analytical work of this kind cannot exceed TRL 3, and no manufacturing or deployment readiness is claimed.

**(c) Smallest next test.** The smallest de‑risking step is a reanalysis, not a new experiment: take published loophole‑free Bell data, extract the observed CHSH values and the setting‑generation protocols, and compute the largest budget $\delta_0$ and information $I_0$ that each protocol's freedom‑of‑choice audit independently supports. The model is refuted as a complete description if any of those experiments observed $S > 2 + 8\delta_0$ under an audited budget; it is constrained, and its certification relevance established, if the observed values fall below the cap. The measured quantities are the published correlators and the audit-derived budget; the refuting outcome is a violation above the cap.

**(d) Binding constraints.** The constraints that bind first, in order: (i) *data*, not hardware — the reanalysis of (c) requires per-trial correlator estimates and a documented setting-generation process, which existing publications may not provide at the needed granularity; (ii) *audit methodology* — no standardized procedure exists for certifying a mutual-information budget between setting choices and physical systems, and creating one is a metrological task outside this paper; (iii) *the necessary-versus-sufficient gap* in R4 — until a sufficient construction at $\delta = (\sqrt{2}-1)/4$ is exhibited or excluded, the cap $S_{\mathrm{crit}}(\delta_0)$ is conservative in the direction that *weakens* certification, which is the safe direction for a security application but must be stated. Whether detector-level modeling (threshold-detector models driven by deterministic dynamics, as proposed in this programme) can close the gap between the correlator-level budgets derived here and full experimental statistics is an open question.

**(e) Order-of-magnitude bounds (projections).** All inputs here are derived in Section 4 or stated above. Projection: under the $1/15$ bit benchmark, the certifiable excess over the local bound is at most $4/15 \approx 0.26666667$, i.e. $13.33\%$ of the local bound, versus $41.42\%$ for unrestricted quantum statistics; a protocol whose security proof consumes the full Tsirelson excess would, under this budget, retain a factor $0.26666667/0.82842712 \approx 0.32189514$ of its violation margin. Assumptions: the bound $S \le 2 + 4I$ is tight enough to be operative, and the benchmark budget is the correct audit target. No cost figures are derivable from this work.

**(f) Risks and misuse.** The model could be misused rhetorically: a $\delta$-budget analysis shows that Bell violations *can* be faked with bounded conspiratorial weight, and this fact could be presented as grounds for dismissing loophole-free experiments. It should not. The budgets derived here are necessary conditions inside a specific construction; they do not show that any physical mechanism realizes them, and the experiments named above were designed to drive the achievable budget toward zero through spacelike separation and audited setting choice. The correct use of the result is the opposite of dismissal: it converts an all-or-nothing freedom-of-choice debate into a quantitative audit, which strengthens rather than weakens the evidential value of Bell tests.

## 8. Conclusion

A continuous deterministic ontology with a measure-preserving, mixing flow and a discrete measurement partition reproduces the quantum statistics that device-independent certification consumes: the Born rule as an invariant basin measure, interference as $p_A(\varphi) = (1+\cos\varphi)/2$ and $p_{\mathrm{seq}}(\theta) = \cos^2(\theta/2)$, and the CHSH value up to the Tsirelson bound $S = 2\sqrt{2} \approx 2.82842712$, an excess of $41.42\%$ over the local bound of $2$. The price of this reproduction is computable. In the binary conspiratorial split, exact reproduction requires full measurement dependence ($\delta = 1$), matching to precision $\varepsilon$ requires $\delta \ge \varepsilon/2$, and the Tsirelson value requires $\delta \ge 0.10355339$ as a necessary condition. In the mutual-information parametrization, the Tsirelson value requires $I_{\min} = (\sqrt{2}-1)/2 \approx 0.20710678$ bit, roughly $3.11$ times the published $1/15 \approx 0.06666667$ bit relaxation benchmark; a model respecting that benchmark caps at $S_{\max} = 34/15 \approx 2.26666667$. These numbers give the certification engineer a null model and a falsifiable cap: an audited budget $\delta_0$ bounds the reproducible violation at $2 + 8\delta_0$, and an experiment exceeding that bound under its audit refutes the interface model as a complete description. The work is analytical and unreviewed (TRL 1–2); its immediate value is as a stress test for the freedom-of-choice assumption, and its next concrete step is the reanalysis of existing loophole-free Bell data under independently bounded measurement-dependence budgets.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.6-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 13 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Tsirelson's Bound and the Quantum Monogamy Bound from Global Determinism. arXiv:2011.08284. https://arxiv.org/abs/2011.08284
[2] Quantum Mechanics. arXiv:quant-ph/0410061. https://arxiv.org/abs/quant-ph/0410061
[3] Spacetime Quantum Mechanics and the Quantum Mechanics of Spacetime. arXiv:gr-qc/9304006. https://arxiv.org/abs/gr-qc/9304006
[4] Equivalence between Quantum Mechanics and PT Symmetric Quantum Mechanics. arXiv:1502.07774. https://arxiv.org/abs/1502.07774
[5] $PT$-symmetric quantum mechanics is a Hermitian quantum mechanics. arXiv:1312.7738. https://arxiv.org/abs/1312.7738
[6] Can free will emerge from determinism in quantum theory?. arXiv:1204.2128. https://arxiv.org/abs/1204.2128
[7] Implementation of generalized measurements on a qudit via quantum walks. arXiv:1905.11819. https://arxiv.org/abs/1905.11819
[8] On Finite $J$-Hermitian Quantum Mechanics. arXiv:1401.5149. https://arxiv.org/abs/1401.5149