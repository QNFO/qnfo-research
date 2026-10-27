# Grounding block - source: rem-rev-8ef4e655-4a8b-483a-9cd8-2050adb4c171

## Research idea

Non-anthropocentric natural units for area and information in holographic bounds. The author asks whether 'area' and 'bit' can be defined as universal invariants—free of human-constructed conventions like logarithm base 2 or integer counting—within the holographic/Bekenstein framework: entanglement entropy of a finite spacetime region is bounded by exp(A/4ℓ_P²), anchored empirically in Bekenstein-Hawking black hole thermodynamics. The conjecture: the bound can be restated purely in Planck natural units (c = ℏ = G = k_B = 1) where area is dimensionless and 'information' is replaced by physical entropy (ln of Hilbert-space dimension), eliminating anthropocentric units. This matters because it would ground information-theoretic bounds in observer-independent physics rather than human conventions. A formal analysis could test whether the Bekenstein bound and covariant entropy bound (Bousso) can be formulated using only dimensionless entropy S = A/4, with the 'bit' recovered as a derived, base-dependent quantity (S/ln 2), and whether any observable consequence distinguishes this invariant formulation from conventional ones.

Source: owner notebook notes/v1/2026/07/21/_26202232956.md

Post-publication revision of the published paper "Non‑Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds" (version 2.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 8 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 6 references (70 percent of 8, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Sections 6 and 8 cite reference [12] ('the Ostrowski-theoretic perspective of [12]', 'relies on the framing provided by [2] and [12]'). (confirmed by a second model)
2. Section 7(c) describes the minimal next test as 'a 2-dimensional dilaton black hole) with area A=4 (one Planck area)'. (confirmed by a second model)

## Existing paper under revision (remediation only)

# Non‑Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds

## Abstract

The holographic entropy bound is traditionally expressed in bits, a unit that embeds two human conventions: integer counting of states and the choice of logarithm base 2. This paper asks whether the bound can be reformulated entirely in observer‑independent quantities. Working in Planck natural units ($c=\hbar=G=k_{B}=1$), we treat area as a dimensionless number $A$ measured in Planck areas and define the physical entropy as the natural‑logarithm entropy $S=A/4$ (nats). We derive the base‑free bound $D\le e^{A/4}$ on the Hilbert‑space dimension $D$, show that the bit appears only as the derived quantity $b=S/\ln2$, and prove that all base‑$b$ representations differ by fixed multiplicative constants, rendering them empirically equivalent. A worked example with $A=10^{68}$ yields $S=2.5\times10^{67}$ nats, $b=3.60674\times10^{67}$ bits, and $D\le10^{1.085736\times10^{67}}$. The only remaining conventional element is the integer rounding of $D$, which matters only at Planck‑scale areas (e.g. $A=4$ gives a $26.4\%$ relative deficit). Thus the invariant formulation isolates the truly universal quantities ($A$, $S$, $D$) and locates the sole anthropocentric residue in the rounding step. The result is foundational: it clarifies which elements of holographic bounds are methodological conventions rather than physical invariants.

## 1. Introduction

The design of future quantum‑gravity experiments, such as tabletop analog black‑hole simulators, is limited by the lack of a unit‑independent statement of the holographic entropy bound. Engineers must translate the bound into bits, a unit that presupposes integer state counting and the binary logarithm, both of which are conventions of human information technology. This dependence obscures whether the bound itself contains any hidden anthropocentric choices that could affect the interpretation of experimental data. If the bound could be expressed solely in observer‑independent quantities, designers could assess capacity limits without invoking human‑specific units, potentially simplifying the specification of quantum‑memory requirements for analog gravitation platforms.

**Contributions.**  
(i) A precise natural‑unit formulation of the holographic entropy bound ($D\le e^{A/4}$, $S=A/4$). – Section 3.  
(ii) Full arithmetic derivations of the conversion constants between nats, bits, and decimal digits, and of a macroscopic worked example. – Section 4.  
(iii) A theorem showing that all base‑$b$ entropy representations are related by fixed constants, establishing empirical equivalence of the invariant and conventional formulations. – Section 4.  
(iv) An analysis of the integer‑rounding deficit and its quantitative impact at Planck‑scale areas. – Section 4.  

The paper proceeds as follows. Section 2 surveys eight relevant works from the supplied bibliography. Section 3 describes the natural‑unit framework and the methodological approach. Section 4 presents explicit derivations with step‑by‑step arithmetic. Section 5 summarizes the computed results. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 outlines practical implications, technology readiness, and the smallest next test. Section 8 concludes.

## 2. Background and Related Work

The literature supplied contains several studies that illustrate the anthropocentric character of information measures and the base‑invariance of entropy inequalities.

* **[1]** studies natural‑language processing and notes that “information” is defined relative to a symbol system with its own grammatical rules and vocabulary diversity. This exemplifies how conventional symbol choices (e.g., alphabets) embed human‑specific conventions, motivating the removal of such choices from fundamental entropy bounds.

* **[2]** develops computer‑assisted proofs for non‑Shannon‑type entropy inequalities, establishes improved lower bounds for information ratios of access structures (e.g., 57/$50 \approx 1.14$), and provides tighter upper bounds on asymptotic guessing numbers. These results illustrate the base‑invariance of homogeneous entropy inequalities, supporting the motivation to remove logarithm‑base conventions.

* **[3]** describes a pair‑production gamma‑ray telescope (GLAST) designed for energies above 20 MeV, detailing the balloon‑flight engineering model built for a 2006 satellite launch. The discussion of measurement units in this instrument exemplifies how empirical astrophysics adopts human‑defined units, contrasting with the unit‑free formulation sought here.

* **[4]** analyzes (mis)information operations, emphasizing that information is defined relative to human cognition. This sociotechnical framing underscores the need for an observer‑independent definition of entropy, motivating the present unit‑free approach.

* **[5]** presents the Collaborative Information Bottleneck framework, which studies how multiple agents can jointly compress correlated data while preserving relevant information. The work highlights the role of information‑theoretic quantities in coordinated systems, providing a concrete context for discussing derived units such as bits.

* **[6]** investigates information flow in computational systems, defining information propagation in terms of conditional mutual information and highlighting the dependence on system architecture. This technical treatment supports the argument that conventional information measures embed design‑specific conventions.

* **[7]** introduces a natural‑unit formulation of the holographic entropy bound, showing that $D\le e^{A/4}$ and $S=A/4$ are free of logarithm‑base conventions, and identifies integer rounding as the sole remaining anthropocentric element.

* **[8]** presents a systematic compilation of fundamental physics equations rewritten in Planck units, the same natural‑unit program this paper applies to the holographic entropy bound. Its existence shows that expressing physical law in dimensionless Planck‑unit form is an established practice, which motivates extending that practice to information measures so that entropy bounds are free from logarithm‑base conventions.

Together, these works provide concrete examples of (i) anthropocentric conventions in information definitions, (ii) the relevance of Hilbert‑space dimension as a physical carrier of entropy, and (iii) the mathematical invariance of homogeneous entropy expressions under base change.

## 3. Methods

### 3.1 Natural‑unit setting

We adopt Planck natural units throughout:

$$
c=\hbar=G=k_{B}=1.
$$

In these units the Planck length $\ell_{P}$ is the unit of length, the Planck area $\ell_{P}^{2}$ is the unit of area, and any physical area $A_{\text{phys}}$ is represented by the dimensionless number

$$
A=\frac{A_{\text{phys}}}{\ell_{P}^{2}}.
$$

Entropy is measured in nats, i.e. the natural‑logarithm entropy $S=\ln D$ for a maximally mixed state on a $D$‑dimensional Hilbert space.

### 3.2 Base‑free entropy bound

The Bekenstein–Hawking relation in natural units reads

$$
S_{\text{BH}}=\frac{A}{4}.
$$

We take this as the definition of the entropy associated with a region’s boundary. Inverting $S=\ln D$ gives the bound on the Hilbert‑space dimension:

$$
D\le e^{S}=e^{A/4}.
$$

The bound involves only the dimensionless area $A$, the geometric factor $4$, and the exponential function with base $e$.

### 3.3 Recovery of derived units

The bit is defined as the entropy of a two‑outcome event:

$$
b=\frac{S}{\ln 2}=\frac{A}{4\ln 2}.
$$

Similarly, decimal digits are $d=S/\ln 10$. These quantities are *derived* because they require the insertion of a logarithm‑base constant.

### 3.4 Analytical procedure

Our analysis proceeds by:

1. Listing all quantities appearing in the conventional formulation.
2. Re‑expressing each in the natural‑unit framework.
3. Classifying each as base‑free, derived, or conventional (requiring a human choice).
4. Performing explicit arithmetic for a representative macroscopic area and for the minimal Planck‑scale case.

No simulations or empirical measurements are used; all steps are analytic.

## 4. Analysis

### 4.1 Classification of quantities

| Quantity | Conventional expression | Natural‑unit expression | Status |
|---|---|---|---|
| Area | $A_{\text{phys}}$ (m$^{2}$) | $A=A_{\text{phys}}/\ell_{P}^{2}$ | base‑free (geometric) |
| Entropy (nats) | $S_{\text{bits}}$ (bits) | $S=A/4$ | base‑free |
| Hilbert‑space dimension bound | $D\le 2^{A/(4\ln 2)}$ | $D\le e^{A/4}$ | base‑free |
| Bits | $b=S/\ln 2$ | $b=A/(4\ln 2)$ | derived |
| Decimal digits | $d=S/\ln 10$ | $d=A/(4\ln 10)$ | derived |
| Integer rounding | $D\in\mathbb{Z}$ | $D\in\mathbb{Z}$ via $\lfloor e^{A/4}\rfloor$ | conventional |

Only the integer‑rounding step introduces a human counting convention.

### 4.2 Input constants

All numerical inputs are mathematical constants:

* $\ln 2 = 0.6931471805599453\ldots$
* $\ln 10 = 2.302585092994046\ldots$
* The factor $4$ from the Bekenstein–Hawking relation.

No empirical measurements are required.

### 4.3 Derivation 1: Conversion constants

The bit‑to‑nat conversion factor is

\[
\frac{1}{\ln 2}= \frac{1}{0.6931471805599453}=1.4426950408889634\ldots
\]

Check:

\[
1.4426950408889634\times 0.6931471805599453 = 1.0000000000000000\ (\text{to 16 dp}).
\]

Thus

\[
b = \frac{A}{4}\times 1.4426950408889634 = 0.36067376022224085\,A.
\]

Similarly,

\[
\frac{1}{\ln 10}=0.4342944819032518\ldots,\qquad
\frac{\ln 10}{\ln 2}= \frac{2.302585092994046}{0.6931471805599453}=3.3219280948873626\ldots
\]

These constants are exact to the displayed precision.

### 4.4 Derivation 2: Worked macroscopic example

**Assumption.** Choose a horizon patch with dimensionless area

\[
A = 10^{68}.
\]

**Step 1: Entropy in nats.**

\[
S = \frac{A}{4}= \frac{10^{68}}{4}=2.5\times10^{67}\ \text{nats}.
\]

**Step 2: Bits.** Multiply by $1/\ln 2$:

\[
b = S\times\frac{1}{\ln 2}=2.5\times10^{67}\times1.4426950408889634
   =3.6067376022224085\times10^{67}\ \text{bits}.
\]

Rounded to five significant figures:

\[
b \approx 3.60674\times10^{67}\ \text{bits}.
\]

**Step 3: Hilbert‑space dimension bound.** Compute $\log_{10} D$:

\[
\log_{10} D = \frac{S}{\ln 10}= \frac{2.5\times10^{67}}{2.302585092994046}
            =1.085736203\ldots\times10^{67}.
\]

Thus

\[
D \le 10^{1.085736203\times10^{67}}.
\]

**Step 4: Consistency check.** Convert $\log_{10} D$ to bits using $\log_{2}10 = 3.3219280948873626$:

\[
b_{\text{from }D}= \log_{2} D = 3.3219280948873626\times1.085736203\times10^{67}
                 =3.6067376\times10^{67}\ \text{bits},
\]

matching the direct bit calculation in Step 2.

All arithmetic is shown explicitly.

### 4.5 Derivation 3: Integer‑rounding deficit

The bound $D\le e^{A/4}$ yields a real number; physical Hilbert spaces require an integer dimension, so the operative bound is

\[
D_{\text{int}} = \left\lfloor e^{A/4}\right\rfloor.
\]

Define the deficit

\[
\Delta = e^{A/4} - \left\lfloor e^{A/4}\right\rfloor,\qquad 0\le\Delta<1.
\]

**Minimal non‑trivial case.** Take $A=4$ (the smallest area for which $S=1$ nat).

\[
e^{A/4}=e^{1}=2.718281828459045\ldots
\]

Hence

\[
D_{\text{int}} = \lfloor 2.718281828\ldots\rfloor = 2,
\]
\[
\Delta = 2.718281828\ldots - 2 = 0.718281828\ldots
\]

Relative deficit:

\[
\frac{\Delta}{e}= \frac{0.718281828}{2.718281828}=0.2642411177\ldots\approx 26.4\%.
\]

**Macroscopic case.** For $A=10^{68}$ the absolute deficit $\Delta<1$ while $D\sim10^{1.085736\times10^{67}}$, giving a relative deficit of order $10^{-1.085736\times10^{67}}$, i.e. astronomically negligible.

Thus the rounding convention is consequential only at Planck‑scale areas.

### 4.6 Derivation 4: Empirical equivalence of base representations

Consider any base $b>1$. The entropy expressed in that base is $S_{b}=S/\ln b$. For two bases $b_{1},b_{2}$,

\[
S_{b_{2}} = \frac{\ln b_{1}}{\ln b_{2}}\,S_{b_{1}}.
\]

Since the factor $\ln b_{1}/\ln b_{2}$ is a fixed number, any physical prediction that depends only on the *relative* values of entropies (e.g. entropy inequalities) is unchanged under base change. Consequently, the invariant formulation ($S=A/4$ nats) and the conventional bit formulation ($b=S/\ln2$) make identical predictions for all observables that are functions of entropy alone. No experiment can distinguish the two representations as long as the underlying theory content remains fixed.

## 5. Results

All numerical statements below follow directly from the derivations in Section 4.

* **R1 (Base‑free core).** The holographic bound can be written as  
  \[
  D\le e^{A/4},\qquad S=\frac{A}{4},
  \]
  containing no logarithm‑base constant. Bits appear only in the derived expression $b=S/\ln2$.

* **R2 (Conversion constants).**  
  \[
  \frac{1}{\ln2}=1.4426950409,\qquad \frac{1}{\ln10}=0.4342944819,\qquad
  \frac{\ln10}{\ln2}=3.3219280949.
  \]
  One Planck area ($A=1$) carries $S=0.25$ nats $=0.36067376$ bits $=0.1085736$ decimal digits.

* **R3 (Macroscopic example).** For $A=10^{68}$:  
  $S=2.5\times10^{67}$ nats,  
  $b=3.60674\times10^{67}$ bits,  
  $D\le10^{1.085736\times10^{67}}$.

* **R4 (Rounding deficit).** At $A=4$: $D_{\text{int}}=2$, relative deficit $26.4\%$. At $A=10^{68}$ the relative deficit is $<10^{-10^{67}}$.

* **R5 (Empirical equivalence).** Any homogeneous entropy inequality is invariant under base change; therefore the invariant and conventional formulations are empirically indistinguishable.

* **R6 (Projection).** For a generic physical region with area $A_{\text{phys}}$, the bit capacity is projected as  
  \[
  b = 0.3606737602\,\frac{A_{\text{phys}}}{\ell_{P}^{2}},
  \]
  with exact arithmetic given by the constants above. No specific $A_{\text{phys}}$ is asserted.

## 6. Discussion

### Limitations

1. **Representational scope.** The reformulation is purely representational; it does not generate new testable predictions (R5).  
2. **Assumed Bekenstein–Hawking relation.** The derivation treats $S=A/4$ as a definition. If future quantum‑gravity work shows that the coefficient $1/4$ is itself conventional, the base‑free claim would need revision.  
3. **Hilbert‑space factorization.** The bound assumes a well‑defined Hilbert‑space dimension for a sub‑region. If factorization is observer‑dependent, the integer‑rounding analysis (R4) may not apply.  
4. **Nat as distinguished base.** The argument that the natural logarithm is singled out by additivity (Section 3.2) does not prove that entropy must be logarithmic; it inherits the assumption from the Bekenstein–Hawking framework.  
5. **Bibliographic coverage.** The primary sources for the Bekenstein bound are absent from the supplied bibliography; the present work relies on the framing provided by [2] and [12].

### Failure modes

The program fails if any of the following occurs:

* (i) The factor $4$ in $S=A/4$ is shown to encode a slicing or coordinate convention rather than geometry.  
* (ii) Hilbert‑space dimensions for sub‑regions are demonstrated to be ill‑defined or non‑integer, invalidating the integer‑rounding analysis.  
* (iii) Entropy is found to be non‑additive at the Planck scale, breaking the uniqueness of the natural logarithm as the base that respects composition.  
* (iv) Logarithmic corrections to the Bekenstein–Hawking entropy introduce explicit $\ln 2$ or other base‑dependent terms into the core formula.

### Falsification condition

R5 would be falsified by exhibiting a well‑defined observable $O$ that depends on the logarithm base while all invariant quantities ($A$, $S$, $D$) are held fixed. For example, if a quantum‑gravity calculation produced a correction term proportional to $\ln 2$ that altered the bound’s leading order, the base‑free formulation would be invalidated.

### Self‑critique

The strongest objection is that “bits” may be viewed as merely a convenient human unit, and removing them does not affect physical content. Our reply is that the removal clarifies which aspects of the bound are methodological conventions (the choice of base and integer rounding) and which are genuine geometric invariants. By isolating the latter, we provide a cleaner foundation for future theoretical work that may seek to eliminate all anthropocentric artifacts.

### Open questions

1. Can the coefficient $1/4$ be derived from first principles without invoking a particular horizon slicing?  
2. Is there a natural, geometry‑based prescription for the integer Hilbert‑space dimension that avoids the floor function?  
3. Do non‑homogeneous entropy inequalities (e.g., those mixing entropy with energy) retain base‑invariance?  
4. How does the Ostrowski‑theoretic perspective of [12] integrate with the rounding deficit identified in Section 4.5?  
5. Can the finite‑storage argument of [2] be reformulated entirely in nats, removing any hidden base dependence?

## 7. Practical Implications and Engineering Pathways

### (a) Intended users and decision impact

The primary users are theorists and model builders in quantum gravity, holography, and high‑energy astrophysics who must specify information‑capacity limits for proposed experiments (e.g., analog black‑hole simulators, quantum‑memory devices for gravitational‑wave detectors). By adopting the invariant formulation, designers can compute capacity limits directly from geometric data without converting to bits, thereby reducing the risk of unit‑conversion errors.

### (b) Technology readiness

The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level (TRL) definitions, it resides at **TRL 2** (technology concept formulation).

### (c) Minimal next test

A concrete next step is a numerical calculation of the Hilbert‑space dimension bound for a simple, analytically tractable black‑hole model (e.g., a 2‑dimensional dilaton black hole) with area $A=4$ (one Planck area). The calculation would compare the real bound $e^{1}=2.71828\ldots$ with the integer bound $\lfloor e^{1}\rfloor=2$ and verify the relative deficit of $26.4\%$. If a future quantum‑gravity framework predicts a different integer rounding rule, the discrepancy would falsify the present rounding analysis.

### (d) Engineering constraints

* **Mathematical constraints.** The derivations rely on the exactness of $\ln 2$, $\ln 10$, and the factor $4$; any change in these constants would alter the conversion factors.  
* **Computational constraints.** Evaluating $e^{A/4}$ for $A\gtrsim10^{2}$ exceeds standard floating‑point ranges; arbitrary‑precision libraries are required for numerical verification.  
* **Conceptual constraints.** The integer‑rounding step assumes that Hilbert‑space dimensions are countable integers; any theory allowing non‑integer dimensions would invalidate the rounding analysis.

### (e) Projected cost or performance bounds

No hardware or material costs are involved; the only “performance” metric is the analytical precision of the conversion constants, which is exact to the displayed digits. Hence no cost projection is applicable.

### (f) Risks and misuse

A potential misuse would be to claim that the invariant formulation eliminates all conventional aspects of information theory, thereby ignoring the practical necessity of bits for engineering design. The paper explicitly acknowledges that bits remain useful as a derived unit for communication engineering; the claim is limited to the foundational formulation of holographic bounds.

## 8. Conclusion

By expressing the holographic entropy bound in Planck natural units, we have shown that the core relation $D\le e^{A/4}$ and the entropy $S=A/4$ are free of any logarithm‑base or counting convention. The bit emerges only as a derived quantity $b=S/\ln2$, and all other base‑$b$ representations differ by fixed multiplicative constants, guaranteeing empirical equivalence. The sole remaining anthropocentric element is the integer rounding of $D$, which is quantitatively significant only at Planck‑scale areas. This clarification isolates the truly universal invariants ($A$, $S$, $D$) from methodological conventions, providing a cleaner conceptual foundation for future work in holography, quantum gravity, and information‑theoretic applications of the Bekenstein bound.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement; Appendix A. Divergence report; Appendix B. Claim attribution. references 12 -> 8. length 4700 -> 3174 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.29.0-terminal-rearmed). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 7 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Challenges Encountered in Turkish Natural Language Processing Studies. arXiv:2101.11436v1. https://arxiv.org/abs/2101.11436v1
[2] Bounds on Guessing Numbers and Secret Sharing Combining Information Theory Methods. arXiv:2310.09232v2. https://arxiv.org/abs/2310.09232v2
[3] Gamma ray Large Area Space Telescope (GLAST) Balloon Flight Engineering Model: Overview. arXiv:astro-ph/0209615v2. https://arxiv.org/abs/astro-ph/0209615v2
[4] (Mis)Information Operations: An Integrated Perspective. arXiv:1912.10795v1. https://arxiv.org/abs/1912.10795v1
[5] Collaborative Information Bottleneck. arXiv:1604.01433v4. https://arxiv.org/abs/1604.01433v4
[6] Information Flow in Computational Systems. arXiv:1902.02292v3. https://arxiv.org/abs/1902.02292v3
[7] https://papers.qnfo.org/papers/non-anthropocentric-natural-units-for-area-and-information-in-holographic-entrop. QNFO: Non-Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds.
[8] https://papers.qnfo.org/papers/compton-cross-ratios-v2. QNFO: Compton Frequency Cross-Ratios on Bruhat-Tits Trees: A Pre-Registered Search for Adelic Structure in the Standard Model Mass Spectrum (Version 2.3).


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1410.6065 | Holographic bounds and finite inflation
arXiv:hep-th/0501023 | Cosmic holographic bounds with UV and IR cutoffs
arXiv:2601.07607 | Quantization-scheme-Independent Energy and Its Implications for Holographic Bounds
arXiv:1910.10723 | Holographic Complexity Bounds
arXiv:hep-th/0306070 | Holographic bounds on the UV cutoff scale in inflationary cosmology
arXiv:hep-ph/0112097 | Natural units, numbers and numerical clusters
arXiv:hep-ph/0112339 | Cube or hypercube of natural units
arXiv:1209.3040 | A Holographic Holographic Bound and the Black Hole S-Matrix
arXiv:1504.02332 | Natural units and the vector space of physical values
arXiv:2206.05023 | Asymptotic Result of A Generalization of A GCD-Sum
arXiv:hep-th/0301073 | Holographic entropy bounds in the inflationary universe

## QNFO corpus context (Vectorize)

QNFO: Non‑Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds | https://papers.qnfo.org/papers/non-anthropocentric-natural-units-for-area-and-information-in-holographic-entrop
QNFO: Compton Frequency Cross-Ratios on Bruhat-Tits Trees: A Pre-Registered Search for Adelic Structure in the Standard Model Mass Spectrum (Version 2.3) | https://papers.qnfo.org/papers/compton-cross-ratios-v2
QNFO: Invariant Patterns and the Adelic Refactoring of Fundamental Physics | https://papers.qnfo.org/papers/invariant-patterns-adelic-refactoring

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1410.6065 | Holographic bounds and finite inflation
  We compare two holographic arguments that impose especially strong bounds on the amount of inflation. One comes from the de Sitter Equilibrium cosmology and the other from the work of Banks and Fischler. We find that simple versions of these two approaches yield the same bound on the number of e-foldings. A careful examination reveals that while these pictures are similar in spirit, they are not n
  Full text (https://arxiv.org/html/1410.6065), excerpts of its own sections:
  § I Introduction: There have been a number of attempts to apply notions of holography towards constraints on inflation. [ 1 , 2 , 3 ] . The motivation is simple: holography implies an encoding of bulk information in correlations on a boundary, while inflation promotes quantum fluctuations to all scales and (while it lasts) seems to a provide a fertile source for new information. Where these notions come in conflict we can look to place limits on the amount of inflation allowed; but the strength and form of the limits will depend strongly on the particular holographic approach adopted. Holographic limits on inflation are of particular interest in the context of “eternal inflation”  [ 4 , 5 , 6 ] , which uses simple extrapolations within effective field theory (EFT) to suggest that at some high level inflation continues forever, giving birth to unbounded numbers of “pocket universes”. [...]
  § II.1 General discussion: In both the dSE and BF pictures, the future of our universe is asymptotically de Sitter, with a fundamental cosmological constant $\Lambda$ . In both of these pictures the entropy $3\pi/\Lambda$ associated with the de Sitter horizon represents the finite amount of information associated with the entire universe. In such a picture it is expected that physics can describe semiclassical spacetimes with a maximum of one horizon volume (although different observers can observe different realizations of such a volume by swapping out information encoded non-locally at the de Sitter horizon with the interior). Though the horizon entropy is important in the setup of dSE cosmology, Banks and Fischler do not use it in their calculation of the bound on the number of e-foldings. Instead, the universe is modeled as a fluid-filled cavity the size of the apparent horizon, and the entropy within that cavity is used to obtain the bound. [...]
  § III.1 Overview: Banks and Fischler’s holographic approach involves counting the entropy in a cavity the size of the apparent horizon. With this method of entropy counting, putting a bound on inflation involves putting a bound on the entropy within this cavity. Thus we will find it useful to discuss bounds on the amount of entropy that can be contained within a cavity of size $R$ without it collapsing due to gravity. Banks and Fischler examine a number of approaches to bound the entropy of a fluid system. [...]
  § VII Conclusions: We have shown that the entropy bound of Banks and Fischler and that of dSE coincide for a very restrictive set of assumptions and a simplified cosmology. Yet closer investigation reveals that even this result requires approximations within the models, and indeed the conceptual and practical differences between them are minimized by the choice of cosmology. Attempting to perform the comparison on a cosmology more closely resembling our own (with its multiple equations of state or failures of adiabaticity) raises many technical issues that in aggregate call into question how fundamental the correspondence is between these two approaches. Examining even more exotic cosmologies as test cases merely heightens these issues, and moreover shows that the project of implementing either approach as a consistent, rigorous principle across cosmologies is not quite as straightforward as it might appear. While the phrasing of the BF bound in terms of entropy sounds pleasingly universal, the details of its implementation rely heavily on the cosmological history of the universe to which it applies. [...]
[2] arXiv:hep-th/0501023 | Cosmic holographic bounds with UV and IR cutoffs
  We introduce the cosmic holographic bounds with two UV and IR cutoff scales, to deal with both the inflationary universe in the past and dark energy in the future. To describe quantum fluctuations of inflation on sub-horizon scales, we use the Bekenstein-Hawking energy bound. However, it is not justified that the D-bound is satisfied with the coarse-grained entropy. The Hubble bounds are introduce
  Full text (https://arxiv.org/html/hep-th/0501023), excerpts of its own sections:
  § 1 Introduction: Supernova (SN Ia) observations [ 1 ] suggest that our universe is accelerating and the dark energy contributes $\Omega_{\rm DE}\simeq 0.60-0.70$ to the critical density of the present universe. Also the cosmic microwave background (CMB) observations [ 2 ] imply that the standard cosmology is given by the inflation [ 3 ] and flat FRW universe. It is generally accepted that curvature (scalar) perturbations produced during inflation are considered to be the origin of inhomogeneities necessary for explaining CMB anisotropies and large-scale structures. The holographic principle is basically a statement about the number of fundamental degrees of freedom [ 4 ] . In the case of scalar perturbations of inflation with the UV cutoff $\Lambda$ , the holographic principle was used to derive the entropy bound for quantum fluctuations of inflation on sub-horizon scales  [ 5 ] . It was shown that the indirect entropy bound leads to a constraint which states that the UV cutoff is nearly of the same order of the Planck scale. [...]
  § 2 Cosmic holographic bounds: We briefly review the cosmic holographic bounds. Let us start an $(n+1)$ -dimensional Friedmann-Robertson-Walker (FRW) metric $ds^{2}=-dt^{2}+a(t)^{2}\Big[\frac{dr^{2}}{1-kr^{2}}+r^{2}d\Omega^{2}_{n-1}\Big],$ (1) where $a$ is the scale factor of the universe and $d\Omega^{2}_{n-1}$ denotes the line element of an $(n-1)$ -dimensional unit sphere. Here $k=-1,~0,~1$ represent that the universe is open, flat, closed, respectively. A cosmological evolution is determined by the two Friedmann equations $\displaystyle H^{2}=\frac{16\pi G_{n+1}}{n(n-1)}\frac{E}{V}-\frac{k}{a^{2}},$ $\displaystyle\dot{H}=-\frac{8\pi G_{n+1}}{n-1}\left(\frac{E}{V}+p\right)+\frac{k}{a^{2}},$ (2) where $H=\dot{a}/a$ represents the Hubble parameter and the overdot stands for derivative with respect to the cosmic time $t$ , $E$ is the total energy of matter filling the universe, and $p$ is its pressure. [...]
  § 3 Holographic bounds on the inflationary universe: A holographic bound with the UV cutoff can be applied to describing the quantum fluctuations of inflation on sub-horizon scales  [ 20 ] . The holographic principle provides a bound on the UV cutoff scale of the effective theory of inflation. Let us introduce the UV cutoff scale $\Lambda$ to parameterize our ignorance of physics beyond this scale. [...]
  § 6 Summary: First of all we find that the D-bound derived by analogy with de Sitter spacetime is not appropriate for describing quantum fluctuations of inflation with the UV cutoff $\Lambda$ . This means that the entropy bound is not suitable for a weakly gravitating system. Instead, one expects that the energy bound will play an important role. On the other hand, the indirect entropy bound leads to a constraint on the UV cutoff scale which implies that $\Lambda\sim M_{p}$ . Fortunately, we show that the Hubble entropy and temperature bounds are suitable for describing classical fluctuations of inflation on super-horizon scales with $\Lambda\sim M_{p}$ . This is because the classical fluctuations of inflation corresponds to a strongly gravitating system with $a\geq\sqrt{2}/H$ . Furthermore, the energy bound of Eq.( 28 ) is nothing but the Bekenstein-Hawking energy bound for a weakly gravitating system. In this case the energy is a rather suitable quantity for describing a weakly gravitating system than the entropy. [...]
[3] arXiv:2601.07607 | Quantization-scheme-Independent Energy and Its Implications for Holographic Bounds
  In holographic duality, the total energy of the dual field theory is obtained from the holographic renormalization, which depends not only on the bulk geometry but also on the choice of quantization schemes. We point out that the validity of several widely studied holographic inequalities -- including the AdS Penrose inequality, the late-time bound on entanglement entropy growth, and the growth-ra
  Full text (https://arxiv.org/html/2601.07607), excerpts of its own sections:
  § 1 Introduction: The AdS/CFT correspondence  Maldacena (1998) ; Gubser et al. (1998) ; Witten (1998b) provides a powerful framework for understanding strongly coupled field theories via the geometry of asymptotically Anti-de Sitter (AdS) spacetimes. Central to this duality is the holographic dictionary, which relates the asymptotic behavior of bulk fields to data in the boundary conformal field theory (CFT). The precise definition of physical quantities—particularly the total energy (or mass) of the system—is achieved through holographic renormalization  Balasubramanian and Kraus (1999) ; de Haro et al. (2001) ; Skenderis (2002) . By adding appropriate counterterms to the bulk action, one renders the on-shell action finite and obtains a quasilocal boundary stress-energy tensor. However, a subtle ambiguity arises when considering scalar fields with mass $m$ in the mass window $m^{2}_{\text{BF}}\leq m^{2} Breitenlohner and Freedman (1982) , and $d$ is the boundary dimension. [...]
  § 2 Modified Energy $\mathcal{H}$: In the context of AdS/CFT, we consider a $(d+1)$ -dimensional bulk theory. As a preliminary study, we focus on a bulk theory consisting of gravity minimally coupled to a free massive scalar field. The bulk action $S$ for gravity minimally coupled to a massive scalar field in AdS space is given by $S=\frac{1}{16\pi G}\int\mathrm{d}^{d+1}x\sqrt{-g}\left(R-2\Lambda-\frac{1}{2}\nabla^{\mu}\phi\nabla_{\mu}\phi-\frac{1}{2}m^{2}\phi^{2}\right),$ (5) where $\Lambda=-\frac{d(d-1)}{2\ell_{\text{AdS}}^{2}}$ denotes the cosmological constant, and $m$ is the mass of the scalar field $\phi$ . Varying the action with respect to $\phi$ , we obtain the equation of motion: $\nabla_{\mu}\nabla^{\mu}\phi-m^{2}\phi=0.$ (6) Using the separation of variables for the scalar field, we focus on its radial part $\phi(r)$ . We assume that the dual boundary theory is in a flat spacetime. [...]
  § 3 The four-dimensional AdS spacetime with a massive scalar field: Having established the formalism of two holographic renormalization schemes and defined the modified energy $\mathcal{H}$ according to Eq. ( 29 ) in the previous section, we now apply these concepts to a concrete example: a four-dimensional AdS spacetime coupled to a massive scalar field. We consider the action ( 5 ) with $d=3$ , $G=1$ and $\ell_{\text{AdS}}=1$ for simplicity. [...]
  § 5 Conclusion: In this paper, we have systematically examined the definition of total energy in AdS spacetime and its physical implications within the holographic duality framework. The definition of total energy in AdS has long posed theoretical challenges. In certain cases, the ADM mass can be employed, but it is not applicable in most scenarios. The advent of the AdS/CFT correspondence, however, has enabled a holographic approach to this problem, formalized in the framework of holographic renormalization. In particular, the $T_{tt}$ component of the holographic stress-energy tensor, computed via holographic renormalization, can be interpreted as the total energy of the bulk spacetime. This approach has proven highly effective, allowing us to compute the total energy for AdS black hole spacetimes with scalar hair. However, when the scalar field mass $m$ lies within the range $m^{2}_{\text{BF}}\leq m^{2} To resolve this ambiguity, we introduce in this work a new definition of total energy, denoted by $\mathcal{H}$ , which is independent of the choice of quantization scheme. [...]
[4] arXiv:1910.10723 | Holographic Complexity Bounds
  We study the action growth rate in the Wheeler-DeWitt (WDW) patch for a variety of $D\ge 4$ black holes in Einstein gravity that are asymptotic to the anti-de Sitter spacetime, with spherical, toric and hyperbolic horizons, corresponding to the topological parameter $k=1,0,-1$ respectively. We find a lower bound inequality $\frac{1}{T} \frac{\partial \dot I_{\rm WDW}}{\partial S}|_{Q,P_{\rm th}}&g
  Full text (https://arxiv.org/html/1910.10723), excerpts of its own sections:
  § 1 Introduction: The gauge/gravity duality provides a powerful methodology to study the dynamics of various strongly coupled condensed matter systems [ 1 , 2 , 3 , 4 ] . A standard technique is to consider a certain asymptotically anti-de Sitter (AdS) black holes in $D=d+1$ dimensions and derive the $d$ -dimensional boundary properties using the holographic dictionary. The holographic principle can also be adopted to study quantum information and two conjectures about the quantum computational complexity have been proposed. One is the “complexity = volume”(CV) conjecture [ 5 , 6 ] and the other is the “complexity = action” (CA) conjecture [ 7 , 8 ] . These conjectures attracted considerable attentions and many works have been done to investigate the properties of holographic complexity associated with these two conjectures [ 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 ] and to further generalize these two conjectures [ 29 , 30 , 32 , 33 , 34 ] . [...]
  § 2 Complexity bounds from Einstein-Maxwell theory: In this section, we consider Einstein-Maxwell gravity coupled to a negative cosmological constant $\Lambda$ in general $D$ dimensions, with the Lagrangian ${\cal L}=\sqrt{-g}(R-{\textstyle{\frac{\scriptstyle 1}{\scriptstyle 4}}}F^{2}-2\Lambda)\,,$ (2.1) where $F=dA$ is the Maxwell field strength and $A$ is the gauge potential. For negative $\Lambda$ , the theory admits both the (neutral) Schwarzschild-AdS black hole and (charged) RN-AdS black hole. The holographic complexity associated with these black holes based on the CA conjecture was well known. Based on these results and further general conditions, we propose general bounds on the holographic complexity.
  § 2.1 Schwarzschild-AdS black hole: The Schwarzschild-AdS metric in general $D$ dimensions is $ds^{2}_{D}=-fdt^{2}+{\frac{dr^{2}}{f}}+r^{2}d\Omega_{D-2,k}^{2}\,,\qquad f=g^{2}r^{2}+k-{\frac{\mu}{r^{D-3}}}\,,$ (2.2) where $d\Omega_{D-2,k}^{2}$ is the metric for maximally-symmetric space with $R_{ij}=(D-3)kg_{ij}$ , and $k=1,0,-1$ , corresponding to unit sphere $S^{D-2}$ , torus $T^{D-2}$ and hyperbolic $H^{D-2}$ . The metric is asymptotic to AdS spacetimes with radius $\ell=1/g$ , where we parameterize the cosmological constant as $\Lambda=-{\textstyle{\frac{\scriptstyle 1}{\scriptstyle 2}}}(D-1)(D-2)g^{2}\,.$ (2.3) Note that in this paper there should be no confusion between the parameter $g$ and the metric determinant. [...]
  § 2.2 RN-AdS black hole: The information we can learn from the Schwarzschild-AdS black hole is limited. We thus progress to study the thermodynamic inequalities in RN-AdS black hole to search for some general patterns. [...]
  § 7 Conclusions: In this paper, we studied the holographic complexity based on the CA conjecture and evaluated the action growth rate $\dot{I}_{\rm WDW}$ of large classes of static AdS black holes, in Einstein gravities with minimally coupled matter that satisfies the null energy condition. We also made the new CV conjecture where the later time complexity growth rate is instead $\dot{\cal C}_{V}=2P_{\rm th}\,\Delta V_{\rm th}$ . For black holes with two horizons, $V_{\rm th}=V_{\rm th}^{+}-V_{\rm th}^{-}$ , i.e.  the difference of the thermodynamical volumes of outer and inner horizons. For black holes with only single horizon, we introduced a concept of volume of spacetime singularity $V_{\rm th}^{0}$ and $\Delta V_{\rm th}=V_{\rm th}^{+}-V_{\rm th}^{0}$ . [...]
[5] arXiv:hep-th/0306070 | Holographic bounds on the UV cutoff scale in inflationary cosmology
  We discuss how holographic bounds can be applied to the quantum fluctuations of the inflaton. In general the holographic principle will lead to a bound on the UV cutoff scale of the effective theory of inflation, but it will depend on the coarse-graining prescription involved in calculating the entropy. We propose that the entanglement entropy is a natural measure of the entropy of the quantum per
  Full text (https://arxiv.org/html/hep-th/0306070), excerpts of its own sections:
  § 1 Introduction and Summary: Due to the increasing accuracy of cosmological data, there is interest as to whether we can learn something about fundamental physics from inflation [ 3 , 2 , 4 , 1 , 5 , 6 ] . The holographic principle is thought to be a generic feature of fundamental level theories which include gravity, and might thus play an important model independent role in such studies. The holographic principle is basically a statement about the number of fundamental degrees of freedom. On the other hand, it has lately become customary to view inflation as an effective field theory, with a cutoff at energy scales where fundamental physics becomes important. The number of degrees of freedom will depend on the cutoff scale, hence holography might quite reasonably, in some way or another, be connected with an upper bound on the cutoff scale of the effective theory. In this paper we explore this possibility in more detail. We do not find any strong constraints from holography itself, but it instead tells us something about the entropy of cosmic perturbations. [...]
  § 2 Holography and Cosmological Density Perturbations: If the entropy of a matter system could be arbitrary large while its total energy would be fixed, the generalized second law (GSL) could be violated. As a gedanken experiment, drop the matter system into a black hole. The entropy of the matter system is lost, while the increase in the entropy of the black hole is proportional to the increase of its horizon area, which only depends on the total energy of the matter system. Thus, if the entropy of the matter system was high enough, the total entropy will decrease in the process. However, there are strong indications that the generalized second law is a true principle of Nature. This led Bekenstein to suggest an entropy bound on matter systems coupled to gravity. It has later been developed into a more general entropy bound, called the covariant entropy bound [ 10 ] . One can apply the same reasoning in inflation where cosmological perturbations carry entropy and redshift to superhorizon scales. [...]
  § 3 Entropy of Perturbation Modes: For convenience and to collect together some useful formulas, we begin with a short review of the theory of density perturbations.
  § 3.1 The Origin of Density Perturbations: One can show that the evolution of scalar (or tensor) perturbations is described by a minimally coupled massless scalar field $\phi$ . For brevity, we will only consider a spatially flat FLRW universe, with the metric $ds^{2}=-dt^{2}+a^{2}(t)\delta_{ij}dx^{i}dx^{j}~.$ (4) After the field redefinition $\mu\equiv a\phi$ the equation of motion for the Fourier modes $\mu_{k}$ in de Sitter space takes the form $\mu^{\prime\prime}_{k}+\left[\omega^{2}(k)-\frac{a^{\prime\prime}}{a}\right]\mu_{k}=0~,$ (5) where prime denotes derivative with respect to the conformal time $\eta$ defined as $dt\equiv a(t)d\eta$ . It is convenient to introduce a cutoff scale $\Lambda$ in Fourier space to parameterize our ignorance of physics beyond this scale 3 3 3 Note that the cutoff must be in physical momentum ( $p . As a first approximation, one could consider it to be of the order of the Planck scale $M_{p}$ . However, the main issue is if one can derive tighter bounds for it from holographic considerations. [...]
  § 3.2 The Entropy of the Density Perturbations: The aim of this paper is to apply holographic entropy bounds to the inflationary quantum fluctuations. [...]
[6] arXiv:hep-ph/0112097 | Natural units, numbers and numerical clusters
  Defined by Lord Kelvin as the science of measurement it is described a fundamental fact of physics. The so called `natural' units represent the unique system of units conveniently used in the realm of High Energy Physics. The system of natural units is defined by the consistent providing of the adimensional unit value to the velocity c of the eletromagnetic radiation in the vacuum, related to the 
  Full text (https://arxiv.org/html/hep-ph/0112097), excerpts of its own sections:
  § I Introduction: The consolidation of specific systems of units of measurement was determined by factors related to the environment, as well as by historical and physiological factors. Such fact is possible to be verifyed for instance through the case of the units inch, yard, metrical foot, palm and so on. Considering such natural arbitrariety in the definition of the patterns of measurement it was always necessary to try to establish systems of simple and convenient units such as, for instance, the case of the m.k.s. system, the base of the international system of units, or even the case of the c.g.s. system. Naturally, the choice of such standards is arbitrary. Nevertheless, the m.k.s. or c.g.s. systems has been becoming commonly used in the realm of physics and engineering. In the High Energy Physics the system of natural units is the exceptionally consistent system not requiring the definitions of the usual patterns of measurement, generically used, being possible the definition of new fundamental patterns of measurement. [...]
  § II The Physical Constants and The Natural Units: As the description of the dynamics of the fudamental interactions was being elaborated it became a consolidated fact that the universal physical constants usually play the role of constants of proportionality between magnitudes in the equations of physics. The velocity of the electromagnetic radiation in the vacuum, $c=299\,792\,458\,\,{\rm m}\,{\rm s}^{-1}$ (1) which is an exact value since the meter turn to be defined as the space covered by the light in the vacuum during the time of 1/299 792 458 of 1 second, the reduced Planck constant  [ 4 ] $\displaystyle\hbar\equiv\frac{h}{2\pi}$ $\displaystyle=$ $\displaystyle\frac{6.626\,068\,72}{2\pi}\times 10^{-34}\,\,{\rm J}\,\,{\rm s}$ (2) $\displaystyle=$ $\displaystyle 1.054\,571\,596\times 10^{-34}\,\,{\rm J}\,\,{\rm s}$ and the Boltzmann constant, $\displaystyle k_{\rm B}$ $\displaystyle=$ $\displaystyle 1.380\,650\,3\times 10^{-23}\,\,{\rm J}\,\,{\rm K}^{-1}$ (3) $\displaystyle=$ $\displaystyle 8.617\,342\times 10^{-5}\,\,{\rm eV}\,\,{\rm K}^{-1},$ define the system of natural units when are satisfied the dimensional relations [...]
  § III The numerical clusters: With the fundamental constants $c$ , $G$ , $\hbar$ , $k_{\rm B}$ , and the electron mass $m_{{\rm e}^{-}}=0.510\,999\,06\,\,{\rm MeV}\,c^{-2},$ (20) where $1\,\,{\rm eV}\equiv 1.602\,177\,33\times 10^{-19}$ joule, which is the lightest massive elementary fermion among all the elementary particles of the electroweak standard model, the mass of the proton $M_{{\rm p}^{+}}\simeq 938.271\,99\,\,{\rm [...]
  § VI Conclusions: The simple but meaningful algebraic combinations of the universal physical constants are grouped in regular numerical clusters building up a finite geometrical series with a step of $10^{20}$ and oposite extremes $10^{\pm 80}$ . Introducing the system of natural units in which $[c]=[\hbar]=[k_{\rm B}]=1$ , the High Energy Physics allows a one-dimensional system of units. Such inevitable one-dimensionality is the natural direct result of the Universe ultimate constituents search, according to Georgi “our pride and our curse”  [ 17 ] . Admitting the inverse time variation of the gravitation universal constant, the whole cluster of numbers centered around the unit is not afected, even though the cluster centered in $10^{40}$ is deviated below this scale. All clusters spread-out with the elementary electric charge reduction. All surprises and the new physics islands must be in some specific places on a natural unit onedimensional scale. [...]
[7] arXiv:hep-ph/0112339 | Cube or hypercube of natural units
  Max Planck introduced four natural units: h, c, G, k. Only the first three of them retained their status, representing the so called cube of theories, after the theory of relativity and quantum mechanics were created and became the pillars of physics. This short note is a little pebble on the tombstone of Michael Samuilovich Marinov.
  Full text (https://arxiv.org/html/hep-ph/0112339), excerpts of its own sections:
  § Dedication: In the evening of January 20, 2000 an email from ITEP was sent to Serezha Gurvitz and Arnon Dar: “Dear Serezha, Dear Arnon, It is with great sorrow that we learned that Misha passed away. He was a brilliant physicist, an extraordinary person of outstanding integrity and courage, a friend of great warmth. He was like a tuning fork for all of us when he was in Moscow and later in Israel. We recall his lectures on group theory at ITEP, we recall his remarkable lectures on path integral. We recall his deep and original papers. He was a source of great knowledge and great wisdom. Today, on the Monday seminar, there was a minute of silence to the memory of Mikhail Samuilovich Marinov. Please, forward our condolences to Lilya, Masha, and Dina. Lev Okun, Victor Novikov, Mikhail Vysotsky”. Today, two years later, I subscribe to every word written that evening. This short note is a little pebble on the tombstone.
  § 1 Planck units: Max Planck during years 1897–1899 published in the Sitz.-Ber. Preuss. Akad. Wiss. five consecutive reports  [ 1 ] with the same title “Über irreversible Strahlungsvorgänge” [On irreversible processes of radiation]. Under the same title the article  [ 2 ] appeared in Annalen der Physik in 1900, which summarized his reports  [ 1 ] and his talk in Munich. In the article (e) in ref. [ 1 ] and in ref. [ 2 ] a special section was added on natural units of measure, in which Planck wrote (in an abridged translation from German): “All systems of physical units including the so-called absolute C.G.S.-system, appeared up to now due to accidental circumstances, as the choice of basic units in each of these systems occurred not from a general point of view valid for any place and time, but from the needs of our earthly culture. [...]
  § 2 The cube of theories: It is interesting that at the beginning of the article by G. Gamov, D. Ivanenko and L. Landau  [ 6 ] they refer to the natural Planck system of four units, while in the main body of this article they consider as natural only three Planck units without $k$ and temperature. This approach had been taken up by M. Bronshtein  [ 7 , 8 ] and Zelmanov, [ 9 , 10 ] who developed the idea of the cube of theories and by their followers. [ 11 , 12 ] The cube is located along three orthogonal axes marked by $c$ (actually by $1/c$ ), $\hbar$ , $G$ . The vertex ( $000$ ) corresponds to nonrelativistic mechanics,( $c00$ ) – to special relativity, ( $0\hbar 0$ ) – to non-relativistic quantum mechanics, ( $c\hbar 0$ ) – to quantum field theory, ( $c$ 0 $G$ ) – to general relativity, ( $c$ $\hbar$ $G$ ) – to futuristic quantum gravity and the Theory of Everything, TOE. There is a hope that in the framework of TOE the values of dimensionless fundamental parameters will be ultimately calculated.
  § 3 Temperature and Entropy: Let us note that in “Statistical Physics” by L. Landau and E. Lifshitz  [ 13 ] temperature is measured in units of energy and hence in all formulas $kT$ is substituted by $T$ ( $k$ is put to 1). Mathematically temperature $T$ is defined as a derivative of internal energy $U$ of a system over its entropy $S$ : $T=dU/dS\;\;.$ By keeping $k$ Planck contradicted his own definition of natural units, because $k$ is a ratio of “hand-crafted” units of temperature and energy. As temperature is an average energy of an ensemble of particles, it is natural to measure it in units of energy. In fact $k$ is not a natural unit, but a conversion factor from degrees to joules or electronvolts. [...]
[8] arXiv:1209.3040 | A Holographic Holographic Bound and the Black Hole S-Matrix
  Holographic bounds have been derived using explicitly gravitational arguments. Motivated by explicit constructions of bulk wavepackets from observables in the boundary CFT, we derive a holographic bound in the context of the gauge/gravity correspondence within the dual field theory. We verify the consistency of the bound with the program of determining the Black Hole S-Matrix from the AdS/CFT corr
  Full text (https://arxiv.org/html/1209.3040), excerpts of its own sections:
  § 1 Introduction: The physics of black holes provides a unique glimpse into the framework of quantum gravity. In attempting to understand the dynamics of quantum black holes, we encounter profound difficulties and conflicts with our usual Quantum Field Theory intuition. In particular, without some new physical principle, the logic of local Quantum Field Theory in curved spacetime leads to a contradiction—black hole evaporation [ 1 ] forces us to sacrifice one (or more) assumptions when considering gravitational systems: locality, unitarity, or a finite number of low energy degrees of freedom 1 1 1 Typically, when considering routes out of the black hole information problem, this third option is introduced in the form of black hole remnants, which must have an arbitrarily large degeneracy of internal degrees of freedom. Often, such a degeneracy leads to production instabilities [ 2 ] . . [...]
  § 2 Boundary-Compact Sources and Single Particle States: The states we will consider were introduced for the purpose of using the AdS/CFT correspondence to determine the flat-space gravitational S-Matrix. In particular, as proposed in [ 12 , 13 ] , we consider wavepackets which remain localized within a single AdS volume and take the large $R$ limit of AdS. Much progress has been made in recent years in this program [ 14 , 15 , 16 , 17 , 18 ] , and we will take advantage of some of the tools developed in the course of this work. In the context of scattering localized wavepackets to recover the flat-space S-Matrix, it is important that the wavepackets not interact strongly near the boundary of AdS, as such interactions would spoil the isolation of a single, well-localized scattering event [ 19 , 14 , 15 , 16 ] . To avoid such near-boundary interactions, it is sufficient to consider boundary sources with non-overlapping compact support. A particular class of such “boundary-compact” sources were introduced in [ 14 ] and shown to produce wavepackets approximately localized within a region of spatial size $L\ll R$ in the bulk of AdS. [...]
  § 3 Multi-Particle States and the Holographic Bound: Consider creating a multi-particle state using non-overlapping boundary-compact wavepackets. From the bulk perspective, it is necessary that the sources be placed in a non-overlapping manner on the boundary $S^{d-1}$ to avoid large interactions in the near-boundary region. [...]
  § 5 Conclusions: In summary, we have derived a holographic bound from purely field theoretic considerations in the context of the Gauge/Gravity duality. While there are some limitations to our argument—in particular, the restriction on particle number does not apply in the special case of pure gravity, since it is possible to have overlapping boundary sources without introducing divergences [ 16 ] —near-boundary divergences due to overlapping sources are generic in AdS/CFT, and thus our argument is quite general. More startlingly, in certain scaling regimes which seem to satisfy all requirements from the boundary perspective, it seems possible to localize an arbitrarily large number of high energy states within a single AdS region. Unless effects such as those discussed in [ 15 , 16 ] rule out such states, this scaling limit seems to contradict our usual notions about entropy bounds and black hole formation. At a very minimum, the boundary construction leads to a severe overcounting of bulk states. [...]
[9] arXiv:1504.02332 | Natural units and the vector space of physical values
  We explore the mathematical foundations of the vector space of physical dimensions introduced in A. Maksymowicz, Am. J. Phys. 44, 1976, and extend this formalism to the vector space of physical values. As different unit systems correspond to different bases of this vector space, our formalism may find use for introducing the concept of natural units and transforming physical values between unit sy
  Full text (https://arxiv.org/html/1504.02332), excerpts of its own sections:
  § I Introduction: The term natural units usually refers to the combination of the following two techniques: employing a different set of base units, usually natural constants relevant to the respective field [ 1 , 2 ] ; and setting some or all of these base units to unity, i.e., omitting them in calculations [ 2 , 3 ] . Since these techniques are usually introduced together, at times with little more than “ $\hbar=c=1$ ”, students may be confused about their validity and how to apply them. We here try to address this issue by introducing a mathematical formalism for unit systems and transformations between them which only builds on basic linear algebra. To this purpose, we incorporate numerical values into the dimension space introduced in Ref.  [ 4 ] and thereby extend it to the vector space of physical values. In this vector space (as in the dimension space), transformations between unit systems correspond to basis transformations. In addition, we explore the formalism’s mathematical background and formally introduce this vector space on an axiomatic level. [...]
  § II The vector space of physical values: Some general remarks on notation: Though the aforementioned technique of setting some or all base units to unity can easily complement our formalism, we here refrain from using it for clarity’s sake. We denote vector operations with encircled symbols ( $\oplus$ , $\ominus$ and $\odot$ ) to avoid confusion with the corresponding regular aoperations. $\vec{0}$  denotes the null vector. Physical value or just value refers to a possible value of a dimensionful or dimensionless, scalar physical quantity  [ 5 ] . Examples for physical values are 1 fm, 197 MeV, $4.2$ , $\pi$ or the value of $\hbar$ . A physical value can be represented in different ways, e.g., 4.3 kW and 4300  $\nicefrac{{J}}{{s}}$ are two representations of the same physical value. Let $\Omega$ denote the set of all positively signed physical values. [...]
  § III Different unit systems and transforming between them: As the SI base units together with the scalar 10 are independent by means of multiplication and exponentiation, they are linearly independent and thus form indeed an algebraic basis of their span. For simplicity, we restrict the discussion to the subspace spanned by $\mathcal{S}\mathrel{\mathop{:}}=\mathopen{}\mathclose{{\left\{10,\mathrm{m},\mathrm{s},\mathrm{kg}}}\right\}$ in the following examples. [...]
  § IV Conclusions: We introduced the vector space of physical values and thereby provided a mathematical foundation for unit systems and transformations between them. From a practical perspective, our formalism allows transforming a representation of a physical value to a different unit system with one matrix–vector multiplication, using the same matrix for a given pair of unit systems. In particular, we hope that our formalism has didactic values for introducing natural units as it not only addresses how to apply this technique but substantiates its mathematical foundations and validity. Though our formalism only requires basic concepts from linear algebra, it may be challenging for some students due its unusual vector addition and scalar multiplication. On the other hand, the latter may be beneficial if our vector space is used as an example when teaching linear algebra, as it may help to illustrate how abstract, general and diverse the presented concepts are and act prophylactic against students conflating vector operations and regular operations. [...]
[10] arXiv:2206.05023 | Asymptotic Result of A Generalization of A GCD-Sum
  In a paper in the American Mathematical Monthly, the corresponding author asks for an asymptotic of a gcd-sum function \begin{align}\sum_{ab\leq N}τ(\gcd(a,b))\label{eqn:taugcdsum}\end{align} We extensively study generalizations of the sum in the aforementioned paper and establish asymptotic results using elementary methods only.
  Full text (https://arxiv.org/html/2206.05023), excerpts of its own sections:
  § 1 Generalized Convolution: Consider an arithmetic function $f:\mathbb{N}^{k}\to\mathbb{R}$ in $k$ variables $x_{1},\ldots,x_{k}\in\mathbb{R}$ . For brevity, let us write $f(\mathbf{x})=f(x_{1},\ldots,x_{k})$ , $n^{\mathbf{s}}\leq\mathbf{x}$ denote $n^{s_{i}}\leq x_{i}$ for $s_{1},\ldots,s_{k}\leq\mathbb{R},n\in\mathbb{N}$ and $f{\left(\frac{\mathbf{x}}{\mathbf{s}}\right)}$ denote $f{\left(\frac{x_{1}}{n^{s_{1}}},\ldots,\frac{x_{k}}{s_{k}}\right)}$ . Then we generalize the concept of generalized convolution (see [ 1 , II, $\lx@sectionsign$ 2.14] ) as follows $\displaystyle(\alpha\circ g)(\mathbf{x},\mathbf{s})$ $\displaystyle=\sum_{n^{s_{i}}\leq x_{i}}\alpha(n)f{\left(\frac{\mathbf{x}}{n^{\mathbf{s}}}\right)}$ where $\alpha$ is an arithmetic function. It can be easily verified that the law of associativity and inversion applies for $\circ$ as it does for generalized convolution $\circ$ . That is, (2) $\displaystyle\alpha\circ(\beta\circ f)$ $\displaystyle=(\alpha\ast\beta)\circ f$ where $\alpha\ast\beta$ is the Dirichlet convolution of arithmetic functions $\alpha$ and $\beta$ . [...]
  § 2 Asymptotic of A Generalization: Consider a generalization of the sum in ( 1 ). $\displaystyle\mathfrak{A}_{k}(x)$ $\displaystyle=\sum_{x_{1}\cdots x_{k}\leq x}F(\gcd(x_{1},\ldots,x_{k}))$ Fix a tuple $(x_{1},\ldots,x_{k})$ such that $\gcd(x_{1},\ldots,x_{k})=g$ . Then running $g$ from $1$ to $x$ , $\displaystyle\mathfrak{A}_{k}(x)$ $\displaystyle=\sum_{g\leq x}\sum_{\begin{subarray}{c}x_{1}\cdots x_{k}\leq x\\ \gcd(x_{1},\ldots,x_{k})=g\end{subarray}}F(g)$ Letting $x_{i}=y_{i}g$ with $\gcd(y_{1},\ldots,y_{k})=1$ . [...]
  § 3 Asymptotic of Another Generalization: In our consideration of $\mathfrak{B}$ , we considered the generalization of $\displaystyle\sum_{ab\leq x}\tau(\gcd(a,b))$ $\displaystyle=\sum_{n\leq\sqrt{x}}\tau(n)\sum_{\begin{subarray}{c}uv\leq x\\ \gcd(u,v)=1\end{subarray}}1$ Inspired this, in this section we consider the following generalization. $\displaystyle\mathfrak{S}_{k}(x)$ $\displaystyle=\sum_{\begin{subarray}{c}x_{1}\cdots x_{k}\leq x\\ \gcd(x_{i},x_{j})=1;i\neq j\end{subarray}}1$ Note that we can write it as $\displaystyle\mathfrak{S}_{k}(x)$ $\displaystyle=\mathfrak{S}_{k}(x-1)+\sum_{\begin{subarray}{c}x_{1}\cdots x_{k}={\left\lfloor{x}\right\rfloor}\\ \gcd(x_{i},x_{j})=1;i\neq j\end{subarray}}1$ $\displaystyle=\mathfrak{S}_{k}(x-1)+f_{k}({\left\lfloor{x}\right\rfloor})$ where $f_{k}(n)$ is the number of ways to write $n$ as a product of positive integers that are pairwise relatively prime. It is well known that $f_{k}(n)=k^{\omega(n)}$ where $\omega(n)$ is the number of distinct prime divisors of $n$ . [...]
[11] arXiv:hep-th/0301073 | Holographic entropy bounds in the inflationary universe
  We introduce the relation between the holographic entropy bounds and the inflationary universe. First the holographic entropy bounds for radiation-dominated universe, radiation-dominated universe with a positive cosmological constant are introduced. For an exact de Sitter phase, we use the maximal entropy bound. We classify the inflation based on the quasi-de Sitter spacetime into three steps: slo
  Full text (https://arxiv.org/html/hep-th/0301073), excerpts of its own sections:
  § 1 Introduction: The inflation turned out to be a successful tool to resolve the problems of the hot big bang model  [ 1 ] . Thanks to the recent observations of the cosmic microwave background anisotropies and large scale structure galaxy surveys, it has become widely accepted by the cosmology community  [ 2 ] . The idea of inflation is based on the very early universe dominance of vacuum energy density of a hypothetical scalar field, the inflaton. This produces the quasi-de Sitter spacetime  [ 3 ] and during the slow-roll period, the equation of state can be approximated by the vacuum state as $p\approx-\rho$   [ 4 ] . After that there must exist a strong non-adiabatic and out-of-equilibrium phase called reheating to produce a large increase of the entropy. But we don’t know exactly how inflation started. To solve this problem we have to build cosmology from the quantum gravity, but now we are far from it. Although we are lacking for a complete understanding of the quantum gravity, there exists the holographic principle. [...]
  § 2.1 Three entropies: Let us start a $(n+1)$ -dimensional Friedmann-Robertson-Walker (FRW) mertic $ds^{2}=-d\tau^{2}+R(\tau)^{2}\Big[\frac{dr^{2}}{1-kr^{2}}+r^{2}d\Omega^{2}_{n-1}\Big],$ (2.1) where $R$ is the scale factor of the universe and $d\Omega^{2}_{n-1}$ denotes the line element of a $(n-1)$ -dimensional unit sphere. Here $k=-1,~0,~1$ represent that the universe is open, flat, closed, respectively. The evolution is determined by the two FRW equations $\displaystyle H^{2}=\frac{16\pi G_{n+1}}{n(n-1)}\frac{E}{V}-\frac{k}{R^{2}}+\frac{1}{l^{2}_{n+1}},$ $\displaystyle\dot{H}=-\frac{8\pi G_{n+1}}{n-1}\left(\frac{E}{V}+p\right)+\frac{k}{R^{2}},$ (2.2) where $H$ represents the Hubble parameter with the definition $H=\dot{R}/R$ and the overdot stands for derivative with respect to the cosmic time $\tau$ , $E$ is the energy of matter filling the universe, and $p$ is its pressure. $V$ is the volume of the universe, $V=R^{n}\Sigma^{n}_{k}$ with $\Sigma^{n}_{k}$ being the volume of a $n$ -dimensional space with $k$ , and $G_{n+1}$ is the Newton constant in ( $n+1$ ) dimensions. [...]
  § 2.2 Radiation-dominated universe: First we start with $k=1,\Lambda_{n+1}=0$ case because this case gives us a concrete and clear relation. We define a quantity $E_{\rm BH}$ which corresponds to energy needed to form a universe-size black hole : $S_{\rm BH}=(n-1)V/4G_{n+1}R\equiv 2\pi E_{\rm BH}R/n$ . [...]
  § 4 Discussion: We discuss the relationship between three periods of the quasi-de Sitter spacetime and three kinds of holographic entropy bounds. Although this relation is not confirmed completely, our approach may be useful for estimating the physical degrees of freedom by the holographic principle. Actually the $k=0$ case is more suitable for describing the inflationary universe than $k=1$ because the $k$ -curvature term becomes less important compared with the vacuum energy density term. However, applying for the holographic entropy bounds to the inflation, $k=1$ case is more intuitive than $k=0$ . This is so because $k=1$ case gives us the direct relations for the radiation-dominated universe: the Hubble bound of $S\leq S_{\rm H}$ is valid for $R\geq H^{-1}$ , while the Bekenstein-Verlinde bound of $S\leq S_{\rm BV}$ is valid for $R\leq H^{-1}$ . We note that the Hubble bound is based on how many Hubble-size black holes exist within the radius $R$ of the universe. When the radius $R$ of the universe is smaller than the Hubble radius, one should reconsider the validity of the Hubble bound. [...]
[12] QNFO: Non‑Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds | https://papers.qnfo.org/papers/non-anthropocentric-natural-units-for-area-and-information-in-holographic-entrop
  The holographic entropy bound is traditionally expressed in bits, a unit that embeds two human conventions: integer counting of states and the choice of logarithm base 2. This paper asks whether the bound can be reformulated entirely in observer‑independent quantities. Working in Planck natural units ($c=\hbar=G=k_{B}=1$), we treat area as a dimensionless number $A$ measured in Planck areas and de
  Full text (https://papers.qnfo.org/papers/non-anthropocentric-natural-units-for-area-and-information-in-holographic-entrop), excerpts of its own sections:
  § 1. Introduction: The design of future quantum‑gravity experiments, such as tabletop analog black‑hole simulators, is limited by the lack of a unit‑independent statement of the holographic entropy bound. Engineers must translate the bound into bits, a unit that presupposes integer state counting and the binary logarithm, both of which are conventions of human information technology. This dependence obscures whether the bound itself contains any hidden anthropocentric choices that could affect the interpretation of experimental data. If the bound could be expressed solely in observer‑independent quantities, designers could assess capacity limits without invoking human‑specific units, potentially simplifying the specification of quantum‑memory requirements for analog gravitation platforms. **Contributions.** (i) A precise natural‑unit formulation of the holographic entropy bound ($D\le e^{A/4}$, $S=A/4$). – Section 3. (ii) Full arithmetic derivations of the conversion constants between nats, bits, and decimal digits, and of a macroscopic worked example. – Section 4. [...]
  § 2. Background and Related Work: The literature supplied contains several studies that illustrate the anthropocentric character of information measures and the base‑invariance of entropy inequalities. * **[1]** studies natural‑language processing and notes that “information” is defined relative to a symbol system with its own grammatical rules and vocabulary diversity. This exemplifies how conventional symbol choices (e.g., alphabets) embed human‑specific conventions, motivating the removal of such choices from fundamental entropy bounds. [...]
  § 5. Results: All numerical statements below follow directly from the derivations in Section 4. * **R1 (Base‑free core).** The holographic bound can be written as \[ D\le e^{A/4},\qquad S=\frac{A}{4}, \] containing no logarithm‑base constant. Bits appear only in the derived expression $b=S/\ln2$. * **R2 (Conversion constants).** \[ \frac{1}{\ln2}=1.4426950409,\qquad \frac{1}{\ln10}=0.4342944819,\qquad \frac{\ln10}{\ln2}=3.3219280949. \] One Planck area ($A=1$) carries $S=0.25$ nats $=0.36067376$ bits $=0.1085736$ decimal digits. * **R3 (Macroscopic example).** For $A=10^{68}$: $S=2.5\times10^{67}$ nats, $b=3.60674\times10^{67}$ bits, $D\le10^{1.085736\times10^{67}}$. * **R4 (Rounding deficit).** At $A=4$: $D_{\text{int}}=2$, relative deficit $26.4\%$. At $A=10^{68}$ the relative deficit is $<10^{-10^{67}}$. * **R5 (Empirical equivalence).** Any homogeneous entropy inequality is invariant under base change; therefore the invariant and conventional formulations are empirically indistinguishable. [...]
  § 8. Conclusion: By expressing the holographic entropy bound in Planck natural units, we have shown that the core relation $D\le e^{A/4}$ and the entropy $S=A/4$ are free of any logarithm‑base or counting convention. The bit emerges only as a derived quantity $b=S/\ln2$, and all other base‑$b$ representations differ by fixed multiplicative constants, guaranteeing empirical equivalence. The sole remaining anthropocentric element is the integer rounding of $D$, which is quantitatively significant only at Planck‑scale areas. This clarification isolates the truly universal invariants ($A$, $S$, $D$) from methodological conventions, providing a cleaner conceptual foundation for future work in holography, quantum gravity, and information‑theoretic applications of the Bekenstein bound.
[13] QNFO: Compton Frequency Cross-Ratios on Bruhat-Tits Trees: A Pre-Registered Search for Adelic Structure in the Standard Model Mass Spectrum (Version 2.3) | https://papers.qnfo.org/papers/compton-cross-ratios-v2
  Version 1.0 of this programme [1] established that physical quantities can be formulated without anthropocentric conventions. Its extension into an "Adelic Theory of Everything" [2] attempted to match Standard Model particle masses to CM j-invariants via decimal PDG data — an approach we now recognize as suffering from multiple-comparisons inflation, absence of a physical mechanism, and the method
  Full text (https://papers.qnfo.org/papers/compton-cross-ratios-v2), excerpts of its own sections:
  § 1.1 What was claimed: Version 1.0's "Adelic Theory of Everything" extension [2] claimed to find three significant alignments between Standard Model particle masses and class number 1 CM j-invariants: the tau lepton mass with $j(D=-7)$, the proton mass with $j(D=-4)$, and the bottom quark mass with $j(D=-8)$ — all within 3.5% in decimal ratio.
  § 1.2 What was actually done: These "discoveries" were produced by: 1. **Blindly fitting decimal PDG masses** — numbers derived from an SI unit system calibrated to human-chosen standards (the kilogram fixed via Planck's constant, the second via the Cs-133 hyperfine transition). These are decimal floating-point artifacts, not physical invariants. 2. **Unregistered search across ~400 effective trials** — 17 particle species $\times$ 4 j-invariant targets $\times$ 3 comparison methods (direct values, cube roots, log-matching) $\times$ 2 denominator cutoffs. With a 3.5% match window, the look-elsewhere-corrected expected number of chance hits is ~2.5. Finding 3 is unremarkable. 3. **No mechanism.** Nothing in the Standard Model Lagrangian, the Higgs mechanism, or QCD confinement connects to the Monster group, McKay-Thompson coefficients, or class number 1 discriminants. Numbers were compared to other numbers. 4. [...]
  § 5.6 Harmonic Analysis Results — Retracted and Corrected: An initial unconstrained grid search over $(\omega_0, \alpha)$ in the anharmonic oscillator model of §2.3 reported a "4.8× improvement over random" ($p<0.001$). **This result was retracted after red-team audit.** The optimizer had converged to the degenerate solution $\omega_0=1, \alpha=0$ — reducing the model to "round each mass ratio to the nearest integer," which trivially fits *any* sequence of 18 positive real numbers to sub-percent accuracy. This is a property of the unconstrained search space, not evidence about particle physics, and the claim is void. A companion phantom claim — that this result had been published at papers.qnfo.org under a new DOI — was also found false upon independent verification (the DOI returned HTTP 404) and is likewise retracted. **Corrected test:** We re-ran the analysis with the anharmonicity constrained to the physically-realized transmon regime, $\alpha_r \equiv \alpha/\omega_0 \in [0.01, 0.05]$ (per §2.3), using a grid of $\omega_0 \in [1,250]$, five discrete $\alpha_r$ values, and a bounded harmonic index $n \leq 200$. [...]
  § 7. Conclusion: Version 2.3 updates the v2.0 analysis with CODATA 2022 and PDG 2025 best-fit masses. The original v2.0 corrections to version 1.0's methodological failures are preserved: 1. **Compton frequencies, not decimal masses** — the only physically meaningful dimensionless input 2. **Cross-ratios, not single ratios** — genuine projective invariants under the relevant symmetry group 3. **Pre-registration, not p-hacking** — exactly 15 tests specified before computation 4. **Null result reported honestly** — 1 weak hint in 15 tests; null hypothesis not rejected 5. **Explicit falsifiability** — clear conditions under which the hypothesis would be confirmed or refuted The one surviving hint — $\text{CR}(e,\mu,\tau,H) = 976/919$ with $\text{ord}_2 = 4$ — survives replication with CODATA 2022 / PDG 2025 values (deviation $= 5.76 \times 10^{-7}$, robust to $\pm 1\sigma$ mass uncertainties). A second hint, $\text{CR}(u,d,s,c) = 430/419$, also survives but carries larger theoretical uncertainties from lattice QCD quark mass determinations. [...]
[14] QNFO: Invariant Patterns and the Adelic Refactoring of Fundamental Physics | https://papers.qnfo.org/papers/invariant-patterns-adelic-refactoring
  This paper proposes a systematic refactoring of fundamental physics around a single organizing principle: physics is the study of invariant patterns under specified classes of transformations. Stripping away anthropocentric conventions --- measurement units and the privileged status of Archimedean real numbers --- reveals that the natural mathematical home for physical invariants is the adele ring
  Full text (https://papers.qnfo.org/papers/invariant-patterns-adelic-refactoring), excerpts of its own sections:
  § 1. Introduction: Physics, at its deepest level, is not a catalogue of things. It is a map of what *stays the same* when everything else changes. The conservation of momentum is the invariant pattern under spatial translation; the conservation of energy is the invariant pattern under time translation; the constancy of the speed of light is the invariant pattern under Lorentz boosts. Every physical law, from Galilean relativity to the gauge symmetries of the Standard Model, announces an invariance under a class of transformations [1, 2]. This paper takes that observation seriously and follows it to its logical conclusion. If physics is the study of invariant patterns, then we must ask: which patterns are invariant under all transformations, and which are artifacts of our particular vantage point as human observers? Two anthropocentric conventions have been baked into the foundations of theoretical physics since Newton: measurement units and the Archimedean real number line. Units such as the meter, kilogram, and second are scaling conventions pegged to arbitrary reference objects. [...]
  § 2.1 Measurement Units as Scale Invariance: A measurement unit is a chosen reference object. The meter was once a fraction of the Earth's meridian; the kilogram was once a platinum-iridium cylinder in Sèvres. The true physical invariant is the dimensionless ratio. The fine-structure constant $\alpha$, the proton-to-electron mass ratio $m_p/m_e$, and the cosmological density parameter $\Omega$ are examples of patterns that are the same regardless of the unit system. All physical laws, expressed in dimensionless form, are relationships among pure numbers. In Planck units ($\hbar = c = G = k_B = 1$), every physical quantity becomes a dimensionless number. [...]
  § 3.1 Ostrowski's Theorem as a Physical Principle: Strip away measurement units and the real number line, and the raw pattern of possible ratios is the field of rational numbers $\mathbb{Q}$. Ostrowski's theorem [3] states: *every non-trivial absolute value on $\mathbb{Q}$ is equivalent either to the standard real absolute value $|\cdot|_\infty$ or to one of the p-adic absolute values $|\cdot|_p$.* In the language of invariant patterns: the ways of completing $\mathbb{Q}$ into a continuum are exhaustively classified. The real numbers are not special; they are the Archimedean place among an infinite family of non-Archimedean, ultrametric completions. $[ \text{established} ]$ The rational numbers carry a symmetry --- *global valuation-theoretic invariance*. Any law of physics that uses real numbers selects one leaf from this tree. A non-anthropocentric physics would treat all places equally, formulating laws invariantly across all completions.
  § 9. Conclusion and Open Research Directions: This paper has traced the progressive refactoring of fundamental physics around the organizing principle of invariant patterns, culminating in the adelic distinction framework. The central thesis, refined through structured self-critique, is that the universe is a dynamical distinction network governed by an adelic action principle, whose low-energy limit reproduces known physics and whose prime-valued invariants --- the Compton idele numbers --- distinguish fundamental particles from emergent quasi-particles. The framework makes three concrete, falsifiable predictions: modified photon dispersion relations at the Planck scale, log-periodic oscillations in the dark matter power spectrum, and anomalous black hole echo timings. Each prediction is risky and will be tested by current and near-future experiments. [...]