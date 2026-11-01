# Syntactic Token Calculus: Deriving Particle-like Normal Forms from Distinction Operations (Erratum-Corrected Revision)

## Abstract

High-energy physics explains the particle spectrum through continuous quantum fields and a growing inventory of unobservable entities, a framework whose theoretical and experimental costs are substantial and whose falsifiability is contested. A gap exists in supplying a minimal discrete substrate from which particle-like structures could be generated without presupposing fields. This paper revises the Syntactic Token Calculus (STC), a two-primitive formal system built from a mark $\#$ and nested enclosures $[\,]$, and corrects two published errors: the earlier claim of proven confluence is downgraded to a conjecture supported by a termination proof and a proposed Newman's-lemma route, and the previously reported normal-form counts (42 at depth 5, 114 at depth 6) are withdrawn as underived results. What remains established is a termination proof for the four-rule rewrite system, a well-defined enumeration algorithm, and three quantitative benchmarks carried over from the prior version with shown arithmetic: an average multilingual parsing score of $78.7\%$ across nine languages, an expected $0.063$ stochastic noise events per logical gate in a depth-5 Bruhat-Tits tree model, and a conditional error-suppression factor exceeding $6.3\times10^{10}$. The revision converts the central particle-correspondence claim into a falsifiable target for a concrete enumeration experiment whose resource cost is bounded below a standard laptop budget.

## 1. Introduction

Researchers and funding agencies in particle physics face escalating costs for experiments that probe ever higher energies without a guaranteed conceptual payoff, because the prevailing framework explains the observed spectrum through continuous quantum fields, spontaneous symmetry breaking, and unobservable entities such as virtual particles and dark sectors. A decision that would change under the result of this paper is the allocation of theoretical effort: if particle-like structures can be generated as stable normal forms of a minimal distinction-drawing calculus, then model building becomes a matter of enumerating and classifying normal forms rather than solving field-theoretic equations, and the epistemic burden of continuous-field postulates is reduced to a checkable combinatorial claim.

The Syntactic Token Calculus (STC) is a two-primitive formal system: a mark $\#$ representing the act of drawing a distinction, and an enclosure pair $[\,]$ that nests arbitrarily. The prior version of this paper [14] stated in its Section 3.3 that the rewrite system is confluent immediately after conceding that confluence was only conjectured, and stated in its Result 4 that enumeration yields 42 irreducible normal forms at depth 5 and 114 at depth 6 while Section 4 contained no derivation of those counts. Both statements are corrected here. The corrected position is stronger as science: a termination proof and a clearly labeled conjecture, plus an enumeration algorithm whose execution is proposed rather than claimed, give a falsifiable program instead of an unearned conclusion.

**Contributions.**
- **C1.** Definition of the STC reduction system with a proof of termination and an explicitly conjectural status for confluence, together with the Newman's-lemma route by which the conjecture would be closed (Section 3).
- **C2.** Specification of an enumeration algorithm for irreducible normal forms up to nesting depth 6 and a parity invariant hypothesized to classify them, with no counts claimed as derived (Section 3).
- **C3.** Derivation of the average multilingual parsing score across nine languages, $78.7\%$, from the score table carried over from the prior version (Section 4).
- **C4.** Derivation of the expected stochastic noise events per logical gate, $0.063$, in a depth-5 Bruhat-Tits tree model with the parameters carried over from the prior version (Section 4).
- **C5.** Derivation of the conditional error-suppression factor exceeding $6.3\times10^{10}$ from C4 and an assumed logical error bound (Section 4).
- **C6.** Withdrawal of the previously reported normal-form counts as underived, and their restatement as provisional hypotheses for the proposed enumeration experiment (Sections 4 and 5).
- **C7.** Limitations, falsifiability criteria, and a roadmap for the smallest experimental validation (Section 6).
- **C8.** Practical implications for theoretical physicists and formal-methods engineers, including readiness level and engineering constraints (Section 7).

## 2. Background and Related Work

The STC sits in a lineage of rewrite systems that compute canonical forms, and the corrected confluence status of Section 3 is calibrated against what that lineage actually proves.

The rewrite system for $(S)_{\mathrm{reg}}$ [1] presents an arbitrary semigroup's regular extension by a complete string rewrite system and obtains a new proof of the normal form theorem for $(S)_{\mathrm{reg}}$ as a consequence of completeness. Its termination argument is structured: Lemma 4.1 of [1] shows that if the sub-system of rules (2.1)–(2.4) terminates then the whole system terminates, because the first group of rules is strictly length-reducing so an infinite chain would eventually contain only those rules. This layered termination strategy is the template for the lexicographic measure used in Section 3.3.

The LTL normalization rewrite system [2] transforms any Linear Temporal Logic formula into an equivalent $\Delta_2$ normal form, with Theorem 4.1 of [2] bounding the output at $4^{7|\varphi|}$ nodes for an input formula $\varphi$. Its normal form is characterized by three syntactic exclusion properties (no $\mathbf{U}$-node under a $\mathbf{W}$-node, no limit node under another temporal node, no $\mathbf{W}$-node under a $\mathbf{GF}$-node), and the authors implemented the procedure as a C++ program and compared it against the Owl tool implementation. This shows that a rewrite-based normal-form theory can be carried through proof, implementation, and benchmark; the STC program of Section 7 follows the same three stages and currently sits before the implementation stage.

The associativity rewrite system $(x*y)*z \rightarrow x*(y*z)$ [3] is the closest methodological precedent for the confluence question. Its Section 2 proves strong normalization by assigning each term a positive integer measure $\sigma x$ that strictly decreases, its Lemma 2 proves weak confluence (local confluence) by case analysis on overlapping redexes, and its Lemma 3 records Newman's lemma: $\mathrm{WCR} \wedge \mathrm{SN} \supset \mathrm{CR}$. Section 3.3 of the present paper uses exactly this route: termination is proven, local confluence is conjectured, and the conjecture plus termination would yield confluence by Newman's lemma. Work [3] also shows the payoff of completing this route: once confluence holds, the unique normal form of an associativity term is computable in linear time, and the results were incorporated into an efficient parsing algorithm for Combinatory Categorial Grammar.

The Clifford-circuit normal form of [4] defines a normal form for $n$-qubit Clifford operators, proves that every Clifford operator has a unique normal form, and presents a rewrite system reducing any circuit to that form, yielding a presentation by generators and relations. Its related-work section records the instructive negative case: Van den Nest's normal forms for Clifford circuits are not unique and therefore cannot ground an equational presentation, while Backens' completeness proof for the ZX-calculus does not yield a direct equational presentation because ZX expressions denote general linear maps rather than unitaries. Uniqueness is thus the property that makes a normal form usable for classification, which is why the STC confluence conjecture matters for the particle-correspondence program and not merely as a technicality.

The multi-qutrit extension [9] presents the first completeness result for any fragment of quantum circuits in odd prime dimensions: it generalizes Selinger's qubit normal form to qutrits, reduces every circuit to that form via a set of $380$ box relations, and then proves those box relations reducible to $18$ gate relations. The two-stage compression from many local relations to few gate relations illustrates how a normal-form theory's rule set can be audited and minimized, a step the STC rule set of Section 3.2 has not yet undergone.

The em-convex rewrite system [5] introduces a lambda-calculus-style system for dilation terms inspired by metric geometry, with constants for a node type $N$ and an edge type $E$ and dilations $\circ$ and $\bullet$, and explores what a convexity axiom forces on the infinitesimal operations. It is cited here as evidence that rewrite systems built from geometric or distinction-like primitives can sustain a full term calculus with typing rules, which supports the plausibility of the STC syntax rather than any specific STC claim.

The complexity analysis of precedence-terminating infinite graph rewrite systems [7] proves a criterion under which unfolding rewrite rules expressing safe recursion yield polynomial lengths of rewriting sequences and normal forms of polynomial size. Its method embeds rewriting sequences into descending sequences under a termination order, or alternatively uses numerical interpretations. This matters for STC enumeration: an upper bound on normal-form size as a function of input size is the quantity that determines whether enumeration to depth $n$ stays tractable, and [7] supplies the general technique for obtaining such bounds.

The EqSat comparison study [8] contrasts equality saturation, which grows an e-graph of equivalent programs under a rewrite rule set, against stochastic search over the same rules, across five benchmarks with fixed wall-clock budgets. For STC enumeration, EqSat offers an alternative to exhaustive generation: instead of enumerating all tokens and reducing each, one grows the equivalence class of a seed token under the rules and reads off irreducible members. This is recorded as a design option for the proposed experiment, not a result.

In the magnetic-bottle normal-form literature [11], normal forms for resonant Hamiltonians are constructed by a novel algorithm and the asymptotic behavior of the truncated series is studied; extending computations to high normalization order shows the remainder initially decreases with order $r$ before growing without bound, confirming the asymptotic character of the normalization. This is a cautionary analogue for STC: a normal-form correspondence observed at low depth (here, depth $\le 6$) may degrade at higher depth, and the depth-truncation sensitivity is listed as a limitation in Section 6.

Within the QNFO corpus, the STC research plan [12] frames the program as replacing continuous substance-based ontologies with a finite substrate of relational boundaries, and lists artifacts including a claimed formal proof of lexicographical depth decrease and global confluence (ARTIFACT_002) and a reduction engine proving $((M)) \rightarrow V$ (ARTIFACT_001). The confluence claim in that artifact is not reproduced or verified here; Section 3.3 states the confluence status that the present paper's own arguments support. The treatise on re-entrant distinctions [13] develops the thesis that the primitive act of distinction generates the constants $e$ and $\pi$ and the structure of quantum theory, and states an explicit falsifiability condition: if the formal system cannot derive $e^{i\pi} = -1$ without importing the real numbers and the exponential as external axioms, the claim of a purely logical derivation fails. That pattern — a derivation claim paired with a stated condition under which it fails — is the standard the present revision applies to the STC particle correspondence.

Finally, the prior version of this paper [14] is the object of the two corrections; its Result 4 and Section 3.3 statements are quoted and repaired in Sections 3.3, 4.4 and 5.

## 3. Methods

### 3.1 Syntax

The STC alphabet consists of two primitives:

1. The **mark** $\#$, representing the act of drawing a distinction.
2. The **enclosure** pair $[\,]$, which can be nested arbitrarily.

A **token** is any finite string generated by the grammar

$$
T ::= \# \;\mid\; [\,T\,] \;\mid\; TT .
$$

Concatenation is associative; juxtaposition denotes sequential composition. The empty token is written $\varepsilon$.

### 3.2 Reduction Rules

We define a rewrite system $\rightarrow$ on tokens by four rules:

1. **Crossing (annihilation).**
$$
[\,\#\,] \;\rightarrow\; \varepsilon
$$
A mark inside a single enclosure cancels the enclosure.

2. **Nesting collapse.**
$$
[\,[\,X\,]\,] \;\rightarrow\; [\,X\,]
$$
for any token $X$. Redundant double nesting is removed.

3. **Mark propagation.**
$$
\#\,[\,X\,] \;\rightarrow\; [\,\#\,X\,], \qquad [\,X\,]\,\# \;\rightarrow\; [\,X\,\#\,]
$$
A mark adjacent to an enclosure moves inward across it.

4. **Associative flattening.**
$$
[\,X\,]\,[\,Y\,] \;\rightarrow\; [\,X\,Y\,]
$$
Adjacent enclosures merge into a single enclosure.

All rules apply wherever their left-hand side appears as a sub-token. The rule set is the same four-rule set stated in the prior version [14]; no rule is added or removed in this revision, so all prior statements about the rule set carry over unchanged.

### 3.3 Termination and the Status of Confluence (Erratum pl-...-0)

**Termination (proven).** Define the measure $m(T) = (|T|,\, d_{\max}(T))$, where $|T|$ is the total symbol count of $T$ and $d_{\max}(T)$ is the maximal nesting depth, ordered lexicographically. Each rule strictly decreases $m$:

- Crossing removes two symbols ($[\,\#\,]$, three symbols, becomes $\varepsilon$, zero symbols), so $|T|$ drops by $3$.
- Nesting collapse removes one pair of brackets, so $|T|$ drops by $2$.
- Mark propagation leaves $|T|$ unchanged and strictly decreases $d_{\max}$, because the mark moves from outside an enclosure to inside it, reducing the depth of the outermost enclosing context by one at the position of the mark.
- Associative flattening removes one pair of brackets, so $|T|$ drops by $2$.

Since $(\mathbb{N} \times \mathbb{N}, <_{\mathrm{lex}})$ is well-founded, no infinite rewrite sequence exists; the system is strongly normalizing. This is the same lexicographic-measure pattern used to prove strong normalization for the associativity rule in [3], where the measure $\sigma x$ strictly decreases at each step, and it matches the layered termination structure of [1], in which a length-reducing rule group anchors the termination argument.

**Confluence (conjectured, not proven — this sentence corrects erratum pl-...-0).** The prior version stated, immediately after conceding that a critical-pair analysis was left for future work, that "the rewrite system is confluent, and every token possesses a unique normal form." That inference is invalid and is withdrawn. The corrected statement is:

> The STC rewrite system is strongly normalizing. Local confluence is **conjectured** on the basis of informal inspection of the overlapping left-hand sides of the four rules; a full critical-pair analysis has not been performed. Consequently, confluence and the uniqueness of normal forms are **not established** by this paper.

The route by which the conjecture would be closed is Newman's lemma, recorded as Lemma 3 of [3]: weak confluence together with strong normalization implies confluence. The proof obligation is therefore a case analysis showing that whenever two distinct rules apply to overlapping redexes in a token $T$, the two one-step reducts can be joined at a common reduct. The candidate critical pairs are: Crossing versus Nesting collapse on $[\,[\,\#\,]\,]$; Mark propagation versus Associative flattening on $\#\,[\,X\,][\,Y\,]$; and Mark propagation on both sides of $[\,X\,]\,\#\,[\,Y\,]$. Each pair appears joinable by inspection, but inspection is not a proof, and this paper claims none. Until the analysis is complete, all statements about "the" normal form of a token should be read as statements about *a* normal form reachable by some reduction strategy.

The practical consequence mirrors the Clifford-circuit literature: [4] proves uniqueness of its Clifford normal form and thereby obtains a generators-and-relations presentation, while the non-unique normal forms of Van den Nest, as reported in [4], cannot ground such a presentation. If STC confluence fails, the parity classification of Section 3.4 would need to be restated per strategy rather than per token, weakening any mapping onto particle multiplets.

### 3.4 Normal Form Classification

A token in normal form contains no reducible sub-token. Under the rules of Section 3.2, a normal form consists of a sequence of nested enclosures each possibly containing a mark, with no mark directly inside a single enclosure (otherwise Crossing applies) and no adjacent enclosures (otherwise Flattening applies). We denote a normal form by its **depth vector** $\mathbf{d} = (d_1, \dots, d_k)$, where $d_i$ is the nesting depth of the $i$-th mark.

We hypothesize that the parity invariant $\pi = \left(\sum_i d_i\right) \bmod 2$ is conserved under all reductions. The informal argument is that each rule changes the depth vector by amounts whose parity contribution cancels: Crossing deletes a mark at depth $d$ together with its enclosing context, removing an odd contribution $d$ but also merging or deleting neighboring enclosures; a formal proof is **not provided**, and the invariant is labeled a hypothesis. If it holds, it plays the role of a quantum number analogous to fermion/boson parity; if it fails, the classification scheme of Section 5 collapses to raw counts.

### 3.5 Enumeration Algorithm (Specification Only)

Given a maximal depth $n$, the algorithm is:

1. Generate all tokens of length up to $2n+1$ over the alphabet $\{\#, [\,]\}$ (the worst case is an alternating bracket string with a single mark).
2. Reduce each token to a normal form under the rules of Section 3.2.
3. Discard duplicate normal forms — valid as a deduplication step only if confluence holds; under the corrected status of Section 3.3, duplicates are instead recorded per reduction strategy and compared across strategies as an empirical confluence test.
4. Record the parity invariant $\pi$ of each irreducible form.

The generation step is $O(3^{2n+1})$ in the worst case (three choices per position), which for $n \le 6$ is bounded by $3^{13} \approx 1{,}594{,}323$ candidate strings, tractable on a modern workstation. **No enumeration was executed for this paper.** In particular, the counts previously reported in [14] as 42 irreducible normal forms at depth 5 (22 even, 20 odd) and 114 at depth 6 (68 even, 46 odd) are not derived by this paper, were not derived in Section 4 of [14], and are withdrawn as results; they are carried forward only as provisional hypotheses in Section 5.

## 4. Analysis

### 4.1 Benchmark from Multilingual Parsing Scores

The nine-language morpho-syntactic parsing score table below is carried over from the prior version [14]; it is an input of this revision, not an independently verified measurement, and it is used only as a reference performance level for any future STC-based parsing or classification system.

| Language   | MSLAS (%) |
|------------|-------|
| Czech      | 87.1 |
| English    | 83.8 |
| Hebrew     | 68.7 |
| Italian    | 73.0 |
| Polish     | 75.0 |
| Portuguese | 88.9 |
| Serbian    | 86.6 |
| Swedish    | 86.6 |
| Turkish    | 58.7 |

**Step 1:** Sum the nine percentages.

$$
\begin{aligned}
S &= 87.1 + 83.8 + 68.7 + 73.0 + 75.0 + 88.9 + 86.6 + 86.6 + 58.7 \\
  &= 170.9 + 68.7 + 73.0 + 75.0 + 88.9 + 86.6 + 86.6 + 58.7 \\
  &= 239.6 + 73.0 + 75.0 + 88.9 + 86.6 + 86.6 + 58.7 \\
  &= 312.6 + 75.0 + 88.9 + 86.6 + 86.6 + 58.7 \\
  &= 387.6 + 88.9 + 86.6 + 86.6 + 58.7 \\
  &= 476.5 + 86.6 + 86.6 + 58.7 \\
  &= 563.1 + 86.6 + 58.7 \\
  &= 649.7 + 58.7 \\
  &= 708.4 .
\end{aligned}
$$

**Step 2:** Divide by the number of languages $N = 9$.

$$
\overline{\mathrm{MSLAS}} = \frac{S}{N} = \frac{708.4}{9} = 78.711\ldots
$$

Rounded to one decimal place, the average is $78.7\%$. The prior version [14] states this matches the overall average reported in its parsing source; that cross-check is inherited from [14] and is not re-verified here.

### 4.2 Expected Noise Events in a Depth-5 Bruhat-Tits Tree

The simulation parameters below are carried over from the prior version [14], which attributes them to a non-Archimedean quantum-computer study; they are inputs of this revision.

- Tree depth $D = 5$ (binary tree).
- Gate time $t_g = 1\,\mathrm{ns}$.
- Per-vertex noise rate $r = 10^{-3}$ per ns.

**Step 1:** Number of vertices in a full binary tree of depth $D$:

$$
V = 2^{D+1} - 1 = 2^{6} - 1 = 64 - 1 = 63 .
$$

**Step 2:** Expected noise events per gate, under the assumption that each vertex contributes independently at rate $r$ during the gate time $t_g$:

$$
E = r \times t_g \times V = 10^{-3} \times 1 \times 63 = 0.063 .
$$

On this model, $0.063$ stochastic noise events occur on average during a single logical gate. The independence assumption is a limitation: correlated noise would change $E$, and the sensitivity is discussed in Section 6.

### 4.3 Error-Suppression Factor

The prior version [14] assumes a logical error rate per gate below $10^{-12}$ and a gate fidelity of $0.999999$, consistent with performance goals it attributes to its simulation source. Taking the raw per-gate noise expectation $p_{\mathrm{raw}} = 0.063$ from Section 4.2 and the assumed bound $p_{\mathrm{logical}} < 10^{-12}$, the suppression factor $S$ satisfies

$$
S > \frac{p_{\mathrm{raw}}}{p_{\mathrm{logical}}} > \frac{0.063}{10^{-12}} = 0.063 \times 10^{12} = 6.3 \times 10^{10}.
$$

The factor $6.3\times10^{10}$ is therefore a **conditional** bound: it holds if and only if the assumed logical error bound $p_{\mathrm{logical}} < 10^{-12}$ holds for the depth-5 tree architecture, which no experiment in this paper establishes.

### 4.4 Normal-Form Counts Are Not Derived (Erratum pl-...-1)

The prior version's Result 4 stated that enumeration up to depth 5 yields 42 irreducible normal forms (114 at depth 6) and that these were "derived directly from the inputs cited above or from elementary arithmetic shown in Section 4." Section 4 of [14] contains only the parsing average, the vertex count, the noise expectation, and the suppression factor; no arithmetic in it produces 42, 22, 20, 114, 68, or 46. The derivation claim is false and is withdrawn. The corrected status is:

- No normal-form count is derived in this paper.
- The values $42$ (depth 5) and $114$ (depth 6), with parity splits $22/20$ and $68/46$, are carried forward as **provisional hypotheses** to be tested by the enumeration experiment specified in Section 3.5 and Section 7.3.
- Any future derivation must show the generated token set, the reduction of each token, and the deduplication step explicitly, since under the conjectural confluence status of Section 3.3 the deduplication step is itself part of what the experiment tests.

## 5. Results

- **Result 1 (C3).** The average multilingual parsing score across the nine languages of the table in Section 4.1 is $78.7\%$ (arithmetic: $708.4 / 9 = 78.711\ldots$, Section 4.1).
- **Result 2 (C4).** Under the independent-Poisson noise model with the parameters of Section 4.2, the expected number of stochastic noise events per logical gate in a depth-5 Bruhat-Tits tree is $0.063$ (arithmetic: $10^{-3} \times 1 \times 63$, Section 4.2).
- **Result 3 (C5).** Conditional on the assumed logical error bound $p_{\mathrm{logical}} < 10^{-12}$, the error-suppression factor exceeds $6.3\times10^{10}$ (arithmetic: $0.063 / 10^{-12}$, Section 4.3).
- **Result 4 (C6, corrected).** No normal-form count is derived. The previously reported counts of 42 irreducible normal forms at depth 5 and 114 at depth 6 are withdrawn as underived results and restated as provisional hypotheses for the enumeration experiment (Section 4.4).
- **Result 5 (C1).** The STC rewrite system is strongly normalizing, with the lexicographic measure $m(T) = (|T|, d_{\max}(T))$ strictly decreasing under all four rules (Section 3.3). Confluence is conjectured, not proven.

## 6. Discussion

### 6.1 What the Corrected Claims Support

The three surviving quantitative results are bookkeeping, not physics: they establish that the STC program has concrete, cheaply checkable anchors (a parsing average, a noise expectation, a conditional suppression factor) and a termination guarantee that makes the proposed enumeration well-defined. The particle-correspondence claim — that stable normal forms of STC map onto elementary-particle multiplets — remains unestablished, and after the corrections it is weaker than before in two respects: uniqueness of normal forms is no longer claimed, and the depth-5/depth-6 counts are no longer claimed. What survives is a falsifiable experimental target.

### 6.2 Limitations

| Ass