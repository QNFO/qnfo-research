# Infomatics v2 — Phased Research WBS (v2.0)

**Foundation:** Laws of Form (Spencer-Brown 1969) + Ultrametric Metrology  
**Date:** 2026-07-19  
**Repository:** [rwnq8/infomatics-v2](https://github.com/rwnq8/infomatics-v2)  
**Tag:** v0.1-phase0 → v0.2-phase1-search (in progress)

---

## §0. Foundation Axioms

The project rests on four primitives, drawn from Laws of Form and specialized to metrology:

| Primitive | Source | Translation to Physics |
|:----------|:-------|:-----------------------|
| **Draw a distinction** | Spencer-Brown 1969, Ch. 1 | Perform a measurement. The act of measurement IS the act of drawing a distinction |
| **Re-entry** (f = ┐f┌) | Spencer-Brown 1969, Ch. 11 | The distinction that re-enters its own space. Generates OSCILLATION → TIME. ZBW at Compton scale IS re-entry |
| **Closure** (completeness) | Spencer-Brown 1969, Ch. 9 + ultrametric completion | Every valid form reduces to marked/unmarked. Every Cauchy sequence of finer distinctions converges. The tree has no gaps |
| **Ultrametric tree** (d(x,z) ≤ max(d(x,y), d(y,z))) | Strong triangle inequality | Distinctions are NESTED. Coarser distinctions enclose finer ones. Taxonomy discovers, not invents |

---

## §1. Phased WBS

### Phase 0: Project Initialization ✅

| ID | Task | Deliverable | Status |
|:---|:-----|:------------|:-------|
| 0.1 | Create GitHub repo, directory scaffold | Repo live: rwnq8/infomatics-v2 | ✅ |
| 0.2 | Define classification system | notebooks/classification-system.md — DRAWN/DEFINED/INFERRED/HORIZON/QNFO | ✅ |
| 0.3 | Define evidence standards | notebooks/classification-system.md §3 — API-verified citations only | ✅ |
| 0.4 | Define search methodology | PROJECT-PLAN.md §4.1 — arXiv API, Semantic Scholar, INSPIRE | ✅ |
| 0.5 | Phase 0 closeout | Git tag v0.1-phase0, R2 upload, KG update | ✅ |

---

### Phase 1: External Literature Search (IN PROGRESS)

For each of the 7 claim domains, search ≥3 external sources. Verify every citation against API. Tag every claim with Laws of Form distinction class. **Zero unverified citations.**

| ID | Domain | Key Question | Laws of Form Framing | External Sources |
|:---|:-------|:-------------|:---------------------|:-----------------|
| **1.1** | D1: "It from Bit" | Is "information is fundamental" a DRAWN distinction or a DEFINED proposal? | Wheeler: Does drawing the "information is fundamental" distinction create structure isomorphic to physics? | arXiv, S2, Web |
| **1.2** | D2: Zitterbewegung | Is ZBW DRAWN (measured in free electrons), DEFINED (simulated), or INFERRED (required by Dirac + LoF)? | Re-entry at Compton scale: f = ┐f┌ → ω_ZBW = 2mc²/ħ. Is this re-entry observable? | arXiv, S2 |
| **1.3** | D3: α as Distinction Ratio | IS α a DRAWN metrology ratio (r_e/λ_C), or is it INFERRED from deeper structure? | α IS the distinction ratio between classical boundary and quantum oscillation. It's not derived — it's measured | CODATA, arXiv, textbooks |
| **1.4** | D4: Electron Structure | Where in the distinction tree does electron structure become HORIZON vs INFERRED? | "Point-like" is a measurement BOUNDARY, not an ontological claim. The tree continues below 10⁻¹⁸ m per Laws of Form | arXiv, S2, LEP papers |
| **1.5** | D5: p-Adic Connection | Has any external group DRAWN a p-adic distinction in a physical system? | Ultrametric = tree = nested distinctions. Is there external evidence for p-adic structure in physics beyond QNFO? | arXiv, S2, Dragovich et al. |
| **1.6** | D6: Adelic Framework | What external citations does the adelic Dirac equation have? | Adelic = ALL completions of ℚ. Does the physics community recognize this as a DRAWN or DEFINED framework? | arXiv, S2, citation tracking |
| **1.7** | D7: Info-Theoretic QFT | Can QFT be derived from information-theoretic axioms per Chiribella/Hardy? | If drawing information distinctions generates physics, the formalism should reproduce known results. Does it? | arXiv, S2 |

**Deliverable per domain:** Search report with ≥5 verified external citations, each tagged with Laws of Form distinction class.

---

### Phase 2: QNFO Due Diligence

| ID | Task | Questions |
|:---|:-----|:----------|
| 2.1 | KG cross-reference | Which QNFO papers make claims in these 7 domains? |
| 2.2 | D1 paper audit | What DOIs exist? What external citations do they have? |
| 2.3 | Vectorize semantic overlap | Where does QNFO work overlap with external work? |
| 2.4 | External citation tracking | How many non-QNFO citations per QNFO paper? → maps to QNFO vs External tags |

---

### Phase 3: Distinction-Theoretic Classification

Apply the Laws of Form classification system to EVERY claim across all 7 domains.

| ID | Task |
|:---|:-----|
| 3.1 | Classify all claims: DRAWN / DEFINED / INFERRED / HORIZON / QNFO |
| 3.2 | Assign metrology scale (λ) and tree depth (n) per claim |
| 3.3 | Assign parent distinction (what enables this claim?) |
| 3.4 | Assign external recognition tag (Established / Active / Noted / None) |
| 3.5 | Build the ultrametric distinction tree visualization |

**Deliverable:** artifacts/classification-matrix.md — every claim classified

---

### Phase 4: Synthesis

| ID | Task |
|:---|:-----|
| 4.1 | Write consolidated survey paper: "What Can Be Drawn: An Evidence-Based Survey of Information-Theoretic Physics" |
| 4.2 | Gap analysis: which domains are HORIZON vs QNFO vs INFERRED? |
| 4.3 | Identify legitimate open problems (DEFINED distinctions without metrology) |
| 4.4 | Build PDF via Pandoc+XeLaTeX |

---

### Phase 5: Publication

| ID | Task |
|:---|:-----|
| 5.1 | Zenodo deposit with DOI |
| 5.2 | D1 living-paper insert |
| 5.3 | papers.qnfo.org deploy |
| 5.4 | 4-D distribution (IPFS, DNSLink, Archive) |

---

## §2. Evidence Classification System (Distinction-Theoretic)

### Five Distinction Classes

```
DRAWN —    ≥2 independent metrological acts have drawn this distinction.
           Requires: reproducibility, different measurement methods.

DEFINED —  Mathematically specified at a known scale. Apparatus proposed,
           not yet operated. Requires: falsifiability condition.

INFERRED — Required by the tree structure. Given parent distinctions that ARE
           drawn, this distinction MUST exist. (Like Planck length from ħ, G, c.)

HORIZON —  Below current metrology floor. Per Laws of Form, structure MUST exist
           (every distinction implies an inside AND an outside), but we cannot
           label the nodes at this scale.

QNFO —     Exists within QNFO framework. No external group has drawn, defined,
           or inferred this distinction. May be internally rigorous.
```

### External Recognition Tags

| Tag | Criteria |
|:----|:---------|
| External — Established | ≥3 independent non-QNFO groups, reviewed in journals, ≥100 citations |
| External — Active | ≥2 groups discussing in peer-reviewed literature, ≥5 citations |
| External — Noted | ≥1 non-QNFO citation |
| External — None | Zero non-QNFO citations |
| QNFO — Falsifiable | No external citations, but clear falsification condition stated |
| QNFO — Philosophical | No external citations, no falsification condition |

### α Reframed

α is NOT a "constant to derive." It IS the **distinction ratio**:

| Scale | Distinction Class | Tree Depth |
|:------|:------------------|:-----------|
| α ≈ 1/137.036 | **DRAWN** (CODATA, e⁺e⁻, Rb, Cs, g-2) | Depth 0 — organizes all EM distinctions |
| α = r_e/λ_C | **DEFINED** (standard formula, new vocabulary) | Depth 1 — derived from α |
| ZBW amplitude = λ_C | **DEFINED** (Dirac eq. feature, simulated not free-electron) | Depth 2 |
| Sub-Compton structure | **HORIZON** (below metrology, required by LoF) | Depth 3+ |

---

## §3. Deliverable Registry (Updated)

| ID | Deliverable | Format | Status |
|:---|:------------|:-------|:-------|
| D0 | Classification system + WBS | Markdown | ✅ Complete |
| D1.1–D1.7 | 7 domain search reports | Markdown | 🔄 Phase 1 in progress |
| D2.1–D2.4 | QNFO due diligence reports | Markdown | Pending |
| D3.1–D3.5 | Distinction-theoretic classification matrix | Markdown | Pending |
| D4.1 | Consolidated survey paper | Markdown + PDF | Pending |
| D5.1–D5.4 | Publication (Zenodo, D1, papers-server, 4-D) | DOI + Web | Pending |

---

## §4. Version History

| Version | Date | Tag | Description |
|:--------|:-----|:----|:------------|
| v0.1 | 2026-07-19 | v0.1-phase0 | Project initialization, distinction-theoretic classification system |
| v0.2 | TBD | v0.2-phase1-search | Phase 1 — external literature search across 7 domains |
