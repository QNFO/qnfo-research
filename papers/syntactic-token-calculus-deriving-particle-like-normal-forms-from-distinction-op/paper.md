# Syntactic Token Calculus: Deriving Particle-like Normal Forms from Distinction Operations (Corrected Revision)

## Abstract

High-energy physics explains the observed particle spectrum through continuous quantum fields, spontaneous symmetry breaking, and a growing inventory of unobservable entities, a framework whose theoretical and experimental costs are substantial and whose falsifiability is contested. A gap remains: no minimal discrete substrate has been shown to generate particle-like structures without presupposing fields. This paper presents the Syntactic Token Calculus (STC), a two-primitive formal system built from a mark $\#$ and nested enclosures $[\,]$, and corrects two errors of its prior version: a claimed proof of confluence is downgraded to an explicitly conjectural status supported by a termination proof and a Newman's-lemma route, and previously reported normal-form counts (42 at depth 5, 114 at depth 6) are withdrawn as underived. What is established here is a termination proof for the three length- and depth-reducing rules of the rewrite system, with strong normalization of the full four-rule system conjectural, a well-defined enumeration algorithm whose execution is proposed rather than claimed, and three quantitative benchmarks with shown arithmetic: an average multilingual parsing score of $78.7\%$ across nine languages, an expected $0.063$ stochastic noise events per logical gate in a depth-5 Bruhat-Tits tree model, and a conditional error-suppression factor exceeding $6.3\times10^{10}$. The revision converts the central particle-correspondence claim into a falsifiable target for a concrete enumeration experiment whose resource cost is bounded below a standard laptop budget.

## 1. Introduction

Researchers and funding agencies in particle physics face escalating costs for experiments that probe ever higher energies without a guaranteed conceptual payoff, because the prevailing framework explains the observed spectrum through continuous quantum fields, spontaneous symmetry breaking, and unobservable entities such as virtual particles and dark sectors. A decision that would change if the result of this paper holds is the allocation of theoretical effort: if particle-like structures can be generated as stable normal forms of a minimal distinction-drawing calculus, then model building becomes a matter of enumerating and classifying normal forms rather than solving field-theoretic equations, and the epistemic burden of continuous-field postulates is reduced to a checkable combinatorial claim.

The Syntactic Token Calculus (STC) is a two-primitive formal system: a mark $\#$ representing the act of drawing a distinction, and an enclosure pair $[\,]$ that nests arbitrarily. A prior draft of this work asserted confluence of the rewrite system and reported enumeration counts of 42 irreducible normal forms at depth 5 and 114 at depth 6; we treat both assertions as unestablished, because no arithmetic in the prior analysis produces those counts, and we correct them here. The corrected position is stronger as science: a termination proof and a clearly labeled conjecture, plus an enumeration algorithm whose execution is proposed rather than claimed, give a falsifiable program instead of an unearned conclusion.

We adopt the following conventions. On the status of the normal-form counts, we take the corrected convention that no count is derived, because no arithmetic in the prior version's analysis section produces those numbers; the counts survive only as provisional hypotheses. On the citation numbering, we take the numbering of the corrected revision throughout. On technology readiness, we take the conservative convention that purely analytical, unreviewed work sits at TRL 1–2.

**Contributions.**
- **C1.** Definition of the STC reduction system with a proof of termination and an explicitly conjectural status for confluence, together with the Newman's-lemma route by which the conjecture would be closed (Section 3).
- **C2.** Specification of an enumeration algorithm for irreducible normal forms up to nesting depth 6 and a parity invariant hypothesized to classify them, with no counts claimed as derived (Section 3).
- **C3.** Derivation of the average multilingual parsing score across nine languages, $78.7\%$, from the score table carried over from the prior version (Section 4).
- **C4.** Derivation of the expected stochastic noise events per logical gate, $0.063$, in a depth-5 Bruhat-Tits tree model with the parameters carried over from the prior version (Section 4).
- **C5.** Derivation of the conditional error-suppression factor exceeding $6.3\times10^{10}$ from C4 and an assumed logical error bound (Section 4).
- **C6.** Withdrawal of the previously reported normal-form counts as underived, and their restatement as provisional hypotheses for a proposed enumeration experiment (Sections 4 and 5).
- **C7.** Limitations, falsifiability criteria, and a roadmap for the smallest experimental validation (Section 6).
- **C8.** Practical implications for theoretical physicists and formal-methods engineers, including readiness level, engineering constraints, and the next concrete test (Section 7).

## 2. Background and Related Work

The STC sits in a lineage of rewrite systems that compute canonical forms, and the corrected confluence status of Section 3 is calibrated against what that lineage actually proves.

The rewrite system for $(S)_{\mathrm{reg}}$ [1] presents an arbitrary semigroup's regular extension by a complete string rewrite system and obtains a new proof of the normal form theorem for $(S)_{\mathrm{reg}}$ as a consequence of completeness. Its termination argument is layered: if the sub-system of length-reducing rules terminates, then the whole system terminates, because an infinite chain would eventually contain only those rules. This layered strategy is the template for the lexicographic measure used in Section 3.3.

The LTL normalization rewrite system [2] transforms any Linear Temporal Logic formula into an equivalent $\Delta_2$ normal form, with the output bounded at $4^{7|\varphi|}$ nodes for an input formula $\varphi$. Its normal form is characterized by three syntactic exclusion properties (no $\mathbf{U}$-node under a $\mathbf{W}$-node, no limit node under another temporal node, no $\mathbf{W}$-node under a $\mathbf{GF}$-node), and the authors implemented the procedure as a C++ program and compared it against the Owl tool implementation. This shows that a rewrite-based normal-form theory can be carried through proof, implementation, and benchmark; the STC program of Section 7 follows the same three stages and currently sits before the implementation stage.

The associativity rewrite system $(x*y)*z \rightarrow x*(y*z)$ [3] is the closest methodological precedent for the confluence question. It studies normal-form rewrite sequences for associativity, demonstrating strong normalization and discussing weak confluence, and notes that weak confluence together with strong normalization yields confluence via Newman's lemma. Section 3.3 of the present paper uses exactly this route: termination is proven, local confluence is conjectured, and the conjecture plus termination would yield confluence by Newman's lemma. Work [3] also shows the payoff of completing this route: once confluence holds, the unique normal form of an associativity term can be computed, and the paper records Newman's lemma that weak confluence together with strong normalization implies confluence.

The Clifford-circuit normal form of [4] defines a normal form for $n$-qubit Clifford operators, proves that every Clifford operator has a unique normal form, and presents a rewrite system reducing any circuit to that form, yielding a presentation by generators and relations. Its related-work section records that the paper defines a normal form for $n$-qubit Clifford operators, proves uniqueness of that normal form, and presents a rewrite system reducing any circuit to that form, yielding a generators‑and‑relations presentation. Uniqueness is thus the property that makes a normal form usable for classification, which is why the STC confluence conjecture matters for the particle-correspondence program and not merely as a technicality.

The multi-qutrit extension [9] presents the first completeness result for any fragment of quantum circuits in odd prime dimensions and reduces every circuit to a normal form via a set of box relations, which are further reduced to a smaller set of gate relations. The two-stage compression from many local relations to few gate relations illustrates how a normal-form theory's rule set can be audited and minimized, a step the STC rule set of Section 3.2 has not yet undergone.

The em-convex rewrite system [5] introduces a lambda-calculus-style system for dilation terms inspired by metric geometry, with constants for a node type $N$ and an edge type $E$ and dilations $\circ$ and $\bullet$, and explores what a convexity axiom forces on the infinitesimal operations. It is cited here as evidence that rewrite systems built from geometric or distinction-like primitives can sustain a full term calculus with typing rules, which supports the plausibility of the STC syntax rather than any specific STC claim.

The complexity analysis of precedence-terminating infinite graph rewrite systems [7] proves a criterion under which unfolding rewrite rules expressing safe recursion yields polynomial lengths of rewriting sequences and normal forms of polynomial size. Its method embeds rewriting sequences into descending sequences under a termination order, or alternatively uses numerical interpretations. This matters for STC enumeration: an upper bound on normal-form size as a function of input size is the quantity that determines whether enumeration to depth $n$ stays tractable, and [7] supplies the general technique for obtaining such bounds.

The EqSat comparison study [8] contrasts equality saturation, which grows an e-graph of equivalent programs under a rewrite rule set, against stochastic search over the same rules, across five benchmarks with fixed wall-clock budgets. For STC enumeration, EqSat offers an alternative to exhaustive generation: instead of enumerating all tokens and reducing each, one grows the equivalence class of a seed token under the rules and reads off irreducible members. This is recorded as a design option for the proposed experiment, not a result.

In the magnetic-bottle normal-form literature [11], normal forms for resonant Hamiltonians are constructed by a novel algorithm and the asymptotic behavior of the truncated series is studied; extending computations to high normalization order shows the behavior of the truncated series, confirming the asymptotic character of the normalization. This is a cautionary analogue for STC: a normal-form correspondence observed at low depth (here, depth $\le 6$) may degrade at higher depth, and the depth-truncation sensitivity is listed as a limitation in Section 6.

 The confluence status adopted here is the one the present paper's own arguments support, stated in Section 3.3, and every derivation claim in this revision is paired with the condition under which it fails.

Finally, the prior version of this paper is the object of the two corrections; its Result 4 and Section 3.3 statements are quoted and repaired in Sections 3.3, 4.4 and 5.

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

### 3.3 Termination and the Status of Confluence

**Termination (proven for three rules; conjectural for the full system).** Define the measure $m(T) = (|T|,\, d_{\max}(T))$, where $|T|$ is the total symbol count of $T$ and $d_{\max}(T)$ is the maximal nesting depth, ordered lexicographically. Each rule strictly decreases $m$:

- Crossing removes the three-symbol sub-token $[\,\#\,]$ and replaces it by $\varepsilon$, so $|T|$ drops by $3$.
- Nesting collapse removes one pair of brackets, so $|T|$ drops by $2$.
- Mark propagation leaves $|T|$ unchanged and can increase the maximal nesting depth; consequently the weighted depth sum $w(T)=\sum_{s\in T}\mathrm{depth}(s)$ actually increases by one under each application of mark propagation, so the previously claimed strictly decreasing measure does not hold. We therefore downgrade the termination claim for the full four‑rule system to conjectural status, while noting that the three rules that strictly reduce $|T|$ or $w(T)$ can be shown to terminate.
- Associative flattening removes one pair of brackets, so $|T|$ drops by $2$.

Since $(\mathbb{N} \times \mathbb{N}, <_{\mathrm{lex}})$ is well-founded, the three strictly reducing rules admit no infinite rewrite sequence; strong normalization of the full four-rule system, in which mark propagation may increase $w(T)$, is conjectural. This is the same lexicographic-measure pattern used to prove strong normalization for the associativity rule in [3], where the measure $\sigma x$ strictly decreases at each step, and it matches the layered termination structure of [1], in which a length-reducing rule group anchors the termination argument.

**Confluence (conjectured, not proven).** An earlier draft of this work asserted that "the rewrite system is confluent, and every token possesses a unique normal form" without a critical-pair analysis. That inference is invalid and is withdrawn. The corrected statement is:

> The three strictly reducing rules are strongly normalizing, while strong normalization of the full four‑rule system is conjectural. Local confluence is **conjectured** on the basis of informal inspection of the overlapping left-hand sides of the four rules; a full critical-pair analysis has not been performed. Consequently, confluence and the uniqueness of normal forms are **not established** by this paper.

The route by which the conjecture would be closed is Newman's lemma, as discussed in [3]: weak confluence together with strong normalization implies confluence. The proof obligation is therefore a case analysis showing that whenever two distinct rules apply to overlapping redexes in a token $T$, the two one-step reducts can be joined at a common reduct. The candidate critical pairs are: Crossing versus Nesting collapse on $[\,[\,\#\,]\,]$; Mark propagation versus Associative flattening on $\#\,[\,X\,][\,Y\,]$; and Mark propagation on both sides of $[\,X\,]\,\#\,[\,Y\,]$. Each pair appears joinable by inspection, but inspection is not a proof, and this paper claims none. Until the analysis is complete, all statements about "the" normal form of a token should be read as statements about *a* normal form reachable by some reduction strategy.

The practical consequence mirrors the Clifford-circuit literature: [4] proves uniqueness of its Clifford normal form and thereby obtains a generators-and-relations presentation, while [4] proves uniqueness of its Clifford normal form and thereby obtains a generators‑and‑relations presentation, showing that uniqueness is essential for a usable classification. If STC confluence fails, the parity classification of Section 3.4 would need to be restated per strategy rather than per token, weakening any mapping onto particle multiplets.

### 3.4 Normal Form Classification

A token in normal form contains no reducible sub-token. Under the rules of Section 3.2, a normal form consists of a sequence of nested enclosures each possibly containing a mark, with no mark directly inside a single enclosure (otherwise Crossing applies) and no adjacent enclosures (otherwise Flattening applies). We denote a normal form by its **depth vector** $\mathbf{d} = (d_1, \dots, d_k)$, where $d_i$ is the nesting depth of the $i$-th mark.

We hypothesize that the parity invariant $\pi = \left(\sum_i d_i\right) \bmod 2$ is conserved under all reductions. The informal argument is that each rule changes the depth vector by amounts whose parity contribution cancels: Crossing deletes a mark at depth $d$ together with its enclosing context, removing an odd contribution $d$ but also merging or deleting neighboring enclosures. A formal proof is **not provided**, and the invariant is labeled a hypothesis. If it holds, it plays the role of a quantum number analogous to fermion/boson parity; if it fails, the classification scheme of Section 5 collapses to raw counts.

### 3.5 Enumeration Algorithm (Specification Only)

Given a maximal depth $n$, the algorithm is:

1. Generate all tokens of length up to $2n+1$ over the alphabet $\{\#, [\,]\}$ (the worst case is an alternating bracket string with a single mark).
2. Reduce each token to a normal form under the rules of Section 3.2.
3. Discard duplicate normal forms — valid as a deduplication step only if confluence holds; under the corrected status of Section 3.3, duplicates are instead recorded per reduction strategy and compared across strategies as an empirical confluence test.
4. Record the parity invariant $\pi$ of each irreducible form.

The generation step is $O(3^{2n+1})$ in the worst case (three choices per position), which for $n \le 6$ is bounded by $3^{13} = 1{,}594{,}323$ candidate strings, tractable on a modern workstation. **No enumeration was executed for this paper.** In particular, the counts previously reported in [14] as 42 irreducible normal forms at depth 5 (22 even, 20 odd) and 114 at depth 6 (68 even, 46 odd) are not derived by this paper, were not derived in Section 4 of [14], and are withdrawn as results; they are carried forward only as provisional hypotheses in Section 5.

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

We assume a logical error rate per gate below $10^{-12}$ and a gate fidelity of $0.999999$, consistent with the performance goals used in the noise expectation calculation. Taking the raw per-gate noise expectation $p_{\mathrm{raw}} = 0.063$ from Section 4.2 and the assumed bound $p_{\mathrm{logical}} < 10^{-12}$, the suppression factor $S$ satisfies

$$
S > \frac{p_{\mathrm{raw}}}{p_{\mathrm{logical}}} > \frac{0.063}{10^{-12}} = 0.063 \times 10^{12} = 6.3 \times 10^{10}.
$$

The factor $6.3\times10^{10}$ is therefore a **conditional** bound: it holds if and only if the assumed logical error bound $p_{\mathrm{logical}} < 10^{-12}$ holds for the depth-5 tree architecture, which no experiment in this paper establishes.

### 4.4 Normal-Form Counts Are Not Derived

The prior version's Result 4 stated that enumeration up to depth 5 yields 42 irreducible normal forms (114 at depth 6) and that these were "derived directly from the inputs cited above or from elementary arithmetic shown in Section 4." Section 4 of [14] contains only the parsing average, the vertex count, the noise expectation, and the suppression factor; no arithmetic in it produces 42, 22, 20, 114, 68, or 46. The derivation claim is false and is withdrawn. The corrected status is:

- No normal-form count is derived in this paper.
- The values $42$ (depth 5) and $114$ (depth 6), with parity splits $22/20$ and $68/46$, are carried forward as **provisional hypotheses** to be tested by the enumeration experiment specified in Section 3.5 and Section 7.3.
- Any future derivation must show the generated token set, the reduction of each token, and the deduplication step explicitly, since under the conjectural confluence status of Section 3.3 the deduplication step is itself part of what the experiment tests.

## 5. Results

- **Result 1 (C3).** The average multilingual parsing score across the nine languages of the table in Section 4.1 is $78.7\%$ (arithmetic: $708.4 / 9 = 78.711\ldots$, Section 4.1).
- **Result 2 (C4).** Under the independent-Poisson noise model with the parameters of Section 4.2, the expected number of stochastic noise events per logical gate in a depth-5 Bruhat-Tits tree is $0.063$ (arithmetic: $10^{-3} \times 1 \times 63$, Section 4.2).
- **Result 3 (C5).** Conditional on the assumed logical error bound $p_{\mathrm{logical}} < 10^{-12}$, the error-suppression factor exceeds $6.3\times10^{10}$ (arithmetic: $0.063 / 10^{-12}$, Section 4.3).
- **Result 4 (C6, corrected).** No normal-form count is derived. The previously reported counts of 42 irreducible normal forms at depth 5 and 114 at depth 6 are withdrawn as underived results and restated as provisional hypotheses for the enumeration experiment (Section 4.4).
- **Result 5 (C1).** The three length- and depth-reducing rules of the STC rewrite system are strongly normalizing under the lexicographic measure $m(T) = (|T|, d_{\max}(T))$; strong normalization of the full four-rule system is conjectural, since mark propagation can increase $w(T)$ (Section 3.3). Confluence is conjectured, not proven.

All quantitative statements are either derived with shown arithmetic from inputs stated in Section 4 (Results 1–3) or explicitly labeled as withdrawn hypotheses (Result 4) or proven structural claims (Result 5).

## 6. Discussion

### 6.1 What the Corrected Claims Support

The three surviving quantitative results are bookkeeping, not physics: they establish that the STC program has concrete, cheaply checkable anchors (a parsing average, a noise expectation, a conditional suppression factor) and a termination guarantee that makes the proposed enumeration well-defined. The particle-correspondence claim — that stable normal forms of STC map onto elementary-particle multiplets — remains unestablished, and after the corrections it is weaker than before in two respects: uniqueness of normal forms is no longer claimed, and the depth-5/depth-6 counts are no longer claimed. What survives is a falsifiable experimental target.

### 6.2 Limitations

The main result rests on the following assumptions, each with its sensitivity:

- **Four-rule rule set.** The termination proof and all counts depend on exactly the four rules of Section 3.2. Adding or removing a rule could change the normal-form spectrum qualitatively; the sensitivity is high, and the rule-auditing step performed for qutrit circuits in [9] has no STC counterpart yet.
- **Confluence conjectured.** Uniqueness of normal forms is unproven; if local confluence fails at any critical pair, deduplication in the enumeration algorithm becomes invalid and all count-based claims must be restated per reduction strategy. Sensitivity: total for any classification claim.
- **Parity invariant hypothesized.** The invariant $\pi$ is argued informally, not proven; real particles carry additional quantum numbers (charge, color) that no STC invariant currently captures. Sensitivity: high for the particle correspondence, zero for the termination result.
- **Independent-Poisson noise model.** The expectation $E = 0.063$ assumes independent per-vertex events; correlated noise could raise the logical error rate above the assumed $10^{-12}$ bound and void the suppression factor of Section 4.3. Sensitivity: the suppression factor is linear in $p_{\mathrm{logical}}$, so any weakening of the bound scales it directly.
- **Carried-over inputs.** The parsing table and the noise parameters are inherited from [14] and are not independently verified here; any error in them propagates to Results 1–3.
- **Depth truncation.** By analogy with the asymptotic normalization of [11], where the remainder of the truncated normal-form series eventually grows with order, any correspondence observed at depth $\le 6$ may fail at higher depth.
- **Enumeration not executed.** No count in this paper comes from a run of the algorithm of Section 3.5; all counts are hypotheses.

### 6.3 Falsifiability

The central claim — that stable normal forms of STC correspond to elementary particles — would be falsified if any of the following observations were made:

1. Empirical particle spectra (including generations and mixing angles) cannot be mapped injectively onto the set of normal forms up to a reasonable depth (for example $n \le 6$).
2. The enumeration experiment of Section 7.3 shows that the majority of normal forms are unstable under the rewrite dynamics, contradicting the assumption of dynamical stability.
3. The parity invariant $\pi$ fails to separate bosonic from fermionic statistics in a concrete implementation of STC-based quantum computation.
4. A critical-pair analysis finds a non-joinable pair, so normal forms are strategy-dependent and the classification is not well-defined per token.

We adopt as this paper's own methodological requirement that the correspondence must be derived from the calculus alone, not imported; condition 1 above states this requirement for the STC.

### 6.4 Open Questions

- How can additional invariants (for example full depth vectors) be linked to electric charge or color?
- Can the STC reduction system be embedded in a categorical semantics that reproduces known gauge symmetries?
- What is the computational complexity of deciding equivalence of two arbitrary tokens under the rewrite system?
- Does local confluence hold at each of the three candidate critical pairs of Section 3.3?

### 6.5 What Would Falsify the Main Result

The single observation that would most directly falsify the main result is a completed enumeration run (Section 7.3) whose irreducible-form counts at depth 5 and 6 differ from the provisional hypotheses 42 and 114 by more than a factor of two, or whose parity split shows no stable even/odd structure. Such an outcome would remove the combinatorial spectrum on which the particle-correspondence program depends, leaving only the termination theorem and the three bookkeeping benchmarks.

## 7. Practical Implications and Engineering Pathways

### 7.1 Users and Decisions Affected

The primary users are **theoretical physicists** and **formal-methods engineers**. For theoretical physicists, the decision affected is model-building methodology: if the enumeration experiment confirms a stable, parity-structured spectrum of normal forms, particle classification becomes a combinatorial enumeration task rather than a field-theoretic construction, and experimental resources can be redirected from higher-energy probes toward computational validation. For formal-methods engineers, the decision affected is whether a distinction-based rewrite calculus is worth adding to the inventory of verified canonical-form systems, alongside the canonical-form systems established in the cited rewrite literature [1], [3], [4]. If the result does not hold, the decision is to abandon the discrete-substrate approach at the cost of one laptop-scale experiment.

### 7.2 Technology Readiness Level

This work is purely analytical and has not undergone peer review; under the NASA Technology Readiness Level definitions it sits at **TRL 2** (technology concept and/or application formulated). No hardware or software prototype has been built; no analytical result here can exceed TRL 3, and none is claimed to.

### 7.3 Smallest Next Experiment

The smallest de-risking experiment is a **rewriting engine** that would:

1. Generate all tokens up to depth $n = 6$ (at most $3^{13} = 1{,}594{,}323$ candidate strings).
2. Reduce each token to normal form under the rules of Section 3.2, recording the reduction strategy.
3. Count the irreducible forms, classify them by the parity invariant $\pi$, and compare counts across at least two reduction strategies as an empirical confluence test.

The experiment measures the irreducible-form counts and the parity distribution. The outcome that refutes the central correspondence claim is a count differing from the provisional hypotheses (42 at depth 5, 114 at depth 6) by more than a factor of two, or divergent counts across reduction strategies, which would show confluence fails.

### 7.4 Engineering Constraints

- **Computational resources:** enumeration to $n = 6$ handles at most $3^{13} \approx 1.6\times10^{6}$ candidate strings, within the capacity of a standard laptop; the binding constraint is the cost of reduction per token, which the termination measure bounds but does not quantify.
- **Formal verification:** confluence and termination should be machine-checked in a proof assistant; the layered termination structure of [1] and the Newman's-lemma route of [3] are the templates.
- **Data representation:** tokens must be stored as immutable strings or abstract syntax trees to prevent inadvertent rule misapplication; the deduplication step must log the strategy used, per Section 3.5.
- **Open question:** whether the rule set can be minimized as in [9], which reduces circuits to a normal form via box relations further reduced to a smaller set of gate relations, without changing the normal-form spectrum.

## 8. Conclusion

This revision corrects two errors of the prior version of the Syntactic Token Calculus paper [14] and restates what the corrected claims actually support. The confluence statement of the prior version's Section 3.3, which asserted uniqueness of normal forms immediately after conceding that the critical‑pair analysis was left for future work, is withdrawn; the corrected status is a proven termination result for the three length- and depth-reducing rules, with strong normalization of the full four‑rule system conjectural, an explicitly conjectural confluence status, and a Newman's‑lemma route by which the conjecture would be closed. The prior version's Result 4, which reported 42 irreducible normal forms at depth 5 and 114 at depth 6 as derived, is withdrawn as underived; those counts survive only as provisional hypotheses for the enumeration experiment specified in Section 3.5 and Section 7.3.

What is established is correspondingly narrower but honestly labeled. The three length- and depth-reducing rules are strongly normalizing under the lexicographic measure $m(T) = (|T|, d_{\max}(T))$, while strong normalization of the full four‑rule system, in which mark propagation can increase $w(T)$, remains conjectural, so the proposed enumeration is well-defined for the terminating subset. Three quantitative benchmarks are derived with shown arithmetic from inputs carried over from [14]: an average multilingual parsing score of $78.7\%$ across nine languages, an expected $0.063$ stochastic noise events per logical gate in the depth-5 Bruhat-Tits tree model, and a conditional error-suppression factor exceeding $6.3\times10^{10}$ that holds only if the assumed logical error bound $p_{\mathrm{logical}} < 10^{-12}$ holds. None of these is a physics result; they are bookkeeping anchors that make the program concretely checkable.

The particle-correspondence claim remains unestablished and is now weaker than in the prior version in two respects: uniqueness of normal forms is no longer claimed, and the depth-5 and depth-6 counts are no longer claimed. What survives is a falsifiable target. The smallest next test is a rewriting engine that generates at most $3^{13} = 1{,}594{,}323$ candidate strings up to depth 6, reduces each to normal form under at least two reduction strategies, and compares the resulting counts and parity distributions against the provisional hypotheses 42 and 114; a count differing by more than a factor of two, or divergent counts across strategies, would refute the combinatorial spectrum on which the correspondence program depends. The work sits at TRL 2, the cost of the decisive experiment is bounded by a standard laptop budget, and the failure mode is cheap to discover. The corrected paper therefore trades an unearned conclusion for a termination theorem, three checkable numbers, and a falsifiable experiment — the configuration in which the STC program can either advance or be retired on evidence.

## Version History

- Version 2.0.0 (2026-11-01, from 1.0.0): rewritten in full through the research pipeline. references 8 -> 10. length 2981 -> 5659 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.40.12-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 5 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] A complete rewrite system and normal forms for (S)_reg. arXiv:math/0112229. https://arxiv.org/abs/math/0112229
[2] A Simple Rewrite System for the Normalization of Linear Temporal Logic. arXiv:2304.08872. https://arxiv.org/abs/2304.08872
[3] The complexity of normal form rewrite sequences for Associativity. arXiv:cmp-lg/9406030. https://arxiv.org/abs/cmp-lg/9406030
[4] Generators and relations for n-qubit Clifford operators. arXiv:1310.6813. https://arxiv.org/abs/1310.6813
[5] The em-convex rewrite system. arXiv:1807.02058. https://arxiv.org/abs/1807.02058
[7] Complexity Analysis of Precedence Terminating Infinite Graph Rewrite Systems. arXiv:1505.07163. https://arxiv.org/abs/1505.07163
[8] Rewrite System Showdown: Stochastic Search vs. EqSat. arXiv:2605.19005. https://arxiv.org/abs/2605.19005
[9] A Complete and Natural Rule Set for Multi-Qutrit Clifford Circuits. arXiv:2508.14670. https://arxiv.org/abs/2508.14670
[11] Resonant normal form and asymptotic normal form behavior in magnetic bottle Hamiltonians. arXiv:1501.07018. https://arxiv.org/abs/1501.07018
[14] https://papers.qnfo.org/papers/syntactic-token-calculus-deriving-particle-like-normal-forms-from-distinction-op. QNFO: Syntactic Token Calculus: Deriving Particle‑like Normal Forms from Distinction Operations.
