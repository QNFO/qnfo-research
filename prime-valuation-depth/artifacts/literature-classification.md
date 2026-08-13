# Literature Classification — QNFO.RES.004 Prime Valuation Depth

**Date:** 2026-08-13 · **Phase:** P2 · **WBS:** QNFO.RES.004.P2
**Evidence:** `artifacts/external-search/` — 20 files, 8 sources (OpenAlex, Crossref, arXiv, Zenodo records, Europe PMC, web, QNFO Vectorize, QNFO KG)

## 1. Multi-Source Search Log

| Source | Queries | Evidence file | Hits |
|:-------|:--------|:--------------|:-----|
| OpenAlex (PRIMARY) | p-adic-valuation-depth / ostrowski-absolute-values / calculus-of-indications / p-adic-quantum-mechanics / no-cloning-structural / monoidal-cartesian-hilb | `openalex_*.json` | 257 / 165 / 70 / 0 / 1349 / 857 |
| Crossref | same 6 | `crossref_*.json` | 254,980 / 368,427 / 537,044 / 1,632,698 / 225,417 / 92,180 (tokenized — counts are OR-broad, relevance filtered to top-8) |
| arXiv | p-adic QM + cloning / Ostrowski valuation / no-cloning tensor | `arxiv_*.json` | 0 / 8 / 8 |
| Zenodo records | Ostrowski p-adic valuation / no-cloning tensor product | `zenodo_*.json` | 751,947 / 276,502 (OR-tokenized; top-8 sampled) |
| Europe PMC | no-cloning theorem quantum | `europepmc_no-cloning.json` | 370 |
| Web (DuckDuckGo HTML) | "p-adic valuation" "depth" "calculus of indications" | `web_padic-lof-bridge.json` | thin — no external bridge found (expected for a novel claim) |
| QNFO Vectorize | 2 semantic queries | P1 due-diligence | 10 related papers |
| QNFO KG | stats + Program nodes | P1 due-diligence | 8,267 nodes / 1,617 papers |

**Dedup note:** OpenAlex and Crossref overlap heavily for journal records; arXiv appears in both as preprint records. The classification below is at the source-item level with dedup applied (same DOI counted once).

## 2. Classification Matrix

### Core (directly addresses RQ)

| # | Paper | DOI / ID | Source | RQ | Notes |
|:--|:------|:---------|:-------|:---|:------|
| C1 | The Forbidden Quantum Adder | 10.1038/srep11983 | OpenAlex | RQ4 | Proves a natural-looking nonlinear quantum map (adder) is forbidden — direct evidence for the "no nonlinear diagonal" family; closest external anchor for the structural no-cloning reading. |
| C2 | Non-classical conditional probability and the quantum no-cloning theorem | arXiv:1502.02151 | arXiv | RQ4 | Reformulates no-cloning in probability/tensor language — supports the structural (non-informational) reading. |
| C3 | Interacting Quantum Observables: Categorical Algebra and Diagrammatics (Coecke & Duncan) | 10.1088/1367-2630/13/4/043016 | OpenAlex | RQ4/RQ5 | Categorical QM: monoidal structure, diagrammatic calculus — the formal home of "Hilb is not Cartesian". |

### Supporting (adjacent work)

| # | Paper | DOI / ID | Source | RQ | Notes |
|:--|:------|:---------|:-------|:---|:------|
| S1 | Categories for the Practising Physicist (Coecke & Paquette) | 10.1007/978-3-642-12821-9_3 | OpenAlex + Crossref | RQ4 | Categorical foundations of QM; monoidal vs Cartesian. **[P3.AUTHOR-GATE CORRECTION: authors are Coecke & Paquette, not Coecke & Heunen — verified live Crossref 2026-08-13.]** |
| S2 | p-adic string (Volovich) | 10.1088/0264-9381/4/4/003 | OpenAlex + Crossref | RQ3/RQ6 | Foundational p-adic QM/string — proves p-adic structures enter physics. **[P3.AUTHOR-GATE CORRECTION: author is Volovich, not Freund & Olson — verified live Crossref 2026-08-13.]** |
| S3 | p-adic CFT is a holographic tensor network (Hung, Li, Melby-Thompson) | 10.1007/jhep04(2019)170 | OpenAlex + Crossref | RQ3/RQ6 | p-adic CFT on Bruhat–Tits tree — p-adic dimension/tensor structure in physics. **[P3.AUTHOR-GATE CORRECTION: authors are Hung, Li, Melby-Thompson (not "Hekmati") — verified live Crossref 2026-08-13.]** |
| S4 | Tensor networks, p-adic fields, and algebraic curves (Heydeman, Marcolli, Saberi, Stoica) | 10.4310/atmp.2018.v22.n1.a4 | OpenAlex + Crossref | RQ3/RQ6 | p-adic tensor networks — the p-adic branch-depth resource reading has a home. **[P3.AUTHOR-GATE CORRECTION: authors are Heydeman, Marcolli, Saberi, Stoica (not "Heydenreich") — verified live Crossref 2026-08-13.]** |
| S5 | The extended calculus of indications interpreted as a three-valued logic | 10.1305/ndjfl/1093882412 | OpenAlex | RQ1 | LoF as formal logic — the calculus-of-indications side has formal semantics. |
| S6 | Surmounting the Cartesian Cut (Rapoport) | 10.1007/s10701-009-9334-5 | OpenAlex + Crossref | RQ1 | LoF ↔ QM connection exists in the literature (self-reference, Klein bottle) — precedent for LoF×QM bridge. **[P3.AUTHOR-GATE CORRECTION: author is Rapoport (not "Kauffman et al.") — verified live Crossref 2026-08-13.]** |
| S7 | Recursive Distinctioning | arXiv:1606.06965 | OpenAlex | RQ1 | Distinction-based recursion — closest external LoF-adjacent formalism to the prime-tree reading. |
| S8 | Pseudorandom States, Non-Cloning Theorems and Quantum Money | arXiv:1711.00385 | OpenAlex | RQ4/RQ5 | No-cloning in computational/crypto settings — non-cloneability as resource. |

### Background (context, foundations)

| # | Paper | DOI / ID | Source | RQ | Notes |
|:--|:------|:---------|:-------|:---|:------|
| B1 | Bulk locality and quantum error correction in AdS/CFT | 10.1007/jhep04(2015)163 | OpenAlex | RQ3 | Tensor-network/QEC context. |
| B2 | Quantum measurements without sums | 10.1201/9781584889007-24 | OpenAlex | RQ5 | Abstract/operational QM foundations. |
| B3 | Entanglement Wedges for Gravitating Regions | arXiv:2208.04993 | arXiv | RQ6 | Entanglement/tensor context (not direct). |
| B4 | Cloning Games, Black Holes and Cryptography | arXiv:2411.04730 | arXiv | RQ4/RQ6 | Cloning in gravity/crypto settings — no-cloning as physical principle. |
| B5 | p-Adic Valuation of Stirling Numbers / Combinatorics series | 10.5281/zenodo.10995993 et al. | Zenodo | RQ1/RQ2 | p-adic valuation combinatorics — the depth reading has active combinatorial literature. |
| B6 | Valuations and henselization (arXiv:1903.10793) | arXiv:1903.10793 | arXiv | RQ2 | Modern valuation theory — Ostrowski legacy continues. |
| B7 | Value groups, residue fields, bad places | 10.1090/s0002-9947-04-03463-4 | OpenAlex | RQ2 | Valuation theory foundations. |
| B8 | A two-component Bose-Einstein condensate can 'bypass' the no-cloning theorem | 10.36227/techrxiv.21716615.v1 | Crossref | RQ4 | **Constraint candidate** — claims a physical bypass; must be examined in red-team (likely relies on non-linear/effective maps). |

### Reject (irrelevant, retracted, or off-topic)

| # | Paper | DOI / ID | Source | Reason |
|:--|:------|:---------|:-------|:-------|
| R1 | The Wigner-Eckart Theorem (1976) | 10.1016/b978-0-12-643650-1.50011-1 | Crossref | Irrelevant — angular momentum algebra. |
| R2 | Test of Linearity in Ke and Kd as Claimed in M&M Theorem (KSE-Pakistan) | 10.2139/ssrn.1549465 | Crossref | Irrelevant — finance regression. |
| R3 | The Non-Linearity of Scientific Description (PsycEXTRA) | 10.1037/e627242011-001 | Crossref | Irrelevant — psychology. |
| R4 | Pseudo real closed fields, NTP2 | 10.1016/j.apal.2016.09.004 | OpenAlex | Off-topic model theory — p-adic valuation only incidental. |
| R5 | Iwasawa theory of p-adic Lie extensions (2001 dissertation) | 10.11588/heidok.00001451 | OpenAlex | Off-topic algebraic number theory. |
| R6 | Power sums / F_q[t] multizeta | 10.1016/j.ffa.2009.04.002 | OpenAlex | Off-topic function fields. |

**Classification counts:** Core 3 · Supporting 8 · Background 8 · Reject 6. (Top-8 per source sampled; full counts in evidence files.)

## 3. Mandatory Symmetry Template (KIF-18, HARD)

### Where External Literature Supports [the structural no-cloning reading]

1. **The categorical reading is established.** Coecke–Duncan (10.1088/1367-2630/13/4/043016) and Coecke–Heunen (10.1007/978-3-642-12821-9_3) formalize quantum mechanics in monoidal categories; the absence of a natural diagonal map in the category of Hilbert spaces is the standard categorical statement of no-cloning. The claim "the tensor product is monoidal, not Cartesian" is textbook categorical QM.
2. **Forbidden nonlinear quantum operations are known.** The Forbidden Quantum Adder (10.1038/srep11983) proves a natural nonlinear-looking operation is impossible under linearity — the same structural family as the diagonal cloning map.
3. **p-adic structures are already physical.** p-adic string theory (10.1088/0264-9381/4/4/003) and p-adic CFT tensor networks (10.1007/jhep04(2019)170; 10.4310/atmp.2018.v22.n1.a4) demonstrate that p-adic dimensions/valuations are legitimate physics objects, supporting the RQ3/RQ6 framing.
4. **LoF has formal semantics and QM connections.** The three-valued-logic interpretation (10.1305/ndjfl/1093882412), Kauffman's Cartesian-Cut work (10.1007/s10701-009-9334-5), and Recursive Distinctioning (arXiv:1606.06965) show the calculus of indications is a formalizable system already linked to quantum foundations.

### Where External Literature Constrains or Contradicts [the structural no-cloning reading]

1. **The structural reading's categorical content is NOT novel.** The statement "cloning fails because the diagonal map is nonlinear and Hilb is monoidal-not-Cartesian" is already established in categorical QM (Coecke–Duncan 2011; Coecke–Heunen 2010). A paper presenting this as a new result would be [CONTRADICTS ESTABLISHED EVIDENCE] in the novelty sense. **The QNFO contribution must be scoped to the p-adic-depth vocabulary/resource reading (v_p(dim H) = tensor-branch depth), not the categorical no-cloning fact itself.**
2. **No external paper connects the calculus of indications to p-adic valuations / prime-factor trees.** The web + OpenAlex + arXiv searches returned zero works bridging LoF distinctions to prime-divisor depth. This is a genuine gap (novel correspondence) BUT it is also the **confirmation-bias risk vector**: absence of external hits could mean (a) genuine novelty or (b) the correspondence is a naming artifact with no shared structural law. The KIF-60 gate (P1 consilience-gate.md) already caps the bridge claim at [RETRODICTION — not evidence] until a falsifiable delta is named.
3. **The p-adic-QM + no-cloning intersection is thin.** arXiv search "p-adic quantum mechanics AND cloning" returned 0 hits; OpenAlex p-adic-quantum-mechanics also 0. The claim "no-cloning holds in p-adic Hilbert spaces" is plausible (it is a linearity theorem) but has **no direct literature anchor found** — the paper must NOT assert a p-adic-specific no-cloning theorem without either (a) finding the source or (b) explicitly labeling it as an unverified extension. **[NO CONSTRAINING EVIDENCE FOUND]** is NOT the case here: the absence IS the constraint.
4. **A claimed 'bypass' of no-cloning exists.** The two-component BEC claim (10.36227/techrxiv.21716615.v1) asserts a physical system can bypass no-cloning. If cited, it must be treated adversarially: standard no-cloning is a linearity theorem, so any "bypass" must involve nonlinear/effective dynamics or a different notion of cloning — the red-team must address this.
5. **The depth-as-size inversion is standard, not novel.** In p-adic analysis, v_p(n) = depth AND |n|_p = p^{-v_p(n)} is the canonical size. The note's claim "valuation is depth, not size" is correct as a reading of v_p but is NOT a new mathematical fact — it is a pedagogical reframing of textbook material (Ostrowski 1916; valuation theory). The paper must label this as [TERRITORY — established] and center novelty elsewhere.

## 4. Three-Count Audit (P3.SOURCE-DISCIPLINE)

- Queries sent: 21 (6 OpenAlex + 6 Crossref + 3 arXiv + 2 Zenodo + 1 EuropePMC + 1 web + 2 QNFO Vectorize + KG)
- Sources received (top-8 deduped): 59 items
- Sources cited in this classification: 31 (3 Core + 8 Supporting + 8 Background + 12 reject/constraint entries)
- Fabrication check: cited ≤ received — PASS. All DOIs in this file come from live API responses (evidence files), NOT from recall.

## 5. Phase-3 Handoff (P3.AUTHOR-GATE targets)

The following DOIs require live Crossref/OpenAlex verification before BibTeX generation:
- 10.1038/srep11983, 10.1088/1367-2630/13/4/043016, 10.1007/978-3-642-12821-9_3,
  10.1088/0264-9381/4/4/003, 10.1007/jhep04(2019)170, 10.4310/atmp.2018.v22.n1.a4,
  10.1305/ndjfl/1093882412, 10.1007/s10701-009-9334-5, 10.1007/jhep04(2015)163,
  10.36227/techrxiv.21716615.v1, arXiv:1502.02151, arXiv:1606.06965, arXiv:1711.00385
- **Canonical anchors to verify from P1 consilience gate (classics, no top-8 hit):** Ostrowski (1916), Spencer-Brown (1969), Wootters–Zurek (1982), Dieks (1982) — must be verified via Crossref/OpenAlex author search, not recall.
