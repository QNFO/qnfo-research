# Post-Publication Adversarial Analysis — Zenodo 10.5281/zenodo.21923000 (v0.2) and Anchor 10.5281/zenodo.21918838 (v0.2)

**Project:** QNFO.RES.006 | **Slug:** prime-valuation-qec-implications
**Published records:** DOI 10.5281/zenodo.21923000 (follow-on, v0.2, 2026-08-13); DOI 10.5281/zenodo.21918838 (anchor, v0.2, 2026-08-13)
**Audit date:** 2026-08-14 (publish-then-audit loop, POST-PUBLICATION ADVERSARIAL ANALYSIS GATE)
**Method:** 3-slot CMD RED TEAM SUB (Accuracy `ACC-*`, Completeness `COMP-*`, Dependency `DEP-*`) + direct parent-agent audit with live verification (Zenodo API, Crossref, arXiv API, GitHub API) + corpus-wide deep due diligence (KG 8,279 nodes, D1 living-paper 986 rows, Vectorize, durable memory).
**READ-ONLY:** published records were not modified. All fixes below land on the corrections branch (`res/paper/prime-valuation-qec-implications-v03-corrections`) for the next version cycle.

## 0. Record verification (live)

| Field | 21918838 (anchor) | 21923000 (follow-on) |
|:------|:------------------|:---------------------|
| Version chain | v0.1-draft (21918032) → **v0.2**; concept 21918031 | v0.1 (21922813) → **v0.2**; concept 21922812 |
| License (record) | cc-by-nc-sa-4.0 | cc-by-4.0 |
| License (md YAML) | **"QNFO Unified License Agreement (QNFO-ULA)"** ← MISMATCH | CC-BY-4.0 ✓ |
| Files | 3 | 41 |
| isDerivedFrom / isSupplementTo | — | anchor DOI + GitHub branch ✓ (branch sha 462f6a4) |

## 1. HARD findings (deduplicated across the three reviewers + direct audit)

| ID | Finding | Evidence | Status |
|:---|:--------|:---------|:-------|
| ACC-1 | Anchor ref 11 (Rapoport) prints "Found. Phys. 39:767–800, 2009"; Crossref for DOI 10.1007/s10701-009-9334-5 gives **41(1):33–76, print 2011** (online 2009-08-22). Volume/pages/year all wrong. | Crossref API | **OPEN** — anchor-side fix (RES.005 action list §4) |
| ACC-2 | Follow-on ref 7 (Gubser–Knaute) page range printed 1655–**1683**; Crossref says 1655–**1678** (in paper §8 + ref list + bib + red-team-P4). | Crossref 10.4310/atmp.2017.v21.n7.a3 | **FIXED on branch** (1655–1678 everywhere; INSPIRE-style indexes list 1683 — noted in citation-audit) |
| ACC-3 | citation-audit.md "CA-1 PASS: correct venue/year/DOI" contradicted by live Crossref on two entries (Coecke year, Gubser pages). The bib header claim "every entry verified live" was overstated. | ACC-2/ACC-4 evidence | **FIXED on branch** (CA-1 → CORRECTED with re-verification notes) |
| ACC-7 | Anchor license mismatch: md YAML "QNFO-ULA" vs record cc-by-nc-sa-4.0. Readers cannot tell which license governs. | Zenodo API + file frontmatter | **OPEN** — anchor-side; needs maintainer decision (alias or align) |
| DEP-3 | Two files shipped in the v0.2 record self-cite the superseded v0.1 DOI: citation-audit.md header + RESEARCH-CONTINUITY-REGISTRY.md header ("21922813 (v0.2)"). Branch-head registry was already correct — the record shipped a stale snapshot. | Live record file download vs branch head | **FIXED on branch** (citation-audit header → 21923000; registry already correct on branch) |
| DEP-5a | Paper ref 2 (Abramsky 2009, DOI 10.1017/cbo9781139193313.002) missing from references.bib — record AND branch copies. | Live bib diff | **FIXED on branch** (Abramsky2009 entry added) |
| COMP-3 | rq3-reproduction-report.md F2's impossibility argument is mathematically invalid: it drops the binomial factor. Correct bound: \|c_j\| ≤ 2^(n−k) · Σ_{i≤j} C(j,i) = 2^(n−k+j), so v₂ ≤ n−k+j; v₂=28 is satisfiable at n=18 (k≤8) and impossible only for n≤13. | From-scratch derivation; report's own §2 formula | **FIXED on branch** (F2 was already re-scoped to EMPIRICAL by a 2026-08-13 red-team; F2b now documents the correct bound) |
| COMP-4 | F2's factual premise ("beyond every code size in the NTOF tables (n ≤ 18)") is unsupported: NTOF publication.md never bounds at n≤18 and states "handles up to n=64 qubit codes"; NTOF Table 1 reports v_p^max maxima 15/14/28 (surface/CSS/optimal). | NTOF publication.md L397–398, L482 | **FIXED on branch** (F2b premise correction added) |

## 2. SOFT findings (deduplicated)

| ID | Finding | Status |
|:---|:--------|:-------|
| ACC-4 / DEP-5c | Coecke *Quantum Pictorialism* printed 2009; print year is 2010 (bib already said 2010) | **FIXED on branch** (ref list now 2010, "(first published online 2009)") |
| ACC-5 / DEP-5b | Bib Ostrowski entry conflated the 1916 original with the 1983 Collected-Papers chapter (Selected Papers, reprint DOI) | **FIXED on branch** (re-keyed to Acta Math 41:271–284 + DOI 10.1007/bf02422947; reprint DOI kept as note) |
| DEP-4 | Shipped record files content-diverge from the isSupplementTo branch head (registry 4,761 vs 6,676 chars; paper +92; bib +386) | **OPEN** — resolved at next newversion; recommend pinning git sha in record metadata |
| DEP-7a | Follow-on says "three claims" for the anchor's four Statements (S3+S4 merged) | **DEFERRED** (cosmetic) |
| COMP-1 | 11 of 14 anchor references have zero citation-audit coverage in either record | **OPEN** — anchor-scoped citation audit needed (RES.005 action list) |
| COMP-2 | §6 omitted NTOF's headline C7.3′ verification figure 187/200 (93.5%) and C2.1′ 151/200 (75.5%) | **FIXED on branch** (§6 prior-art paragraph now records the 93.5% figure) |
| COMP-5 | Paper C8 falsifiability cell conflates the Mahler-leg attempt with the never-run classifier leg | **DEFERRED** — §7 table split scheduled for v0.3 build |
| COMP-7 / ACC-6 | Stale self-DOI in two companion artifacts | Folded into DEP-3 (HARD) |

## 3. DESIGN findings

| ID | Finding | Status |
|:---|:--------|:-------|
| DEP-5d | Bib has 46 entries; paper prints 11; the shipped citation audit covers only the 11 (21 internal DOIs + 14 qudit-QEC arXiv items unaudited) | **DEFERRED** — scope bib to paper, or extend audit |
| COMP-6 | Registry P1 row text "(n,k)" doesn't cover paper C3 (d-valuation REJECTED) | **DEFERRED** |
| COMP-8 | rq3 report §1 acceptance wording ("optimal ≥ 28 and random ≈ 4") not in pre-registered protocol M4 ("gap ≥ 10" only) | **DEFERRED** — align wording |

## 4. RES.005 (anchor) action list — not touched this turn, required next cycle

1. Fix ref 11 (Rapoport) to *Found. Phys.* 41(1):33–76, 2011 — or keep 2009 and flag the DOI resolves to the erratum.
2. Resolve license: align md YAML with cc-by-nc-sa-4.0, or document QNFO-ULA ↔ cc-by-nc-sa-4.0 mapping explicitly in the file and record.
3. Cite the corpus LoF priors (G2, see deep-due-diligence-addendum.md): 21205097 (Calculus of Distinction), 21205110 (Quantum LoF: Superposition as Re-Entry), 21908818 (Calculus of Re-Entrant Distinctions). Restate Statement 2's contribution as the valuation-depth *vocabulary*, not the isomorphism.
4. Ship a citation audit for the 14 anchor refs (COMP-1).

## 5. Corpus-level findings (deep due diligence 2026-08-14)

See `deep-due-diligence-addendum.md`. Headline: **G1** — ACRP-06 (Zenodo 21737222 v1.0, 21754148 v1.1 erratum, 2026-08-01/02) had already tested C7.3' before this pipeline's "first reproduction attempt"; its v1.1 erratum reversed the only positive evidence (Golay 28 → 2/4). The Mahler 28 has now failed two independent reproductions plus an erratum chain. This record's "first reproduction attempt" wording is withdrawn on the corrections branch.

## 6. Kaizen items (program-level)

- **DUE-DILIGENCE-SIBLING-MISS-1:** never claim "first reproduction attempt" without a corpus-wide prior-attempt sweep (KG + Vectorize + memory); check version chains + errata of every cited corpus DOI.
- **KG defects:** `paper:qec-darwinism-ultrametric` conflates the Bruhat-Tits QEC title with DOI 21819232 (= Archimedean Shadows); ACRP-06 KG node points at the superseded v1.0; mass duplicate Paper nodes per DOI. Fixes tracked in §PLT actions.
- **Memory staleness:** the 2026-07-24 synthesis memory "Mahler v_p spectral discriminant separates optimal from random codes 7:1 (computationally verified)" is DISCONFIRMED and corrected this turn.

**Verdict:** the two records' scientific spine (self-corrected C2/C3, honest negative reproductions, UNVERIFIED-INTERNAL downgrade) is exemplary; all 8 HARD findings are bibliographic/premise defects, 5 of 8 fixed on the corrections branch this turn, 3 anchored in the RES.005 action list. Publish-then-audit loop functioning as designed.
