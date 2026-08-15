# Phase 2 Literature Review — QNFO.RES.010 (exchange-phase-logical-scalar)

**Date:** 2026-08-14 | **WBS:** QNFO.RES.010 | **Branch:** res/paper/exchange-phase-logical-scalar
**Phase-1 frame:** G1–G5 (from artifacts/due-diligence-phase1.md)
**Method:** 8 parallel sources attempted: arXiv API, Crossref, OpenAlex, Zenodo, EuropePMC, Semantic Scholar, DBLP, Google Patents (paced). This cycle completed successfully for **arXiv (Q1, Q2), Crossref (Q1, Q2, Q4-partial), OpenAlex (Q1, Q2), Google Patents (Q1)**. Zenodo/EuropePMC/S2/DBLP and Crossref Q4 were rate-limited or timed out this cycle (`[NOT-VERIFIED]` — retry in P3 citation pass with pacing).
**Classification:** KIF-18 Mandatory Symmetry Template (each accepted work gets a symmetric treatment: claim / role / boundary / relation to RES.010).

## Queries

- **Q1** = `"exchange phase" "half-turn" spin statistics`
- **Q2** = `"laws of form" exchange statistics Spencer-Brown`
- **Q4** = `spin-statistics braided tensor category ribbon identity anyon` (Crossref only; 429)

## Results by source

| Source | Query | Result |
|---|---|---|
| arXiv | Q1 | 8 hits — **all noise** (six-vertex model, brain networks, spin asymmetries, statistical inference). No exchange-phase × half-turn work. |
| arXiv | Q2 | 8 hits — **all noise**. No Laws-of-Form × exchange-statistics work. |
| Crossref | Q1 | EPL evasion paper (10.1209/0295-5075/ac97bd + erratum acabe2) + geometric-phase chapter (10.1142/9789813221215_0008) — both already known from Phase 1. No new relevant work. |
| Crossref | Q2 | Laws-of-Form German monographs (Kaehr's "Laws of Form" appendices/contexts, 2004/2009) — background, no exchange-statistics content. |
| Crossref | Q4 | **HTTP 429** — `[NOT-VERIFIED, retry in P3]` |
| OpenAlex | Q1 | **0 results** — corroborates novelty of the exact-phrase combination. |
| OpenAlex | Q2 | **"A Review of Majorana fermions and the laws of form"** (2022, J. Phys.: Conf. Ser. 2197 012001, DOI 10.1088/1742-6596/2197/1/012001) — **NEW find; Laws-of-Form × fermion literature, must be engaged.** Plus noise (power laws in economics, energy democracy, neutrosophy proceedings). |
| Google Patents | Q1 | **total=0** — exact-phrase patent novelty **VERIFIED** (re-runs Phase-1 NOT-VERIFIED check). No patent claims the exchange-phase × half-turn × spin-statistics combination. |
| Zenodo / EuropePMC / S2 / DBLP | — | timeouts / rate limits this cycle `[NOT-VERIFIED, retry in P3]` |

## Classification (KIF-18)

### Core (directly engages the invariant or its derivation target)
1. **Quni-Gudzinas, R. B. (2026). The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant. DOI 10.5281/zenodo.21938971** — internal parent (RES.009). Claim: R = e^{2πis}; dichotomy is its 3+1D shadow. Role: prior claim + derivation target. Boundary: symmetric-category η = ±1; T2 identifies η = −1 ↔ treatise half-turn; explicitly does NOT write (e^{iπ})^{2s} nor claim full derivation. Relation: RES.010 delta = (e^{iπ})^{2s} composite monodromy power + e/π/R scalar-family + treatise-anchored derivation.
2. **Quni-Gudzinas, R. B. (2026). The Calculus of Re-Entrant Distinctions. DOI 10.5281/zenodo.21908818** — internal parent (treatise). Claim: e (D f = f), π (Tr id_S¹), half-turn e^{iπ} = −1 (§12.1); §2.3 marks parity → spin-statistics as [my conjecture]. Role: the machinery RES.010 derives from. Boundary: never constructs the exchange of two marks. Relation: RES.010 supplies the missing construction.

### Supporting (adjacent; must be cited and engaged in P5)
3. **"A Review of Majorana fermions and the laws of form" — Louis H. Kauffman (2022), J. Phys.: Conf. Ser. 2197 012001, DOI 10.1088/1742-6596/2197/1/012001** (author verified live via Crossref this cycle) — Laws-of-Form representation of fermion structure. Kauffman is a knot-theory/Laws-of-Form authority; his engagement with Majorana fermions through the mark calculus is the strongest external LoF-fermion literature and **must be engaged directly in P5's relation-to-prior-art**. Claim: connects Majorana fermions to the calculus of indications. Role: closest external LoF-fermion work; RES.010 must differentiate (exchange-phase invariant derivation vs representation of fermion algebra). Boundary: not the exchange-phase relation; no (2s)-fold half-turn. Relation: Supporting — evidence that LoF-fermion connections are active in the literature; strengthens novelty of the specific invariant claim. **P3 must pull full body.**
4. **"Spin-half bosons with mass dimension three-half: Evading the spin-statistics theorem" — Dharam Vir Ahluwalia & Cheng-Yang Lee (EPL 2023, DOI 10.1209/0295-5075/ac97bd; erratum acabe2)** — evasion strategy via mass-dimension-3/2 spinors. Role: F2-relevant (empirical escape hatch class). Boundary: attacks the standard theorem statement, not the invariant R itself. Relation: RES.010's F2 (inherited RES.009 F1) already covers the general evasion class.
5. **"Indistinguishability for quantum particles: spin, statistics and the geometric phase" — M. V. Berry & J. M. Robbins (2017 book chapter, DOI 10.1142/9789813221215_0008)** — the canonical geometric-phase construction of spin-statistics. Role: closest external conceptual neighbor (Berry-type monodromy). Boundary: not LoF-native. Relation: RES.010's monodromy-power reading is distinct and LoF-native; P5 should acknowledge the Berry–Robbins lineage explicitly.

### Background (context; optional citation)
6. **Kaehr, R. "Laws of Form" commentaries (2004/2009, Springer book chapters)** — German-language LoF scholarship. Role: LoF literature context. Not exchange-statistics. Optional citation in relation-to-prior-art.
7. Mainstream spin-statistics anchors (Pauli 1940; Leinaas–Myrheim 1977; Wilczek 1982; Duck–Sudarshan 1998; Joyal–Street 1993; Kitaev 2006) — already verified in RES.009's citation-audit; carried forward.

### Reject (with reason)
- arXiv Q1/Q2 statistics/noise hits (brain networks, six-vertex, sparse PCA, spin asymmetries, recidivism, Lévy processes) — no relevance.
- Crossref Q1: half-turn split inductor (RF hardware), transparent conductors, SSRN posted-content — no relevance.
- OpenAlex Q2: power laws in economics, energy democracy, neutrosophy proceedings, collective memory — no relevance.

## KIF-18 Mandatory Symmetry Template

| Work | Claim (one line) | Role | Boundary | Relation to RES.010 |
|---|---|---|---|---|
| RES.009 (parent) | R = e^{2πis} invariant; dichotomy = 3+1D shadow | Prior claim + target | η = ±1 symmetric only | Delta: (e^{iπ})^{2s} composite + scalar family + full derivation |
| Treatise (parent) | e, π, half-turn from the mark | Machinery | No two-mark exchange | Supplies the primitive RES.010 uses |
| Majorana–LoF review (2022) | LoF represents fermion structure | Supporting/adjacent | No exchange-phase invariant | Differentiates RES.010's invariant claim |
| EPL evasion (2023) | Mass-dimension-3/2 evades S-S theorem | Supporting/F2 | Attacks theorem, not invariant | F2 covers evasion class |
| Geometric-phase chapter (2017) | Geometric phase × statistics | Supporting | Not LoF-native | Acknowledge lineage; distinct reading |

## Novelty verdict (updated)

Crossref (Q1/Q2) + OpenAlex (Q1 = 0 results; Q2 no invariant claim) + Google Patents (Q1 = 0) + arXiv (Q1/Q2 = noise): **no external prior art derives the exchange phase as a (2s)-fold half-turn of the re-entrant mark or states the e/π/R scalar-family unification.** The Majorana–LoF review is the nearest LoF-fermion literature and is Supporting, not a blocker. Net-new claim stands.

## Gate

**P2 gate: PASS** (with `[NOT-VERIFIED]` disclosures for Zenodo/EuropePMC/S2/DBLP/Crossref-Q4 — retried in P3 citation pass).
