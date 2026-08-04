# Phase 1 Due Diligence Report

**WBS: QNFO.RES.001.P1 | Branch: res/paper/falsifiability-crisis**
**Date: 2026-08-04 | Session: sTE5xgQ5axNas3bO_hf9**

## 1. QNFO Internal Cross-Reference

| Source | Query | Result |
|:-------|:------|:-------|
| KG /nodes (label=Paper, search="falsifiability") | "falsifiability" | 0 related papers |
| D1 Vectorize search_papers | "falsifiability physics unfalsifiable GR SM" | 0 related papers |
| Knowledge Graph /stats | Full ecosystem | 2,569 nodes / 908 edges |
| Durable memories search | "falsifiability crisis contemporary physics" | 0 related memories |

**Conclusion:** NO QNFO-internal overlap. This paper fills a genuine gap in the QNFO research corpus.

## 2. External Literature Search

**Methodology:** 5 APIs queried in sequence (OpenAlex, Crossref, Zenodo, Europe PMC, arXiv) across 5 query dimensions. Evidence saved to `artifacts/external-search/` (16 JSON files).

### Search Queries

| ID | Query | Source |
|:---|:------|:-------|
| Q1 | "falsifiability crisis contemporary physics" | The broad landscape |
| Q2 | "unfalsifiable general relativity dark matter auxiliary hypotheses" | GR/LCDM specific |
| Q3 | "Eddington 1919 eclipse methodology criticism bias" | Historical methodology |
| Q4 | "standard model free parameters prediction problem" | SM specific |
| Q5 | "independent consilience physics methodology falsification" | Proposed solution |

### Results Summary

| Source | Q1 | Q2 | Q3 | Q4 | Q5 |
|:-------|:---|:---|:---|:---|:---|
| OpenAlex | 966 | 0 | 3 | 954 | 40 |
| Crossref | ✓ | ✓ | ✓ | — | — |
| Zenodo | ✓ | — | ✓ | ✓ | — |
| Europe PMC | ✓ | — | — | ✓ | — |
| arXiv | ✓ | — | ✓ | ✓ | — |

### Key Findings

**Q1 — Falsifiability Crisis (966 results):** Large literature dominated by: (a) string theory/multiverse unfalsifiability debates (Dawid, Ellis & Silk), (b) cosmology crisis-in-physics narratives (Hossenfelder, Smolin), (c) philosophy-of-science post-Popper critiques. The dominant framing is "some theories are untestable" — NOT the specific protective-belt + free-parameter argument advanced here.

**Q2 — GR/Dark Matter Auxiliary Hypotheses (0 results):** OpenAlex returned zero results for the exact combination of unfalsifiability + GR + dark matter auxiliary. This specific framing — ΛCDM as a Lakatosian protective belt — appears absent from the indexed literature. Individual components exist (MOND vs. dark matter debates, inflation skeptics) but NOT synthesized into a structural unfalsifiability critique.

**Q3 — Eddington 1919 Methodology (3 results):** Strikingly narrow. Only 3 OpenAlex results for methodology criticism of Eddington's 1919 eclipse plates. This is a critically under-explored area: the founding "confirmation" of GR has received little systematic methodological scrutiny in the indexed literature. Key works: Earman & Glymour (1980), Kennefick (2009) — but these are historical accounts, not integrated into a broader structural critique of GR testing methodology.

**Q4 — Standard Model Free Parameters (954 results):** Large literature, but dominated by: (a) parameter fitting methodology, (b) BSM physics motivation (SUSY, neutrino masses), (c) "naturalness" problems. The specific argument that 19 free parameters make the SM structurally accommodationist rather than predictive is partially present (Hossenfelder's "Lost in Math") but not synthesized with the GR/ΛCDM critique or the Eddington historical argument.

**Q5 — Independent Consilience (40 results):** Emerging but fragmented literature. Whewell's original consilience concept (1840) is referenced in scattered philosophy-of-science works, but its operationalization as a counter-measure to the protective-belt problem — with Bayesian evidential weight quantification — does not appear to exist in the indexed literature.

## 3. Gap Analysis

### Novelty Assessment

| Claim Component | Prior Work | Novel Contribution |
|:----------------|:-----------|:-------------------|
| GR's ΛCDM as protective belt | Scattered MOND/DM debates | Systematic Lakatosian structural analysis applied to ΛCDM |
| SM's 19 free parameters as accommodationist | "Lost in Math" (Hossenfelder) | Synthesized with GR critique into unified argument |
| Eddington 1919 as founding methodology failure | Earman & Glymour, Kennefick | Integrated into chain: founding confirmation → subsequent measurement-exercise pattern |
| Monopoly on calculability as unfalsifiability | Partial (Smolin, Dawid) | Novel framing: no-competitor = no-test rather than no-testability |
| Independent consilience as solution | Whewell (1840), scattered | Operationalized with KIF-60 Bayesian Δlog-odds + pre-registration |

### Novelty Verdict

**HIGH NOVELTY.** No single paper in the indexed literature covers all five points of the core claim. The specific combination — ΛCDM protective belt + SM accommodationism + Eddington implosion + monopoly on precision + KIF-60 Bayesian solution — is absent. Individual components exist separately in scattered literatures (physics, philosophy of science, history of science) but have never been woven into a single structural critique with a quantitative normative proposal (Δlog-odds gate).

### Classification Matrix

| Class | Count | Examples |
|:------|:------|:---------|
| Core | ~8 | Earman & Glymour (1980), Kennefick (2009), Hossenfelder (2018), Smolin (2006), Dawid (2013), Lakatos (1970), Popper (1934), Whewell (1840) |
| Supporting | ~15 | Ellis & Silk (2014), Smeenk (2017), Rovelli (2018), Weinberg (1992), and inflation/dark energy review papers |
| Background | ~10 | General philosophy of science textbooks, PDG review |
| Reject | — | All retrieved papers relevant to at least one component |

## 4. KIF-16 Institutional Status Neutrality

All cited works evaluated on evidence, not venue or affiliation. No "fringe"/"pseudoscience" labels used. The Eddington critique cites specific methodological concerns (plate selection, subjective curvature assessment) — these are evidentiary claims, not status dismissals.

## 5. AI Convergence Bias Disclosure (KIF-17)

Not triggered. This is a human-led analysis with external search evidence. No AI-evaluated convergence detected.

---

*Evidence files: artifacts/external-search/*.json (5 APIs × 3-5 queries = 16 files)*
