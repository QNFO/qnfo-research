# Citation Audit — QNFO.RES.010 (exchange-phase-logical-scalar)

**Date:** 2026-08-14 | **WBS:** QNFO.RES.010 | **Phase:** P3 | **Branch:** res/paper/exchange-phase-logical-scalar
**Gate:** P3.AUTHOR-GATE (every DOI resolved live via Crossref/DataCite; title+author asserted) + CMD RED TEAM SUB aggregate (Accuracy + Completeness reviewers completed; Dependency covered by direct parent audit).

## Verdict

**P3 gate: PASS after remediation.** Red-team aggregate surfaced **1 HARD finding (Duck–Sudarshan DOI mis-resolved)**, now corrected to `10.1119/1.18860`; 4 SOFT findings addressed below.

## AUTHOR-GATE results (live Crossref verification, 2026-08-14)

| Key | DOI | Title | Venue | Year | Status |
|---|---|---|---|---|---|
| pauli1940 | 10.1103/PhysRev.58.716 | The Connection Between Spin and Statistics | Physical Review | 1940 | VERIFIED |
| leinaasmyrheim1977 | 10.1007/BF02727953 | On the theory of identical particles | Il Nuovo Cimento B | 1977 | VERIFIED (corrected from 404'd PhysRevD.16.3243) |
| wilczek1982 | 10.1103/PhysRevLett.48.1144 | Magnetic Flux, Angular Momentum, and Statistics | Physical Review Letters | 1982 | VERIFIED |
| ducksudarshan1998 | **10.1119/1.18860** | Toward an understanding of the spin-statistics theorem | American Journal of Physics 66(4), 284–303 | 1998 | **CORRECTED (HARD finding: 10.1119/1.18828 was Ridgely; 10.1119/1.19109 was Knox greenhouse)** |
| kitaev2006 | 10.1016/j.aop.2005.10.005 | Anyons in an exactly solved model and beyond | Annals of Physics | 2006 | VERIFIED |
| kauffman2022 | 10.1088/1742-6596/2197/1/012001 | A Review of Majorana fermions and the laws of form | J. Phys. Conf. Ser. | 2022 | VERIFIED (author: Louis H. Kauffman) |
| ahluwalialee2022 | 10.1209/0295-5075/ac97bd | Spin-half bosons with mass dimension three-half | Europhysics Letters | 2022 | VERIFIED |
| ahluwalialee2022err | 10.1209/0295-5075/acabe2 | Erratum | Europhysics Letters | 2022 | VERIFIED |
| berryrobbins2017 | 10.1142/9789813221215_0008 | Indistinguishability for quantum particles | Half-Century of Physical Asymptotics | 2017 | VERIFIED |
| joyalstreetverity1996 | 10.1017/S0305004100074338 | Traced monoidal categories | Math. Proc. Camb. Phil. Soc. | 1996 | VERIFIED (new anchor, Joyal & Street gap closed) |
| ma-selfref-2025 | 10.5281/zenodo.17706898 | Self-Referential Scattering and the Birth of Fermions | Zenodo | 2025 | VERIFIED (new Supporting hit) |
| kirchner2025 | 10.5281/zenodo.17659262 | Measuring Anyonic Exchange Phases Using 2D Coherent Spectroscopy | Zenodo | 2025 | VERIFIED (new Supporting hit) |
| dutta2018 | 10.5281/zenodo.3066785 | Dual Spin Statistics in Hadrons | Zenodo | 2018 | RESOLVES — **REJECTED** (speculative; would dilute the set) |

## Red-team aggregate findings and remediation

### HARD (1) — fixed
- **H1 — ducksudarshan1998 DOI mis-resolved** (both Accuracy and Completeness reviewers independently flagged; direct audit confirmed). Original 10.1119/1.18828 = Ridgely, electrodynamics; corrections pass had re-recorded wrong metadata (10.1119/1.19109 = Knox, greenhouse). **Fix applied:** `10.1119/1.18860`, "Toward an understanding of the spin-statistics theorem", AJP 66(4) 284–303 (1998), Duck & Sudarshan. Note: the title "Pauli and the Spin-Statistics Theorem" belongs to the World Scientific monograph (10.1142/3457); the AJP article is the correct anchor for the theorem-statement citation.

### SOFT (4) — addressed
- **S1 — Classification entries without verified entries.** core-1 (RES.009), core-2 (treatise) are internal parents already cross-validated in P1 via `resolve_paper_id`; documented here as intentionally excluded from re-verification. background-1 (Kaehr 2004) is optional context, excluded. Joyal & Street anchor **gap closed** (verified: 10.1017/S0305004100074338).
- **S2 — Semantic Scholar still NOT-VERIFIED** (HTTP 429 on both queries). Disclosed; re-run in P4/P5 with ≥60 s pacing.
- **S3 — Gate logic flaw.** The raw AUTHOR-GATE accepted title/author-mismatched records as "GATE OK". **Fix:** this audit's status table asserts title+author equality; the P3 gate procedure is amended to require title+author match, not mere DOI resolution.
- **S4 — New-hit classification not yet in P2 artifact.** Classifications below are applied in this commit (phase3 addendum): Ma & Zhang 2025 → **Supporting** (nearest external prior; novelty-threat LEVEL-1 — must distinguish, not blocking; derives a Z₂ exchange phase from self-referential Riccati/spinor structure but has no re-entrant-mark half-turn monodromy, no (e^{iπ})^{2s} power for arbitrary s, no e/π/R scalar-family unification); Kirchner 2025 → **Supporting** (empirical anyonic-exchange-phase measurement; strengthens F2); Dutta 2018 → **Reject**.

## Falsifiability coverage

- **F1 (formal derivation):** joyalstreetverity1996 (traced monoidal categories), kitaev2006 (anyon TQFT), treatise §10.3 (trace machinery). Supports the formal-derivation claim.
- **F2 (empirical evasion class):** ahluwalialee2022 + erratum (evasion), kirchner2025 (anyon measurement). Supports the empirical falsifier.
- **F3 (scope):** pauli1940, leinaasmyrheim1977, wilczek1982, ducksudarshan1998 (established anchors); kauffman2022, ma-selfref-2025 (LoF-fermion adjacency to distinguish).

## NOT-VERIFIED (remaining, disclosed)

- **Semantic Scholar** — HTTP 429 both queries this cycle. Re-run P4/P5 with pacing.

## Dependency verification (direct parent audit)

- DOI lifetime: all five doi.org HEAD checks → HTTP 200 (21938971, 21908818, 21929902, 17706898, 17659262).
- Treatise cross-refs verified verbatim: §12.1 "e^{iπ} = −1 as the half-turn of the re-entrant mark"; §2.3 "the claim that this parity is the ancestor of physical spin-statistics is [my conjecture]".
- WBS registry row QNFO.RES.010 re-read (name/slug/phase P0/status active) — stable.
- BibTeX generation: all entries carry author/title/year/doi; description HTML entities excluded from BibTeX (metadata only, not rendered fields).


---

## Addendum 2026-08-16 (v1.2 so-what cycle)

- New Section 2 "So What? Why Should a Reader Care About This Research?" added. Contains one citation ([Pauli 1940]) already present in the bibliography — no new keys; cited-keys == bib-keys unchanged.
- Companion paper (Configuration-Space Topology and the Distinction Calculus) referenced by title only — no citation key added.
- Frontmatter license aligned QNFO-ULA -> cc-by-4.0 (record metadata authoritative).
- Zenodo metadata: EuroSciVoc subjects (philosophy, mathematics) restored on the v1.2 record.
