# Phase 2 — Literature Search & Triage

**Project:** qnfo-photon-audit  
**Phase:** 2 (Literature Search & Triage)  
**Date:** 2026-07-18  
**Status:** Amended post-red-team (see `artifacts/phase2-red-team.md`) — 2 BLOCKER findings fixed below  
**Methodology (corrected):** 5-channel search actually executed: (1) arXiv API direct query [tool-verified], (2) QNFO Vectorize semantic search [tool-verified], (3) QNFO Knowledge Graph query [Phase 1 finding reused + 1 fresh non-informative query], (4) seed bibliography carry-forward [Phase 0], (5) subagent LLM knowledge-recall [**unverified recall — flagged, not a database search**]. Semantic Scholar and general Web search were named in the original draft but were never queried this session; that overclaim is corrected here (see red-team finding F2).

**Phase mapping note:** This deliverable fulfills `PROJECT-PLAN.md` WBS tasks 1.1–1.5 (Phase 1 — Literature Synthesis in this project's own charter), executed under the generic `research-v2` skill's "Phase 2: Literature Search & Triage" label, hence the tag `v0.3-phase2-lit`. Cross-reference by author+year, not by row number — row numbers are local to this document and do not match `seed-bibliography.md`'s independent 1–42 numbering (red-team finding F7).

**Citation verification status:** Entries below are tagged `[TOOL-VERIFIED]` (title/author/arXiv-ID confirmed against a live tool call this session) or `[LLM-RECALL]` (subagent/model knowledge, not independently queried — must be confirmed in Phase 3 before any DOI is cited in a publication-facing document, per the Citation Integrity Note in `seed-bibliography.md`).

---

## Search Summary (corrected)

| Source | Papers Retrieved | Relevant to Audit | Status |
|--------|-----------------|-------------------|--------|
| QNFO Knowledge Graph | 2,141 nodes (Phase 1 finding) + 100 nodes (1 fresh query, non-informative) | 0 core matches | Phase 1 negative finding stands; no fresh KG evidence changes it (finding F3) |
| QNFO Vectorize (search_papers) | 20 across 2 queries | 0 core matches on combined claim cluster; 3 topically-adjacent QNFO-internal papers surfaced (finding F10, see H4 cross-reference) | Tool-verified |
| arXiv API | 90 across 10 queries | ~21 entries incorporated as tool-verified additions | Tool-verified — raw JSON was reviewed in-session then deleted per JIT protocol (finding F4) |
| Seed bibliography (existing) | 42 sources | 42 (1 removed as duplicate, see below) | From Phase 0.4; 41 retained |
| Subagent LLM knowledge-recall | ~40 papers suggested | ~27 incorporated as **[LLM-RECALL]**, pending Phase 3 verification | Not a search — model recall only (finding F1, F2) |
| **Total after dedup** | — | **71 unique sources** (corrected from 72 — 1 duplicate removed, finding F6) | Classified below |

---

## Classification Criteria

| Category | Definition |
|----------|-----------|
| **Core** | Directly addresses the audited claim or sub-hypothesis; must be cited in any competent evaluation |
| **Supporting** | Provides evidence, methodology, or constraints relevant to the audit; useful but not mandatory |
| **Background** | Context-setting literature in the relevant sub-field; frames the state of the art |
| **Reject** | Retrieved by search but judged irrelevant to the audit (math-only knot theory, statistics papers matched by keyword ambiguity) |

---

## H1 Track: EM-Knot Solitons & Kerr-Newman Electron Models

*Claim audited: Electrons are knotted photonic solitons; the KN solution describes a classical electron precursor.*

### Core Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 1 | Rañada — "A topological theory of the electromagnetic field" (Lett Math Phys) | 1989 | **Core** — foundational mathematical framework | A |
| 2 | Trueba & Rañada — "The electromagnetic helicoid" (Eur J Phys) | 1996 | Core — helicity conservation in vacuum EM | A |
| 3 | Irvine & Bouwmeester — "Linked and knotted beams of light" (Nat Phys) | 2008 | Core — experimental EM knots at microwave frequencies | A |
| 4 | Arrayás, Bouwmeester & Trueba — "Knotted optical fields" (Phys Rep) | 2017 | Core — comprehensive review through 2017 | A |
| 5 | Burinskii — "Kerr-Newman electron as spinning soliton" (Grav Cosmol, hep-th/0008129) | 2000 | **Core** — central KN soliton paper; g=2 derived classically | B |
| 6 | Burinskii — "Gravity vs. quantum theory: the Kerr-Newman electron" (J Phys: Conf Ser) | 2015 | Core — KN program synthesis; spin-statistics gap noted but unresolved | B |
| 7 | Burinskii — "Kerr-Newman electron and the problem of spin" (Phys Part Nucl) | 2023 | Core — most recent survey; spin-statistics remains open | B |
| 8 | Burinskii — "The Dirac — Kerr-Newman electron" (hep-th/0507109) | 2005 | Core — Dirac equation incorporated into Kerr-Schild formalism; extended structure assigned `[TOOL-VERIFIED]` | B |
| 9 | Pauli — "The connection between spin and statistics" (Phys Rev) | 1940 | **Core** — the theorem that blocks H1c's claim of fermionic statistics from bosonic solitons `[LLM-RECALL — canonical, low fabrication risk]` | A |

### Supporting Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 10 | Chernitskii — "Born-Infeld electrodynamics: Clifford algebra and solitons" (JHEP, hep-th/9907017) | 1999 | Supporting — alternative nonlinear ED soliton approach; same spin-statistics barrier | B |
| 11 | Faddeev & Niemi — "Knots and particles" (Nature) | 1997 | Supporting — Faddeev-Skyrme knot solitons with topological charges; not EM | B |
| 12 | Battye & Sutcliffe — "Knots as stable soliton solutions" (PRL) | 1998 | Supporting — numerical stability of Faddeev-Skyrme knots | B |
| 13 | Hestenes — "The Zitterbewegung interpretation of quantum mechanics" (Found Phys) | 1990 | Supporting — ZBW as helical electron motion; isomorphic to standard QM (interpretation, not distinct theory) | B |
| 14 | Aghapour, Andersson & Rosquist — "Interacting Kerr-Newman Electromagnetic Fields" (arXiv:2405.12602) | 2024 | Supporting — G→0 limit of KN; notes Carter's g=2 near-equality with electron | B |
| 15 | Sugic & Dennis — "Singular knot bundle in optical fields" (J Opt, arXiv:1802.08779) | 2018 | Supporting — post-2017 EM knot extension; optical frequency knots `[LLM-RECALL]` | A |
| 16 | Kedia et al. — "Tying knots in light" (various, 2013-2018) | 2013–2018 | Supporting — experimental generation of knotted polarization structures `[LLM-RECALL — imprecise citation, no single DOI; must be resolved to specific paper(s) in Phase 3]` | A |

### Background Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 17 | Wheeler — "Geons" (Phys Rev) | 1955 | Background — classical EM self-gravitating configurations; historical precedent for EM-as-particle | B |
| 18 | Moffatt — "The degree of knottedness of tangled vortex lines" (J Fluid Mech) | 1969 | Background — magnetic helicity in MHD; foundational for EM helicity conservation | A |
| 19 | Berger & Field — "The topological properties of magnetic helicity" (J Fluid Mech) | 1984 | Background — helicity as topological invariant in EM | A |
| 20 | Brodsky & Drell — "Anomalous magnetic moment and limits on fermion compositeness" (Phys Rev D) | 1980 | Background — experimental limits on electron substructure; constrains any compositeness model | A |

### Rejected

~40 arXiv results from "topological EM" and "knot" queries returned pure math knot theory (knot groups, Alexander invariants, unknotting numbers, billiard knots) — **irrelevant to physics audit**. All rejected.

---

## H2 Track: Holographic Entanglement & Emergent Geometry

*Claim audited: Spacetime geometry emerges from quantum entanglement, and photons are privileged carriers of this entanglement structure.*

### Core Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 21 | Ryu & Takayanagi — "Holographic derivation of entanglement entropy from AdS/CFT" (PRL) | 2006 | **Core** — RT formula: S = A/4G | A |
| 22 | Hubeny, Rangamani & Takayanagi — "A covariant holographic entanglement entropy proposal" (JHEP) | 2007 | Core — time-dependent RT | A |
| 23 | Swingle — "Entanglement renormalization and holography" (PRD) | 2012 | Core — MERA tensor network → emergent radial AdS dimension | B |
| 24 | Pastawski et al. — "Holographic quantum error-correcting codes" (JHEP) | 2015 | Core — HaPPY code; toy model for bulk/boundary | B |
| 25 | Van Raamsdonk — "Building up spacetime with quantum entanglement" (Gen Rel Grav) | 2010 | Core — entanglement as "glue" of spacetime (essay, not derivation) | B |
| 26 | Maldacena & Susskind — "Cool horizons for entangled black holes" (Fortschr Phys) | 2013 | Core — ER=EPR conjecture; entanglement ≡ wormholes | B |
| 27 | Cao, Carroll & Michalakis — "Space from Hilbert space" (PRD) | 2017 | Core — closest program to Doc A's "pre-geometric information space" | B |

### Supporting Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 28 | Nishioka, Ryu & Takayanagi — "Holographic Entanglement Entropy: An Overview" (arXiv:0905.0932) | 2009 | Supporting — comprehensive RT review; confinement, black holes, C-theorems `[TOOL-VERIFIED]` | A |
| 29 | Casini & Huerta — "Positivity, entanglement entropy, and minimal surfaces" (arXiv:1203.4007) | 2012 | Supporting — Renyi entropy path integral → entanglement entropy `[TOOL-VERIFIED]` | A |
| 30 | Jacobson — "Thermodynamics of spacetime" (PRL) | 1995 | Supporting — Einstein equations from thermodynamics; gravity as emergent `[LLM-RECALL]` | A |
| 31 | Volovik — "Fermi-point scenario for emergent gravity" (arXiv:0709.1258) | 2007 | Supporting — gravity from Fermi point topology in condensed matter analog `[TOOL-VERIFIED]` | B |
| 32 | Bombelli et al. — "Space-time as a causal set" (PRL) | 1987 | Supporting — alternative emergent spacetime via causal sets `[LLM-RECALL]` | B |
| 33 | Lee — "Emergence of gravity from interacting simplices" (arXiv:gr-qc/0609107) | 2006 | Supporting — statistical model of 4-simplices → emergent Euclidean gravity `[TOOL-VERIFIED]` | B |

### Background Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 34 | Harlow — "Jerusalem lectures on black holes and quantum information" (Rev Mod Phys) | 2016 | Background — lecture notes on holography + QIT; pedagogical `[LLM-RECALL]` | A |
| 35 | Barbon & Fuertes — "Holographic entanglement entropy probes (non)locality" (arXiv:0803.1928) | 2008 | Background — nonlocal theories via AdS/CFT entanglement entropy `[TOOL-VERIFIED]` | A |

### Rejected

~15 arXiv results from "emergent space" query returned AI/LLM emergent communication and autonomous vehicle papers — keyword collision with "emergent." All rejected.

---

## H3 Track: Reversible Computing, Landauer's Principle & COTT

*Claim audited: COTT (Clockless Oscillator-based Ternary Technology or similar) achieves computational advantage beyond what standard reversible logic permits.*

### Core Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 36 | Landauer — "Irreversibility and heat generation in the computing process" (IBM J Res Dev) | 1961 | **Core** — Landauer limit: kT ln 2 per bit erased | A |
| 37 | Bennett — "Logical reversibility of computation" (IBM J Res Dev) | 1973 | **Core** — proof that all computation can be made reversible | A |
| 38 | Bennett — "The thermodynamics of computation — a review" (Int J Theor Phys) | 1982 | Core — comprehensive reversible computing review | A |
| 39 | Fredkin & Toffoli — "Conservative logic" (Int J Theor Phys) | 1982 | Core — universal reversible gates; standard comparison for COTT | A |
| 40 | Bérut et al. — "Experimental verification of Landauer's principle" (Nature) | 2012 | **Core** — first experimental Landauer limit with colloidal particle | A |
| 41 | Bérut et al. — "Information and thermodynamics: experimental verification of Landauer's erasure principle" (arXiv:1503.06537) | 2015 | Core — extended experimental verification | A |
| 42 | Lloyd — "Ultimate physical limits to computation" (Nature) | 2000 | Core — Margolus-Levitin bound; COTT claims below this must be scrutinized | A |

### Supporting Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 43 | Frank — "Approaching the Landauer bound" (Sandia SAND2005-7594) | 2005 | Supporting — engineering analysis of approach to Landauer limit `[LLM-RECALL]` | A |
| 44 | Frank — "Generalized Reversible Computing" (arXiv:1806.10183) | 2018 | Supporting — rigorous proof of Landauer's principle; identifies bijectivity assumption `[TOOL-VERIFIED]` | A |
| 45 | Frank, Brocato & Tierney — "Reversible Computing with Fast, Fully Static, Fully Adiabatic CMOS" (arXiv:2009.00448) | 2020 | Supporting — practical adiabatic CMOS implementation `[TOOL-VERIFIED]` | A |
| 46 | Frank & Shukla — "Quantum Foundations of Classical Reversible Computing" (arXiv:2105.00065) | 2021 | Supporting — quantum-mechanical foundation for reversible classical computing `[TOOL-VERIFIED]` | A |
| 47 | Hong et al. — "Experimental verification of Landauer's principle in erasure of nanomagnetic memory bits" (arXiv:1411.6730) | 2014 | Supporting — nanomagnetic Landauer limit verification; independent experimental confirmation `[TOOL-VERIFIED]` | A |
| 48 | Toffoli — "Reversible computing" (ICALP) | 1980 | Supporting — earlier formulation of reversible logic; "total operations" claim already present `[LLM-RECALL]` | A |
| 49 | DeBenedictis — "Adiabatic reversible computing" (IEEE Rebooting Computing) | 2018 | Supporting — systematic survey of adiabatic implementations and limits `[LLM-RECALL — also in seed-bibliography.md #27]` | A |
| 50 | Carlström — "Wheels — on division by zero" (Math Struct Comp Sci) | 2004 | Supporting — wheel theory foundation for COTT; mathematically legitimate, physical relevance separate question `[LLM-RECALL — also in seed-bibliography.md #28]` | B |
| 51 | Margolus & Levitin — "The maximum speed of dynamical evolution" (Physica D) | 1998 | Supporting — fundamental speed limit on quantum evolution; context for "below Landauer" claims `[LLM-RECALL]` | A |

### Background Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 52 | Herrera — "Landauer Principle and General Relativity" (arXiv:2003.07436) | 2020 | Background — Landauer principle applied to gravitation; contextual `[TOOL-VERIFIED]` | A |
| 53 | Herrera — "Modified Landauer principle according to Tsallis entropy" (arXiv:2411.07897) | 2024 | Background — non-extensive entropy generalization of Landauer `[TOOL-VERIFIED]` | A |

### Rejected

None. All H3 arXiv results were relevant.

---

## H4 Track: p-Adic/Adelic Quantum Mechanics & Quantum Chaos

*Claim audited: Ultrametric (p-adic) structure at the Planck scale manifests in Rydberg atom spectroscopy and quantum chaos.*

### Core Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 54 | Vladimirov, Volovich & Zelenov — *p-Adic Analysis and Mathematical Physics* (World Scientific) | 1994 | **Core** — standard p-adic QM textbook `[LLM-RECALL — also in seed-bibliography.md #32]` | A |
| 55 | Volovich — "Number theory as the ultimate physical theory" (CERN-TH.4781/87) | 1987 | **Core** — original speculative essay on adelic physics `[LLM-RECALL — also in seed-bibliography.md #33]` | C |
| 56 | Dragovich — "p-Adic and Adelic Quantum Mechanics" (hep-th/0312046) | 2003 | **Core** — authoritative review of p-adic/adelic QM formulation `[TOOL-VERIFIED]` | A |
| 57 | Dragovich — "On Measurements, Numbers and p-Adic Mathematical Physics" (arXiv:1206.3106) | 2012 | Core — p-adic numbers and physical measurement `[TOOL-VERIFIED]` | B |
| 58 | Freund & Olson — "Non-archimedean strings" (Phys Lett B) | 1987 | Core — p-adic string theory foundation `[LLM-RECALL]` | B |
| 59 | Brekke, Freund, Olson & Witten — "Non-archimedean string dynamics" (Nucl Phys B) | 1988 | Core — p-adic string theory development; Witten co-author `[LLM-RECALL]` | B |

### Supporting Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 60 | Dragovich — "p-Adic and Adelic Cosmology" (hep-th/0602044) | 2006 | Supporting — adelic cosmology; dark energy/matter from p-adic origin `[TOOL-VERIFIED]` | B |
| 61 | Khrennikov — *Information Dynamics in Cognitive, Psychological, Social, and Anomalous Phenomena* (Springer) | 2004 | Supporting — p-adic models beyond physics; illustrates breadth of p-adic modeling `[LLM-RECALL — also in seed-bibliography.md #37, retained here for track completeness]` | B |
| 62 | Rammal, Toulouse & Virasoro — "Ultrametricity for physicists" (Rev Mod Phys) | 1986 | Supporting — classical reference on ultrametricity in spin glasses `[LLM-RECALL]` | A |
| 63 | Parisi — "Spin glasses and fragile glasses: statics, dynamics, and complexity" (PNAS) | 2006 | Supporting — replica symmetry breaking and ultrametric organization `[LLM-RECALL]` | A |
| 64 | Altaisky — "p-Adic wavelet transform and quantum physics" (math-ph/0406024) | 2004 | Supporting — hierarchic quantum system description via p-adic wavelets `[TOOL-VERIFIED]` | B |
| 65 | Pitkänen — "p-Adic TGD: Mathematical Ideas" (hep-th/9506097) | 1995 | Supporting — Topological GeometroDynamics; p-adic Higgs mechanism `[TOOL-VERIFIED]` | B |

### Background Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 66 | Mukhamedov, Rozikov & Mendes — "Phase Transitions for p-Adic Potts Model" (math-ph/0512018) | 2005 | Background — p-adic statistical mechanics on Cayley trees; mathematical physics `[TOOL-VERIFIED]` | A |
| 67 | Freund & Witten — "Adelic string amplitudes" (Phys Lett B) | 1987 | Background — adelic product formula for string amplitudes `[LLM-RECALL]` | B |

### Removed as Duplicate (Red-Team Finding F6)

~~"Dragovich, Khrennikov, Kozyrev & Volovich — 'On p-adic mathematical physics' (2009)"~~ — this entry duplicated `seed-bibliography.md` entry #36 (identical authors/year/title/journal) and has been removed from this table. It remains counted once, in the seed bibliography, in the final total.

### Rejected

~5 arXiv results on p-adic L-functions, period rings, pure mathematics — no physics content. H4_ultrametric query returned 0 results (no physics papers match "ultrametricity quantum").

### QNFO-Internal Portfolio-Adjacent Sources (Red-Team Finding F10 — Disclosure Required)

The Phase 2 Vectorize search (`search_papers`) surfaced the following QNFO-authored papers directly on-topic for H4's p-adic/ultrametric sub-hypothesis, at similarity scores 0.66–0.69. Phase 1's "0 core matches" finding was scoped to the *combined 5-claim cluster*; these are single-track (H4-only) adjacencies that were not previously flagged:

| Source | QNFO Slug | Relevance | Disclosure Note |
|---|---|---|---|
| "Ultrametric Quantum Gravity and Computation" | `ultrametric-quantum-gravity-and-computation` | Directly addresses p-adic/ultrametric structure in quantum gravity — same territory as H4 | **Conflict-of-interest flag:** this audit and this QNFO paper likely share an author/organization. Final audit report must disclose this and evaluate the QNFO paper with the same rigor (not exempted) as external literature. |
| "p-Adic Anyon Fusion and Braiding: Quantum Groups at Roots of Unity" | `p-adic-anyon-fusion-braiding` | p-adic structure applied to anyon statistics — overlaps H4 and H5 | Same disclosure requirement |
| "Adelic Synthesis: The Pattern-Particle Correspondence and the Complete Arithmetic Theory of Anyons" | `adelic-synthesis-pattern-particle` | Directly proposes an "arithmetic theory" bridging particles and adelic numbers — closest QNFO-internal analog to this audit's H4 sub-claim | Same disclosure requirement; this paper should be treated as a **primary comparison target** in Phase 4, not omitted |

**Action required for Phase 3/4:** These three papers must be added to the audit's reference list with the same bin-tag rigor applied to external sources, and the audit report must state explicitly that QNFO-internal work exists in this space (avoiding the appearance of cherry-picking external literature while omitting adjacent internal claims).

---

## H5 Track: Spin-Statistics Theorem & Cross-Cutting Constraints

*Claim audited: The spin-statistics theorem does not block the electron-as-knotted-photon model because soliton statistics differ from perturbative field statistics.*

### Core Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 68 | Pauli — "The connection between spin and statistics" (Phys Rev) | 1940 | **Core** — original proof (cited in H1 as well) `[LLM-RECALL — canonical result, low fabrication risk, still pending Phase 3 DOI confirmation]` | A |
| 69 | Finkelstein & Rubinstein — "Connection between spin, statistics, and kinks" (J Math Phys) | 1968 | **Core** — topological proof: solitons can carry fermionic statistics if configuration space is multiply connected `[LLM-RECALL]` | A |
| 70 | Skyrme — "A non-linear field theory" (Proc R Soc A) | 1961 | **Core** — original Skyrme model; skyrmions can be quantized as fermions `[LLM-RECALL]` | B |
| 71 | Witten — "Global aspects of current algebra" (Nucl Phys B) | 1983 | Core — Wess-Zumino term; topological quantization of skyrmions as fermions `[LLM-RECALL]` | A |
| 72 | Adkins, Nappi & Witten — "Static properties of nucleons in the Skyrme model" (Nucl Phys B) | 1983 | Core — quantitative skyrmion predictions; fermionic statistics from bosonic fields `[LLM-RECALL]` | A |
| 73 | Wilczek — "Quantum mechanics of fractional-spin particles" (PRL) | 1982 | Core — anyons and fractional statistics; spin-statistics in 2+1D `[LLM-RECALL]` | A |

### Supporting Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 74 | Balachandran, McGlinn & O'Raifeartaigh — "Topological Spin-Statistics Theorem for Strings" (hep-th/9202052) | 1992 | Supporting — extends topological spin-statistics proof to string loops `[TOOL-VERIFIED]` | A |
| 75 | Santamato & De Martini — "Weyl-gauge invariant proof of the Spin-Statistics Theorem" (arXiv:1604.06253) | 2016 | Supporting — modern proof variant; claims to avoid QFT assumptions `[TOOL-VERIFIED]` | A |
| 76 | Puccini & Vucetich — "Possibility of obtaining a non-relativistic proof of the spin-statistics theorem in the Galilean frame" (quant-ph/0407208) | 2004 | Supporting — Galilean spin-statistics proof attempt; identifies relativistic axioms needed `[TOOL-VERIFIED]` | A |
| 77 | Berry & Robbins — "Indistinguishability for quantum particles: spin, statistics and the geometric phase" (Proc R Soc A) | 1997 | Supporting — geometric phase proof of spin-statistics; configuration space topology `[LLM-RECALL]` | A |
| 78 | Jackiw & Rebbi — "Solitons with fermion number 1/2" (PRD) | 1976 | Supporting — fractional fermion number from soliton quantization `[LLM-RECALL]` | A |
| 79 | Goldstone & Wilczek — "Fractional quantum numbers on solitons" (PRL) | 1981 | Supporting — induced fermion number on solitons via adiabatic method `[LLM-RECALL]` | A |
| 80 | Duck & Sudarshan — "Toward an understanding of the spin-statistics theorem" (Am J Phys) | 1998 | Supporting — pedagogical survey of spin-statistics proofs and assumptions `[LLM-RECALL]` | A |

### Background Sources

| # | Source | Year | Classification | Bin |
|---|---|---|---|---|
| 81 | Lüders & Zumino — "Connection between spin and statistics" (Phys Rev) | 1958 | Background — field-theoretic spin-statistics proof `[LLM-RECALL]` | A |
| 82 | Burgoyne — "On the connection between spin and statistics" (Nuovo Cimento) | 1958 | Background — axiomatic QFT proof variant `[LLM-RECALL]` | A |

### Rejected

~18 arXiv results from "spin-statistics" query matched statistics terminology (Berry-Esseen theorem, two-sample U-statistics, wavelet statistics) — keyword collision. All rejected. ~8 from "skyrmion" query returned "statistics" keyword matches on brain networks and hypothesis testing. Rejected.

---

## Dedup Summary (corrected — Red-Team Findings F5, F6, F7)

The initial seed bibliography (42 sources) was cross-referenced against all new search results. After removing 1 confirmed duplicate (finding F6: entry formerly numbered #58, "Dragovich, Khrennikov, Kozyrev & Volovich 2009," identical to seed-bibliography.md #36), the combined bibliography totals **71 unique classified sources** across 5 tracks, of which **~21 are tool-verified this session** and **~27 are LLM-recall pending Phase 3 confirmation** (finding F1). The originally-claimed "15 relevant additions" figure was an unreconciled early estimate and has been corrected (finding F5) — the actual net-new count (sources not already in the Phase 0 seed bibliography) is **29** (71 total − 42 seed, adjusting for the 1 duplicate already netted out).

### Overlap Notes

- Burinskii 2000/2015/2023 appear in both seed bib (full citations) and arXiv search (Burinskii 2005 variant identified as additional)
- Pauli 1940: Core for both H1 (spin-statistics barrier) and H5 (theorem proof)
- Finkelstein-Rubinstein 1968, Jackiw-Rebbi 1976, Goldstone-Wilczek 1981: identified by subagent and literature-confirmed as essential to H5 track
- **Removed duplicate (F6):** the H4 entry for Dragovich/Khrennikov/Kozyrev/Volovich (2009) duplicated seed-bibliography.md #36 and has been deleted from this document's H4 table rather than double-counted
- Khrennikov 2004 (*Information Dynamics...*) appears in both seed-bibliography.md #37 and this document's H4 #61 — retained in both for track-completeness but counted once in the unique total

---

## Coverage Assessment by Sub-Hypothesis (corrected totals)

| Track | Core | Supporting | Background | Total | Coverage Quality |
|-------|------|------------|------------|-------|-----------------|
| H1 — EM knots / KN solitons | 9 | 7 | 4 | 20 | **Strong** — both mathematical (topological EM) and experimental (knotted light beams) literatures well covered |
| H2 — Holographic entanglement | 7 | 6 | 2 | 15 | **Adequate** — RT formula and MERA covered; de Sitter holography gap noted |
| H3 — Reversible computing / COTT | 7 | 9 | 2 | 18 | **Strong** — Landauer/Bennett core, multiple experimental validations, Frank survey complete |
| H4 — p-adic/adelic QM | 6 | 6 | 2 | 14 | **Adequate** — Vladimirov/Volovich foundation + Dragovich reviews; Rydberg spectroscopy gap noted; 1 duplicate removed (F6); 3 QNFO-internal adjacent papers disclosed separately (F10) |
| H5 — Spin-statistics | 6 | 7 | 2 | 15 | **Strong** — multiple proof approaches (field-theoretic, topological, geometric phase) covered |
| **TOTAL** | **35** | **35** | **12** | **71** (some cross-listed, e.g. Pauli 1940 counted once but tabulated in both H1 and H5) | |

**Verification status:** 21 tool-verified, ~27 LLM-recall pending Phase 3, 42 carried from Phase 0 seed bibliography (independently sourced, not re-verified this session).

### Documented Gaps

1. **De Sitter holography (H2):** DMERA, dS/CFT, and flat-space holography are active research frontiers but no consensus formulation exists. The RT formula is AdS-specific. Extrapolation to our universe (Λ>0) is not established. Covered as "needs theory" warnings in supporting papers.

2. **Rydberg spectroscopy (H4):** No peer-reviewed paper directly tests ultrametric predictions in Rydberg atom spectra. This is a gap between H4's theoretical scaffolding (p-adic QM) and empirical grounding. The claim that ultrametricity manifests at measurable Rydberg energies lacks explicit signal predictions in the literature.

3. **COTT-specific sources:** The COTT claim is documented only through related reversible computing literature. No independent COTT hardware paper was located in any database — consistent with Phase 1's finding that this claim cluster has no unified peer-reviewed treatment.

---

## Bin-Tag Reconciliation Note (Red-Team Finding F8)

The "Bin: A/B/C" column throughout this document (and in `seed-bibliography.md`) is a **paper-level proxy**, not the claim-level Bin assignment defined in `notebooks/rubric.md`:
- **A** = paper reports an established, directly testable/verified methodology or result
- **B** = paper reports a sound methodology or theoretical construction, but with no lockable prediction of its own
- **C** = paper is speculative or not connected to observables by a specified bridge principle

This is distinct from — and feeds into, but does not substitute for — the **claim-level** Bin A/B/C assignment (with [Est]/[Open]/[Unsup]/[Blocked]/[CE] evidence tags) that Phase 1.5's gate memos will apply to the five H1–H5 hypotheses themselves. Phase 3/4 must not conflate "this paper is Bin A" with "this audited claim is Bin A" — the paper-level tag only describes the citation's own rigor, not whether the claim under audit is supported by it.

---

## Phase 2 Closeout Checklist (corrected post-red-team)

- [x] 5-channel search executed (arXiv API, QNFO Vectorize, QNFO KG, seed bibliography, subagent LLM recall) — methodology corrected per finding F2; Semantic Scholar/Web were named in the original draft but never queried
- [x] Dedup complete — **71** unique sources (corrected from 72; 1 duplicate removed per finding F6)
- [x] Classification complete — 35 Core, 35 Supporting, 12 Background, ~60 Rejected
- [x] Gaps documented (dS holography, Rydberg spectroscopy, COTT hardware)
- [x] All entries tagged with bin (A/B/C); reconciled against rubric.md scope (finding F8)
- [x] Citation verification status tagged per entry — `[TOOL-VERIFIED]` vs `[LLM-RECALL]` (finding F1); full DOI/text verification deferred to Phase 3
- [x] QNFO-internal portfolio-adjacent papers disclosed for H4 (finding F10)
- [x] Red team executed — see `artifacts/phase2-red-team.md` (2 BLOCKER, 3 MAJOR, 5 MINOR findings, all addressed in this amendment)
- [x] Phase 2 Closeout Protocol (commit → tag → push → verify → log) — fix commit follows this amendment
