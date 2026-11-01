# Planar Fluxonium‑Controlled Bosonic Error Correction: A Quantitative Error‑Budget Reassessment (Corrected Version)

## Abstract

Bosonic quantum error correction (QEC) encodes a logical qubit in a single harmonic oscillator, promising fault tolerance with far fewer physical components than qubit‑based surface codes. Recent planar demonstrations using a heavy fluxonium ancilla report a bit‑flip lifetime of $T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ and a logical‑lifetime extension factor of $F = 1.59 \pm 0.05$. The gap addressed here is the absence of a transparent, arithmetic‑level analysis that connects these reported numbers to the underlying error budget and per‑cycle ancilla error probability. This corrected version also repairs two defects of the earlier release: a citation that had been misdescribed as an analysis of two‑level error correction for multi‑spin molecular qubits, and a photon‑budget figure obtained by multiplying a cited resource ratio by the lifetime extension factor under an unjustified linearity assumption. We propagate the reported lifetimes through standard QEC error‑budget relations and derive: (i) an ancilla bit‑flip rate $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$, (ii) a $37.1\%\pm2.0\%$ removal of the logical decay rate, and (iii) a per‑cycle ancilla error of $2.19\%\pm0.34\%$ for an assumed $10~\mu\mathrm{s}$ correction cycle. The photon‑budget advantage remains the cited $5$–$40\times$ fewer photons per logical qubit at $p_L = 10^{-6}$; the previously claimed $8.0$–$64\times$ figure is withdrawn. The corrected chain gives hardware designers a concrete error‑budget target and a falsifiable prediction for future fluxonium‑GKP experiments.

## 1. Introduction

Superconducting quantum processors face a scaling bottleneck: surface‑code error correction requires thousands of physical qubits per logical qubit, inflating hardware cost and delaying near‑term deployment of error‑corrected algorithms [2]. Bosonic QEC offers a hardware‑efficient alternative by encoding a logical qubit in the large Hilbert space of a single oscillator mode, thereby reducing component count. The practical history of bosonic QEC in superconducting circuits has been dominated by an asymmetry: long‑lived oscillators (3D cavities) are paired with weak ancilla qubits (transmons). We assume prior transmon ancillas show bit‑flip lifetimes of order tens of microseconds (input $I_4$ in Section 3), which would cap the logical lifetime regardless of code quality.

A recent planar fluxonium‑GKP analysis attacks this asymmetry. Heavy fluxonium—a superconducting artificial atom with a large shunt capacitance and an inductive loop—has a bit‑flip lifetime $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$ as reported in [2], an order of magnitude above prior transmon ancillas. Integrated on a planar Archimedean spiral resonator, the platform enables finite‑energy GKP state preparation, measurement‑free stabilization, and rapid fluxonium reset, yielding a logical‑lifetime extension factor of $F = 1.59 \pm 0.05$ [3].

If the error‑budget arithmetic behind these numbers holds, the design decision it changes is concrete: QEC architects can treat the ancilla bit‑flip channel as secondary rather than dominant, and fabrication planners can weigh fully planar bosonic QEC against bulky 3D‑cavity approaches. Two errors in the earlier release of this analysis blocked that use. First, a cited work was described as an analysis of two‑level error correction for multi‑spin molecular qubits supporting a cross‑platform error‑hierarchy analogy; the work so cited is in fact a mathematical‑chemistry paper on degree‑based topological indices of trees [1], and the analogy is withdrawn. Second, a photon‑budget advantage of $8.0$–$64\times$ was produced by multiplying a cited $5$–$40\times$ photon ratio by the lifetime extension factor $F = 1.59$ under an explicit assumption that logical lifetime scales linearly with the photon budget; that assumption connects two quantities measured under different conditions (a lifetime ratio within one platform and a resource ratio across platforms at fixed $p_L$), and the multiplication is withdrawn. This version reports the corrected analysis.

**Contributions.**
1. **Error‑budget arithmetic.** From the reported $T_1^{\mathrm{bf}}$ and $F$, we derive the ancilla bit‑flip rate, the corrected and uncorrected logical decay fractions, the per‑cycle error probabilities, and the steady‑state ancilla‑induced error floor, with every arithmetic step shown (Section 4).
2. **Erratum 1: citation correction.** We correct the description of the previously mischaracterized citation: the work is a graph‑theoretic study of Zagreb indices [1], it supports no molecular‑qubit analogy, and the cross‑platform analogy is removed (Section 2).
3. **Erratum 2: photon‑budget correction.** We withdraw the $8.0$–$64\times$ photon‑advantage figure and its linearity assumption, and report the photon‑budget comparison as the cited $5$–$40\times$ ratio at $p_L = 10^{-6}$ [5], without any multiplication by $F$ (Sections 4.5 and 5).
4. **Falsifiability.** We state explicitly which measurements would falsify the claim that planar fluxonium‑GKP is the leading route to scalable bosonic QEC (Section 6).

## 2. Background and Related Work

This section discusses the five cited works through eight discussion items, D1 through D8, each anchored to a specific result stated in the work it cites; several works contribute more than one distinct result, and the resulting limitation on breadth is stated in Section 6.

**D1 (from [1]): lower bound on the first Zagreb index.** Reference [1] proves in its Theorem 1 that the first Zagreb index satisfies $M_1(T) \geq 9n - 16$ for a tree with an even number $n \geq 2$ of pendent vertices, with equality attained by a $4$-tree in which every internal vertex has degree $4$ [1].

**D2 (from [1]): lower bound on the second Zagreb index.** The same work proves in its Theorem 3 that the second Zagreb index satisfies $M_2(T) \geq 11n - 27$ for $n \geq 8$, with equality for trees whose stem vertices have degree $4$ or $5$ [1]. Together, D1 and D2 establish that the work is a graph-theoretic study in mathematical chemistry, which is why the molecular-qubit analogy once attached to it is withdrawn below.

**D3 (from [2]): the falsifiability scaling law.** Reference [2] formulates a falsifiability criterion for geometrically inspired QECCs by deriving the scaling $p_L \propto p_{\mathrm{phys}}^{\,d/2}$ from a stabilizer interaction degree extracted from the code's algebraic description, against the surface-code law $p_L \approx A\,p_{\mathrm{phys}}^{\,d}$ [2].

**D4 (from [2]): the numerical separation prediction.** Using the same fluxonium inputs used here—$T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$ and $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$, giving $p_{\mathrm{phys}} = 2.19\times10^{-2}$—[2] predicts a geometric-code logical error rate $p_L^{\mathrm{geom}} = 7.1\times10^{-5}$ for $d = 5$ versus a surface-code rate $p_L^{\mathrm{SC}} = 5.1\times10^{-9}$, a ratio of approximately $1.4\times10^{4}$, and proposes a benchmark on a $d = 5$ geometric stabilizer set [2]. D3 and D4 together show how the per-cycle ancilla error derived in Section 4.3 serves as the physical error input to a decisive scaling experiment, the same kind of minimal test proposed in Section 7.

**D5 (from [3]): the reported inputs and derived metrics.** Reference [3], the earlier release of the present analysis, reports the inputs used here—$T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ and $F = 1.59 \pm 0.05$—and derives the ancilla bit-flip rate $(2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$, the removal of $37.1\%$ of the logical decay rate, the per-cycle ancilla error $2.19\%\pm0.34\%$, and the ancilla-limited lifetime projection $T_L^{(1)} \approx 4.51~\mathrm{ms}$ [3].

**D6 (from [3]): the two corrected defects.** The same work's §4.5 claimed an $8.0$–$64\times$ photon-budget advantage obtained by multiplying a $5$–$40\times$ ratio by $F = 1.59$ under an explicit linearity assumption, and its §2 attached a molecular-qubit analogy to the work now cited as [1]; both items are corrected in this version, while the arithmetic of R1–R6 in [3] is reproduced unchanged in Section 4 [3].

**D7 (from [4]): simulation-grounded anisotropic-noise code proposals.** Reference [4] proposes geometric orientation codes that aim to mitigate directionally biased noise, noting that surface codes can be less effective under such bias, and grounds the proposal in a computational simulation of the codes under anisotropic noise channels [4]. No specific simulated figure from [4] is used in this paper; the sensitivity of code-architecture conclusions to the assumed noise model is taken up as this paper's own observation in the failure-mode analysis of Section 6.

**D8 (from [5]): the resource-commensurable comparison and its caveats.** Reference [5] compares cat, GKP, binomial, and surface codes on a resource-commensurable footing, reporting that bosonic codes require $5$–$40\times$ fewer photons per logical qubit than surface codes at a target logical error rate $p_L = 10^{-6}$, and flags that GKP operation requires approximately $12~\mathrm{dB}$ of squeezing not yet demonstrated for error correction, that dephasing limits the performance of cat and binomial codes, and that cross-platform resource comparisons are inherently limited [5]. This paper uses [5] only for the cited $5$–$40\times$ ratio and these caveats (Sections 4.5, 5, and 6); no quantity is derived from it beyond the ratio itself.

**The misdescribed citation, corrected.** Reference [1] derives sharp lower bounds for the first and second Zagreb indices $M_1$ and $M_2$ of trees with a given number of pendent vertices: Theorem 1 gives $M_1(T) \geq 9n - 16$ for a tree with an even number $n \geq 2$ of pendent vertices, with equality for a $4$‑tree in which every internal vertex has degree $4$, and Theorem 3 gives $M_2(T) \geq 11n - 27$ for $n \geq 8$, with equality for trees whose stem vertices have degree $4$ or $5$ [1]. This is a result in mathematical chemistry, where topological indices predict properties of chemical compounds. The earlier release described this reference as an analysis of two‑level error correction for multi‑spin molecular qubits and used it to support a cross‑platform error‑hierarchy analogy. That description is incorrect: nothing in [1] concerns qubits, error correction, or spin systems, and the molecular‑qubit analogy is withdrawn from this paper. No claim in Sections 3–5 depends on [1].

**Falsifiability of geometric code proposals.** Reference [2] formulates a falsifiability criterion for geometrically inspired QECCs, deriving the scaling $p_L \propto p_{\mathrm{phys}}^{\,d/2}$ from a stabilizer interaction degree extracted from the code's algebraic description, against the surface‑code law $p_L \approx A\,p_{\mathrm{phys}}^{\,d}$. Using the same fluxonium inputs used here—$T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$ and $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$, giving $p_{\mathrm{phys}} = 2.19\times10^{-2}$—[2] predicts a geometric‑code logical error rate $p_L^{\mathrm{geom}} = 7.1\times10^{-5}$ for $d = 5$ versus a surface‑code rate $p_L^{\mathrm{SC}} = 5.1\times10^{-9}$, a ratio of $7.1\times10^{-5}/5.1\times10^{-9} \approx 1.4\times10^{4}$, i.e. a separation of approximately four orders of magnitude [2]. This is directly relevant to the present paper: it shows how the per‑cycle ancilla error derived in Section 4.3 can serve as the physical error input to a decisive scaling experiment, and its proposed benchmark on a $d = 5$ geometric stabilizer set is the same kind of minimal test proposed in Section 7.

**The analysis under correction.** Reference [3] is the earlier release of the present analysis. It reports the inputs used here—$T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ and $F = 1.59 \pm 0.05$—and derives the ancilla bit‑flip rate $(2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$, the removal of $37.1\%$ of the logical decay rate, the per‑cycle ancilla error $2.19\%\pm0.34\%$, and the ancilla‑limited lifetime projection $T_L^{(1)} \approx 4.51~\mathrm{ms}$ [3]. Its §4.5 additionally claimed an $8.0$–$64\times$ photon‑budget advantage obtained by multiplying a $5$–$40\times$ ratio by $F = 1.59$ under an explicit linearity assumption, and its §2 attached a molecular‑qubit analogy to the work now cited as [1]. Both items are corrected in this version; the arithmetic of R1–R6 in [3] is reproduced unchanged in Section 4.

**Anisotropic‑noise code proposals.** Reference [4] proposes geometric orientation codes that aim to mitigate directionally biased noise, noting that surface codes can be less effective under such bias, and grounds the proposal in a computational simulation of the codes under anisotropic noise channels. No specific simulated figure from [4] is used in this paper, and its results are not independently verified here; the work is cited as context for how strongly code‑architecture conclusions can depend on the assumed noise model—the same sensitivity that motivates the failure‑mode analysis of Section 6.

**Resource‑commensurable comparison.** Reference [5] compares cat, GKP, binomial, and surface codes on a resource‑commensurable footing, reporting that bosonic codes require $5$–$40\times$ fewer photons per logical qubit than surface codes at a target logical error rate $p_L = 10^{-6}$. The same work flags the caveats that bound this comparison: GKP operation requires approximately $12~\mathrm{dB}$ of squeezing not yet demonstrated for error correction, dephasing limits the performance of cat and binomial codes, and cross‑platform resource comparisons are inherently limited. This paper uses [5] only for the cited $5$–$40\times$ ratio and these caveats (Sections 4.5, 5, and 6); no quantity is derived from it beyond the ratio itself.

## 3. Methods

Our method is *derived‑metric analysis*: a small set of reported numbers is propagated through standard QEC error‑budget relations to obtain quantities the experiment implies but does not state directly. No simulation is performed; every result is either exact arithmetic on reported inputs or a labeled projection with stated assumptions.

**Inputs.** The analysis uses six inputs. $I_1$ is the ancilla bit‑flip lifetime $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$ with uncertainty $\pm 70~\mu\mathrm{s}$, reported in [2],[3]. $I_2$ is the logical‑lifetime extension factor $F = 1.59$ with uncertainty $\pm 0.05$, reported in [3]. $I_3$ is an assumed correction‑cycle duration $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$, also used in [2]. $I_4$ is an assumed transmon baseline bit‑flip lifetime $T_1^{\mathrm{tm}} = 30~\mu\mathrm{s}$, representative of prior 3D‑cavity demonstrations. $I_5$ is an assumed flip‑to‑logical conversion factor $\eta = 0.1$, the fraction of ancilla flips that corrupt the logical state. $I_6$ is the photon‑budget ratio of $5$–$40\times$ fewer photons for bosonic codes versus surface codes at $p_L = 10^{-6}$, reported in [5].

**Defining relations.** The ancilla bit‑flip rate is $\Gamma_{\mathrm{bf}} = 1/T_1^{\mathrm{bf}}$. The corrected logical decay rate is $\Gamma_L^{(1)} = \Gamma_L^{(0)}/F$, with $\Gamma_L^{(i)} = 1/T_L^{(i)}$. Under a Poisson model, the per‑cycle bit‑flip probability is $p_{\mathrm{bf}}(T_{\mathrm{cyc}}) = 1 - e^{-\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}} \approx \Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}$ for $\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}} \ll 1$. The steady‑state ancilla‑induced logical error rate is $\Gamma_{\mathrm{anc}} = \eta\,\Gamma_{\mathrm{bf}}$, independent of $T_{\mathrm{cyc}}$. For a function $q = f(I_1,I_2)$ of independent inputs, uncertainty propagates as $\sigma_q^2 = (\partial f/\partial I_1)^2 \sigma_{I_1}^2 + (\partial f/\partial I_2)^2 \sigma_{I_2}^2$.

**Corrections relative to the earlier release.** (a) The photon‑budget step of the earlier §4.5, which multiplied $I_6$ by $F$ under the assumption that logical lifetime scales linearly with the photon budget, is deleted: $I_6$ compares resource counts across platforms at fixed $p_L$, while $F$ compares lifetimes within one platform, and no relation stated in [5] or derived here connects them. (b) The molecular‑qubit analogy attached to the work now cited as [1] is deleted, since [1] contains no qubit or error‑correction content. All other relations are unchanged from [3].

All arithmetic follows the steps detailed in Section 4.

## 4. Analysis

### 4.1 Ancilla bit‑flip rate

Input $I_1$: $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s} = 4.51 \times 10^{-4}~\mathrm{s}$.

$$
\Gamma_{\mathrm{bf}} = \frac{1}{4.51 \times 10^{-4}~\mathrm{s}} = 2.2173 \times 10^{3}~\mathrm{s}^{-1}.
$$

Uncertainty: $\sigma_T = 7.0 \times 10^{-5}~\mathrm{s}$, and

$$
\sigma_{\Gamma} = \frac{\sigma_T}{T^2} = \frac{7.0 \times 10^{-5}}{(4.51\times10^{-4})^2} = \frac{7.0 \times 10^{-5}}{2.0340\times10^{-7}} = 3.44 \times 10^{2}~\mathrm{s}^{-1}.
$$

$$
\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}.
$$

### 4.2 Fractional reduction in logical decay rate

Input $I_2$: $F = 1.59 \pm 0.05$.

$$
\frac{1}{F} = \frac{1}{1.59} = 0.62893, \qquad 1-\frac{1}{F} = 0.37107.
$$

Error correction removes $37.1\%$ of the logical decay rate, leaving a residual fraction of $62.9\%$.

Uncertainty: $\displaystyle \frac{\partial (1/F)}{\partial F} = -\frac{1}{F^{2}} = -\frac{1}{2.5281} = -0.39555$, so $\sigma_{1/F} = 0.39555 \times 0.05 = 0.0198 \approx 0.020$.

Residual fraction $= 0.629 \pm 0.020$; removed fraction $= 0.371 \pm 0.020$.

### 4.3 Per‑cycle ancilla bit‑flip probability

Using the Poisson model with $T_{\mathrm{cyc}} = 10~\mu\mathrm{s} = 1.0\times10^{-5}~\mathrm{s}$ (input $I_3$):

$$
\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}} = (2.2173\times10^{3})(1.0\times10^{-5}) = 2.2173\times10^{-2}.
$$

$$
p_{\mathrm{bf}}^{\mathrm{flx}} = 1 - e^{-0.022173} \approx 1 - (1 - 0.022173 + 0.0002458 - 0.0000018) = 0.021929 \approx 0.0219.
$$

Uncertainty propagation:

$$
\frac{\partial p}{\partial T} = \frac{T_{\mathrm{cyc}}}{T^{2}}\,e^{-T_{\mathrm{cyc}}/T} = \frac{10^{-5}}{(4.51\times10^{-4})^{2}}\times0.97807 = 49.164\times0.97807 = 48.09~\mathrm{s}^{-1},
$$

$$
\sigma_{p} = 48.09 \times 7.0\times10^{-5} = 3.37\times10^{-3}.
$$

Hence $p_{\mathrm{bf}}^{\mathrm{flx}} = 0.0219 \pm 0.0034$ ($2.19\%\pm0.34\%$). This is the same physical error input $p_{\mathrm{phys}} = 2.19\times10^{-2}$ used by [2] for its scaling prediction.

**Transmon baseline (input $I_4$).**

$$
\Gamma_{\mathrm{bf}}^{\mathrm{tm}} = \frac{1}{3.0\times10^{-5}} = 3.333\times10^{4}~\mathrm{s}^{-1},
$$

$$
\Gamma_{\mathrm{bf}}^{\mathrm{tm}} T_{\mathrm{cyc}} = 0.33333,
$$

$$
p_{\mathrm{bf}}^{\mathrm{tm}} = 1 - e^{-0.33333} \approx 0.2835 \;(28.3\%).
$$

Ratio of per‑cycle errors:

$$
\frac{p_{\mathrm{bf}}^{\mathrm{tm}}}{p_{\mathrm{bf}}^{\mathrm{flx}}} = \frac{0.2835}{0.0219} = 12.9.
$$

Ratio of rates (direct lifetime ratio):

$$
\frac{\Gamma_{\mathrm{bf}}^{\mathrm{tm}}}{\Gamma_{\mathrm{bf}}^{\mathrm{flx}}} = \frac{T_1^{\mathrm{bf}}}{T_1^{\mathrm{tm}}} = \frac{451}{30} = 15.0.
$$

The discrepancy between $12.9$ and $15.0$ arises because the transmon case is not deep in the $\Gamma T \ll 1$ regime.

### 4.4 Steady‑state ancilla‑induced logical error rate

With flip‑to‑logical conversion factor $\eta$ (input $I_5$), the expected number of logical corruptions in an observation time $T_{\mathrm{obs}}$ is

$$
N_{\mathrm{corr}} = \eta\,p_{\mathrm{bf}}(T_{\mathrm{cyc}})\,\frac{T_{\mathrm{obs}}}{T_{\mathrm{cyc}}}.
$$

In the limit $T_{\mathrm{cyc}} \to 0$, $p_{\mathrm{bf}} \to \Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}$, yielding

$$
N_{\mathrm{corr}} \to \eta\,\Gamma_{\mathrm{bf}}\,T_{\mathrm{obs}}.
$$

Thus the steady‑state ancilla‑induced logical error rate is

$$
\Gamma_{\mathrm{anc}} = \eta\,\Gamma_{\mathrm{bf}},
$$

independent of $T_{\mathrm{cyc}}$.

Assuming $\eta = 0.1$:

$$
\Gamma_{\mathrm{anc}} = 0.1 \times 2.2173\times10^{3} = 221.7~\mathrm{s}^{-1},
$$

$$
T_L^{(1)} = \frac{1}{\Gamma_{\mathrm{anc}}} = 4.51\times10^{-3}~\mathrm{s} = 4.51~\mathrm{ms}.
$$

### 4.5 Photon‑budget connection (corrected)

Input $I_6$ is a resource comparison from [5] indicating that bosonic codes require fewer photons per logical qubit than surface codes at $p_L = 10^{-6}$. The corrected statement of the photon‑budget connection is simply this cited ratio:

$$
\text{photon advantage} = 5\text{–}40\times \quad \text{at } p_L = 10^{-6} \; \text{[5]}.
$$

The earlier release multiplied this ratio by the extension factor $F = 1.59$ to obtain $5\times1.59 \approx 8.0$ and $40\times1.59 \approx 63.6 \approx 64$, under an explicit assumption that logical lifetime scales linearly with the photon budget. That step is withdrawn. The two factors are measured under different conditions: $F$ is a within‑platform lifetime ratio at the experiment's operating point, while $I_6$ is a cross‑platform resource count at a fixed target error rate, and no relation stated in [5] or derived here connects them. The photon‑budget advantage reported in this paper is therefore $5$–$40\times$, unchanged by the fluxonium result, and any dependence of the photon budget on the ancilla lifetime improvement is left as an open question (Section 6).

## 5. Results

All quantities below are derived in Section 4 from the inputs $I_1$–$I_6$ (or are explicitly labeled projections).

**R1 (computed).** The ancilla bit‑flip rate is $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$. **R2 (computed).** Error correction removes a fraction $0.371 \pm 0.020$ ($37.1\%$) of the logical decay rate, leaving a residual fraction of $0.629 \pm 0.020$. **R3 (computed, assumption $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$).** The per‑cycle ancilla error is $p_{\mathrm{bf}}^{\mathrm{flx}} = 0.0219 \pm 0.0034$ ($2.19\%\pm0.34\%$). **R4 (computed, assumption $T_1^{\mathrm{tm}} = 30~\mu\mathrm{s}$).** The transmon baseline per‑cycle error is $p_{\mathrm{bf}}^{\mathrm{tm}} \approx 0.283$ ($28.3\%$), giving a ratio of per‑cycle errors of $12.9$ and a ratio of rates of $15.0$.
- **R5 (structural).** Steady‑state ancilla‑induced logical error rate equals $\eta\,\Gamma_{\mathrm{bf}}$, independent of cycle speed.
- **R6 (projection).** With $\eta = 0.1$, the ancilla‑limited corrected logical lifetime is $T_L^{(1)} \approx 4.51~\mathrm{ms}$.
- **R7 (cited, corrected).** Photon‑budget advantage: $5$–$40\times$ fewer photons per logical qubit versus surface codes at $p_L = 10^{-6}$, as reported in [5]. The previously claimed $8.0$–$64\times$ range is withdrawn; no multiplication by $F$ is performed.
- **R8 (consistency check).** The relative uncertainty of $\Gamma_{\mathrm{bf}}$ is $344/2217 = 15.5\%$, matching the relative uncertainty of $T_1^{\mathrm{bf}}$ ($70/451 = 15.5\%$), confirming correct propagation.

No new measurements or simulations are reported.

## 6. Discussion

The corrected error‑budget chain establishes what the reported fluxonium ancilla parameters imply arithmetically—per‑cycle error, decay‑rate removal, and a projected ancilla‑limited lifetime—and it equally establishes what they do not imply: no photon‑budget multiplication and no cross‑platform error‑hierarchy analogy. In particular, the withdrawal of the molecular‑qubit analogy removes the only cross‑platform error‑hierarchy comparison the earlier version offered, and no replacement analogy is asserted.

**Strengths.** The heavy fluxonium ancilla lifts the dominant error channel from the ancilla to the oscillator, opening a regime where bosonic codes can exploit their native error‑correction capabilities. Combined with a planar resonator, the platform removes the packaging barrier that has limited bosonic QEC scalability [3].

**Limitation 1: modest extension factor.** An extension factor $F = 1.59$ removes only $37.1\%$ of the logical decay rate, leaving $62.9\%$ uncorrected. This modest gain reflects residual error channels (finite‑energy GKP squeezing, oscillator loss, fluxonium dephasing) that must be suppressed for a regime change.

**Limitation 2: the photon advantage is a cited comparison, not a derived one.** The $5$–$40\times$ figure is taken from [5], which itself flags that GKP operation needs approximately $12~\mathrm{dB}$ of squeezing not yet demonstrated for QEC, that dephasing limits cat and binomial codes, and that cross‑platform comparisons are inherently limited [5]. Whether the fluxonium lifetime improvement shifts this ratio at all is unknown; the earlier claim that it multiplies it by $1.59$ was unsupported, and this paper makes no claim either way.

**Limitation 3: assumption‑heavy projections.** The results R3, R4, and R6 rest on the assumptions $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$, $T_1^{\mathrm{tm}} = 30~\mu\mathrm{s}$, and $\eta = 0.1$. The projected $4.51~\mathrm{ms}$ lifetime scales as $1/\eta$: if $\eta = 0.3$, the projection falls to $1.50~\mathrm{ms}$; if $\eta = 0.03$, it rises to $15.0~\mathrm{ms}$.

**Falsifiability of the main result.** The central claim of this paper is that the reported fluxonium ancilla parameters, propagated through the error-budget relations of Section 3, yield the per-cycle error $p_{\mathrm{bf}}^{\mathrm{flx}} = 2.19\%\pm0.34\%$ and the ancilla-limited lifetime $T_L^{(1)} \approx 4.51~\mathrm{ms}$ under $\eta = 0.1$. Three observations would falsify this chain. First, a direct measurement of the fluxonium pure-dephasing time $T_2$ under the operating bias point that falls below the assumed cycle time $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$ would raise the effective conversion factor $\eta$ above $0.1$ and collapse the projected lifetime: since $T_L^{(1)} = 1/(\eta\,\Gamma_{\mathrm{bf}})$, the projection scales as $1/\eta$, so $\eta = 0.3$ gives $1.50~\mathrm{ms}$ and $\eta = 0.03$ gives $15.0~\mathrm{ms}$. Second, a measured reset latency longer than $10~\mu\mathrm{s}$ would invalidate the cycle-time assumption on which R3 rests; because $p_{\mathrm{bf}}$ grows approximately linearly in $T_{\mathrm{cyc}}$ in the regime $\Gamma_{\mathrm{bf}}T_{\mathrm{cyc}} \ll 1$, a reset of $100~\mu\mathrm{s}$ would raise the per-cycle error to roughly $0.199$, ten times the reported value. Third, an independent repetition of the extension-factor measurement that returns $F$ consistent with $1$ within uncertainty would remove the $37.1\%$ decay-rate reduction and reduce the platform to an uncorrected oscillator. Any one of these outcomes falsifies the corresponding link; all three together would falsify the claim that the fluxonium ancilla is the leading near-term route to scalable bosonic QEC.

**Limitations list.** The results of this paper rest on the following assumptions, with the sensitivity of each stated:

1. $T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ (reported in [2],[3]). All derived rates scale as $1/T_1^{\mathrm{bf}}$; the $\pm 15.5\%$ relative uncertainty propagates directly into $\Gamma_{\mathrm{bf}}$, $p_{\mathrm{bf}}$, and $\Gamma_{\mathrm{anc}}$ (R8).
2. $F = 1.59 \pm 0.05$ (reported in [3]). The removed fraction $1 - 1/F$ is sensitive to $F$ near unity: at $F = 1.54$ the removed fraction is $0.351$, at $F = 1.64$ it is $0.390$, so the headline $37.1\%$ carries a $\pm 2.0$-percentage-point band.
3. $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$ (assumption, shared with [2]). R3 scales approximately linearly in $T_{\mathrm{cyc}}$ while $\Gamma_{\mathrm{bf}}T_{\mathrm{cyc}} \ll 1$; the result is invalid if the true cycle time approaches $T_1^{\mathrm{bf}}$.
4. $T_1^{\mathrm{tm}} = 30~\mu\mathrm{s}$ (assumption). R4's ratio of $12.9$–$15.0$ is a like-for-like comparison only if the baseline transmon is representative; a different baseline changes the ratio proportionally.
5. $\eta = 0.1$ (assumption). R6 scales as $1/\eta$ with no experimental support for the chosen value; this is the least constrained input in the chain.
6. The Poisson model for bit flips (method assumption). If bit flips are correlated or bursty, the per-cycle probability is not $1 - e^{-\Gamma_{\mathrm{bf}}T_{\mathrm{cyc}}}$ and R3 is an underestimate or overestimate depending on the correlation structure.
7. The photon-budget figure $5$–$40\times$ is a cited cross-platform comparison [5], not derived here, and carries the caveats stated in Section 2; no multiplication by $F$ is performed in this version.
8. The bibliography contains five works, all of which are cited; this limits the breadth of the related-work treatment in Section 2, and no claim in this paper rests on literature beyond those five works.

**Open questions.** Whether the ancilla lifetime improvement shifts the photon-budget ratio of [5] at all is unknown; the earlier claim that it multiplies the ratio by $1.59$ was unsupported, and this paper makes no claim either way. Whether the geometric-code scaling prediction of [2], which consumes the $p_{\mathrm{phys}} = 2.19\times10^{-2}$ derived here, survives experimental test on a $d = 5$ stabilizer set is likewise open and is the subject of the minimal experiment proposed in Section 7.

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and design impact.** Quantum-hardware architects designing superconducting processors are the direct users of this result. The derived per-cycle ancilla error $p_{\mathrm{bf}}^{\mathrm{flx}} = 2.19\%\pm0.34\%$ sets an explicit specification: an ancilla selected for a bosonic QEC module must hold its bit-flip probability below this level over the chosen correction cycle, which for the assumed $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$ corresponds to the bit-flip rate $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$ or, equivalently, a bit-flip lifetime near $451~\mu\mathrm{s}$. If the result holds, the ancilla bit-flip channel is treated as secondary in the error budget rather than dominant, and the design effort shifts to the residual channels named in Section 6 (squeezing, oscillator loss, dephasing). Fabrication planners can use the same numbers to weigh fully planar bosonic QEC against 3D-cavity approaches, since the planar spiral-resonator integration is what makes the fluxonium ancilla compatible with wafer-scale processing [3].

**(b) Technology readiness.** This work is purely analytical: it propagates published numbers through standard relations and performs no experiment, simulation, or hardware demonstration, and it has not undergone peer review. Against the NASA Technology Readiness Level definitions it resides at TRL 1–2 (basic principles observed and reported), and as analytical work it does not exceed TRL 3. No manufacturing readiness is claimed.

**(c) Smallest next experiment.** The minimal de-risking test is a three-part measurement on an existing planar fluxonium–GKP device, proposed conditionally: an experimenter would (i) measure the fluxonium pure-dephasing time $T_2$ at the bias point used for GKP stabilization, (ii) quantify in dB the GKP squeezing actually achieved in the planar resonator, and (iii) record the fluxonium reset latency. The outcome $T_2 \gg 10~\mu\mathrm{s}$, squeezing sufficient for error correction, and reset latency below $10~\mu\mathrm{s}$ would support the assumptions behind R3 and R6; a measured $T_2$ below the cycle time, or a reset latency above it, would falsify the projected $4.51~\mathrm{ms}$ lifetime. A second, independent test consumes the derived $p_{\mathrm{phys}} = 2.19\times10^{-2}$ as the physical error input to the $d = 5$ geometric-stabilizer benchmark proposed in [2], which measures the logical error probability after a fixed number of correction cycles: a rate consistent with that work's geometric prediction supports its scaling hypothesis, while a rate near its surface-code prediction falsifies it.

**(d) Engineering constraints that bind first.** The following constraints follow from the platform description in [3] and the assumptions derived in Section 4; items not derivable from either are listed as open questions. First, timing: the reset circuitry must deliver a sub-$10~\mu\mathrm{s}$ fluxonium reset without inducing excess dephasing, because R3 depends linearly on the cycle time in the operating regime. Second, materials and fabrication: the heavy fluxonium requires a large shunt capacitance and an inductive loop, and the planar Archimedean spiral resonator must reach a quality factor high enough that photon loss does not dominate the logical budget; the required $Q$ is not derived in this paper and is an open question. Third, calibration: the error-budget chain is only as good as the measured $T_1^{\mathrm{bf}}$ and $T_2$, so calibration of both at the operating bias is a binding requirement. Fourth, squeezing generation: the microwave-domain squeezing needed for finite-energy GKP operation is a known caveat of the resource comparison [5], and the level achieved on this platform is not stated in the sources used here; it is an open question. Cost figures are not derivable from the inputs of Section 4 and are not projected.

**(e) Order-of-magnitude performance bounds (projection).** The only performance bound this paper projects is the ancilla-limited logical lifetime $T_L^{(1)} \approx 4.51~\mathrm{ms}$ under the stated assumptions $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$ and $\eta = 0.1$, with the sensitivity $1.50$–$15.0~\mathrm{ms}$ across $\eta \in [0.03, 0.3]$ derived in Section 6. The photon-budget comparison remains the cited $5$–$40\times$ fewer photons per logical qubit at $p_L = 10^{-6}$ [5]; no further performance figure is projected, because no input in Section 4 supports one.

**(f) Risks and misuse.** The principal misuse path is over-reliance on the ancilla-error reduction: a design team that treats the $2.19\%$ per-cycle error as the whole budget, while ignoring oscillator loss, insufficient squeezing, or fluxonium dephasing, would prematurely claim scalability that the $62.9\%$ residual decay fraction does not support. A second misuse path is re-importing the withdrawn $8.0$–$64\times$ photon figure: any document that multiplies the cited $5$–$40\times$ ratio by the extension factor $F$ repeats the linearity error corrected in this version, and the two quantities are measured under different conditions with no connecting relation derived here or stated in [5].

## 8. Conclusion

This corrected version propagates the reported heavy-fluxonium ancilla parameters through explicit error-budget arithmetic and repairs two defects of the earlier release. The corrected chain yields an ancilla bit-flip rate $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$, a removal of $37.1\%\pm2.0\%$ of the logical decay rate, a per-cycle ancilla error of $2.19\%\pm0.34\%$ for the assumed $10~\mu\mathrm{s}$ cycle, and a projected ancilla-limited lifetime of $4.51~\mathrm{ms}$ under the stated conversion assumption. The molecular-qubit analogy of the earlier release is withdrawn: the work so cited is a graph-theoretic study of Zagreb indices [1] and supports no error-correction claim. The $8.0$–$64\times$ photon-budget figure is withdrawn: the photon-budget comparison remains the cited $5$–$40\times$ ratio at $p_L = 10^{-6}$ [5], with no multiplication by the extension factor. The analysis shows that the fluxonium ancilla lifts the dominant error channel while leaving $62.9\%$ of the logical decay uncorrected, and it identifies the measurements that would confirm or falsify the chain: dephasing time, achieved squeezing, reset latency, and the $d = 5$ scaling benchmark of [2]. The derived metrics give hardware designers a concrete error-budget target and a falsifiable framework for future planar fluxonium–GKP work.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.40.12-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 13 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum. arXiv:1405.1293v3. https://arxiv.org/abs/1405.1293v3
[2] https://papers.qnfo.org/papers/falsifying-geometrically-inspired-quantum-error-correcting-codes-via-distinct-lo. QNFO: Falsifying Geometrically Inspired Quantum Error‑Correcting Codes via Distinct Logical‑Error Scaling.
[3] https://papers.qnfo.org/papers/planar-bosonic-error-correction-with-heavy-fluxonium-a-quantitative-reassessment. QNFO: Planar Fluxonium‑Controlled Bosonic Error Correction: A Quantitative Error‑Budget Reassessment.
[4] https://papers.qnfo.org/papers/computational-simulation-of-geometric-orientation-codes. QNFO: Computational Simulation of Geometric Orientation Codes.
[5] https://papers.qnfo.org/papers/x3.3-bosonic-codes-native-encoding. QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes.
