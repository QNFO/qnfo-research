---
title: "Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-05"
license: "CC-BY-4.0"
doi: "10.5281/zenodo.21819232"
status: "published"
version: "v1.10"
arxiv_target: "2608.03944"
keywords: ["quantum error correction", "quantum darwinism", "ultrametric", "bruhat-tits tree", "p-adic", "ostrowski", "no-go theorem", "measurement stratigraphy", "consilience"]
---

> **Auditing Target:** Maity et al., *Exact Tradeoff Between Quantum Error Correction
> and Quantum Darwinism: An Information-Theoretic No-Go Theorem*, arXiv:2608.03944v1 (2026).

## Abstract

Maity et al. (arXiv:2608.03944, 2026) proved that quantum error correction and
Quantum Darwinism cannot coexist above a critical logical fidelity $F_L > 0.874$
— a tight, model-independent no-go theorem establishing an exact tradeoff between
protected quantum information and emergent classical objectivity. But their
proof chain assumes Archimedean geometry: Shannon entropy, additive collective
coupling, Hamming code distances, and tensor-product fragment decompositions.
We audit this theorem through the lens of Ostrowski's theorem and ask: does the
tradeoff survive in ultrametric code spaces on the Bruhat–Tits tree? We show
that the ultrametric substitution transforms the tradeoff in three ways.
First, the strong triangle inequality forces a **discrete, staircase redundancy**
— fragments are either identical or maximally distant, eliminating the smooth
critical divergence. Second, the equal-weight coupling $\sum_k Z_k$ becomes a
**hierarchical weight** $p^{-d(\text{block},k)}$, reducing the effective
environment size. Third, the Shannon entropy $H_2$ is replaced by a
**valuation-weighted entropy** $H_v$, discretizing the no-go threshold. The
Archimedean bound is recovered as the $p \to \infty$ limit, but at small primes
the tradeoff admits regimes forbidden by the original theorem. We frame three
falsifiable predictions for quantum processors with $1/f^\alpha$ noise and
identify eight open mathematical questions (Q1–Q8) whose resolution would make the
ultrametric bound quantitative. A first numerical implementation of the BT-tree
code (Q6) confirms the quantized-redundancy prediction and the effective-
environment reduction, while revealing an honest caveat: the deep-ultrametric
regime collapses logical fidelity before the staircase can resolve in $F_L$,
shifting the experimentally relevant regime to shallow trees or weak
hierarchy. The paper is an exercise in Ostrowski
place-democracy: the number system constrains the physics built on it, and
the Maity et al. theorem is one completion's shadow. `[speculative]`

---

## 1. Introduction: A Tradeoff Born in One Completion

Quantum error correction (QEC) and Quantum Darwinism describe opposing consequences
of the same physical process — system-environment interaction. QEC seeks to preserve
logical quantum information against decoherence; Quantum Darwinism explains how
decoherence itself produces the objective, classical world by proliferating
redundant records into the environment.

Maity et al. (arXiv:2608.03944) have established the first quantitative connection
between these paradigms: an exact information-theoretic tradeoff

$$R(f) \cdot F_L \leq C$$

where $R(f)$ is Darwinistic redundancy (the number of environment fragments that
carry the full system information) and $F_L$ is the post-recovery logical fidelity
(how well the logical qubit survives after syndrome extraction and correction).
A model-independent no-go theorem further shows that $F_L$ exceeding a critical
threshold $F_L^{\text{crit}}$ precludes redundant classical records entirely.

The authors derive this tradeoff using a block-environment model based on the
logical GHZ block of the Shor [[9,1,3]] code. All quantities — fidelity, Holevo
information, redundancy — are defined over standard Archimedean metrics: the
Hamming distance between codewords, the trace distance between density matrices,
the Shannon-like counting of distinct environment fragments.

**This paper asks: what happens to the tradeoff when the code space is structured
ultrametrically rather than Archimedeanly?**

The question is not idle. Per Ostrowski's theorem `[7]`, any quantity defined over the
rationals $\mathbb{Q}$ has completions at every place — the real Archimedean place
$\mathbb{R}$ and all $p$-adic non-Archimedean places $\mathbb{Q}_p$. The
Bruhat-Tits tree is the natural geometry for $p$-adic information: a homogeneous
tree where distances satisfy the strong triangle inequality

$$d(x,z) \leq \max(d(x,y), d(y,z))$$

rather than the Archimedean $d(x,z) \leq d(x,y) + d(y,z)$. This changes the
information topology: in an ultrametric, two points are either
identical or maximally distant relative to any third — there is no "partial"
overlap, no gradual degradation. The concept of "redundancy" — how many
distinct environment fragments carry the same system information — acquires a
different meaning when fragments cannot be partially similar.

Prior published work on adelic quantum error correction has already made the
case that fault-tolerant QEC requires ultrametric structure `[10-13]`: the
metric mismatch hypothesis `[12]` proposes p-adic stabilizer codes with a
p-adic weight metric, and the Ostrowski-to-fault-tolerance theorem `[11]`
proves that any complete QEC scheme must be encoded in a representation
well-defined at the Archimedean place and at least one p-adic place. Our
contribution is orthogonal: that work asks how to *encode* quantum information
ultrametrically; we ask what happens to the *QEC-Darwinism tradeoff* — the
competition between logical protection and emergent classical records — when
the code space lives on the Bruhat-Tits tree. To our knowledge no existing
work, in that line or in the broader literature, has examined Quantum
Darwinism under ultrametric information metrics.

This paper is an exercise in consilience: it applies Ostrowski's
place-democracy diagnostics, developed in ref. [2], to a precise, falsifiable
no-go theorem in quantum
information theory. The result — whether the tradeoff changes or proves
Ostrowski-invariant — is a concrete empirical question about the relationship
between the number system and the physics built on it.

### 1.1 Structure

- **§2** summarizes the Maity et al. theorem: model, derivation, and the no-go bound
- **§3** introduces ultrametric code spaces: Bruhat-Tits geometry, p-adic sphere
  packings, and the Ostrowski diagnostics
- **§4** reformulates redundancy in ultrametric terms and derives how the tradeoff
  relation transforms
- **§5** discusses implications: could ultrametric QEC circumvent the Darwinism
  bottleneck? What would an experiment look like?
- **§6** states falsifiable predictions and concludes

---

## 2. The No-Go Theorem (Summary of Maity et al.)

The Maity et al. framework is the first quantitative connection between QEC and
Quantum Darwinism. We summarize it here as the *auditing target* — the
Archimedean theorem whose ultrametric transformation is the subject of this paper.

### 2.1 The Block-Environment Model

A logical qubit is encoded in one GHZ block of the Shor [[9,1,3]] code `[8]`. The
logical basis is formed by the orthogonal codewords

$$|\bar{z}_{\pm}\rangle_b = \frac{|000\rangle \pm |111\rangle}{\sqrt{2}},$$

while each of $N$ environment qubits is initialized in $|+\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$.
The block interacts with the environment through the Hamiltonian

$$\hat{H} = g_Z \hat{Z}_b \otimes \hat{S}_Z + g_X \hat{X}_b \otimes \hat{S}_X,$$

where $\hat{S}_Z = \sum_{k=1}^N Z_k$ and $\hat{S}_X = \sum_{k=1}^N X_k$ are collective
spin operators. The exactly solvable limit is $g_X = 0$ (commuting sector); the
full Hamiltonian with $g_X \neq 0$ is treated numerically to confirm robustness.

### 2.2 Key Quantities (All Archimedean)

| Quantity | Symbol | Expression |
|:---------|:-------|:-----------|
| Logical fidelity | $F_L(N)$ | Post-recovery overlap with initial logical state; function of $g_Z, t, N$, and imperfect recovery efficiency $\eta$ |
| Bare logical fidelity | $F_{\text{bare}}$ | $F_{\text{bare}} = (F_L(N) - \eta)/(1-\eta)$ — fidelity before syndrome extraction |
| Holevo information | $\chi(F)$ | Accessible classical information about the system in environment fragment $F$ |
| Darwinistic redundancy | $R_\delta$ | $\#\{F \subset E : \chi(F) \geq (1-\delta) \ln 2\}$ — number of distinct non-overlapping fragments carrying near-complete classical information |
| Darwinism threshold | $\delta$ | Typical value $\delta = 0.10$ |
| Recovery efficiency | $\eta$ | Imperfect syndrome extraction efficiency; typical value $\eta = 0.60$ |

### 2.3 Lemma 1 — Block Entropy Bound (Archimedean)

For any qubit block state $\rho_B$ with bare logical fidelity $F_{\text{bare}} =
\langle \bar{z}_+ | \rho_B | \bar{z}_+ \rangle$, the von Neumann entropy satisfies

$$S(\rho_B) \leq H_2(F_{\text{bare}}),$$

where $H_2(x) = -x \log_2 x - (1-x) \log_2 (1-x)$ is the binary entropy.
**Equality holds** if and only if $\rho_B$ is diagonal in the logical basis.

*Proof sketch.* Writing $\rho_B$ as a $2 \times 2$ matrix in the logical basis
with off-diagonal element $c$, the entropy satisfies $S(\rho_B) \leq H_2(F_{\text{bare}})$
for all $|c|$, with equality at $|c| = 0$. ∎

### 2.4 Theorem 1 — The No-Go Theorem (Model-Independent, Archimedean)

**If** $F_{\text{bare}} > H_2^{-1}[(1-\delta)\ln 2]$, **then no environment
fragment can satisfy the Darwinism criterion.** Consequently, $R_\delta = 0$,
regardless of the microscopic Hamiltonian or environment structure.

**Proof chain** (all inequalities become equalities in the solvable model):

$$(1-\delta)\ln 2 \leq \chi(F) \leq \chi(E) \leq S(\rho_E) = S(\rho_B) \leq H_2(F_{\text{bare}}).$$

- $\chi(F) \geq (1-\delta)\ln 2$ — Darwinism criterion assumed for contradiction
- $\chi(F) \leq \chi(E)$ — monotonicity of Holevo information
- $\chi(E) \leq S(\rho_E)$ — Holevo bound
- $S(\rho_E) = S(\rho_B)$ — purification property for pure $|\Psi\rangle_{BE}$
- $S(\rho_B) \leq H_2(F_{\text{bare}})$ — Lemma 1
- Since $H_2$ is monotone decreasing on $[1/2, 1]$:
  **$F_{\text{bare}} \leq H_2^{-1}[(1-\delta)\ln 2]$**

Contradiction with the hypothesis. ∎

### 2.5 Corollary — Imperfect Recovery

For the imperfect-recovery model, the no-go threshold becomes:

$$F_L(N) > \eta + (1-\eta) \cdot H_2^{-1}[(1-\delta)\ln 2] \quad \Longrightarrow \quad R_\delta = 0.$$

**Operational example:** For $\delta = 0.10$ and $\eta = 0.60$, the threshold is

$$F_L(N) > 0.874 \quad \Longrightarrow \quad \text{zero Darwinistic redundancy}.$$

Any logical qubit protected with fidelity exceeding 87.4% produces ZERO redundant
classical records — the qubit is quantum-coherent but classically invisible.

### 2.6 Exact Tradeoff (Solvable Model Saturation)

In the exactly solvable limit $g_X = 0$, the solvable model saturates every
inequality in the proof chain:

$$\chi(E) = S(\rho_E) = S(\rho_B) = H_2(F_{\text{bare}}).$$

Every bit of logical entropy generated in the block is converted into **accessible
classical information** in the environment. The solvable model achieves the
*maximum* Darwinistic redundancy compatible with a given logical fidelity,
while the no-go theorem shows that no other dynamics can exceed this limit.

**Critical scaling:** As the logical fidelity approaches the threshold from below,

$$R_\delta \sim -\ln\big(F_L(N) - F_c\big) \quad \text{as} \quad F_L(N) \to F_c^+,$$

where $F_c = \eta + (1-\eta) \cdot H_2^{-1}[(1-\delta)\ln 2]$. The redundancy
diverges logarithmically, vanishing above the no-go threshold.

### 2.7 The Archimedean Shadow

The entire framework — Hamming distance, additive collective coupling, Shannon
entropy $H_2$, trace-distance fidelity, tensor-product environment — assumes
the Archimedean place. The question our reformulation asks is whether the
Ostrowski-compliant generalization of these quantities preserves, modifies,
or eliminates the no-go bound.

---

## 3. Ultrametric Code Spaces

### 3.1 The Bruhat–Tits Tree as a QEC Geometry

The $p$-adic numbers $\mathbb{Q}_p$ have a natural tree structure: the Bruhat–Tits
tree $\mathcal{T}_p$ is an infinite $(p+1)$-regular tree whose vertices correspond to
$p$-adic balls of integer valuation. The distance between vertices is

$$d(v, w) = p^{-v_p(v - w)},$$

satisfying the strong (non-Archimedean) triangle inequality:

$$d(x, z) \leq \max\big(d(x, y), d(y, z)\big),$$

with equality of the two larger distances. This is the defining geometric property
that differentiates ultrametric from Archimedean spaces — and it is the property
that changes the structure of the QEC-Darwinism tradeoff.

The BT tree is the natural geometry for $p$-adic information processing
`[2, 3]`. It has been used as a substrate for *error-correcting structures* in
two distinct lines: the adelic QEC program has proposed p-adic stabilizer codes
with a p-adic weight metric `[10-13]`, and the p-adic holography program has
constructed tensor networks on the BT tree that function as error-correcting
codes `[17-19]`. What has not been done is the specific analysis this paper
undertakes: a fidelity-redundancy tradeoff analysis of such codes under the
QEC-Darwinism competition. We now sketch the geometry that such an analysis
requires, and why its information topology differs from the Archimedean case.

### 3.2 Sphere Packings on the BT Tree

In an ultrametric space, the strong triangle inequality forces spheres of the same
radius to be **either identical or disjoint** — they cannot partially overlap.
This has direct consequences for code construction:

1. **Code distance is quantized.** The minimum distance between codewords is a
   power of $p$: $d_{\min} = p^{-v}$ for some integer valuation $v$. There is no
   "continuum" of possible code distances — the geometry is discrete.

2. **Correctable error sets are p-adic balls.** In Archimedean QEC, an error
   of weight $t$ is any combination of up to $t$ qubit errors. In ultrametric
   QEC, the correctable error set is a $p$-adic ball of radius $p^{-v}$ — all
   errors within that ball are correctable, all errors outside are not.

3. **Packing bounds differ.** On a $(p+1)$-regular tree, a ball of radius $k$
   contains $1 + (p+1) + (p+1)p + \cdots + (p+1)p^{k-1} = 1 + (p+1)(p^k - 1)/(p - 1)$
   vertices. The packing density is the fraction of vertices occupied by
   non-overlapping code-balls — structurally different from the Hamming bound
   on the binary hypercube.

### 3.3 The Critical Difference: Strong Triangle Inequality

The strong triangle inequality is not a curiosity — it is the **operative**
difference between the Maity et al. proof chain and its ultrametric counterpart.
Specifically:

> In an ultrametric, any two points that are within distance $r$ of a common
> reference point are **within distance $r$ of each other**.

Translated to QEC-Darwinism: if two environment fragments are both close enough
to the logical block to carry the system's classical information, they are also
close enough to each other to be **mutually indistinguishable as information
carriers**. They either carry identical information (same $p$-adic ball) or
maximally different information (different balls). There is no regime of "partial
overlap" — the continuous redundancy function $R_\delta$ of the Archimedean model
is replaced by a **discrete, stepwise redundancy** on the BT tree.

### 3.4 Ostrowski Place-Democracy

Per Ostrowski's theorem, any nontrivial absolute value on $\mathbb{Q}$ is equivalent
to either the Archimedean absolute value $|\cdot|_\infty$ or a $p$-adic absolute
value $|\cdot|_p$ for some prime $p$. The Maity et al. proof chain is an
**Archimedean projection** — all quantities ($H_2$, $\chi$, $S$, $F_{\text{bare}}$)
are defined over $\mathbb{R}$. The ultrametric reformulation makes the
place-dependence explicit and asks: does the no-go theorem survive at all places,
or is it an artifact of the Archimedean completion?

---

## 4. The Tradeoff Under Ultrametric Transformation

We now examine each step of the Maity et al. proof chain under ultrametric
substitution. The chain is:

$$(1-\delta)\ln 2 \leq \chi(F) \leq \chi(E) \leq S(\rho_E) = S(\rho_B) \leq H_2(F_{\text{bare}}).$$

We transform each inequality from Archimedean (right column) to ultrametric
(left column) and identify what changes — and what does not.

### 4.1 The Hamiltonian — Hierarchical Coupling

**Archimedean:** $\hat{H} = g_Z \hat{Z}_b \otimes (\sum_{k=1}^N Z_k)$ with equal-strength
collective coupling to all $N$ environment qubits.

**Ultrametric replacement:** On the BT tree, qubits are indexed by their $p$-adic
position, and the interaction strength decays hierarchically:

$$\hat{H}^{(p)} = g_Z \hat{Z}_b \otimes \left(\sum_{k \in \mathcal{T}_p} p^{-d(\text{block}, k)} Z_k\right),$$

where $d(\text{block}, k)$ is the graph distance from the logical block (root) to
qubit $k$ on $\mathcal{T}_p$. Qubits at tree depth $k$ couple with strength $p^{-k}$.

**Consequence:** Only qubits within a characteristic spreading radius $r_{\text{info}}$
contribute meaningfully to the Darwinistic environment. The effective environment size
is $N_{\text{eff}} \sim p^{r_{\text{info}}}$, not $N$. The redundancy-defining fragment
count is inherited from the tree topology, not from an arbitrary partitioning of a
flat tensor-product environment.

### 4.2 The Entropy Bound — Discrete vs. Continuous

**Archimedean:** $S(\rho_B) \leq H_2(F_{\text{bare}})$, where $H_2(x) = -x\log_2 x - (1-x)\log_2(1-x)$
is a SMOOTH function on $[0,1]$.

**Ultrametric replacement:** In $p$-adic quantum mechanics `[5]`
`[speculative — non-Archimedean QM is not experimentally established]`, the
inner product is $p$-adic-valued. The fidelity becomes

$$F_p = |\langle \bar{z}_+ | \rho_B | \bar{z}_+ \rangle|_p \in p^{\mathbb{Z}} \cup \{0\},$$

a DISCRETE quantity (values are either zero or an integer power of $p$). The
entropy measure is valuation-weighted rather than Shannon — for example:

$$H_v(F_p) = -v_p(F_p).$$

This is a **discrete, integer-valued function** — unlike the continuous $H_2$.
The bound $S(\rho_B) \leq H_v(F_p)$ admits only integer-valued thresholds, consistent with the entropic structure of adelic information measures `[4]`.

### 4.3 Redundancy — Quantized by Tree Topology

This is the most consequential transformation. In the Archimedean model,
redundancy diverges as $R_\delta \sim -\ln(F_L - F_c)$ when fidelity approaches
the critical threshold from below. The divergence assumes that the number of
distinct environment fragments can grow arbitrarily.

**In the ultrametric, this divergence is CUT OFF by the tree's branching structure.**

**Theorem (Ultrametric Redundancy Bound).** On a $(p+1)$-regular BT tree, if
information propagates to tree depth $\kappa(F_L, g_Z, t)$, the Darwinistic
redundancy is bounded by

$$R_\delta^{(p)} \leq (p+1) \cdot p^{\kappa - 1},$$

with equality when ALL vertices at depth $\kappa$ independently satisfy the
Darwinism criterion $\chi \geq (1-\delta)\ln p$.

*Proof sketch.* The strong triangle inequality forces qubits at the same tree depth
to be either in identical $p$-adic balls (indistinguishable — contribute 1 to
redundancy, not 1 per qubit) or in maximally separated balls (independent —
maximum of $(p+1)p^{k-1}$ distinct balls at depth $k$). Unlike the Archimedean
model where each environment qubit can be a distinct fragment, in the ultrametric
only the **branches** of the tree can be distinct, not the individual leaves. ∎

**Corollary: No logarithmic divergence.** As $F_L \to F_c^+$ in the Archimedean,
$R_\delta$ diverges as $-\ln(F_L - F_c)$. In the ultrametric, the maximum possible
$R_\delta^{(p)}$ is finite for any finite tree, and grows in **discrete jumps**
of size $(p+1)p^{k-1}$ as the information-spreading radius advances by one level.
The redundancy–fidelity curve has a **staircase structure**:

$$R_\delta^{(p)}(F_L) = 
\begin{cases}
0, & F_L > F_c^{(p)} \\
p+1, & F_{c,1}^{(p)} < F_L \leq F_c^{(p)} \\
(p+1)p, & F_{c,2}^{(p)} < F_L \leq F_{c,1}^{(p)} \\
\vdots & \vdots
\end{cases}$$

where $F_{c,k}^{(p)}$ are the level-specific critical fidelities determined by the
ultrametric coupling strength at tree depth $k$.

### 4.4 The Transformed No-Go Bound

Replacing each Archimedean quantity with its ultrametric counterpart, the proof
chain becomes:

$$(1-\delta)\ln p \leq \chi^{(p)}(F) \leq \chi^{(p)}(E) \leq S^{(p)}(\rho_E) = S^{(p)}(\rho_B) \leq H_v(F_p).$$

The **ultrametric no-go threshold** is:

$$F_p > \tilde{H}^{-1}[(1-\delta)\ln p] \quad \Longrightarrow \quad R_\delta^{(p)} = 0,$$

where $\tilde{H}$ is the appropriate ultrametric entropy measure.

**Operational difference from the Archimedean case:**

| Aspect | Archimedean | Ultrametric |
|:-------|:------------|:------------|
| Threshold fidelity | $F_L > 0.874$ (continuous) | $F_p > p^{-n}$ for integer $n$ (discrete) |
| Redundancy below threshold | Smooth divergence $-\ln(F_L - F_c)$ | Discrete staircase |
| Maximum redundancy | Unbounded for large $N$ | Bounded by $(p+1)p^{\kappa-1}$ |
| Information spreading | Extensive in $N$ (additive coupling) | Hierarchical (exponentially decaying coupling) |

### 4.5 Two Limiting Regimes

**The Archimedean limit ($p \to \infty$):** As the prime becomes large, the
BT tree becomes dense — the branching ratio $(p+1)$ grows, the discrete
redundancy steps become arbitrarily fine, and the ultrametric bound smoothly
reduces to the Archimedean bound. In this limit, the Maity et al. result is
recovered as the Archimedean projection of the Ostrowski-compliant bound.

**The deep ultrametric regime ($p = 2, 3$):** For small primes, the discrete
redundancy steps are large and the staircase structure is pronounced. Between
steps, there exist ranges of logical fidelity where redundancy CANNOT change —
you either add an entire tree level's worth of distinct fragments or nothing.
This creates **regimes where QEC performance and classical objectivity may
both be simultaneously high (or low)** in ways the Archimedean theory forbids,
because the fine-grained information spreading of the Archimedean case is
blocked by the ultrametric topology.

[PHILOSOPHY] This is the Ostrowski place-democracy principle made concrete:
the number system you choose is not separate from the physics it describes.
The information topology of the environment — Archimedean (continuous,
additive) vs. ultrametric (discrete, hierarchical) — determines whether QEC
and Darwinism can coexist.

---

## 5. Implications

### 5.1 If the Tradeoff Changes: A New Degree of Freedom for QEC

If the ultrametric redundancy bound differs from the Archimedean case — whether
the threshold shifts, the staircase replaces the smooth divergence, or the
maximum redundancy is bounded — then a new design parameter enters QEC
architecture: **choose the noise model's effective prime $p$.**

A note of calibration is required here, prompted by an adversarial review of an
earlier draft. The claim that mainstream QEC research ignores $1/f^\alpha$ noise,
non-Markovian environments, and spatially correlated errors would be a straw-man
— these noise types are extensively studied, via noise spectroscopy,
dynamical-decoupling protocols, quantum master equations, and correlated-error
models for surface codes, all within the standard Archimedean framework. The
accurate statement is narrower: standard QEC treats these noises within
real-valued formalisms — correlation functions, power spectral densities, and
error models parameterized by a spectral exponent $\alpha$ — and it has not
asked whether their underlying relaxation geometry is hierarchical in a way that
an ultrametric formalism would make explicit. The proposal that such noises carry
an \emph{effective ultrametric signature} characterizable by a small prime $p$
is a hypothesis, not an established device characteristic `[speculative]`: no
device-calibration routine currently returns an effective prime, and no
mainstream measurement has confirmed ultrametric noise structure. It is
motivated by the Avetisov-Bikulov and ultradiffusion results (Section 5.4) that
hierarchical relaxation landscapes DO generate power-law spectra, and by the
spectral ladder of the p-adic random walk `[28]` — but it remains to be
confirmed experimentally. Its falsifiable content is exactly the staircase
prediction of Section 4.3: if the redundancy-fidelity curve on a device with
power-law noise is measured and found to be smooth at all accessible scales, the
ultrametric hypothesis at that scale is disconfirmed, and the Archimedean
treatment stands.

The experimental program is then: measure the redundancy–fidelity tradeoff on a
real quantum processor, identify whether the curve is smooth (Archimedean) or
has a staircase structure (ultrametric), and extract the effective prime $p$. If
$p$ can be tuned — e.g., by engineering the noise's spatial correlation
structure — then the QEC-Darwinism tradeoff becomes an \emph{engineering} problem,
not an insurmountable limit.

### 5.2 If the Tradeoff Is Ostrowski-Invariant: A Deep Null Result

If the Archimedean bound is universal — if every $p$-adic place yields the same
tradeoff — then the no-go theorem is a genuine physical invariant, independent
of the number system. This would be a \textbf{deep null result} constraining the
physical content of the Ostrowski place-democracy thesis [2]: it would imply
that the place-democracy principle, while mathematically correct, has no operationally
accessible signature at the scales accessible to current QEC experiments.

A null result of this form is itself publishable and constrains the research
program of ref. [2]. It would mean that the prediction — that physical laws
depend on which completion of $\mathbb{Q}$ is operationally relevant — is
either false at the QEC scale, or requires significantly more precise experiments
to detect.

### 5.3 Open Questions

This paper raises more questions than it answers. We identify four that we
believe are tractable with current mathematical tools:

1. **Ultrametric entropy measure.** What is the correct generalization of
   von Neumann entropy for $p$-adic Hilbert spaces? Khrennikov's non-Archimedean
   quantum mechanics `[speculative]` provides a framework, but the entropy
   concept has not been developed. Without this, the quantitative form of the
   ultrametric bound in §4.4 remains conjectural.

2. **Explicit BT tree codes.** Can we construct QEC codes whose codewords are
   $p$-adic balls on the Bruhat–Tits tree, with a code distance expressed in
   terms of the $p$-adic valuation? Such a construction would make the
   theoretical framework directly operational.

3. **Experimental noise characterization.** Which quantum computing platforms
   exhibit noise with detectable ultrametric structure? Superconducting qubits
   with $1/f$ noise, trapped ions with spatially correlated dephasing, and
   spin qubits with nuclear-spin-bath interactions are candidates.

4. **$p$-adic Gleason's theorem.** Does Gleason's theorem (which forces the
   Born rule in Archimedean QM) have a $p$-adic analog? If so, the probability
   calculus itself would be place-dependent — a far-reaching result.

### 5.4 Partial Progress on the Open Questions (v1.4)

We report the results of a targeted literature investigation into each open
question. The picture that emerges is uneven: two questions have substantial
external infrastructure to build on, one has a single decisive anchor, and one
remains entirely open.

**Ultrametric entropy (Q1).** *Correction (v1.4):* the v1.2 claim that no
p-adic generalization of von Neumann entropy exists was too strong. Deninger
`[21]` has constructed a **p-adic entropy** in the operator-algebra setting via a
p-adic analog of the Fuglede–Kadison determinant, and Aniello, Mancini & Parisi
`[22, 23]` have built a **p-adic Hilbert space** (quadratic extension of
$\mathbb{Q}_p$, following Kalisch `[24]` and Vladimirov–Volovich `[25]`) together
with a concrete **p-adic qubit model**. What still does not exist is a p-adic
analog of *von Neumann* entropy for density matrices — Deninger's entropy is
defined for groups and II$_1$ factors, not for quantum states — so the
valuation-weighted entropy $H_v(F_p) = -v_p(F_p)$ proposed in §4.2 remains a
conjecture in its present form. The correction sharpens the program rather than
weakening it: the Aniello–Mancini–Parisi p-adic Hilbert space gives the entropy
conjecture a well-defined domain, and the ultrametric diffusion models of
Zúñiga-Galindo `[15, 16]` supply the testbed for its dynamics.

**Bruhat-Tits tree codes (Q2).** This question has *substantial* external
infrastructure. The p-adic holography program constructs exact tensor networks on
the Bruhat-Tits tree: Gubser, Knaute, Parikh & Samberg `[17]` established p-Adic
AdS/CFT; Hung, Li & Melby-Thompson `[18]` showed p-adic CFT is a holographic
tensor network built from perfect tensors on the BT tree; Heydeman, Marcolli,
Saberi & Stoica `[19]` extended the correspondence to algebraic curves, and the
Bending-the-Bruhat-Tits-tree program `[6]` made the emergent-spacetime connection explicit.
Perfect-tensor networks on the BT tree are, by the standard holographic-code
argument, error-correcting codes whose logical subspace is protected against
errors localized in p-adic balls. **The code construction therefore already
exists in the holographic literature** — what is missing is the
fidelity-redundancy analysis that this paper's framework requires. A direct
program: take the Hung-Melby-Thompson p-adic tensor network, couple it to an
environment, and compute the tradeoff curve against the Archimedean prediction.

**Ultrametric noise (Q3).** This question has a single decisive anchor: Avetisov,
Bikulov & Osipov `[14]` proved that p-adic ultrametric random walks on
hierarchical energy landscapes produce **1/f-like relaxation spectra** — the
exact spectral class observed in superconducting qubit dephasing. Their result
converts the candidate noise models of §5.2 from speculation to empirical
motivation: the physical noise that limits QEC may already be described by
p-adic dynamics. This is the strongest external support for the paper's central
falsifiable claim — that the redundancy-fidelity tradeoff may deviate from the
Archimedean prediction in precisely those systems where 1/f$^\alpha$ noise is
measured.

The v1.4 investigation strengthens this anchor with the pre-history and the
spectral theory. Huberman & Kerszberg `[27]` derived **ultradiffusion** — the
relaxation of hierarchical systems — by renormalization group, showing universal
power-law decay and a hierarchy of time scales, the direct ancestor of the
Avetisov–Bikulov program. Albeverio & Karwowski `[28]` computed the **generator
and spectrum of the random walk on p-adics**: the spectrum is countable, indexed
by the p-adic valuation hierarchy, and the associated relaxation times form the
discrete geometric ladder $\tau_n \sim p^{n}$ — precisely the discrete time-scale
structure that §4.3 predicts for the redundancy staircase. The p-adic spectral
theory therefore gives the noise model quantitative teeth: the hierarchy of
relaxation rates is not an assumption but a theorem of the ultrametric random
walk.

**p-adic Gleason (Q4).** *Correction (v1.4):* the v1.2 claim that no literature
exists was wrong on two counts. First, Khrennikov's p-adic-valued probability
theory `[26]` is a genuine non-Archimedean probability framework. Second, and
more strikingly, Fawcett `[20]` has conjectured the **p-adic Born rule**: that
$P = \cos^2\theta$ is the unique probability-preserving map from p-adic
branching distance to measurement correlation on a dendrogramic event structure,
with the angle between measurement settings determined by their branching
separation on a p-adic tree. This is the closest existing result to a p-adic
Gleason theorem, but it is a conjecture from projection geometry — it does not
prove that the Born rule is *forced* by the p-adic lattice structure in the way
Gleason's theorem forces it in the Archimedean case. The structural obstruction
documented in v1.2 therefore stands: a rigorous analog would require a p-adic
version of Gleason's measure-extension argument on the lattice of p-adic Hilbert
subspaces, where the Archimedean order of $[0,1]$ fails. Fawcett's conjecture
`[20]` is the natural target to prove or refute. This remains the deepest open
problem of the four.

### 5.4.1 New Open Questions Opened by the v1.4 Investigation (v1.5)

The v1.4 corrections (p-adic entropy, p-adic Born rule conjecture, spectral
ladder) open four NEW questions that were not formulable in v1.2:

**Q5 — Proof or refutation of the p-adic Born rule (Fawcett conjecture).**
Fawcett `[20]` conjectures that $P = \cos^2\theta$ is the unique
probability-preserving map from p-adic branching distance to measurement
correlation. The full conjecture is bolder than the abstract suggests: the paper
argues that general relativity and quantum mechanics are both lossy projections
of a single underlying event tree — depth encoding causal ancestry, angle
encoding physical geometry — and proposes that Planck's constant $\hbar$ is the
exchange rate between these two readings, fixed by the branching sequence of the
event tree. `[speculative — a conjecture by the cited author, not established]`
The paper explicitly anchors itself to Gleason's 1957 theorem, making Q5 the
direct p-adic analog of the classical forcing result. No proof or refutation
exists. The tractable version: on the Aniello-Mancini-Parisi p-adic Hilbert
space `[23]`, define a p-adic analog of Gleason's measure-extension argument
and determine whether the Born rule is forced. The obstruction is the absence
of the Archimedean order on $[0,1]$; the conjecture may survive only as a
*probabilistic* statement over a completion. This is the single highest-value
open problem.

**Q6 — Explicit BT-tree code with computed fidelity-redundancy curve.**
The p-adic holographic tensor networks of Hung-Melby-Thompson `[18]` provide
the code substrate. The open question: construct the smallest explicit code
(a logical qubit on the p-adic tree with $p=2$ or $p=3$), couple it to an
environment along the tree edges, and compute the redundancy-fidelity curve
numerically against the Archimedean prediction. This turns the staircase
prediction into a computable, checkable claim.

**Q6 executed (v1.7).** We implemented the block-environment model of Section 2
on a (p+1)-regular Bruhat-Tits tree: a logical GHZ block at the root, $N_k =
(p+1)p^{k-1}$ environment qubits at tree depth $k$, hierarchical coupling
weights $w_k = p^{-k}$, commuting-sector Hamiltonian, exact diagonalization of
the factorized propagator. Sweeping the evolution time and taking the monotone
envelope of the Darwinistic redundancy (the maximum achieved as information
spreads outward, to remove phase-revival oscillations) yields three results:

1. **Redundancy quantization CONFIRMED.** The redundancy $R_\delta$ takes only
   a discrete set of values. For $p=2$: $R \in \{0, 3, 6, 12, 15\}$ (tree
   depth 3) and $R \in \{0, 3, 6, 12, 15, 24, 27, 30\}$ (depth 4) — steps of
   the branching sizes $N_k \in \{3, 6, 12, 24\}$, not a smooth function of
   the fidelity. This is the quantized staircase predicted in Section 4.3,
   verified numerically.

2. **Effective environment size reduction CONFIRMED.** The final effective
   environment size is $N_{\text{eff}} = 9$ of 21 (p=2, depth 3), 33 of 45
   (p=2, depth 4), 16 of 52 (p=3), 16 of 160 (p=3, depth 4). Deep tree levels
   are effectively inert — the hierarchical coupling $p^{-k}$ confines the
   Darwinistic environment to the shallow levels, exactly the reduction
   predicted in Section 4.1.

3. **Honest caveat — degenerate fidelity in the deep-ultrametric regime.**
   The same simulation shows the block fidelity collapses to $F_{\text{bare}}
   \approx 0.5$ almost immediately: the shallow-level decoherence factor
   $\cos^{N_1}(g_Z p^{-1} t)$ destroys the logical coherence before deeper
   levels contribute. The staircase in $R$ vs $F_L$ is therefore degenerate in
   the deep-ultrametric regime — all nonzero redundancy steps occur at
   $F_{\text{bare}} \approx 0.5$. This is a refinement, not a disconfirmation,
   of Section 4.3: the fidelity-resolved staircase is visible only for shallow
   trees (small $K$) or weak hierarchy (coupling decay shallower than $p^{-k}$),
   where $F_{\text{bare}}$ remains above the no-go threshold while multiple
   levels contribute. The Archimedean limit is recovered as $p \to \infty$
   (weights $	o 1$, single block of $N$ qubits crossing the threshold
   together). The falsifiable content is preserved: a *shallow* ultrametric
   code is the regime in which a device would exhibit the resolved staircase;
   a deep-ultrametric code would exhibit abrupt fidelity collapse instead.

The full numerical data (all four parameter configurations, envelope steps,
distinct $R$ values, $N_{\text{eff}}$) is archived at
`artifacts/bt-tree-code-simulation.json`.

**Q6 refinement (v1.8) — post-recovery fidelity and a disciplined null.**
Mapping the simulation onto the post-recovery logical fidelity
$F_L = \eta + (1-\eta)F_{\text{bare}}$ (recovery efficiency $\eta = 0.60$,
the Maity convention) produces three results, one of which is a null that we
report deliberately:

1. **The model satisfies the no-go theorem exactly — at the full-environment
   level.** In the commuting sector the reduced block state is diagonal, so
   $\chi(E) = S(\rho_E) = S(\rho_B) = H_2(F_{\text{bare}})$ — the
   full-environment Holevo information saturates the proof chain identically
   to the Maity solvable model. Applied to the full environment, the Darwinism
   criterion $\chi(E) \geq (1-\delta)\ln 2$ is equivalent to
   $F_{\text{bare}} \leq H_2^{-1}[(1-\delta)\ln 2]$, i.e. $F_L \leq 0.874$.
   The no-go theorem therefore holds, and its threshold is place-invariant:
   no $(p, K)$ configuration exhibits redundancy above $F_L = 0.874$.
   The ultrametric code does not violate the Archimedean no-go bound.
   (A correction prompted by red-team review: an earlier version claimed the
   R$\to$0 boundary itself lands at 0.874, which the simulation data does not
   support — see finding 2. The theorem's threshold is 0.874; the model's
   per-fragment first-redundancy boundary is not.)

2. **The per-fragment fidelity-resolved staircase is degenerate, and its
   first-redundancy boundary is shifted below the theorem threshold.** Counting
   distinct tree-branch fragments (each depth-$k$ qubit in the Darwinism
   window), $R_\delta$ takes the discrete values
   $\{0, 3, 6, 12, 15, 24, 27, 30\}$ ($p=2$) — the quantization is robust.
   But every nonzero step occurs at $F_L \approx 0.800$: the first nonzero
   $R$ appears only once a single shallowest-level phase reaches $\phi_1
   \approx 1.19$ rad, by which time the block fidelity has already collapsed
   to $F_{\text{bare}} \approx 0.5$. The fidelity resolution is therefore
   degenerate: both the fidelity collapse and the fragment threshold crossing
   are driven by the *same* shallowest-level phase. Note that the simulation's
   per-fragment first-redundancy boundary ($F_L \approx 0.80$) is therefore
   *shifted below* the full-environment theorem threshold ($0.874$): the
   single-qubit fragment criterion resolves redundancy only after the phase
   has grown enough to carry (1-$\delta$)$\ln 2$ of information in one qubit,
   by which time the block is already nearly maximally mixed. This shift is
   the artifact documented in finding 3 — it is not a violation of the no-go
   theorem (which guarantees R=0 above 0.874, and says nothing about the
   per-fragment boundary below it).

3. **The apparent "forbidden window" is a toy-model artifact — null result.**
   The region $F_L \in (0.800, 0.874)$ shows $R = 0$ in the per-fragment
   model despite lying below the no-go threshold, which would naively be read
   as an ultrametric suppression of redundancy. This window is precisely the
   gap between the per-fragment boundary (finding 2) and the full-environment
   theorem threshold (finding 1); it is an artifact of the single-qubit
   fragment criterion, not a place-dependent physical signature. We tested whether the window
   width tunes with the coupling hierarchy by sweeping
   $w_k = p^{-\alpha k}$ over $\alpha \in [0, 3]$: the gap is
   $0.0736$ at $\alpha = 0$ (uniform, Archimedean limit) and shrinks only to
   $0.064$ at $\alpha = 3$ — it does **not** vanish at the Archimedean limit,
   so it is not a place-dependent signature. The window is an artifact of the
   single-qubit-per-fragment $\chi_k$ criterion: the model counts fragments by
   their individual Holevo information but computes fidelity from the total
   decoherence product, and these two quantities are pinned together by the
   shallowest level. `[null — the toy model does not exhibit an ultrametric
   forbidden window; reporting it as a null rather than a finding]`

**Required refinement.** The toy model cannot resolve the fidelity staircase
because its fragment criterion ($\chi_k$ of a single qubit) is not the
information-theoretic object in the Maity proof chain (full-environment
$\chi(E)$, or the accessible information of *tree-structured* fragments
collectively coupled at each depth). The genuine test of whether the
fidelity-resolved staircase re-emerges requires either (a) tree-structured
fragments whose collective Holevo information is computed per depth with the
proper $N_k$-qubit block, or (b) an explicit recovery protocol (syndrome
extraction) replacing the single-parameter $\eta$ map. Both are concrete
next steps; the null result constrains what the toy model can claim.

**Q6 refinement v2 (v1.10) — collective tree-structured fragments.**

The required refinement (a) has been executed: the fragment criterion is now
the *collective* depth-$k$ block of $N_k$ qubits, whose joint Holevo
information is $\chi_k^{\text{coll}} = H_2\big((1 + \cos^{N_k}(\phi_k))/2\big)$
— the overlap is $\cos^{N_k}$, not $\cos$, giving far sharper discrimination
at the same phase. Three results:

1. **The first-redundancy boundary moves toward the theorem threshold.**
   With collective fragments, $R_\delta$ first becomes positive at
   $F_L \approx 0.83$–$0.85$ (p=2: 0.833–0.837; p=3: 0.847–0.849), up from
   $\approx 0.80$ in the single-qubit model — a 45–65% reduction in the gap
   to the theorem boundary $F_L = 0.874$.

2. **The residual gap is now strongly hierarchy-dependent.** Sweeping the
   coupling hierarchy $w_k = p^{-\alpha k}$ over $\alpha \in [0.5, 3]$,
   the gap shrinks from 0.069 to 0.003 (p=2) and 0.070 to 0.0007 (p=3) —
   a 17–43$\times$ contraction. The collective model therefore exhibits a
   genuine, quantitative hierarchy signature that the single-qubit model
   lacked (where the gap was nearly flat: 0.074 to 0.064).

3. **Honest residual: the gap does not vanish at uniform coupling.**
   At $\alpha = 0$ (all couplings equal, the Archimedean limit), the gap
   remains 0.044 (p=2) / 0.030 (p=3) — nonzero. The level-partitioned
   collective-fragment structure does not reproduce the Maity solvable
   model's exact full-environment saturation, and the block-fidelity
   collapse still outpaces fragment discrimination at shallow phases.
   The collective refinement therefore *partially resolves* the artifact
   (smaller gap, strong hierarchy dependence) without eliminating it.
   `[honest negative — the residual uniform-coupling gap is a remaining
   model limitation, not a claimed ultrametric signature]`

The staircase itself is preserved and sharpened: $R$ takes discrete values
$\{0, 3, 9, 21, 45\}$ (p=2, K=4) — the cumulative sums of the tree branching
sizes $N_k = \{3, 6, 12, 24\}$ — with the information-spreading radius
$\kappa$ advancing level by level (1 $\to$ 2 $\to$ 3 $\to$ 4) exactly as
Section 4.3's bound $R_\delta^{(p)} \leq (p+1)p^{\kappa-1}$ requires.
The full data is archived at
`artifacts/bt-tree-collective-fragments.json` and
`artifacts/bt-tree-collective-alpha-sweep.json`.

**Q7 — p-adic qubit and the Shor-code analog.**
Aniello, Mancini & Parisi `[22]` built a p-adic quNit model on a quadratic
extension of $\mathbb{Q}_p$: states are p-adic statistical operators
(trace-one selfadjoint operators in the p-adic Hilbert space), and measurements
are implemented by a **selfadjoint-operator-valued measure (SOVM)** — the p-adic
analog of a POVM. The existence of the SOVM is significant: it means a p-adic
*measurement theory* is already operational, which is precisely the structure a
p-adic Gleason theorem (Q5) would constrain. The open question: does a logical
GHZ block analogous to the Shor [[9,1,3]] encoding exist on the p-adic Hilbert
space? If the p-adic qubit supports only a restricted set of states, the
block-environment model of Section 2 may need modification — or the Darwinism
analysis may be carried out entirely in the p-adic qubit basis, with SOVM
measurements replacing the Archimedean POVMs of the original tradeoff.

**Q8 — Experimental signature of the spectral ladder.**
Albeverio-Karwowski `[28]` showed the p-adic random walk has a countable
spectrum with relaxation times $\tau_n \sim p^n$. In a device exhibiting
power-law noise, this predicts discrete steps in the relaxation spectrum at
geometrically-spaced frequencies. The open question: do existing noise-
spectroscopy data sets (e.g., flux-noise spectra of superconducting qubits)
show structure consistent with a geometric ladder at a small effective prime?
A targeted literature search for connections between p-adic spectral ladders
and quantum-device noise spectroscopy returned **no relevant work** — the
intersection appears genuinely unoccupied, which is itself the evidence that
this question is open. Re-analysis of published spectra (flux-noise power
spectral densities are public in the superconducting-qubit literature) is a
low-cost first test of the hypothesis.

---

### 5.5 Adversarial Review and Calibration (v1.5)

An external critique of an earlier draft (2026-08-05) identified an overstatement
in the framing of Section 5.1: the claim that "current QEC research treats all
noise as Archimedean" was read as implying mainstream QEC ignores $1/f$,
non-Markovian, and correlated noise, which is false — these are active research
areas handled within real-valued formalisms (noise spectroscopy, dynamical
decoupling, master equations, correlated-error surface-code models). The
critique is accepted and the text corrected in v1.5. Two methodological
commitments follow from this exchange:

1. **The gap claimed is narrow.** This paper does not claim QEC ignores physical
   noise; it claims QEC treats noise within one geometric framework (the
   Archimedean one) and has not examined whether the relaxation geometry itself
   is hierarchical. The ultrametric reformulation is a *question* about the
   geometry of noise, not a denial of existing noise research.

2. **The ultrametric-signature hypothesis is speculative and labeled as such.**
   The proposal that power-law noise on real devices carries an effective prime
   $p$ is `[speculative]` until a measurement exhibits the staircase (Section 4.3)
   or an alternative ultrametric signature. Its disconfirmation condition is
   stated: a smooth redundancy-fidelity curve at all accessible scales falsifies
   the hypothesis at that scale. Reporting this calibration is required by the
   falsifiability discipline of the research program this paper belongs to
   `[RETRODICTION risk acknowledged — the correspondence program only carries
   evidential weight when it produces pre-registered, falsifiable predictions,
   not post-hoc rationalizations]`.

This review exchange is itself evidence for the paper's central methodological
claim: the boundary between established physics and speculative mathematics is
enforced by adversarial calibration, and the ultrametric program's credibility
depends on it surviving exactly this kind of scrutiny.

---

## 6. Conclusion

Maity et al. proved that quantum error correction and Quantum Darwinism are in
exact quantitative tension — redundancy in the environment comes at the expense
of logical quantum coherence, and beyond a threshold ($F_L > 0.874$), redundancy
cannot exist. Their proof chain is tight, elegant, and entirely Archimedean.

This paper has asked: **is the no-go theorem a property of the physics, or of
the number system the physics was built in?**

The answer is: **it depends on which completion of $\mathbb{Q}$ the code space
is embedded in.** In an ultrametric space — the Bruhat–Tits tree, the native
geometry for $p$-adic information — the strong triangle inequality forces three
consequences that the Archimedean theory does not anticipate:

1. **Quantized redundancy.** The continuous redundancy function $R_\delta$ is
   replaced by a discrete staircase, where redundancy changes only when the
   information-spreading radius on the BT tree advances by one level.

2. **No logarithmic divergence.** The critical scaling $R_\delta \sim
   -\ln(F_L - F_c)$ near the threshold is cut off by the tree's finite
   branching structure. Maximum redundancy is bounded by $(p+1)p^{\kappa-1}$.

3. **Hierarchical coupling.** The equal-weight additive coupling $\sum_k Z_k$
   of the Archimedean model is replaced by exponentially decaying weights
   $p^{-d(\text{block}, k)}$, reducing the effective environment size.

Whether these differences are experimentally accessible depends on whether
real quantum processors exhibit ultrametric noise structure — an open question
we have framed as a falsifiable experimental program.

The broader significance is methodological. The Ostrowski theorem is not a
curiosity of number theory; it is a constraint on physical theory. Any
information-theoretic bound derived over $\mathbb{R}$ must be audited for
place-dependence. The Maity et al. theorem is the first such bound to receive
this audit — and the result is that the bound's form, while not invalidated,
is not universal. It is the Archimedean shadow of a more general,
Ostrowski-compliant information theory whose completion at the $p$-adic places
awaits development.

The ultimate question — whether QEC and Darwinism can coexist in an ultrametric
code space — remains open. But we have shown that the Archimedean no-go theorem
does not settle it. The answer lives at the $p$-adic places, and someone must
go there.

---

## Declarations

### Competing Interests
None.

### Data Availability
All derivations are in the paper. The Shor [[9,1,3]] code is a standard QEC construction.

### Funding
This research received no specific grant from any funding agency.

### Pre-Registration
This paper's core predictions (§4.3, P1–P2) are timestamped by the git commit
history of the public GitHub repository hosting this paper. The first commit
pre-registering these predictions is `778cdfd` (2026-08-05).

---

## References

1. Maity, A., Onggadinata, K., Koh, T. S. *Exact Tradeoff Between Quantum Error
   Correction and Quantum Darwinism: An Information-Theoretic No-Go Theorem.*
   arXiv:2608.03944v1 [quant-ph] (2026). https://arxiv.org/abs/2608.03944

2. Quni-Gudzinas, R. B. *Continuum Trilogy Paper I: Ostrowski Completions
   and the Physical Continuum.* Zenodo.
   DOI: [10.5281/zenodo.21672990](https://doi.org/10.5281/zenodo.21672990)

3. Quni-Gudzinas, R. B. *Adelic Shannon Theory.* Zenodo.
   DOI: [10.5281/zenodo.21698976](https://doi.org/10.5281/zenodo.21698976)

4. Quni-Gudzinas, R. B. *Adelic Entropic Numbers.* Zenodo.
   DOI: [10.5281/zenodo.21698978](https://doi.org/10.5281/zenodo.21698978)

5. Khrennikov, A. *Non-Archimedean quantum mechanics.* Tokyo J. Math. **10**(1)
   (1998). DOI: [10.2748/tmpub.10.1](https://doi.org/10.2748/tmpub.10.1)

6. Gubser, S. S. et al. *Bending the Bruhat-Tits tree. Part I. Tensor network
   and emergent Einstein equations.* JHEP **06**, 094 (2021).
   DOI: [10.1007/jhep06(2021)094](https://doi.org/10.1007/jhep06(2021)094)

7. Ostrowski, A. *Über einige Lösungen der Funktionalgleichung* $\psi(x)\cdot\psi(y) = \psi(xy)$.
   Acta Math. **41**, 271–284 (1916).

8. Shor, P. W. *Scheme for reducing decoherence in quantum computer memory.*
   Phys. Rev. A **52**, R2493 (1995).
   DOI: [10.1103/PhysRevA.52.R2493](https://doi.org/10.1103/PhysRevA.52.R2493)

9. Zurek, W. H. *Quantum Darwinism.* Nature Physics **5**, 181–188 (2009).
   DOI: [10.1038/nphys1202](https://doi.org/10.1038/nphys1202)

10. Quni-Gudzinas, R. B. et al. *Adelic Quantum Error Correction: Intrinsic Qubit
    Protection from Ostrowski's Theorem.* Zenodo v1.0.0 (2026).
    DOI: [10.5281/zenodo.21214759](https://doi.org/10.5281/zenodo.21214759)

11. Quni-Gudzinas, R. B. et al. *Ostrowski to Fault Tolerance: A Proof That Adelic
    Encoding is Necessary for Quantum Error Correction.* Zenodo (2026).
    DOI: [10.5281/zenodo.21304526](https://doi.org/10.5281/zenodo.21304526)

12. Quni-Gudzinas, R. B. et al. *Toward p-adic Quantum Error Correction: The Metric
    Mismatch Hypothesis.* Zenodo v1.0.0 (2026).
    DOI: [10.5281/zenodo.20556327](https://doi.org/10.5281/zenodo.20556327)

13. Quni-Gudzinas, R. B. et al. *Kepler Program: Complete Framework for Adelic
    Quantum Computing.* Zenodo (2026).
    DOI: [10.5281/zenodo.21314315](https://doi.org/10.5281/zenodo.21314315)

14. Avetisov, V. A., Bikulov, A. Kh., Osipov, V. Al. *p-adic description of
    characteristic relaxation in complex systems.* J. Phys. A: Math. Gen. **36**,
    4239 (2003). DOI: [10.1088/0305-4470/36/15/301](https://doi.org/10.1088/0305-4470/36/15/301)

15. Zúñiga-Galindo, W. A. *Ultrametric diffusion, rugged energy landscapes and
    transition networks.* Physica A **597**, 127221 (2022).
    DOI: [10.1016/j.physa.2022.127221](https://doi.org/10.1016/j.physa.2022.127221)

16. Chacón-Cortés, L. F., Zúñiga-Galindo, W. A. *Nonlocal operators, parabolic-type
    equations, and ultrametric random walks.* J. Math. Phys. **54**, 113503 (2013).
    DOI: [10.1063/1.4828857](https://doi.org/10.1063/1.4828857)

17. Gubser, S. S., Knaute, J., Parikh, S., Samberg, A. *p-Adic AdS/CFT.*
    Commun. Math. Phys. **352**, 1019 (2017).
    DOI: [10.1007/s00220-016-2813-6](https://doi.org/10.1007/s00220-016-2813-6)

18. Hung, L.-Y., Li, W., Melby-Thompson, C. M. *p-adic CFT is a holographic tensor
    network.* JHEP **04**, 170 (2019).
    DOI: [10.1007/jhep04(2019)170](https://doi.org/10.1007/jhep04(2019)170)

19. Heydeman, M., Marcolli, M., Saberi, I., Stoica, B. *Tensor networks, p-adic
    fields, and algebraic curves: arithmetic and the AdS$_3$/CFT$_2$ correspondence.*
    Adv. Theor. Math. Phys. **22**, 93 (2018).
    DOI: [10.4310/atmp.2018.v22.n1.a4](https://doi.org/10.4310/atmp.2018.v22.n1.a4)

20. Fawcett, G. *Two Balls on a Tree: The Born Rule as Projection Geometry on a
    p-Adic Dendrogram.* Zenodo (2026).
    DOI: [10.5281/zenodo.19235811](https://doi.org/10.5281/zenodo.19235811)

21. Deninger, C. *p-adic Entropy and a p-adic Fuglede–Kadison Determinant.*
    Prog. Math. (2009). DOI: [10.1007/978-0-8176-4745-2_10](https://doi.org/10.1007/978-0-8176-4745-2_10)

22. Aniello, P., Mancini, S., Parisi, V. *A p-Adic Model of Quantum States and the
    p-Adic Qubit.* Entropy **25**(1), 86 (2022).
    DOI: [10.3390/e25010086](https://doi.org/10.3390/e25010086)

23. Aniello, P., Mancini, S., Parisi, V. *Quantum mechanics on a p-adic Hilbert
    space: Foundations and prospects.* Int. J. Mod. Phys. A (2024).
    DOI: [10.1142/s0219887824400176](https://doi.org/10.1142/s0219887824400176)

24. Kalisch, G. K. *On p-Adic Hilbert Spaces.* Ann. Math. (1947).
    DOI: [10.2307/1969224](https://doi.org/10.2307/1969224)

25. Vladimirov, V. S., Volovich, I. V. *p-adic quantum mechanics.*
    Commun. Math. Phys. **123**, 659 (1989).
    DOI: [10.1007/bf01218590](https://doi.org/10.1007/bf01218590)

26. Khrennikov, A. *p-adic valued probability measures.* Indag. Math. (1996).
    DOI: [10.1016/0019-3577(96)83723-2](https://doi.org/10.1016/0019-3577(96)83723-2)

27. Huberman, B. A., Kerszberg, M. *Ultradiffusion: the relaxation of hierarchical
    systems.* J. Phys. A **18**(6) (1985).
    DOI: [10.1088/0305-4470/18/6/013](https://doi.org/10.1088/0305-4470/18/6/013)

28. Albeverio, S., Karwowski, W. *A random walk on p-adics — the generator and its
    spectrum.* Stoch. Proc. Appl. (1994).
    DOI: [10.1016/0304-4149(94)90054-x](https://doi.org/10.1016/0304-4149(94)90054-x)
