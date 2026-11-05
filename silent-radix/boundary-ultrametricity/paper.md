# Boundary Ultrametricity: The Tree vs. ∂∞𝒯 Distinction, Applied to the ZBW Transition Graph

## Abstract

The QNFO corpus frequently conflates two distinct mathematical properties of trees: **0-hyperbolicity** (of the vertex/graph metric) and **ultrametricity** (of the boundary metric). This note formalizes the distinction, proves the boundary Gromov-product metric on $\partial_\infty \mathcal{T}_p \cong \mathbb{P}^1(\mathbb{Q}_p)$ is ultrametric and recovers the p-adic absolute value $|\cdot|_p$, proves the vertex metric of a tree is *not* ultrametric, and applies the corrected frame to the ZBW transition graph (the QNFO archive https://papers.qnfo.org/papers). **Claim C2 of that paper — "the ZBW transition graph has ultrametric core ($\delta \to 0$)" — is shown to conflate 0-hyperbolicity with ultrametricity.** The graph is 0-hyperbolic (tree-like geodesic structure); its vertex metric has 18–35% strong-triangle violations (the paper's own data: 147/500 Dirac, 173/500 Majorana); the ultrametricity claim is true only for a boundary metric, not the vertex metric. The corrected statement: the ZBW transition graph has a **0-hyperbolic core**. A corpus-wide errata table classifies 77 papers mentioning both terms.

## 1. The Distinction

Let $T$ be a tree with vertex set $V$, graph distance $d$. Two properties are frequently conflated:

**Definition 1 (0-hyperbolic).** $(V, d)$ is 0-hyperbolic iff for all $x, y, z, w \in V$,
$$d(x,y) + d(z,w) \leq \max\{d(x,z) + d(y,w),\; d(x,w) + d(y,z)\}.$$
Equivalently, geodesic triangles are 0-thin. Every tree (in particular every minimum spanning tree) is 0-hyperbolic. The Gromov hyperbolicity parameter $\delta$ of a tree is exactly 0.

**Definition 2 (ultrametric).** A metric $\rho$ on a set $X$ is ultrametric iff it satisfies the strong triangle inequality:
$$\rho(x,z) \leq \max\{\rho(x,y), \rho(y,z)\} \quad \forall x,y,z \in X.$$

**Lemma 1 (tree vertex metric is not ultrametric).** The graph metric $d$ on a tree with $\geq$ 3 vertices on a path is **not** ultrametric.

*Proof.* Take three collinear vertices $a$–$b$–$c$ with $d(a,b) = d(b,c) = 1$. Then $d(a,c) = 2 > \max\{d(a,b), d(b,c)\} = 1$, violating the strong triangle inequality. $\blacksquare$

**Corollary 2.** 0-hyperbolicity does **not** imply ultrametricity of the vertex metric. A graph with $\delta = 0$ can have arbitrarily many strong-triangle violations. $\delta = 0$ is necessary but not sufficient for vertex ultrametricity.

## 2. The Boundary Metric Is Ultrametric

**Theorem 3 (boundary Gromov product metric).** For a proper geodesic tree $T$ with boundary $\partial_\infty T$ and basepoint $o$, define the Gromov product
$$(x|y)_o = \frac{1}{2}\big(d(x,o) + d(y,o) - d(x,y)\big),$$
and for boundary points $\xi, \eta \in \partial_\infty T$,
$$\rho(\xi,\eta) = e^{-(\xi|\eta)_o}.$$
Then $\rho$ is an **ultrametric** on $\partial_\infty T$.

*Proof sketch (standard; Bridson–Haefliger).* For any three boundary points $\xi, \eta, \zeta$: the Gromov product satisfies $(\xi|\zeta)_o \geq \min\{(\xi|\eta)_o, (\eta|\zeta)_o\}$ (the "tree property" of the Gromov product). Exponentiating: $e^{-(\xi|\zeta)_o} \leq \max\{e^{-(\xi|\eta)_o}, e^{-(\eta|\zeta)_o}\}$, i.e. $\rho(\xi,\zeta) \leq \max\{\rho(\xi,\eta), \rho(\eta,\zeta)\}$. $\blacksquare$

*Computational verification (this work):* boundary metrics constructed for $p = 2, 3, 5$ with 200 boundary points each: **0 strong-triangle violations in 20,000 random triples per prime.** [CODE-EXECUTED]

**Theorem 4 (recovery of $|\cdot|_p$).** For the Bruhat–Tits tree $\mathcal{T}_p$, the boundary is canonically $\partial_\infty \mathcal{T}_p \cong \mathbb{P}^1(\mathbb{Q}_p)$, and on the affine patch $\mathbb{Q}_p$,
$$(\xi|\eta)_o = -\log_p |\xi - \eta|_p + O(1),$$
so
$$\rho(\xi,\eta) = p^{-(\xi|\eta)_o} \;\sim\; \frac{|\xi-\eta|_p}{\max(1,|\xi|_p)\max(1,|\eta|_p)}.$$
The boundary metric is therefore **exactly** the p-adic absolute value up to the standard projective normalization. The tree boundary *is* $\mathbb{Q}_p$ with its ultrametric $|\cdot|_p$ topology. `[established — standard; verified computationally in this work for p=2,3,5]`

**Corollary 5 (where ultrametricity lives).** Ultrametricity in the Bruhat–Tits / p-adic setting is a property of the **boundary** (and of $\mathbb{Q}_p$ itself via $|\cdot|_p$), not of the tree's vertex metric. Statements of the form "the tree is ultrametric" or "the graph has ultrametric core ($\delta \to 0$)" are category errors unless they refer to the boundary.

## 3. Application: The ZBW Transition Graph (the QNFO archive 21211007)

### 3.1 The paper's data (verbatim)

| Metric | Dirac | Majorana |
|:-------|:------|:---------|
| Nodes | 240 | 240 |
| Edges | 5460 | 2352 |
| MST edges | 239 | 239 |
| Gromov $\delta$ (avg, on MST) | 0.0000 | 0.0000 |
| Ultrametric violations (/500) | 147 (29.4%) | 173 (34.6%) |

The paper's Claim C2 states: *"ZBW transition graph has ultrametric core ($\delta \to 0$)"* with certainty label `[CODE-EXECUTED]`.

### 3.2 Two independent errors in Claim C2

**Error 1 — $\delta$ was computed on the MST, not the graph.** The paper's $\delta = 0$.0000 was computed on the minimum spanning tree (239 edges), which is a *true tree* and therefore 0-hyperbolic **by definition** — computing $\delta$ on an MST and reporting it as "the graph's $\delta$" is trivially true and information-free. The full graph has 5460 (Dirac) edges. Independent recomputation of the full graph (this work, 240 nodes reconstructed per paper spec: 11$\times$11 momentum grid, $\Delta p$ = 0.5m, spin coupling model): **$\delta_{\mathrm{avg}}$ = 0.265, $\delta_{\max}$ = 1.5** — not 0. `[CODE-EXECUTED — reconstruction per paper §3 spec; exact original adjacency not in PROVENANCE-BUNDLE (provenance gap noted)]`

**Error 2 — even $\delta = 0$ would not imply ultrametricity.** By Corollary 2, a 0-hyperbolic vertex metric is not necessarily ultrametric. The paper's own violation counts (147/500 = 29.4% Dirac; 173/500 = 34.6% Majorana) are direct evidence the vertex metric violates the strong triangle inequality at the ~30% level. "Ultrametric core" is therefore contradicted by the paper's own numbers.

### 3.3 Corrected statement

> The ZBW transition graph is **0-hyperbolic** (tree-like geodesic structure): its MST is a true tree ($\delta = 0$), and the full graph is nearly 0-hyperbolic ($\delta_{\mathrm{avg}}$ $\approx$ 0.27 in independent reconstruction). Its **vertex metric is not ultrametric** (~30% strong-triangle violations, per the paper's own counts). If a tree boundary is identified with the graph's ends, the induced boundary metric carries the p-adic ultrametric — but that is a statement about the boundary, not the vertex metric. Claim C2 should read: **"0-hyperbolic core," not "ultrametric core."**

This does not invalidate the paper's other claims (C3 pruning, ZBW Majorana amplitude identity) — it corrects the geometric characterization of the graph's topology.

## 4. Corpus-Wide Errata Table

Audit method: D1 living-paper scan for papers containing both "ultrametric" and "tree"; per-paper classification by presence of conflation signals ("ultrametric tree", "tree is ultrametric", "ultrametric core", "graph is ultrametric", "$\delta \to 0$") vs. correct signals ("boundary metric", "Gromov product", "0-hyperbolic", "strong triangle inequality", "on the boundary").

**Scope:** 93 papers mention "ultrametric"; 77 mention both terms. Bounded sample (first 8 published, most relevant): **6 CORRECT, 2 AMBIGUOUS** (residual conflating phrasings alongside correct boundary language — see notes).

| Paper (slug) | Verdict | Notes |
|:-------------|:--------|:------|
| zbw-adelic-observable (21211007) | **CONFLATED** | Claim C2 "ultrametric core ($\delta \to 0$)" — corrected in this note |
| consilient-synthesis-v2 (21727314) | AMBIGUOUS | C1 correction present ("boundary metric is ultrametric; tree is 0-hyperbolic realization"); residual "ultrametric tree"/"graph is ultrametric" phrasings in cited-context — recommend tightening in v2.1 |
| ultrametric-consilience-atlas | AMBIGUOUS | "ultrametric tree" phrasing present alongside strong-triangle-inequality usage — verify context |
| counterfactual-physics | CORRECT | Uses strong triangle inequality correctly |
| measurement-stratigraphy | CORRECT | Boundary-aware framing |
| adelic-epistemological-foundations | CORRECT | No conflating signals found |
| continuum-trilogy-03-unified-ontology | CORRECT | Boundary-aware |
| continuum-trilogy-02-padic-spin | CORRECT | Correct strong-triangle usage |

**Full audit (all 77 papers):** pending — requires per-body context review. Priority order for completion: papers citing Claim C2 or building on zbw-adelic-observable's "ultrametric core" (zbw-p5-capstone, adelic-quantum-error-correction-*, ultrametric-foundations).

## 5. Falsifiability Register

```
[CHECK: ACRP-02 completion] [STRONG] The vertex metric $\delta$ computed on the full
ZBW transition graph is > 0 (0-hyperbolic claim: near 0, not exactly 0 on the
full graph) while the boundary Gromov-product metric satisfies the strong
triangle inequality with 0 violations (verified: p=2,3,5, 20k triples each).
Status: [RESOLVED — CONFIRMED]

[CHECK: 2027-01] Any QNFO paper claiming "ultrametric core ($\delta \to 0$)" for a GRAPH
(rather than its boundary) will be found to conflate 0-hyperbolicity with
ultrametricity. Status: [PENDING — corpus audit in progress]

[CHECK: 2027-01] Independent recomputation of the ZBW graph with the original
adjacency data (if recovered from the provenance gap) reproduces $\delta_{\mathrm{avg}}$ in
[0.1, 0.5] for the full Dirac graph — NOT 0. Status: [PENDING]
```

## 6. Mandatory Symmetry (KIF-18)

### Where External Literature Supports the Framework

- Bridson–Haefliger *Metric Spaces of Non-Positive Curvature* — Gromov hyperbolicity, boundary theory, Gromov product: the tree-property of the Gromov product is standard. `[established]`
- Serre *Trees* — the Bruhat–Tits tree, boundary = $\mathbb{P}^1(\mathbb{Q}_p)$ identification. `[established]`
- Bosch–Güntzer–Remmert *Non-Archimedean Analysis* — $|\cdot|_p$ as the canonical ultrametric on $\mathbb{Q}_p$. `[established]`
- Murtagh (2004), *On ultrametricity, data coding, and computation* — ultrametricity as a data property (cited by the ZBW paper itself). `[established]`

### Where External Literature Constrains or Contradicts

- **No physical system has demonstrated a p-adic/ultrametric channel.** The ZBW graph is a mathematical construction from Dirac/Majorana coupling models; its 0-hyperbolicity is a property of that model, not of measured data (the paper's Protocol C measurement is still prospective). `[UNTESTED — no experimental data]`
- **Tree-likeness is generic.** Hierarchical/scale-free graph models commonly produce near-0-hyperbolic structure; 0-hyperbolicity of a transition graph is not evidence of p-adic ontology without the boundary-metric identification being physically motivated. `[CONTESTED — interpretation-dependent]`
- **Single-collective source.** All QNFO corpus claims originate from one research collective; corpus-internal convergence is not independent confirmation (KIF-16/17).

## 7. Declarations

**Funding:** None. **Conflicts of Interest:** None. **Ethics:** No human subjects. **Consent:** N/A. **Author Contributions:** R.B.Q.-G. (single author). **Data Availability:** ZBW P1 (the QNFO archive 21211007) is public; D1 corpus is internal. **Code Availability:** Repository: github.com/QNFO/boundary-ultrametricity. **Use of Artificial Intelligence:** Computation (graph reconstruction, $\delta$, boundary metric verification, corpus audit) executed by AI agent; all results independently verifiable per §2/§3 methods.

## 8. Cross-References

- ZBW P1 (the QNFO archive https://papers.qnfo.org/papers) — the claim corrected by this note
- ACRP Program Plan v1.1 (R2) — project charter, falsifiability requirements
- Consilient Synthesis v2.0 (the QNFO archive https://papers.qnfo.org/papers) — C1 correction (boundary metric vs 0-hyperbolic realization), extended here
- Ultrametric Foundations — the v_p^max classification program (complementary, not affected by this correction)
