# Deep Due-Diligence Addendum — Corpus-Wide Sweep for the Prime-Valuation-Depth Thread

**Project:** QNFO.RES.005/RES.006 | **Date:** 2026-08-14 | **Trigger:** user directive — "more in-depth due diligence when executing research" (corpus ~1,000 records and growing)
**Method:** KG (stats + 10 topic sweeps + neighbors of both papers), D1 living-paper census (986 rows / 431 distinct Zenodo DOIs), Vectorize semantic sweeps (5 queries × 2 backends), durable-memory sweep (recall_facts × 6 + search_memories × 2), live Zenodo/Crossref/arXiv verification of every critical hit.

## G1 — The "first reproduction attempt" was not first; the decisive evidence was missed (HARD)

`ACRP-06` — *Extending v_p^max Code Classification* (Zenodo **21737222 v1.0**, 2026-08-01; **21754148 v1.1 erratum**, 2026-08-02; program ACRP, project ACRP-06, planned in the ACRP v1.0 program document) tested NTOF's C7.3' on 8 additional families **twelve days before** RES.006's rq3 run.

- v1.0 verdict: "C7.3 bounded — Golay CSS confirmed at v_p^max=28 … The 28 vs 4 gap is a Golay-specific property of self-dual weight distributions, not a general code-classification discriminant."
- v1.1 **ERRATUM**: "Corrected Golay v_p^max values from 28 to 2/4. Independent BP-10 recomputation confirmed original values unreproducible."

Consequences:
1. The Mahler "28" has now failed **two independent reproductions plus an erratum chain** (ACRP-06 v1.1: Golay = 2/4; RES.006 rq3: optimal 4, random 3).
2. RES.006's §6/§9/abstract "first reproduction attempt" framing was factually false — withdrawn on the corrections branch.
3. The KG node `paper:acrp06-vpmax-extension` points at the superseded v1.0 (DOI 21737222) — stale KG data propagated the error. Fixed this turn.
4. This record's own pipeline had ACRP-06 within reach (KG, Vectorize, memory all carried it) and missed it → anti-pattern `DUE-DILIGENCE-SIBLING-MISS-1`.

## G2 — The anchor's LoF↔prime-tree bridge is pre-empted in-corpus and uncited (HARD)

- *The Calculus of Distinction: A Formal Isomorphism Between Laws of Form and Ultrametric Trees* (**21205097**, 2026-07-05) — states the anchor's Statement 2 correspondence, five weeks earlier.
- *Quantum Laws of Form: Superposition as Re-Entry, Measurement as Distinction* (**21205110**, 2026-07-05) — pre-empts part of the quantum extension.
- *The Calculus of Re-Entrant Distinctions* (**21908818**, 2026-08-12, v0.8) — "completions of the rational numbers … the mathematical structure of quantum theory … zitterbewegung," published one day before the anchor.

None are cited by the anchor (21918838) or follow-on. The follow-on's due-diligence claim that the calculus-of-indications bridge is "unique to the Prime Valuation Depth lineage" is **false**. Remediation: RES.005 action list item 3 (cite priors; restate contribution as the *valuation-depth vocabulary*).

## G3 — rq3 F2 was wrong twice: mathematically and factually (HARD, now fixed)

- Mathematics: |c_j| ≤ 2^(n−k) · Σ_{i≤j} C(j,i) = 2^(n−k+j) ⇒ v₂ ≤ n−k+j (not n−k). v₂=28 is satisfiable at n=18, impossible only for n≤13.
- Fact: NTOF handles "up to n=64 qubit codes"; its Table 1 maxima (15/14/28) sit far above the pipeline's observations.
- Independent corroboration: ACRP-06 v1.0 initially *confirmed* 28 on Golay (n=23, k=12 — outside the n≤18 premise entirely), then v1.1 retracted it. The empirical NOT-REPRODUCED conclusion stands; the impossibility proof does not.

## G4 — KG data defects (root causes of downstream errors)

1. `paper:qec-darwinism-ultrametric`: node name "Ultrametric Code Spaces: The Bruhat–Tits Tree as a Geometry for QEC" but DOI **21819232** = *Archimedean Shadows* (live-verified). Root cause of the due-diligence.md title↔DOI swap (already corrected in the branch DD). Fixed this turn (name aligned to the DOI's live title; Bruhat-Tits QEC = 21824195, draft).
2. `paper:acrp06-vpmax-extension` → superseded v1.0 DOI; erratum fields added this turn.
3. Mass duplicate Paper nodes per DOI (21193487 ×4, 21205100 ×3, 20570212 ×3, 20119700 ×3, Hensel ×7) — needs a KG reconciliation run.
4. Node-name search returns 0 for topics ("no-cloning", "room temperature", "Kodaira") even when papers exist — topic coverage requires the semantic layer.

## G5 — Memory-layer staleness

The 2026-07-24 Consilient Synthesis memory states "Mahler v_p spectral discriminant separates optimal from random codes 7:1 (computationally verified)." Disconfirmed by ACRP-06 v1.1 + RES.006 rq3. A corrective durable fact was written this turn; the stale synthesis document itself should be amended in its next revision.

## Corpus coverage map (WBS legs)

| Leg | Density | Notable corpus items | Gaps |
|:----|:--------|:---------------------|:-----|
| UMP (p-adic/ultrametric) | Very dense (50+ hits) | NTOF (21193487), Hensel ×7, Morita Γ (20119700), Q-PNA (20287743), Bridge Theorem (21102770), Radix→Bruhat-Tits (21102764), p-adic anyons/braids/Temperley-Lieb (21208491/21208366/21208368), Adelic Cross-Domain (21546243), Ostrowski reformulation (21751722) | — (under-citation is the issue, not absence) |
| SLB (Laws of Form) | Dense (9+ hits) | Calculus of Distinction (21205097), Quantum LoF ×5 (21205110/21205582/21206074/19598745/21205554), Principia Ontologica, Re-Entrant Distinctions (21908818), Cancellation Rule (21470438) | **Bricken Unitary Logic / void-equivalence / unary computers: zero coverage** (note 08-12) |
| INM (QEC/no-cloning) | Very dense (~30 hits) | Adelic QEC ×10, Bruhat-Tits QEC/processor/validation ×8, Qudit QEC (21046993), ACRP-06, classifier verification (21698279), bosonic/GKP (x3.3), holographic QEC (x3.4) | — |
| CFE (hardware/room-temp) | Sparse on this thread | Qudit Advantage JPCUB (21880104, errata published), Signal-Worker ambient-superconductivity series, external qudit processors (Ringbauer 2022/2023/2024) | **Room-temperature qudit coherence validation: zero hits** (note 08-07) |
| RES (consilience) | Dense | 29-Schisms (21458373), Consilience Physics↔Number Theory (21590155), QWAV Decade (21722393), Ultrametric Consilience Atlas (21722395) | RES.005/006 not yet linked into the consilience fabric |

## Corrected scientific position for C8 / FQ1

The 83% Kodaira–Néron claim remains UNVERIFIED-INTERNAL. The Mahler leg now has **two negative reproductions and an internal erratum** — the prior probability that "28" is real is very low, and the open question shifts from "reproduce 28" to **"what did NTOF's Mahler computation actually compute?"** (the registry P0 clarification, now with two independent failure datasets + ACRP-06's Golay finding to anchor it). The rq3 companion artifacts carry the corrected F2/F2b.

## Net-new research opportunities (unworked corpus gaps)

1. **[CFE] Room-temperature qudit coherence** — zero corpus coverage; closest work is energy-metric (JPCUB). Pre-registrable desk-based literature audit → falsifiable prediction for the ultrametric error model at T=300 K.
2. **[SLB] Bricken's Unitary Logic / void-equivalence** — zero coverage; the reversible-computing/Landauer corpus (Physics of Computation, 21255013) is the natural anchor.
3. **[UMP/INM] The p=2-privilege critique** — "qubits are just the p=2 branch" is asserted across papers but has no dedicated foundational treatment; qudit QEC externals (Wills, Spagnoli, Uy, …) are already in the bib.

## Program-level fixes executed this turn

- Corrective memory: stale 7:1 synthesis claim superseded (durable memory updated).
- Anti-pattern logged: `DUE-DILIGENCE-SIBLING-MISS-1`.
- KG: ACRP-06 erratum fields added; qec-darwinism-ultrametric name/DOI conflation fixed (verified by re-query).
