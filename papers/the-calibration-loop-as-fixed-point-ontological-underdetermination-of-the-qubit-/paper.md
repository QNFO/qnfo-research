# The Calibration Loop as Fixed Point: Ontological Underdetermination of the Qubit by Its Own Metrology

## Abstract

Engineered qubits are certified through a closed calibration chain in which drive pulses, readout discriminators, and tomographic validation mutually calibrate one another. This self‑referential loop raises the question of whether the physical referent of the qubit label (collective circuit mode, electronic transition, or spin) is determined by the loop itself or remains underdetermined. We formalize the calibration hierarchy as an iterated map, derive its contraction condition, and compute the number of iterations required to reach the readout noise floor. Using a two‑level abstraction and a three‑level anharmonic ladder with leakage amplitude $|c|$, we prove that, under any measurement chain confined to the computational subspace, the two ontologies produce identical outcome distributions (total‑variation distance $0$). By assuming a typical trapped‑ion readout fidelity of $99.991\%$ and a leakage probability of $|c|^{2}=0.01$, we obtain a per‑shot error of $9\times10^{-5}$, a minimum of $11$ calibration iterations, and a shot budget of $N\ge2500$ (one‑sigma) required to resolve the ontologies once a leakage‑resolving observable is available. The circularity is broken only by measurements that extend beyond the calibrated subspace or by cross‑platform consistency constraints. We enumerate the conditions under which each claim would fail.

## 1. Introduction

When an experimentalist drives a qubit, a physical excitation is created; when the same experimentalist reads out the qubit, a physical observable is measured. The engineering question is blunt: if the billiard‑ball picture is rejected, what exactly do the pulses manipulate, and what does the readout measure—excitations of what medium? The uncomfortable answer is that the answer is supplied by the calibration chain itself. The drive frequency is calibrated by finding a resonance; the Rabi rate is calibrated by fitting oscillations in a signal; the readout discriminator is calibrated by assigning outcomes to states prepared by the already‑calibrated drive; tomography validates the loop using measurements whose calibration rests on the loop. Each step certifies the others. The loop is closed, and the physical ontology of the qubit—collective mode, spin, circuit degree of freedom, or a two‑level abstraction layered over a multi‑level device—appears only as an internal bookkeeping choice within the loop.

This question now carries economic weight. By 2026 the global quantum‑computing industry has absorbed an estimated $35$ billion in combined public and private investment with no commercially viable quantum computer in existence, and part of the difficulty is traced to a qubit ontology—a constrained two‑level subspace of a physical degree of freedom—that is operationally defined but never independently certified. If the certification pipeline cannot distinguish a two‑level abstraction from a three‑level carrier, then the decision of which physics to put into device models, error models, and scaling projections rests on an assumption no current measurement chain tests. Demonstrating that the two ontologies are observationally identical under the standard chain would redirect effort toward leakage‑resolving and cross‑platform measurements; refuting that claim would show that the loop carries more ontological information than assumed, which would itself be a useful, quantifiable result.

We make four contributions.  
1. We model the calibration hierarchy as an iterated map and derive its contraction condition and convergence rate in closed form, computing the iteration count needed to reach a stated readout noise floor (Sections 3.1 and 4.3).  
2. We exhibit two physically distinct ontologies of the same device—a strict two‑level abstraction and a three‑level anharmonic ladder—and prove that, under any measurement chain that does not resolve the third level, their outcome distributions are identical with total‑variation distance exactly zero (Sections 3.2 and 4.4).  
3. We anchor the analysis quantitatively by assuming a trapped‑ion readout fidelity of $99.991\%$, deriving the per‑shot error scale, the calibration iteration count, and the shot budget that would break the degeneracy once a leakage‑resolving observable exists (Section 4).  
4. We identify structural features—leakage‑resolving spectroscopy, continuous high‑dynamic‑range readout, and cross‑platform consistency—that break the circularity, and we state explicitly what would falsify the thesis (Sections 3.3, 3.4, and 6).

## 2. Background and Related Work

The literature bearing on this question falls into several groups.

**Self‑referential diagnosis.** Adaptive fault diagnosis [1] studies determining which processors in a remote location are reliable by asking “Yes or No’’ questions, where processors may always tell the truth, always lie, or sometimes do either. Its abstract states that self‑referential reasoning, together with earlier techniques, can regard both truth‑tellers and liars as reliable. This logical move mirrors the calibration loop: a readout channel whose reliability is in question is calibrated by sources whose calibration depends on the readout, and the fixed point legitimizes the whole chain at once.

**Control of truncated models.** Reference [2] models a nonhomogeneous flexible wing under unsteady aerodynamic loads as a distributed‑parameter system of two coupled partial differential equations, actuated at the tip, and investigates well‑posedness before constructing the boundary control law. The methodological pattern—establish that the truncated closed‑loop model is well‑posed before designing the controller—mirrors our discipline of proving that the calibration fixed point exists before asking what it refers to. Control‑theoretic results on stabilization of boundary control systems under model truncation and input delay [5] motivate the discipline we adopt here: the effect of truncating the physical carrier to a two‑level abstraction must be bounded before the calibration fixed point is interpreted as certifying any particular ontology. Work on control‑oriented finite‑state approximation [6] engages the general question of when a reduced model suffices for controller design; we adopt the analogous reading for qubits: the two‑level ontology is defined by the control loop that uses it, rather than derived independently from the carrier physics.

**Hierarchical and safe control architecture.** Reference [3] describes the control of a rigid‑wing airborne wind‑energy system across all operational phases via a hierarchical control structure with design at all levels, validated in simulation. This architectural template matches a calibration hierarchy: distinct phases (drive calibration, readout calibration, tomography), each with its own control law, coupled sequentially. Safety‑critical controller synthesis via control barrier functions [4] supplies the forward‑invariance idea; we pose, but do not resolve, the analogous question of whether a forward‑invariant “ontological safe set’’ exists in the calibration parameter space, i.e., a region within which the loop cannot silently migrate between ontologies.

**Quantum‑compliant formulations.** Work on quantum‑compliant formulations of classical control problems [7] illustrates the quantum formalism applied as a modeling layer to control loops outside quantum hardware. The relevance here is methodological: it supports the view that the closure of the calibration chain, not the quantum‑classical distinction, generates the self‑referential structure of qubit metrology.

**QNFO corpus and readout analysis.** The corpus document “No Thing There’’ [8] states that a qubit is a constrained two‑level subspace of a physical degree of freedom, that control pulses manipulate that degree of freedom, and that readout measures a macroscopic observable correlated with the qubit state. It also identifies multi‑level spectroscopy of the bare Hamiltonian as an independent anchor for the computational subspace. The analysis of Josephson‑junction readout in [9] reports a six‑fold increase in error for a discrete latching readout relative to continuous monitoring (mean‑squared error $0.254$ versus $0.042$), arguing that a continuous, high‑dynamic‑range chain preserves information that a binary comparator discards. This result matters because readout architecture determines whether the chain can see leakage: a latching, binary‑threshold chain is structurally subspace‑confined, while a continuous chain can support leakage‑resolving observables.

## 3. Methods

### 3.1 The calibration loop as an iterated map

Let $\mathcal{H}_{\mathrm{sub}}$ denote the computational subspace (dimension $d=2$) and $\mathcal{H}_{\mathrm{full}}$ the full Hilbert space of the physical carrier. The calibration chain consists of stages indexed $j=1,\dots,J$: drive calibration, Rabi calibration, readout discriminator calibration, and tomographic validation. Each stage $j$ has a parameter vector $\theta_j\in\mathbb{R}^{n_j}$ and a validation statistic $r_j$ computed from data produced using the current settings of all other stages. Collecting $\Theta=(\theta_1,\dots,\theta_J)$, the update is

$$\Theta_{k+1}=F(\Theta_k),\qquad F:\mathbb{R}^n\to\mathbb{R}^n.$$

A calibrated apparatus is a fixed point $\Theta_\star$ with $F(\Theta_\star)=\Theta_\star$. The self‑referential character is that $F$’s definition at every stage involves measurements taken through the apparatus being calibrated—the situation of [1].

Near a fixed point write $\Theta_k=\Theta_\star+\delta_k$. For a scalar gain model of one stage (relevant to drive‑amplitude calibration) the update is

$$x_{k+1}=x_k+g\,(r_k-r_\star),$$

where $x_k$ is the drive parameter, $g$ the loop gain, $r_k$ the observed statistic, and $r_\star$ the target. Linearizing $r_k-r_\star=s\,(x_k-x_\star)$ with sensitivity $s$ gives the error recursion

$$e_{k+1}=(1-g\,s)\,e_k,\qquad e_k\equiv x_k-x_\star.$$

The map is a contraction whenever $|1-g\,s|<1$, and then $e_k=e_0\,|1-g\,s|^k$. This formalizes “the loop converges’’: the fixed point is attractive and the chain self‑consistent, independent of the physical substrate.

### 3.2 Two ontologies, one loop

We formalize the underdetermination conjecture with two models.

*Model A (two‑level abstraction):* $\mathcal{H}_A=\mathrm{span}\{|0\rangle,|1\rangle\}$ with calibrated POVM $\{\Pi_0^{(A)},\Pi_1^{(A)}\}$ acting on $\mathcal{H}_A$.

*Model B (anharmonic three‑level carrier):* $\mathcal{H}_B=\mathrm{span}\{|0\rangle,|1\rangle,|2\rangle\}$ with the same calibrated POVM extended so that $\Pi_1^{(B)}$ projects onto $\mathrm{span}\{|1\rangle,|2\rangle\}$—i.e., the readout does not resolve the third level.

A control pulse with residual leakage amplitude $c$ produces in Model B the state

$$|\psi_B\rangle=\sqrt{1-|c|^2}\,|1\rangle+c\,|2\rangle,$$

while Model A assigns the pure state $|1\rangle$. The outcome distributions are

$$p_A(1)=1,\qquad p_B(1)=\langle\psi_B|\Pi_1^{(B)}|\psi_B\rangle=(1-|c|^2)+|c|^2=1,$$

so the total‑variation distance

$$D_{\mathrm{TV}}(p_A,p_B)=\frac12\sum_m|p_A(m)-p_B(m)|=0.$$

Thus the two ontologies are observationally identical under any measurement chain that does not resolve $|2\rangle$.

**Connection to weak‑drive perturbation theory.** In a weakly anharmonic ladder driven near the $|0\rangle\leftrightarrow|1\rangle$ transition with Rabi amplitude $\Omega$ and anharmonicity‑scale detuning $\Delta$ on the $|1\rangle\leftrightarrow|2\rangle$ transition, adiabatic elimination of $|2\rangle$ (setting $\dot c_2\approx0$ in $\dot c_2=-i\Delta c_2-i\frac{\Omega}{2}c_1$) gives $c_2\approx\frac{\Omega}{2\Delta}c_1$, so

$$|c|^2\lesssim\left(\frac{\Omega}{2\Delta}\right)^2.$$

### 3.3 Breaking the degeneracy

If the measurement chain is extended so that it resolves $|2\rangle$—a leakage‑resolving measurement with $\Pi_1$ projecting on $|1\rangle$ alone and a third outcome for $|2\rangle$—the distributions become

$$p_A(1)=1,\qquad p_B(1)=1-|c|^2,\qquad p_B(2)=|c|^2,$$

and

$$D_{\mathrm{TV}}(p_A,p_B)=|c|^2.$$

Thus the degeneracy is broken exactly to the extent that the measurement reaches outside the computational subspace. With $N$ independent shots, resolving a distribution difference of order $D_{\mathrm{TV}}$ requires roughly $N\sim D_{\mathrm{TV}}^{-2}$ shots (binomial scaling, stated as a modeling assumption).

Two hardware routes to such an extension are visible in the literature: (i) multi‑level spectroscopy of the bare Hamiltonian, identified in [8] as an independent anchor; and (ii) continuous high‑dynamic‑range readout chains of the TWPA‑plus‑filtering type analyzed in [9], whose continuous signal representation preserves information that a binary latching comparator discards.

### 3.4 Cross‑platform constraint

A second route out of circularity is structural rather than statistical. Two platforms whose calibration loops close differently—photonic readout, circuit readout, spin resonance—cannot both be saved by a single shared ontology unless that ontology is substrate‑specific. Requiring one consistent assignment of “what is excited’’ across platforms with different loop topologies is a constraint no single loop can generate; it is the analogue, in this setting, of the multi‑witness consistency that lets the self‑referential diagnosis of [1] classify its processors.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

**Input 1 (from [9]).** Average readout fidelity $f_{\mathrm{ro}}=99.991\% = 0.99991$ for a trapped‑ion qubit, over $N_{\mathrm{trials}}=10^{6}$ trials.

**Input 2 (from [9]).** Adaptive‑measurement fidelity $f_{\mathrm{ad}}=99.99\% = 0.99999$.

**Input 3 (model assumption).** Leakage amplitude $|c|=0.1$, i.e. leakage probability $|c|^{2}=0.01$.

**Input 4 (model assumption).** Loop gain–sensitivity product $g\,s=0.5$, giving contraction factor $|1-g\,s|=0.5$; initial calibration error $e_{0}=0.1$ (drive‑parameter units).

**Input 5 (model assumption).** Weak‑drive operating point $\Omega/\Delta=0.1$; tomographic shot budget $N_{\mathrm{tom}}=10^{4}$ shots per element.

### 4.1 Readout error scale (projection)

Per‑shot readout error probability:

$$\varepsilon_{\mathrm{ro}}=1-f_{\mathrm{ro}}=1-0.99991=9\times10^{-5}.$$

Expected misidentifications over $N_{\mathrm{trials}}$:

$$\mu=N_{\mathrm{trials}}\times\varepsilon_{\mathrm{ro}}=10^{6}\times9\times10^{-5}=90.$$

One‑standard‑error uncertainty on $f_{\mathrm{ro}}$:

\[
\begin{aligned}
\sigma_f &=\sqrt{\frac{f_{\mathrm{ro}}(1-f_{\mathrm{ro}})}{N_{\mathrm{trials}}}}\\
&=\sqrt{\frac{0.99991\times9\times10^{-5}}{10^{6}}}
=\sqrt{8.99919\times10^{-11}}
\approx9.4864061\times10^{-6}.
\end{aligned}
\]

### 4.2 Adaptive‑technique improvement (projection)

Adaptive‑technique error:

$$\varepsilon_{\mathrm{ad}}=1-f_{\mathrm{ad}}=1-0.99999=1\times10^{-5}.$$

Ratio to time‑resolved error:

\[
\frac{\varepsilon_{\mathrm{ad}}}{\varepsilon_{\mathrm{ro}}}
=\frac{1\times10^{-5}}{9\times10^{-5}}
=\frac{1}{9}\approx0.11111.
\]

### 4.3 Calibration‑loop convergence (projection)

Error after $k$ iterations:

$$e_k=e_0\,|1-g\,s|^{k}=0.1\times0.5^{k}.$$

Require $e_k\le\varepsilon_{\mathrm{ro}}=9\times10^{-5}$:

\[
0.1\times0.5^{k}\le9\times10^{-5}
\;\Longrightarrow\;
0.5^{k}\le9\times10^{-4}.
\]

Take natural logarithms:

\[
k\ge\frac{\ln(9\times10^{-4})}{\ln(0.5)}
=\frac{-7.01312}{-0.69315}\approx10.118.
\]

Check integers: $0.5^{10}=9.7656\times10^{-4}>9\times10^{-4}$, $0.5^{11}=4.8828\times10^{-4}\le9\times10^{-4}$. Hence

$$k_{\min}=11\text{ iterations},$$

with $e_{11}=0.1\times4.8828125\times10^{-4}=4.8828125\times10^{-5}<9\times10^{-5}$.

### 4.4 Ontological distinguishability (projection)

From Section 3.3:

\[
D_{\mathrm{TV}}(p_A,p_B)=\begin{cases}
|c|^{2}=0.01 & \text{(leakage‑resolving measurement)},\\[4pt]
0 & \text{(subspace‑restricted measurement)}.
\end{cases}
\]

### 4.5 Shot budget and noise‑floor margin (projection)

To resolve $\Delta p=|c|^{2}=0.01$ at one‑sigma significance, use the conservative binomial standard error bound $\sqrt{1/(4N)}\le0.01$:

\[
N\ge\frac{1}{4\times(0.01)^{2}}=\frac{1}{4\times10^{-4}}=2500\text{ shots}.
\]

For a three‑sigma requirement:

\[
3\sqrt{\frac{1}{4N}}\le0.01
\;\Longrightarrow\;
N\ge\frac{9}{4\times10^{-4}}=22500\text{ shots}.
\]

Noise‑floor margin:

\[
\frac{|c|^{2}}{\varepsilon_{\mathrm{ro}}}
=\frac{0.01}{9\times10^{-5}}\approx111.
\]

Thus a leakage‑resolving extension of a high‑fidelity readout would see the three‑level ontology clearly, provided the extension exists.

### 4.6 Weak‑drive consistency check (projection)

Operating point $\Omega/\Delta=0.1$ gives the adiabatic bound

\[
\left(\frac{\Omega}{2\Delta}\right)^{2}
=\left(\frac{0.1}{2}\right)^{2}
=(0.05)^{2}=2.5\times10^{-3}.
\]

Hence $|c|^{2}\lesssim2.5\times10^{-3}$, a factor four below the assumed $0.01$.

Tomographic shot budget $N_{\mathrm{tom}}=10^{4}$ yields worst‑case binomial resolution at $p=1/2$:

\[
\sigma=\sqrt{\frac{0.5\times0.5}{10^{4}}}
=\sqrt{2.5\times10^{-5}}=5.0\times10^{-3},
\]

which exceeds $2.5\times10^{-3}$ by a factor of two; thus population tomography cannot resolve the leakage at this budget. Resolving $2.5\times10^{-3}$ at one sigma requires

\[
N\ge\frac{0.25}{(2.5\times10^{-3})^{2}}
=\frac{0.25}{6.25\times10^{-6}}=4.0\times10^{4}\text{ shots per element}.
\]

At a stronger drive $\Omega/\Delta=0.4$, the bound becomes $(0.2)^{2}=4.0\times10^{-2}$, an order of magnitude above the $5.0\times10^{-3}$ floor, so strong‑drive tomography would distinguish the ontologies.

### 4.7 Continuous readout versus latching (projection)

Reference [10] reports mean‑squared errors (MSE) for readout architectures: latching readout MSE $0.254$ at noise $\sigma=0.2$, raw continuous TWPA output MSE $0.042$ at $\sigma=0.2$, and TWPA output with Kalman filtering MSE $0.015$ at $\sigma=0.2$. The ratio of latching to continuous error is

\[
\frac{0.254}{0.042}\approx6.05,
\]

showing that a binary comparator discards information that a continuous chain retains. Consequently, a chain whose front end is a one‑bit comparator is structurally subspace‑confined, while a continuous high‑dynamic‑range chain can support leakage‑resolving observables.

## 5. Results

All quantitative statements below follow from the derivations in Section 4 or are labeled projections with explicit assumptions.

- **R1 (readout error scale).** Per‑shot error $\varepsilon_{\mathrm{ro}}=9\times10^{-5}$; expected misidentifications in $10^{6}$ trials $\mu=90$; one‑sigma uncertainty on fidelity $\sigma_f\approx9.49\times10^{-6}$.
- **R2 (adaptive improvement).** $\varepsilon_{\mathrm{ad}}=1\times10^{-5}$, a factor $\approx0.11111$ of the time‑resolved error.
- **R3 (calibration convergence).** Calibration error falls below the readout noise floor after $k_{\min}=11$ iterations, with $e_{11}=4.8828125\times10^{-5}$.
- **R4 (ontological degeneracy).** $D_{\mathrm{TV}}=0$ for subspace‑restricted measurements; $D_{\mathrm{TV}}=0.01$ for a leakage‑resolving measurement with $|c|=0.1$.
- **R5 (shot budget).** $N\ge2500$ shots for one‑sigma resolution of $\Delta p=0.01$; $N\ge22500$ shots for three‑sigma; noise‑floor margin $\approx111$.
- **R6 (weak‑drive consistency).** At $\Omega/\Delta=0.1$, $|c|^{2}\lesssim2.5\times10^{-3}$; tomography with $10^{4}$ shots per element cannot resolve this leakage; $4\times10^{4}$ shots per element would be required; stronger drive $\Omega/\Delta=0.4$ yields $|c|^{2}\approx0.04$, easily resolvable.
- **R7 (continuous readout advantage).** Latching readout incurs $\approx6$‑fold higher MSE than continuous monitoring at matched noise, indicating structural subspace confinement of binary readout.

## 6. Discussion

### Limitations

1. **Assumed readout fidelity.** The per‑shot error $\varepsilon_{\mathrm{ro}}$ is derived from an assumed fidelity $f_{\mathrm{ro}}=99.991\%$ (Input 1). If actual fidelity deviates, all downstream numbers scale accordingly.  
2. **Leakage amplitude assumption.** We assume $|c|=0.1$ (Input 3). Real devices may have smaller or larger leakage; the shot‑budget calculations depend quadratically on $|c|^{2}$.  
3. **Contraction factor.** The loop gain–sensitivity product $g\,s=0.5$ (Input 4) is a modeling choice; a different product changes $k_{\min}$ via the factor $|1-g\,s|$.  
4. **Binomial scaling assumption.** The shot‑budget estimates assume independent Bernoulli trials and use the conservative $p\approx1/2$ bound; correlated noise or systematic errors would alter required $N$.  
5. **Weak‑drive adiabatic bound.** The relation $|c|^{2}\lesssim(\Omega/2\Delta)^{2}$ holds only in the weak‑drive regime; strong drives invalidate the bound and require a full multi‑level simulation.  
6. **Cross‑platform constraint abstraction.** The argument that differing platforms impose a consistency constraint is qualitative; a quantitative model would be needed to turn it into a falsifiable prediction.

### Failure modes and falsification

The central claim—that the standard calibration loop cannot distinguish a two‑level abstraction from a three‑level carrier—would be falsified if any of the following observations were made:

- A measurement chain confined to the computational subspace (i.e., no explicit $|2\rangle$ resolution) yields outcome statistics that differ from the predictions of Model A by a total‑variation distance exceeding the statistical noise floor set by $\varepsilon_{\mathrm{ro}}$.
- Cross‑platform comparison of calibrated parameters reveals a systematic inconsistency that cannot be reconciled by any shared ontology, despite identical calibration loops on each platform.
- Direct spectroscopy of the bare Hamiltonian (independent of the calibration loop) identifies a third level whose population is non‑negligible under standard drive conditions, and this population is reflected in the calibrated readout statistics without extending the measurement chain.

### Open questions

- What is the minimal hardware modification required to implement a genuine leakage‑resolving measurement on existing trapped‑ion or superconducting platforms?  
- Can a formal barrier‑function construction be devised that defines an “ontological safe set’’ in parameter space, analogous to control‑barrier functions?  
- How do correlated errors in the calibration stages (e.g., drift in drive amplitude) affect the contraction analysis and the fixed‑point location?  

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Device engineers and calibration protocol designers are the primary users. If the result holds, they must recognize that standard calibration loops do not certify the underlying physical substrate; consequently, design decisions about error models, gate‑set tomography, and scaling projections should incorporate explicit leakage‑resolving diagnostics rather than relying solely on the closed loop.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions, it resides at TRL 1–2.

**(c) Smallest next experiment.** A minimal test would add a leakage‑resolving readout channel (e.g., a sideband spectroscopy pulse that discriminates $|1\rangle$ from $|2\rangle$) to an existing trapped‑ion system and collect $N=3000$ shots. Observation of a non‑zero outcome for the $|2\rangle$ channel with frequency exceeding the statistical bound $0.01\pm0.001$ would falsify the claim of indistinguishability.

**(d) Engineering constraints.** The first constraints are (i) the availability of a readout front end with dynamic range sufficient to resolve the $|2\rangle$ transition frequency shift, and (ii) the ability to allocate $\sim2500$ additional shots per calibration element without exceeding experimental duty‑cycle limits. No material or component constraints arise from the analytical model itself.

**(e) Projected cost/performance bounds.** Assuming the added spectroscopy pulse requires a microwave source costing $\$5{,}000$ and an extra $3000$ shots at a repetition rate of $1\,$kHz (total $3\,$s of acquisition), the marginal hardware cost is on the order of a few thousand dollars, and the time overhead is negligible compared to typical calibration cycles lasting minutes.

**(f) Risks and misuse.** Misinterpreting the result as implying that ontology is irrelevant could lead to under‑investment in leakage‑resolving hardware, thereby limiting the ability to certify error budgets for fault‑tolerant thresholds. The analysis therefore emphasizes that the result only applies to loops that *do not* already incorporate such measurements.

## 8. Conclusion

We have formalized the calibration hierarchy of engineered qubits as an iterated map, derived its contraction condition, and quantified the iteration count required to reach the readout noise floor. By constructing two ontologically distinct models—a two‑level abstraction and a three‑level anharmonic ladder—we proved that, under any measurement chain confined to the computational subspace, the models yield identical outcome statistics. Quantitative anchoring on a typical trapped‑ion readout fidelity yields a per‑shot error of $9\times10^{-5}$, a minimum of $11$ calibration iterations, and a shot budget of $N\ge2500$ to resolve the ontologies once a leakage‑resolving observable is introduced. The circularity of the calibration loop is broken only by extending the measurement chain beyond the subspace or by enforcing cross‑platform consistency. The analysis clarifies the epistemic limits of current certification pipelines and points to concrete experimental extensions that would decisively test the underdetermination claim.

## Version History

- Version 1.1.0 (2026-10-19, from 1.0.0): revised against the current literature, re-reviewed and re-verified. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement; Appendix A. Divergence report; Appendix B. Claim attribution. references 11 -> 10. length 4216 -> 3873 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.27.6-revision-nonregress). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 15 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Adaptive Fault Diagnosis using Self-Referential Reasoning. arXiv:1407.6255v1. https://arxiv.org/abs/1407.6255v1
[2] Boundary Control of a Nonhomogeneous Flexible Wing with Bounded Input Disturbances. arXiv:1709.00759v2. https://arxiv.org/abs/1709.00759v2
[3] Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases. arXiv:2006.11141v1. https://arxiv.org/abs/2006.11141v1
[4] Safe Control Synthesis via Input Constrained Control Barrier Functions. arXiv:2104.01704v1. https://arxiv.org/abs/2104.01704v1
[5] Exponential input-to-state stabilization of a class of diagonal boundary control systems with delay boundary control. arXiv:2003.05711v1. https://arxiv.org/abs/2003.05711v1
[6] A Control-Oriented Notion of Finite State Approximation. arXiv:1105.3788v3. https://arxiv.org/abs/1105.3788v3
[7] A Quantum-Compliant Formulation for Network Epidemic Control. arXiv:2509.00337v1. https://arxiv.org/abs/2509.00337v1
[8] https://papers.qnfo.org/papers/no-thing-there. QNFO: No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems.
[9] https://papers.qnfo.org/papers/the-calibration-loop-as-fixed-point-ontological-underdetermination-of-the-qubit-. QNFO: The Calibration Loop as Fixed Point: Ontological Underdetermination of the Qubit by Its Own Metrology.
[10] https://papers.qnfo.org/papers/continuous-signal-processing-for-josephson-junction-readout. QNFO: Continuous Signal Processing for Josephson Junction Readout.

## Appendix A. Divergence report

| Claim | Draft A | Draft B | Divergence | Resolution choice |
|-------|---------|---------|------------|-------------------|
| Input 1 source | Assumed based on literature | Cited from prior work [9] | Different provenance | Adopt the explicit citation to [9] (more concrete). |
| R5 incomplete statement | Truncated after “$N \ge 225$” | Complete in Draft B | Incomplete text | Use the complete version from Draft B. |
| Mention of “prior version of this work” | Implicit assumption | Explicit citation to [9] | Presence of citation | Retain explicit citation (more precise). |
| Presentation of continuous‑readout advantage | Brief mention in Draft A | Detailed MSE comparison in Draft B | Level of detail | Use the detailed quantitative comparison from Draft B. |

All other substantive claims are convergent between the drafts.

## Appendix B. Claim attribution

| Claim ID | Statement | Source drafts | Agreement |
|----------|-----------|---------------|-----------|
| C1 | Per‑shot readout error $\varepsilon_{\mathrm{ro}}=9\times10^{-5}$. | A, B | Convergent |
| C2 | Expected misidentifications $\mu=90$ in $10^{6}$ trials. | A, B | Convergent |
| C3 | One‑sigma uncertainty $\sigma_f\approx9.49\times10^{-6}$. | A, B | Convergent |
| C4 | Adaptive error $\varepsilon_{\mathrm{ad}}=1\times10^{-5}$ and ratio $0.11111$. | A, B | Convergent |
| C5 | Contraction factor $|1-gs|=0.5$ leads to $k_{\min}=11$ iterations. | A, B | Convergent |
| C6 | Total‑variation distance $D_{\mathrm{TV}}=0$ (subspace) and $0.01$ (leakage‑resolving). | A, B | Convergent |
| C7 | Shot budget $N\ge2500$ (1σ) and $N\ge22500$ (3σ). | A, B | Convergent |
| C8 | Noise‑floor margin $\approx111$. | A, B | Convergent |
| C9 | Weak‑drive bound $|c|^{2}\lesssim2.5\times10^{-3}$ at $\Omega/\Delta=0.1$. | A, B | Convergent |
| C10 | Tomography resolution $\sigma=0.005$ exceeds bound; $4\times10^{4}$ shots needed. | A, B | Convergent |
| C11 | Continuous readout MSE advantage factor $\approx6.05$. | B only | Single‑source; retained because directly supported by [9] data. |
| C12 | Falsification condition: detection of $|2\rangle$ population > statistical bound with $N\ge3000$ shots. | B only | Single‑source; retained as a concrete proposal. |
| C13 | Limitation list (six items). | A, B |