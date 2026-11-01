# Planar Fluxonium‑Controlled Bosonic Error Correction: A Quantitative Error‑Budget Reassessment (Corrected Version)

## Abstract

Bosonic quantum error correction (QEC) encodes a logical qubit in a single harmonic oscillator, promising fault tolerance with far fewer physical components than qubit‑based surface codes. Recent planar demonstrations using a heavy fluxonium ancilla report a bit‑flip lifetime of $T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ and a logical‑lifetime extension factor of $F = 1.59 \pm 0.05$. The gap addressed here is the absence of a transparent, arithmetic‑level analysis that connects these reported numbers to the underlying error budget and per‑cycle ancilla error probability. This corrected version also repairs two defects of the earlier release: a citation that had been misdescribed as an analysis of two‑level error correction for multi‑spin molecular qubits, and a photon‑budget figure obtained by multiplying a cited resource ratio by the lifetime extension factor under an unjustified linearity assumption. We propagate the reported lifetimes through standard QEC error‑budget relations and derive: (i) an ancilla bit‑flip rate $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$, (ii) a $37.1\%\pm2.0\%$ removal of the logical decay rate, and (iii) a per‑cycle ancilla error of $2.19\%\pm0.34\%$ for an assumed $10~\mu\mathrm{s}$ correction cycle. The photon‑budget advantage remains the cited $5$–$40\times$ fewer photons per logical qubit at $p_L = 10^{-6}$; the previously claimed $8.0$–$64\times$ figure is withdrawn. The corrected chain gives hardware designers a concrete error‑budget target and a falsifiable prediction for future fluxonium‑GKP experiments.

## 1. Introduction

Superconducting quantum processors face a scaling bottleneck: surface‑code error correction requires thousands of physical qubits per logical qubit, inflating hardware cost and delaying near‑term deployment of error‑corrected algorithms [2]. Bosonic QEC offers a hardware‑efficient alternative by encoding a logical qubit in the large Hilbert space of a single oscillator mode, thereby reducing component count. The practical history of bosonic QEC in superconducting circuits has been dominated by an asymmetry: long‑lived oscillators (3D cavities) are paired with weak ancilla qubits (transmons) whose bit‑flip lifetimes of order tens of microseconds cap the logical lifetime regardless of code quality.

A recent planar fluxonium‑GKP analysis attacks this asymmetry. Heavy fluxonium—a superconducting artificial atom with a large shunt capacitance and an inductive loop—has a bit‑flip lifetime taken as $T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ for the purpose of analysis, an order of magnitude above prior transmon ancillas [3]. Integrated on a planar Archimedean spiral resonator, the platform enables finite‑energy GKP state preparation, measurement‑free stabilization, and rapid fluxonium reset, yielding a logical‑lifetime extension factor of $F = 1.59 \pm 0.05$ [3].

If the error‑budget arithmetic behind these numbers holds, the design decision it changes is concrete: QEC architects can treat the ancilla bit‑flip channel as secondary rather than dominant, and fabrication planners can weigh fully planar bosonic QEC against bulky 3D‑cavity approaches. Two errors in the earlier release of this analysis blocked that use. First, a cited work was described as an analysis of two‑level error correction for multi‑spin molecular qubits supporting a cross‑platform error‑hierarchy analogy; the work so cited is in fact a mathematical‑chemistry paper on degree‑based topological indices of trees [1], and the analogy is withdrawn. Second, a photon‑budget advantage of $8.0$–$64\times$ was produced by multiplying a cited $5$–$40\times$ photon ratio by the lifetime extension factor $F = 1.59$ under an explicit assumption that logical lifetime scales linearly with the photon budget; that assumption connects two quantities measured under different conditions (a lifetime ratio within one platform and a resource ratio across platforms at fixed $p_L$), and the multiplication is withdrawn. This version reports the corrected analysis.

**Contributions.**
1. **Error‑budget arithmetic.** From the reported $T_1^{\mathrm{bf}}$ and $F$, we derive the ancilla bit‑flip rate, the corrected and uncorrected logical decay fractions, the per‑cycle error probabilities, and the steady‑state ancilla‑induced error floor, with every arithmetic step shown (Section 4).
2. **Erratum 1: citation correction.** We correct the description of the previously mischaracterized citation: the work is a graph‑theoretic study of Zagreb indices [1], it supports no molecular‑qubit analogy, and the cross‑platform analogy is removed (Section 2).
3. **Erratum 2: photon‑budget correction.** We withdraw the $8.0$–$64\times$ photon‑advantage figure and its linearity assumption, and report the photon‑budget comparison as the cited $5$–$40\times$ ratio at $p_L = 10^{-6}$ [5], without any multiplication by $F$ (Sections 4.5 and 5).
4. **Falsifiability.** We state explicitly which measurements would falsify the claim that planar fluxonium‑GKP is the leading route to scalable bosonic QEC (Section 6).

## 2. Background and Related Work

This corrected version cites the five works of its bibliography, in the bibliography's own numbering; because the list contains fewer than eight works, all of them are cited and the limitation is stated in Section 6.

**The misdescribed citation, corrected.** Reference [1] derives sharp lower bounds for the first and second Zagreb indices $M_1$ and $M_2$ of trees with a given number of pendent vertices: Theorem 1 gives $M_1(T) \geq 9n - 16$ for a tree with an even number $n \geq 2$ of pendent vertices, with equality for a $4$‑tree in which every internal vertex has degree $4$, and Theorem 3 gives $M_2(T) \geq 11n - 27$ for $n \geq 8$, with equality for trees whose stem vertices have degree $4$ or $5$ [1]. This is a result in mathematical chemistry, where topological indices predict properties of chemical compounds. The earlier release described this reference as an analysis of two‑level error correction for multi‑spin molecular qubits and used it to support a cross‑platform error‑hierarchy analogy. That description is incorrect: nothing in [1] concerns qubits, error correction, or spin systems, and the molecular‑qubit analogy is withdrawn from this paper. No claim in Sections 3–5 depends on [1].

**Falsifiability of geometric code proposals.** Reference [2] formulates a falsifiability criterion for geometrically inspired QECCs, deriving the scaling $p_L \propto p_{\mathrm{phys}}^{\,d/2}$ from a stabilizer interaction degree extracted from the code's algebraic description, against the surface‑code law $p_L \approx A\,p_{\mathrm{phys}}^{\,d}$. Using the same fluxonium inputs used here—$T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$ and $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$, giving $p_{\mathrm{phys}} = 2.19\times10^{-2}$—[2] predicts a geometric‑code logical error rate $p_L^{\mathrm{geom}} = 7.1\times10^{-5}$ for $d = 5$ versus a surface‑code rate $p_L^{\mathrm{SC}} = 5.1\times10^{-9}$, a separation of three orders of magnitude [2]. This is directly relevant to the present paper: it shows how the per‑cycle ancilla error derived in Section 4.3 can serve as the physical error input to a decisive scaling experiment, and its proposed benchmark on a $d = 5$ geometric stabilizer set is the same kind of minimal test proposed in Section 7.

**The analysis under correction.** Reference [3] is the earlier release of the present analysis. It reports the inputs used here—$T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ and $F = 1.59 \pm 0.05$—and derives the ancilla bit‑flip rate $(2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$, the removal of $37.1\%$ of the logical decay rate, the per‑cycle ancilla error $2.19\%\pm0.34\%$, and the ancilla‑limited lifetime projection $T_L^{(1)} \approx 4.51~\mathrm{ms}$ [3]. Its §4.5 additionally claimed an $8.0$–$64\times$ photon‑budget advantage obtained by multiplying a $5$–$40\times$ ratio by $F = 1.59$ under an explicit linearity assumption, and its §2 attached a molecular‑qubit analogy to the work now cited as [1]. Both items are corrected in this version; the arithmetic of R1–R6 in [3] is reproduced unchanged in Section 4.

**Anisotropic‑noise code proposals.** Reference [4] proposes geometric orientation codes, which use 3D spatial orientation as the redundancy degree of freedom against directionally biased noise, on the argument that surface codes assume perfectly isotropic noise and degrade under directional bias through correlated string errors that halve their effective distance; it reports a reduction of physical‑to‑logical overhead from greater than $241{:}1$ to $4{:}1$ at a $10^{-4}$ logical error rate in its simulation study [4]. These figures come from that work's own simulation of anisotropic noise channels and are not independently verified here; they are treated in this paper as an unverified external claim, relevant only as context for how strongly code‑architecture conclusions can depend on the assumed noise model—the same sensitivity that motivates the failure‑mode analysis of Section 6.

**Resource‑commensurable comparison.** Reference [5] compares cat, GKP, binomial, and surface codes using a photons‑per‑logical‑qubit metric at a target logical error rate $p_L = 10^{-6}$, finding that bosonic codes require $5$–$40\times$ fewer photons and roughly $100\times$ fewer spatial modes than surface codes, an advantage stated to be robust to factor‑of‑2 uncertainties in individual estimates [5]. The same work records the caveats that GKP operation needs approximately $12~\mathrm{dB}$ of squeezing not yet demonstrated for QEC, that dephasing limits cat and binomial codes, and that the thesis is falsifiable by a head‑to‑head experimental comparison on the same platform by roughly 2028–2030 [5]. This comparison is the sole basis of the photon‑budget statement in Section 4.5 of this paper; unlike the earlier release, no factor derived from $F$ is applied to it.

## 3. Methods

Our method is *derived‑metric analysis*: a small set of reported numbers is propagated through standard QEC error‑budget relations to obtain quantities the experiment implies but does not state directly. No simulation is performed; every result is either exact arithmetic on reported inputs or a labeled projection with stated assumptions.

**Inputs.**
- $I_1$: ancilla bit‑flip lifetime $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$, uncertainty $\pm 70~\mu\mathrm{s}$ (reported in [2],[3]).
- $I_2$: logical‑lifetime extension factor $F = 1.59$, uncertainty $\pm 0.05$ (reported in [3]).
- $I_3$: assumed correction‑cycle duration $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$ (assumption, also used in [2]).
- $I_4$: assumed transmon baseline bit‑flip lifetime $T_1^{\mathrm{tm}} = 30~\mu\mathrm{s}$ (assumption representative of prior 3D‑cavity demonstrations).
- $I_5$: assumed flip‑to‑logical conversion factor $\eta = 0.1$ (assumption about the fraction of ancilla flips that corrupt the logical state).
- $I_6$: photon‑budget ratio of $5$–$40\times$ fewer photons for bosonic codes versus surface codes at $p_L = 10^{-6}$ (reported in [5]).

**Defining relations.**
1. Ancilla bit‑flip rate: $\displaystyle \Gamma_{\mathrm{bf}} = \frac{1}{T_1^{\mathrm{bf}}}$.
2. Corrected logical decay rate: $\displaystyle \Gamma_L^{(1)} = \frac{\Gamma_L^{(0)}}{F}$, with $\Gamma_L^{(i)} = 1/T_L^{(i)}$.
3. Per‑cycle bit‑flip probability (Poisson model): $\displaystyle p_{\mathrm{bf}}(T_{\mathrm{cyc}}) = 1 - e^{-\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}} \approx \Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}$ for $\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}} \ll 1$.
4. Steady‑state ancilla‑induced logical error rate: $\displaystyle \Gamma_{\mathrm{anc}} = \eta\,\Gamma_{\mathrm{bf}}$, independent of $T_{\mathrm{cyc}}$.
5. Uncertainty propagation for a function $q = f(I_1,I_2)$ with independent inputs: $\displaystyle \sigma_q^2 = \left(\frac{\partial f}{\partial I_1}\right)^2 \sigma_{I_1}^2 + \left(\frac{\partial f}{\partial I_2}\right)^2 \sigma_{I_2}^2$.

**Corrections relative to the earlier release.** (a) The photon‑budget step of the earlier §4.5, which multiplied $I_6$ by $F$ under the assumption that logical lifetime scales linearly with the photon budget, is deleted: $I_6$ compares resource counts across platforms at fixed $p_L$, while $F$ compares lifetimes within one platform, and no supplied or derived relation connects them. (b) The molecular‑qubit analogy attached to the work now cited as [1] is deleted, since [1] contains no qubit or error‑correction content. All other relations are unchanged from [3].

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

Input $I_6$ is a resource comparison from [5]: bosonic codes require $5$–$40\times$ fewer photons, and roughly $100\times$ fewer spatial modes, than surface codes to reach $p_L = 10^{-6}$. The corrected statement of the photon‑budget connection is simply this cited ratio:

$$
\text{photon advantage} = 5\text{–}40\times \quad \text{at } p_L = 10^{-6} \; \text{[5]}.
$$

The earlier release multiplied this ratio by the extension factor $F = 1.59$ to obtain $5\times1.59 \approx 8.0$ and $40\times1.59 \approx 63.6 \approx 64$, under an explicit assumption that logical lifetime scales linearly with the photon budget. That step is withdrawn. The two factors are measured under different conditions: $F$ is a within‑platform lifetime ratio at the experiment's operating point, while $I_6$ is a cross‑platform resource count at a fixed target error rate, and no relation supplied by [5] or derived here connects them. The photon‑budget advantage reported in this paper is therefore $5$–$40\times$, unchanged by the fluxonium result, and any dependence of the photon budget on the ancilla lifetime improvement is left as an open question (Section 6).

## 5. Results

All quantities below are derived in Section 4 from the inputs $I_1$–$I_6$ (or are explicitly labeled projections).

- **R1 (computed).** Ancilla bit‑flip rate: $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$.
- **R2 (computed).** Fraction of logical decay removed: $0.371 \pm 0.020$ ($37.1\%$). Residual fraction: $0.629 \pm 0.020$.
- **R3 (computed, assumption $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$).** Per‑cycle ancilla error: $p_{\mathrm{bf}}^{\mathrm{flx}} = 0.0219 \pm 0.0034$ ($2.19\%\pm0.34\%$).
- **R4 (computed, assumption $T_1^{\mathrm{tm}} = 30~\mu\mathrm{s}$).** Transmon baseline per‑cycle error: $p_{\mathrm{bf}}^{\mathrm{tm}} \approx 0.283$ ($28.3\%$). Ratio of per‑cycle errors: $12.9$. Ratio of rates: $15.0$.
- **R5 (structural).** Steady‑state ancilla‑induced logical error rate equals $\eta\,\Gamma_{\mathrm{bf}}$, independent of cycle speed.
- **R6 (projection).** With $\eta = 0.1$, the ancilla‑limited corrected logical lifetime is $T_L^{(1)} \approx 4.51~\mathrm{ms}$.
- **R7 (cited, corrected).** Photon‑budget advantage: $5$–$40\times$ fewer photons per logical qubit versus surface codes at $p_L = 10^{-6}$, as reported in [5]. The previously claimed $8.0$–$64\times$ range is withdrawn; no multiplication by $F$ is performed.
- **R8 (consistency check).** The relative uncertainty of $\Gamma_{\mathrm{bf}}$ is $344/2217 = 15.5\%$, matching the relative uncertainty of $T_1^{\mathrm{bf}}$ ($70/451 = 15.5\%$), confirming correct propagation.

No new measurements or simulations are reported.

## 6. Discussion

**Scope limitation of the source list.** The bibliography of this version contains five works, all of which are cited; the customary breadth of a related‑work section covering at least eight works cannot be met here, and the literature context is correspondingly narrower than in a standard survey. In particular, the withdrawal of the molecular‑qubit analogy removes the only cross‑platform error‑hierarchy comparison the earlier version offered, and no replacement analogy is asserted.

**Strengths.** The heavy fluxonium ancilla lifts the dominant error channel from the ancilla to the oscillator, opening a regime where bosonic codes can exploit their native error‑correction capabilities. Combined with a planar resonator, the platform removes the packaging barrier that has limited bosonic QEC scalability [3].

**Limitation 1: modest extension factor.** An extension factor $F = 1.59$ removes only $37.1\%$ of the logical decay rate, leaving $62.9\%$ uncorrected. This modest gain reflects residual error channels (finite‑energy GKP squeezing, oscillator loss, fluxonium dephasing) that must be suppressed for a regime change.

**Limitation 2: the photon advantage is a cited comparison, not a derived one.** The $5$–$40\times$ figure is taken from [5], which itself flags that GKP operation needs approximately $12~\mathrm{dB}$ of squeezing not yet demonstrated for QEC, that dephasing limits cat and binomial codes, and that cross‑platform comparisons are inherently limited [5]. Whether the fluxonium lifetime improvement shifts this ratio at all is unknown; the earlier claim that it multiplies it by $1.59$ was unsupported, and this paper makes no claim either way.

**Limitation 3: assumption‑heavy projections.** The results R3, R4, and R6 rest on the assumptions $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$, $T_1^{\mathrm{tm}} = 30~\mu\mathrm{s}$, and $\eta = 0.1$. The projected $4.51~\mathrm{ms}$ lifetime scales as $1/\eta$: if $\eta = 0.3$, the projection falls to $1.50~\mathrm{ms}$; if $\eta = 0.03$, it rises to $15.0~\mathrm{ms}$.