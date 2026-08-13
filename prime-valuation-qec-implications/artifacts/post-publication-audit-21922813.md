# Post-Publication Adversarial Analysis — Zenodo 10.5281/zenodo.21922813

**Project:** QNFO.RES.006 | **Slug:** prime-valuation-qec-implications
**Published record:** DOI 10.5281/zenodo.21922813 (v0.1, 2026-08-13)
**Audit date:** 2026-08-13 (publish-then-audit loop, POST-PUBLICATION ADVERSARIAL ANALYSIS GATE)
**Auditor:** direct parent-agent analysis with live verification (Zenodo API, GitHub API) + the
RQ3 reproduction executed in the same session (`artifacts/rq3-reproduction-report.md`).

## 0. Record verification (live, this session — Zenodo API)

| Field | Value |
|:------|:------|
| Title | Implications for Computing and Quantum Error Correction |
| Version | v0.1 |
| Publication date | 2026-08-13 |
| DOI | 10.5281/zenodo.21922813 |
| License | cc-by-4.0 |
| Resource type | Preprint |
| Creators | Quni-Gudzinas, Rowan Brad (QNFO Research Collective) |
| Files | **14** (full provenance set: README, manuscript.md v0.1 16,289 B, PDF, HTML, references.bib, PROJECT-PLAN, core-claim, consilience-gate, due-diligence, due-diligence-phase1, red-team-phase1, phase2-literature-review, external-search-README + literature-review) |
| Related | isSupplementTo = GitHub branch URL (verified); isDerivedFrom = 10.5281/zenodo.21918838 (anchor) |

## 1. Findings

### HARD: 3

**H1 — C7.3' (Mahler v_p-spectral separation) NOT reproduced at n <= 18.**
The published paper's §6/C8 cites NTOF's claim that a Mahler v_p-spectral profile separates code
families with v_p^max = 28 for optimal vs 4 for random. This session's independent reproduction
(55/55 verified codes; weight-enumerator Mahler v_2-spectrum; CSS [[7,1,3]], [[15,7,3]], toric
L=2,3, [[5,1,3]], 50 random [[10,4]]) observed: optimal 4, random median 3 (max 6), gap 1.
Magnitude incompatibility: v_p^max = 28 requires |c_j| >= 2^28, i.e., n-k >= 28, impossible at the
record's reported code sizes (n <= 18) under the weight-enumerator normalization. Either the
source's Mahler target/normalization differs (undefined in the record) or the claim is
inconsistent as stated. C8 must remain [UNVERIFIED-INTERNAL].

**H2 — Algorithm 4.4 (Kodaira-Néron classifier, the "83%") is not reproducible from the shipped
specification.** Step 2 ("Construct the Cox ring R_C = C[x_1,...,x_n]/I_C") never defines the
ideal I_C; the record ships no dataset, no implementation, no baseline, no generation protocol.
The 83% aggregate (166/200; Surface 92%, CSS 78%, Optimal 90%, Random 72%) also conceals the
source's own documented surface-code I_n* boundary FAIL. The 83% claim is unreproducible from
spec alone.

**H3 — The published record contains manuscript v0.1, which lacks the P4 v0.2 corrections.**
The deposited manuscript.md (16,289 B) is the pre-P4-patch version: its §6 still says "83%
classification accuracy" without the precise per-family breakdown, and its References #7 still
carries the Gubser-Knaute venue error (Commun. Math. Phys. vs verified ATMP 21:1655,
DOI 10.4310/atmp.2017.v21.n7.a3). Both were fixed on the branch at 3866daf (v0.2) — those fixes
are NOT in the published record. (Also H1's reproduction finding is branch-only.)

### SOFT: 2

**S1 — Post-publication artifacts are branch-only.** The RQ3 reproduction (bf5152e) and this
audit land after publication; the record does not contain them. Expected in the publish-then-audit
loop; reconciled in the next newversion. (NOTE: this audit draft initially claimed the deposit was
2-file and that it violated PUBLICATION-SOURCE-COMPLETENESS-1 — both were WRONG. The live record
check shows the full 14-file provenance set is present. The audit methodology error is recorded
here so the record of the correction is explicit.)

**S2 — Record version label (v0.1) vs branch manuscript (v0.2).** Divergence between the
published file and the branch tip must be flagged in any citation of the record; a newversion is
needed to align them.

### DESIGN: 1

**D1 — Reproduction protocol value.** The pre-registered acceptance criteria in
artifacts/rq3-reproduction-protocol.md worked as intended: the negative result was reported
honestly rather than fitted. This is the model for C7.3'/C8 going forward.

## 2. Remediation plan (next cycle)

1. Clarify with the source: (a) the exact Mahler target function + normalization; (b) the I_C
   construction; (c) the 50-code-per-family generation protocol.
2. Extend the Mahler run to n <= 30 (where v_2 >= 28 becomes attainable) once the target is defined.
3. Publish a Zenodo **newversion** carrying: manuscript **v0.2** (with §6 precision + reference
   corrections) + the RQ3 reproduction report + results + this audit (S1/S2/H3). C8 stays
   [UNVERIFIED-INTERNAL] until then.

## 3. Verdict

The published record's scientific spine (self-corrected C2/C3; C4 open question) survives and its
provenance set is complete. The C7.3'/C8 empirical leg does not yet meet the standard the paper
itself demands (H1/H2), and the record lags the branch corrections (H3/S2). Publication stands
(read-only); findings feed the next cycle per the publish-then-audit loop.
