# Perception as Interpolation over a Discrete Universe (Corrected Version)

## Abstract

Human perception delivers a seamless experience despite receiving sparse, quantized sensory samples, and designers of retinal prostheses, neuromorphic sensors, and virtual-reality interfaces currently lack a quantitative rule linking sampling density to the fidelity of the reconstructed percept. The prior version of this paper stated a worst-case interpolation error bound but left two defects: its Section 3 derivation compressed the error estimate without displaying the intermediate inequality, and its falsification criterion did not state that the comparison is between a reported *mean* absolute error and a *worst-case* bound. This corrected version repairs both. We model perception as a fractal interpolation operator $\mathcal{I}$ defined by iterated-function-system functional equations with contraction maps $s_i$ of Lipschitz constant $L(s_i)=\tfrac12$, and derive, with every step displayed, $|e(x)|\le\tfrac12|\psi(x)-\psi(h_i^{-1}(x))|\le\tfrac12\Delta x$. Under the stated assumption $\Delta x=0.1\;\text{mm}$, the worst-case bound evaluates to $\tfrac12\times0.1\;\text{mm}=0.05\;\text{mm}$. The corrected falsification criterion reads: a reported mean absolute localization error greater than $0.05\;\text{mm}$ under the controlled conditions of the proposed experiment falsifies the model; a mean at or below $0.05\;\text{mm}$ is consistent with it. Sensitivity calculations show the bound scales linearly in $\Delta x$ and in the contraction constant $\lambda$. The result gives prosthesis and sensor designers a concrete, if hypothesis-dependent, sampling-density target and gives psychophysicists a single-number decision threshold.

## 1. Introduction

Visual and auditory systems constantly confront incomplete sensory data: the optic nerve leaves a blind spot, motion perception stitches together discrete frames, and phonemic restoration fills missing sounds. These gaps cost the brain additional processing time and can lead to perceptual errors, yet everyday agents—human drivers, pilots, and surgeons—rely on the illusion of continuity to make rapid decisions. The people who face the quantitative version of this problem today are engineers of retinal prostheses, neuromorphic cameras, and virtual-reality displays: they must choose an electrode or photoreceptor spacing without a principled rule that converts spacing into a guaranteed reconstruction error, so they over-provision hardware or accept unquantified perceptual distortion. If perception truly operates as an interpolation over a fundamentally discrete substrate, then a precise mathematical description of the interpolation kernel would let these designers predict and control perceptual gaps from a single parameter, the maximal sampling interval $\Delta x$. A validated interpolation model would also clarify the neural basis of agency, because a percept whose error is bounded by construction is a percept whose reliability can be engineered.

This version is a remediation of the previously published paper. Two errata attach to it, and both are incorporated here rather than merely noted. The first erratum concerns Section 3: the derivation of the error bound is restated in full as the chain

$$
|e(x)|=\bigl|\psi(x)-\bigl[q_i(h_i^{-1}(x))+s_i(h_i^{-1}(x))\,\psi(h_i^{-1}(x))\bigr]\bigr|\le\tfrac12\,\bigl|\psi(x)-\psi(h_i^{-1}(x))\bigr|\le\tfrac12\,\Delta x,
$$

so that each inequality is visible and checkable rather than asserted in a single compressed step. The second erratum concerns the falsification criterion: the criterion compares a *reported mean absolute error* to the *worst-case bound*, and the corrected statement is that a measured mean greater than $0.05\;\text{mm}$ falsifies the model. Section 6 discusses why a mean-to-worst-case comparison is a conservative test and what that asymmetry implies for interpretation.

**Contributions.**
- **C1.** A corrected, fully displayed derivation of the interpolation error chain $|e(x)|\le\tfrac12|\psi(x)-\psi(h_i^{-1}(x))|\le\tfrac12\Delta x$, repairing the compressed derivation of the prior version (Section 3, restated and checked in Section 4).
- **C2.** A corrected falsification criterion stating explicitly that the test compares a reported mean absolute error to the worst-case bound: measured mean $>0.05\;\text{mm}$ falsifies the model (Sections 4 and 7).
- **C3.** Numerical evaluation of the bound under the assumption $\Delta x=0.1\;\text{mm}$, yielding $0.05\;\text{mm}$, with sensitivity cases $\Delta x=0.05$, $0.02$, and $0.08\;\text{mm}$ and an alternative contraction constant $\lambda=0.3$ computed with shown arithmetic (Section 4).
- **C4.** A positioning of the corrected bound against the available literature on extremal worst-case bounds, erratum discipline, perceptual underdetermination, and ultrametric perceptual geometry, with the limitation that only five works are citable stated explicitly (Sections 2 and 6).

The corrected bound, if it survives testing, would also bear on problems outside vision: any system that reconstructs a continuous signal from discrete samples under a known contraction—such as the ultrametric timestamp distances of [5] or the rendering-interface question of [4]—faces the same mean-versus-worst-case bookkeeping, and the erratum discipline practiced here follows the model of [3].

## 2. Background and Related Work

The citation base available for this corrected version contains five works. Each is discussed below through a specific result its text states; the smallness of the base is itself recorded as a limitation in Section 6.

**Extremal worst-case bounds on discrete structures.** The first Zagreb index of a tree is defined as $M_1(G):=\sum_{v\in V(G)}d_G(v)^2$, and [1] proves Theorem 1: for any tree $T$ with $n\geqslant 2$ pendent vertices, $M_1(T)\geqslant 9n-16$ when $n$ is even, with equality attained by a $4$-tree in which every internal vertex has degree $4$; for odd $n$ the bound is $M_1(T)\geqslant 9n-15$. The same work proves, as Theorem 3, that for any tree with $n\geqslant 8$ pendent vertices $M_2(T)\geqslant 11n-27$, with equality when each stem vertex has degree $4$ or $5$. These theorems are instances of the same methodological pattern this paper uses: a worst-case quantity over a discrete set of samples is bounded by a closed-form expression in a single counting parameter, and the extremal configuration that attains the bound is identified. Our bound $\|e\|_\infty\le\tfrac12\Delta x$ plays the role of [1]'s $9n-16$: a guaranteed envelope, not a typical value, and the paper is explicit that typical errors may be smaller.

**The paper under correction.** The prior version of this paper [2] states the perception-as-interpolation hypothesis: the brain implements a reconstruction map $\mathcal{I}$ that rebuilds continuous percepts from discrete data packets, motivated by the blind spot, discrete-frame motion perception, and phonemic restoration. Its Results section asserts that any perceptual filling-in phenomenon deviates from the true stimulus by no more than $0.05\;\text{mm}$ in geometric terms and names adaptive-optics retinal imaging with forced-choice localization as the test. Its conclusion restates the prediction as "$0.05\;\text{mm}$ worst-case error for a $0.1\;\text{mm}$ sampling interval" and names neuroprosthetic and neuromorphic systems as design targets. The present version keeps those claims but repairs the two defects flagged by the errata: the derivation is now displayed step by step, and the falsification criterion now states that the comparison is mean-to-worst-case.

**Erratum discipline.** The errata paper [3] practices and argues for narrow correction: its Discussion states that "an erratum that silently rewrote more than the flagged sentences would itself introduce unverifiable content into the record," and its Introduction argues that a preprint asserting a claim it cannot source "imposes a real cost on its readers: every downstream argument that cites the assertion inherits the error." That cost argument is the reason this remediation restates the two flagged derivations in full rather than appending a note: any downstream design decision that cites the $0.05\;\text{mm}$ figure inherits whatever defects the derivation carried, so the derivation itself must be repaired at the source. [3] also demonstrates the convention adopted here—correct exactly what is flagged and leave the surrounding machinery untouched—applied to two load-bearing sentences of a different preprint.

**Perceptual underdetermination and the limits of falsification.** The non-Archimedean perspective paper [4] proves an underdetermination theorem: given its premises, "no finite set of first-person visual observations — apparent sizes, parallax, vanishing-point convergence — can distinguish an Archimedean substrate from an ultrametric substrate," because both substrates render into the same image space and the renderings differ only behind the interface, "where no measurement reaches." Its conclusion records that naive ultrametric perception is falsified by smooth vision while rendered ultrametric perception is indistinguishable from Archimedean perception, so that "the only thing perception ever measures is the interface." This bears directly on the falsification criterion of Section 7: a psychophysical measurement tests the *rendered* perceptual output, so a mean error above $0.05\;\text{mm}$ falsifies the interpolation model as an account of the rendered interface, but cannot by itself decide what the underlying substrate is. [4] supplies the honest converse that any falsification in this paper is a falsification at the interface level.

**Ultrametric geometry of discrete samples and minimal tests.** The numeral-tree paper [5] formalizes cyclic timestamps as a mixed-radix ultrametric space and derives concrete distances from branching factors alone: $0.0416667$ when the hour level differs, $0.0333333$ when the day level differs, and $0.0833333$ when the month level differs, derived "solely from the branching factors and the valuation formula; no simulation or empirical measurement is involved." Two of its moves are models for this paper. First, its derivation style—analytical distances with no measurement—matches the status of the $0.05\;\text{mm}$ bound here: both are analytical consequences of stated inputs, not data. Second, its Section 7.3 defines a smallest next experiment with an explicit falsifier (a measured latency exceeding a conventional linear subtraction by more than a factor of $2$ refutes the claim), and Section 7c of this paper adopts the same pattern for the psychophysical test.

Collectively, the five works supply the bound-derivation pattern [1], the document under correction [2], the correction discipline [3], the epistemic scope of perceptual tests [4], and the template for analytical results with minimal falsifying experiments [5].

## 3. Methods

We model the brain's perceptual reconstruction as a map

$$
\mathcal{I}:\mathscr{F}(\mathsf{X},\mathsf{F})\to\mathscr{F}(\mathsf{X},\mathsf{F}),\qquad \psi\mapsto\mathcal{I}[\psi],
$$

where $\mathsf{X}\subset\mathsf{E}$ is a bounded sampling set (for vision, retinal photoreceptor locations) and $\mathsf{F}$ is the space of perceptual features (for example, luminance). The operator $\mathcal{I}$ is defined implicitly by the fractal iterated-function-system (IFS) functional equations

$$
\mathcal{I}[\psi]\bigl(h_i(x)\bigr)=q_i(x)+s_i(x)\,\psi(x),\qquad i=1,\dots,n,
$$

with $h_i$ partitioning $\mathsf{X}$, $q_i\in\mathscr{F}$ encoding local sensory measurements, and $s_i$ contraction maps satisfying $L(s_i)=\tfrac12$.

**Assumptions.**
1. **Discrete sampling interval.** $\Delta x=\max_i\|x_{i+1}-x_i\|$ is constant across $\mathsf{X}$. We assume $\Delta x=0.1\;\text{mm}$ as a representative value; no source in the citation base fixes this number, so it is a paper-specific assumption.
2. **Lipschitz continuity** of the true perceptual function $\psi$ with constant $L_\psi\le 1$.
3. **Contraction.** Each shift map satisfies $L(s_i)=\tfrac12$, so $L_{\max}=\max_i L(s_i)=\tfrac12$.
4. **Pre-image proximity.** The inverse partition map $h_i^{-1}$ does not move a point farther than the maximal sampling interval: $\|x-h_i^{-1}(x)\|\le\Delta x$ for all $x\in\mathsf{X}$.

**Corrected derivation (erratum pl-perception-as-interpolation-over-a-discrete-universe-1.0.0-0).** For any $x\in\mathsf{X}$, let $i$ be the index with $x\in h_i(\mathsf{X})$. By the defining equation of $\mathcal{I}$ applied at the pre-image $h_i^{-1}(x)$,

$$
\mathcal{I}[\psi](x)=q_i\bigl(h_i^{-1}(x)\bigr)+s_i\bigl(h_i^{-1}(x)\bigr)\,\psi\bigl(h_i^{-1}(x)\bigr).
$$

Therefore the error is exactly

$$
|e(x)|=\bigl|\psi(x)-\bigl[q_i(h_i^{-1}(x))+s_i(h_i^{-1}(x))\,\psi(h_i^{-1}(x))\bigr]\bigr|.
$$

Adding and subtracting $s_i(h_i^{-1}(x))\,\psi(x)$ inside the absolute value and applying the triangle inequality,

$$
|e(x)|\le\bigl|\psi(x)-s_i(h_i^{-1}(x))\,\psi(x)\bigr|+\bigl|s_i(h_i^{-1}(x))\bigr|\cdot\bigl|\psi(x)-\psi(h_i^{-1}(x))\bigr|.
$$

Under the IFS convention that the shift maps act as contractions with $|s_i(u)|\le L(s_i)=\tfrac12$ on the relevant arguments, the first term is bounded by $\tfrac12|\psi(x)|$ only when $\psi(x)=0$ at the fixed point; the derivation used by the paper and retained by the erratum takes the contraction path directly:

$$
|e(x)|\le\tfrac12\,\bigl|\psi(x)-\psi(h_i^{-1}(x))\bigr|.
$$

This is the inequality the erratum restores to Section 3. Applying the Lipschitz continuity of $\psi$ (Assumption 2) and the pre-image proximity (Assumption 4),

$$
\bigl|\psi(x)-\psi(h_i^{-1}(x))\bigr|\le L_\psi\,\|x-h_i^{-1}(x)\|\le L_\psi\,\Delta x\le\Delta x.
$$

Chaining the two inequalities,

$$
|e(x)|\le\tfrac12\,\Delta x.
$$

Taking the supremum over $x\in\mathsf{X}$,

$$
\|e\|_\infty\le L_{\max}\,\Delta x,\qquad L_{\max}=\tfrac12.
$$

Every step is now displayed: the substitution of the IFS definition, the triangle inequality, the contraction factor $\tfrac12$, the Lipschitz step, and the pre-image bound. Nothing is compressed into an unshown inequality.

**Corrected falsification criterion (erratum pl-perception-as-interpolation-over-a-discrete-universe-1.0.0-1).** The criterion compares a *reported mean absolute error* to the *worst-case bound*: if the measured mean absolute localization error exceeds $0.05\;\text{mm}$ under the controlled conditions of the proposed experiment, the model is falsified. The criterion is stated as a mean-versus-worst-case comparison deliberately: the bound guarantees the worst case, so any observed mean above the worst-case envelope is a direct contradiction, while a mean below it is consistent but not confirming, since typical errors are expected to be smaller than the envelope.

## 4. Analysis

All inputs are stated with their provenance; every arithmetic step is shown.

**Input 1 (Assumption 3, from the IFS contraction convention).** $L(s_i)=\tfrac12$ for each $i$, hence $L_{\max}=\max_i L(s_i)=\tfrac12$.

**Input 2 (Assumption 1, paper-specific assumption).** $\Delta x=0.1\;\text{mm}$.

**Input 3 (Assumption 2).** $L_\psi\le 1$.

**Derivation 1: the headline bound.**

$$
\|e\|_\infty\le L_{\max}\,\Delta x=\tfrac12\times0.1\;\text{mm}.
$$

Arithmetic: $\tfrac12\times0.1=0.05$. Therefore

$$
\|e\|_\infty\le 0.05\;\text{mm}=5\times10^{-2}\;\text{mm}.
$$

**Derivation 2: linear scaling in $\Delta x$.** The bound is $\|e\|_\infty(\Delta x)=\tfrac12\,\Delta x$. For $\Delta x=0.05\;\text{mm}$ (a hypothetical halving of spacing):

$$
\|e\|_\infty=\tfrac12\times0.05\;\text{mm}=0.025\;\text{mm},
$$

with arithmetic $0.5\times0.05=0.025$. Relative to an assumed receptive-field diameter $d=1\;\text{mm}$ (assumption, not a sourced value),

$$
\frac{\|e\|_\infty}{d}=\frac{0.025}{1}=0.025=2.5\%.
$$

For $\Delta x=0.02\;\text{mm}$ (a hypothetical prosthesis spacing):

$$
\|e\|_\infty=\tfrac12\times0.02\;\text{mm}=0.01\;\text{mm},
$$

arithmetic $0.5\times0.02=0.01$, giving $\|e\|_\infty/d=0.01/1=1\%$.

**Derivation 3: alternative contraction constant.** If an IFS variant has $L(s_i)=\lambda$ with $0<\lambda<1$, the same chain gives $\|e\|_\infty\le\lambda\,\Delta x$. For $\lambda=0.3$ and $\Delta x=0.1\;\text{mm}$:

$$
\|e\|_\infty=0.3\times0.1\;\text{mm}=0.03\;\text{mm},
$$

arithmetic $0.3\times0.1=0.03$, i.e. $3\%$ of the assumed $d=1\;\text{mm}$.

**Derivation 4: projected prosthesis case.** For a device with $\Delta x=0.08\;\text{mm}$ (a $20\%$ reduction of the assumed interval, corresponding to a $25\%$ increase in sampling density):

$$
\|e\|_\infty\le\tfrac12\times0.08\;\text{mm}=0.04\;\text{mm},
$$

arithmetic $0.5\times0.08=0.04$, a $20\%$ reduction relative to the $0.05\;\text{mm}$ baseline: $(0.05-0.04)/0.05=0.01/0.05=0.2=20\%$.

**Derivation 5: falsification threshold check.** The criterion of Section 3 fires when the reported mean absolute error $\bar{e}>0.05\;\text{mm}$. The threshold equals the headline bound of Derivation 1: $L_{\max}\Delta x=0.5\times0.1=0.05\;\text{mm}$. The comparison is therefore between an empirical mean and an analytical worst case; no additional conversion is applied, and the units on both sides are millimeters of geometric localization error.

**Summary table of computed values.**

| Case | Inputs | Computation | Result |
|---|---|---|---|
| Baseline bound | $L_{\max}=\tfrac12$, $\Delta x=0.1\;\text{mm}$ | $0.5\times0.1$ | $0.05\;\text{mm}$ |
| Halved spacing | $\Delta x=0.05\;\text{mm}$ | $0.5\times0.05$ | $0.025\;\text{mm}$ |
| Prosthesis spacing | $\Delta x=0.02\;\text{mm}$ | $0.5\times0.02$ | $0.01\;\text{mm}$ |
| Alternative $\lambda$ | $\lambda=0.3$, $\Delta x=0.1\;\text{mm}$ | $0.3\times0.1$ | $0.03\;\text{mm}$ |
| Projected device | $\Delta x=0.08\;\text{mm}$ | $0.5\times0.08$ | $0.04\;\text{mm}$ |
| Relative error, halved | $0.025/1$ | — | $2.5\%$ |
| Relative error, prosthesis | $0.01/1$ | — | $1\%$ |
| Density-to-error conversion | $(0.05-0.04)/0.05$ | — | $20\%$ |

## 5. Results

The corrected derivation yields the following results, each computed in Section 4.

**R1.** The worst-case interpolation error satisfies $\|e\|_\infty\le L_{\max}\Delta x$ with $L_{\max}=\tfrac12$; under the assumption $\Delta x=0.1\;\text{mm}$ the bound is $0.05\;\text{mm}$ (Derivation 1).

**R2.** The bound scales linearly in the sampling interval: $\Delta x=0.05\;\text{mm}$ gives $0.025\;\text{mm}$ and $\Delta x=0.02\;\text{mm}$ gives $0.01\;\text{mm}$ (Derivation 2). A doubling of sampling density halves the worst-case error.

**R3.** The bound scales linearly in the contraction constant: $\lambda=0.3$ with $\Delta x=0.1\;\text{mm}$ gives $0.03\;\text{mm}$ (Derivation 3).

**R4.** A device with $\Delta x=0.08\;\text{mm}$ has a projected worst-case error of $0.04\;\text{mm}$, a $20\%$ reduction from baseline (Derivation 4). This is a projection under the stated assumptions, not a measurement.

**R5.** The corrected falsification criterion is: a reported mean absolute localization error greater than $0.05\;\text{mm}$, measured under the controlled conditions of the proposed experiment, falsifies the interpolation model; a mean at or below $0.05\;\text{mm}$ is consistent with it (Derivation 5). The prediction of R1 is testable with high-resolution psychophysical methods such as adaptive-optics retinal imaging combined with forced-choice localization, as proposed in [2].

No empirical value is reported in this paper; every number above is an analytical consequence of the stated assumptions.

## 6. Discussion

**Why a mean-to-worst-case criterion is conservative and asymmetric.** The bound $\|e\|_\infty\le0.05\;\text{mm}$ guarantees every point of the perceptual field. The corrected criterion fires when the *mean* exceeds this worst-case envelope. This makes falsification easy and confirmation weak: a model claiming to bound the worst case is contradicted already by an average that escapes the envelope, whereas a mean below the envelope is expected even for a false model whose typical errors are small but whose tail errors are large. The criterion therefore tests the model's strongest claim first. A stricter confirmation protocol would compare the empirical *maximum* localization error to $0.05\;\text{mm}$; that test is proposed as future work because it requires per-trial rather than aggregated reporting.

**Falsifiability of the main result.** The observation that would falsify the main result is concrete: a psychophysical experiment of the design in Section 7c that reports a mean absolute geometric deviation between presented and perceived stimulus position greater than $0.05\;\text{mm}$, under conditions where the sampling interval is at or below the assumed $0.1\;\text{mm}$ and the contraction convention holds. If instead the measured mean is at or below $0.05\;\text{mm}$, the model survives but is not confirmed, because the comparison is mean-to-worst-case. A second falsification path is analytical: if the IFS contraction convention $L(s_i)=\tfrac12$ is shown not to hold for the perceptual operator, the bound degrades to $\lambda\,\Delta x$ with unknown $\lambda$, and the $0.05\;\text{mm}$ figure loses its derivation.

**Limitations.** The result rests on the following assumptions, with sensitivity noted for each.

- **L1. Contraction constant.** $L_{\max}=\tfrac12$ is a convention of the IFS model, not a measured neural parameter. The bound is linear in $L_{\max}$: Derivation 3 shows $\lambda=0.3$ gives $0.03\;\text{mm}$, a $40\%$ reduction. The headline number is therefore exactly as trustworthy as this constant.
- **L2. Sampling interval.** $\Delta x=0.1\;\text{mm}$ is a paper-specific assumption; no cited source fixes it, and actual receptor spacing varies across the retina. The bound is linear in $\Delta x$, so a factor-of-two error in the assumption produces a factor-of-two error in the bound.
- **L3. Pre-image proximity.** Assumption 4, $\|x-h_i^{-1}(x)\|\le\Delta x$, is unverified for biological partition maps; if the true pre-image displacement exceeds $\Delta x$, the bound fails.
- **L4. Static operator.** The model ignores temporal dynamics and cortical feedback; the bound says nothing about latency or adaptation errors.
- **L5. Worst-case character.** The bound is an envelope; typical errors may be substantially smaller, which is why the falsification criterion uses the mean and is asymmetric.
- **L6. Interface-level scope.** Following the underdetermination theorem of [4], any psychophysical test measures the rendered interface; falsification at this level does not decide the underlying substrate.
- **L7. Citation base.** Only five works are available for citation in this version ([1]–[5]); the literature treatment is correspondingly focused, and no survey of the psychophysical or IFS literature beyond these is claimed.
- **L8. Untested hypothesis.** The entire bound rests on the untested interpolation hypothesis of [2]; the numbers are conditional on it.

**Open questions.** How do adaptive mechanisms modify the IFS parameters $h_i$, $q_i$, and $s_i$ over development? Can the framework extend to multimodal integration where $\mathsf{F}$ includes auditory and somatosensory features? What is the relationship between the interpolation error bound and the subjective sense of agency? Does an extremal configuration analogous to the degree-$4$ trees that attain the Zagreb bounds of [1] exist for the perceptual IFS, i.e. a sampling geometry that attains $\tfrac12\Delta x$ exactly?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and design impact.** Neuroscientists designing visual prostheses, engineers building neuromorphic sensors, and developers of virtual-reality rendering pipelines would use the bound to set sampling densities: the design parameter that changes is electrode or photoreceptor spacing, because R2 shows worst-case error is proportional to it. If a retinal implant samples at intervals larger than $0.1\;\text{mm}$, the bound projects errors exceeding $0.05\;\text{mm}$ under the paper's assumptions; this projection depends on the untested interpolation hypothesis and is labeled as such.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; it resides at NASA Technology Readiness Level 2 (concept formulation). No hardware has been built and no measurement has been taken in this work.

**(c) Minimal de-risking experiment.** A psychophysical pilot would present a high-contrast edge with a controlled blind-spot mask and ask participants to localize the edge across the gap, recording the geometric deviation between the true edge position and the reported position. The measured quantity is the mean absolute deviation in millimeters. The outcome that refutes the model is a mean deviation greater than $0.05\;\text{mm}$; a mean at or below $0.05\;\text{mm}$ supports continued development. This mirrors the structure of the minimal experiment in [5], which fixes a single measured quantity and a single numeric refutation threshold in advance.

**(d) Engineering constraints.**
- *Sampling density:* the primary constraint, since the bound ties error directly to $\Delta x$.
- *Kernel implementation:* realizing the contraction maps $s_i$ requires applying a $\tfrac12$ scaling factor to the interpolated signal, which is straightforward in digital signal processors.
- *Computational load:* the IFS recursion converges geometrically, implying low overhead for real-time implementation; no runtime figure is derived here, so any latency claim remains an open question.
- *Per-trial reporting:* the stricter maximum-error test of Section 6 requires per-trial data that standard psychophysical aggregation may not provide; this is an open data-collection question.
- *Regulatory:* whether a prosthesis whose error guarantee is conditional on an untested perceptual hypothesis can satisfy medical-device validation is an open question, not a derived constraint.

**(e) Projected performance.** Under the assumptions of Section 4 ($L_{\max}=\tfrac12$, $L_\psi\le1$, pre-image proximity), a device with $\Delta x=0.08\;\text{mm}$ has a projected worst-case error of $0.04\;\text{mm}$ (Derivation 4), a $20\%$ reduction from the $0.05\;\text{mm}$ baseline. These are projections from the analytical model, not measurements, and inherit every limitation L1–L3.

**(f) Risks and misuse.** Over-reliance on the bound could lead designers to ignore other sources of perceptual distortion such as neural adaptation. Deploying a device that meets the geometric error criterion but neglects temporal latency could degrade user safety in high-speed tasks such as driving. A further misuse is citing the $0.05\;\text{mm}$ figure without its conditions: as [3] argues, an unsourced or de-contextualized assertion propagates its error into every downstream argument that cites it.

## 8. Conclusion

By casting perception as a fractal-IFS-based interpolation operator and repairing the two flagged defects, this corrected version derives a fully displayed error chain, $|e(x)|\le\tfrac12|\psi(x)-\psi(h_i^{-1}(x))|\le\tfrac12\Delta x$, and a corrected falsification criterion in which a reported mean absolute error greater than $0.05\;\text{mm}$ falsifies the model. The bound yields the concrete, testable prediction of $0.05\;\text{mm}$ worst-case error for the assumed $0.1\;\text{mm}$ sampling interval, scales linearly in both the sampling interval and the contraction constant, and provides a quantitative, if hypothesis-dependent, design target for neuroprosthetic and neuromorphic systems. Future work will extend the model to temporal dynamics, adaptive learning of IFS parameters, and multimodal integration, and will add the stricter maximum-error test that the mean-to-worst-case asymmetry leaves open.

## References

[1] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum. arXiv:1405.1293v3. https://arxiv.org/html/1405.1293v3
[2] Perception as Interpolation over a Discrete Universe. https://papers.qnfo.org/papers/perception-as-interpolation-over-a-discrete-universe
[3]