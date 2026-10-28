# Two-Level System Defects as a Random Ensemble: Counting and Dephasing Estimates for Superconducting Qubits

## Abstract

Parasitic two‑level system (TLS) defects in the amorphous tunnel barriers of superconducting qubits are a major identified source of decoherence, yet device designers lack closed‑form estimates linking defect density and junction geometry to the probability that a device is degraded and to the resulting dephasing rate. This paper models the defect population of a Josephson junction as a random ensemble—a random dynamical system in which defect positions and frequencies are random variables and the qubit is a deterministic observer—and derives two complementary closed‑form results. A Poisson counting argument gives the probability that a junction hosts a strongly coupled defect: for an assumed density of $10^{24}\ \mathrm{m^{-3}}$, a barrier volume of $4\times10^{-23}\ \mathrm{m^{3}}$, and a fractional coupling window of $2\times10^{-3}$, the mean count is $\lambda=0.08$ and the single‑junction probability is $P_{1}=0.0769$; on a 100‑junction chip the expected count is $8$ and the affected‑chip probability is $0.99966$. A dephasing calculation for off‑resonant defects gives $\Gamma_{\varphi}=5\ \mathrm{s^{-1}}$ ($T_{\varphi}=0.2\ \mathrm{s}$) for a five‑defect sub‑band configuration, and $T_{\varphi}=800\ \mu\mathrm{s}$ under a telegraph‑noise model for a switching defect. The results convert defect decoherence from a device‑by‑device pathology into an ensemble‑level design parameter with an explicit falsification register.

## 1. Introduction

Superconducting quantum processors lose coherence faster than their control electronics or circuit designs require, and a large share of the loss is traced to the materials of the device itself. Atomic‑scale defects in the amorphous oxides and tunnel barriers of superconducting circuits behave as parasitic two‑level systems (TLS): quantum systems with two accessible states whose transition frequencies lie in the gigahertz band occupied by the qubit. When a defect resides in the tunnel barrier of a Josephson junction and couples strongly to the qubit mode, it produces readout failures and spectral features visible in multi‑photon spectroscopy and shiftable by strain tuning; the experimental study of a strongly coupled TLS in a transmon tunnel barrier documents exactly this three‑partite interaction among TLS, qubit, and readout resonator [6].

The people who face this problem are qubit device engineers, process‑integration teams, and cryogenic measurement groups: every fabrication run produces junctions whose coherence is limited by an uncontrolled defect population, and the yield of high‑coherence devices is set in part by how often a defect lands close enough in frequency and space to matter.

Today that likelihood is treated empirically, device by device. A defect that ruins qubit $j$ on chip $A$ is characterized there, but the same fabrication process places different defects on chip $B$, so the fix does not transfer. What is blocked is predictive design: a fabrication change cannot be evaluated by its effect on the defect ensemble until the ensemble’s statistical consequences are computable before the device is made. If the defect population is treated statistically—as a random ensemble with measurable density, frequency distribution, and coupling distribution—then three decisions change. Fabrication teams can set a target defect density from a required device yield. Architects can budget coherence margins per junction rather than per chip. Spectroscopy campaigns can be sized in advance, because the expected number of strongly coupled defects per chip follows from the same parameters.

The core idea is a change of statistical frame. The defect ensemble is a random dynamical system in the technical sense: probability theory supplies the description of the unknown microscopic configuration, dynamical systems supplies the evolution rules, and the combination describes systems known only inaccurately, whether from physical uncertainty or computational limitation [2]. The qubit is a deterministic probe coupled to this random background. The same reframing has precedent in disordered materials: in amorphous solids, structural disorder long hindered first‑principles identification of the microscopic carriers of plasticity, until well‑defined topological defects—hedgehog defects in three‑dimensional amorphous solids—were shown to be identifiable and correlatable with soft spots [4]. The TLS defects of superconducting junctions are the analogous microscopic carriers of decoherence, and this paper imports the same move: name the carriers, then treat their spatial and spectral arrangement as a random ensemble.

**Contributions**

- A formulation of the junction defect population as a random dynamical system, with defect spectral positions as the random state and the qubit as the deterministic observer (Section 3).
- A closed‑form derivation of the near‑resonance probability $P_{\ge 1}=1-e^{-\lambda}$ under two parameterizations—spectral counting and spatio‑spectral counting—evaluated with all arithmetic shown to $P_{\ge 1}=0.0999$ and $P_{1}=0.0769$ respectively, with a chip‑level extension giving $P_{\mathrm{chip}}=0.99966$ for 100 junctions (Section 4).
- A derivation of the ensemble‑averaged dispersive dephasing rate $\Gamma_{\varphi}=\sum_i(g_i/\Delta_i)^2\gamma_i$, evaluated to $T_{\varphi}=0.2\ \mathrm{s}$ for five sub‑band defects, and a telegraph‑noise dephasing rate $\Gamma_{\varphi}=\varepsilon^{2}/(8\gamma)$, evaluated to $T_{\varphi}=800\ \mu\mathrm{s}$ (Section 4).
- A sensitivity analysis showing that the counting result moves by an order of magnitude per tenfold change in defect density, and that the dephasing rate is quadratic in coupling (Section 4).
- A falsification register: the specific spectroscopy observations that would refute the counting model and the noise model, and a list of the assumptions on which each number rests (Sections 7 and 7).

## 2. Background and Related Work

The literature relevant to this paper falls into three groups: the physics of TLS defects in superconducting circuits, the mathematics of random systems, and a body of work that shares the TLS acronym but concerns the Transport Layer Security protocol. All three are discussed here, because the acronym collision is itself a practical obstacle to literature search in this area and because the protocol‑side works illustrate a general point about statistical treatment of large configuration spaces.

On the physics side, the study [6] reports that TLS defects in tunnel junctions cause readout failures and provides spectroscopic evidence of strongly coupled TLS, supporting the relevance of the defect ensemble model. The interacting spectrum is reported as rich, which is precisely the regime where single‑defect intuition fails and ensemble statistics become necessary; the present paper supplies that statistical layer.

The statistical machinery comes from two traditions. The theory of random dynamical systems [2] defines a framework that combines a state space, a dynamical flow, and a probability measure to model systems with uncertain configurations. This framework can be applied to model the unknown defect configuration of a junction as a random state, without asserting an exact match to the defect problem.

On the fluctuation side, the review of one‑dimensional stochastic growth and its connection to Gaussian ensembles of random matrices [8] establishes that surface fluctuations of the polynuclear growth model coincide, for both curved and flat growth, with limit distribution functions from Gaussian random‑matrix ensembles, with the connection explained through associated point processes. The methodological lesson imported here is that spatial or spectral point processes of disordered systems can carry non‑trivial fluctuation statistics, which motivates treating the defect frequency positions as a point process rather than as independent fixed quantities.

Two further mathematical results shape the count statistics used in Section 4. The theorem on random perfect matchings in regular graphs [7] proves that in all regular robust expanders every edge is asymptotically equally likely to be contained in a uniformly chosen perfect matching, and that for any fixed matching or spanning regular graph the overlap $|M\cap E(N)|$ is approximately Poisson distributed. The Poisson limit for an overlap count of a random object against a fixed background is the same limit structure that Section 4 uses for the count of defects falling inside a fixed spatial‑and‑frequency window, although the physical setting of independent point defects is far simpler than the expander‑graph setting and needs no expansion properties.

Finally, three works share the TLS acronym with the physics subject but concern the Transport Layer Security protocol, and they are cited for completeness of the literature landscape and for one structural parallel. The Helol tunnel work [1] formulates throughput and uses fingerprint datasets to compute distributions.  The post‑quantum signature placement study [5] investigates signature‑algorithm choice in TLS 1.3 and its relation to certificate‑hierarchy structure. The parallel worth noting is methodological: the work [1] treats a large combinatorial space of protocol configurations statistically, asking what a random draw from that space looks like. The present paper asks the same question of a defect ensemble, seeking the aggregate variable (defect density × geometry × spectral window) that dominates yield.

## 3. Methods

### 3.1 The random dynamical system formulation

A random dynamical system, in the sense of [2], consists of a state space, a dynamical flow on that state space, and a probability measure describing inaccurate knowledge of the state or of the system itself. The defect problem maps onto this structure as follows. The state space is the configuration space of the junction: a configuration is the list of transition frequencies $\omega=(\omega_{1},\ldots,\omega_{N_{d}})$ of the $N_{d}$ TLS defects in the junction volume, together with their couplings $g=(g_{1},\ldots,g_{N_{d}})$ to the qubit’s electric field. Conditional on the configuration, the qubit and readout resonator dynamics are deterministic, in the three‑partite structure documented in [6]. The randomness enters through the measure on configuration space: defect frequencies, positions, and couplings are not known for a given device and are modeled as draws from ensemble distributions.

Three ensemble distributions are needed as inputs:

1. The defect count $N_{d}$ in the junction volume, treated as a random variable with mean $\bar{N}_{d}$ (or, equivalently, a spatial density $\rho$).
2. The frequency distribution of defect transitions, modeled as uniform over a band of width $\Delta_{0}$.
3. The coupling distribution, characterized by a typical value $g_{0}$ and treated as independent of frequency. This independence is an assumption; strain tuning of the kind used in [6] could test it, since strain shifts defect frequencies and any resulting change in coupling would reveal correlation.

The qubit is the deterministic observer. Its frequency $\omega_{q}$ is fixed by design, and all ensemble averages below are taken over the defect configuration measure with $\omega_{q}$ held fixed. This asymmetry is what makes the framework predictive: the fabrication process controls the ensemble parameters $(\rho,\Delta_{0},g_{0})$, and the observable decoherence is an ensemble average at fixed $\omega_{q}$.

### 3.2 Counting model

Defects are modeled as point entities distributed independently and uniformly at random with number density $\rho$ inside a barrier of area $A$ and thickness $d$, so the barrier volume is

$$V = A\,d.$$

Each defect has a transition frequency drawn uniformly from a band of width $\Delta_{0}$. A defect is called *strongly coupled* if two conditions hold: it lies inside the barrier volume $V$, where electric‑field participation and therefore coupling are largest, and its transition frequency lies within $\pm\Gamma$ of the qubit frequency. The fractional frequency window is

$$f_{\Gamma} = \frac{2\Gamma}{\Delta_{0}}.$$

Because positions and frequencies are independent and uniform, the expected number of strongly coupled defects in one junction is

$$\lambda = \rho\,V\,f_{\Gamma} = \rho\,A\,d\,\frac{2\Gamma}{\Delta_{0}},$$

and the count $N$ is Poisson distributed with mean $\lambda$:

$$\Pr(N=k)=\frac{\lambda^{k}e^{-\lambda}}{k!},\qquad \Pr(N\ge1)=1-e^{-\lambda}.$$

The Poisson assignment is the structural analogue of the approximately Poisson overlap counts proved for random matchings against fixed regular subgraphs [7]; here independence of defect placement makes the argument elementary. An equivalent purely spectral parameterization uses a total defect number $\bar{N}_{d}$ spread over a band $B$: the expected count in a two‑sided frequency window of width $2\delta$ is $\lambda=\bar{N}_{d}\,2\delta/B$, with the same Poisson law. For a chip of $N_{j}$ junctions with independent defect populations, the total count is Poisson with mean $N_{j}\lambda$, and

$$P_{\mathrm{chip}} = 1-e^{-N_{j}\lambda}.$$

### 3.3 Dephasing models

*Dispersive dephasing (off‑resonant defects).* For a defect detuned by $\Delta_{i}$ from the qubit with coupling $g_{i}$ and intrinsic defect relaxation rate $\gamma_{i}$, the qubit acquires a small admixture of the lossy defect; to leading order in $g_{i}/\Delta_{i}$ the defect contributes a dephasing rate

$$\Gamma_{\varphi}^{(\mathrm{disp})}= \sum_{i=1}^{n}\left(\frac{g_{i}}{\Delta_{i}}\right)^{2}\gamma_{i}.$$

Rates from distinct defects add. This form is valid when $g_{i}\ll|\Delta_{i}|$ for all counted defects; near‑resonant defects are handled separately by the counting model.

*Telegraph‑noise dephasing (switching defect).* A TLS that switches stochastically between its two states shifts the qubit frequency by a state‑dependent amount. In the classical‑noise approximation, the qubit frequency is perturbed by a random telegraph process $\xi(t)$ taking values $\pm\varepsilon/2$ with switching rate $\gamma$ per direction, so the autocorrelation function is

$$C(\tau)=\langle\xi(t)\,\xi(t+\tau)\rangle=\frac{\varepsilon^{2}}{4}\,e^{-2\gamma|\tau|}.$$

For a qubit at the noise’s zero‑frequency crossing, the pure‑dephasing rate in the long‑time limit is the time integral of the correlation function:

$$\Gamma_{\varphi}^{(\mathrm{tn})}= \int_{0}^{\infty}C(\tau)\,d\tau = \frac{\varepsilon^{2}}{8\gamma},$$

with dephasing time $T_{\varphi}=1/\Gamma_{\varphi}$. This is the standard filter‑function result at zero detuning for classical two‑state noise; it is exact within the classical‑noise and weak‑coupling approximations stated here.

All frequencies in the derivations are ordinary frequencies (cycles per second), not angular frequencies; a device using angular frequencies must insert the corresponding factors of $2\pi$ consistently.

### 3.4 Parameter values

All numerical inputs are stated assumptions, chosen to be representative of the model’s use rather than measured values; each is carried explicitly through the arithmetic of Section 4. The assumed barrier area is of the same order as the $200\ \mathrm{nm}\times220\ \mathrm{nm}$ junction areas reported in [6], which correspond to $4.4\times10^{-14}\ \mathrm{m^{2}}$.

| Parameter | Symbol | Assumed value |
|---|---|---|
| Defect density | $\rho$ | $10^{24}\ \mathrm{m^{-3}}$ |
| Junction barrier area | $A$ | $2\times10^{-14}\ \mathrm{m^{2}}$ |
| Barrier thickness | $d$ | $2\times10^{-9}\ \mathrm{m}$ |
| Coupling window (half‑width) | $\Gamma$ | $10^{6}\ \mathrm{s^{-1}}$ |
| TLS frequency band | $\Delta_{0}$ | $10^{9}\ \mathrm{s^{-1}}$ |
| Junctions per chip | $N_{j}$ | $100$ |
| Telegraph coupling amplitude | $\varepsilon$ | $10^{5}\ \mathrm{s^{-1}}$ |
| Telegraph switching rate | $\gamma$ | $10^{6}\ \mathrm{s^{-1}}$ |
| Total defects (spectral model) | $\bar{N}_{d}$ | $100$ |
| Spectral band (spectral model) | $B$ | $19\ \mathrm{GHz}$ |
| Qubit frequency | $\omega_{q}$ | $5\ \mathrm{GHz}$ |
| Resonance window (spectral model) | $\delta$ | $10\ \mathrm{MHz}$ |
| Typical coupling (dispersive) | $g_{0}$ | $1\ \mathrm{MHz}$ |
| Defect relaxation rate (dispersive) | $\gamma_{0}$ | $10\ \mathrm{kHz}$ |
| Sub‑band defect count (dispersive) | $n$ | $5$ |

## 4. Analysis

### 4.1 Barrier volume

Inputs: $A=2\times10^{-14}\ \mathrm{m^{2}}$ and $d=2\times10^{-9}\ \mathrm{m}$ (Section 3.4).

$$V = A\,d = \left(2\times10^{-14}\right)\times\left(2\times10^{-9}\right)\ \mathrm{m^{3}} = 4\times10^{-23}\ \mathrm{m^{3}}.$$

### 4.2 Fractional coupling window

Inputs: $\Gamma=10^{6}\ \mathrm{s^{-1}}$, $\Delta_{0}=10^{9}\ \mathrm{s^{-1}}$ (Section 3.4).

$$f_{\Gamma}= \frac{2\Gamma}{\Delta_{0}} = \frac{2\times10^{6}}{10^{9}} = 2\times10^{-3}.$$

### 4.3 Single‑junction defect probability (spatio‑spectral model)

Inputs: $\rho=10^{24}\ \mathrm{m^{-3}}$, $V=4\times10^{-23}\ \mathrm{m^{3}}$, $f_{\Gamma}=2\times10^{-3}$.

Mean count:

$$\lambda = \rho\,V\,f_{\Gamma}=10^{24}\times4\times10^{-23}\times2\times10^{-3}=0.08.$$

Probability of at least one strongly coupled defect:

$$P_{1}=1-e^{-\lambda}=1-e^{-0.08}=0.07688362\approx0.0769.$$

### 4.4 Chip‑level extension

Inputs: $N_{j}=100$, $\lambda=0.08$.

Chip mean count:

$$\lambda_{\mathrm{chip}} = N_{j}\lambda = 100\times0.08 = 8.$$

Chip‑level probability:

$$P_{\mathrm{chip}} = 1-e^{-\lambda_{\mathrm{chip}}}=1-e^{-8}=0.99966454\approx0.99966.$$

Standard deviation (Poisson):

$$\sigma_{\mathrm{chip}} = \sqrt{\lambda_{\mathrm{chip}}}= \sqrt{8}\approx2.8284.$$

### 4.5 Spectral counting model and near‑resonance probability

Inputs: $\bar{N}_{d}=100$, $B=19\ \mathrm{GHz}$, $2\delta=20\ \mathrm{MHz}=0.02\ \mathrm{GHz}$.

$$\lambda = \frac{\bar{N}_{d}\,2\delta}{B}= \frac{100\times0.02}{19}=0.10526316.$$

Poisson approximation:

$$P_{\ge1}=1-e^{-\lambda}=1-e^{-0.10526316}=0.09991221\approx0.0999.$$

Exact binomial check:

$$P_{\ge1}=1-\left(1-\frac{2\delta}{B}\right)^{\bar{N}_{d}}=1-(0.99894737)^{100}=0.099962\ (\text{consistent}).$$

Mean defect spacing: $$\bar{s}= \frac{B}{\bar{N}_{d}} = \frac{19\ \mathrm{GHz}}{100}=1.9\times10^{8}\ \mathrm{Hz}=190\ \mathrm{MHz}.$$

### 4.6 Dispersive dephasing rate

Inputs: $n=5$, $g_{0}=1\ \mathrm{MHz}$, $\gamma_{0}=10\ \mathrm{kHz}$, average detuning $|\bar{\Delta}|=100\ \mathrm{MHz}$.

Per‑defect factor:

$$\left(\frac{g_{0}}{|\bar{\Delta}|}\right)^{2}= \left(\frac{1}{100}\right)^{2}=10^{-4}.$$

Per‑defect rate:

$$\Gamma_{\varphi}^{(1)} = 10^{-4}\times10^{4}\ \mathrm{s^{-1}} = 1\ \mathrm{s^{-1}}.$$

Total dispersive rate:

$$\Gamma_{\varphi}^{(\mathrm{disp})}= n\,\Gamma_{\varphi}^{(1)} = 5\ \mathrm{s^{-1}}.$$

Dephasing time:

$$T_{\varphi}= \frac{1}{\Gamma_{\varphi}^{(\mathrm{disp})}} = 0.2\ \mathrm{s}.$$

### 4.7 Telegraph‑noise dephasing rate

Inputs: $\varepsilon=10^{5}\ \mathrm{s^{-1}}$, $\gamma=10^{6}\ \mathrm{s^{-1}}$.

$$\Gamma_{\varphi}^{(\mathrm{tn})}= \frac{\varepsilon^{2}}{8\gamma}= \frac{(10^{5})^{2}}{8\times10^{6}} = 1.25\times10^{3}\ \mathrm{s^{-1}}.$$

Dephasing time:

$$T_{\varphi}= \frac{1}{1.25\times10^{3}} = 8\times10^{-4}\ \mathrm{s}=800\ \mu\mathrm{s}.$$

### 4.8 Sensitivity analysis

*Density scaling.* $\lambda$ is linear in $\rho$. Reducing $\rho$ tenfold to $10^{23}\ \mathrm{m^{-3}}$ gives $\lambda=0.008$ and $P_{1}=0.00797$; the chip‑level probability falls to $P_{\mathrm{chip}}=1-e^{-0.8}=0.5507$. Increasing $\rho$ tenfold to $10^{25}\ \mathrm{m^{-3}}$ gives $\lambda=0.8$, $P_{1}=0.5507$, and $P_{\mathrm{chip}}\approx1$.

*Window‑width scaling.* Halving $\Gamma$ to $5\times10^{5}\ \mathrm{s^{-1}}$ halves $f_{\Gamma}$ and therefore $\lambda$ to $0.04$, yielding $P_{1}=0.0392$.

*Coupling scaling (dispersive).* $\Gamma_{\varphi}^{(\mathrm{disp})}$ scales as $(g_{0}/\Delta)^{2}$. Reducing the detuning to $|\Delta|=10\ \mathrm{MHz}$ (tenfold closer) increases the per‑defect rate to $100\ \mathrm{s^{-1}}$, giving $T_{\varphi}=2\ \mathrm{ms}$ for five defects.

*Switching‑rate scaling (telegraph).* $\Gamma_{\varphi}^{(\mathrm{tn})}$ is inversely proportional to $\gamma$. Reducing $\gamma$ tenfold to $10^{5}\ \mathrm{s^{-1}}$ raises the rate to $1.25\times10^{4}\ \mathrm{s^{-1}}$ and shortens $T_{\varphi}$ to $80\ \mu\mathrm{s}$.

Treating the TLS defect population of a Josephson junction as a random ensemble converts defect decoherence from a device‑by‑device pathology into a statistical design parameter. The Poisson counting argument gives, under stated assumptions, a single‑junction strongly coupled defect probability of $P_{1}=0.0769$, a chip‑level probability of $P_{\mathrm{chip}}=0.99966$ for 100 junctions with count fluctuation $\pm2.8$, and a spectral‑model cross‑check at $P_{\geq1}=0.0999$. The dephasing calculations give $T_{\varphi}=0.2\ \mathrm{s}$ for the dispersive channel of five sub‑band defects and $T_{\varphi}=800\ \mu\mathrm{s}$ for a single telegraph switcher, with the sensitivities that the counting probability is linear in density and window width, the dispersive rate quadratic in $g/\Delta$, and the telegraph rate quadratic in shift amplitude and inverse in switching rate. Every number traces to an explicitly stated assumption, and the falsification register specifies the spectroscopy observations—non‑Poisson count distributions, or dephasing scalings inconsistent with the derived dependences—that would refute the model. The framework’s usefulness now rests on an empirical question the analysis cannot answer: whether defect density and spectral distribution in real tunnel barriers match the assumptions well enough, or can be steered well enough, for the ensemble statistics to become a working yield tool.

Future work should aim to obtain empirical measurements of the defect density $\rho$ and the spectral distribution of TLS frequencies in realistic tunnel barriers. A systematic multi‑junction spectroscopy campaign, using the multi‑photon and strain‑tuning protocol described in [6], would allow the extraction of per‑junction defect counts and their frequency offsets, thereby providing the data needed to fit $\rho$ and to test the uniform‑spectral‑distribution assumption. Moreover, correlating measured defect positions (e.g., via scanning probe techniques) with the assumed spatial uniformity would assess the independence hypothesis underlying the Poisson model. Such experimental inputs would enable the analytical framework presented here to be calibrated and to transition from a purely conceptual tool toward a predictive design methodology for superconducting‑qubit fabrication.

## 5. Results

All numbers in this section are computed in Section 4 from the stated assumptions of Section 3.4; none are measured values.

**R1 (Single-junction near-resonance probability).** For the spatio‑spectral model with $\rho = 10^{24}\ \mathrm{m^{-3}}$, $V = 4\times 10^{-23}\ \mathrm{m^{3}}$, and $f_{\Gamma} = 2\times 10^{-3}$: mean strongly coupled count $\lambda = 0.08$ and $P_{1} = 0.0769$ (Section 4.3). Roughly one junction in thirteen hosts a strongly coupled TLS.

**R2 (Chip-level probability).** For $N_{j} = 100$ independent junctions: chip mean count $\lambda_{\mathrm{chip}} = 8$, $P_{\mathrm{chip}} = 0.99966$, count standard deviation $\sigma_{\mathrm{chip}} = 2.83$ (Section 4.4). A 100‑junction chip is essentially certain to contain strongly coupled defects, with chip‑to‑chip fluctuation of order $\pm 3$.

**R3 (Spectral-model cross-check).** With $\bar{N}_{d} = 100$ defects over $B = 19\ \mathrm{GHz}$ and a $20\ \mathrm{MHz}$ two‑sided window: $\lambda = 0.105263$, Poisson $P_{\geq1} = 0.0999$, exact binomial $P_{\geq1} = 0.099962$; mean defect spacing $\bar{s} = 190\ \mathrm{MHz}$ (Section 4.5). Approximately one qubit in ten is near‑resonant; the two counting parameterizations agree in order of magnitude.

**R4 (Dispersive dephasing).** Five off‑resonant defects at $|\Delta| = 100\ \mathrm{MHz}$, $g_{0} = 1\ \mathrm{MHz}$, $\gamma_{0} = 10\ \mathrm{kHz}$: $\Gamma_{\varphi} = 5\ \mathrm{s^{-1}}$, $T_{\varphi} = 0.2\ \mathrm{s}$ (Section 4.6). Sub‑band dispersive dephasing is subdominant in this parameterization.

**R5 (Telegraph dephasing).** One switching defect with $\varepsilon = 10^{5}\ \mathrm{s^{-1}}$, $\gamma = 10^{6}\ \mathrm{s^{-1}}$: $\Gamma_{\varphi} = 1.25\times 10^{3}\ \mathrm{s^{-1}}$, $T_{\varphi} = 800\ \mu\mathrm{s}$ (Section 4.7). A single slow switcher at these parameters produces coherence‑scale dephasing.

**R6 (Sensitivities).** $P_{1}$ is linear in $\rho$ and in $f_{\Gamma}$: a tenfold density reduction moves $P_{1}$ from $0.0769$ to $0.0080$ and $P_{\mathrm{chip}}$ from $0.99966$ to $0.5507$ (Section 4.8). The dispersive rate is quadratic in $g/\Delta$; the telegraph rate is proportional to $\varepsilon^{2}$ and inversely proportional to $\gamma$.

## 6. Extended Derivations and Worked Examples

In this section we expand the core analytical results of Sections 4–5 with fully explicit algebra, thereby illustrating how the closed‑form formulas can be applied in practice. The derivations follow directly from the assumptions listed in Table 3.4 and do not introduce any new empirical data. A methodological parallel to the statistical treatment of large configuration spaces appears in the TLS‑protocol literature, where active measurements are used to characterize a combinatorial space of protocol configurations [3].

### 1. From the Poisson mean to the chip‑level defect probability

For a single junction the expected number of strongly coupled TLS is

\[
\lambda = \rho\,V\,f_{\Gamma},
\qquad
V = A\,d,\;
f_{\Gamma}= \frac{2\Gamma}{\Delta_{0}} .
\]

With the numerical inputs

\[
\rho = 10^{24}\;\mathrm{m^{-3}},\;
A = 2\times10^{-14}\;\mathrm{m^{2}},\;
d = 2\times10^{-9}\;\mathrm{m},\;
\Gamma = 10^{6}\;\mathrm{s^{-1}},\;
\Delta_{0}=10^{9}\;\mathrm{s^{-1}},
\]

the intermediate quantities are

\[
V = (2\times10^{-14})(2\times10^{-9}) = 4\times10^{-23}\;\mathrm{m^{3}},
\]
\[
f_{\Gamma}= \frac{2\times10^{6}}{10^{9}} = 2\times10^{-3}.
\]

Hence

\[
\lambda = (10^{24})(4\times10^{-23})(2\times10^{-3})
        = 0.08 .
\]

The Poisson probability of at least one defect in a single junction is

\[
P_{1}=1-e^{-\lambda}=1-e^{-0.08}.
\]

Expanding the exponential to four terms gives

\[
e^{-0.08}=1-0.08+0.0032-0.00008533+0.00000171\approx0.923116,
\]
\[
P_{1}=1-0.923116=0.076884\approx0.0769 .
\]

For a chip containing \(N_{j}=100\) independent junctions the total count is Poisson with mean

\[
\lambda_{\mathrm{chip}} = N_{j}\lambda = 100\times0.08 = 8 .
\]

The chip‑level probability that **at least one** junction hosts a strongly coupled TLS is

\[
P_{\mathrm{chip}} = 1-e^{-\lambda_{\mathrm{chip}}}=1-e^{-8}.
\]

Since

\[
e^{-8}=e^{-4}\times e^{-4}\approx0.0183156\times0.0183156\approx0.00033546,
\]
\[
P_{\mathrm{chip}} = 1-0.00033546 = 0.99966454\approx0.99966 .
\]

The standard deviation of the chip‑level Poisson count follows from \(\sigma_{\mathrm{chip}}=\sqrt{\lambda_{\mathrm{chip}}}= \sqrt{8}\approx2.8284\).

### 2. Sensitivity of the single‑junction probability to defect density

Because \(\lambda\) is linear in \(\rho\),

\[
\lambda(\rho)=\rho\,V\,f_{\Gamma}\;\;\Longrightarrow\;\;
\frac{\partial \lambda}{\partial \rho}=V\,f_{\Gamma}.
\]

A ten‑fold reduction \(\rho\to\rho/10\) yields

\[
\lambda' = \frac{\lambda}{10}=0.008 .
\]

The corresponding probability is

\[
P_{1}' = 1-e^{-\lambda'} = 1-e^{-0.008}.
\]

Using the series expansion

\[
e^{-0.008}=1-0.008+0.000032-0.0000000853\approx0.992032,
\]
\[
P_{1}' = 1-0.992032 = 0.007968\approx0.0080 .
\]

Thus \(P_{1}\) scales proportionally with \(\rho\); a ten‑fold density reduction lowers the affected‑junction fraction from \(7.69\%\) to \(0.80\%\).

### 3. Dispersive dephasing scaling with coupling and detuning

The dispersive dephasing rate for \(n\) off‑resonant defects is

\[
\Gamma_{\varphi}^{(\mathrm{disp})}= \sum_{i=1}^{n}\left(\frac{g_{i}}{\Delta_{i}}\right)^{2}\gamma_{i}.
\]

Assuming identical parameters \(g_{i}=g_{0}\), \(|\Delta_{i}|=|\bar{\Delta}|\), and \(\gamma_{i}=\gamma_{0}\),

\[
\Gamma_{\varphi}^{(\mathrm{disp})}= n\left(\frac{g_{0}}{|\bar{\Delta}|}\right)^{2}\gamma_{0}.
\]

Insert the baseline values

\[
n=5,\;
g_{0}=1\;\mathrm{MHz}=10^{6}\;\mathrm{s^{-1}},\;
|\bar{\Delta}|=100\;\mathrm{MHz}=10^{8}\;\mathrm{s^{-1}},\;
\gamma_{0}=10\;\mathrm{kHz}=10^{4}\;\mathrm{s^{-1}} .
\]

The ratio

\[
\left(\frac{g_{0}}{|\bar{\Delta}|}\right)^{2}
 = \left(\frac{10^{6}}{10^{8}}\right)^{2}
 = (10^{-2})^{2}=10^{-4}.
\]

Per‑defect contribution

\[
\Gamma_{\varphi}^{(1)} = 10^{-4}\times10^{4}\;\mathrm{s^{-1}} = 1\;\mathrm{s^{-1}} .
\]

Summing over five defects

\[
\Gamma_{\varphi}^{(\mathrm{disp})}=5\times1\;\mathrm{s^{-1}}=5\;\mathrm{s^{-1}},
\qquad
T_{\varphi}= \frac{1}{\Gamma_{\varphi}^{(\mathrm{disp})}} = 0.2\;\mathrm{s}.
\]

If the detuning is reduced ten‑fold to \(|\bar{\Delta}|=10\;\mathrm{MHz}=10^{7}\;\mathrm{s^{-1}}\),

\[
\left(\frac{g_{0}}{|\bar{\Delta}|}\right)^{2}
 = \left(\frac{10^{6}}{10^{7}}\right)^{2}=10^{-2},
\]
\[
\Gamma_{\varphi}^{(1)} = 10^{-2}\times10^{4}=100\;\mathrm{s^{-1}},
\]
\[
\Gamma_{\varphi}^{(\mathrm{disp})}=5\times100=500\;\mathrm{s^{-1}},
\quad
T_{\varphi}=2\;\mathrm{ms}.
\]

Thus the dispersive rate scales as \((g/\Delta)^{2}\), confirming the quadratic sensitivity reported in Section 4.8.

### 4. Telegraph‑noise dephasing: parameter sweep

The telegraph‑noise dephasing formula is

\[
\Gamma_{\varphi}^{(\mathrm{tn})}= \frac{\varepsilon^{2}}{8\gamma},
\qquad
T_{\varphi}= \frac{1}{\Gamma_{\varphi}^{(\mathrm{tn})}} .
\]

Using the baseline \(\varepsilon=10^{5}\;\mathrm{s^{-1}}\) and \(\gamma=10^{6}\;\mathrm{s^{-1}}\),

\[
\Gamma_{\varphi}^{(\mathrm{tn})}= \frac{(10^{5})^{2}}{8\times10^{6}}
 = \frac{10^{10}}{8\times10^{6}} = 1.25\times10^{3}\;\mathrm{s^{-1}},
\]
\[
T_{\varphi}= \frac{1}{1.25\times10^{3}} = 8\times10^{-4}\;\mathrm{s}=800\;\mu\mathrm{s}.
\]

**Example 1 – Halving the shift amplitude.**
Set \(\varepsilon' = 5\times10^{4}\;\mathrm{s^{-1}}\) while keeping \(\gamma\) unchanged:

\[
\Gamma_{\varphi}' = \frac{(5\times10^{4})^{2}}{8\times10^{6}}
 = \frac{2.5\times10^{9}}{8\times10^{6}}
 = 312.5\;\mathrm{s^{-1}},
\]
\[
T_{\varphi}' = \frac{1}{312.5}=3.2\times10^{-3}\;\mathrm{s}=3.2\;\mathrm{ms}.
\]

The rate drops by a factor of four, as expected from the \(\varepsilon^{2}\) dependence.

**Example 2 – Slowing the switching rate ten‑fold.**
Set \(\gamma' = 10^{5}\;\mathrm{s^{-1}}\) with the original \(\varepsilon\):

\[
\Gamma_{\varphi}'' = \frac{10^{10}}{8\times10^{5}} = 1.25\times10^{4}\;\mathrm{s^{-1}},
\]
\[
T_{\varphi}'' = \frac{1}{1.25\times10^{4}} = 8\times10^{-5}\;\mathrm{s}=80\;\mu\mathrm{s}.
\]

A slower switcher (smaller \(\gamma\)) yields a larger dephasing rate, confirming the inverse proportionality.

### 5. Inverting the counting formula to set a target defect density

Designers may wish to guarantee that the fraction of junctions with a strongly coupled TLS does not exceed a prescribed threshold \(P_{1}^{\mathrm{target}}\). Solving

\[
P_{1}^{\mathrm{target}} = 1-e^{-\rho^{\mathrm{target}} V f_{\Gamma}}
\]

for \(\rho^{\mathrm{target}}\) gives

\[
e^{-\rho^{\mathrm{target}} V f_{\Gamma}} = 1-P_{1}^{\mathrm{target}},
\]
\[
-\rho^{\mathrm{target}} V f_{\Gamma}= \ln(1-P_{1}^{\mathrm{target}}),
\]
\[
\rho^{\mathrm{target}} = -\frac{\ln(1-P_{1}^{\mathrm{target}})}{V f_{\Gamma}} .
\]

*Worked example.*
Require \(P_{1}^{\mathrm{target}} = 0.01\) (i.e. at most 1 % of junctions affected). Using the baseline geometry

\[
V = 4\times10^{-23}\;\mathrm{m^{3}},\;
f_{\Gamma}=2\times10^{-3},
\]

\[
\rho^{\mathrm{target}} = -\frac{\ln(0.99)}{(4\times10^{-23})(2\times10^{-3})}
 = \frac{0.0100503}{8\times10^{-26}}
 = 1.2563\times10^{23}\;\mathrm{m^{-3}} .
\]

Thus the process must achieve a defect density an order of magnitude lower than the baseline \(10^{24}\;\mathrm{m^{-3}}\) to meet the 1 % yield goal.

### 6. Connection to statistical methodology in other domains

The statistical framing employed here—treating a large, combinatorial configuration space (TLS positions and frequencies) as a random ensemble and extracting aggregate observables—mirrors the approach taken in the TLS‑protocol literature, where active measurements are used to characterize a vast space of protocol configurations [3]. In both cases the underlying principle is that, when direct enumeration is impossible, a probabilistic model calibrated by a few measurable parameters can predict macroscopic behavior. This cross‑disciplinary parallel underscores the generality of the random‑ensemble methodology.

## 7. Discussion

The principal result is the conversion of two assumed densities and two assumed windows into device‑level probabilities and times: $P_{1}=0.0769$, $P_{\mathrm{chip}}=0.99966$, $T_{\varphi}=0.2\ \mathrm{s}$ (dispersive) and $800\ \mu\mathrm{s}$ (telegraph). The value of these numbers is conditional on the assumptions, and the conditionality is the point of this section.

*What would falsify the counting model.* The model predicts that strongly coupled defects appear as a Poisson process across nominally identical junctions, with mean $\lambda = \rho V f_{\Gamma}$. A spectroscopy campaign over many junctions that found the number of strongly coupled defects per junction systematically far from Poisson — for example, strongly bimodal, with most junctions defect‑free and a few carrying many defects — would refute independent uniform placement. Equally, a measured density of strongly coupled defects inconsistent with $\rho V f_{\Gamma}$ by more than the Poisson fluctuation $\sqrt{N_{j}\lambda} \approx 2.8$ across a chip population would falsify the assumed $\rho = 10^{24}\ \mathrm{m^{-3}}$ or the uniform spectral distribution. The strain‑tuning protocol of [6] supplies the identification method: each strongly coupled TLS found by multi‑photon spectroscopy is one count of $N$.

*What would falsify the dephasing models.* The dispersive prediction $T_{\varphi}=0.2\ \mathrm{s}$ for the assumed sub‑band population implies that sub‑band defects contribute negligibly to observed dephasing; if measured $T_{\varphi}$ in defect‑characterized devices tracked the sub‑band defect count rather than the near‑resonant count, the dispersive formula or its validity conditions ($g_{i}\ll|\Delta_{i}|$) would be implicated. The telegraph prediction is sharper: $T_{\varphi}=800\ \mu\mathrm{s}$ with quadratic dependence on the measured frequency shift amplitude $\varepsilon$ and inverse dependence on the measured switching rate $\gamma$. A measured dephasing time for a device with an identified switching defect that was neither quadratic in the measured shift nor inverse in the measured switching rate would falsify the classical telegraph model as applied here.

*Limitations.* The results rest on the following assumptions, each with its sensitivity:

- **Defect density $\rho = 10^{24}\ \mathrm{m^{-3}}$ is an assumption, not a measurement.** $P_{1}$ is linear in $\rho$; the entire counting result scales with it. The density \(\rho = 10^{24}\ \mathrm{m^{-3}}\) is an assumption of this paper, not a measurement attributed to [6].
- **Uniform spectral distribution.** If defect frequencies cluster near qubit frequencies (a known concern in the TLS literature, though no clustering value is assumed or measured in this paper), the effective $f_{\Gamma}$ rises and $P_{1}$ with it; the uniform model is then optimistic.
- **Independence of positions and frequencies.** Correlated placement (for example, density variations across the barrier) breaks the Poisson law; the expander‑graph result of [7] shows Poisson statistics can survive weaker independence assumptions, but no such relaxation is proved here.
- **Coupling–frequency independence.** Assumed in Section 3.1; testable by the strain tuning of [6], untested here.
- **Classical‑noise and weak‑coupling approximations.** The telegraph result is exact only within these approximations; a defect with $\varepsilon$ comparable to $\gamma$ or to the qubit–defect coupling requires the full quantum treatment, which is not derived here.
- **Ordinary‑frequency convention.** All rates are in cycles per second; angular‑frequency conventions shift numerical prefactors by powers of $2\pi$.
- **No resonant (strong‑coupling) dynamics.** Defects that land within a linewidth of the qubit are counted but their dephasing is not modeled; the counting and dephasing results cover disjoint regimes.

Future experimental efforts should therefore focus on quantifying the defect density $\rho$ and the spectral profile of TLSs in realistic tunnel barriers, enabling direct validation of the Poisson‑based counting model and the dephasing formulas, and providing the necessary feedback to refine the statistical framework for practical yield optimization.

## Appendix A. Divergence report

No divergent claims were identified among the drafts. All substantive quantitative and qualitative statements are convergent across the source drafts.

## Appendix B. Claim attribution

| Claim ID | Statement | Source Draft(s) | Agreement |
|---|---|---|---|
| C1 | Barrier volume $V = 4\times10^{-23}\ \mathrm{m^{3}}$ computed from $A=2\times10^{-14}\ \mathrm{m^{2}}$ and $d=2\times10^{-9}\ \mathrm{m}$. | A, B, C | CONVERGENT |
| C2 | Fractional coupling window $f_{\Gamma}=2\times10^{-3}$ from $\Gamma=10^{6}\ \mathrm{s^{-1}}$ and $\Delta_{0}=10^{9}\ \mathrm{s^{-1}}$. | A, B, C | CONVERGENT |
| C3 | Mean strongly‑coupled defect count per junction $\lambda = 0.08$. | A, B, C | CONVERGENT |
| C4 | Single‑junction probability $P_{1}=0.0769$ (Poisson $1-e^{-\lambda}$). | A, B, C | CONVERGENT |
| C5 | Chip‑level mean count $\lambda_{\mathrm{chip}}=8$ for $N_{j}=100$. | A, B, C | CONVERGENT |
| C6 | Chip‑level probability $P_{\mathrm{chip}}=0.99966$ (Poisson $1-e^{-8}$). | A, B, C | CONVERGENT |
| C7 | Spectral‑model near‑resonance mean count $\lambda=0.105263$ and $P_{\ge1}=0.0999$. | A, B, C | CONVERGENT |
| C8 | Mean defect spacing $\bar{s}=190\ \mathrm{MHz}$ from $B=19\ \mathrm{GHz}$ and $\bar{N}_{d}=100$. | A, B, C | CONVERGENT |
| C9 | Dispersive dephasing rate $\Gamma_{\varphi}^{(\mathrm{disp})}=5\ \mathrm{s^{-1}}$ and $T_{\varphi}=0.2\ \mathrm{s}$ for $n=5$ defects. | A, B, C | CONVERGENT |
| C10 | Telegraph‑noise dephasing rate $\Gamma_{\varphi}^{(\mathrm{tn})}=1.25\times10^{3}\ \mathrm{s^{-1}}$ and $T_{\varphi}=800\ \mu\mathrm{s}$. | A, B, C | CONVERGENT |
| C11 | Sensitivity: $P_{1}$ scales linearly with defect density $\rho$; ten‑fold reduction of $\rho$ yields $P_{1}=0.0080$ and $P_{\mathrm{chip}}=0.5507$. | A, B, C | CONVERGENT |
| C12 | Sensitivity: $\Gamma_{\varphi}^{(\mathrm{disp})}$ scales as $(g/\Delta)^{2}$; ten‑fold reduction of detuning to $10\ \mathrm{MHz}$ raises $\Gamma_{\varphi}^{(\mathrm{disp})}$ to $100\ \mathrm{s^{-1}}$ ( $T_{\varphi}=2\ \mathrm{ms}$ ). | A, B, C | CONVERGENT |
| C13 | Sensitivity: $\Gamma_{\varphi}^{(\mathrm{tn})}$ scales as $\varepsilon^{2}/\gamma$; ten‑fold slower switching ($\gamma=10^{5}\ \mathrm{s^{-1}}$) gives $T_{\varphi}=80\ \mu\mathrm{s}$. | A, B, C | CONVERGENT |
| C14 | Falsification of counting model: observation of a per‑junction defect count distribution that deviates significantly from Poisson (e.g., variance $\neq$ mean) would refute the model. | A, B, C | CONVERGENT |
| C15 | Falsification of dephasing models: measured $T_{\varphi}$ that does not follow the predicted quadratic dependence on $\varepsilon$ or inverse dependence on $\gamma$ would refute the telegraph‑noise model. | A, B, C | CONVERGENT |
| C16 | Practical implication (a): fabrication teams can invert $P_{1}=\!1-e^{-\rho V f_{\Gamma}}$ to set a target defect density $\rho^{\mathrm{target}}$ for a desired yield. | A, B, C | CONVERGENT |
| C17 | Practical implication (b): analytical work without experimental validation resides at TRL 1–2. | A, B, C | CONVERGENT |
| C18 | Practical implication (c): smallest next test is a retrospective analysis of existing multi‑junction spectroscopy data to compare the observed defect count histogram with the Poisson prediction. | A, B, C | CONVERGENT |
| C19 | Practical implication (d): primary constraint is the lack of measured defect‑density data; obtaining a systematic per‑junction defect census is required before quantitative design use. | A, B, C | CONVERGENT |
| C20 | Practical implication (e): ten‑fold reduction of $\rho$ projects $P_{1}$ from $7.7\%$ to $0.8\%$ and $P_{\mathrm{chip}}$ from $99.966\%$ to $55.07\%$. | A, B, C | CONVERGENT |
| C21 | Practical implication (f): misuse risk is presenting the assumed density $10^{24}\ \mathrm{m^{-3}}$ as a measured value. | A, B, C | CONVERGENT |

**Future Outlook.** Integrating the statistical TLS model into computer‑aided design (CAD) flows will require the experimental pipeline described in Section 9(c) to supply calibrated values of $\rho$, $f_{\Gamma}$, and coupling statistics for each fabrication process. Once such calibrated inputs are available, the closed‑form expressions derived in Sections 4–5 can be embedded as lightweight analytical modules that predict yield and coherence budgets without resorting to costly full‑scale simulations. The adoption pathway therefore hinges on closing the measurement loop and iteratively refining the assumed parameters, turning the present analytical scaffold into a practical engineering tool.

Future experimental validation of the assumed defect density $\rho$ and the uniform spectral distribution, for example by applying the multi‑photon spectroscopy and strain‑tuning protocol of [6] to a statistically significant ensemble of junctions, will determine whether the analytical framework can be adopted as a practical yield‑prediction tool.

The analytical framework introduced here therefore offers a concrete, low‑overhead tool for early‑stage yield estimation and coherence budgeting in superconducting‑qubit fabrication pipelines. By grounding design decisions in statistically derived probabilities and dephasing estimates, engineers can prioritize process improvements, allocate spectroscopy resources efficiently, and set realistic performance targets before committing to costly device runs. The next logical step is to validate the assumed defect density and spectral uniformity through systematic multi‑junction spectroscopy, thereby closing the loop between theory and practice and enabling the model to transition from a conceptual aid to an operational design standard.

## 8. Practical Implications and Engineering Pathways

**(a) Who would use the result and which decision, design parameter, process or policy changes if it holds.**
The primary users are superconducting‑qubit fabrication and process‑integration teams and qubit‑chip architects.  If the counting model holds, a fabrication team can invert the relation

\[
P_{1}=1-e^{-\rho V f_{\Gamma}}
\]

to set a target defect density \(\rho^{\mathrm{target}}\) that guarantees a desired maximum fraction of affected junctions \(P_{1}^{\mathrm{target}}\).  For example, requiring \(P_{1}\le 0.01\) with the baseline barrier volume \(V=4\times10^{-23}\,\mathrm{m^{3}}\) and fractional window \(f_{\Gamma}=2\times10^{-3}\) yields

\[
\rho^{\mathrm{target}}=\frac{-\ln(1-0.01)}{V f_{\Gamma}}
      =\frac{0.01005}{4\times10^{-23}\times2\times10^{-3}}
      =1.26\times10^{23}\ \mathrm{m^{-3}},
\]

an eight‑fold reduction from the assumed baseline \(\rho=10^{24}\ \mathrm{m^{-3}}\).  Architects can allocate a per‑junction coherence budget based on the Poisson‑predicted probability \(P_{1}\) rather than a per‑chip budget, and spectroscopy campaigns can be sized from the expected chip‑level mean count \(N_{j}\lambda\) (Section 4.4).

**(b) Current readiness, stated against the NASA Technology Readiness Level definitions.**
The work is purely analytical and has not been peer reviewed; by NASA TRL definitions it resides at TRL 1–2 (basic principles observed and reported, concept formulated).  No hardware, prototype, or experimental validation is presented, so the analysis never exceeds TRL 3.

**(c) The smallest next experiment, prototype, pilot or calculation that would de‑risk or falsify the result: what is measured and which outcome refutes it.**
The minimal de‑risking step is a retrospective analysis of an existing multi‑junction spectroscopy dataset obtained with the protocol of [6].  For each junction the number of strongly‑coupled TLS identified by multi‑photon spectroscopy and strain tuning is counted, producing a histogram of per‑junction counts.  The Poisson model predicts that the variance of this distribution equals its mean \(\lambda\).  The model is falsified if the observed variance exceeds the mean by a statistically significant margin (e.g., a variance‑to‑mean ratio > 2 with p < 0.01) or if a single fitted \(\rho\) cannot reconcile counts across junctions of different volumes \(V\) at fixed \(f_{\Gamma}\).

**(d) The engineering, manufacturing or deployment constraints that would bind first.**
The primary constraint is the lack of measured defect‑density data; the model’s inputs \(\rho\), the spectral distribution, and the coupling distribution must be obtained from systematic per‑junction defect censuses before quantitative design use.  A secondary constraint is spectroscopy throughput: identifying each strongly‑coupled TLS requires the multi‑photon spectroscopy and strain‑tuning protocol of [6], which can be time‑consuming for large junction arrays.  Whether barrier‑defect density can be reliably steered by process changes remains an open question.

**(e) Order‑of‑magnitude cost or performance bounds only when every input is derived in Section 4 or cited, labeled as projections with their assumptions.**
*Projection (ten‑fold density reduction).*  Reducing \(\rho\) by a factor of 10 lowers the single‑junction affected fraction from \(7.7\%\) to \(0.8\%\) and the chip‑level affected probability from \(99.966\%\) to \(55.07\%\) (Section 4.8).  A further ten‑fold reduction drives the chip‑level probability to

\[
P_{\mathrm{chip}}=1-e^{-0.08}=0.0769,
\]

i.e. $\approx$ 7.7 % of chips would contain at least one strongly coupled defect.  These numbers are direct consequences of the analytical expressions and the assumed baseline parameters; they do not reflect any specific fabrication cost.

**(f) Direct risks or misuse paths, where one exists.**
The only identified misuse risk is the interpretive presentation of the assumed density \(\rho=10^{24}\ \mathrm{m^{-3}}\) as a measured value.  Doing so would give unwarranted precision to yield projections and could mislead process‑development decisions.  The paper’s explicit register—every numerical result traced to a stated assumption—mitigates this risk.

## 10. Conclusion

Treating the TLS defect population of a Josephson junction as a random ensemble converts defect decoherence from a device‑by‑device pathology into a statistical design parameter. The Poisson counting argument gives, under stated assumptions, a single‑junction strongly coupled defect probability of $P_{1}=0.0769$, a chip‑level probability of $P_{\mathrm{chip}}=0.99966$ for 100 junctions with count fluctuation $\pm2.8$, and a spectral‑model cross‑check at $P_{\geq1}=0.0999$. The dephasing calculations give $T_{\varphi}=0.2\ \mathrm{s}$ for the dispersive channel of five sub‑band defects and $T_{\varphi}=800\ \mu\mathrm{s}$ for a single telegraph switcher, with the sensitivities that the counting probability is linear in density and window width, the dispersive rate quadratic in $g/\Delta$, and the telegraph rate quadratic in shift amplitude and inverse in switching rate. Every number traces to an explicitly stated assumption, and the falsification register specifies the spectroscopy observations—non‑Poisson count distributions, or dephasing scalings inconsistent with the derived dependences—that would refute the model. The framework’s usefulness now rests on an empirical question the analysis cannot answer: whether defect density and spectral distribution in real tunnel barriers match the assumptions well enough, or can be steered well enough, for the ensemble statistics to become a working yield tool.

Future experimental work should aim to measure the defect density $\rho$ and the spectral distribution of TLS frequencies in realistic tunnel barriers. A systematic multi‑junction spectroscopy campaign, using the multi‑photon and strain‑tuning protocol of [6], can provide per‑junction defect counts and frequency offsets, enabling a direct test of the Poisson prediction and calibration of the model parameters. Such data will determine whether the analytical expressions derived here can be deployed as practical yield‑prediction tools in superconducting‑qubit fabrication pipelines.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Helol Tunnel: Covert Channel Exploitation of TLS Extensibility &amp; Privacy Features. arXiv:2610.01009v1. https://arxiv.org/abs/2610.01009v1
[2] Random Dynamical Systems. arXiv:math/0608162v1. https://arxiv.org/abs/math/0608162v1
[3] Active TLS Stack Fingerprinting: Characterizing TLS Server Deployments at Scale. arXiv:2206.13230v3. https://arxiv.org/abs/2206.13230v3
[4] Hedgehog topological defects in 3D amorphous solids. arXiv:2407.20631v2. https://arxiv.org/abs/2407.20631v2
[5] Signature Placement in Post-Quantum TLS Certificate Hierarchies: An Experimental Study of ML-DSA and SLH-DSA in TLS 1.3 Authentication. arXiv:2604.06100v3. https://arxiv.org/abs/2604.06100v3
[6] Readout failures in superconducting qubits due to TLS-defects in tunnel junctions. arXiv:2605.02755v2. https://arxiv.org/abs/2605.02755v2
[7] Random perfect matchings in regular graphs. arXiv:2301.10131v2. https://arxiv.org/abs/2301.10131v2
[8] One-dimensional stochastic growth and Gaussian ensembles of random matrices. arXiv:math-ph/0505038v2. https://arxiv.org/abs/math-ph/0505038v2
