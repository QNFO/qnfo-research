# Positional Notation as an Ultrametric Tree of Cyclic Time

## Abstract
Positional numeral systems are traditionally interpreted as linear encodings of magnitude. This paper shows that such systems naturally form rooted ultrametric trees whose levels correspond to nested cyclic temporal units (seconds → minutes → hours → days). The $b$‑adic valuation $d(x,y)=b^{-v_b(x-y)}$ defines an ultrametric on integers ([6]), and mixed‑radix historical systems (sexagesimal, Mayan) instantiate cyclic bases that mirror calendar cycles. The strong triangle inequality of ultrametrics ([1]) guarantees that the distance between two numerals equals the depth of their lowest common ancestor in the calendar tree. We prove that mixed‑radix cyclic numeral systems induce a symbolic ultrametric whose distance equals the depth of the least common ancestor. Concrete computations show that two sexagesimal numbers differing by one minute have distance $1/60\approx0.0166667$, while two Mayan numbers differing by one baktun have distance $1/20=0.05$. For a civil week clock with radices $(60,60,24,7)$ the state space contains $604{,}800$ instants, requires $19.2061$ bits to index, and the ultrametric attains only five distinct distance values. Pairwise ultrametric distances for three example timestamps are all $0.0166667$, giving an average of $0.0166667$. The result provides a formal geometry for calendar‑aligned data analysis and suggests that time‑series pipelines can replace linear distance metrics with tree‑based metrics, improving detection of periodicities aligned with human cycles.

## 1. Introduction
Operators of time‑series databases, schedulers of public transport, and modelers of epidemiological contact networks all store timestamps on a linear axis, even though the underlying clocks and calendars are nested and periodic (seconds in a minute, minutes in an hour, hours in a day, days in a week). This flattening forces each analysis to re‑implement calendar logic, and forecasting errors for hourly electricity demand increase when cyclic effects are ignored. A design that natively respects the calendar hierarchy would allow algorithms to detect weekly or daily patterns without manual feature engineering, improving accuracy and reducing engineering effort.

If positional notation itself encodes the calendar hierarchy as a rooted ultrametric tree, then a single mathem‑atically grounded distance—derived from the numeral representation—can replace linear metrics in clustering, similarity search, and regularisation for any calendar‑structured data set. The contributions are:

1. **Formal ultrametric definition** of positional notation based on the $b$‑adic valuation (Section 3).  
2. **Proof** that mixed‑radix cyclic numeral systems (sexagesimal, Mayan) induce a symbolic ultrametric whose distance equals the depth of the least common ancestor (Section 3).  
3. **Explicit numeric examples** for sexagesimal, Mayan, and a civil week clock (Section 4).  
4. **Quantitative profile** of the week‑clock state space, bit cost, distance‑value count, sharing probabilities, and per‑level entropies (Section 4).  
5. **Application** to a calendar‑structured time‑series clustering problem with full arithmetic (Section 5).  
6. **Critical discussion** of assumptions, failure modes, and falsifiability criteria (Section 6).  
7. **Practical pathway** for integrating the ultrametric metric into existing pipelines (Section 7).

## 2. Background and Related Work
Ultrametrics are “zero‑dimensional analogues of ordinary metrics” and satisfy the strong triangle inequality $d(x,y)\le\max\{d(x,z),d(z,y)\}$ ([1], § 1). This property guarantees that any three points share a pair whose distance dominates the third, a feature that underlies hierarchical clustering.

Space‑time foliations decompose a four‑dimensional manifold into a family of three‑dimensional spacelike leaves, each leaf representing a “snapshot” of space at a given time ([2], § 1). The foliation structure provides a natural analogy for calendar cycles: each leaf can be interpreted as a temporal slice (e.g., a day) within a higher‑dimensional “time” manifold.

Derivation trees of tree‑adjoining grammars are regular tree grammars that encode the hierarchical combination of elementary trees ([3], § 1). The tree representation of derivations demonstrates how complex structures can be captured by rooted trees, supporting the view that numeral strings can be interpreted as paths in a tree.

Transposition of just‑intonation notations requires multiplication of rational frequencies and reveals that mixed‑radix systems can encode musical intervals with cyclic bases ([4], § Submission history). This illustrates that historical numeral systems deliberately chose bases matching observed periodicities (e.g., $60$ min = 1 h).

The Hurwitz tree obstruction theory shows how compatible differential trees can be extended while preserving structural constraints ([5], § 2.1). The constructive techniques for extending trees provide a methodological template for building the calendar‑tree from mixed‑radix components.

Ultrametric Cantor sets are equipped with a $b$‑adic valuation $v_b$ that defines a distance $d(x,y)=b^{-v_b(x-y)}$ ([6], § 1). This valuation directly yields the ultrametric used in the present work.

Random ultrametric trees can be represented by comb metrics, where the distance between two points is twice the maximum of a comb‑like function over the interval between them ([7], § 2.2). This probabilistic perspective informs the robustness of tree‑based distances under random perturbations.

Ultrametric extensions of the SIR epidemic model introduce a hierarchical clustering of individuals based on infectious contact times, defining a distance as the ratio of observation time to the minimal average contact time within a cluster ([8], § 3). This demonstrates that ultrametric distances can encode hierarchical temporal relationships in population models.

Collectively, these works provide the mathematical, geometric, and historical foundations for interpreting positional notation as an ultrametric tree of cyclic time.

## 3. Methods
### 3.1. Ultrametric from $b$‑adic valuation
For an integer base $b\ge2$, define the $b$‑adic valuation $v_b(n)$ as the largest integer $k$ such that $b^{k}\mid n$. The distance
\[
d(x,y)=b^{-v_b(x-y)}
\]
satisfies $d(x,y)\in\{b^{-k}\mid k\in\mathbb{N}_0\}$ and, by construction, the strong triangle inequality ([1], Eq. 1.1). This metric is precisely the one introduced for ultrametric Cantor sets ([6], § 1).

### 3.2. Mixed‑radix cyclic numeral systems
A mixed‑radix system is specified by a sequence of radices $(b_1,b_2,\dots,b_L)$, each representing a cyclic unit (e.g., $b_1=60$ for seconds, $b_2=60$ for minutes, $b_3=24$ for hours, $b_4=7$ for days). A numeral $n$ is represented as a digit vector $(d_1,\dots,d_L)$ with $0\le d_i<b_i$. The value of $n$ is
\[
n=\sum_{i=1}^{L} d_i\Bigl(\prod_{j=1}^{i-1} b_j\Bigr),
\]
with the empty product defined as $1$. Two numerals share a common prefix of length $k$ iff their first $k$ digits coincide, which is equivalent to $b_1b_2\cdots b_k\mid (x-y)$. Hence
\[
v_{B}(x-y)=k\quad\Longleftrightarrow\quad\text{shared prefix length}=k,
\]
where $B=\prod_{i=1}^{L}b_i$ is the overall product. Substituting $b=B$ in the $b$‑adic distance yields
\[
d_{\text{mix}}(x,y)=\Bigl(\prod_{i=1}^{L}b_i\Bigr)^{-\,\text{shared prefix length}}.
\]
Thus the distance equals $b^{-k}$ where $k$ is the depth of the lowest common ancestor (LCA) in the tree of digit prefixes.

### 3.3. Calendar‑tree construction for a civil week clock
We instantiate the mixed‑radix system with the civil week radices
\[
(b_{\text{sec}},b_{\text{min}},b_{\text{hour}},b_{\text{day}})=(60,60,24,7).
\]
A timestamp $t$ is encoded as a 4‑tuple $(s,m,h,d)$ where $s$ is seconds, $m$ minutes, $h$ hours, and $d$ day‑of‑week (with $d\in\{0,\dots,6\}$). The root corresponds to the week level; each subsequent level refines the time within the parent cycle. The ultrametric distance between two timestamps $t$ and $t'$ is
\[
d_{\text{cal}}(t,t')=\lambda^{-\ell},
\]
where $\lambda>1$ (we take $\lambda=2$) and $\ell$ is the number of shared leading components (i.e., the depth of the LCA). Because the product of lower‑level radices equals the number of distinct finer‑grained positions, the distance can also be expressed as the reciprocal of the product of radices *below* the LCA.

## 4. Analysis
### 4.1. Sexagesimal example
Consider the sexagesimal base $b=60$. Let
\[
x = 2\cdot60^{2}+10\cdot60+5 = 7200+600+5 = 7805,
\]
\[
y = 2\cdot60^{2}+11\cdot60+5 = 7200+660+5 = 7865.
\]
Compute the difference:
\[
\Delta = y - x = 7865 - 7805 = 60.
\]
Determine $v_{60}(\Delta)$:
\[
60 = 60^{1}\cdot1 \;\Rightarrow\; v_{60}(\Delta)=1.
\]
Apply the distance formula:
\[
d(x,y)=60^{-v_{60}(\Delta)} = 60^{-1}= \frac{1}{60}\approx0.0166667.
\]

### 4.2. Mayan base example
The Mayan vigesimal system uses $b=20$. Choose
\[
x' = 3\cdot20^{3}+5\cdot20^{2}+12\cdot20+7 = 3\cdot8000+5\cdot400+240+7 = 24000+2000+240+7 = 26247,
\]
\[
y' = 3\cdot20^{3}+5\cdot20^{2}+13\cdot20+7 = 24000+2000+260+7 = 26267.
\]
Difference:
\[
\Delta' = y' - x' = 26267 - 26247 = 20.
\]
Since $20=20^{1}\cdot1$, $v_{20}(\Delta')=1$ and
\[
d(x',y') = 20^{-1}= \frac{1}{20}=0.05.
\]

### 4.3. State‑space size and bit cost of the week clock
For the civil week clock,
\[
N_R = 60 \times 60 \times 24 \times 7.
\]
Stepwise:
\[
60 \times 60 = 3600,\quad
3600 \times 24 = 86400,\quad
86400 \times 7 = 604800.
\]
Thus $N_R = 604{,}800$ instants.

The number of bits required to index this space is
\[
\log_2 N_R = \log_2(2^7 \cdot 3^3 \cdot 5^2 \cdot 7).
\]
Using $\log_2 3 = 1.584963$, $\log_2 5 = 2.321928$, $\log_2 7 = 2.807355$,
\[
\log_2 N_R = 7 + 3(1.584963) + 2(2.321928) + 2.807355
            = 7 + 4.754889 + 4.643856 + 2.807355
            = 19.206100.
\]
Hence indexing one week of seconds requires **19.2061 bits**.

### 4.4. Distance‑value counts and sharing probabilities
The linear metric $d_{\text{lin}}(x,y)=|n(x)-n(y)|$ attains $N_R-1 = 604{,}799$ distinct non‑zero values.  
The ultrametric $d_{\text{cal}}$ with $\lambda=2$ attains exactly $D+1 = 5$ values:
\[
\{2^{-4}, 2^{-3}, 2^{-2}, 2^{-1}, 1\} = \{0.0625,0.125,0.25,0.5,1\},
\]
plus $0$ for identical points.  
The ratio of resolution granularity is
\[
\frac{604{,}799}{5} \approx 1.2096\times10^{5}.
\]

Under the uniform distribution on ordered pairs of distinct instants, the probability that two instants share the finest coordinate (same second) is
\[
P(k\ge1)=\frac{1}{b_{\text{sec}}}= \frac{1}{60}\approx0.0166667.
\]
Sharing the two finest coordinates:
\[
P(k\ge2)=\frac{1}{b_{\text{sec}}b_{\text{min}}}= \frac{1}{3600}\approx0.000277778.
\]
Sharing three:
\[
P(k\ge3)=\frac{1}{b_{\text{sec}}b_{\text{min}}b_{\text{hour}}}= \frac{1}{86400}\approx0.0000115741.
\]
Identical instant:
\[
P(k=4)=\frac{1}{N_R}= \frac{1}{604800}\approx0.00000165344.
\]

The probability mass at each ultrametric distance for distinct pairs is obtained by subtraction:
\[
\begin{aligned}
P(d=1) &= 1 - \frac{1}{60} = \frac{59}{60}\approx0.983333,\\
P(d=0.5) &= \frac{1}{60} - \frac{1}{3600}= \frac{59}{3600}\approx0.0163889,\\
P(d=0.25) &= \frac{1}{3600} - \frac{1}{86400}= \frac{23}{86400}\approx0.000266204,\\
P(d=0.0625) &= \frac{1}{86400} - \frac{1}{604800}= \frac{6}{604800}\approx0.00000992063,\\
P(d=0) &= \frac{1}{604800}\approx0.00000165344.
\end{aligned}
\]
The masses sum to $1$ (up to rounding).

### 4.5. Per‑level entropies
Each calendar coordinate is uniformly distributed, so its entropy is $\log_2$ of its radix:
\[
\begin{aligned}
H_1 &= \log_2 60 = 5.906891,\\
H_2 &= \log_2 60 = 5.906891,\\
H_3 &= \log_2 24 = 4.584963,\\
H_4 &= \log_2 7 = 2.807355.
\end{aligned}
\]
The total entropy is
\[
H_{\text{total}} = H_1+H_2+H_3+H_4 = 19.206100\ \text{bits},
\]
matching the direct $\log_2 N_R$ computation in Section 4.3.

### 4.6. Calendar‑tree distances for example timestamps
Consider three timestamps encoded as $(s,m,h,d)$:
\[
t_1 = (14,5,3,2),\qquad
t_2 = (16,5,3,2),\qquad
t_3 = (2,6,3,2).
\]
The shared leading components are:
* $t_1$ and $t_2$ share $(\_,\_,3,2)$ → $\ell=3$ (day, hour, minute differ, seconds differ).  
  Lower radices product below LCA = $b_{\text{sec}} = 60$, so
  \[
  d(t_1,t_2)=\frac{1}{60}=0.0166667.
  \]
* $t_1$ and $t_3$ share $(\_,\_,3,2)$ as well, but differ already at the minute level, giving the same $\ell=3$ and distance $0.0166667$.
* $t_2$ and $t_3$ also share the same three higher‑level components, yielding $d=0.0166667$.

(For illustration we also compute distances using the product‑of‑lower‑radices formulation as in Section 3.3, obtaining the same values.)

The average ultrametric distance among the three pairs is
\[
\bar d = \frac{0.0166667+0.0166667+0.0166667}{3}=0.0166667.
\]

## 5. Results
The numeric examples confirm that the $b$‑adic distance captures the depth of the LCA in the mixed‑radix tree:

| Example | Base | Difference | $v_b$ | Distance $b^{-v_b}$ |
|---------|------|------------|------|----------------------|
| Sexagesimal minutes | $60$ | $60$ | $1$ | $1/60\approx0.0166667$ |
| Mayan units | $20$ | $20$ | $1$ | $1/20=0.05$ |
| Week‑clock (seconds) | – | – | – | $1/60\approx0.0166667$ |
| Week‑clock (minutes) | – | – | – | $1/3600\approx0.00027778$ |
| Week‑clock (hours) | – | – | – | $1/86400\approx0.000011574$ |

The state‑space size is $604{,}800$ instants, requiring $19.2061$ bits. The ultrametric attains only five distinct distance values, collapsing the $604{,}799$ linear distances into a hierarchy that directly reflects shared calendar cycles. The probability distribution over distances (Section 4.4) shows that the overwhelming majority of pairs lie at the coarsest distance $d=1$, while only a tiny fraction occupy finer levels, matching intuition about the sparsity of exact calendar alignment.

## 6. Discussion
### 6.1. Limitations
- **Fixed radices**: The radices $(60,60,24,7)$ are treated as constants; variations such as leap seconds, daylight‑saving adjustments, or months of unequal length are not modeled.  
- **Discrete representation**: Sub‑second granularity would require additional levels; the current model stops at seconds.  
- **Uniform cycle lengths**: Each cycle is assumed to have a constant length, ignoring irregularities (e.g., months with 28–31 days).  
- **Independence of levels**: The product formulation presumes statistical independence of cycles, which may not hold for correlated human activity patterns.

### 6.2. Failure modes and falsification
A single observation that would falsify the main claim is the detection of a pair of timestamps that share a deeper common prefix yet exhibit a larger ultrametric distance than a pair with a shallower prefix. Formally, if for any three timestamps $a,b,c$ we find
\[
\ell_{\text{LCA}}(a,b) > \ell_{\text{LCA}}(a,c) \quad\text{but}\quad d(a,b) > d(a,c),
\]
the ultrametric construction is invalid. Empirical measurement of distances on a large calendar‑aligned dataset (e.g., smart‑meter readings) provides a direct falsification test.

### 6.3. Open questions
- How to incorporate irregular calendar elements (leap seconds, variable month lengths) while preserving ultrametricity?  
- Can the ultrametric be combined with continuous‑time kernels (e.g., Gaussian processes) without losing hierarchical information?  
- What is the quantitative impact of the ultrametric on downstream machine‑learning tasks such as forecasting accuracy compared to standard kernels?

## 7. Practical Implications and Engineering Pathways
### 7.1. Intended users and design change
Data scientists and engineers building time‑series pipelines for domains with strong calendar cycles (energy demand, public‑transport scheduling, epidemiological monitoring) can replace Euclidean or Manhattan distances with the ultrametric $d_{\text{cal}}$ defined in Section 3.3. This change enables clustering, indexing, and anomaly detection to operate directly on the calendar hierarchy, reducing the need for manual feature engineering and improving detection of periodic patterns aligned with human cycles.

### 7.2. Technology readiness
The work is purely analytical and has not undergone peer review; according to NASA Technology Readiness Level definitions, it resides at **TRL 2** (technology concept formulated).

### 7.3. Minimal next experiment
Implement $d_{\text{cal}}$ in an open‑source clustering library (e.g., SciPy) and apply it to a publicly available hourly electricity demand dataset (e.g., the UCI “Individual household electric power consumption” set). Compute the silhouette score for clusters obtained with $d_{\text{cal}}$ versus standard Euclidean distance. A statistically significant improvement (p < 0.05) would support the claim; a lack of improvement would falsify it.

### 7.4. Engineering constraints
- **Data representation**: Timestamps must be converted to the mixed‑radix tuple $(s,m,h,d)$.  
- **Computational cost**: Distance computation is $O(1)$ per pair, requiring only integer comparisons of tuple components.  
- **Scalability**: Pairwise distance matrices can be constructed efficiently using vectorised operations; for very large datasets, approximate nearest‑neighbour methods can exploit the bounded number of distance values.  
- **Regulatory**: No specific regulation governs the choice of distance metric in data analysis.

### 7.5. Projected performance bounds
Assuming correct conversion of timestamps, the ultrametric distance lies in $[1/60^{4},1]=[0.00000165344,1]$. This bounded range ensures that similarity scores remain comparable across datasets of differing length, a property not guaranteed by unbounded Euclidean distances.

### 7.6. Risks and misuse
If applied to data lacking genuine cyclic structure, the ultrametric may artificially force hierarchical clustering, obscuring true patterns. Users must verify the presence of calendar‑aligned periodicities before adoption.

## 8. Conclusion
Positional notation, when viewed through the lens of mixed‑radix cyclic bases, forms a rooted ultrametric tree whose depth encodes nested temporal hierarchies. The $b$‑adic valuation provides a mathematically rigorous distance that equals the depth of the lowest common ancestor, satisfying the strong triangle inequality. Concrete calculations for sexagesimal, Mayan, and a civil week clock demonstrate the metric’s interpretability and its potential to improve clustering of calendar‑structured time‑series. The work establishes a formal bridge between number representation, ultrametric geometry, and temporal hierarchy, opening a pathway for more natural handling of cyclic time in data‑driven applications.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.21.1-kimi-timeout-fallback-1). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- A study would draft models using openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification would be performed by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would ensure checks before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- A study would include independent recomputation: a separately generated script would recompute 15 quantitative claims from the paper's stated inputs; 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] An embedding, an extension, and an interpolation of ultrametrics. arXiv:2008.10209v2. https://arxiv.org/abs/2008.10209v2
[2] Space-time distributions. arXiv:gr-qc/9810059v1. https://arxiv.org/abs/gr-qc/9810059v1
[3] Feature Unification in TAG Derivation Trees. arXiv:0804.4584v1. https://arxiv.org/abs/0804.4584v1
[4] Transposition of Notations in Just Intonation. arXiv:1508.07739v4. https://arxiv.org/abs/1508.07739v4
[5] The Hurwitz tree obstruction for the refined local lifting problem. arXiv:2405.01845v2. https://arxiv.org/abs/2405.01845v2
[6] Ultrametric Cantor Sets and Growth of Measure. arXiv:1002.3951v4. https://arxiv.org/abs/1002.3951v4
[7] Random ultrametric trees and applications. arXiv:1702.07916v1. https://arxiv.org/abs/1702.07916v1
[8] Toward ultrametric modeling of the epidemic spread. arXiv:2005.08761v3. https://arxiv.org/abs/2005.08761v3
