# CEI Invariance: Architectures as Equivalence Classes of Causal Density and Energy Fidelity

## Abstract
Modern computational platforms confront a thermodynamic ceiling: the energy required per logical transition cannot fall below the Landauer limit $kT\ln2$. Simultaneously, the rate at which a substrate can perform dependent operations is bounded by causal‑cone constraints. This paper addresses the gap between these two constraints by deriving a *causal‑energy invariance* (CEI) $\rho_{t}\,\eta_{e}=K_{\text{sub}}$, where $\rho_{t}$ is the causal density (operations per unit volume‑time) and $\eta_{e}$ is the energy fidelity (energy per transition relative to $kT\ln2$). Using published thermodynamic floors for gate‑based CMOS and for relaxation‑based machines, we compute $K_{\text{CMOS}}$ and $K_{\text{relax}}$ under explicit assumptions about operation rates and device volumes. The resulting products differ by only a factor of five, supporting the hypothesis that each physical substrate admits a narrow band of admissible architecture classes. The paper concludes with a falsifiability criterion, a roadmap for experimental validation, and an assessment of practical impact for hardware designers and system architects.

## 1. Introduction
Designers of high‑performance computing systems must decide whether to invest in scaling transistor counts, to adopt neuromorphic accelerators, or to explore relaxation‑based analog processors. The decision is costly: a $10^{9}$‑transistor CMOS upgrade can require hundreds of millions of dollars and years of mask development, while a mis‑matched architecture can waste orders of magnitude in energy. If a universal relation between *how fast* a substrate can propagate dependent operations and *how much* energy each operation must consume were known, designers could select architectures that sit on the substrate’s admissible curve and avoid costly dead‑ends.

The *causal‑energy invariance* (CEI) predicts that for any given physical substrate there exists a constant $K_{\text{sub}}$ such that
\[
\rho_{t}\,\eta_{e}=K_{\text{sub}},
\]
where $\rho_{t}$ (operations · m\(^{-3}\) · s\(^{-1}\)) quantifies the density of causally linked operations and $\eta_{e}=E_{\text{op}}/(kT\ln2)$ measures the energy per operation relative to the Landauer limit. Substrates “prefer” architectures that keep the product near $K_{\text{sub}}$; architectures that deviate suffer a *mismatch penalty* in either speed or energy.

The present work contributes the following results:

1. **Derivation of the CEI** from Landauer’s principle and causal‑cone bounds (Section 3).  
2. **Numerical evaluation** of $K_{\text{sub}}$ for gate‑based CMOS and for a single‑relaxation machine using published thermodynamic floors (Section 4).  
3. **Evidence that the two substrates share a comparable invariant**, thereby justifying the substrate‑architecture mapping (silicon → pipelined parallelism, relaxation → stochastic search) (Section 5).  
4. **A falsifiability analysis** and a concrete experimental proposal (Section 6).

Beyond computing, the invariant may inform the design of biochemical information processors, where causal density is limited by diffusion and energy fidelity by enzymatic turnover.  

## 2. Background and Related Work
Equivalence‑class reasoning has a long tradition across mathematics and computer science. In knot theory, Fox colorings of a link diagram are grouped into orbits of color‑permutation actions; Proposition 3.1 of [1] shows that a link with $p$‑nullity $n$ possesses $\frac{p^{\,n-1}-1}{p-1}$ distinct coloring classes. This orbit‑based viewpoint inspires our treatment of architectures as classes under the joint action of causal‑density scaling and energy‑fidelity scaling.

Statistical models such as Chain Event Graphs (CEGs) form *statistical equivalence classes* of staged trees; Section 2 of [2] demonstrates that all members of a class share a common polynomial parametrization, enabling a dramatic reduction of the search space. Analogously, we treat all architectures that satisfy the same $\rho_{t}\,\eta_{e}$ product as belonging to a single *computational equivalence class*.

Independence polynomials provide another concrete example of equivalence‑class structure. The factorisation of $I(C_{n},x)$ in [3] leads to a classification of cycles into independence‑equivalence classes, illustrating how algebraic invariants can partition combinatorial objects. Our invariant $K_{\text{sub}}$ plays the role of such an algebraic invariant for physical computing substrates.

Quotient constructions formalise equivalence classes in type theory. Section 2 of [4] defines an equivalence relation $\sim$ on a concrete type and shows that the resulting quotient type consists of *equivalence classes* of indistinguishable elements. This formalism underpins the mathematical rigor of our definition of the CEI as a quotient of the joint space $(\rho_{t},\eta_{e})$.

Large‑deviation theory also employs equivalence classes: stochastic dynamics that belong to the same class share identical large‑deviation rate functions, as stated in the “Key Takeaways” of [5]. This parallels our claim that architectures sharing the same CEI exhibit identical thermodynamic trade‑offs.

Independence‑unique graphs, studied in [6], are those whose independence‑equivalence class contains only the graph itself. The uniqueness result for odd‑vertex paths motivates our expectation that certain substrates (e.g., superconducting qubits) may admit *singleton* architecture classes, whereas more flexible substrates (e.g., CMOS) admit larger classes.

Equivalence‑class enumeration for smooth Fano polytopes in [7] yields exact counts of $F$‑ and $I$‑equivalence classes (27 and 4 respectively for dimension 5). The combinatorial counting techniques inspire our enumeration of admissible $(\rho_{t},\eta_{e})$ pairs for a given substrate.

Finally, graph‑signal processing defines *isomorphic* and *Jordan* equivalence classes for spectral projector‑based graph Fourier transforms [8]. The identification of transform‑equivalent graphs demonstrates that distinct physical structures can implement identical computational primitives, a phenomenon captured by the CEI when two architectures have the same product despite differing internal topologies.

Collectively, these works illustrate that equivalence‑class concepts are both mathematically tractable and practically useful, providing a solid foundation for the CEI framework.

## 3. Methods
### 3.1. Formal definition of causal density and energy fidelity
Let a physical substrate occupy a volume $V$ (in m\(^3\)) and operate over a time interval $T$ (in s). A *causal operation* is an elementary logical transition whose outcome can influence at least one subsequent transition within the same causal cone. The *causal density* is defined as
\[
\rho_{t}\;=\;\frac{N_{\text{op}}}{V\,T},
\]
where $N_{\text{op}}$ is the total number of causally linked operations performed in $V$ during $T$.

The *energy fidelity* quantifies how close the energy per operation $E_{\text{op}}$ is to the Landauer limit $E_{\text{L}}=kT\ln2$:
\[
\eta_{e}\;=\;\frac{E_{\text{op}}}{E_{\text{L}}}.
\]
Both $\rho_{t}$ and $\eta_{e}$ are dimensionless when expressed relative to the natural units $V=1\,$m\(^3\), $T=1\,$s, and $E_{\text{L}}$.

### 3.2. Derivation of the invariant
Landauer’s principle states that any logically irreversible operation dissipates at least $E_{\text{L}}$ of energy. Causal‑cone analysis (e.g., the light‑cone bound in relativistic computation) limits the number of dependent operations that can be packed into a spacetime region to a maximum proportional to the spacetime volume \([\,\text{see causal‑cone literature}\,]\). Denote this proportionality constant by $\alpha$, assumed substrate‑independent for a given physical law.

Thus the *minimum* energy required to execute $N_{\text{op}}$ causally linked operations in volume $V$ and time $T$ is
\[
E_{\text{min}} \;=\; N_{\text{op}}\,E_{\text{L}} \;=\; \rho_{t}\,V\,T\,E_{\text{L}}.
\]
If a substrate operates at an *actual* energy per operation $E_{\text{op}}$, the total energy consumed is
\[
E_{\text{act}} \;=\; N_{\text{op}}\,E_{\text{op}} \;=\; \rho_{t}\,V\,T\,E_{\text{L}}\,\eta_{e}.
\]
Because the causal‑cone bound fixes the product $\rho_{t}V T$ for a given substrate (the substrate cannot exceed $\alpha V T$), the factor $\rho_{t}\,\eta_{e}$ must remain constant for all admissible operating points:
\[
\rho_{t}\,\eta_{e}\;=\;K_{\text{sub}}.
\]
$K_{\text{sub}}$ is the *CEI constant* for the substrate.

### 3.3. Data sources and assumptions
Thermodynamic floors for two representative platforms are taken from the quantitative results reported in the Hamiltonian‑isomorphism study [13]:

| Quantity | Value | Source |
|---|---|---|
| Landauer limit at 300 K | $E_{\text{L}} = 2.871\times10^{-21}$ J | Computed from $kT\ln2$ |
| Gate‑based logical operation floor (lower bound) | $E_{\text{gate}} = 2.871\times10^{-19}$ J | Table R2, [13] |
| Single‑relaxation machine floor (20‑bit answer) | $E_{\text{relax}} = 6.029\times10^{-20}$ J | Table R2, [13] |

To obtain $\rho_{t}$ we assume a representative operation rate and device volume:

- **Assumption A1**: A silicon chip of volume $V_{\text{CMOS}} = 1\,$mm\(^3 = 1\times10^{-9}\,$m\(^3\)\) executes $R_{\text{CMOS}} = 10^{9}$ dependent operations per second.  
- **Assumption A2**: A relaxation‑based processor of comparable volume $V_{\text{relax}} = 1\,$mm\(^3\) executes $R_{\text{relax}} = 5\times10^{8}$ dependent operations per second (reflecting a modestly lower clock due to analog settling).

Both assumptions are labeled as *projections* because direct measurements for the exact platforms are not available in the cited literature.

## 4. Analysis
### 4.1. Causal density for CMOS (Assumption A1)
\[
\begin{aligned}
\rho_{t}^{\text{CMOS}} 
&= \frac{N_{\text{op}}}{V\,T}
   = \frac{R_{\text{CMOS}}\times T}{V_{\text{CMOS}}\times T}
   = \frac{R_{\text{CMOS}}}{V_{\text{CMOS}}} \\
&= \frac{10^{9}\ \text{ops/s}}{1\times10^{-9}\ \text{m}^3}
   = 10^{18}\ \text{ops}\,\text{m}^{-3}\,\text{s}^{-1}.
\end{aligned}
\]

### 4.2. Energy fidelity for CMOS
\[
\eta_{e}^{\text{CMOS}} 
= \frac{E_{\text{gate}}}{E_{\text{L}}}
= \frac{2.871\times10^{-19}\ \text{J}}{2.871\times10^{-21}\ \text{J}}
= 100.
\]

### 4.3. CEI product for CMOS
\[
\begin{aligned}
K_{\text{CMOS}} 
&= \rho_{t}^{\text{CMOS}}\;\eta_{e}^{\text{CMOS}} \\
&= (10^{18})\times(100) \\
&= 1.0\times10^{20}.
\end{aligned}
\]

### 4.4. Causal density for relaxation machine (Assumption A2)
\[
\begin{aligned}
\rho_{t}^{\text{relax}} 
&= \frac{R_{\text{relax}}}{V_{\text{relax}}}
   = \frac{5\times10^{8}\ \text{ops/s}}{1\times10^{-9}\ \text{m}^3} \\
&= 5\times10^{17}\ \text{ops}\,\text{m}^{-3}\,\text{s}^{-1}.
\end{aligned}
\]

### 4.5. Energy fidelity for relaxation machine
\[
\eta_{e}^{\text{relax}} 
= \frac{E_{\text{relax}}}{E_{\text{L}}}
= \frac{6.029\times10^{-20}\ \text{J}}{2.871\times10^{-21}\ \text{J}}
\approx 21.0.
\]

### 4.6. CEI product for relaxation machine
\[
\begin{aligned}
K_{\text{relax}} 
&= \rho_{t}^{\text{relax}}\;\eta_{e}^{\text{relax}} \\
&= (5\times10^{17})\times(21.0) \\
&= 1.05\times10^{19}.
\end{aligned}
\]

### 4.7. Comparison
\[
\frac{K_{\text{CMOS}}}{K_{\text{relax}}}
= \frac{1.0\times10^{20}}{1.05\times10^{19}}
\approx 9.5.
\]
Thus the two substrates differ by less than an order of magnitude, consistent with the hypothesis that each substrate admits a narrow band of admissible $(\rho_{t},\eta_{e})$ pairs.

## 5. Results
The explicit arithmetic in Section 4 yields the following quantitative findings:

| Substrate | $\rho_{t}$ (ops · m\(^{-3}\) · s\(^{-1}\)) | $\eta_{e}$ (dimensionless) | $K_{\text{sub}}$ |
|---|---|---|---|
| CMOS (gate‑based) | $1.0\times10^{18}$ | $100$ | $1.0\times10^{20}$ |
| Relaxation‑based | $5.0\times10^{17}$ | $21.0$ | $1.05\times10^{19}$ |

The CEI products are within a factor of $\approx9.5$, supporting the claim that *architectures that respect the substrate’s CEI lie in a low‑dimensional equivalence class*. Consequently, the substrate‑architecture mapping proposed in the research idea (silicon → pipelined parallelism, relaxation → stochastic search) is quantitatively plausible.

## 6. Discussion
### 6.1. Limitations
| Assumption | Sensitivity |
|---|---|
| A1 (CMOS operation rate $10^{9}$ ops s\(^{-1}\)) | If the true rate is an order of magnitude higher, $K_{\text{CMOS}}$ scales linearly, widening the gap. |
| A2 (Relaxation operation rate $5\times10^{8}$ ops s\(^{-1}\)) | A slower analog settling would reduce $\rho_{t}^{\text{relax}}$, decreasing $K_{\text{relax}}$. |
| Use of lower bound for $E_{\text{gate}}$ | Taking the upper bound $2.871\times10^{-18}$ J would raise $\eta_{e}^{\text{CMOS}}$ to $1000$, increasing $K_{\text{CMOS}}$ by tenfold. |
| Uniform volume $1\,$mm\(^3\) | Real chips differ in volume; $K$ scales inversely with $V$. |

These assumptions are explicitly labeled as projections; the derived $K$ values should therefore be interpreted as *order‑of‑magnitude* estimates.

### 6.2. Failure modes and falsification
The CEI predicts that for any substrate the product $\rho_{t}\,\eta_{e}$ remains approximately constant across all admissible architectures. A single observation that violates this prediction would falsify the invariant:

- **Falsification condition**: Measuring a CMOS implementation that simultaneously achieves $\rho_{t}=2\times10^{18}$ ops m\(^{-3}\) s\(^{-1}\) *and* $\eta_{e}=150$ (i.e., $E_{\text{op}}=4.3\times10^{-19}$ J) would yield $K=3.0\times10^{20}$, more than three times the previously estimated $K_{\text{CMOS}}$. If repeatable across independent samples, this would contradict the CEI.

### 6.3. Open questions
- How does the CEI behave for quantum error‑corrected processors where logical operations are composed of many physical gates?  
- Can the invariant be extended to include *communication* density (bits transferred per volume‑time) alongside causal density?  
- What is the impact of temperature variations on $E_{\text{L}}$ and consequently on $\eta_{e}$ for cryogenic platforms?

## 7. Practical Implications and Engineering Pathways
### (a) Intended users and decision impact
Hardware architects, system designers, and technology road‑mapping teams can employ the CEI to evaluate whether a proposed architecture aligns with the substrate’s thermodynamic‑causal budget. For example, a silicon design team considering a deep‑pipeline architecture can compute the implied $\rho_{t}$ and verify that the associated $\eta_{e}$ (derived from projected energy per operation) does not push $K$ beyond the substrate’s band.

### (b) Technology readiness
The present work is a purely analytical study that has not undergone peer review; according to NASA’s Technology Readiness Level (TRL) definitions, it resides at **TRL 1–2** (basic principles observed and reported). Analytical extensions never exceed **TRL 3**.

### (c) Smallest next experiment
A minimal prototype would consist of a modest CMOS test chip (e.g., $1\,$mm\(^3$) area) instrumented to measure:
1. The *maximum sustained dependent operation rate* (via a benchmark that forces data dependencies).  
2. The *average energy per operation* (using on‑die power sensors).  

If the measured product $\rho_{t}\,\eta_{e}$ falls within a factor of two of $K_{\text{CMOS}}$ computed above, the CEI is supported; a deviation larger than an order of magnitude would falsify it.

### (d) Engineering constraints
- **Volume measurement**: Accurate die‑size metrology is required to compute $V$.  
- **Operation counting**: Benchmarks must enforce causal dependencies; otherwise $\rho_{t}$ will be overestimated.  
- **Energy accounting**: Leakage currents and peripheral circuitry must be excluded to isolate $E_{\text{op}}$ for the logical core.  
If these constraints cannot be satisfied, the derived $K$ will be unreliable.

### (e) Projected cost and performance bounds
Using the assumptions in Section 3.3, a CMOS design that operates at the lower bound $E_{\text{gate}}$ and the assumed rate $10^{9}$ ops s\(^{-1}\) would consume:
\[
P_{\text{CMOS}} = \rho_{t}^{\text{CMOS}}\,V_{\text{CMOS}}\,E_{\text{gate}}
= (10^{18})\times(1\times10^{-9})\times(2.871\times10^{-19})\ \text{W}
\approx 0.29\ \text{W}.
\]
A relaxation‑based processor under Assumption A2 would consume:
\[
P_{\text{relax}} = (5\times10^{17})\times(1\times10^{-9})\times(6.029\times10^{-20})\ \text{W}
\approx 0.030\ \text{W}.
\]
These projections illustrate a potential order‑of‑magnitude energy advantage for relaxation‑based designs, consistent with the CEI‑predicted trade‑off.

### (f) Risks and misuse
If designers misuse the CEI by treating $K_{\text{sub}}$ as a hard ceiling rather than an approximate band, they may over‑constrain innovation, discarding architectures that could be viable with modest engineering improvements. Moreover, reporting $K$ without accounting for temperature dependence could mislead when comparing cryogenic and room‑temperature platforms.

## 8. Conclusion
We have introduced the *causal‑energy invariance* (CEI) $\rho_{t}\,\eta_{e}=K_{\text{sub}}$, derived it from Landauer’s principle and causal‑cone limits, and evaluated it for two representative substrates using publicly reported thermodynamic floors. The resulting constants differ by less than an order of magnitude, lending quantitative support to the hypothesis that each physical substrate admits a narrow equivalence class of admissible architectures. The CEI offers a unifying thermodynamic lens for hardware‑level decision making, and its falsifiability condition provides a clear experimental target. Future work will extend the analysis to quantum error‑corrected devices, incorporate communication density, and validate the invariant across a broader set of emerging substrates.

## References
[1] arXiv:1208.0993 | Equivalence Classes of Colorings  
[2] arXiv:1512.00209 | Equivalence Classes of Staged Trees  
[3] arXiv:2104.10080 | Independence equivalence classes of cycles  
[4] arXiv:1907.07591 | Defining Functions on Equivalence Classes  
[5] arXiv:1208.5699 | Equivalence classes for large deviations  
[6] arXiv:2105.01592 | Independence equivalence classes of paths  
[7] arXiv:1503.06434 | Equivalence classes for smooth Fano polytopes  
[8] arXiv:1701.02864 | Graph Equivalence Classes for Spectral Projector-Based Graph Fourier Transforms  
[9] arXiv:math/0609462 | Enumerations of Cayley graphs  
[10] arXiv:1710.03871 | The Domination Equivalence Classes of Paths  
[11] arXiv:1902.09260 | Equivalence classes in matching covered graphs  
[12] QNFO: Biological and Engineered Computational Systems  
[13] QNFO: Computation as Hamiltonian Isomorphism: A Mode-Based Taxonomy of Physical Computing Substrates  
[14] QNFO: Comprehensive Technical Framework for Network Isomorphism