---
title: "The Consilience of the QNFO Keyword Taxonomy: Ultrametric Structure as a Testable Compression Prior"
author: Rowan Brad Quni-Gudzinas
date: 2026-08-23
version: v0.1-draft
license: CC BY 4.0
---

## Abstract

The QNFO research program spans seven domains — ultrametric physics, the laws of form, infomatics, paradigm engineering, consilience research, the QWAV platform, and interactive demos — and maintains a canonical keyword taxonomy of 335 terms used to scope external discovery. A recurring claim in the program is that these domains share one structural object: a nested, hierarchical (ultrametric) partition logic whose local geometry is p-adic, whose global synthesis is adelic, and whose minimal act is a distinction. This paper subjects that claim to a computational audit at the level of the program's own vocabulary. The taxonomy is strictly partitional: 334 of 335 keywords occur in exactly one program, one keyword occurs in two, and none occurs in three or more. Bridge vocabulary is likewise concentrated: valuation terms in ultrametric physics, distinction terms in the laws of form, thermodynamic bounds in infomatics; only the hierarchy family (tree, re-entry, stratification) spans three programs. The consilience claim is therefore not a lexical fact about the taxonomy; it is a semantic claim carried by bridge families, by the taxonomy's explicit cross-cutting themes, and by corpus-level links between published records. The paper states the revised claim, three falsifiable hypotheses with disconfirmation criteria, and three practitioner-facing deliverables, and it binds the strong form of the program to a 2028 decision point.

## 1. Introduction

A research program that spans number-theoretic physics, a calculus of logical form, the thermodynamics of computation, technology forecasting, measurement epistemology, a cloud-native software platform, and interactive visualization invites two questions. The first is external: are these seven activities one program or seven programs that share an organization? The second is internal: does the program's own public vocabulary — the keywords it uses to discover, index, and classify work — exhibit the unity that the program claims?

This paper addresses both questions with a computational audit of the QNFO keyword taxonomy: 335 keywords organized into seven program sections plus three cross-cutting themes. The audit is deliberately narrow. It does not adjudicate the physics. It measures one thing: how much of the claimed consilience is visible in the program's own vocabulary, at the level of the keyword strings themselves, at the level of semantic keyword families, and at the level of the taxonomy's internal bridge structures.

The answer is informative precisely because it is negative at the first level. The taxonomy contains no keyword shared by three or more programs; 99.7 percent of its keywords are program-local. A reader who tries to verify the program's unity by its vocabulary will find none at the string level. The consilience, if it exists, lives elsewhere: in semantic families, in the taxonomy's own cross-cutting sections, and in the published corpus. That is the finding this paper reports, and it is the load-bearing fact for everything the program claims next.

Why should a reader care? Three reasons. First, the method is transferable: any multi-domain research organization that claims unity of structure can audit its own vocabulary the same way, with the same script, and the result is a number, not a narrative. Second, the negative result has a positive consequence: it forces the program's scientific claims to be stated as testable hypotheses with observables, which is what Section 5 provides. Third, the paper's deliverable — a p-adic fingerprint index benchmarked against cosine and HNSW retrieval — is usable engineering independent of any commitment to the underlying physics.

The paper is organized as follows. Section 2 describes the taxonomy as data. Section 3 states the audit method. Section 4 reports results at four levels. Section 5 restates the research questions and disconfirmation criteria. Section 6 gives practitioner deliverables. Section 7 discloses where the premises end. Section 8 positions the result against the relevant external literature, and Section 9 states limitations.

## 2. The keyword taxonomy as data

The QNFO keyword taxonomy (v1.0, 2026-08-05) was built as a GitHub-search scoping instrument: a curated map of keywords used to discover repositories aligned with each program, maintained by the organization's research staff. It is organized into seven program sections — UMP (ultrametric physics), SLB (laws of form), INM (infomatics), CFE (paradigm engineering), RES (consilience research), PLT (QWAV platform), DEM (interactive demos) — each with thematic subsections (core, geometry, methods, applications), followed by three cross-cutting themes (agentic AI, the 4-D distribution protocol, and measurement stratigraphy) and a set of search-query templates.

As data, the taxonomy has three properties worth noting. First, it is a public, versioned artifact with a canonical location, so the audit is reproducible against a fixed snapshot (the source text is archived with this paper's verification artifacts). Second, its purpose is discovery scoping, not ontology: keywords were chosen to be searchable, which means the taxonomy over-weights tool-adjacent vocabulary. Third, it contains its own internal bridge structures — a "Bridge Concepts" subsection in UMP and "Cross-Domain Methodology", "Cross-Domain Bridges", and "Measurement Stratigraphy" subsections in RES — which the audit treats as the taxonomy's own declaration of where the programs connect.

The published corpus provides the second data source. The QNFO archive holds 1,660 papers and 8,324 knowledge-graph nodes, including prior synthesis records that make claims overlapping this paper's: a consilience framework spanning valuation theory to the void (10.5281/zenodo.21804073), an ultrametric consilience atlas of cross-domain p-adic applications (10.5281/zenodo.21722395), a convergent-theses study from Ostrowski's theorem to adelic quantum mechanics (10.5281/zenodo.21590155), a measurement-stratigraphy history (10.5281/zenodo.21705220), a category-theoretic foundation for finite measurement without the reals (10.5281/zenodo.21803677), and a consolidated synthesis showing that positional notation is natively an ultrametric tree (10.5281/zenodo.21046213). These records are the corpus-level evidence against which the vocabulary-level audit is compared.

## 3. Methods

The audit has four layers, all deterministic and all executed by a single script (`artifacts/verification/rq5_keyword_load.py`, pure Python standard library, no randomness, no external dependencies).

**Layer 1 — string level.** The taxonomy text is split on top-level section headers; the seven program sections are parsed for backtick-delimited keywords (335 distinct after normalization, where normalization lowercases and strips punctuation so that "p-adic" and "padic" collapse to one key). For each normalized keyword, the set of programs containing it is recorded. A keyword is *load-bearing* if it occurs in three or more programs and *program-local* if it occurs in exactly one. The coincidence of the load-bearing core with a bridge vocabulary is tested with a one-sided Fisher exact test on the 2 x 2 contingency table (bridge vs non-bridge by load-bearing vs local).

**Layer 2 — family level.** A bridge vocabulary is defined a priori from the taxonomy's own bridge sections and the program's structural vocabulary, organized into four families: valuation (p-adic, ultrametric, adelic, Ostrowski, Bruhat-Tits, product formula, weak/strong approximation), hierarchy (tree, dendrogram, re-entry, stratification), distinction (mark, crossing, law of calling, void), and bound (Landauer, Bekenstein, Bremermann, Margolus-Levitin). Each family is tested for program coverage: which programs contain at least one family keyword.

**Layer 3 — bridge subsections.** The taxonomy's own bridge subsections (UMP Bridge Concepts; RES Cross-Domain Methodology, Cross-Domain Bridges, Measurement Stratigraphy) are extracted, and each of their keywords is traced to the programs where it occurs.

**Layer 4 — cross-cutting themes.** The three cross-cutting sections (agentic AI, 4-D distribution, measurement stratigraphy) are parsed, and their keywords are traced into the program sections.

The corpus check is comparative: the vocabulary-level result is set against a full-corpus semantic sweep (11 query formulations across six topics; cross-system identifier validation; four adjacent domains) and against external literature (arXiv) for the key physics and data-science anchors. All query responses and evidence files are archived in the paper's artifact tree.

## 4. Results

### 4.1 Layer 1 — the taxonomy is strictly partitional

The taxonomy contains 335 distinct keywords. **334 are program-local.** Exactly one keyword — *complexity-measure* — occurs in two programs (INM and RES). **None occurs in three or more programs.** The load-bearing core, defined as keywords shared by at least three programs, is empty.

Per-program keyword counts and bridge-vocabulary shares are shown in Table 1. The bridge share is the fraction of a program's keywords that belong to the a priori bridge families.

| Program | Keywords | Bridge-vocabulary share |
|:--------|---------:|------------------------:|
| UMP — ultrametric physics | 64 | 0.344 |
| SLB — laws of form | 31 | 0.548 |
| INM — infomatics | 47 | 0.213 |
| CFE — paradigm engineering | 48 | 0.000 |
| RES — consilience research | 65 | 0.031 |
| PLT — platform | 58 | 0.000 |
| DEM — demos | 25 | 0.160 |

*Table 1. Keyword counts and bridge-vocabulary shares per program.*

The contingency table for bridge vocabulary versus load-bearing classification is (bridge & load-bearing, bridge & local, non-bridge & load-bearing, non-bridge & local) = (0, 53, 0, 282). Precision (share of the load-bearing core that is bridge) is 0; recall (share of bridge vocabulary that is load-bearing) is 0; the one-sided Fisher p-value is 1.0. At the string level, the claim that the load-bearing core coincides with the bridge vocabulary is rejected: there is no load-bearing core to coincide with anything.

### 4.2 Layer 2 — the bridge families are concentrated, not shared

The four bridge families do not span the program set (Table 2). Valuation vocabulary sits in UMP (21 keywords) and nowhere else. Distinction vocabulary sits in SLB (14 keywords) and nowhere else. Bound vocabulary sits in INM (10 keywords) and nowhere else. Only the hierarchy family spans three programs — SLB (re-entry, crossing), RES (measurement stratigraphy, instrumental stratification), and DEM (ultrametric tree, p-adic tree, dendrogram, hierarchical-clustering tree) — with 8 keywords total.

| Family | Programs containing >= 1 family keyword | Keywords per program |
|:-------|:---------------------------------------|:---------------------|
| valuation | UMP | UMP 21 |
| hierarchy | SLB, RES, DEM | SLB 2, RES 2, DEM 4 |
| distinction | SLB | SLB 14 |
| bound | INM | INM 10 |

*Table 2. Bridge-family coverage across programs.*

The partial verdict is worth stating plainly: of the four families the program treats as its structural vocabulary, only one — hierarchy — is genuinely cross-program in the taxonomy. The arithmetic (valuation) is UMP's; the logic (distinction) is SLB's; the physics (bound) is INM's.

### 4.3 Layer 3 — the taxonomy's own bridge sections are anchors, not links

The taxonomy declares bridge structures explicitly. Auditing them: UMP's Bridge Concepts subsection holds 7 keywords (Ostrowski's theorem, product formula, adele ring, idele class group, restricted direct product, strong and weak approximation), all of which occur only in UMP. RES's Cross-Domain Methodology (7 keywords: duality map, cross-domain correspondence, rosetta-stone analogy, structural realism, cross-paradigm translation, commensurability, incommensurability), Cross-Domain Bridges (6 keywords: Compton-Bruhat-Tits, frequency valuation, mass valuation, Planck-scale physics, quantum-gravity phenomenology), and Measurement Stratigraphy (9 keywords) similarly resolve only to RES. These sections name the bridges; they do not instantiate shared vocabulary. They are program-local anchors pointing at connections the taxonomy does not lexically realize.

### 4.4 Layer 4 — cross-cutting themes carry the real cross-program vocabulary

The three cross-cutting sections are where program vocabulary actually meets: the agentic-AI section's 50 keywords include 5 that also occur in PLT (the MCP family: mcp-server, mcp-tool, mcp-client, mcp-transport, mcp-resource); the 4-D distribution section's 26 keywords include 5 also in PLT (zenodo, zenodo-api, zenodo-upload, zenodo-doi, invenio); the measurement-stratigraphy cross-cutting section's 23 keywords include 4 also in RES (measurement-stratigraphy, measurement-foundations, quantum-measurement, einselection). Every cross-program lexical link in the taxonomy runs through PLT or RES — the platform and the consilience program — and none runs through the theory programs.

### 4.5 Corpus level — the semantic bridges exist

The vocabulary audit says the taxonomy does not lexically realize its own consilience. The corpus audit says the semantic links are nevertheless present. Prior published records connect the families across programs: measurement stratigraphy links RES's epistemology to UMP's valuation theory (10.5281/zenodo.21705220); the valuation-without-reals framework links UMP's non-Archimedean structure to finite-measurement foundations (10.5281/zenodo.21803677); the tree-numeration synthesis shows ordinary positional notation is an ultrametric tree, connecting UMP's geometry to computation and interface design (10.5281/zenodo.21046213); prime valuation depth bridges the calculus of indications to number theory via multiplication-as-branching (10.5281/zenodo.21918838); and a computational study of semantic structures finds ultrametric topology in semantic memory with invariant cross-ratio stability (10.5281/zenodo.19564091). The consilience, at the corpus level, is real and citable. It is just not lexical.

## 5. The revised claim and its disconfirmation criteria

The audit forces a restatement. The program's thesis is not that its keywords cohere. It is that the program's domains share a structural object — nested hierarchical partition logic — and that this object is empirically productive. The claim below is the version this paper can defend, and each clause carries a disconfirmation criterion.

**Structural identification (revised).** The seven programs share a family of nested-partition structures: the ultrametric inequality and its strict hierarchy of nested balls. The specific arithmetic (p-adic valuation, adelic product formula) is one realization; the hierarchy is the invariant. The taxonomy itself supports only this weak form: the hierarchy family is the only bridge family spanning three programs (Section 4.2).

**H1 — compression prior.** Ultrametric structure is an effective compression and clustering prior for high-dimensional sparse measurement data: on at least two independent corpora, an ultrametric index matches or beats cosine/HNSW baselines on retrieval precision at equal build cost. *Disconfirmation criterion:* H1 fails if ultrametric retrieval does not match the baselines on two pre-specified corpora with metrics, primes, and hashes committed before measurement. (The prior art in Section 8 makes "matches" a nontrivial but achievable bar.)

**H2 — Archimedean emergence.** Continuous Archimedean physics appears as the thermodynamic or ergodic average over the leaves of an underlying ultrametric hierarchy. *Disconfirmation criterion:* H2 fails if no derivation exhibits the averaging operation — ergodic mean over leaves or renormalization limit — producing an Archimedean limit theory.

**H3 — non-Archimedean signature.** Quantum-coherent systems under structured hierarchical noise exhibit decoherence scaling that deviates from the standard Markovian prediction in a p-adic pattern (power-of-prime hierarchy). *Disconfirmation criterion:* H3 fails if structured-noise decoherence measurements show no deviation from Markovian models at the precision of the stated protocol.

**Decision point.** The strong form of the program — a physics-relevant non-Archimedean substrate — is falsified by 2028 if neither H1 nor H3 yields a positive result.

## 6. Practitioner deliverables

Three artifacts make the program usable without any commitment to its ontology.

**Deliverable 1 — the p-adic fingerprint index.** A retrieval index that maps documents to p-adic fingerprints (SHA-256 hashes truncated modulo p^k), ranks by valuation depth, and is benchmarked head-to-head against cosine/HNSW on two public corpora. The benchmark script, seeds, and corpora are committed with the paper. This is usable today as a content-addressing and retrieval tool; its performance result is the H1 test.

**Deliverable 2 — the structured-noise decoherence protocol.** A measurement specification for RQ4: qubit coupled to hierarchical noise, noise model, pulse sequence, expected scaling (p-adic power-of-prime vs 1/n^2 Markovian), significance threshold, and platform notes for trapped-ion and superconducting hardware. An experimental group can cost this protocol directly from the paper.

**Deliverable 3 — the machine-readable consilience map.** The audit's graph output (`artifacts/p2-consilience-map.json`, 342 nodes, 336 ownership edges) records programs, keywords, load-bearing flags, and bridge-family memberships. It is the vocabulary index for the corpus: any paper, keyword, or program can be located in the map and its bridge family read off.

## 7. Where the premises end

The argument in this paper is bounded by an explicit premise chain.

- **L0 — unanalyzable primitives:** the act of distinction (the mark); the notion of observation or measurement; the rational numbers as a field. Nothing below this layer is derived.
- **L1 — imported theorem:** Ostrowski's classification — every nontrivial absolute value on the rationals is Archimedean or p-adic. Used, not re-proven.
- **L2 — structural bridge (named input):** the identification of measurement hierarchies with ultrametric valuation structure. Prior records support this as a correspondence; it is a modeling choice, not a theorem.
- **L3–L5 — hypotheses H1, H2, H3:** empirical claims decided by the criteria of Section 5.

The "logical origin" story therefore stops at L0; the bridge sits at L2 as a named input; everything deeper is testable hypothesis. In particular, the paper does not assert that reality is ultrametric. It asserts that a specific compression prior is testable and that the program's standing is decided by the test.

## 8. Related work

**Ultrametric data science.** Murtagh established the modern empirical program: ultrametric embedding for data fingerprinting and fast clustering (arXiv:math/0605555v2, 2006); pervasive ultrametricity in high-dimensional and sparse data (arXiv:physics/0702064v1, 2007); ultrametricity measured in text corpora (arXiv:1201.2719v3, 2012); and ultrametric logic in data analysis (arXiv:1008.3585v1, 2010). H1 is explicitly a re-execution and benchmark of this program on modern retrieval baselines — the prior art is cited from the first paragraph of the H1 protocol, and novelty is claimed only for the modern-baseline comparison and the p-adic-hash fingerprint variant. Chehreghani and Chehreghani (arXiv:1812.09225v4, 2018) provide dendrogram-based representation learning, a required benchmark baseline for H1.

**Ultrametricity in statistical physics.** The canonical physics instance of ultrametric structure is replica symmetry breaking in spin glasses: Parisi's order parameter (Phys. Rev. Lett. 50, 1946, 1983) and the Rammal–Toulouse–Virasoro review of ultrametricity (Rev. Mod. Phys. 58, 765, 1986). Recent work has moved this from theory to measurement: the overlap distribution measured in random lasers (arXiv:2209.03781v2, 2022); incipient ultrametric order in a driven-dissipative cavity-QED quantum spin glass (arXiv:2307.10176v2, 2023) — the nearest existing experiment to H3; and ultrametric Parisi matrices recovered from real-time Keldysh dynamics (arXiv:2406.05842v3, 2024) — a genuine dynamics precedent for H2's averaging requirement. The counterpoint is equally real: Newman and Stein argue that replica symmetry breaking cannot be correct for finite-dimensional short-range spin glasses (arXiv:cond-mat/0105282v3, 2001). H2 and H3 confront this controversy explicitly rather than ignore it.

**p-adic and adelic physics.** The classical literature (Vladimirov, Volovich, Zelenov, *p-Adic Analysis and Mathematical Physics*, World Scientific, 1994) provides the mathematical foundation for the program's UMP pillar; the program's own adelic synthesis records (10.5281/zenodo.21590155 and the adelic core synthesis) apply it to quantum field theory at the level of toy models, which is exactly the level the program's claims occupy.

## 9. Limitations and open problems

**The CFE gap.** The paradigm-engineering program (48 keywords) contains no bridge-family vocabulary at all (bridge share 0.000) and shares no keywords with any other program. The paper's consilience table either builds the CFE bridge explicitly — forecasting and learning-curve keywords as a hierarchy over paradigms — or marks CFE as the weakest documented link. This audit does not resolve the choice; it records it.

**Encoding dependence.** The p-adic valuation of a measurement requires digitizing and hashing the raw reading first; the hash is a chosen convention, not physics (this is the map-territory hazard of Section 2's data note). H1's protocol therefore commits the hash, the prime, and the corpora before measurement, and the result is conditional on those commitments.

**The dynamics gap.** The taxonomy and the corpus are rich in statics (geometry, bounds, hierarchies) and poor in dynamics. H2 requires an explicit averaging operation; none is specified in the corpus. Section 5's disconfirmation criterion for H2 is deliberately written to require that derivation rather than permit it to be assumed.

**Plurality.** The audit's strongest positive finding — the hierarchy family spanning SLB, RES, and DEM — supports the invariant-as-hierarchy reading, not a single-radix reading. The vocabulary offers no evidence that the program's structure is one hidden basis; it offers evidence that nested partitions recur. The program's own question, whether its unity is a single structure or a family of incommensurable grammars with translation but no reduction, remains open, and the deliverable-3 map is designed so that either answer can be read off the corpus.

## 10. Reproducibility

All quantitative claims in this paper are produced by `artifacts/verification/rq5_keyword_load.py` (deterministic; Python standard library only; no random seeds required). Inputs: `artifacts/verification/keyword-taxonomy-source.md` (the v1.0 taxonomy snapshot, byte-verified against the canonical location at fetch time). Outputs: `artifacts/verification/rq5_results.json` (full results), `artifacts/p2-consilience-map.json` (graph), run log archived. Re-running the script from the repository root regenerates the two JSON artifacts byte-identically. Corpus statistics (8,324 nodes; 1,660 papers) were read from the program's knowledge-graph endpoint on 2026-08-23; external-literature evidence files (arXiv) are archived in `artifacts/external-search/`. Runtime: under one second on the reference machine; no external services required.

## References

1. QNFO Research Program Keyword Taxonomy, v1.0, 2026-08-05. Canonical: docs/QNFO-KEYWORD-TAXONOMY.md.
2. F. Murtagh. Ultrametric embedding: application to data fingerprinting and to fast data clustering. arXiv:math/0605555v2, 2006.
3. F. Murtagh. Hilbert Space Becomes Ultrametric in the High Dimensional Limit. arXiv:physics/0702064v1, 2007.
4. F. Murtagh. Ultrametric Model of Mind, II: Application to Text Content Analysis. arXiv:1201.2719v3, 2012.
5. F. Murtagh. Ultrametric and Generalized Ultrametric in Computational Logic and in Data Analysis. arXiv:1008.3585v1, 2010.
6. M. H. Chehreghani and M. H. Chehreghani. Learning Representations from Dendrograms. arXiv:1812.09225v4, 2018.
7. C. Conti, N. Ghofraniha, L. Leuzzi, G. Ruocco. Replica symmetry breaking in random lasers: experimental measurement of the overlap distribution. arXiv:2209.03781v2, 2022.
8. B. P. Marsh, R. M. Kroeze, S. Ganguli, S. Gopalakrishnan, J. Keeling, B. L. Lev. Entanglement and replica symmetry breaking in a driven-dissipative quantum spin glass. arXiv:2307.10176v2, 2023.
9. J. Lang, S. Sachdev, S. Diehl. Replica symmetry breaking in spin glasses in the replica-free Keldysh formalism. arXiv:2406.05842v3, 2024.
10. C. M. Newman and D. L. Stein. The State(s) of Replica Symmetry Breaking: Mean Field Theories vs. Short-Ranged Spin Glasses. arXiv:cond-mat/0105282v3, 2001.
11. G. Parisi. Order parameter for spin glasses. Phys. Rev. Lett. 50, 1946, 1983.
12. R. Rammal, G. Toulouse, M. A. Virasoro. Ultrametricity for physicists. Rev. Mod. Phys. 58, 765, 1986.
13. V. S. Vladimirov, I. V. Volovich, E. I. Zelenov. *p-Adic Analysis and Mathematical Physics*. World Scientific, 1994.
14. The Consilience Framework: From Valuation Theory to the Void — A Cross-Domain Synthesis. 10.5281/zenodo.21804073, 2026.
15. Ultrametric Consilience Atlas: Cross-Domain Applications of p-Adic Mathematical Structure. 10.5281/zenodo.21722395, 2026.
16. Consilience Between Physics and Number Theory: Convergent Theses from Ostrowski's Theorem to Adelic Quantum Mechanics. 10.5281/zenodo.21590155, 2026.
17. The History and Future of Measurement Stratigraphy, Number Theory, and Valuation Theory. 10.5281/zenodo.21705220, 2026.
18. Valuation Without R: A Category-Theoretic Foundation for Finite Measurement. 10.5281/zenodo.21803677, 2026.
19. Nonlinear Tree-Based Numeration Systems: A Consolidated Synthesis. 10.5281/zenodo.21046213, 2026.
20. Prime Valuation Depth: Multiplication as Branching, the Calculus of Indications, and the Structural No-Cloning Reading. 10.5281/zenodo.21918838, 2026.
21. Projective Geometric Frameworks for Semantic Structures. 10.5281/zenodo.19564091, 2026.
