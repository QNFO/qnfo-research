# Majorana fermions × Laws of Form — Source Verification & Due-Diligence Record

**Cycle:** 2026-08-16 · **Protocol:** CMD RESEARCH → Phase 1 Due Diligence (DUE-DILIGENCE-DEPTH-1 HARD GATE)
**Target projects (existing — Phase 0 skipped):** QNFO.RES.010 `exchange-phase-logical-scalar`, QNFO.RES.011 `configuration-space-topology`
**Corpus baseline (live):** KG 8,290 nodes / 8,432 edges / 1,630 Paper nodes; D1 living-paper 994 papers.

## 1. Source verification (all 8 URLs)

| # | URL | Verified identity | Status |
|---|---|---|---|
| 1 | Google search `review of majorana fermions and laws of form` | context probe (not a source) | n/a |
| 2 | RG 240194298 | Kauffman, "Form dynamics", *J. Social Biol. Syst.* 3(2):171–206 (1980), DOI 10.1016/0140-1750(80)90008-1 | ✓ |
| 3 | RG 376259552 | Kauffman, "Autopoiesis and Eigenform", *Computation* (MDPI) 11(12):247 (2023), DOI 10.3390/computation11120247, OA | ✓ |
| 4 | RG 233017186 | Kauffman, "Arithmetic in the Form", *Cybernetics and Systems* 26(1):1–57 (1995), DOI 10.1080/01969729508927486 | ✓ |
| 5 | JPSJ 10.7566/JPSJ.85.072001 | Sato & Fujimoto, "Majorana Fermions and Topology in Superconductors", *J. Phys. Soc. Jpn.* 85 072001 (2016); 364 citations, 256 refs | ✓ |
| 6–7 | IOP 10.1088/1742-6596/2197/1/012001 | **Louis H. Kauffman, "A Review of Majorana fermions and the laws of form"**, *J. Phys.: Conf. Ser.* 2197 012001 (2022), CC-BY, 33 refs, **0 Crossref citations** | ✓ |
| 8 | arXiv 2603.28538v1 | **Francesco Vissani**, "From Hole Theory to Quantum Field Theory: Relativistic Fermions and the Role of Ettore Majorana (1933–1937)", 2026-03-30, physics.hist-ph/hep-th/quant-ph, 34 pp | ✓ |

**Bonus discoveries (not in the URL list — MUST enter the reference corpus):**
- Kauffman, "Laws of Form, Majorana Fermions, and Discrete Physics", *The Physics of Reality* (World Scientific), 1–18 (2013), DOI 10.1142/9789814504782_0001 — **direct predecessor of the 2022 IOP review**.
- Kauffman, "The Semiotics of Laws of Form", *When Form Becomes Substance* (Springer), 3–26 (2022), DOI 10.1007/978-3-030-83125-7_1.

**Evidence discipline:** all identities confirmed against Crossref works/bibliographic + arXiv export API + OpenAlex (HTTP 200s); IOP meta page is Radware-CAPTCHA-walled and JPSJ 403s bots — Crossref is the authoritative verifier (DOI-WAF-403-1 fallback). Machine-readable record: `majorana-lof-source-verification-2026-08-16.json`.

## 2. Corpus cross-reference (internal)

- **F1 Majorana titles (6):** ZBW-Majorana-TQC series (P2 correlator 21336045, P3 readout 21336081, capstone 21574555/21609223, p-adic observable 21736327) — **UMP domain**.
- **F2 LoF/Spencer-Brown titles (9):** Silent Radix (21148596/21090347), Quantum Laws of Form (21206074/21205110/21205097/19598745), cancellation-rule (21470438), void-is-not-false (21916970), prime-valuation-depth (21918838) — **SLB domain**.
- **F4 exchange-phase/spin-statistics (3):** spin-statistics-distinction RES.009 (21944401 v1.4), from-distinction-to-dissipation (21940822), exchange-phase-logical-scalar RES.010 (21941238) — **RES domain**.
- **Kauffman cited in 16 corpus bodies** (incl. reentrant-distinctions 21908818, p-adic-anyon-fusion-braiding 21208491, adelic-synthesis-pattern-particle 21208568, syntactic-token-calculus-research-plan 21206272, + 8 draft bodies with null DOIs). Zero QNFO titles mention Kauffman — engagement is via citation, never co-authorship. ✓

## 3. Gap analysis

**HARD**
- **G1 — R2 mirror path corruption (WRONG-BUCKET-SELECTION-1 class):** `exchange-phase-logical-scalar` and `from-distinction-to-dissipation` carry `r2_path: qnfo-releases/releases/2026/08/…` (double `releases/` prefix; resolve_paper_id reports the bare `releases` bucket). Canonical: `qnfo-releases/2026/08/<slug>/`. Remediate: re-mirror both to `qnfo-releases`, fix KG + D1 `r2_path`, verify bucket listing.

**SOFT**
- **G2 — doi vs zenodo_doi mismatch:** quantum-laws-of-form (21206074 vs 21206166); from-distinction-to-dissipation (21940822 vs 21943007). Likely record-vs-concept DOI stored inconsistently — document, do not rewrite without ownership verification (ZENODO-KG-OWNERSHIP-1).
- **G3 — KG registry drift:** RES.011 Project node says `phase: P0, created 2026-08-15` while the git branch head is P8 distribution-complete (fcd24c1) and the record is published (10.5281/zenodo.21957291). Sync KG Project node to P8.
- **G4 — historical:** `zbw-majorana-tqc` has `r2_key: null` (pre-mirror-mandate record) — no action.

**LITERATURE**
- **L1 — citation vacuum:** Kauffman's 2022 IOP review has **zero Crossref citations** (2026-08-16). A QNFO engagement would be the first — relation-to-prior-art must say "uncited external line", and QNFO's citation would make QNFO the reference for it.
- **L2 — missing predecessor:** the 2013 World Scientific chapter (Laws of Form, Majorana Fermions, and Discrete Physics) is absent from the URL list and from the earlier RES.010 P2 record — add to references.bib for both RES.010 (P3) and RES.011.
- **L3 — classification of arXiv 2603.28538:** history-of-physics (Vissani), NOT a LoF competitor; Background for Majorana's 1937 anti-commutation lineage. Do not classify as Supporting for the LoF claim.

## 4. Next-step plan (WBS-coded)

1. `[QNFO.RES.010.P3]` Pull Kauffman 2022 full text (arXiv/Chicago repository copies) + add 2013 chapter + Vissani 2026 to references.bib; update P2 classification with L1/L2/L3.
2. `[QNFO.RES.011.P1R]` Absorb this verification record into the derivation program's literature base (this file is the evidence).
3. `[QNFO.GOV/CF]` Remediate G1 (re-mirror two records to `qnfo-releases`, fix r2_path in KG+D1); sync RES.011 KG Project node (G3).
4. `[QNFO.SLB]` Optional cross-check: does the Kauffman eigenform/re-entry corpus (Computation 2023, Kybernetes 2005) shift the re-entry reading in `quantum-laws-of-form-superposition-as-re-entry`? Deferred — no evidence of conflict.
