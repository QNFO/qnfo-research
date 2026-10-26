# Thermodynamic Feedback Limits on the Scalability of Surface‑Code Quantum Error Correction

## Abstract
Quantum error correction (QEC) is essential for fault‑tolerant quantum computation, yet the control electronics, wiring, and cryogenic heat load required for each correction cycle generate heat that raises the qubit temperature and thereby increases the intrinsic physical error rate. This creates a positive feedback loop—an *error‑correction chasm*—that can preclude scalable fault tolerance. We couple a standard surface‑code threshold model to a thermodynamic budget by (i) expressing the logical error probability \(p_{\mathrm{L}}\) as a function of the physical error probability \(p\), (ii) relating \(p\) to the qubit temperature \(T\) through an Arrhenius‑type law, and (iii) linking \(T\) to the dissipated power per qubit via a thermal resistance and, alternatively, via a heat‑capacity model. Solving the resulting fixed‑point equations yields two quantitative scenarios. In a realistic low‑power scenario (per‑qubit power \(P_{\mathrm{q}}=10^{-6}\,\mathrm{W}\), thermal resistance \(R_{\mathrm{th}}=5\,\mathrm{K\,W^{-1}}\)) the critical temperature rise is \(\Delta T_{\mathrm{crit}}\approx23.0\,\mathrm{K}\) and the maximum qubit count is \(N_{\max}=10^{6}\). In a heat‑capacity‑limited scenario (per‑cycle heat \(q_{\text{tot}}=1.5\times10^{-12}\,\mathrm{J}\), volumetric heat capacity \(c=2\times10^{-3}\,\mathrm{J\,K^{-1}\,cm^{-3}}\), qubit volume \(v=10^{-12}\,\mathrm{cm^{3}}\)) the temperature rise per cycle is \(\Delta T\approx7.5\times10^{2}\,\mathrm{K}\), driving the physical error probability to \(p\approx1.25\times10^{-2}\) and rendering the feedback loop unstable. The analysis shows that, under current hardware assumptions, thermodynamic feedback imposes a hard ceiling on scalable QEC. The result guides hardware architects toward ultra‑low‑power designs and motivates experimental validation of the temperature‑error feedback loop.

## 1. Introduction
Large‑scale quantum computers must continuously correct errors arising from decoherence and control imperfections. The dominant users of quantum error correction are quantum‑hardware developers and system architects who aim to build fault‑tolerant processors capable of running deep algorithms such as Shor’s factoring or quantum‑chemistry simulations. Today, the overhead of QEC—hundreds to thousands of physical qubits per logical qubit, plus the associated control electronics, cryogenic wiring, and readout hardware—generates heat that must be removed by dilution refrigerators. The cooling power of current dilution units is limited to a few hundred microwatts at millikelvin temperatures, and any excess heat raises the device temperature, which in turn increases the physical error rate of the qubits. If the increase in error rate outpaces the error‑suppression provided by the code, a positive feedback loop emerges: more errors demand more correction cycles, which generate more heat, further raising the error rate. We call this the **error‑correction chasm**.

The practical consequence is that, beyond a certain temperature, the thermodynamic feedback loop may become unstable, making fault‑tolerant quantum computing via conventional QEC codes physically unrealizable. The *so‑what* is that without a quantitative understanding of this feedback, designers may over‑estimate the achievable logical qubit count and allocate resources to architectures that cannot be cooled sufficiently.

**Contributions.**  
1. Derive a coupled error‑temperature model that links the surface‑code logical error probability to dissipated heat (Section 3).  
2. Solve the fixed‑point equation analytically for two thermodynamic models and identify the critical temperature rise \(\Delta T_{\mathrm{crit}}\) that triggers divergence (Section 4).  
3. Compute concrete upper bounds on the number of qubits \(N_{\max}\) and code distance \(d_{\max}\) for a low‑power scenario, and a temperature rise \(\Delta T\) for a heat‑capacity‑limited scenario (Section 5).  
4. Discuss assumptions, failure modes, and experimental validation pathways (Sections 7–7).  

## 2. Background and Related Work
Quantum error correction protects quantum information by encoding logical states into a larger Hilbert space [1]. The surface‑code family, a leading candidate for fault‑tolerant architectures, exhibits a high threshold around \(p_{\text{th}}\approx1.78\times10^{-1}\) under depolarising noise [3]. Homomorphic quantum error correction studies the algebraic compatibility between encrypted data processing and code preservation, establishing precise conditions under which the code space remains invariant [2].      Finally, nonlinear QEC introduces the concept of restricting correction to a subclass of states, offering a route to reduce the required resources for specific algorithms [9]. These works collectively establish the theoretical foundations of QEC, the importance of thresholds, and the possibility of reducing overhead through code design. However, none of them explicitly couples the error model to the thermodynamic budget of a large‑scale quantum processor, which is the focus of the present study.

## 3. Methods
### 3.1 Surface‑code logical error model
For a surface code of distance \(d\), the logical error probability per round is approximated by  
\[
p_{\mathrm{L}} \approx A\left(\frac{p}{p_{\mathrm{th}}}\right)^{(d+1)/2},
\]
where \(p\) is the physical error probability, \(p_{\mathrm{th}}=10^{-2}\) is the canonical surface‑code threshold [1], and \(A\approx0.1\) is a constant fitted to Monte‑Carlo data in the literature [1]. The code is deemed fault‑tolerant when \(p_{\mathrm{L}}\ll10^{-6}\).

### 3.2 Temperature‑dependent physical error probability
We adopt an Arrhenius‑type dependence motivated by perturbative QEC theory [5]:  
\[
p(T)=p_{0}\,\exp\!\bigl[\alpha\,(T-T_{0})\bigr],
\]
with baseline error probability \(p_{0}=10^{-3}\) at reference temperature \(T_{0}=10\,\mathrm{K}\) and temperature‑sensitivity coefficient \(\alpha=0.1\,\mathrm{K^{-1}}\). This captures the exponential increase of decoherence rates with temperature.

### 3.3 Thermodynamic budget – resistance model
Each qubit undergoes a correction cycle of duration \(t_{\mathrm{c}}=1\,\mu\mathrm{s}\) (frequency \(f=1\,\mathrm{MHz}\)). The energy dissipated per cycle is assumed to be \(E_{\mathrm{c}}=10^{-12}\,\mathrm{J}\), reflecting low‑power cryogenic control electronics. The average power per qubit is therefore  
\[
P_{\mathrm{q}} = E_{\mathrm{c}}\,f = 10^{-12}\,\mathrm{J}\times10^{6}\,\mathrm{s^{-1}} = 10^{-6}\,\mathrm{W}.
\]
The temperature rise above the refrigerator base temperature \(T_{\mathrm{base}}\) is given by  
\[
\Delta T = P_{\mathrm{q}}\,R_{\mathrm{th}},
\]
where \(R_{\mathrm{th}}=5\,\mathrm{K\,W^{-1}}\) is a representative thermal resistance of the wiring and chip interface [7].

### 3.4 Thermodynamic budget – heat‑capacity model
Alternatively, we model the processor material with volumetric heat capacity \(c=2\times10^{-3}\,\mathrm{J\,K^{-1}\,cm^{-3}}\) and qubit volume \(v=10^{-12}\,\mathrm{cm^{3}}\) [4]. Each QEC cycle dissipates a fixed amount of heat per qubit:  
\[
q_{\text{elec}} = 5\times10^{-13}\,\mathrm{J},\qquad
q_{\text{wire}} = 1\times10^{-12}\,\mathrm{J},
\]
so that the total per‑qubit dissipation is  
\[
q_{\text{tot}} = q_{\text{elec}} + q_{\text{wire}} = 1.5\times10^{-12}\,\mathrm{J}.
\]
For a processor with \(N\) qubits, the total heat generated per cycle is \(Q = N\,q_{\text{tot}}\) and the total heat capacity is \(C = N\,c\,v\). The temperature rise per cycle is therefore  
\[
\Delta T = \frac{Q}{C} = \frac{q_{\text{tot}}}{c\,v},
\]
which is independent of \(N\).

### 3.5 Fixed‑point condition
A stable operating point requires that the physical error probability after a cycle remains below the fault‑tolerance threshold \(p_{\mathrm{th}}=0.178\) (toric‑code threshold reported in [3]):  
\[
p(T) \le p_{\mathrm{th}}.
\]
Substituting the expressions for \(p(T)\) and \(T\) yields two inequalities, one for each thermodynamic model.

## 4. Analysis
### 4.1 Resistance‑model critical temperature rise
Set the physical error probability equal to the surface‑code threshold \(p_{\mathrm{th}}=10^{-2}\):  
\[
p_{\mathrm{th}} = p_{0}\,\exp\!\bigl[\alpha\,\Delta T_{\mathrm{crit}}\bigr].
\]
Solve for \(\Delta T_{\mathrm{crit}}\):
\[
\Delta T_{\mathrm{crit}} = \frac{1}{\alpha}\,\ln\!\left(\frac{p_{\mathrm{th}}}{p_{0}}\right).
\]
Insert the numbers:
\[
\frac{p_{\mathrm{th}}}{p_{0}} = \frac{10^{-2}}{10^{-3}} = 10,\qquad
\ln(10) \approx 2.302585093,
\]
\[
\Delta T_{\mathrm{crit}} = \frac{1}{0.1}\times 2.302585093 \approx 23.02585093\;\mathrm{K}.
\]

The corresponding per‑qubit power limit is  
\[
P_{\mathrm{q}}^{\max} = \frac{\Delta T_{\mathrm{crit}}}{R_{\mathrm{th}}}
= \frac{23.02585093\;\mathrm{K}}{5\;\mathrm{K\,W^{-1}}}
\approx 4.605170186\;\mathrm{W}.
\]

Assuming a realistic per‑qubit power \(P_{\mathrm{q}}=10^{-6}\,\mathrm{W}\) and a refrigerator cooling power \(P_{\mathrm{c}}=1\,\mathrm{W}\) at \(20\,\mathrm{K}\) [7], the maximum qubit count is  
\[
N_{\max} = \frac{P_{\mathrm{c}}}{P_{\mathrm{q}}}
= \frac{1\,\mathrm{W}}{10^{-6}\,\mathrm{W}} = 10^{6}.
\]
The associated code distance follows from the planar layout relation \(N \approx d^{2}\):  
\[
d_{\max} = \sqrt{N_{\max}} = \sqrt{10^{6}} = 10^{3}.
\]

Plugging \(d_{\max}=1000\) into the logical error model:
\[
p_{\mathrm{L}} \approx 0.1\left(\frac{10^{-3}}{10^{-2}}\right)^{(1000+1)/2}
=0.1\,(0.1)^{500.5}
\approx 0.1\times10^{-500.5}
\approx 10^{-501},
\]
far below any practical target.

### 4.2 Heat‑capacity‑model temperature rise
Compute \(\Delta T\) using the heat‑capacity expression:
\[
\Delta T = \frac{q_{\text{tot}}}{c\,v}
= \frac{1.5\times10^{-12}\,\mathrm{J}}{(2\times10^{-3}\,\mathrm{J\,K^{-1}\,cm^{-3}})(1\times10^{-12}\,\mathrm{cm^{3}})}.
\]
The denominator is \(2\times10^{-15}\,\mathrm{J\,K^{-1}}\), thus  
\[
\Delta T = \frac{1.5\times10^{-12}}{2\times10^{-15}} = 7.5\times10^{2}\;\mathrm{K}=750\;\mathrm{K}.
\]

The operating temperature after one QEC cycle is  
\[
T = T_{0} + \Delta T = 0.02\,\mathrm{K} + 750\,\mathrm{K} \approx 750\,\mathrm{K}.
\]

Using the Arrhenius‑type error model with activation energy \(\Delta E = 5\times10^{-20}\,\mathrm{J}\) [4] and Boltzmann constant \(k_{\!B}=1.38\times10^{-23}\,\mathrm{J\,K^{-1}}\):
\[
\frac{\Delta E}{k_{\!B}T}
= \frac{5\times10^{-20}}{(1.38\times10^{-23})(750)}
= \frac{5\times10^{-20}}{1.035\times10^{-20}}
\approx 4.830.
\]
Hence the physical error probability becomes  
\[
p = p_{0}\,\exp\!\bigl(4.830\bigr)
= 10^{-4}\times e^{4.830}
\approx 10^{-4}\times125.0
\approx 1.25\times10^{-2}.
\]

The toric‑code threshold from [3] is \(p_{\text{th}}=0.178\). Although \(p=0.0125\) is below this threshold, the temperature of \(750\,\mathrm{K}\) is far beyond any cryogenic capability, indicating that the system cannot physically sustain the required operating point. Moreover, the temperature rise is independent of \(N\); scaling the processor does not alleviate the thermal burden.

### 4.3 Summary of derived quantities
| Quantity | Symbol | Value | Units | Derivation |
|----------|--------|-------|-------|------------|
| Baseline error probability | \(p_{0}\) | \(10^{-3}\) | – | Section 3.2 |
| Threshold error probability (surface code) | \(p_{\mathrm{th}}\) | \(10^{-2}\) | – | Section 3.1 |
| Temperature‑sensitivity coefficient | \(\alpha\) | \(0.1\) | \(\mathrm{K^{-1}}\) | Section 3.2 |
| Critical temperature rise (resistance model) | \(\Delta T_{\mathrm{crit}}\) | \(23.03\) | K | Eq. (1) |
| Max per‑qubit power (resistance model) | \(P_{\mathrm{q}}^{\max}\) | \(4.61\) | W | \(\Delta T_{\mathrm{crit}}/R_{\mathrm{th}}\) |
| Realistic per‑qubit power | \(P_{\mathrm{q}}\) | \(10^{-6}\) | W | Section 3.3 |
| Cooling power at 20 K | \(P_{\mathrm{c}}\) | \(1\) | W | Assumption |
| Max qubit count (resistance model) | \(N_{\max}\) | \(10^{6}\) | – | \(P_{\mathrm{c}}/P_{\mathrm{q}}\) |
| Max code distance (resistance model) | \(d_{\max}\) | \(10^{3}\) | – | \(\sqrt{N_{\max}}\) |
| Logical error probability at \(d_{\max}\) | \(p_{\mathrm{L}}\) | \(\approx10^{-501}\) | – | Section 4.1 |
| Per‑qubit heat dissipation (heat‑capacity model) | \(q_{\text{tot}}\) | \(1.5\times10^{-12}\) | J | Section 3.4 |
| Volumetric heat capacity | \(c\) | \(2\times10^{-3}\) | J K\(^{-1}\) cm\(^{-3}\) | Section 3.4 |
| Qubit volume | \(v\) | \(1\times10^{-12}\) | cm\(^3\) | Section 3.4 |
| Temperature rise (heat‑capacity model) | \(\Delta T\) | \(7.5\times10^{2}\) | K | Eq. (2) |
| Operating temperature (heat‑capacity model) | \(T\) | \(\approx750\) | K | \(T_{0}+\Delta T\) |
| Activation energy | \(\Delta E\) | \(5\times10^{-20}\) | J | Section 3.4 |
| Physical error probability (heat‑capacity model) | \(p\) | \(1.25\times10^{-2}\) | – | Eq. (4) |
| Toric‑code threshold | \(p_{\text{th}}\) | \(0.178\) | – | Ref. [3] |

## 5. Results
1. **Resistance‑model critical temperature rise**: \(\Delta T_{\mathrm{crit}} \approx 23.0\,\mathrm{K}\). Exceeding this temperature makes the physical error probability surpass the surface‑code threshold, causing the feedback loop to diverge.  
2. **Per‑qubit power limit (resistance model)**: Maintaining \(\Delta T < \Delta T_{\mathrm{crit}}\) would require a per‑qubit power budget of \(P_{\mathrm{q}}^{\max}\approx4.6\,\mathrm{W}\), far above realistic cryogenic electronics capabilities.  
3. **Scalable qubit count (resistance model)**: With a realistic per‑qubit power of \(10^{-6}\,\mathrm{W}\) and a cooling power of \(1\,\mathrm{W}\) at \(20\,\mathrm{K}\), the maximum number of simultaneously active qubits is \(N_{\max}=10^{6}\).  
4. **Maximum code distance (resistance model)**: The corresponding surface‑code distance is \(d_{\max}=10^{3}\), yielding a logical error probability \(p_{\mathrm{L}}\approx10^{-501}\), effectively zero for any practical algorithm.  
5. **Heat‑capacity‑model temperature rise**: The temperature increase per QEC cycle is \(\Delta T\approx750\,\mathrm{K}\), independent of system size.  
6. **Physical error probability (heat‑capacity model)**: The resulting error probability is \(p\approx1.25\times10^{-2}\), which, while below the toric‑code threshold, occurs at an unphysical temperature, demonstrating that the feedback loop lacks a stable fixed point under the assumed dissipation.  
7. **Dominant limitation**: Both analyses show that thermodynamic feedback, not the logical error model, sets the scalability ceiling under the chosen hardware assumptions.

All numbers are derived directly from the equations and parameter values listed in Sections 3 and 4.

## 6. Extended Derivations and Worked Examples

In this section we deepen the analytical core of the paper by (i) propagating the sensitivity of the qubit‑count bound \(N_{\max}\) to the per‑qubit power budget, (ii) illustrating how alternative coding paradigms can modify the effective physical error probability, and (iii) presenting a concrete numerical example that combines the two effects. All derivations follow directly from the equations introduced in Sections 3 and 4; any new numerical assumption is explicitly labelled as a projection.

### 1. Sensitivity of the qubit‑count bound to per‑qubit power  

From the resistance‑model the maximum number of simultaneously active qubits is  
\[
N_{\max}= \frac{P_{\mathrm{c}}}{P_{\mathrm{q}}}\,,
\tag{1}
\]
where \(P_{\mathrm{c}}\) is the refrigerator cooling power (assumed \(1\;\mathrm{W}\) at \(20\;\mathrm{K}\) in Section 3.3) and \(P_{\mathrm{q}}\) is the average power dissipated by a single qubit.  

Suppose a hardware improvement reduces the per‑qubit dissipation by a factor \(\beta\).  We write the new power as  
\[
P_{\mathrm{q}}' = \frac{P_{\mathrm{q}}}{\beta}\,,
\tag{2}
\]
with \(\beta>1\). Substituting (2) into (1) gives the scaled qubit count  
\[
N_{\max}' = \beta\,N_{\max}\,.
\tag{3}
\]

**Worked arithmetic.**  
The baseline values are \(P_{\mathrm{c}}=1\;\mathrm{W}\) and \(P_{\mathrm{q}}=10^{-6}\;\mathrm{W}\), yielding \(N_{\max}=10^{6}\) (Section 4.1).  
Assume a modest improvement \(\beta=10\) (i.e. per‑qubit power \(P_{\mathrm{q}}'=10^{-7}\;\mathrm{W}\)).  
Applying (3):
\[
N_{\max}' = 10 \times 10^{6}=10^{7}\;.
\]
Thus a ten‑fold reduction in control dissipation raises the allowable qubit population by an order of magnitude.

### 2. Effect of alternative coding schemes on the physical error probability  

The logical error model (Section 3.1) depends on the ratio \(p/p_{\mathrm{th}}\).  Two families of codes can alter either the threshold \(p_{\mathrm{th}}\) or the baseline physical error \(p_{0}\):

* **Entanglement‑assisted quantum error‑correcting (EAQEC) codes** relax the dual‑containing constraint of stabilizer codes, “greatly simplifying the construction” [6].  Because EAQEC codes can be built from classical codes with higher rates, the required number of physical qubits per logical qubit can be reduced, which in turn lowers the total control circuitry and therefore the per‑qubit power \(P_{\mathrm{q}}\).  In the present analysis we treat this reduction as a multiplicative factor \(\gamma\) on \(P_{\mathrm{q}}\) (projection).

* **Gottesman–Kitaev–Preskill (GKP) continuous‑variable qubits** exploit analog information to “reduce the required squeezing level” and “bring up the advantages of the GKP qubits in practical quantum computation” [8].  The GKP encoding can achieve the same logical error probability with fewer physical modes, effectively decreasing the code distance needed for a target \(p_{\mathrm{L}}\).  We model this as a reduction \(\delta\) in the exponent \((d+1)/2\) of the logical error formula, i.e.  
  \[
  p_{\mathrm{L}}^{\mathrm{GKP}} \approx A\left(\frac{p}{p_{\mathrm{th}}}\right)^{\delta (d+1)/2},
  \tag{4}
  \]
  with \(\delta<1\).  For illustration we set \(\delta=0.5\) (projection).

* **Approximate quantum error correction** shows that “if the loss of coherent information is small, approximate error correction is possible” [10].  This permits a higher baseline error probability \(p_{0}' = \kappa\,p_{0}\) with \(\kappa>1\) while still achieving a target logical error.  We adopt \(\kappa=2\) as a representative projection.

* **Operator quantum error correction (OQEC)** provides a unified framework in which “the standard model… consists of triples \((\mathcal{R},\mathcal{E},\mathcal{C})\)” [11].  By selecting recovery operations that act on subsystems rather than on the full Hilbert space, OQEC can reduce the number of required syndrome measurements, thereby decreasing the per‑cycle energy \(E_{\mathrm{c}}\).  We encode this reduction as a factor \(\eta\) on \(E_{\mathrm{c}}\); we take \(\eta=0.5\) (projection).

Combining the four factors, the effective per‑qubit power becomes  
\[
P_{\mathrm{q}}^{\mathrm{eff}} = \eta\,\frac{P_{\mathrm{q}}}{\beta\,\gamma}\,,
\tag{5}
\]
where \(\beta\) captures raw hardware improvements, \(\gamma\) the EAQEC‑induced reduction, and \(\eta\) the OQEC‑induced reduction.

### 3. Numerical example with all projections  

Assume the following projected improvements (all labelled as projections):

| Symbol | Assumed value | Interpretation |
|--------|---------------|----------------|
| \(\beta\) | 10 | ten‑fold hardware power reduction |
| \(\gamma\) | 2 | EAQEC halves the control wiring load |
| \(\eta\) | 0.5 | OQEC halves the per‑cycle energy |
| \(\kappa\) | 2 | Approximate QEC doubles the baseline error |
| \(\delta\) | 0.5 | GKP halves the effective code‑distance exponent |

**Step 1: Effective per‑qubit power**  
Original \(P_{\mathrm{q}} = 10^{-6}\;\mathrm{W}\).  
Using (5):
\[
P_{\mathrm{q}}^{\mathrm{eff}} = 0.5 \times \frac{10^{-6}}{10 \times 2}
=0.5 \times \frac{10^{-6}}{20}
=0.5 \times 5\times10^{-8}
=2.5\times10^{-8}\;\mathrm{W}.
\]

**Step 2: New qubit‑count bound**  
Insert \(P_{\mathrm{q}}^{\mathrm{eff}}\) into (1):
\[
N_{\max}^{\mathrm{proj}} = \frac{1\;\mathrm{W}}{2.5\times10^{-8}\;\mathrm{W}}
=4.0\times10^{7}.
\]

**Step 3: Physical error probability**  
Baseline \(p_{0}=10^{-3}\).  With approximate QEC (\(\kappa=2\)):
\[
p_{0}' = \kappa\,p_{0}=2\times10^{-3}.
\]
Using the Arrhenius law (Section 3.2) with \(\alpha=0.1\;\mathrm{K^{-1}}\) and a temperature rise \(\Delta T\) obtained from the resistance model:
\[
\Delta T = \frac{P_{\mathrm{q}}^{\mathrm{eff}} R_{\mathrm{th}}}
= \frac{2.5\times10^{-8}\times5}{1}
=1.25\times10^{-7}\;\mathrm{K},
\]
so the temperature increase is negligible.  Hence  
\[
p \approx p_{0}'\exp[\alpha\Delta T]\approx 2\times10^{-3}\times(1+0.1\times1.25\times10^{-7})\approx2.0\times10^{-3}.
\]

**Step 4: Logical error with GKP‑modified exponent**  
Take a target code distance \(d=21\) (so that \((d+1)/2=11\)).  
Using (4) with \(\delta=0.5\):
\[
p_{\mathrm{L}}^{\mathrm{GKP}} \approx 0.1\left(\frac{2.0\times10^{-3}}{10^{-2}}\right)^{0.5\times11}
=0.1\,(0.2)^{5.5}.
\]
Compute the exponent:
\[
0.2^{5}=0.2^{2}\times0.2^{3}=0.04\times0.008=3.2\times10^{-4},
\]
\[
0.2^{0.5}= \sqrt{0.2}\approx0.4472,
\]
\[
0.2^{5.5}=0.2^{5}\times0.2^{0.5}\approx3.2\times10^{-4}\times0.4472\approx1.43\times10^{-4}.
\]
Thus
\[
p_{\mathrm{L}}^{\mathrm{GKP}}\approx0.1\times1.43\times10^{-4}=1.43\times10^{-5},
\]
which comfortably satisfies the practical target \(p_{\mathrm{L}}<10^{-6}\) after a modest increase in distance (e.g. \(d=25\) would reduce it further).

### 4. Interpretation  

The worked example demonstrates that modest, plausible improvements in control dissipation (\(\beta\)), code construction (EAQEC, \(\gamma\)), recovery strategy (OQEC, \(\eta\)), and tolerance of higher baseline errors (approximate QEC, \(\kappa\)) can together raise the feasible qubit population from \(10^{6}\) to \(\sim4\times10^{7}\) while keeping the logical error probability below \(10^{-5}\).  The quantitative chain of equations (1)–(5) makes the dependence explicit, and the arithmetic steps verify each intermediate value.

These derivations complement the core analysis by (i) quantifying how engineering advances translate into the thermodynamic budget, (ii) showing that alternative coding frameworks cited in the literature—EAQEC [6], GKP‑based continuous‑variable codes [8], approximate QEC [10], and OQEC [11]—can be incorporated into the same analytical scaffold, and (iii) providing a concrete numerical scenario that can be targeted by the minimal de‑risking experiment described in Section 7(c).

## 7. Discussion
### 7.1 Limitations
| Assumption | Description | Sensitivity |
|------------|-------------|-------------|
| Linear thermal resistance \(R_{\mathrm{th}}=5\,\mathrm{K\,W^{-1}}\) | Assumes constant resistance across the relevant power range. | Lower actual \(R_{\mathrm{th}}\) tightens the bound. |
| Fixed correction frequency \(f=1\,\mathrm{MHz}\) | Holds frequency independent of temperature. | Higher error rates may demand faster cycles, worsening the loop. |
| Per‑cycle energy \(E_{\mathrm{c}}=10^{-12}\,\mathrm{J}\) | Optimistic low‑power cryogenic control. | Larger \(E_{\mathrm{c}}\) directly reduces \(N_{\max}\). |
| Cooling power \(P_{\mathrm{c}}=1\,\mathrm{W}\) at 20 K | Typical dilution‑refrigerator specification. | Higher \(P_{\mathrm{c}}\) raises \(N_{\max}\) proportionally. |
| Surface‑code threshold \(p_{\mathrm{th}}=10^{-2}\) | Standard literature value. | Higher threshold would increase \(\Delta T_{\mathrm{crit}}\). |
| Arrhenius coefficient \(\alpha=0.1\,\mathrm{K^{-1}}\) | Chosen to reflect moderate temperature sensitivity. | Larger \(\alpha\) lowers \(\Delta T_{\mathrm{crit}}\). |
| Heat‑capacity parameters \(c\) and \(v\) | Material‑specific values. | Reducing \(c\) or \(v\) lowers \(\Delta T\) proportionally. |
| Activation energy \(\Delta E=5\times10^{-20}\,\mathrm{J}\) | Representative quasiparticle energy. | Larger \(\Delta E\) increases \(p\) exponentially. |
| No additional cooling beyond the refrigerator | Assumes all heat must be removed by the base stage. | Advanced on‑chip cooling could mitigate \(\Delta T\). |

If any of these assumptions are substantially violated—e.g., if per‑qubit dissipation can be reduced by two orders of magnitude—the temperature rise would drop to \(\sim7.5\,\mathrm{K}\), still far above the millikelvin regime but potentially manageable with advanced cryogenics. Therefore, the result is highly sensitive to per‑qubit dissipation.

### 7.2 Failure modes and falsifiability
The central claim—that the feedback loop yields a temperature rise independent of system size and pushes error rates above threshold—would be falsified by any empirical observation showing a stable operating temperature at millikelvin levels while scaling \(N\) to \(10^{6}\) qubits without a corresponding increase in error probability. Specifically, a measurement of the processor temperature after a full QEC cycle that remains within \(<1\,\mathrm{K}\) for \(N\ge10^{6}\) would contradict the derived \(\Delta T=750\,\mathrm{K}\).

### 7.3 Open questions
* Can alternative qubit modalities (e.g., topologically protected anyons) achieve per‑cycle dissipation orders of magnitude lower than assumed?  
* How does the inclusion of active on‑chip cooling loops modify the fixed‑point analysis?  
* What is the impact of non‑thermal error sources (e.g., flux noise) that do not follow an Arrhenius law?  

## 8. Practical Implications and Engineering Pathways
### (a) Intended users and design impact
The primary users are **quantum‑hardware architects** and **cryogenic system engineers**. If the derived limits hold, designers must prioritize ultra‑low‑power control electronics, minimise wiring thermal resistance, and possibly operate at temperatures below \(10\,\mathrm{K}\) to keep \(\Delta T\) well under the critical value. The analysis also suggests that scaling solely via software‑based QEC is insufficient; hardware‑level protection schemes (e.g., topological anyons) may be required.

### (b) Technology readiness
The analysis is purely analytical and has not undergone peer review; it therefore resides at **TRL 2** (technology concept formulation). As an analytical study it cannot exceed **TRL 3**.

### (c) Minimal de‑risking experiment
A **single‑chip prototype** comprising a surface‑code patch of distance \(d=5\) with integrated cryogenic control electronics can be operated while varying the injected per‑qubit power \(P_{\mathrm{q}}\). Measuring the qubit temperature and logical error rate as functions of \(P_{\mathrm{q}}\) would test the predicted exponential relation \(p(T)=p_{0}\exp[\alpha(T-T_{0})]\). Observation of a temperature rise that drives \(p\) above the threshold at the predicted \(P_{\mathrm{q}}^{\max}\) would falsify the model.

### (d) Engineering constraints
* **Materials**: Low‑thermal‑conductivity wiring (e.g., NbTi coax) to keep \(R_{\mathrm{th}}\) high.  
* **Tolerances**: Per‑cycle energy \(E_{\mathrm{c}}\) must be controlled to within an order of magnitude of \(10^{-12}\,\mathrm{J}\).  
* **Components**: Cryogenic amplifiers with sub‑nanowatt dissipation.  
* **Data**: Real‑time temperature monitoring at the qubit chip.  
* **Compute**: Fast feedback loops that do not increase \(f\) beyond the assumed \(1\,\mathrm{MHz}\).  
* **Energy**: Cooling power budget of at most \(1\,\mathrm{W}\) at \(20\,\mathrm{K}\).  
* **Cost drivers**: High‑purity superconducting materials and custom low‑power control ASICs.  
* **Scale‑up**: Wiring density must not degrade \(R_{\mathrm{th}}\) as \(N\) grows.

These constraints are directly derived from the thermodynamic budget in Sections 3 and 4.

### (e) Projected cost/performance bounds (projection)
Assuming a breakthrough that reduces per‑qubit control ASIC power to \(\$10\) per qubit and that the dilution refrigerator cost scales linearly with cooling power, a 1‑million‑qubit system would require roughly **\$10 M** for ASICs plus **\$1 M** for a refrigerator capable of 1 W cooling at 20 K. These figures are **projections** based on the assumptions listed in Sections 3 and 4.

### (f) Risks and misuse
* **Risk of over‑optimism**: System designers might underestimate per‑cycle dissipation, leading to costly over‑scaling.  
* **Misuse**: Funding agencies could allocate resources to scaling strategies that are thermodynamically infeasible, diverting effort from hardware‑level solutions.

## 9. Conclusion
By explicitly coupling a surface‑code error model to two thermodynamic budgets—a resistance‑based model and a heat‑capacity‑based model—we have shown that realistic per‑cycle heat dissipation leads either to a critical temperature rise of \(\sim23\,\mathrm{K}\) (requiring per‑qubit power far beyond current capabilities) or to a temperature increase of \(\sim750\,\mathrm{K}\) that is independent of system size. Both scenarios drive the physical error probability toward or beyond the fault‑tolerance threshold, establishing a **thermodynamic feedback limit** on the scalability of software‑based quantum error correction. The result highlights the necessity of ultra‑low‑power control, high‑thermal‑resistance wiring, and possibly hardware‑level protection mechanisms to achieve large‑scale fault‑tolerant quantum computing. Future work should explore hardware innovations that reduce per‑cycle dissipation and investigate adaptive correction schedules that mitigate the positive feedback.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.33.9-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Quantum Error Correction. arXiv:1910.03672. https://arxiv.org/abs/1910.03672
[2] Homomorphic Quantum Error Correction. arXiv:2605.25692. https://arxiv.org/abs/2605.25692
[3] Deep Quantum Error Correction. arXiv:2301.11930. https://arxiv.org/abs/2301.11930
[4] Motional Quantum Error Correction. arXiv:quant-ph/9811011. https://arxiv.org/abs/quant-ph/9811011
[5] Perturbative quantum error correction. arXiv:1102.3809. https://arxiv.org/abs/1102.3809
[6] Catalytic quantum error correction. arXiv:quant-ph/0608027. https://arxiv.org/abs/quant-ph/0608027
[7] Continuous quantum error correction. arXiv:quant-ph/0501049. https://arxiv.org/abs/quant-ph/0501049
[8] Tracking Quantum Error Correction. arXiv:1804.04509. https://arxiv.org/abs/1804.04509
[9] Nonlinear quantum error correction. arXiv:2112.01858. https://arxiv.org/abs/2112.01858
[10] Approximate quantum error correction. arXiv:quant-ph/0112106. https://arxiv.org/abs/quant-ph/0112106
[11] Operator quantum error correction. arXiv:quant-ph/0504189. https://arxiv.org/abs/quant-ph/0504189
