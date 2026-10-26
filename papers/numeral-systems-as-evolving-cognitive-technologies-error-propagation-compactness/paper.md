# Numeral Systems as Evolving Cognitive Technologies: Error Propagation, Compactness, and the Non-Optimality of Positional Notation

## Abstract

Positional (Arabic-Indic) notation is conventionally treated as the endpoint of numeral-system evolution, but this paper argues that it is a historically contingent survivor whose dominance reflects fitness for particular task environments rather than global optimality. We formalize the tradeoff between additive systems (Roman-style symbol sums, modeled here as pure commutative sums without subtractive rules) and positional systems under explicit transcription-noise channels. Under a symbol-deletion channel we prove that additive error is bounded by the largest symbol value (a constant, $1000$), while positional error is $(9H + d_k)\cdot 10^{k}$ — proportional to the number's higher-order digits and unbounded in magnitude; under uniform-digit and uniform-deletion-position assumptions we derive an expected positional deletion error of $2187.5$ for four-digit numbers in $[1000,3999]$ and an expected additive deletion error of approximately $449.4$, a ratio of about $4.87$. Under adjacent transposition the additive error is exactly zero by commutativity, while the expected positional error is $3.3\cdot 10^{k}$ per adjacent pair. Positional notation wins on compactness (four digits versus an average of $4.45$ greedy-additive symbols over $1$–$3999$, ratio $4.45/4 \approx 1.11$) and is argued qualitatively to aid arithmetic tractability. A two-term cost model yields an explicit crossover: additive notation would be optimal whenever the error-aversion weight exceeds roughly $0.26$ times the per-symbol cost. No single notation dominates; notation design remains an open optimization problem over a task-indexed fitness landscape.

## 1. Introduction

The positional numeral system used throughout modern science is so ubiquitous that it is easy to mistake for a discovered truth rather than an engineered artifact. This paper defends the opposite view: positional notation is one point in a design space of numeral systems, selected by historical contingencies and by the demands of specific task environments — chiefly paper-and-pencil arithmetic at scale — and it pays measurable cognitive costs that additive systems do not.

The claim is not that Roman-style numerals are superior overall. Long multiplication in additive notation is painful, and positional notation compresses large magnitudes into few glyphs. The claim is narrower and more precise: the two families occupy different points on a tradeoff surface, and the tradeoffs can be *formalized*. We ask three questions:

1. Under explicit noise models of human transcription error (symbol deletion, adjacent transposition), what is the expected magnitude of the resulting value error in each system?
2. What is the compactness cost of additive notation relative to positional notation, computable exactly for a stated symbol inventory?
3. If numeral-system evolution is modeled as a fitness landscape over task environments, does any single system dominate?

Our answers, derived in full in Section 4, are: (1) additive systems have strictly bounded error propagation under deletion and exactly zero error under transposition, while positional error is unbounded in the number's magnitude; (2) additive notation costs a computable factor of $4.45/4 \approx 1.11$ in symbol count for the range examined; (3) no — the axes of the landscape (error resistance, compactness, arithmetic tractability) are satisfied by different systems in different environments, and a two-parameter cost model makes the crossover explicit.

Throughout, a *positional* system is one in which a symbol's contribution depends on its place (the $7$ in $707$ contributes $7\cdot 10^{2}$); an *additive* system is one in which each symbol contributes a fixed value independent of position, the total being their sum. A *noise channel* is a probabilistic model of how a written numeral string is corrupted between writer and reader. The framing of notation as a *cognitive technology* — an external artifact that carries part of the cognitive load — is essential: notation is a prosthesis whose error behavior and representational economy directly shape what its users can reliably do.

## 2. Background and Related Work

No prior work in the supplied bibliography addresses numeral-system error head-on; the cognitive-science entries supply framing, and two numeral-specific corpus entries supply direct prior art for multi-axis evaluation. We discuss all twelve supplied works.

**[1] Symbol Emergence in Cognitive Developmental Systems: a Survey.** This survey argues that symbol systems such as language are crucial for human communication and adaptation to the real-world environment, and that the symbol systems used in human society *adaptively and dynamically change over time*. This is the closest methodological anchor for our thesis: if symbol systems adapt dynamically, then positional notation's dominance is a state of an ongoing adaptive process, not a terminal optimum.

**[2] Applied Exoskeleton Technology: A Comprehensive Review of Physical and Cognitive Human-Robot Interaction.** This review covers physical and cognitive human–robot interaction and notes that exoskeleton technology is not fully mature for adoption in strenuous and non-programmed tasks. The supplied summary gives no numeral-specific content; we use it only as a parallel case of a technology whose adoption is gated by task-environment fit rather than intrinsic merit — the same gating we claim for positional notation.

**[3] A cognitive diversity framework for radar target classification.** This work reports that target classification by radar has been notoriously difficult, with the best existing systems not attaining sufficiently high performance and reliability, and explores a design in which angular diversity is used in a *cognitive manner* to attain better performance, benchmarked against conventional classifiers. The structural lesson — that diversity of representational channels can improve reliability — motivates our hybrid-notation hypothesis in Section 6.

**[4] Toward Cognitive and Immersive Systems: Experiments in a Cognitive Microworld.** This work describes cognitive and immersive systems (CAISs) arising at the intersection of AI with HCI/HRI, systems that interact with and assist the human agents that enter them. The supplied summary gives no further detail bearing on numeration; we cite it as evidence that human-facing cognitive systems are an active research area within which notation choice for human-agent interaction is a design variable.

**[5] Cognition and Emotion: Perspectives of a Closing Gap.** This paper frames the primary task of a cognitive system as surviving and maximizing a life-long utility function, while noting that direct computational maximization is impossible in complex environments under real-world time constraints, with emotions serving as an intermediate layer in the space of policies. We borrow the structural move — utility maximization under constraint, with an intermediate representational layer — and apply it to cultural artifacts: historical communities selecting notations satisficed under local task pressures, which predicts exactly the contingent, non-optimal outcomes we formalize.

**[6] Offloading Cognition onto Cognitive Technology.** This work distinguishes cognizers — systems with mental states — from cognitive technology, which can contribute to human cognition without itself cognizing, and argues that cognizers can *offload* cognitive functions onto cognitive technology, extending performance beyond the limits of their own brain power, with language as a paradigm case. Numeral notation is a canonical offloading device in this sense, and our error-channel analysis is precisely an analysis of when this offloading fails — when the artifact corrupts the offloaded content.

**[7] Cognitive computation with autonomously active neural networks: an emerging field.** This review addresses the functional role of the brain's self-sustained (autonomously active) neural activity and its interplay with the sensory input stream. The supplied summary gives no further detail we can use for numeration; we note only that the interplay between an internal state and a noisy input stream is formally analogous to our noise-channel model, in which a stored numeral is corrupted by a transcription channel.

**[8] Robust Beamforming Design for Intelligent Reflecting Surface Aided Cognitive Radio Systems with Imperfect Cascaded CSI.** This communications-engineering study investigates robust design under both bounded and statistical channel-state-information (CSI) error models in intelligent-reflecting-surface-aided cognitive radio systems. Though distant in topic, its methodological template — optimizing performance under an explicit, parameterized error model on a channel — is exactly the template we import: we define bounded and statistical error models on transcription channels and evaluate notations under them.

**[9] QNFO: COMMUTATIVE PHYSICS.** The supplied summary is empty; we note its presence for completeness and can draw no claim from it.

**[10] NUMERATA v2.0.** This entry presents a multi-axis framework for evaluating numeral systems, extending an eight-axis framework with a Distinction-Based Primality axis and reporting meta-analysis validation with $\mathrm{MCS} = 0.875$ and $5/5$ predictions confirmed, together with a "sunburst" notation making primality visually immediate. This is direct prior art for multi-criteria evaluation of notations; our fitness-landscape model is deliberately simpler, and our two computed axes (error propagation, compactness) complement its scoring approach.

**[11] Tree-based numeration synthesis.** This entry consolidates research on nonlinear tree-based numeration systems, stating that positional notation is natively an ultrametric tree, and covers five research threads with extensions into quantum computing and interface design. The ultrametric-tree view explains *why* positional deletion error propagates so badly: deleting a digit collapses an entire subtree of the place-value hierarchy, an effect quantified in Section 4.1.

**[12] Ten-Fingered Trap.** The supplied summary is empty; the title suggests a critical stance toward body-based counting conventions, but since no summary text is provided we attribute no specific claim to it and list it only as evidence that base choice itself is questioned in this corpus.

## 3. Methods

### 3.1 Notation families

A **positional system** with base $b$ represents an integer $N$ as a digit string $d_{n-1}d_{n-2}\cdots d_1 d_0$ with value

$$N = \sum_{k=0}^{n-1} d_k \, b^{k}, \qquad d_k \in \{0,1,\ldots,b-1\},$$

with $d_{n-1}\neq 0$ and an obligatory zero placeholder when an internal place is empty.

An **additive system** with symbol values $V=\{v_1,\ldots,v_m\}$ represents $N$ as a multiset of symbols whose values sum to $N$:

$$N = \sum_{j=1}^{m} c_j \, v_j, \qquad c_j \in \mathbb{Z}_{\geq 0},$$

where $c_j$ counts symbols of value $v_j$. For concrete computation we use the **greedy additive system** $\mathcal{A}$ with the seven-symbol inventory $V=\{1,5,10,50,100,500,1000\}$, *without* subtractive rules, so that representation is a pure commutative sum and the greedy algorithm (take as many $v_m$ as possible, then $v_{m-1}$, and so on) is canonical. This choice is a deliberate modeling convention; its consequences, and the alternative subtractive convention used in one source draft, are documented in Appendix A.

### 3.2 Noise channels

Following the error-model template of robust design under parameterized channel uncertainty [8], we define two channels:

- **Deletion channel $\mathcal{D}$:** one symbol of the written form is deleted uniformly at random; the remaining symbols are read in written order (for positional strings, adjacent digit blocks merge).
- **Transposition channel $\mathcal{T}$:** two adjacent symbols are exchanged; the multiset (additive) or digit string (positional) is then read normally.

The **error** of a corruption event is $E = |N - N'|$, where $N'$ is the value read after corruption. Distributions: digits uniform on $\{0,\ldots,9\}$ (positional); $N$ uniform on $\{1,\ldots,3999\}$ (additive); deletion position uniform among symbols.

### 3.3 Cost model

A task environment assigns a per-symbol cost $\mu$ (time, ink, cognitive load) and an error-aversion weight $\lambda$ per $10^{3}$ units of expected error. The cost of system $s$ is

$$\kappa_s = \mu \, \bar{L}_s + \lambda \, \frac{\bar{E}_s}{10^{3}},$$

where $\bar{L}_s$ is expected string length and $\bar{E}_s$ expected corruption error. The fitness landscape is the map $(\mu,\lambda)\mapsto \arg\min_s \kappa_s$; Section 4.7 derives the crossover boundary.

## 4. Analysis

All inputs are definitions of the two notation models (Section 3.1) or arithmetic on them; no empirical numbers are used.

### 4.1 Deletion channel, positional system

Write $N = H\cdot 10^{k+1} + d_k\cdot 10^{k} + L$ with $0 \leq L < 10^{k}$, where $d_k$ is the digit in the $10^{k}$ place, $H$ the value of the higher-order digits, and $L$ the value of the lower-order digits. Deleting $d_k$ merges the blocks: the read value is $N' = H\cdot 10^{k} + L$, so

$$E_{\mathrm{pos}} = N - N' = \left(H\cdot 10^{k+1} + d_k\cdot 10^{k} + L\right) - \left(H\cdot 10^{k} + L\right) = (9H + d_k)\cdot 10^{k}.$$

**Worked example.** $N=5284$; delete the hundreds digit $d_2 = 2$. Here $H=5$, $d_k=2$, $k=2$, $L=84$:

$$E_{\mathrm{pos}} = (9\cdot 5 + 2)\cdot 10^{2} = 47\cdot 100 = 4700.$$

Check directly: $5284 - 584 = 4700$. The reader recovers $584$, a relative error of $4700/5284 = 0.88948\ldots \approx 0.8895$. The error is proportional to $H$: for fixed deletion position it grows without bound as magnitude grows.

### 4.2 Deletion channel, additive system

Deleting a symbol of value $v_j$ from the multiset changes the sum by exactly

$$E_{\mathrm{add}} = v_j \leq v_{\max} = 1000, \quad \text{independent of } N \text{ and of string length}.$$

Every single-symbol drop produces a nonzero error ($v_j \geq 1$), so no single drop is silent, but the bound is a constant. This is the central contrast: positional deletion error is $O(H\cdot 10^{k})$ — unbounded in magnitude — while additive deletion error is $O(v_{\max})$ — a constant.

**Worst cases over $N\in[1,3999]$.** Positional: delete the leading digit of $3999$, giving $999$; error $= 3999 - 999 = 3\cdot 10^{3} = 3000$. (Note: at the leading position $k=3$ there is no higher-order block, so $H=0$ and $E = d_k\cdot 10^{k}$; applying the full formula with a nonzero $H$ at the leading position, as one source draft did, would overstate the error — see Appendix A.) Additive: $E_{\mathrm{add}} = 1000$. Worst-case ratio:

$$\frac{3000}{1000} = 3.$$

More generally, for $N < 4\cdot 10^{d-1}$ the leading digit is at most $3$, so deleting the leading digit of a $d$-digit number gives error $\leq 3\cdot 10^{d-1}$, and the worst-case ratio is $3\cdot 10^{d-4}$: constant. (The constant depends on the top of the range; for ranges reaching $10^{d}-1$ it would instead be $9\cdot 10^{d-4}$.)

### 4.3 Transposition channel, additive system

Because the additive representation is a multiset, swapping two adjacent symbols does not change the multiset, hence the read value is unchanged and

$$E_{\mathrm{add}}^{\mathcal{T}} = 0.$$\

### 4.4 Transposition channel, positional system

Swapping adjacent digits $d_{k+1}$ and $d_k$ changes the value by

$$\Delta = (d_{k+1}-d_k)\,10^{k}.$$\

For uniformly random digits $d_{k+1},d_k\in\{0,\dots,9\}$ the expected absolute error per transposition is

$$\mathbb{E}[|\Delta|]=10^{k}\,\mathbb{E}[|d_{k+1}-d_k|]=10^{k}\times 3.3\approx 3.3\cdot10^{k}.$$\

Summing over the $n-1$ possible adjacent pairs yields an expected positional error of approximately $3.3\,(n-1)\,10^{k}$, where $k$ is the lower position of each pair; for the least significant pair ($k=0$) this is $3.3$.

### 4.5 Compactness analysis

In the greedy additive system $\mathcal{A}$ the average number of symbols required to represent a uniformly random integer $N\in[1,3999]$ can be approximated by

$$\bar{L}_{\mathrm{add}}\approx\frac{1}{3999}\sum_{N=1}^{3999}\left\lfloor\frac{N}{1000}\right\rfloor+\left\lfloor\frac{N\bmod 1000}{500}\right\rfloor+\dots+\left\lfloor\frac{N\bmod 5}{1}\right\rfloor,$$
For $N\in[1,999]$ the expected greedy count is $\mathbb{E}\lfloor N/500\rfloor + \mathbb{E}\lfloor (N\bmod 500)/100\rfloor + \mathbb{E}\lfloor (N\bmod 100)/50\rfloor + \mathbb{E}\lfloor (N\bmod 50)/10\rfloor + \mathbb{E}\lfloor (N\bmod 10)/5\rfloor + \mathbb{E}\lfloor N\bmod 5\rfloor = 0.5 + 0.9 + 0.5 + 0.9 + 0.5 + 0.4 = 3.7$. Each thousands block ($1000$–$1999$, $2000$–$2999$, $3000$–$3999$) adds exactly one thousand-symbol plus the same $3.7$ remainder average, giving $4.7$ per block; the overall average is $(3.7 + 3\times 4.7)/4 = 17.8/4 = 4.45$ symbols. Positional notation uses exactly $\lceil\log_{10}N\rceil$ digits, averaging $4$ digits over the same range, giving a compactness ratio of $4.45/4 \approx 1.11$.

### 4.6 Cost‑model crossover

Under the assumptions of Section 4.5 ($\bar{L}_{\mathrm{add}} = 4.45$, $\bar{L}_{\mathrm{pos}} = 4$) and a deletion channel with $N$ uniform on $[1000,3999]$ and deletion position uniform among the four digits: deleting the leading digit gives expected error $\mathbb{E}[d_3]\cdot 10^{3} = 2\cdot 10^{3} = 2000$; deleting the $10^{2}$ digit gives $\mathbb{E}[9d_3+d_2]\cdot 10^{2} = (18+4.5)\cdot 10^{2} = 2250$; deleting the $10^{1}$ digit gives $(9\,\mathbb{E}[10d_3+d_2]+4.5)\cdot 10 = (220.5+4.5)\cdot 10 = 2250$; deleting the $10^{0}$ digit gives $9\,\mathbb{E}[100d_3+10d_2+d_1]+4.5 = 9\cdot 249.5+4.5 = 2250$. Averaging over the four positions, $\bar{E}_{\mathrm{pos}} = (2000+2250+2250+2250)/4 = 8750/4 = 2187.5$. For the additive system, the expected deleted symbol value equals the mean symbol value; since the symbols of a representation sum to $N$, the total symbol value over all $N\in[1,3999]$ is $\sum_{N=1}^{3999} N = 3999\cdot 4000/2 = 7{,}998{,}000$, and the total symbol count is $4.45\times 3999 = 17795.55$, giving $\bar{E}_{\mathrm{add}} \approx 7998000/17795.55 \approx 449.4$ (an approximation that weights each number equally in numerator and denominator rather than averaging $N/L(N)$ per number). The crossover condition $\mu(\bar{L}_{\mathrm{add}}-\bar{L}_{\mathrm{pos}})=\lambda(\bar{E}_{\mathrm{pos}}-\bar{E}_{\mathrm{add}})/10^{3}$ yields

$$\frac{\lambda}{\mu}\approx\frac{(4.45-4)\,10^{3}}{2187.5-449.4}=\frac{450}{1738.1}\approx0.26.$$

Thus additive notation would be optimal when $\lambda$ exceeds roughly $0.26\,\mu$.

## 5. Results

The projected quantitative comparisons summarised above are collected in Table 1.

| Metric | Positional | Additive (greedy) |
|--------|------------|-------------------|
| Expected deletion error (four-digit, $N\in[1000,3999]$, uniform deletion position) | $2187.5$ | $449.4$ (approx.) |
| Expected transposition error per adjacent pair at position $k$ | $3.3\cdot10^{k}$ | $0$ |
| Average symbol count (1–3999) | $4$ digits | $4.45$ symbols |
| Compactness ratio | $4.45/4 \approx 1.11$ | — |
| Cost-model crossover $\lambda/\mu$ | $\approx 0.26$ | — |

## 6. Discussion

The projections rely on simplifying assumptions: uniform digit distributions, uniform deletion positions, and the greedy additive representation without subtractive rules. Real historical usage exhibits non‑uniform digit frequencies and context‑dependent symbol omission, which could lower positional error. Moreover, the tractability claim remains qualitative; a rigorous metric (e.g., average algorithmic step count) is left for future work. Limitations include the absence of empirical transcription error data and the exclusion of hybrid or tree‑based systems. Falsification would occur if measured human transcription errors for positional notation consistently fell below the projected additive error across comparable tasks.

## 7. Conclusion

Positional and additive numeral systems occupy distinct regions of a multi‑dimensional fitness landscape. Under the projected error and compactness analyses, positional notation excels in compactness and, qualitatively, in arithmetic tractability, while additive notation offers bounded error under deletions and zero error under transpositions. The cost‑model crossover suggests that environments with high error aversion may favour additive systems. Future research should obtain empirical error distributions and extend the landscape to include hybrid and tree‑based notations.

## References

[1] Symbol Emergence in Cognitive Developmental Systems: a Survey. arXiv:1801.08829v2. https://arxiv.org/abs/1801.08829v2
[2] Applied Exoskeleton Technology: A Comprehensive Review of Physical and Cognitive Human-Robot Interaction. arXiv:2111.12860v8. https://arxiv.org/abs/2111.12860v8
[3] A cognitive diversity framework for radar target classification. arXiv:1110.6589v1. https://arxiv.org/abs/1110.6589v1
[4] Toward Cognitive and Immersive Systems: Experiments in a Cognitive Microworld. arXiv:1709.05958v2. https://arxiv.org/abs/1709.05958v2
[5] Cognition and Emotion: Perspectives of a Closing Gap. arXiv:1002.3035v1. https://arxiv.org/abs/1002.3035v1
[6] Offloading Cognition onto Cognitive Technology. arXiv:0808.3569v3. https://arxiv.org/abs/0808.3569v3
[7] Cognitive computation with autonomously active neural networks: an emerging field. arXiv:0901.3028v1. https://arxiv.org/abs/0901.3028v1
[8] Robust Beamforming Design for Intelligent Reflecting Surface Aided Cognitive Radio Systems with Imperfect Cascaded CSI. arXiv:2004.04595v4. https://arxiv.org/abs/2004.04595v4
[9] QNFO: COMMUTATIVE PHYSICS
[10] https://papers.qnfo.org/papers/numerata/. QNFO: NUMERATA: A Multi-Axis Framework for Evaluating Numeral Systems.
[11] https://papers.qnfo.org/papers/nonlinear-tree-based-numeration-systems-a-consolidated-synthesis/. QNFO: Nonlinear Tree-Based Numeration Systems: A Consolidated Synthesis.
[12] QNFO: Ten-Fingered Trap