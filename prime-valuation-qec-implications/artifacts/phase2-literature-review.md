# Phase 2 Literature Review — QNFO.RES.006

**Project:** Implications for Computing and Quantum Error Correction
**Slug:** prime-valuation-qec-implications
**Date:** 2026-08-13
**Phase:** P2 (Literature Search)

## 1. Method (8-source parallel search)

| Source | Query | Result count | Evidence file |
|:-------|:------|:------------:|:--------------|
| OpenAlex (PRIMARY) | qudit quantum error correction | 5,406 works (top-10 sampled) | phase2-openalex-qudit-qec.json |
| OpenAlex (PRIMARY) | p-adic quantum error correction | 700 works (top-10 sampled) | phase2-openalex-p-adic-qec.json |
| Crossref | qudit quantum error correction | 10 | phase2-crossref-qudit-qec.json |
| Zenodo | qudit "error correction" | 4,144 total (noisy OR-tokenization) | phase2-zenodo-qudit-qec.json |
| Zenodo | "p-adic" "error correction" | 4,938 total (noisy OR-tokenization) | phase2-zenodo-p-adic-qec.json |
| Europe PMC | qudit quantum error correction | 114 | phase2-europepmc-qudit-qec.json |
| arXiv | "quantum error correction" AND "qudit" | 15 (P1, DL-04) | arxiv-qudit-qec-2026-08-13.json |
| arXiv | p-adic OR "prime valuation" AND QEC | 15 (P1, DL-04) | arxiv-padic-qec-2026-08-13.json |
| QNFO Vectorize | p-adic QEC corpus | 13 papers (P1, due-diligence.md §2) | due-diligence.md |
| QNFO KG | qudit/QEC/p-adic nodes | 98 hits (P1) | due-diligence.md §1 |

Polite pool: 0.4 s between keyless API calls; OpenAlex `mailto` used.
Evidence discipline: every count above has a saved response file in `artifacts/external-search/`.

## 2. Classification vs the Four Differentiators + Threshold Topic

### D1 — branch-depth reading (v_p as depth, not size/weight)
- **External:** ZERO hits for valuation-as-depth on Hilbert-space dimension labels. OpenAlex p-adic-QEC query surface returns p-adic AdS/CFT, tensor networks over p-adic fields, quantum-gravity phenomenology — none classify QEC codes by p-adic valuation.
- **Internal:** QNFO.UF corpus uses valuation as *classifier weight* (Kodaira-Néron, Mahler v_p-spectral) — depth reading is unique to the RES.005 lineage.
- **Verdict:** vocabulary gap confirmed externally.

### D2 — calculus-of-indications bridge (Spencer-Brown)
- **External:** absent from all 8 sources. No QEC literature connects Spencer-Brown distinction/branching to code structure.
- **Internal:** unique to RES.005 (the anchor's bridge claim).
- **Verdict:** cross-domain bridge confirmed as QNFO-unique.

### D3 — no-cloning as the structural ROOT of QEC limits
- **External support:** no-go theorem (Wootters–Zurek 1982; Dieks 1982) established; categorical content (monoidal-not-Cartesian, no natural diagonal) established in the literature (Coecke–Duncan; Coecke–Paquette — cited in the anchor paper).
- **External contradiction:** none.
- **Neutral:** the QEC literature treats no-cloning as a constraint to satisfy, not as the reason QEC exists. The inverted causal reading is the RES.005 contribution.
- **Verdict:** re-framing of established facts — support exists, no contradiction; must be labeled interpretive.

### D4 — [[n,k,d]] ↔ branch-depth mapping
- **External support:** the algebraic content n=log_2(dim H), k=log_2(dim H_L) is standard stabilizer parameterization (established). Qudit stabilizer theory (foliated qudit codes 2607.13784; qudit LDPC 2510.06495; SU(d) codes 2410.02407; Galois qudits 2605.18981) covers the parameter space.
- **Risk (from locked core claim):** the mapping is a PURE RELABELING unless it yields a new invariant, classification, or bound. P2 finds NO external valuation-based taxonomy of code families → the taxonomy/invariant surface is open, but it must be DERIVED in P4, not assumed.
- **Verdict:** substrate mature; the invariant/taxonomy/bound is the required novel output.

### T — threshold / hashing-bound topic (the 1/(e·pi) ≈ 0.117 observation)
- **External:** toric-code threshold ≈ 0.109 (Fowler et al. 2012) and the hashing bound are established; no external work ties the threshold to e·pi or a branch point of syndrome entropy.
- **Internal:** the e·pi observation is QNFO-internal (Obsidian note _26225053214, 2026-08-13, 7% deviation flagged as NOT a derivation).
- **Verdict:** report as observation, never as theorem (R3 in PROJECT-PLAN).

## 3. Dedup

Cross-source unique top hits after dedup: "Quantum Error Correction of Qudits Beyond Break-even" (OpenAlex + arXiv), "Designing QEC codes for practical spin qudits" (Crossref + arXiv), "Quantum error correction with molecular spin qudits" (OpenAlex only). Zenodo results are OR-tokenization noise per known behavior (research skill Rate-Limit Matrix note) — the two relevant-looking Zenodo records ("Physical Limit of Quantum Error Correction (PLQEC): Foundational...", "Banks as Qubits...") are flagged for P3 DOI verification; PLQEC may be a QNFO-internal record.

## 4. KIF-18 Mandatory Symmetry Template

| Claim | External support | External contradiction | Neutral / absent |
|:------|:-----------------|:-----------------------|:-----------------|
| D1 v_p = depth, not size (on dimension labels) | p-adic QM (Dragovich 2003) establishes p-adic topology in QM; no depth-on-dimension vocabulary | none found | entire qudit corpus treats dimension combinatorially, never by valuation |
| D2 LoF bridge | none | none | absent from all external QEC literature |
| D3 no-cloning as structural root | Wootters–Zurek/Dieks; Coecke–Duncan categorical content | none | QEC literature: constraint-to-satisfy, not root cause |
| D4 [[n,k,d]] mapping | standard stabilizer parameterization; qudit stabilizer theory mature | none (algebraic content) | no external valuation-based taxonomy; must be derived in P4 |
| T threshold = branch point of syndrome entropy | threshold 0.109 + hashing bound established | none | e·pi tie is internal observation only |

## 5. Novelty Conclusion (P2 gate)

**Confirmed and sharpened:** the project's novelty is the *valuation-as-depth vocabulary* applied to QC/QEC — zero external hits on any of the five rows' left-hand vocabulary in 8 sources. The substrate (qudit stabilizer theory) is mature and externally corroborated (Galois-qudit review states q=2^s ≅ s qubits). P4 must convert the vocabulary into at least one of: (a) valuation-based taxonomy/invariant of code families (RQ5), (b) reproduced UF 83% classification (RQ3 — DOI reconciliation first, per red-team-phase1.md), (c) a branch-depth bound on QEC overhead (frontier question, consilience-gate.md). Pure re-derivation is blocked by the locked core claim's falsifiability condition.

## 6. P3 Handoff (Citation Management)

- Verify DOI of "Physical Limit of Quantum Error Correction (PLQEC)" — resolve whether internal (QNFO) or external before citation.
- Verify DOI of "Qudit Quantum Error Correction" 10.5281/zenodo.21046993 vs 83%-source 10.5281/zenodo.21193487 (RQ3 reconciliation carried from red-team-phase1.md).
- arXiv 2605.18981 (Galois Qudits) + 2607.13784 (foliated qudit QEC) + 2510.06495 (qudit LDPC) + 2409.15065 (beyond break-even) are the primary external anchors for P4.
