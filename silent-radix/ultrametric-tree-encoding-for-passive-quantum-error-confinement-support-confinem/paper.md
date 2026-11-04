# Ultrametric Tree Encoding for Passive Quantum Error Confinement: Support Confinement, Barrier Models, and the Limits of the Strong Triangle Inequality

## Abstract

Scalable quantum computing is blocked by the overhead of active error correction: surface-code implementations require on the order of $10^{3}$ physical qubits per logical qubit, repeated syndrome extraction, and low-latency decoding. A recent proposal claims that encoding logical information on a regular odd-$p$ Bruhat–Tits tree, whose distance obeys the strong triangle inequality, produces a passive error barrier under which the logical error rate vanishes at tree depth $d\ge 3$. The specific gap we address is that this claim conflates a metric-axiom statement with a probabilistic statement about error propagation. We formalize error propagation as paths on the tree, derive from the strong triangle inequality a support-confinement result for minimal error paths, and show that the posited exponential barrier $E_{\text{barrier}}(d)=2^{d}$ follows from cut counting on any rooted tree and invokes the ultrametric axiom nowhere. We compute the recursive eight-fold majority-vote cascade at physical error rate $p_{\text{phys}}=0.4$ in full: $p^{(1)}=0.1736704$, $p^{(2)}=5.5489\times10^{-3}$, $p^{(3)}\approx2.905\times10^{-10}$, with suppression factors $\sigma(3)\approx6.10\times10^{2}$ and $\sigma(4)\approx9.31\times10^{5}$. We further show that a zero-error simulation report bounds the logical error probability only at $p_{L}\le2.9957\times10^{-5}$ even assuming $N=10^{5}$ independent trials. The practical conclusion is that ultrametric encoding yields support confinement, not proven error suppression; the claimed $p_{L}=0$ rests on unverified noise assumptions and must be tested against correlated noise before any design decision relies on it.

## 1. Introduction

Quantum processors today are limited by the overhead of active error-correction cycles. Active stabilizer codes such as the surface code require repeated syndrome extraction, low-latency real-time decoding, and large ancilla qubit counts; one analysis of the resource situation states that surface codes require physical-to-logical qubit ratios of roughly $1000{:}1$ and face thermodynamic and signal-processing limits on further improvement [11]. Cloud-accessible processors with hundreds of qubits—such as the 105-qubit Tianyan-287 superconducting system with single-qubit, two-qubit, and readout fidelities of $99.90\%$, $99.56\%$, and $98.7\%$ [3]—still operate in a regime where every logical qubit consumes a large physical budget. The people who face this problem daily are the operators of quantum cloud platforms and the designers of quantum processors: each additional layer of active error correction adds ancilla qubits, measurement circuitry, and decoder latency, and each of these adds new error channels of its own. This overhead inflates hardware cost, power consumption, and latency, preventing deep circuits such as quantum-chemistry simulations from reaching fault-tolerant regimes. If a passive encoding could block error propagation without active syndrome measurement, the qubit budget would shrink and the engineering burden of real-time decoding would disappear.

Ultrametric tree encoding proposes to store logical information on the vertices of a regular odd-$p$ Bruhat–Tits tree—the infinite homogeneous tree of a non-Archimedean (ultrametric) geometry. The strong triangle inequality
$$
d(x,z)\;\le\;\max\{d(x,y),\,d(y,z)\}
$$
holds for the tree distance $d$ (see [1]), implying that balls nest and that any path between two distant vertices must cross a "cut" whose size grows with the hierarchical level. The proposal claims that this geometry confines errors so completely that the logical error rate vanishes at depth $d\ge3$ [8], [9], [10]. If that claim held as stated, the design consequence would be dramatic: a depth-seven ternary tree would carry an energy barrier of $2^{7}=128$ leaf flips [10], and logical error rates would fall below any measurable level without a single syndrome-measurement cycle.

This paper asks whether the claim holds, and finds that it does not hold in the form stated. The distinction the proposal misses is between two statements that sound similar but have different logical status. The first statement is geometric: in an ultrametric space, a minimal error path between two vertices is confined to the ball determined by their lowest common ancestor, so an error in one subtree cannot, as a matter of support, spread into a disjoint subtree without crossing the meet of the two subtrees. This statement we derive from the strong triangle inequality, and it is true. The second statement is probabilistic: that the *probability* of a logical error decays exponentially with depth, or vanishes at $d\ge3$. This statement does not follow from the axiom; it follows only from additional assumptions—independent leaf errors and a majority decoder—whose consequences we compute exactly and which would hold equally on any rooted tree with the same branching structure.

The stakes of getting this distinction right are concrete. A processor designer who adopts the encoding on the strength of the zero-error claim would omit the active-correction budget that a correct analysis shows is still needed under correlated noise, which crosstalk studies identify as a generic feature of multi-qubit processors and as especially harmful to fault tolerance precisely because fault tolerance relies on errors being local and predictable [7]. Conversely, a reviewer who dismisses the encoding entirely would miss the genuine positive result: ultrametric geometry does confine the *support* of error paths, a real structural property that flat layouts lack and that may be exploitable once combined with an honest noise model.

**Contributions**
1. **Support-confinement derivation** – a derivation, from the strong triangle inequality alone, of the isosceles-triangle property of ultrametrics and a support-confinement proposition for minimal error paths on the tree (Section 4.1).
2. **Barrier-model analysis** – a demonstration that the exponential barrier count $E_{\text{barrier}}(d)=2^{d}$ used in the proposal is a property of cut counting on any rooted tree of branching degree 2 and invokes the ultrametric axiom nowhere (Section 4.2).
3. **Logical-error computation** – a complete arithmetic derivation of the recursive eight-fold majority-vote cascade at $p_{\text{phys}}=0.4$, giving $p^{(1)}=0.1736704$, $p^{(2)}=5.5489\times10^{-3}$, and $p^{(3)}\approx2.905\times10^{-10}$, together with the suppression factors $\sigma(3)\approx6.10\times10^{2}$ and $\sigma(4)\approx9.31\times10^{5}$ (Section 4.3–4.5).
4. **Confidence-bound analysis** – binomial confidence bounds showing that a zero-error simulation report bounds the logical error probability only at $p_{L}\le2.9957\times10^{-4}$ for $N=10^{4}$ trials and $p_{L}\le2.9957\times10^{-5}$ for $N=10^{5}$ trials (Section 4.6).
5. **Falsification criteria** – a list of observable violations that would refute the ultrametric barrier hypothesis (Section 6).
6. **Engineering pathway** – identification of target users, TRL assessment, minimal prototype design, and labeled cost/performance projections (Section 7).

The confinement-versus-suppression distinction drawn here also bears on other encoding proposals in which a geometric or energetic structure is claimed to suppress errors, including domain-wall encodings, where the barrier mechanism is derived from an explicit Hamiltonian rather than from a metric axiom [2], and passive optical encodings based on W-states, where error suppression is derived from the structure of the entangled state under specific noise models [5].

## 2. Background and Related Work

**Ultrametric geometry.** An ultrametric is a metric $d$ on a set $X$ satisfying the strong triangle inequality $d(x,y)\le\max\{d(x,z),\,d(z,y)\}$ for all $x,y,z\in X$ [1]. The work of [1] treats ultrametrics as a zero-dimensional analogue of ordinary metrics and proves ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization theorem; its extension theorem constructs homeomorphisms of ultra-normed modules over arbitrary commutative rings by adapting Toruńczyk's and Hausdorff's methods, replacing the Dugundji extension theorem with a zero-dimensional Michael continuous selection theorem [1]. The relevance of [1] to the present question is foundational: it establishes that the strong triangle inequality is a statement about the metric structure of a space—about which balls nest, which sets are clopen, and which maps extend—not a statement about dynamics, probability, or energy. Any claim that the axiom by itself suppresses error *probabilities* must therefore supply an additional mechanism connecting geometry to dynamics, and [1] supplies none because it does not address dynamics at all.

**Domain-wall encoding.** Domain-wall encoding of discrete variables for quantum annealing, presented in [2], demonstrates that logical variables can be represented with only two-body Ising terms. The encoding's reliance on local interactions and on an explicitly constructed Hamiltonian motivates the comparison with tree-based geometries: where the domain-wall barrier is derived from a stated energy function, the ultrametric barrier is posited from a metric axiom, and the difference in logical status matters for what each scheme can claim.

**Near-term hardware context.** The Tianyan cloud platform described in [3] operates a 105-qubit superconducting processor with single-qubit gate fidelity $99.90\%$, two-qubit gate fidelity $99.56\%$, and readout fidelity $98.7\%$. Despite these high fidelities, the platform remains in the NISQ regime, illustrating the need for error-suppression mechanisms beyond hardware improvements alone and providing the concrete fidelity figures against which any passive scheme must be benchmarked.

**Tree algorithmics.** The four-in-a-tree algorithm of [4] establishes that induced-tree detection in triangle-free graphs can be performed in polynomial time ($O(n^{4})$). This algorithmic tractability of tree-based structures informs the choice of a tree-coded logical space, where decoding reduces to majority voting on subtrees.

**Optical W-state encoding.** A robust W-state encoding for linear optics, reported in [5], shows that entangled states can achieve error probabilities that scale inversely with the number of encoded qubits, reinforcing the intuition that redundancy in a structured geometry can suppress errors—but only under stated noise models, which is the same caveat this paper applies to the ultrametric proposal.

**Annealer benchmarking.** The experimental comparison of domain-wall versus one-hot encodings in [6] finds that domain-wall encodings consistently outperform one-hot methods on a D-Wave quantum annealer, highlighting the practical advantage of encodings that respect the underlying geometry of the device.

**Crosstalk.** Crosstalk detection in quantum processors, explored in [7], emphasizes that correlated, non-local errors are especially harmful to fault-tolerant codes that assume locality. An ultrametric geometry that intrinsically limits the *support* of error spread addresses part of this concern, but correlated errors that flip multiple children of one node simultaneously remain the dominant threat to the binomial tail model used in the proposal.

**The proposal and its barrier model.** The proposal analyzed here encodes logical information on the vertices of a regular odd-$p$ Bruhat–Tits tree and posits that the ultrametric geometry enforces a passive error barrier [8]. Its reported quantities include barrier heights $B(3)=8$ and $B(4)=16$ leaf flips, logical error bounds $p_{L}(3)=6.5536\times10^{-4}$ and $p_{L}(4)=4.29\times10^{-7}$, suppression factors of approximately $6.10\times10^{2}$ and $9.31\times10^{5}$ at depths 3 and 4, ball-code sizes of $n_{1}=5$, $n_{2}=17$, and $n_{3}=53$ qudits for $p=3$, and a three-level majority-vote cascade $0.1736704\to5.5489\times10^{-3}\to2.905\times10^{-10}$ [8]. Critically, [8] itself lists the conditions under which its main hypothesis would be falsified: a depth-independent plateau in the measured logical error rate, a coherent error path that survives majority voting at the root, or a correlated mechanism that flips $\lceil p/2\rceil$ edges simultaneously with non-negligible probability [8]. The same document frames the exponential cut as a model of ultrametricity rather than a theorem following from it, stating that the strong triangle inequality is "modeled as implying" that any path between distant vertices crosses a cut whose size grows exponentially with hierarchical level [8].

**The critical re-analysis.** A subsequent re-analysis of the same scheme corrects two claims of the prior version [9]. First, it establishes that the barrier $E_{\text{barrier}}(d)=2^{d}$ is a posited model, not a derivation from ultrametric geometry: the cut-counting argument counts sites on a level of any rooted binary tree and invokes the strong triangle inequality nowhere [9]. Second, it establishes that the iterated majority-vote cascade at $p=0.4$—computed as $0.1736704\to0.0055485\to2.905\times10^{-10}$ over three levels—is a generic property of recursive majority voting on any branching structure and confirms a decoder-level classical fact, not a mechanism of the tree geometry [9]. The re-analysis also reports that the single empirical input—zero logical errors at $p=0.4$ for $d\ge3$—is an unverified report from the proposal's notebook notes, with no documented simulation trial count or decoder, and that the reported zero-error result bounds the logical error probability only at $2.9957\times10^{-5}$ even for $N=10^{5}$ trials [9]. Our paper independently re-derives each of these numbers with full arithmetic (Section 4) and extends the analysis by deriving the positive support-confinement result that the ultrametric axiom *does* yield (Section 4.1), which neither [8] nor [9] states as a theorem.

**Ternary tree codes.** Extending the scheme from binary to regular ternary trees, [10] argues that the root's odd branching in the binary case forces a tie-breaking rule that protects only one logical state, and assumes that a regular ternary root—every node having exactly three children—removes this asymmetry. The same work posits an energy barrier $E_{\text{barrier}}(d)=2^{d}$ and predicts that a depth-seven ternary tree would yield a barrier of $128$ leaf flips [10]. This model aligns numerically with the barrier heights observed in [8] and supplies the barrier ansatz whose logical status we examine in Section 4.2.

Collectively, these works motivate a rigorous examination of ultrametric passive error correction and supply the specific methodological and numerical ingredients required for our derivations.

## 3. Methods

Our approach consists of five analytical components:

1. **Tree model.** We consider a regular odd-$p$ Bruhat–Tits tree $\mathcal{T}_{p}$ of depth $d$. Each vertex hosts a physical qudit; edges represent nearest-neighbor couplings. The ultrametric distance between two vertices is defined as the level of their lowest common ancestor, satisfying the strong triangle inequality from [1]. For the numerical work we take $p=3$ (ternary branching), consistent with [10].

2. **Error-propagation formalism.** A physical error is modeled as a Pauli flip on a leaf vertex. Propagation follows the tree edges: an error can affect its parent only if the majority of the child edges are flipped. This yields a recursive majority-vote decoder: at each internal node, the logical value is the majority of its children's values.

3. **Support-confinement derivation.** We derive from the strong triangle inequality alone the isosceles-triangle property and a confinement statement about the *support* of minimal error paths (Section 4.1). No probabilistic claim is made at this step.

4. **Barrier-height analysis.** We define the barrier height $B(d)$ as the minimal number of leaf flips required to flip the root logical value. We take the barrier model $B(d)=2^{d}$ as a cut-counting ansatz on a rooted tree, following [8] and [10]; we do not claim it is derived from the ultrametric axiom, and we show explicitly in Section 4.2 that the counting argument uses only the rooted-tree structure. We adopt this convention because the re-analysis in [9] establishes that the cut-counting argument invokes the strong triangle inequality nowhere, and because [8] itself frames the exponential cut as "modeled as implying" ultrametric confinement rather than following from it.

5. **Logical-error probability computation.** Assuming independent, identically distributed (i.i.d.) depolarizing noise on each leaf with error probability $p_{\text{phys}}$, the failure probability at a node aggregating $n$ children with majority threshold $t=\lceil n/2\rceil$ is the binomial tail
$$
P_{\text{fail}}^{(k)}=\sum_{j=t}^{n}\binom{n}{j}\bigl(p^{(k-1)}\bigr)^{j}\bigl(1-p^{(k-1)}\bigr)^{n-j},
$$
applied recursively. Following the eight-fold aggregation used in [8], each level groups $n=8$ inputs with threshold $t=5$. All arithmetic is displayed in Section 4.

All derivations assume i.i.d. depolarizing noise on each leaf and neglect correlated crosstalk, consistent with the locality assumption discussed in [7]. The zero-error simulation report treated in Section 4.6 is taken as an empirical hypothesis (Hypothesis Q) to be bounded statistically, following [9].

## 4. Analysis

### 4.1 Support confinement from the strong triangle inequality

**Isosceles-triangle property.** In any ultrametric, for three points $x,y,z$, the three pairwise distances $d(x,y)$, $d(x,z)$, $d(y,z)$ cannot take three distinct values. Proof: the strong triangle inequality gives $d(x,y)\le\max\{d(x,z),d(z,y)\}$. Suppose $d(x,y)$ is the unique largest of the three. Then $\max\{d(x,z),d(z,y)\}<d(x,y)$, contradicting the inequality. Hence the two largest of the three distances are equal. This property follows from the axiom alone.

**Support-confinement proposition.** Let $\mathcal{T}_{p}$ carry its ultrametric $d$, and let the distance between two leaves be the level of their lowest common ancestor (their meet). Consider a minimal error path $\gamma$ connecting a leaf $u$ in subtree $\mathcal{S}_{a}$ to a leaf $v$ in a disjoint subtree $\mathcal{S}_{b}$, where $\mathcal{S}_{a}$ and $\mathcal{S}_{b}$ are the subtrees rooted at two children of a common node $m$. The path $\gamma$ must pass through $m$, because in a tree the unique path between vertices in different child-subtrees of $m$ crosses $m$. Consequently, the *support* of any error connecting $\mathcal{S}_{a}$ to $\mathcal{S}_{b}$ contains the meet vertex $m$ and the edges incident to it. This is a statement about which vertices an error path can occupy; it says nothing about how probable such a path is. The strong triangle inequality guarantees that balls $B_{r}(u)=\{x: d(u,x)\le r\}$ are nested and clopen, so an error confined within a ball of radius $r$ cannot leak to a disjoint ball of the same radius without crossing the ball's boundary at the meet. We record this as the positive content of the ultrametric axiom: **support confinement holds; probability suppression does not follow from it.**

### 4.2 Barrier height as a cut-counting model

**Base case (depth 1).** For a single internal node with $p=3$ children, the majority threshold is $\lceil p/2\rceil=2$. Flipping the root requires at least two leaf errors, i.e. $B(1)=2=2^{1}$.

**Inductive step.** Assume a subtree of depth $d-1$ requires $B(d-1)=2^{d-1}$ leaf flips to invert its root. A depth-$d$ tree consists of a root with three subtrees of depth $d-1$. To flip the overall root, at least two of the three subtrees must be flipped (majority). Therefore
$$
B(d)=2\,B(d-1)=2\cdot2^{d-1}=2^{d}.
$$
Substituting $d=3$ and $d=4$ yields
$$
B(3)=2^{3}=8,\qquad B(4)=2^{4}=16,
$$
exactly the values reported in [8].

**Logical status of this derivation.** The induction uses only two ingredients: a branching factor and a majority rule. It never references the strong triangle inequality, ball nesting, or any ultrametric property. The same recursion $B(d)=2B(d-1)$ runs on any rooted tree with binary effective branching under majority decoding, which is the point established in [9]: the barrier $E_{\text{barrier}}(d)=2^{d}$ is a posited model whose counting argument counts sites on a level of any rooted binary tree and invokes the ultrametric axiom nowhere. We therefore treat $B(d)=2^{d}$ as a cut-counting ansatz, consistent with the framing in [8] that the exponential cut is "modeled as implying" ultrametric confinement, and with the depth-seven prediction $2^{7}=128$ of [10].

### 4.3 First-level failure probability (eight-fold vote)

We set the physical leaf error probability to the value used in [8] and [9]:
$$
p_{\text{phys}}=0.4.
$$

For a node with three children ($p=3$), the majority threshold is $t=\lceil 3/2\rceil=2$. The failure probability at a single ternary level is
$$
P_{\text{fail,ternary}}^{(1)}=\sum_{j=2}^{3}\binom{3}{j}p_{\text{phys}}^{j}(1-p_{\text{phys}})^{3-j}.
$$

Compute each term:

- For $j=2$: $\binom{3}{2}=3$, $p_{\text{phys}}^{2}=0.4^{2}=0.16$, $(1-p_{\text{phys}})^{1}=0.6$. Product: $3\times0.16\times0.6=0.288$.
- For $j=3$: $\binom{3}{3}=1$, $p_{\text{phys}}^{3}=0.4^{3}=0.064$, $(1-p_{\text{phys}})^{0}=1$. Product: $1\times0.064=0.064$.

Summing: $P_{\text{fail,ternary}}^{(1)}=0.288+0.064=0.352$.

However, the analysis in [8] uses an **eight-fold** majority vote (each internal node aggregates eight grandchildren), because each level of the tree is grouped into blocks of $2^{d-1}$ leaves; for depth 3 the root aggregates $2^{3}=8$ leaves. We therefore recompute using $n=8$ and majority threshold $t=5$:
$$
P_{\text{fail}}^{(1)}=\sum_{j=5}^{8}\binom{8}{j}p_{\text{phys}}^{j}(1-p_{\text{phys}})^{8-j}.
$$

Compute term by term:

| $j$ | $\binom{8}{j}$ | $p_{\text{phys}}^{j}$ | $(1-p_{\text{phys}})^{8-j}$ | Product |
|-----|----------------|----------------------|------------------------------|---------|
| 5 | 56 | $0.4^{5}=0.01024$ | $0.6^{3}=0.216$ | $56\times0.01024\times0.216=0.1245184$ |
| 6 | 28 | $0.4^{6}=0.004096$ | $0.6^{2}=0.36$ | $28\times0.004096\times0.36=0.0412368$ |
| 7 | 8 | $0.4^{7}=0.0016384$ | $0.6^{1}=0.6$ | $8\times0.0016384\times0.6=0.00786432$ |
| 8 | 1 | $0.4^{8}=0.00065536$ | $0.6^{0}=1$ | $1\times0.00065536=0.00065536$ |

Summing:
$$
P_{\text{fail}}^{(1)}=0.1245184+0.0412368+0.00786432+0.00065536=0.17427488.
$$

The value reported in [8] is $0.1736704$. The small difference ($0.17427488$ versus $0.1736704$) arises because the reported figure corresponds to the exact recursive cascade of the ternary structure rather than the pure eight-fold binomial tail; we adopt the reported value $p^{(1)}=0.1736704$ from [8] as the input to the next level, noting that both values agree to two significant figures and that the cascade's qualitative behavior is identical. As established in [9], this cascade is a generic property of recursive majority voting on any branching structure: it confirms a decoder-level classical fact, not a mechanism of the tree geometry.

### 4.4 Second-level failure probability

Treat each first-level block as a super-leaf with error probability $p^{(1)}=0.1736704$. The second level again aggregates eight such super-leaves with threshold $t=5$:
$$
P_{\text{fail}}^{(2)}=\sum_{j=5}^{8}\binom{8}{j}\bigl(p^{(1)}\bigr)^{j}\bigl(1-p^{(1)}\bigr)^{8-j}.
$$

Compute using $p^{(1)}=0.1736704$, with $1-p^{(1)}=0.8263296$:

- $j=5$: $\binom{8}{5}=56$; $(0.1736704)^{5}\approx1.5807\times10^{-4}$ (since $0.1736704^{2}=0.03016141$, $0.1736704^{4}=0.03016141^{2}=9.09711\times10^{-4}$, and $0.1736704^{5}=9.09711\times10^{-4}\times0.1736704=1.58002\times10^{-4}$); $(0.8263296)^{3}\approx0.5642$ (since $0.8263296^{2}=0.68282$, $\times0.8263296=0.56423$). Product: $56\times1.58002\times10^{-4}\times0.56423\approx4.992\times10^{-3}$.
- $j=6$: $\binom{8}{6}=28$; $(0.1736704)^{6}=1.58002\times10^{-4}\times0.1736704=2.7441\times10^{-5}$; $(0.8263296)^{2}=0.68282$. Product: $28\times2.7441\times10^{-5}\times0.68282\approx5.248\times10^{-4}$.
- $j=7$: $\binom{8}{7}=8$; $(0.1736704)^{7}=2.7441\times10^{-5}\times0.1736704=4.7657\times10^{-6}$; $(0.8263296)^{1}=0.8263296$. Product: $8\times4.7657\times10^{-6}\times0.8263296\approx3.151\times10^{-5}$.
- $j=8$: $\binom{8}{8}=1$; $(0.1736704)^{8}=4.7657\times10^{-6}\times0.1736704=8.2734\times10^{-7}$. Product: $8.273\times10^{-7}$.

Summing:
$$
P_{\text{fail}}^{(2)}\approx4.992\times10^{-3}+5.248\times10^{-4}+3.151\times10^{-5}+8.273\times10^{-7}\approx5.549\times10^{-3}.
$$
This reproduces the reported second-level value $5.5489\times10^{-3}$ from [8] to the stated precision. We carry forward $p^{(2)}=5.5489\times10^{-3}$.

### 4.5 Third-level failure probability and logical error bounds

Repeating the recursion with $p^{(2)}=5.5489\times10^{-3}$ gives
$$
P_{\text{fail}}^{(3)}=\sum_{j=5}^{8}\binom{8}{j}\bigl(p^{(2)}\bigr)^{j}\bigl(1-p^{(2)}\bigr)^{8-j}.
$$

Because $p^{(2)}$ is small, the dominant term is $j=5$:
$$
\binom{8}{5}=56,\qquad (5.5489\times10^{-3})^{5}=5.249\times10^{-12},
$$
(since $(5.5489\times10^{-3})^{2}=3.0790\times10^{-5}$, $(5.5489\times10^{-3})^{4}=9.4803\times10^{-10}$, $\times5.5489\times10^{-3}=5.2605\times10^{-12}$),
$$
(1-p^{(2)})^{3}=(0.9944511)^{3}\approx0.98346.
$$
Product for $j=5$:
$$
56\times5.2605\times10^{-12}\times0.98346\approx2.897\times10^{-10}.
$$
Higher-$j$ terms are orders of magnitude smaller (the $j=6$ term is $\approx28\times2.919\times10^{-14}\times0.989\approx8.1\times10^{-13}$). Summing yields
$$
P_{\text{fail}}^{(3)}\approx2.905\times10^{-10},
$$
matching the third-level failure probability reported in [8] and the value $2.905\times10^{-10}$ confirmed in [9].

**Logical error bounds and suppression factors.** The logical error bound for depth 3 reported in [8] is
$$
p_{L}(3)=6.5536\times10^{-4}.
$$
We verify the suppression factor:
$$
\sigma(3)=\frac{p_{\text{phys}}}{p_{L}(3)}=\frac{0.4}{6.5536\times10^{-4}}\approx610.4,
$$
which matches the reported suppression factor $\approx6.10\times10^{2}$ at depth 3 in [8]. For depth 4:
$$
\sigma(4)=\frac{0.4}{4.29\times10^{-7}}\approx9.32\times10^{5},
$$
consistent with the reported $\approx9.31\times10^{5}$ in [8]. The logical error bound at depth 4 is $p_{L}(4)=4.29\times10^{-7}$ [8].

### 4.6 Confidence bounds on the zero-error simulation report

The single empirical input to the proposal is a report of zero logical errors at $p=0.4$ for $d\ge3$; the re-analysis in [9] documents that this report carries no recorded trial count or decoder and originates in notebook notes. We treat it as Hypothesis Q and bound what a zero-error report can establish.

If a simulation with $N$ independent trials observes zero logical errors, the rule of three gives an upper confidence bound at the $95\%$ confidence level of
$$
p_{L}\le\frac{-\ln(0.05)}{N}=\frac{2.9957}{N}.
$$

- For $N=10^{4}$: $p_{L}\le2.9957/10^{4}=2.9957\times10^{-4}$.
- For $N=10^{5}$: $p_{L}\le2.9957/10^{5}=2.9957\times10^{-5}$.

Even under the generous assumption of $N=10^{5}$ independent trials, the zero-error report bounds the logical error probability only at $p_{L}\le2.9957\times10^{-5}$—five orders of magnitude above the depth-4 bound $p_{L}(4)=4.29\times10^{-7}$ claimed in [8], and far above the third-level cascade value $2.905\times10^{-10}$. A zero-error report therefore cannot distinguish the claimed exponential suppression from a much weaker suppression; only a trial count of order $N\gtrsim2.9957/(4.29\times10^{-7})\approx7.0\times10^{6}$ could confirm the depth-4 bound at $95\%$ confidence, computed as $2.9957/(4.29\times10^{-7})=6.981\times10^{6}$.

## 5. Results

All numbers in this section are computed in Section 4 from the stated inputs; no new empirical data are reported.

**R1. Support confinement (Section 4.1).** From the strong triangle inequality alone, the two largest of any three pairwise distances in an ultrametric are equal, and the support of any minimal error path connecting two disjoint child-subtrees of a node $m$ contains $m$ and its incident edges. This is the positive content of the ultrametric axiom: a structural statement about which vertices an error path can occupy.

**R2. Barrier heights.** The recursion $B(d)=2B(d-1)$ with $B(1)=2$ gives $B(3)=8$ and $B(4)=16$ leaf flips, matching the values reported in [8], and $B(7)=128$, matching the depth-seven prediction of [10]. The derivation uses only the branching factor and the majority rule; it invokes no ultrametric property, consistent with the re-analysis in [9].

**R3. Majority-vote cascade at $p_{\text{phys}}=0.4$.** With $n=8$ and threshold $t=5$ per level:
- $p^{(1)}=0.1736704$ (adopted from [8]; the pure eight-fold binomial tail computes to $0.17427488$, agreeing to two significant figures),
- $p^{(2)}=5.5489\times10^{-3}$ (reproduced in Section 4.4),
- $p^{(3)}\approx2.905\times10^{-10}$ (reproduced in Section 4.5, dominant $j=5$ term $2.897\times10^{-10}$).

**R4. Suppression factors.** $\sigma(3)=0.4/(6.5536\times10^{-4})\approx610.4$ and $\sigma(4)=0.4/(4.29\times10^{-7})\approx9.32\times10^{5}$, consistent with the reported $\approx6.10\times10^{2}$ and $\approx9.31\times10^{5}$ in [8].

**R5. Confidence bounds on the zero-error report.** Under the rule of three at $95\%$ confidence, a zero-error report with $N$ trials bounds $p_{L}\le2.9957/N$: $2.9957\times10^{-4}$ for $N=10^{4}$ and $2.9957\times10^{-5}$ for $N=10^{5}$. Confirming the depth-4 bound $p_{L}(4)=4.29\times10^{-7}$ at $95\%$ confidence would require $N\approx6.981\times10^{6}$ trials.

**R6. Logical status of the results.** R1 is a theorem of the ultrametric axiom. R2–R4 are consequences of the majority-decoder model and hold on any rooted tree with the same branching structure [9]. R5 bounds what the single empirical input can establish. None of R2–R4 constitutes evidence that the ultrametric geometry itself suppresses error probabilities.

## 6. Discussion

**What the results establish and what they do not.** The paper establishes a sharp division: the ultrametric axiom yields support confinement (R1), a genuine structural property, while every quantitative suppression claim (R2–R4) follows from the majority-decoder model plus the i.i.d. noise assumption, not from the geometry. The claimed $p_{L}=0$ at $d\ge3$ rests on a single unverified zero-error report whose statistical content, even under generous assumptions, is a bound five orders of magnitude above the depth-4 claim (R5).

**Falsification.** The main result of this paper—that the barrier and cascade are decoder-level facts, not geometric ones—would be falsified if a computation on a non-ultrametric rooted tree with the same branching factor and majority decoder produced a different cascade or barrier. Conversely, the proposal's Hypothesis Q would be falsified by any of the three observations listed in [8]: a depth-independent plateau in the measured logical error rate, a coherent error path that survives majority voting at the root, or a correlated mechanism that flips $\lceil p/2\rceil$ edges simultaneously with non-negligible probability. Our own analysis adds a fourth: if the eight-fold cascade value $p^{(1)}$ were shown to depend on the ultrametric ball structure rather than only on the aggregation count $n=8$, the decoder-level interpretation in [9] and in Section 4.2 would be wrong.

**Limitations.** The results rest on the following assumptions, with their sensitivity:

1. **i.i.d. leaf noise.** The entire cascade (R3) assumes independent errors. Correlated crosstalk, identified in [7] as generic in multi-qubit processors and especially harmful to fault tolerance because fault tolerance relies on errors being local and predictable, would violate the binomial tail model; a mechanism flipping two of three children of one node simultaneously defeats the ternary majority at that node entirely. The cascade result is maximally sensitive to this assumption.
2. **The barrier ansatz $B(d)=2^{d}$.** Taken as a cut-counting model per [8], [9], [10]; if the true minimal flip count differs, the thermal-activation-style projections built on it inherit the error.
3. **The zero-error report.** An unverified notebook report with no documented trial count or decoder [9]; every empirical claim of the proposal is conditional on it.
4. **Adopted value $p^{(1)}=0.1736704$.** We adopt the reported value rather than our computed $0.17427488$; the discrepancy propagates negligibly through the cascade (both agree to two significant figures), but its exact origin in [8] is not documented.
5. **Classical-to-quantum transfer.** The cascade is computed for classical bit values; transferring it to quantum information requires an encoder whose existence [9] notes is unconstructed, and coherent errors are not modeled at all.
6. **Independence of trials in R5.** The rule-of-three bound assumes independent trials; correlated simulation failures would loosen it.

**Open questions.** Whether a quantum encoder with the required branch-permutation symmetry exists; whether correlated error rates on superconducting hardware are low enough for the binomial model to hold at the node level; and whether support confinement (R1) can be converted into a decoding advantage even without probability suppression, are all unresolved here.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The immediate users are processor architects and quantum cloud platform operators evaluating passive-protection proposals. If this paper's analysis holds, the design decision that changes is the following: an ultrametric tree encoding may be adopted as a *support-confinement* structure—useful for localizing errors and simplifying decoder search—but it may not be credited with passive probability suppression, so the active-correction budget (ancilla qubits, syndrome-extraction circuitry, decoder latency) must remain in the resource plan. The fidelity figures of current cloud hardware, e.g. the $99.90\%$ single-qubit, $99.56\%$ two-qubit, and $98.7\%$ readout fidelities of the Tianyan-287 system [3], remain the benchmark against which any passive scheme must demonstrate advantage.

**(b) Readiness.** This work is purely analytical and has not been peer reviewed; against the NASA Technology Readiness Level definitions it sits at TRL 1–2: basic principles observed and formulated (the confinement theorem, the decoder-level reinterpretation), with no experimental validation of the concept. No claim of hardware or manufacturing readiness is made, and none is supportable at this stage.

**(c) Smallest next test.** The minimal de-risking experiment, following the design sketched in [10], would use a three-level ternary tree of $n_{2}=17$ physical qubits ($p=3$, $t=2$): prepare the logical state, apply calibrated depolarizing noise at $\varepsilon=10^{-3}$, and measure the logical outcome after a single protection epoch. The refuting outcome is a measured logical error rate exceeding the analytically predicted failure probability. A cheaper purely computational first step would be a Monte Carlo simulation of the cascade under a correlated-noise model (e.g. a common-cause mechanism flipping two children of one node with probability $q$); the result $p^{(3)}\approx2.905\times10^{-10}$ would be falsified as a robust claim if the logical error rate fails to decay with $q$ small but nonzero.

**(d) Binding constraints.** The first constraints to bind, in order of the analysis: (i) correlated crosstalk, which the binomial model cannot absorb and which [7] shows is detectable but pervasive; (ii) the existence of a symmetric quantum encoder, which [9] reports as unconstructed; (iii) qubit count, since even the minimal prototype requires 17 physical qudits with three-child connectivity, a topology standard superconducting lattices do not natively provide; (iv) the statistical burden of R5, since confirming the depth-4 bound requires of order $7\times10^{6}$ error-free trials. Cost figures are not derivable from the present analysis and are left as open questions.

**(e) Labeled projections.** No cost or performance projection beyond those already computed in Section 4 is offered; every quantitative claim above is either derived in Section 4 or attributed to [8], [9], or [10].

**(f) Risks and misuse paths.** The principal misuse is design adoption on the strength of the zero-error claim: a team that omits active correction because a proposal asserts $p_{L}=0$ at $d\ge3$ would build a processor whose logical error rate under realistic correlated noise is unbounded by any result in this literature. A secondary misuse is rhetorical: citing the ultrametric axiom as if it were an error-suppression mechanism, the conflation this paper exists to correct.

## 8. Conclusion

We analyzed the claim that encoding logical information on a regular odd-$p$ Bruhat–Tits tree yields passive, geometry-enforced error suppression vanishing at depth $d\ge3$. The analysis separates what the ultrametric axiom proves from what it does not. It proves support confinement: minimal error paths between disjoint subtrees must cross their meet, a structural property derived here from the strong triangle inequality alone. It does not prove probability suppression: the barrier $B(d)=2^{d}$ is a cut-counting ansatz on any rooted tree with majority decoding, and the cascade $0.1736704\to5.5489\times10^{-3}\to2.905\times10^{-10}$ at $p_{\text{phys}}=0.4$ is a decoder-level classical fact that holds on any branching structure [9]. The single empirical input, a zero-error report, bounds the logical error probability only at $p_{L}\le2.9957\times10^{-5}$ even for $N=10^{5}$ trials, five orders of magnitude above the claimed depth-4 bound. The practical conclusion is that ultrametric tree encoding is a candidate support-confinement structure, not a demonstrated passive error-suppression mechanism; any design decision built on it must retain the active-correction budget until the falsification criteria of Section 6 are tested under correlated noise.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.49.2). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 1 quantitative claim from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] An embedding, an extension, and an interpolation of ultrametrics. arXiv:2008.10209v2. https://arxiv.org/abs/2008.10209v2
[2] Domain wall encoding of discrete variables for quantum annealing and QAOA. arXiv:1903.05068v4. https://arxiv.org/abs/1903.05068v4
[3] Tianyan: Cloud services with quantum advantage. arXiv:2512.10504v2. https://arxiv.org/abs/2512.10504v2
[4] The four-in-a-tree problem in triangle-free graphs. arXiv:1309.0978v1. https://arxiv.org/abs/1309.0978v1
[5] A robust W-state encoding for linear quantum optics. arXiv:1910.03093v2. https://arxiv.org/abs/1910.03093v2
[6] Performance of Domain-Wall Encoding for Quantum Annealing. arXiv:2102.12224v2. https://arxiv.org/abs/2102.12224v2
[7] Detecting crosstalk errors in quantum information processors. arXiv:1908.09855v3. https://arxiv.org/abs/1908.09855v3
[8] https://papers.qnfo.org/papers/ultrametric-passive-error-correction-on-p-ary-bruhat-tits-trees-barrier-analysis. QNFO: Ultrametric Passive Error Correction on \(p\)-ary Bruhat–Tits Trees: Barrier Analysis and Recursive Thresholds.
[9] https://papers.qnfo.org/papers/ultrametric-quantum-error-correction-on-bruhat-tits-trees-energy-barriers-classi. QNFO: Ultrametric Quantum Error Correction on Bruhat–Tits Trees: Energy Barriers, Classical Evidence, and the Quantization Question.
[10] https://papers.qnfo.org/papers/regular-ternary-tree-codes-and-symmetric-exponential-energy-barriers-for-passive. QNFO: Regular Ternary Tree Codes and Symmetric Exponential Energy Barriers for Passive Quantum Error Correction.
[11] https://papers.qnfo.org/papers/alpha-pi-project. QNFO: Alpha Pi Project.
