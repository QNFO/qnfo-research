# Calibration Register — QNFO.RES.006

**Project:** Implications for Computing and Quantum Error Correction
**Date:** 2026-08-13 | **Phase:** P4

Records predictions/assessments made during the pipeline and their outcomes, with confidence
levels. Purpose: detect systematic overconfidence or confirmation bias (per research skill P4
and KIF-60 calibration requirements).

| # | Date | Assessment (pre-outcome) | Confidence | Outcome | Calibration |
|:--|:-----|:------------------------|:----------:|:--------|:------------|
| 1 | 2026-08-13 (P1) | "The [[n,k,d]] ↔ branch-depth mapping is at risk of being PURE RELABELING; must yield new invariant/taxonomy/bound or fail its own falsifiability condition" | 0.75 | CONFIRMED — manuscript v0.1 §3 self-corrects: n,k definitional, d has no valuation reading | accurate (risk flagged before manuscript) |
| 2 | 2026-08-13 (P1) | "Novelty is in the vocabulary (valuation-as-depth), not the substrate (qudit stabilizer theory is external and mature)" | 0.8 | CONFIRMED — P2 external search (0 external hits for valuation-based QEC taxonomy) + manuscript repositioning vs Abramsky/Coecke/Heydeman | accurate |
| 3 | 2026-08-13 (P1/P3) | "RQ3 83% source is DOI 10.5281/zenodo.21193487 (not 21046993)" | 0.85 | CONFIRMED — NTOF publication.md contains the 83%/166-of-200 numbers; 21046993 is a different paper | accurate |
| 4 | 2026-08-13 (P4) | "The 83% figure is a rule-based classifier rate (Algorithm 4.4), not a learned-ML accuracy; NTOF ships no dataset/code/baseline" | 0.9 | CONFIRMED — direct NTOF inspection (M0 of reproduction protocol) | accurate |
| 5 | 2026-08-13 (P2) | "Zenodo OR-tokenization makes record-count totals unreliable as relevance signal" | 0.9 | CONFIRMED — qudit/p-adic Zenodo totals 4,144/4,938 were dominated by irrelevant records | accurate |
| 6 | 2026-08-13 (P3) | "Dragovich 2003 CrossRef top-hit is the cosmology paper, not the QM review" | 0.8 | CONFIRMED — 10.1063/1.2193108 = p-Adic and Adelic Cosmology; QM review = hep-th/0312046 | accurate |
| 7 | 2026-08-13 (P4) | "Manuscript Ref #7 venue is wrong; Ref #6 arXiv ID likely correct" | 0.7 | CONFIRMED — #7 Commun.Math.Phys.→ATMP; #6 1703.05445 verified live | accurate |

**Calibration summary:** 7/7 accurate at stated confidence. No overconfidence error yet
recorded. Watch item: the pipeline has repeatedly confirmed QNFO-internal claims (83%,
v_p^max 28 vs 4); the single external check (Ref #6/#7) did surface real errors — external
verification of every number remains mandatory (P3.AUTHOR-GATE), especially for the P5
publication build.
