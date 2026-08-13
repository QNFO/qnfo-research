# Red-Team Review — Phase 4 (QNFO.RES.006)

**Project:** Implications for Computing and Quantum Error Correction
**Slug:** prime-valuation-qec-implications
**Date:** 2026-08-13
**Gate:** P4 red-team (adversarial review of manuscript v0.1, pre-v0.2 patch)

## Method

Adversarial review of `prime-valuation-qec-implications.md` v0.1 against (a) its own
falsifiability register (§7 C1–C8), (b) the live primary source for the 83% claim
(Zenodo 21193487 `publication.md`, downloaded this session), and (c) the P3-verified
`references.bib`. Claims were checked against the actual source text; no claim was taken
on trust.

## Findings

### HARD: 2 (both FIXED in v0.2 patch)

**H1 — §6 83% claim characterization imprecise vs primary source.**
The manuscript said "a Kodaira–Néron-fiber classifier achieves **83% classification
accuracy**". The primary source (NTOF `publication.md` §13.2) reports:
- 166/200 test codes = 83% aggregate across 4 families, 50 each;
- per-family: Surface 46/50 (92%), CSS 39/50 (78%), Optimal 45/50 (90%), Random 36/50 (72%);
- the classifier is **rule-based Algorithm 4.4** (binary symplectic form H → Cox ring R_C →
  Weierstrass coefficients → degenerate loci → Kodaira–Néron fiber type), not a learned ML
  classifier;
- NTOF ships **no dataset, no implementation, no baseline, no leakage-control protocol**;
- §13.2 also records a documented partial failure: "FAIL for surface codes (systematic
  mismatch in the $I_n^*$ classification boundaries)" — the aggregate 83% conceals a known
  per-family defect.

Fix: §6 now quotes the precise breakdown, labels the classifier rule-based, cites the
documented surface-code boundary failure, and reframes the reproduction requirement.

**H2 — References #7 venue error.**
Manuscript Ref #7 said Gubser & Knaute (2017) in *Commun. Math. Phys.* P3 CrossRef
verification and this review confirm: "A $p$-adic version of AdS/CFT", *Adv. Theor. Math.
Phys.* 21(7):1655–1683, DOI 10.4310/atmp.2017.v21.n7.a3. Fix applied. (Ref #6 arXiv
1703.05445 verified correct live: Bhattacharyya, Hung, Yang Lei, Li, "Tensor network and
(p-adic) AdS/CFT"; DOI 10.1007/jhep01(2018)139 added.)

### SOFT: 3

**S1 — Reproduction language misframes a rule-based classifier.**
"Fresh train/test split with leakage control" presupposes learned parameters. Algorithm 4.4
is deterministic rule-based; the correct protocol is re-implementation from spec + fresh
code-family generation + baseline comparison. Now pointed to
`artifacts/rq3-reproduction-protocol.md`.

**S2 — references.bib author error (Lei, P. → Lei, Y.).**
Fixed in the bib (verified author is Yang Lei).

**S3 — §5.2 overhead hypothesis has no concrete first step.**
"[UNTESTED] no bound has been derived" is honest but stalls. Suggest concrete milestone:
compute the valuation-spectrum quantity (Mahler v_p^max) for a fixed code family and test
whether it separates families at all before attempting a Singleton comparison.

### DESIGN: 2

**D1 — The self-correction structure is the paper's value.**
C2 (n,k definitional → pure relabeling) and C3 (d is a weight, not a depth) are correctly
self-corrected and MUST be preserved; the paper would be dishonest without them.

**D2 — §4 computing leg is promissory.**
Correctly labeled [CONTESTED]/promissory; suggest trimming to a research-program note so it
does not dilute the sharp C4/C7 questions.

## Verdict

**PASS with mandatory fixes.** The paper's scientific spine (self-corrected C2/C3, sharpened
C4 open question, C8 reproduction requirement) is sound and epistemically honest. H1/H2
fixed in v0.2; S1–S3 addressed; D1/D2 documented for the author's P4.2/P5 work.
