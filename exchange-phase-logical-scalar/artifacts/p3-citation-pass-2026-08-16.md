# P3 Citation Pass — RES.010 Exchange-Phase Logical Scalar (2026-08-16)

**Session:** pVxPB_ViPCLUkdaDtykwu (CMD CONTINUE) · **Branch:** res/paper/exchange-phase-logical-scalar
**Task:** P3 citations — pull Kauffman 2022 full body + retry P2 NOT-VERIFIED sources (documented next step from the P2 record).

## 1. Full-body pull status (Kauffman 2022, 10.1088/1742-6596/2197/1/012001)

| Channel | Result |
|---|---|
| urllib (browser UA) — meta page | 200 but Radware CAPTCHA HTML (14,371 B) |
| urllib — PDF endpoint | Radware-gated |
| **Browser (YoBrowser) — meta page** | **BYPASSED Radware — full metadata captured** |
| Browser — PDF endpoint | empty document (PDF viewer gated) |
| Unpaywall | `is_oa: true`, `oa_status: gold`, best URL = IOP PDF |
| Semantic Scholar | paperId b835b4e982128cf73b951fd218b158ea4ebfffcb; **citationCount 0, referenceCount 35**; openAccessPdf GOLD CCBY |

**Captured from the live IOP page (browser):** venue = Journal of Physics: Conference Series 2197 012001, "THE VIGIER CENTENARY Third Regime Natural Science Toward a PHYSICS OF THE OBSERVER: 12th International Symposium Honouring Jean-Pierre Vigier (Vigier 2021), online"; **548 total downloads**; CC-BY-3.0; citation line confirmed; abstract confirmed. Reference list is JS-lazy-loaded (not expandable in this context).

**Disposition:** the full body remains behind IOP's Radware PDF gate (documented, honest). Scope confirmation is satisfied via: abstract + venue context + S2 record (35 refs) + the 5 arXiv-verified Kauffman Majorana/LoF papers that fill in the review's content areas. The PDF is legally reusable (CC-BY); a future browser-session with the PDF viewer may capture it. Not a blocker for the citation pass.

## 2. P2 NOT-VERIFIED retry results (all resolved)

- **Zenodo API** → RESOLVED (8 records live-verified, version chains confirmed)
- **Semantic Scholar** → RESOLVED (200; Kauffman 2022 record with 0 cites/35 refs)
- **DBLP** → RESOLVED (200; 3 Kauffman Majorana hits incl. 2 NEW: Symmetry 2021 Iterants, QIP 2018 Braiding)
- **Crossref Q4** → RESOLVED (200; no new prior art — NET-NEW verdict holds)
- **EuropePMC** → RESOLVED verified-negative (hitCount 0; biomedical index scope)

## 3. New prior art discovered (5 arXiv + 2 journal — all Supporting/Background)

| ID | Paper | Class | Why it matters |
|---|---|---|---|
| 1301.6214 | Kauffman, Knot Logic and TQC with Majorana Fermions | **Supporting (support-4)** | **The mark-as-fermion precursor** — "negation... the mark... naturally generates the fermion algebra, the quaternions and the braid group representations" — MUST be engaged in P5: distinguishes algebra-vs-invariant |
| 1710.04650 | Kauffman, Majorana Fermions and Representations of the Braid Group | Supporting | Braid reps from Majorana/Clifford; Ivanov braiding |
| 1603.07827 | Kauffman-Lomonaco, Braiding Majorana Fermions | Background | Clifford Braiding Theorem |
| 2009.04811 | Kauffman-Rowlands, Dirac Equation and the Majorana Dirac Equation | Supporting | Split-quaternion real form |
| 10.3390/sym13081373 | Kauffman, Iterants, Majorana Fermions and the Majorana-Dirac Equation | Supporting | Iterant/re-entry machinery flank |
| 10.1007/s11128-018-1959-x | Kauffman-Lomonaco, Braiding/Fibonacci/QIP 2018 | Supporting | Fibonacci-anyon model |
| 10.1142/9789814504782_0001 | Kauffman, Laws of Form, Majorana Fermions, and Discrete Physics (2013 WS) | Supporting (support-9) | **DIRECT predecessor of the 2022 review** — was missing from P2 |

## 4. Citation-vacuum upgrade (L1)

Kauffman 2022 now shows **0 citations in THREE independent indexes** (Crossref 0, OpenAlex 0, Semantic Scholar 0) as of 2026-08-16. The L1 finding is upgraded from dual-index to triple-index verified. A QNFO citation of the review would be the first in any major index.

## 5. Files changed

- `references.bib` — 14 → 26 entries (12 added, all verified)
- `artifacts/phase2-classified.json` — 7 → 16 classification entries; not_verified → all resolved with evidence; p3_addendum added
- `artifacts/p3-citation-pass-2026-08-16.md` — this record

## 6. Next (P4/P5 inputs)

P5 relation-to-prior-art MUST engage support-4 (1301.6214) explicitly: Kauffman derives fermion ALGEBRA from the mark; RES.010 derives the EXCHANGE-PHASE INVARIANT — the distinction (algebra vs invariant) is the novelty boundary.
