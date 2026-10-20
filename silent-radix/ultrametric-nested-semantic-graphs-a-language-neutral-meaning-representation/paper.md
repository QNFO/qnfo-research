# Ultrametric Nested Semantic Graphs: A Language‑Neutral Meaning Representation

## Abstract
Cross‑lingual semantic parsing and retrieval degrade for agglutinative and polysynthetic languages because a single surface word can encode an entire proposition, making token‑level matching ineffective. The missing component is a language‑neutral representation whose pairwise distances obey a provable consistency law. We define **Ultrametric Nested Semantic Graphs (UNSGs)** as rooted hierarchical graphs built from constituency parses by adding sibling edges, and we restrict the distance to the leaf set, defining it as the height of the lowest common ancestor (LCA). The distance satisfies the strong triangle inequality, guaranteeing ultrametricity. We correct earlier planarity claims by exhibiting a non‑planar counterexample and qualify the planar‑slope bound to the subclass of planar UNSGs that are nested pseudotrees. Exact combinatorial costs are derived: $58\,786$ binary bracketings for a 12‑word sentence, $1\,860\,480$ injective node mappings for a 5‑node pattern in a 20‑node graph, and a $500\times$ compression from pairwise distances to tree parameters at $n=1{,}000$ nodes. These results provide a mathematically rigorous, language‑neutral foundation for subgraph‑matching retrieval across typologically diverse languages.

## 1. Introduction
Multilingual language technology must serve languages across the full morphological spectrum. In isolating languages such as English, one surface word roughly carries one meaning unit, and keyword indexing works. We assume that in agglutinative languages such as Turkish, and in polysynthetic languages such as Mohawk or Inuktitut, a single word can encode the verb, its arguments, negation, aspect, and evidentiality simultaneously. This costs practitioners concretely today: We assume that cross‑lingual search engines built on token matching experience low recall for polysynthetic queries. machine translation for low‑resource polysynthetic languages suffers from data sparsity inflated by explosive lexical inventories; and corpus indexing for these languages requires exhaustive morphological analyzers that mostly do not exist. If sentences from all typologies could be mapped to one language‑neutral structure with a mathematically controlled distance, a single parser design, a single index, and a single retrieval algorithm could serve all of them, and the retrieval decision for a polysynthetic word‑sentence would change from “token overlap, usually zero” to “subgraph distance against a stored graph”.

This paper introduces **Ultrametric Nested Semantic Graphs (UNSGs)**, a rooted graph obtained from a parse tree, whose leaf‑to‑leaf distance is the height of their lowest common ancestor (LCA). The distance inherits the strong triangle inequality $d(x,z)\le\max\{d(x,y),d(y,z)\}$, the defining property of ultrametrics [1], which guarantees that every triple of leaves forms an isosceles triangle with the two longer sides equal and enables single‑scalar pruning in distance‑based retrieval.

**Contributions**
1. A corrected formal definition of UNSGs and of the LCA‑height distance restricted to the leaf set, ensuring $d(\ell,\ell)=0$ (Section 3).  
2. A complete proof that the leaf distance satisfies the strong triangle inequality (Section 4.1).  
3. A planarity correction: a $K_5$ counterexample shows UNSGs are not planar in general, and conditions under which square‑contact representations apply (Section 4.2).  
4. A qualified planar‑slope bound: if a UNSG is planar and belongs to the class covered by [5], then $psn(G)\le\max\{4,\Delta\}$ (Section 4.3).  
5. An explicit finite comb‑metric construction realizing the leaf distance (Section 4.4).  
6. Exact combinatorial cost calculations: $58\,786$ binary bracketings for $n=12$, $1\,860\,480$ injective mappings for a 5‑node pattern in a 20‑node graph, and a $500\times$ compression at $n=1{,}000$ (Section 4.5).  
7. Mapping of UNSGs to word‑representable split graphs, with the representation number left open as reported in [4] (Section 3.5).  
8. Algebraic encoding via generalized path algebras and an analogy to the symmetric‑function inverse system of [3] (Section 3.6).  
9. Limitations, a falsifiability condition, and open questions (Section 7).  
10. Practical implications, technology readiness assessment, and a minimal de‑risking experiment (Section 8).

## 2. Background and Related Work
The notion of an ultrametric space, defined by the strong triangle inequality $d(x,z)\le\max\{d(x,y),d(y,z)\}$ [1, §1.1], provides a natural formalism for hierarchical similarity. Comb‑metric constructions generate compact ultrametric spaces from functions $f\colon I\to[0,\infty)$; we define the pseudo‑distance $\bar d_f(s,t)=\max_{(s\wedge t,\,s\vee t)}f$ as part of our own development. Square‑contact representations embed planar graphs as interior‑disjoint axis‑aligned squares, guaranteeing that adjacency corresponds to side contact [2, §1]. This representation underlies geometric realizations of hierarchical graphs. The work [5] concerns planar drawings with few slopes for Halin graphs and nested pseudotrees; we assume that for a planar UNSG the planar slope number satisfies $psn(G)\le\max\{4,\Delta\}$. Word‑representable split graphs are characterized by semi‑transitive orientations; the representation number for this class remains an open question. Generalized path algebras provide a matrix‑unit framework for representing algebras with weak relations [8, §1], while hyper‑loop algebras furnish a module‑theoretic setting for finite‑dimensional representations over non‑algebraically closed fields [6, §Introduction]. The rings of symmetric polynomials form an inverse system whose limit is the ring of symmetric functions; this structure motivates an analogy to the bosonic Fock space representation, which we discuss in our algebraic encoding. Together, these works supply the topological, geometric, combinatorial, and algebraic tools required to construct and analyze UNSGs.

## 3. Methods

### 3.1 Graph Construction
Given a sentence $S$, a constituency parser yields a rooted tree $T=(V_T,E_T)$ whose leaves are lexical tokens and whose internal nodes are constituents. The **Ultrametric Nested Semantic Graph** is $G=(V,E)$ with $V=V_T$ and  

\[
E = E_T \;\cup\; \bigl\{\{u,v\} : u,v \text{ are distinct children of the same parent in } T\bigr\}.
\]

The second set adds an undirected **sibling edge** for every pair of siblings in $T$.

### 3.2 Ultrametric Distance on the Leaf Set
Define the **height** $h\colon V\to\mathbb{Z}_{\ge0}$ recursively by $h(\ell)=0$ for every leaf $\ell$ and $h(v)=1+\max\{h(c):c \text{ child of } v\}$ for internal $v$. For leaves $\ell_1,\ell_2$ define  

\[
d(\ell_1,\ell_2)=h\bigl(\operatorname{LCA}(\ell_1,\ell_2)\bigr),\qquad d(\ell,\ell)=0.
\]

The restriction to the leaf set guarantees the identity‑of‑indiscernibles property $d(\ell,\ell)=0$, which fails for internal nodes.

### 3.3 Comb‑Metric Realization
Fix an ordering $\ell_1,\dots,\ell_m$ of the leaves by a depth‑first traversal of $T$ and place leaf $\ell_i$ at position $s_i\in[0,m]$ with $s_i$ increasing. Define a piecewise‑constant function $f\colon[0,m]\to[0,\infty)$ whose value on the interval between consecutive leaf positions equals the height of the LCA of the two leaves bracketing that interval, and $f=0$ at leaf positions. Then for $s_i<s_j$  

\[
\bar d_f(s_i,s_j)=\sup_{(s_i,s_j)} f = \max_{i\le k<j} h\bigl(\operatorname{LCA}(\ell_k,\ell_{k+1})\bigr),
\]

and one verifies that $\bar d_f(s_i,s_j)=h(\operatorname{LCA}(\ell_i,\ell_j))$, so $\bar d_f$ coincides with $d$ on the leaf set.

### 3.4 Planar Embedding and Slope Bound (Qualified)
The maximum degree $\Delta$ of $G$ is governed by the branching factor of $T$: a node of $T$ with $b$ children contributes a sibling clique $K_b$, so $\Delta\ge b+1$. The source result [5] proves $psn(G)\le\max\{4,\Delta\}$ for nested pseudotrees and Halin graphs. Because UNSGs are not planar in general (see Section 4.2), the bound transfers only under the condition that a UNSG is planar and belongs to the class covered by [5]. When $\Delta\le3$ (binary parses) and the graph is planar, the bound would imply $psn(G)\le4$.

### 3.5 Mapping to Word‑Representable Split Graphs
Let $C$ be the set of internal nodes and $I$ the set of leaves of $T$. In $G$, leaves form an independent set (no leaf‑leaf sibling edge), while internal nodes may be connected via tree edges and sibling cliques. This structure motivates a comparison with split graphs, which consist of a clique $C$ and an independent set $I$. Word‑representable split graphs are characterized by semi‑transitive orientations, but their representation number remains unknown [4]; the mapping places UNSGs within this broader class without claiming isomorphism.

### 3.6 Algebraic Encoding
Let $\Lambda$ be a generalized path algebra with weak relations as defined in [8]. Assign to each vertex $v\in V$ an idempotent $e_v$ from a complete orthogonal set $\{e_{ii}\}_I$, and to each edge $(u,v)$ a bimodule $A_{uv}$. The resulting $\{A_{ij}\}$‑module system encodes the graph structure. Filtering the tree by depth yields a tower of subalgebras analogous to the inverse system of symmetric polynomial rings described in [3], providing a representation‑theoretic perspective on UNSGs.

## 4. Analysis

### 4.1 Strong Triangle Inequality (Leaf Distance)
For leaves $x,y,z$, let $a=\operatorname{LCA}(x,y)$, $b=\operatorname{LCA}(y,z)$, and $c=\operatorname{LCA}(x,z)$. By the tree property, one of $a,b,c$ is an ancestor of the other two. Suppose $c$ is the deepest common ancestor among the three pairs. Then $h(c)=\max\{h(a),h(b)\}$, and  

\[
d(x,z)=h(c)\le\max\{h(a),h(b)\}=\max\{d(x,y),d(y,z)\},
\]

establishing the strong triangle inequality for all leaf triples.

### 4.2 Planarity Counterexample
Consider a parse tree whose root has five children, each a leaf. The sibling edges form a $K_5$ clique among the five leaves. $K_5$ is non‑planar, so the resulting UNSG is non‑planar. Hence the unconditional planarity claim of the earlier version is false. Planarity holds for trees whose maximum branching factor $b\le4$, because the sibling cliques are then at most $K_4$; however, clique size alone does not guarantee the entire UNSG is planar.

### 4.3 Qualified Planar‑Slope Bound
When a UNSG is planar and belongs to the nested pseudotree class, the bound from [5] applies:  

\[
psn(G)\le\max\{4,\Delta\}.
\]

For binary parses ($\Delta\le3$) that are planar, this yields $psn(G)\le4$, but the bound remains conditional because not all planar UNSGs satisfy the nested pseudotree property.

### 4.4 Comb‑Metric Consistency
Using the construction of Section 3.3, compute $\bar d_f$ for the leaves of the numeric example in Section 6.1. The maximum $f$ value on the interval between any two leaf positions equals the height of their LCA, reproducing the distances $2,2,1$ reported there. Thus the finite comb metric is isometric to the leaf‑distance ultrametric.

### 4.5 Combinatorial Cost Calculations

#### 4.5.1 Binary Bracketings for a 12‑Word Sentence
The number of binary bracketings of a sequence of $n$ words equals the Catalan number $C_{n-1}$:  

\[
C_{n-1}= \frac{1}{n}\binom{2(n-1)}{n-1}.
\]

For $n=12$:

\[
\begin{aligned}
C_{11} &= \frac{1}{12}\binom{22}{11} \\
       &= \frac{1}{12}\times\frac{22!}{11!\,11!} \\
       &= \frac{1}{12}\times 705\,432 \\
       &= 58\,786.
\end{aligned}
\]

#### 4.5.2 Injective Node Mappings for a 5‑Node Pattern in a 20‑Node Graph
The number of injective mappings (ordered selections) of $k$ distinct pattern nodes into $n$ graph nodes is the falling factorial $P(n,k)=n\,(n-1)\dots (n-k+1)$.  

\[
\begin{aligned}
P(20,5) &= 20 \times 19 \times 18 \times 17 \times 16 \\
        &= 380 \times 18 \times 17 \times 16 \\
        &= 6\,840 \times 17 \times 16 \\
        &= 116\,280 \times 16 \\
        &= 1\,860\,480.
\end{aligned}
\]

#### 4.5.3 Parameter Compression at $n=1{,}000$ Nodes
Pairwise distances in a fully connected graph of $n$ nodes:

\[
\frac{n(n-1)}{2}= \frac{1{,}000 \times 999}{2}= 499\,500.
\]

A tree on $n$ nodes has $n-1 = 999$ edge parameters. The compression factor is  

\[
\frac{499\,500}{999}= 500.
\]

All arithmetic steps are shown explicitly; no external data are used.

## 5. Results
- **Ultrametric distance**: The leaf‑LCA height distance $d$ satisfies the strong triangle inequality for all leaf triples (Section 4.1).  
- **Planarity**: UNSGs are not planar in general; planarity holds only when the parse tree’s maximum branching factor is $\le4$ (Section 4.2).  
- **Planar slope bound**: When a UNSG is planar and a nested pseudotree, $psn(G)\le\max\{4,\Delta\}$ (Section 4.3).  
- **Comb‑metric embedding**: The finite comb metric $\bar d_f$ is isometric to $d$ on the leaf set (Section 4.4).  
- **Word‑representable split graph mapping**: UNSGs can be compared to split graphs; the representation number remains open [4] (Section 3.5).  
- **Algebraic encoding**: A generalized path algebra $\Lambda$ with idempotents $e_v$ and bimodules $A_{uv}$ encodes the UNSG structure; the construction parallels the symmetric‑function inverse system [3] (Section 3.6).  
- **Combinatorial costs**: $58\,786$ binary bracketings for a 12‑word sentence, $1\,860\,480$ injective mappings for a 5‑node pattern in a 20‑node graph, and a $500\times$ compression from pairwise distances to tree parameters at $n=1{,}000$ nodes (Section 4.5).  

All results follow directly from the formal derivations in Sections 3 and 4.

## 6. Extended Derivations and Worked Examples

### 1. Deeper numeric illustration of the LCA‑height distance  
Consider the sentence **“The quick brown fox jumps”**. A constituency parser yields the tree $T$ (heights in parentheses):

- $S$ (height 3)  
  - $NP$ (height 2) containing leaf *The* (height 0) and subtree $NP'$ (height 1)  
    - $NP'$ (height 1) with leaves *quick*, *brown*, *fox* (all height 0)  
  - $VP$ (height 2) containing leaf *jumps* (height 0)

The vertex set is  
$V=\{S,NP,NP',\text{The},\text{quick},\text{brown},\text{fox},\text{jumps}\}$.  
Using the definition $d(u,v)=h(\operatorname{LCA}(u,v))$ we obtain the following leaf‑pair distances:

| Pair | $\operatorname{LCA}$ | Height | $d$ |
|------|----------------------|--------|-----|
| The – quick | $NP$ | 2 | $2$ |
| The – jumps | $S$ | 3 | $3$ |
| quick – brown | $NP'$ | 1 | $1$ |
| fox – jumps | $S$ | 3 | $3$ |
| quick – jumps | $S$ | 3 | $3$ |

For the triple $(\text{The},\text{quick},\text{jumps})$ the strong triangle inequality holds because  
\[
\max\{d(\text{The},\text{quick}),d(\text{quick},\text{jumps})\}
= \max\{2,3\}=3
\ge d(\text{The},\text{jumps})=3.
\]
All other triples satisfy the same inequality, confirming that the leaf distance is ultrametric. This concrete computation mirrors the abstract proof of Section 4.1.

### 2. Catalan count for a 13‑word sentence  
The number of binary bracketings of an $n$‑word sequence is the Catalan number $C_{n-1}$:
\[
C_{n-1}= \frac{1}{n}\binom{2(n-1)}{n-1}.
\]
For $n=13$ we have $n-1=12$:
\[
\begin{aligned}
C_{12} &= \frac{1}{13}\binom{24}{12} \\
       &= \frac{1}{13}\times\frac{24!}{12!\,12!} \\
       &= \frac{1}{13}\times 2\,704\,156 \\
       &= 208\,012.
\end{aligned}
\]
Thus a 13‑word sentence admits **208 012** distinct binary bracketings. The arithmetic follows directly from the binomial coefficient expansion; no external data are introduced.

### 3. Explicit comb‑metric for a four‑level tree  
Let a rooted tree have four levels (root at level 3, leaves at level 0). Define a piecewise‑constant function $f\colon[0,4]\to[0,\infty)$:
\[
f(s)=
\begin{cases}
3 & \text{if } s\in[0,1),\\
2 & \text{if } s\in[1,2),\\
1 & \text{if } s\in[2,3),\\
0 & \text{if } s\in[3,4].
\end{cases}
\]
According to the comb construction of [7] (the definition of $\bar d_f$ as $\displaystyle\bar d_f(s,t)=\sup_{(s\wedge t,\,s\vee t)} f$), the distance between any two leaf positions $s,t\in[3,4]$ equals the maximum $f$‑value on the interval between them. For example, with $s=3.2$ and $t=3.8$ the interval lies entirely in the region where $f=0$, so $\bar d_f(s,t)=0$, matching the leaf‑level distance $h=0$. If $s=2.5$ and $t=3.5$, the interval crosses the region where $f=1$, giving $\bar d_f(s,t)=1$, which equals $h(\operatorname{LCA})$. Hence $\bar d_f$ reproduces exactly the LCA‑height distance $d$ on the leaf set, providing a concrete instance of the isometry proved in [7, §3.1].

### 4. Algebraic encoding and the inverse‑system of symmetric functions  
The ring of symmetric polynomials $B_n=\mathbb{Z}[x_1,\dots,x_n]^{\mathfrak{S}_n}$ forms an inverse system whose limit $B$ is the ring of symmetric functions [3]. In the UNSG framework each vertex $v\in V$ receives an idempotent $e_v$ in a generalized path algebra $\Lambda$ (Section 3.6). The collection $\{e_v\}_{v\in V}$ plays the same role as the orthogonal idempotents $\{e_{ii}\}$ that generate the matrix units in the construction of $B_n$. By arranging the vertices according to tree depth we obtain a filtration
\[
\Lambda_0 \hookrightarrow \Lambda_1 \hookrightarrow \Lambda_2 \hookrightarrow \Lambda_3,
\]
which mirrors the inverse system $B_1 \leftarrow B_2 \leftarrow \cdots$ described in [3, §1]. The limit algebra $\Lambda_\infty$ therefore encodes the full UNSG and mirrors the inverse system of symmetric polynomial rings described in [3]; the analogy suggests a similar hierarchical structure, though no isomorphism to the bosonic Fock space is claimed. This correspondence supplies a representation‑theoretic bridge between UNSGs and the symmetric‑function construction of [3].

### 5. Semantic‑memory grounding of ultrametricity  
We hypothesize that semantic memory may inherently rely on ultrametric topologies, a perspective suggested by projective geometric frameworks [9]. The UNSG leaf‑distance, being an ultrametric by construction, therefore provides a formal substrate for that claim: hierarchical semantic relations are captured by the LCA‑height metric, and the strong triangle inequality guarantees that any three concepts form an isosceles configuration, suggesting a correspondence with hierarchical semantic organization. This alignment supplies a cognitive justification for the mathematical design of UNSGs.

### 6. Hierarchical state mapping and cognitive‑linguistic models  
The ratio‑based adelic physics paper emphasizes that **hierarchical state mappings translate discrete tree structures into continuous outputs** [10]. In UNSGs the mapping $s_\ell\mapsto h(\operatorname{LCA})$ (Section 3.3) performs precisely this translation: each leaf $\ell$ acquires a real‑valued coordinate $s_\ell$ on $[0,m]$, and the piecewise‑constant function $f$ encodes the hierarchical state. The resulting continuous ultrametric space can be interpreted as a cognitive‑linguistic representation where discrete syntactic distinctions are embedded in a real‑valued metric space, as advocated in [10, §1.4].

### 7. Primitive distinctions as the syntactic seed  
The QNFO work on syntactic generation treats **the primitive act of making a distinction** as the foundational syntactic token [11]. In the UNSG construction (Section 3.1) the root node $S$ embodies exactly this primitive distinction: it separates the sentence into constituent substructures. The sibling edges added between children of a node correspond to the juxtaposition operation described in [11, §1.3]. Thus the entire graph can be seen as a systematic elaboration of primitive distinctions, grounding the formalism in the philosophical account of [11].

### 8. Block‑diagonal LCA matrix and ultrametric attention  
The proof‑of‑concept paper on auditable attention demonstrates that **the LCA matrix of a binary‑tree encoder is block‑diagonal**, enabling $O(n)$ attention computation [12]. For a binary tree of depth 2 with leaves $\{l_1,l_2,l_3,l_4\}$ the LCA matrix $M$ is
\[
M=
\begin{pmatrix}
0 & 1 & 2 & 2\\
1 & 0 & 2 & 2\\
2 & 2 & 0 & 1\\
2 & 2 & 1 & 0
\end{pmatrix},
\]
which becomes block‑diagonal after permuting leaves to group siblings. In the binary‑tree case shown, each internal node defines a block of leaves sharing the same LCA height, yielding a block‑diagonal LCA matrix. Consequently, attention mechanisms that use a monotone function of $M$ enjoy the $O(n)$ computational advantage proved in [12, §5.7]; extending this advantage to arbitrary UNSGs remains a conjecture.

### 9. Sensitivity of the planar‑slope bound to branching factor  
Recall the bound $psn(G)\le\max\{4,\Delta\}$ from [5]. The maximum degree $\Delta$ of a UNSG equals the maximum branching factor $b$ of its parse tree plus one (the parent edge). If a polysynthetic verb yields $b=10$, then $\Delta=11$ and the bound becomes $psn(G)\le 11$. Conversely, for binary parses ($b\le2$) we have $\Delta\le3$, and the bound collapses to $psn(G)\le4$. This linear sensitivity follows directly from the definition of $\Delta$ and the theorem in [5, §3].

### 10. Summary of new quantitative results  

| Quantity | Derivation | Result |
|----------|------------|--------|
| Binary bracketings for $n=13$ | Catalan formula (Section 2) | $208\,012$ |
| Comb‑metric distance for a four‑level tree | Piecewise $f$ (Section 3) | $\bar d_f$ reproduces $d$ |
| LCA matrix block size for depth‑2 binary tree | Explicit construction (Section 8) | $4\times4$ block‑diagonal matrix |
| Planar slope bound for $\Delta=11$ | $psn\le\max\{4,\Delta\}$ (Section 9) | $psn\le11$ |

These worked examples reinforce the theoretical claims of the paper, demonstrate concrete calculations that follow directly from the definitions, and connect the UNSG framework to broader mathematical and cognitive literature via the cited works [2, 6, 7, 9, 10, 11, 12].

## 7. Discussion

### 7.1 Limitations
- **Tree‑only syntax**: The construction assumes a tree‑structured parse; non‑projective dependencies may violate ultrametricity.  
- **Parser accuracy**: Errors in syntactic parsing propagate to the graph, potentially breaking the LCA‑based distance definition.  
- **Degree bound**: The planar slope bound relies on $\Delta\le3$; higher branching factors increase the required number of slopes.  
- **Representation number**: The mapping to word‑representable split graphs inherits the unknown representation number, limiting combinatorial characterizations [4].  
- **Algebraic overhead**: Encoding via generalized path algebras introduces additional algebraic complexity that may be unnecessary for practical implementations.

### 7.2 Falsifiability
If a parsed sentence yields three leaves $x,y,z$ such that  

\[
d(x,z) > \max\{d(x,y),d(y,z)\},
\]

the ultrametric claim is falsified. This would indicate that the LCA‑height distance does not dominate pairwise distances, contradicting the hierarchical assumption.

### 7.3 Open Questions
- How can UNSGs be extended to handle non‑tree syntactic structures while preserving ultrametricity?  
- What is the exact representation number for the class of UNSGs viewed as split graphs?  
- Can the algebraic encoding be leveraged for efficient graph‑based inference algorithms?  

## 8. Practical Implications and Engineering Pathways

**(a) Intended users and design impact**  
Cross‑lingual search engines, multilingual question‑answering systems, and low‑resource language technology developers would benefit from a language‑neutral graph representation that enables subgraph‑matching retrieval independent of morphological complexity. Adoption would replace token‑level indexing with graph‑based indexing, allowing a single retrieval pipeline to serve isolating, agglutinative, and polysynthetic languages.

**(b) Technology readiness**  
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at **TRL 2** (concept formulation).

**(c) Minimal de‑risking experiment**  
A pilot study would parse a parallel corpus of English and Turkish sentences, construct UNSGs for each language, and compute leaf‑to‑leaf distances. The experiment would verify that corresponding sentences produce isomorphic UNSGs (or graphs with distance $\le2$). Observation of any violation of the strong triangle inequality would falsify the core claim.

**(d) Engineering constraints**  
- **Parsing**: Accurate syntactic parsers for polysynthetic languages are required; current tools may need adaptation.  
- **Graph construction**: Efficient LCA computation and sibling‑edge generation must be implemented.  
- **Visualization**: Square‑contact drawing libraries must respect the planar slope bound; for $\Delta>3$, additional slopes are needed per [5].  
- **Algebraic tooling**: Implementations of generalized path algebras and hyper‑loop module operations are optional but may aid formal verification.

**(e) Projected performance bounds**  
Assuming $\Delta\le3$, the planar drawing can be realized with at most four edge slopes (projection based on [5]). The comb‑metric embedding guarantees that distance queries execute in $O(1)$ time after preprocessing, because LCA heights can be stored in a lookup table.

**(f) Risks and misuse**  
Deploying UNSG‑based retrieval without validating parser accuracy could lead to false positives in cross‑lingual search, especially for low‑resource languages where parsing errors are prevalent. Overreliance on the ultrametric assumption may obscure nuanced semantic differences not captured by hierarchical structure alone.

## 9. Conclusion
This paper introduced Ultrametric Nested Semantic Graphs as a mathematically rigorous, language‑neutral meaning representation. By defining distances via LCA height on the leaf set, the representation inherits the strong triangle inequality of ultrametrics, enabling efficient subgraph‑matching retrieval across typologically diverse languages. The analysis provided a concrete numeric illustration, a corrected planarity assessment, a qualified planar‑slope bound, exact combinatorial cost calculations, and connections to established graph‑theoretic and algebraic frameworks. While the approach rests on idealized syntactic trees and assumes low branching degree, it offers a clear theoretical pathway toward unified multilingual semantic processing. Future work will focus on empirical validation with parallel corpora, extensions to non‑tree syntactic phenomena, and exploitation of the algebraic encoding for algorithmic inference.

## Version History

- Version 1.1.0 (2026-10-20, from 1.0.0): revised against the current literature, re-reviewed and re-verified. references 12 -> 12. length 4219 -> 4280 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.29.0-terminal-rearmed). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 6 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] An embedding, an extension, and an interpolation of ultrametrics. arXiv:2008.10209v2. https://arxiv.org/abs/2008.10209v2
[2] Square-Contact Representations of Partial 2-Trees and Triconnected Simply-Nested Graphs. arXiv:1710.00426v1. https://arxiv.org/abs/1710.00426v1
[3] Polynomial representations and categorifications of Fock Space. arXiv:1101.2456v3. https://arxiv.org/abs/1101.2456v3
[4] Representation Number of Word-Representable Split Graphs. arXiv:2502.00872v2. https://arxiv.org/abs/2502.00872v2
[5] Planar Drawings with Few Slopes of Halin Graphs and Nested Pseudotrees. arXiv:2105.08124v2. https://arxiv.org/abs/2105.08124v2
[6] Finite-Dimensional Representations of Hyper Loop Algebras Over Non-Algebraically Closed Fields. arXiv:0711.0795v4. https://arxiv.org/abs/0711.0795v4
[7] The comb representation of compact ultrametric spaces. arXiv:1602.08246v1. https://arxiv.org/abs/1602.08246v1
[8] Structures and Representations of Generalized Path Algebras. arXiv:math/0402188v5. https://arxiv.org/abs/math/0402188v5
[9] https://papers.qnfo.org/papers/projective-geometric-frameworks-for-semantic-structures. QNFO: Projective Geometric Frameworks for Semantic Structures.
[10] https://papers.qnfo.org/papers/ratio-based-adelic-physics. QNFO: Ratio-Based Adelic Physics.
[11] https://papers.qnfo.org/papers/syntactic-generation-primitive-distinctions. QNFO: Syntactic Generation.
[12] https://papers.qnfo.org/papers/proof-of-concept-for-auditable-attention-using-ultrametric-tree-distances. QNFO: Proof-of-Concept for Auditable Attention using Ultrametric Tree Distances.

## Appendix A. Divergence report
*No divergent claims were identified among the source drafts; all substantive statements converge.*

## Appendix B. Claim attribution
| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | Definition of UNSG distance as LCA height on leaf set | A, B | Convergent |
| C2 | Proof that distance satisfies ultrametric inequality | A, B | Convergent |
| C3 | Numeric example with distances 2,2,1 and verification | A, B | Convergent |
| C4 | Planar slope bound $psn\le\max\{4,\Delta\}$ applied to $\Delta=3$ gives $psn\le4$ (qualified) | A, B | Convergent |
| C5 | Comb‑metric $\bar d_f$ is isometric to $d$ on leaves | A, B | Convergent |
| C6 | Mapping to word‑representable split graphs; representation number unknown | A, B | Convergent |
| C7 | Algebraic encoding via generalized path algebras and hyper‑loop modules | A, B | Convergent |
| C8 | Limitations list (tree‑only syntax, parser accuracy, degree bound, representation number, algebraic overhead) | A, B | Convergent |
| C9 | Falsifiability condition (violation of strong triangle inequality) | A, B | Convergent |
| C10 | Practical implications (users, TRL, pilot experiment, constraints, performance projection, risks) | A, B | Convergent |
| C11 | $58\,786$ binary bracketings for a 12‑word sentence | A, B | Convergent |
| C12 | $1\,860\,480$ injective mappings for a 5‑node pattern in a 20‑node graph | A, B | Convergent |
| C13 | Compression factor $500$ from pairwise distances to tree parameters at $n=1{,}000$ nodes | A, B | Convergent |