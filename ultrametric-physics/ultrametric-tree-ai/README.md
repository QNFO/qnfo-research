# 🌳 Ultrametric Tree AI vs 🔵 Vector Search — Interactive Explorer

**Live Demo:** [ultrametric-tree-ai.pages.dev](https://ultrametric-tree-ai.pages.dev)

An interactive side-by-side comparison of ultrametric tree-based AI versus vector database search on real estate data. Built to answer: *What would ultrametric/tree AI look like, and what would change?*

---

## Quick Start

```bash
# Clone and open in browser
git clone https://github.com/rwnq8/ultrametric-tree-ai.git
cd ultrametric-tree-ai
open index.html   # or double-click
```

No build step. No dependencies (D3.js loads from CDN).

---

## What This Demonstrates

| Feature | Vector Search (Cosine) | Ultrametric Tree (LCA) |
|---------|----------------------|------------------------|
| **Distance metric** | `d(A,C) ≤ d(A,B) + d(B,C)` | `d(A,C) ≤ max(d(A,B), d(B,C))` |
| **Triangle violations** | **54** (out of 120 triples) | **0** (guaranteed) |
| **Interpretability** | Black-box cosine score | Tree path breadcrumbs + kinship labels |
| **Geometry** | Smooth, continuous | Hierarchical, discrete |
| **Search time** | ~0.10 ms | ~0.80 ms |

### 5 Interactive Tabs
1. **🔍 Live Demo** — Side-by-side search comparison with real-time metrics
2. **📊 Dendrogram** — Zoomable D3.js tree visualization (click leaves to search)
3. **📐 Math & Theory** — Ultrametric foundations, p-adic numbers, tree equivalence theorem
4. **⚠️ Errors Corrected** — 7 errors in the original analysis, corrected with citations
5. **🏭 Existing Systems** — 9 production/research systems catalogued

---

## Mathematical Foundation

### The Strong Triangle Inequality

An **ultrametric** obeys a stronger version of the triangle inequality:

$$\forall A,B,C: \quad d(A,C) \leq \max(d(A,B), d(B,C))$$

This forces every triangle to be **isosceles with two equal longest sides**, and makes the space **totally disconnected** — there are no smooth paths between points, only discrete jumps at tree nodes.

### Tree Equivalence Theorem

> Every finite ultrametric space is isometric to the leaf set of a rooted tree with uniform edge lengths per level. Conversely, every such tree defines an ultrametric.

This means **decision trees, hierarchical clusters, taxonomies, and p-adic number systems all implicitly define ultrametrics**.

### Key Research Referenced

| Year | Paper | Venue | Relevance |
|------|-------|-------|-----------|
| 2018 | **TDM** — Learning Tree-based Deep Model for Recommender Systems | KDD | Billion-scale tree-based retrieval at Alibaba |
| 2019 | **JTM** — Joint Optimization of Tree-based Index and Deep Model | NeurIPS | Joint training of tree structure + neural model |
| 2020 | **HNSW** — Efficient ANN Search using Hierarchical Graphs | TPAMI | Tree-like graph used by all vector databases |
| 2025 | **v-PuNNs** — van der Put Neural Networks | arXiv | Pure p-adic neurons, 99.96% WordNet accuracy |
| 2026 | **HMamba** — Hyperbolic Mamba for Recommendation | ACM TOIS | Hyperbolic geometry as continuous tree space |

---

## Corrected Errors

This project identified and corrected **7 significant errors** in the original "What Ultrametric AI Would Look Like" analysis:

1. ❌ *"No SGD for trees at billion scale"* → Alibaba's TDM/JTM does exactly this (2018)
2. ❌ *"Can't average architectural styles"* → Interior tree nodes provide learned blended representations
3. ❌ *"Trees aren't differentiable"* → Hierarchical softmax (since 2013) is fully differentiable
4. ❌ *"Vector databases are purely linear"* → HNSW (used by all vector DBs) is tree-structured
5. ❌ *"No smooth analogies"* → Hyperbolic embeddings bridge tree and continuous geometry
6. ❌ *"We haven't built this yet"* → Multiple production systems exist (see Existing Systems tab)
7. ❌ *Missing hyperbolic bridge* → Field of hyperbolic deep learning (2017–present)

---

## Architecture

```
index.html  (self-contained, ~43KB)
├── HTML — Semantic structure, 5 tabs
├── CSS  — Dark/light mode, responsive grid, animations
├── JS   — Feature engineering, single-linkage clustering, cosine/LCA search
└── D3.js — Interactive dendrogram with zoom/pan
```

---

## Deployment

Deployed on **Cloudflare Pages** (free tier, unlimited bandwidth):

```bash
npx wrangler pages deploy . --project-name ultrametric-tree-ai --branch main
```

---

## License

MIT — Open source. Contributions welcome.

## Author

Built as part of the QNF0 research project. See [Ask QWAV](https://github.com/rwnq8/ask-qwav) for the production ultrametric discovery engine.
