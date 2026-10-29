# The Margolus-Levitin Bound as an Energy-Time Limit for Quantum Computation at the Landauer Scale: Derivation, Saturation Analysis, and a Joules-per-Compute Normalization for Cryogenic Controllers

## Abstract

Quantum speed limits bound how fast a quantum state can evolve, and the Margolus-Levitin (ML) bound sets the canonical floor: a system with mean energy $\langle H\rangle$ above its ground state needs at least $\tau \ge \pi\hbar/(2\langle H\rangle)$ to reach an orthogonal state. Hardware teams benchmarking cryogenic quantum controllers need an energy-per-operation figure, and it is unclear whether the ML bound, evaluated at the Landauer energy $k_B T\ln 2$, supplies a universal per-operation energy-time floor for that benchmark. This preprint re-derives the ML bound, extends it to arbitrary fidelity and mixed states using recent analytic results, and evaluates it numerically at cryogenic and room temperature. At $T = 10$ mK the Landauer energy is $9.57\times 10^{-26}$ J, giving $\tau_{\mathrm{ML}} = 1.73$ ns; at $T = 300$ K it gives $\tau_{\mathrm{ML}} = 5.77\times 10^{-14}$ s. We show that these intrinsic-register times are irrelevant to system-level energy cost: with a Carnot-limited cryostat removing controller heat from a 10 mK stage, each watt dissipated there costs $29{,}999$ W of wall power, so a proposed joules-per-compute normalization $C_{\mathrm{JPCUB}} = (P_{\mathrm{control}} + P_{\mathrm{cryo}})/f_{\mathrm{ops}}$ yields $3.0\times 10^{-5}$ J per logical operation under stated assumptions, about $3.1\times 10^{20}$ times the Landauer energy. The ML bound therefore constrains register dynamics but not the energy benchmark; the normalization fills that role.

## 1. Introduction

Teams designing control electronics for superconducting and spin-qubit processors face a concrete accounting problem: they must state how many joules a logical qubit operation costs, and no existing single bound gives them that number. The dominant energy sinks sit far from the qubit itself. Room-temperature electronics, cryogenic amplifiers, and the refrigerators that remove their heat dissipate power at rates many orders of magnitude above the thermodynamic floor of computation, and the gap between the floor and the practice is unquantified in most benchmark discussions. Until the gap is quantified, a designer cannot tell whether an proposed controller improvement matters at the level of the energy budget or is lost in the cooling overhead, and a benchmarking program cannot normalize energy per logical operation in a way that separates intrinsic limits from engineering overhead.

Two classical results frame the problem but do not solve it. The Landauer limit states that erasing one bit at temperature $T$ dissipates at least $k_B T \ln 2$ [3], and Bennett showed that logically reversible computation avoids that floor entirely [4]. The Margolus-Levitin (ML) bound states that a system with mean energy $\langle H\rangle$ above its ground state needs at least $\tau \ge \pi\hbar/(2\langle H\rangle)$ to evolve between orthogonal states [5]. If the ML bound were a universal per-operation energy-time limit at the Landauer scale, then the energy figure a benchmark needs would follow from thermodynamics alone. This paper shows that it is not: the bound constrains the intrinsic dynamics of the qubit register, while the energy cost of a real operation is set by control hardware and cooling, which the bound does not see. What changes if the result holds is that benchmarking programs can stop attributing system-level energy cost to the intrinsic register energy and adopt an explicit two-term normalization that names the dominant sinks.

The paper proceeds from a re-derivation of the ML bound through its modern extensions to a numerical evaluation at the Landauer scale and a proposed normalization for the QNFO joules-per-compute (JPCUB) benchmark program. The contributions are:

- A self-contained derivation of the ML bound $\tau \ge \pi\hbar/(2\langle H\rangle)$ from the cosine inequality $\cos x \ge 1 - 2x/\pi$, with the assumption behind the derivation stated explicitly (Section 3).
- A synthesis of the modern ML literature — arbitrary-fidelity extensions, saturation characterizations, observable bounds, and covariant forms — establishing what the bound does and does not claim (Sections 2 and 4).
- Numerical evaluation of the ML time at the Landauer energy for $T = 10$ mK and $T = 300$ K, with full arithmetic: $\tau_{\mathrm{ML}} = 1.73$ ns and $5.77\times 10^{-14}$ s respectively (Section 4).
- A Carnot-limited cooling-overhead calculation showing that $1$ W at a 10 mK stage costs $29{,}999$ W of wall power, and a worked JPCUB normalization giving $C_{\mathrm{JPCUB}} = 3.0\times 10^{-5}$ J per logical operation under stated assumptions (Sections 4 and 5).
- The conclusion that the ML bound is not a universal per-operation energy-time bound for quantum computation at the Landauer scale, with the specific role it does play stated precisely (Sections 5 and 6).

## 2. Background and Related Work

The ML bound sits inside a large literature on quantum speed limits (QSLs), which are lower bounds on the time a quantum transformation requires. This section places the bound among its relatives and identifies what each line of work contributes to the assessment that follows.

Margolus and Levitin's original result bounds orthogonalization time by the mean energy above the ground state, $\tau \ge (\pi/2)/(E - E_0)$ in units with $\hbar = 1$ [4 in the notation of the saturation analysis]. The Mandelstam-Tamm (MT) bound is the complementary classical result: it bounds the same time by the energy variance, $\tau \ge \pi/(2\Delta H)$ [1]. The two bounds are unified by taking the maximum of the two expressions; the phase-space treatment of the quantum-to-classical transition states the unified form explicitly as $\tau_{\mathrm{qsl}} = \max\{\pi\hbar/(2\Delta E),\ \pi\hbar/(2(\langle E\rangle - E_0))\}$ and notes that the ML bound can be viewed as a transition probability amplitude between two orthogonal states [6]. The unified envelope matters for the assessment below because a register with a narrow energy distribution may be MT-bound rather than ML-bound, so any claim that the ML bound is "the" speed limit of a register must be checked against the variance.

The bound has been extended well beyond the orthogonal, pure-state, time-independent case in which it was first proved. For initial and final states of arbitrary fidelity $\delta$, the extended ML bound replaces the constant $\pi/2$ with a fidelity-dependent function $\alpha(\delta)$, which equals $\pi/2$ at $\delta = 0$ and vanishes at $\delta = 1$; the extension has been derived analytically, shown to be tight in all dimensions, and interpreted geometrically as an extremal dynamical phase in a gauge fixed by the ground state [2]. A companion note shows that for the two-level family parametrized by $\xi \in [0,1]$, the lower and upper bounds $m(\delta) \le \alpha(\delta) \le M(\delta)$ on that function coincide, so the arbitrary-fidelity constant is exactly determined [3]. A separate analytic treatment re-proves the ML bound through a supporting-line inequality for the cosine, $\cos x \ge \cos\theta - (x-\theta)\sin\varphi(\theta)$, and shows that for every fidelity $\epsilon \in [0,1]$ there exists a state-Hamiltonian pair saturating the bound, so the bound is not merely tight in principle but attainable [7]. These tightness results matter here because they establish that the numerical ML times computed in Section 4 are achievable floors, not loose inequalities.

Saturation has been characterized structurally. A purification-based analysis proves that mixed-state saturation of the ML bound occurs precisely when the state's support is confined to the sum of two energy eigenspaces — the ground level and one excited level — with the consequence that the rank of the saturating state cannot exceed the ground-state degeneracy, which rules out faithful states [4]. This structural result is directly relevant to the register interpretation: a qubit driven between its ground and excited levels is exactly the two-eigenspace configuration that can saturate the bound, so the ML time of an ideal qubit is not an artifact of the pure-state derivation.

Two generalizations broaden the bound's scope. Covariant versions of the theorem address the fact that the operation count $\# \le 2E\tau/(\pi\hbar)$ implied by the bound is not Lorentz-invariant as written; a moving observer assigns the system average energy $E\gamma$ for a time $\tau\gamma$, giving $\#' \le 2E\gamma^2\tau/(\pi\hbar)$, and the resolution connects the operation bound to time dilation [5]. The operation-count form itself is the bridge from the bound to a per-operation rate, and Section 4 uses it. On the observable side, a recent mean-energy speed limit bounds the change of an expectation value $\langle A(t)\rangle$ quadratically in the fractional change, $T(\langle H\rangle - E_0) \ge C_\star \Delta^2/\sigma_A^2$, completing a $2\times 2$ classification of speed limits by what moves (state or observable) and which energy functional powers the bound (variance or mean energy); being quadratic, it is most constraining for large fractional changes, where the linear variance-based bounds are weakest [1]. This matters for control-hardware benchmarking because the quantities an experiment reads are expectation values, not fidelities.

On the thermodynamic side, Landauer established that irreversible erasure dissipates at least $k_B T\ln 2$ per bit [3], and Bennett proved that computation can be made logically reversible, so that the Landauer floor attaches to irreversibility rather than to computation as such [4]. The distinction drives the central argument of this paper: unitary gates are reversible and need not dissipate the Landauer energy, so identifying the ML driving energy with $k_B T\ln 2$ conflates a dynamical bound with a thermodynamic one.

Within the QNFO corpus, three works bear directly on the present assessment. The preprint under revision derives the ML bound, argues that it does not account for cryogenic control dissipation, and proposes the normalization $C_{\mathrm{JPCUB}} = (P_{\mathrm{control}} + P_{\mathrm{cryo}})/f_{\mathrm{ops}}$, where $P_{\mathrm{cryo}}$ is the equivalent power required by the cryostat to remove controller heat accounting for Carnot efficiency [8]. This paper sharpens that argument with explicit arithmetic and with the modern saturation and tightness results. The spin-chain testbed study places the decoherence time $T_2 = 1/\Gamma$ and the ML time $t_{\mathrm{ML}} = 1/(4f)$ on one computable scale and derives the crossover criterion $\Gamma = 4f$ separating the decoherence-bound regime, where added energy does not help, from the speed-limit-bound regime, where the excitation energy directly bounds the operation time; it also tabulates $t_{\mathrm{ML}}$ across four decades of excitation frequency, from $250$ ns at $1$ MHz to $250$ ps at $1$ GHz [9]. That crossover criterion is the register-level analogue of the system-level argument made here: in both cases the binding constraint must be identified before energy is spent. Finally, the stabilizer-learning analysis states the reporting convention adopted in this paper — every number is either computed with shown arithmetic or explicitly labeled a projection with stated assumptions [11] — and its treatment of asymptotic constants as assumptions rather than measurements is the model for the projection labels in Sections 4 and 5. The Planckian-dissipation work is cited for a complementary point: it derives a universal structural optimum $LCI_{\mathrm{opt}} = \ln(2\pi) \approx 1.83$ at which structural information flow balances Planckian dissipation, illustrating that dissipation floors in quantum systems can be mediated by structure rather than by energy alone [10]; the analogy motivates asking whether controller-side dissipation, like Planckian dissipation, is a structural rather than an energetic constraint.

The gap none of these works fills individually is a system-level energy-and-latency normalization for a physical qubit operation whose cost is dominated by room-temperature control and cryogenic cooling overhead. The JPCUB normalization assessed in Sections 4 and 5 is proposed for that gap.

## 3. Methods

The paper's method is analytical: derive the ML bound from first principles, import the modern tightness and saturation results as cited constraints, evaluate the bound numerically at the Landauer energy for specified temperatures, and construct the JPCUB normalization from a Carnot-limited cooling model. No experiment, measurement, or simulation is performed; every number is computed here with shown arithmetic or labeled a projection with stated assumptions.

**Derivation of the ML bound.** Consider a system with time-independent Hamiltonian $H$ and initial state $|\psi(0)\rangle = \sum_n c_n |n\rangle$, where $H|n\rangle = E_n|n\rangle$. We set the ground-state energy $E_0 = 0$ without loss of generality, so $\langle H\rangle = \sum_n |c_n|^2 E_n$ is the mean energy above the ground state. The evolved state is $|\psi(t)\rangle = \sum_n c_n e^{-iE_n t/\hbar}|n\rangle$, and the overlap with the initial state is

$$\langle\psi(0)|\psi(t)\rangle = \sum_n |c_n|^2 e^{-iE_n t/\hbar}.$$

Orthogonality at time $\tau$ requires $\langle\psi(0)|\psi(\tau)\rangle = 0$; taking the real part,

$$\sum_n |c_n|^2 \cos\!\left(\frac{E_n \tau}{\hbar}\right) = 0.$$

The derivation uses the inequality $\cos x \ge 1 - \frac{2}{\pi}x$, valid for $x \in [0, \pi/2]$, together with the assumption that $E_n\tau/\hbar \le \pi/2$ for all populated levels. Under that assumption,

$$0 = \sum_n |c_n|^2 \cos\!\left(\frac{E_n\tau}{\hbar}\right) \ge \sum_n |c_n|^2 \left(1 - \frac{2}{\pi}\frac{E_n\tau}{\hbar}\right) = 1 - \frac{2\tau}{\pi\hbar}\langle H\rangle,$$

and rearranging yields the ML bound:

$$\tau \ge \frac{\pi\hbar}{2\langle H\rangle}.$$

The assumption $E_n\tau/\hbar \le \pi/2$ is a restriction of the elementary derivation, not of the theorem: the analytic treatment of [7] proves the bound for all fidelities without that restriction, and the arbitrary-fidelity extension holds in all dimensions [2]. We use the elementary derivation for transparency and rely on the cited results for generality.

**Imported constraints.** Three cited results are used as constraints on the interpretation rather than re-derived: (i) the bound is tight and saturable for every fidelity $\epsilon \in [0,1]$ [7]; (ii) mixed-state saturation requires support on at most two energy eigenspaces, so a rank-$r$ saturating state requires $r$-fold ground degeneracy [4]; (iii) the unified speed limit is the maximum of the ML and MT expressions [6], so ML-bound claims are checked against the variance.

**Numerical evaluation.** The ML time is evaluated at the Landauer energy $E_{\mathrm{L}} = k_B T \ln 2$ for $T = 10$ mK and $T = 300$ K, using $\hbar = 1.054571817\times 10^{-34}$ J·s and $k_B = 1.380649\times 10^{-23}$ J/K. The register-level ML time is also evaluated in the frequency form $t_{\mathrm{ML}} = 1/(4f)$ for a two-level qubit with transition frequency $f$, which follows from $E = hf$ since $\pi\hbar/(2hf) = 1/(4f)$.

**Cooling-overhead model.** The cryogenic overhead is modeled as Carnot-limited: a refrigerator removing heat $P_{\mathrm{control}}$ from a stage at $T_{\mathrm{cold}}$ while rejecting to $T_{\mathrm{hot}}$ requires minimum input power $P_{\mathrm{cryo}} = P_{\mathrm{control}}(T_{\mathrm{hot}}/T_{\mathrm{cold}} - 1)$. Real refrigerators perform below Carnot; the Carnot value is a lower bound on $P_{\mathrm{cryo}}$, so all JPCUB figures computed with it are optimistic projections, labeled as such.

**Normalization.** The JPCUB energy per logical operation is

$$C_{\mathrm{JPCUB}} = \frac{P_{\mathrm{control}} + P_{\mathrm{cryo}}}{f_{\mathrm{ops}}},$$

with $f_{\mathrm{ops}}$ the rate of logical qubit operations [8]. Worked values use assumed controller powers and operation rates, stated at the point of use.

## 4. Analysis

This section carries out every computation with shown arithmetic. Constants: $\hbar = 1.054571817\times 10^{-34}$ J·s, $k_B = 1.380649\times 10^{-23}$ J/K, $\ln 2 = 0.6931472$.

**C1. Landauer energy at $T = 10$ mK.**

$$E_{\mathrm{L}} = k_B T \ln 2 = (1.380649\times 10^{-23}\ \mathrm{J/K})(0.010\ \mathrm{K})(0.6931472).$$

Step 1: $1.380649\times 10^{-23} \times 0.010 = 1.380649\times 10^{-25}$ J. Step 2: $1.380649\times 10^{-25} \times 0.6931472 = 9.56988\times 10^{-26}$ J.

$$E_{\mathrm{L}}(10\ \mathrm{mK}) = 9.57\times 10^{-26}\ \mathrm{J}.$$

**C2. ML time at the Landauer energy, $T = 10$ mK.** With $\pi\hbar = 3.14159265 \times 1.054571817\times 10^{-34} = 3.313035\times 10^{-34}$ J·s,

$$\tau_{\mathrm{ML}} = \frac{\pi\hbar}{2E_{\mathrm{L}}} = \frac{3.313035\times 10^{-34}}{2 \times 9.56988\times 10^{-26}} = \frac{3.313035\times 10^{-34}}{1.913976\times 10^{-25}} = 1.73107\times 10^{-9}\ \mathrm{s}.$$

$$\tau_{\mathrm{ML}}(10\ \mathrm{mK}) \approx 1.73\ \mathrm{ns}.$$

**C3. Landauer energy and ML time at $T = 300$ K.** Step 1: $1.380649\times 10^{-23} \times 300 = 4.141947\times 10^{-21}$ J. Step 2: $\times 0.6931472 = 2.87098\times 10^{-21}$ J. Step 3:

$$\tau_{\mathrm{ML}} = \frac{3.313035\times 10^{-34}}{2 \times 2.87098\times 10^{-21}} = \frac{3.313035\times 10^{-34}}{5.74196\times 10^{-21}} = 5.7690\times 10^{-14}\ \mathrm{s}.$$

$$\tau_{\mathrm{ML}}(300\ \mathrm{K}) \approx 5.77\times 10^{-14}\ \mathrm{s}.$$

The ratio of the two ML times is $1.73107\times 10^{-9} / 5.7690\times 10^{-14} = 3.0007\times 10^{4}$, which equals the temperature ratio $300/0.010 = 3.0\times 10^{4}$ as required by the inverse proportionality of $\tau_{\mathrm{ML}}$ to $T$ at fixed $k_B\ln 2$.

**C4. Frequency form for a driven qubit.** For a two-level system with transition frequency $f$, the level splitting is $E = hf$, so

$$\tau_{\mathrm{ML}} = \frac{\pi\hbar}{2hf} = \frac{1}{4f},$$

using $\pi\hbar/2h = \pi/(4\pi) = 1/4$. This reproduces the tabulated values of the spin-chain study [9]: at $f = 1$ MHz, $t_{\mathrm{ML}} = 1/(4\times 10^{6}) = 2.50\times 10^{-7}$ s $= 250$ ns; at $f = 1$ GHz, $t_{\mathrm{ML}} = 2.50\times 10^{-10}$ s $= 250$ ps. For a representative superconducting-qubit drive scale $f = 5$ GHz,

$$t_{\mathrm{ML}} = \frac{1}{4 \times 5\times 10^{9}} = 5.00\times 10^{-11}\ \mathrm{s} = 50\ \mathrm{ps}.$$

**C5. Operation-count form.** The covariant treatment of the ML theorem states the operation bound $\# \le 2E\tau/(\pi\hbar)$ for a system of average energy $E$ over a time $\tau$ [5]. The corresponding maximum orthogonalization-event rate is $2E/(\pi\hbar) = 1/(2\tau_{\mathrm{ML}})$. For the $f = 5$ GHz qubit of C4, $E = hf = 6.62607015\times 10^{-34} \times 5\times 10^{9} = 3.31304\times 10^{-24}$ J, and

$$\frac{2E}{\pi\hbar} = \frac{2 \times 3.31304\times 10^{-24}}{3.313035\times 10^{-34}} = 2.0000\times 10^{10}\ \mathrm{s}^{-1},$$

i.e. an event-rate ceiling of $2.0\times 10^{10}$ orthogonalization events per second, or $2f/\pi \approx 0.637f$ per the count form. The register is therefore dynamically capable of operation rates far above any plausible control-limited clock rate; the ML bound does not bind first at the register level for realistic drive scales.

**C6. Carnot cooling overhead.** With $T_{\mathrm{hot}} = 300$ K and $T_{\mathrm{cold}} = 0.010$ K,

$$\frac{T_{\mathrm{hot}}}{T_{\mathrm{cold}}} - 1 = \frac{300}{0.010} - 1 = 30{,}000 - 1 = 29{,}999.$$

So each watt of heat dissipated at the 10 mK stage requires at least $29{,}999$ W of refrigerator input power at room temperature:

$$P_{\mathrm{cryo}} = 29{,}999\, P_{\mathrm{control}} \quad (\text{Carnot lower bound}).$$

**C7. Worked JPCUB value (projection).** We assume $P_{\mathrm{control}} = 1.0$ mW of cryogenic-stage controller dissipation and $f_{\mathrm{ops}} = 1.0$ MHz of logical operations. Then

$$P_{\mathrm{cryo}} = 29{,}999 \times 1.0\times 10^{-3}\ \mathrm{W} = 29.999\ \mathrm{W},$$
$$P_{\mathrm{total}} = P_{\mathrm{control}} + P_{\mathrm{cryo}} = 1.0\times 10^{-3} + 29.999 = 30.000\ \mathrm{W},$$
$$C_{\mathrm{JPCUB}} = \frac{30.000\ \mathrm{W}}{1.0\times 10^{6}\ \mathrm{s}^{-1}} = 3.0\times 10^{-5}\ \mathrm{J\ per\ logical\ operation}.$$

This is a projection under the stated assumptions ($P_{\mathrm{control}}$, $f_{\mathrm{ops}}$, Carnot limit); real refrigerators perform below Carnot, so the true value is larger.

**C8. Ratio to the Landauer energy.**

$$\frac{C_{\mathrm{JPCUB}}}{E_{\mathrm{L}}(10\ \mathrm{mK})} = \frac{3.0\times 10^{-5}}{9.56988\times 10^{-26}} = 3.13\times 10^{20}.$$

The system-level energy per logical operation exceeds the Landauer energy at the operating temperature by a factor of order $10^{20}$ under the stated assumptions.

**C9. ML time at the Landauer energy versus register capability.** The ML time evaluated with $\langle H\rangle = E_{\mathrm{L}}(10\ \mathrm{mK})$ is $1.73$ ns (C2), while the same register driven at $f = 5$ GHz has $t_{\mathrm{ML}} = 50$ ps (C4), a factor $1.73107\times 10^{-9}/5.00\times 10^{-11} = 34.6$ shorter. The comparison shows that the Landauer energy is not the energy that powers the register's dynamics: the drive splitting $hf$ at $5$ GHz is $3.31304\times 10^{-24}$ J, which is $3.31304\times 10^{-24}/9.56988\times 10^{-26} = 34.6$ times the Landauer energy at 10 mK, matching the time ratio exactly as the inverse proportionality requires.

**C10. Crossover criterion at the register level.** The spin-chain study's criterion $\Gamma = 4f$ separates the decoherence-bound from the speed-limit-bound regime [9]. For the worked example of a chain dephasing at $\Gamma = 100$ MHz, the crossover frequency is $f_c = \Gamma/4 = 25$ MHz: the chain is speed-limit-bound above $25$ MHz of excitation scale and decoherence-bound below it. This criterion is algebraically exact given the exponential-dephasing idealization and the orthogonal-target assumption, as its source states.

## 5. Results

Every number below is computed with shown arithmetic in Section 4 or is explicitly labeled a projection with stated assumptions.

1. **ML bound derived.** $\tau \ge \pi\hbar/(2\langle H\rangle)$, from the cosine inequality under the stated spectral restriction, with generality restored by the all-fidelity analytic proofs [2], [7] (Section 3).

2. **Landauer-scale ML times.** At $T = 10$ mK, $E_{\mathrm{L}} = 9.57\times 10^{-26}$ J and $\tau_{\mathrm{ML}} = 1.73$ ns (C1–C2). At $T = 300$ K, $E_{\mathrm{L}} = 2.87\times 10^{-21}$ J and $\tau_{\mathrm{ML}} = 5.77\times 10^{-14}$ s (C3). The ratio of the times equals the temperature ratio $3.0\times 10^{4}$ exactly.

3. **Register-level ML times.** $t_{\mathrm{ML}} = 1/(4f)$: $250$ ns at $1$ MHz, $25$ ns at $10$ MHz, $2.5$ ns at $100$ MHz, $250$ ps at $1$ GHz [9], and $50$ ps at $5$ GHz (C4). The corresponding event-rate ceiling is $2E/(\pi\hbar) = 2.0\times 10^{10}\ \mathrm{s}^{-1}$ at $5$ GHz (C5).

4. **Cooling overhead.** At a 10 mK stage rejecting to 300 K, the Carnot lower bound on refrigerator input is $29{,}999$ W per watt dissipated at the stage (C6).

5. **JPCUB normalization (projection).** Under the assumptions $P_{\mathrm{control}} = 1.0$ mW, $f_{\mathrm{ops}} = 1.0$ MHz, and the Carnot limit, $C_{\mathrm{JPCUB}} = 3.0\times 10^{-5}$ J per logical operation (C7), which exceeds the Landauer energy at 10 mK by a factor $3.13\times 10^{20}$ (C8). Because the Carnot value is a lower bound on cooling power and real refrigerators perform below it, this figure is an optimistic floor on the true system-level cost.

6. **Main result.** The ML bound evaluated at the Landauer energy ($1.73$ ns at 10 mK) describes neither the register's actual dynamical floor ($50$ ps at a 5 GHz drive, a factor $34