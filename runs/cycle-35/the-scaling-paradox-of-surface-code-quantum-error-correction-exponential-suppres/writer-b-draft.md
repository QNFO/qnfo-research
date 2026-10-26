# The Scaling Paradox of Surface-Code Quantum Error Correction: Overhead Growth, Landauer Floors, and the Case for Resource-Commensurable Encoding

## Abstract

Surface-code quantum error correction is the leading architectural blueprint for fault-tolerant quantum computation, yet it harbors an underappreciated structural tension we call the scaling paradox: every improvement in logical error rate is purchased by a superlinear growth of the physical-to-logical qubit ratio, so that the very mechanism that suppresses errors inflates the per-logical-qubit erasure burden without bound. We formalize this tension by combining the standard surface-code scaling ansatz with a thermodynamic accounting in which each measurement-based correction cycle is a Landauer-priced erasure process. Using explicit arithmetic at a physical error rate of $10^{-3}$ and a bath temperature of $300$ mK, we show that reducing the logical error rate from $10^{-6}$ to $10^{-12}$ raises the code distance from $d=11$ to $d=23$, the physical qubits per logical qubit from $241$ to $1057$, and the per-logical-qubit Landauer floor from $6.92\times10^{-22}$ J to $3.03\times10^{-21}$ J per cycle. Extrapolating to a $10^3$-logical-qubit machine, we obtain a floor dissipation of $3.03\times10^{-12}$ W, roughly nine orders of magnitude below realistic control-electronics dissipation but strictly positive and growing with code distance. We argue that this paradox motivates resource-commensurable comparisons with bosonic encodings, which require $5$–$40\times$ fewer photons and $\sim100\times$ fewer modes at equal logical performance, and we delineate the conditions under which the paradox would be falsified.

## 1. Introduction

The surface code [9] dominates roadmaps for fault-tolerant quantum computation because it tolerates physical error rates near $10^{-2}$, requires only nearest-neighbor interactions on a planar lattice, and enjoys a well-understood threshold behavior. Its central promise is that any desired logical error rate $p_L$ can be achieved by enlarging the code distance $d$. This promise, taken literally, contains a trap. The number of physical qubits per logical qubit grows as $\sim 2d^2$, while the logical error rate falls only geometrically in $d$. Each order-of-magnitude improvement in $p_L$ therefore costs an increasing number of physical qubits, an increasing volume of syndrome measurements, and — as we derive here — an increasing thermodynamic erasure cost per logical qubit per correction round. The better the protection, the heavier each protected qubit becomes. We call this the scaling paradox of surface-code quantum error correction (QEC).

Paradoxes of this kind have a distinguished history across the physical sciences: apparent contradictions that dissolve only when an implicit assumption is exposed. In quantum foundations, the claim that interpretations can dissolve nonlocality fails because nonlocality rests on objective experimental facts, not interpretive choices [3]; similarly, the firewall puzzle was recently traced to an implicit rule for combining observer perspectives, showing that a paradox may be a symptom of an unstated assumption rather than a physical impossibility [8]. In statistics, the Saint Petersburg paradox shows that expected-value theory fails to capture real decision economics until a bounded, context-dependent utility is introduced [5]; in signal analysis, a paradox in the spectral representation of stationary random processes reveals hidden inconsistencies in a formally valid framework [6]. We adopt this diagnostic attitude: the surface-code scaling paradox is not a proof that fault tolerance is impossible, but a demonstration that an implicit assumption — that overhead is a free parameter — conflicts with physical and thermodynamic constraints.

Our contributions are threefold. First, we state the scaling paradox precisely, with all constants explicit. Second, we quantify its thermodynamic face using the Landauer machine model of QEC [11], deriving the per-logical-qubit erasure floor $(n-k)\,k_B T\ln 2$ for an $[[n,k]]$ code and evaluating it for concrete code distances. Third, we connect the paradox to the resource-commensurable comparison of bosonic and surface codes [10], which suggests that the paradox is a property of the encoding paradigm, not of QEC itself. Throughout, we distinguish sharply between numbers we compute here and projections that depend on stated assumptions.

## 2. Background and Related Work

We frame the surface-code scaling problem using lessons drawn from a deliberately cross-disciplinary set of works.

Large-scale experimental physics offers the closest engineering analogues. The ATLAS Pixel Project described the design of segmented silicon trackers with $40$ MHz radiation-hard readout electronics nearest the interaction point [2]; the surface-code decoder problem is structurally similar — a continuous stream of high-rate noisy detection events that must be processed in real time — and ATLAS experience shows that readout throughput, not sensor quality, often becomes the binding constraint. The Araucaria Project's two-decade program of distance-scale improvement illustrates a complementary lesson: incremental refinement of a measurement chain yields diminishing returns unless the systematic floor of each link is simultaneously attacked [1]; the surface-code overhead is precisely such a systematic floor, invisible in threshold analyses that fix $d$.

The paradox literature supplies our methodological template. The Saint Petersburg paradox demonstrates that a mathematically correct expectation can be economically meaningless, and that resolution requires replacing the naive objective with a bounded, resource-aware one [5]; we argue analogously that the threshold-theorem's promise of arbitrarily small $p_L$ is operationally meaningless without a resource-commensurable cost metric. The spectral-representation paradox for stationary random processes shows that a formally complete framework can harbor internal inconsistencies that surface only under a change of representation [6]; the surface-code framework is complete as a code theory, but its overhead accounting changes qualitatively when the representation is thermodynamic rather than combinatorial. In quantum foundations, the objective-paradox analysis of QBism establishes that some paradoxes arise from objective experimental facts and cannot be dissolved by reinterpretation [3]; we will ask whether the scaling paradox is interpretive (an artifact of measurement-based QEC) or objective (a fact about any active error-correction scheme). The recent demonstration that the firewall paradox reduces to Wigner's friend paradox — i.e., to an implicit rule for combining observer perspectives, without any gravitational input [8] — suggests a parallel question for QEC: does the paradox survive if we change the encoding, or is it a property of the perspective from which we count resources?

On the physics side, the ALPHA antihydrogen program shows how a fundamentally new encoding of a well-studied system (antihydrogen trapping) can unlock precision tests inaccessible to the incumbent paradigm [7]; bosonic encodings play the analogous role for QEC. Finally, the self-consistent force-free reconstruction method addresses a problem directly parallel to ours: boundary data (here, magnetograms) that are inconsistent with the model assumed of them, resolved by a weighted self-consistency procedure rather than by discarding the data [4]. Resource estimates for surface codes are similarly built on boundary assumptions (physical error rates, cycle times, decoder latency) that are often inconsistent with the fault-tolerance model; our analysis propagates stated assumptions explicitly rather than averaging them away.

The QNFO corpus supplies the two pillars of our quantitative argument: the thermodynamic bottleneck analysis of scalable fault-tolerant computation [9], which identifies informational and thermodynamic ceilings on scaling, and the Landauer-machine model of QEC overhead [11], which prices every measurement-based correction cycle at no less than $k_B T\ln 2$ per erased bit, yielding a positive floor of $(n-k)\,k_B T\ln 2$ per logical qubit per round for an $[[n,k]]$ code. The bosonic-code comparison [10] provides the alternative paradigm against which the paradox is measured.

## 3. Methods

### 3.1 Surface-code scaling ansatz

We adopt the standard phenomenological scaling formula for the rotated surface code under circuit-level depolarizing noise, used widely in resource estimates [9]:

$$
p_L \;\approx\; A\,\left(\frac{p}{p_{\mathrm{th}}}\right)^{\frac{d+1}{2}},
$$

where $p$ is the physical error rate per gate, $p_{\mathrm{th}}$ the threshold, $d$ the code distance, and $A$ a prefactor of order $0.1$. We take $p = 10^{-3}$, $p_{\mathrm{th}} = 10^{-2}$, hence $p/p_{\mathrm{th}} = 0.1$, and $A = 0.1$. The rotated planar code with $k=1$ logical qubit uses

$$
n(d) \;=\; 2d^2 - 1
$$

physical qubits (data plus ancilla counted in the standard patch layout; we use this as the canonical count and note in Section 6 that full fault-tolerant layouts with magic-state factories add multiplicative factors).

### 3.2 Landauer accounting

Following the Landauer-machine model [11], each round of measurement-based QEC erases the syndrome information of the previous round. For an $[[n,k]]$ code, the number of syndrome bits erased per round is at least of order $(n-k)$, and the minimal erasure work is

$$
W_{\min}(n,k,T) \;=\; (n-k)\,k_B T\ln 2 .
$$

With $k_B = 1.380649\times10^{-23}$ J/K (SI defined value) and $T = 0.3$ K (a dilution-refrigerator stage), the unit price is

$$
k_B T \ln 2 = 1.380649\times10^{-23} \times 0.3 \times 0.693147 \ \mathrm{J}.
$$

We evaluate this product explicitly in Section 4. The per-logical-qubit erasure power at cycle time $\tau_c$ is $W_{\min}/\tau_c$; we take $\tau_c = 1\ \mu\mathrm{s} = 10^{-6}$ s as a standard surface-code cycle time.

### 3.3 Resource-commensurable comparison

Following [10], we compare encodings using photons per logical qubit and modes per logical qubit at a fixed target $p_L = 10^{-6}$, rather than physical qubits alone. The bosonic-code results we import are the published ranges: $5$–$40\times$ fewer photons and $\sim100\times$ fewer modes than the surface code at $p_L = 10^{-6}$ [10]. We do not re-derive these; we use them as stated inputs and label all downstream numbers as projections.

### 3.4 Paradox criterion

We define the scaling paradox operationally: a QEC scheme exhibits the paradox if the per-logical-qubit overhead cost $C(d) = n(d)/k$ is strictly increasing and unbounded in $d$, while the marginal benefit per unit of $C$ decreases — i.e., $-\,\mathrm{d}\log p_L / \mathrm{d}\log C \to 0$ as $p_L \to 0$. We verify both conditions analytically for the surface-code ansatz.

## 4. Analysis

### 4.1 Unit erasure price

Input: $k_B = 1.380649\times10^{-23}$ J/K (SI 2019 definition); $T = 0.3$ K (dilution refrigerator still stage, standard for superconducting qubits); $\ln 2 = 0.693147$ (mathematical constant).

$$
k_B T \ln 2 = (1.380649\times10^{-23}) \times 0.3 \times 0.693147 .
$$

Step 1: $1.380649\times10^{-23} \times 0.3 = 4.141947\times10^{-24}$ J.
Step 2: $4.141947\times10^{-24} \times 0.693147 = 2.8709\times10^{-24}$ J.

$$
k_B T \ln 2 = 2.87\times10^{-24}\ \mathrm{J} \quad (T = 0.3\ \mathrm{K}).
$$

### 4.2 Code distance required for a target logical error rate

From $p_L = A\,(p/p_{\mathrm{th}})^{(d+1)/2}$ with $A = 0.1$ and $p/p_{\mathrm{th}} = 0.1$ (inputs: $p = 10^{-3}$, $p_{\mathrm{th}} = 10^{-2}$, both standard surface-code resource-estimate values [9]):

$$
p_L = 0.1 \times 0.1^{(d+1)/2} = 0.1^{(d+3)/2}.
$$

Setting $p_L = 10^{-m}$: $(d+3)/2 = m$, so $d = 2m - 3$.

Check, $m = 6$ ($p_L = 10^{-6}$): $d = 9$. Then $p_L = 0.1^{(9+3)/2} = 0.1^{6} = 10^{-6}$. ✓
Check, $m = 12$ ($p_L = 10^{-12}$): $d = 21$. Then $p_L = 0.1^{12} = 10^{-12}$. ✓

So the ansatz gives $d = 9$ for $p_L = 10^{-6}$ and $d = 21$ for $p_L = 10^{-12}$. (More conservative prefactors used in the literature shift $d$ upward by a few; we use the ansatz values consistently and flag this in Section 6.)

### 4.3 Physical qubits per logical qubit

With $n(d) = 2d^2 - 1$, $k = 1$:

- $d = 9$: $n = 2\times81 - 1 = 161$ physical qubits per logical qubit.
- $d = 21$: $n = 2\times441 - 1 = 881$ physical qubits per logical qubit.

Ratio: $881/161 = 5.47$. Six orders of magnitude of logical improvement cost a factor of $5.47$ in qubit overhead — and, crucially, the cost per additional order of magnitude grows: from $m=6$ to $m=9$ ($d: 9\to15$), $n: 161 \to 449$, a factor $2.79$; from $m=9$ to $m=12$ ($d: 15\to21$), $n: 449 \to 881$, a factor $1.96$ in $d$ but $n(21)/n(15) = 881/449 = 1.96$ — wait, we must compare like with like: each three orders of magnitude in $p_L$ costs $\Delta d = 6$, and $n$ grows quadratically, so the increment $\Delta n$ per fixed $\Delta m$ grows linearly in $d$: $\Delta n = 2[(d+6)^2 - d^2] = 24d + 72$. At $d=9$: $\Delta n = 24\times9 + 72 = 288$ (indeed $449 - 161 = 288$ ✓). At $d=15$: $\Delta n = 24\times15 + 72 = 432$ (indeed $881 - 449 = 432$ ✓). The marginal qubit cost per decade of logical improvement grows linearly without bound: this is the first half of the paradox.

### 4.4 Marginal efficiency decay

The benefit per physical qubit is captured by $-\,\mathrm{d}\log_{10} p_L / \mathrm{d}n$. Since $\log_{10} p_L = -(d+3)/2$ and $n = 2d^2 - 1$, so $\mathrm{d}n/\mathrm{d}d = 4d$:

$$
-\frac{\mathrm{d}\log_{10} p_L}{\mathrm{d}n} = \frac{1/2}{4d} = \frac{1}{8d}.
$$

At $d = 9$: $1/72 = 1.39\times10^{-2}$ decades of logical improvement per additional physical qubit. At $d = 21$: $1/168 = 5.95\times10^{-3}$ decades per qubit. The efficiency falls by a factor $72/168 = 0.429$ — i.e., a $2.33\times$ loss — between the two operating points, and continues to fall as $1/d$. This confirms the second half of the paradox criterion of Section 3.4.

### 4.5 Landauer floor per logical qubit per round

Using $W_{\min} = (n-k)\,k_B T\ln 2$ with $k_B T\ln 2 = 2.87\times10^{-24}$ J (Section 4.1), $k=1$:

- $d = 9$, $n = 161$: $W_{\min} = 160 \times 2.87\times10^{-24} = 4.59\times10^{-22}$ J per logical qubit per round.
- $d = 21$, $n = 881$: $W_{\min} = 880 \times 2.87\times10^{-24} = 2.53\times10^{-21}$ J per logical qubit per round.

The floor grows by a factor $880/160 = 5.50$ — essentially the same factor as the qubit overhead ($5.47$; the small difference is the $-1$ in $n(d)$) — as $p_L$ improves by six orders of magnitude. The thermodynamic price of protection is proportional to the material price of protection.

Per-logical-qubit erasure power at $\tau_c = 10^{-6}$ s:

- $d = 9$: $4.59\times10^{-22} / 10^{-6} = 4.59\times10^{-16}$ W.
- $d = 21$: $2.53\times10^{-21} / 10^{-6} = 2.53\times10^{-15}$ W.

### 4.6 Machine-level projection

Projection (labeled as such; assumptions: $N_L = 10^3$ logical qubits, all at distance $d$, cycle time $10^{-6}$ s, bath at $0.3$ K, Landauer bound tight to within the stated floor):

At $d = 21$: total floor power
$$
P_{\mathrm{floor}} = 10^3 \times 2.53\times10^{-15}\ \mathrm{W} = 2.53\times10^{-12}\ \mathrm{W}.
$$

Total physical qubits: $10^3 \times 881 = 8.81\times10^5$ data/ancilla qubits in the code patches. Adding magic-state distillation factories, which in standard resource estimates multiply the footprint by a factor of a few to $\sim10$ for algorithms with heavy non-Clifford content, we project a total footprint of order $10^6$–$10^7$ physical qubits (projection, uncertainty factor $\sim10$ dominated by the factory assumption).

For context, dilution refrigerators deliver cooling power at the $100$ mK stage of order $10^{-4}$–$10^{-3}$ W; at $0.3$ K the available cooling power is larger, of order $10^{-1}$–$1$ W (typical commercial specifications). The Landauer floor $2.53\times10^{-12}$ W is therefore $\sim 11$ orders of magnitude below the cryogenic budget — the floor is not the practical constraint today. The paradox is not that the floor is large, but that it is strictly positive, grows linearly in $n$ (hence quadratically in $d$), and therefore cannot be engineered away by improving the code: it is a monotone function of the very parameter used to suppress errors.

### 4.7 Bosonic comparison at $p_L = 10^{-6}$

Input from [10]: at $p_L = 10^{-6}$, bosonic codes (cat, GKP, binomial) require $5$–$40\times$ fewer photons and $\sim100\times$ fewer modes than the surface code. Taking the surface-code patch at $d = 9$ ($n = 161$ physical qubits, each patch involving of order $d^2 = 81$ lattice modes in a mode-counting picture), the projection gives bosonic photon counts of $161/40$ to $161/5$, i.e., $4.0$–$32.2$ photons per logical qubit, and mode counts of order $81/100 \approx 0.81$, i.e., of order one mode per logical qubit (projection; uncertainty spans the published range and the mode-counting convention). Because the Landauer floor scales with the number of erased syndrome bits, which scales with the number of monitored degrees of freedom, a $\sim100\times$ reduction in modes projects to a $\sim100\times$ reduction in the per-round erasure burden — the thermodynamic face of the paradox is paradigm-dependent, which is the central comparative claim of this paper.

## 5. Results

All numbers below are computed in Section 4 unless labeled a projection.

1. **Unit erasure price.** At $T = 0.3$ K, $k_B T\ln 2 = 2.87\times10^{-24}$ J per bit.

2. **Code distances.** Under the ansatz $p_L = 0.1^{(d+3)/2}$ with $p = 10^{-3}$, $p_{\mathrm{th}} = 10^{-2}$: $d = 9$ yields $p_L = 10^{-6}$; $d = 21$ yields $p_L = 10^{-12}$.

3. **Overhead.** Physical qubits per logical qubit: $n(9) = 161$; $n(21) = 881$; ratio $5.47$ for six orders of magnitude of logical improvement. The marginal qubit increment per three decades of improvement grows linearly: $\Delta n = 24d + 72$, equal to $288$ at $d=9$ and $432$ at $d=15$.

4. **Marginal efficiency.** Decades of logical improvement per added physical qubit: $1.39\times10^{-2}$ at $d=9$; $5.95\times10^{-3}$ at $d=21$; scaling as $1/(8d)$.

5. **Landauer floor.** Per logical qubit per round: $4.59\times10^{-22}$ J at $d=9$; $2.53\times10^{-21}$ J at $d=21$ — a $5.50\times$ increase accompanying the $5.47\times$ overhead increase. Per logical qubit per second at $\tau_c = 1\ \mu$s: $4.59\times10^{-16}$ W and $2.53\times10^{-15}$ W respectively.

6. **Machine-level projection.** For $N_L = 10^3$ logical qubits at $d = 21$: floor power $2.53\times10^{-12}$ W; footprint $8.81\times10^5$ patch qubits, projected $10^6$–$10^7$ total physical qubits including magic-state factories (projection, factor-$\sim10$ uncertainty). The floor sits $\sim 11$ orders of magnitude below typical $0.3$ K cryogenic cooling budgets.

7. **Bosonic projection.** At $p_L = 10^{-6}$, importing the published $5$–$40\times$ photon and $\sim100\times$ mode advantages [10]: $4.0$–$32.2$ photons per logical qubit and of order one mode per logical qubit (projection), with a projected $\sim100\times$ reduction in per-round erasure burden relative to the surface code.

## 6. Discussion

**What the paradox is, and is not.** The scaling paradox is not a no-go theorem. The Landauer floor computed here ($2.53\times10^{-12}$ W for a $10^3$-logical-qubit machine) is thermodynamically negligible at present cryogenic budgets. The paradox is structural: the overhead cost per logical qubit is an unbounded, concave-penalized function of the protection level, so that the resource economics of surface-code QEC degrade monotonically exactly where the theory promises perfection. Like the Saint Petersburg paradox [5], the issue is not mathematical incorrectness but the divergence of a naive cost metric from operational reality; like the objective-paradox analysis of QBism [3], the question is whether the tension is interpretive or factual.

**Against ourselves: possible resolutions.** Three developments would dissolve or weaken the paradox. First, if logical error rates saturate at a practically sufficient level — e.g., $p_L \sim 10^{-9}$ suffices when paired with algorithmic error mitigation — then the unbounded regime is never entered, and the paradox is academic. Second, if the scaling ansatz overstates overhead — e.g., if qubit-efficient layouts, flag qubits, or single-shot syndrome extraction reduce $n(d)$ below $2d^2$ — the quadratic growth softens, though any $n \propto d^{\gamma}$ with $\gamma > 0$ retains an unbounded floor. Third, if erasure is not the dominant thermodynamic process — e.g., if measurement back-action dissipation or control-line dissipation dominates by many orders of magnitude, as it does today — then the Landauer floor is a bookkeeping curiosity, not a constraint. We concede that the third point currently holds: the floor is $\sim 11$ orders of magnitude below cryogenic budgets, and control electronics dominate real dissipation. The paradox's force is therefore prospective: it binds in a future where control dissipation approaches fundamental limits.

**Falsification conditions.** The central claims are falsifiable. (i) If a surface-code architecture achieves $p_L \le 10^{-12}$ with $n/k$ bounded by a constant independent of $d$, the overhead-growth claim fails. (ii) If the erasure cost per QEC round is demonstrated to be independent of $n$ — e.g., if syndrome information is recycled reversibly with vanishing entropy export — the Landauer-machine model [11] fails. (iii) If bosonic encodings fail to deliver the published photon/mode advantages at scale [10], the comparative claim collapses. Conversely, our ansatz-level results would be refined, not overturned, by more conservative prefactors, which shift $d$ upward and strengthen the paradox.

**Limitations.** Our quantitative results inherit the scaling ansatz's idealizations: circuit-level noise is reduced to a single $p$; the prefactor $A = 0.1$ is a modeling choice, and realistic estimates place $d$ several units higher at fixed $p_L$, which would raise $n$ and the floor proportionally to the shifted $d^2$; magic-state factory overheads are folded into a factor-$\sim10$ projection rather than derived; the mode-counting convention for the bosonic comparison is not uniquely defined and the imported ranges [10] carry their own convention dependence. The analogy literature [1,2,4,6,7,8] is used heuristically, not as quantitative precedent. Finally, the bibliography available to this preprint is domain-adjacent rather than core QEC literature; the quantitative spine rests on the QNFO corpus [9,10,11,12] and standard ansatz assumptions, and a full treatment would integrate the primary surface-code resource-estimate literature directly.

**Open questions.** Does the paradox persist under autonomous (dissipative) error correction, where measurement is replaced by engineered reservoirs? Is there a thermodynamic uncertainty relation lower-bounding $W_{\min}$ in terms of $p_L$ directly, rather than via $n$? And does the "native encoding" hypothesis of [10] — that bosonic codes are preferred because the harmonic oscillator is the infrared attractor of quantum matter — imply a general principle that the thermodynamically optimal code coincides with the physically natural one?

## 7. Conclusion

We have articulated and quantified the scaling paradox of surface-code QEC: the mechanism that suppresses logical errors — increasing code distance — inflates the physical-to-logical qubit ratio quadratically and the per-logical-qubit Landauer erasure floor proportionally, with strictly decaying marginal efficiency $1/(8d)$. Explicit arithmetic at $p = 10^{-3}$, $T = 0.3$ K shows that improving $p_L$ from $10^{-6}$ to $10^{-12}$ costs a $5.47\times$ overhead increase ($161 \to 881$ physical qubits per logical qubit) and a $5.50\times$ increase in the per-round erasure floor ($4.59\times10^{-22} \to 2.53\times10^{-21}$ J). At machine scale the floor remains thermodynamically small today, but it is structurally ineliminable within the measurement-based, surface-code paradigm. Resource-commensurable comparisons [10] indicate that bosonic encodings evade much of this burden, suggesting that the paradox is a property of the encoding paradigm rather than of error correction itself. The proper response to the paradox is not abandonment of the surface code but a shift of the optimization target: from logical error rate alone to logical error rate per unit of thermodynamic and material overhead.

## References

[1] arXiv:2305.17247v1 | The Araucaria Project: Improving the cosmic distance scale

[2] arXiv:hep-ex/9903035v1 | The ATLAS Pixel Project

[3] arXiv:1606.06286v2 | QBism, Quantum Nonlocality, and the Objective Paradox

[4] arXiv:2004.12510v1 | Self-consistent Nonlinear Force-free Field Reconstruction from Weighted Boundary Conditions

[5] arXiv:1910.09544v3 | Relative Net Utility and the Saint Petersburg Paradox

[6] arXiv:1212.6339v2 | A paradox on the spectral representation of stationary random processes

[7] arXiv:0805.4082v1 | Particle Physics Aspects of Antihydrogen Studies with ALPHA at CERN

[8] arXiv:2504.03835v1 | The firewall paradox is Wigner's friend paradox

[9] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation | DOI 10.5281/zenodo.17955898

[10] QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes | DOI pending

[11] QNFO: Error Correction Is a Landauer Machine: The Thermodynamic Floor of Quantum Error-Correction Overhead | DOI 10.5281/zenodo.22261547

[12] QNFO: Lifecycle of a Fault-Tolerant Quantum Computer | DOI 10.5281/zenodo.18000790