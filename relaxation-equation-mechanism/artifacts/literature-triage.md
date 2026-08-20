# Literature Search & Triage — QNFO.RES.018 Phase 2

**Date:** 2026-08-19 · **Method:** 8-source search (OpenAlex, Crossref, arXiv, Europe PMC, Zenodo/QNFO corpus, web via API) with evidence discipline; every response saved to artifacts/external-search/.

---

## 1. Search inventory (evidence files)

| # | Source | Query | Evidence file |
|:--|:-------|:------|:--------------|
| 1 | OpenAlex | Valentini relaxation to quantum equilibrium subquantum H-theorem | openalex-valentini-relaxation.json |
| 2 | OpenAlex | deterministic hidden variable model Born rule probabilities | openalex-deterministic-born.json |
| 3 | OpenAlex | 't Hooft cellular automaton interpretation quantum mechanics deterministic | openalex-thooft-cellular.json |
| 4 | arXiv | au:Valentini AND abs:quantum equilibrium | arxiv-valentini-equilibrium.xml |
| 5 | arXiv | ti:dynamical origin of quantum probabilities | arxiv-dynamical-origin-probabilities.xml |
| 6 | Crossref | Valentini signal-locality subquantum H-theorem 1991 | crossref-valentini1991.json |
| 7 | Crossref | GRW 1986 unified dynamics | crossref-grw1986.json |
| 8 | Crossref | Pearle CSL 1989 | crossref-csl1989.json |
| 9 | Europe PMC | relaxation quantum equilibrium Born rule | europepmc-quantum-equilibrium.json |
| 10 | arXiv | quantum state diffusion Gisin | arxiv-gisin-qsd.xml |
| 11–15 | QNFO corpus | 4 internal formulations (relaxation-equilibrium, quantum-equilibrium-Bohmian, GRW-CSL, Valentini-subquantum) + P1 evidence (Reddiger full texts, HSH chain, Bassi–Ghirardi, Wu 2013) | P1 files + this phase |

## 2. Counterexample search (novelty-claim guard — MANDATORY per P1b gate)

**Result: the generic claim "a deterministic relaxation mechanism produces Born statistics" is NOT novel.** The following peer-reviewed programs exist:

| Program | Anchor | Relationship to CC-1 |
|:--------|:-------|:---------------------|
| **Valentini subquantum H-theorem** | 10.1016/0375-9601(91)90116-p (1991 I) · 10.1016/0375-9601(91)90330-b (1991 II) | Relaxation to quantum equilibrium under de Broglie–Bohm dynamics — **the canonical prior program** |
| **Valentini & Westman** dynamical origin | arXiv 1007.3842 (Proc. R. Soc. A 2005) | Explicit relaxation simulation producing Born rule from non-equilibrium |
| **Towler, Russell & Valentini** | 10.1098/rspa.2011.0598 (Proc. R. Soc. A 2012) | Time scales for dynamical relaxation to the Born rule |
| **Colin & Struyve** | 10.1088/1367-2630/12/4/043008 (NJP 2010) | Relaxation to equilibrium for a class of dBB-type theories |
| **Nelson stochastic dynamics relaxation** | 10.1007/s10701-023-00730-w (Found. Phys. 2023) | "Relaxation to Quantum Equilibrium and the Born Rule in Nelson's Stochastic Dynamics" — **nearest competitor title** |
| **Deterministic chaos + decoherence Born rule** | 10.3390/e23111371 (Entropy 2021) | Born rule via deterministic chaos + decoherence in dBB |
| **Aerts hidden-measurement solution** | 10.1016/j.aop.2014.09.020 (Ann. Phys. 2014) | Deterministic hidden-measurement resolution of the measurement problem |
| **'t Hooft deterministic program** | 10.3389/fphy.2020.00253 (Front. Phys. 2020) | Deterministic quantum mechanics (cellular automaton interpretation) |
| **GRW/CSL stochastic collapse** | 10.1103/physrevd.34.470 (1986) · 10.1007/bf00692673 (1989) · Bassi–Ghirardi 2003 | Stochastic (not deterministic) relaxation — constraint family |
| **Wiseman quantum state effusion** | arXiv 1609.06572 | Quantum state effusion — stochastic unraveling family (P3 correction: not Gisin–Percival QSD) |

**Scoping conclusion (drives the paper's novelty claim):** CC-1's claim is NOT "relaxation produces Born statistics" generically. It is the specific conjunction: (a) **measurement-triggered** (not cosmological/early-universe relaxation), (b) in the **Madelung / Reddiger Radon–Nikodym-Kolmogorovian formalism** (not Bohmian configuration space, not Nelson stochastic, not hidden-measurement algebra), (c) **basins-of-attraction toward eigenstates** during the measurement interaction, (d) **consistent with Wu et al. 2013 strong-field reproductions**. None of the found programs occupies this exact cell; all must be cited and distinguished in the paper. **If Phase 4 finds a program in that exact cell, CC-1 is downgraded to a replication-with-constraint exercise — the disconfirmation condition absorbs this.**

## 3. Classification matrix

| Class | Item | Action |
|:------|:-----|:-------|
| **CORE** (directly addresses CC-1) | Reddiger 2017/2026 full texts (P1); Valentini 1991 I+II; Towler–Russell–Valentini 2010; Nelson-relaxation 2023 | Deep read; extract mechanism + assumptions |
| **CORE** (constraint set) | Bassi–Ghirardi 2003; GRW 1986; CSL 1989; Gisin–Percival QSD | Constraint table: parameter regimes, experimental bounds |
| **CORE** (consistency anchor) | Wu et al. 2013; Hacohen-Gourgy & Martin 2020 | Empirical anchors for the dynamics family |
| **SUPPORTING** | Valentini & Westman 2005; Entropy 2021; Aerts 2014; 't Hooft 2020; 1409.7467 (hidden variables + early universe); 1310.1899 (signal-locality + subquantum info) | Abstract + methods; distinctions in paper |
| **BACKGROUND** | HSH concept chain (17721007); PQS; pqs-critique-adjudication; e27040399 (dBB completeness 2025) | Corpus anchors; recent dBB status review |
| **REJECT** | EuropePMC noise (fluxonium spectroscopy, molecular motors, Mpemba) | Archived with reason (topic mismatch) |

## 4. Mandatory Symmetry Template (KIF-18, HARD)

### Where External Literature Supports [the core claim that the RN/Madelung formalism lacks a measurement-triggered relaxation dynamics]

1. **Reddiger 2026** (full text, P1 evidence): "the dynamics is borrowed from quantum mechanics and the basic quantities are rigorously defined in the context of said dynamics"; "The projection postulate and the question of measurement are addressed via conditional probabilities in Part III" — the formalism is kinematical; no relaxation mechanism is provided. **Supports the premise that the gap is unconstructed.**
2. **Reddiger & Poirier 2023** (full text, P1 evidence): the Madelung equations are dynamical PDEs, but the paper addresses well-posedness, Wallstrom, and Takabayasi's quantization condition — **no measurement-relaxation mechanism**. **Supports the premise.**
3. **Bassi–Ghirardi 2003** (verified): dynamical reduction models are **stochastic**; no deterministic relaxation-to-eigenstates mechanism exists in that program. **Supports the premise (deterministic variant absent).**
4. **Wu et al. 2013** (verified): Bohmian trajectories quantitatively reproduce HHG spectra — trajectory-level determinism within unitary dynamics is empirically anchored. **Supports the consistency requirement of CC-1.**

### Where External Literature Constrains or Contradicts [the core claim / its novelty]

1. **Valentini 1991 I+II; Valentini & Westman 2005; Towler–Russell–Valentini 2010:** a deterministic relaxation mechanism (subquantum H-theorem) producing Born statistics as equilibrium **already exists** for de Broglie–Bohm-type theories. **CONSTRAINS:** CC-1's novelty claim must be scoped to the measurement-triggered RN/Madelung-basins formulation, NOT to "relaxation produces Born statistics" generically.
2. **Found. Phys. 2023 (10.1007/s10701-023-00730-w):** "Relaxation to Quantum Equilibrium and the Born Rule in Nelson's Stochastic Dynamics" — relaxation to equilibrium + Born rule **already demonstrated in Nelson's stochastic dynamics** (closely adjacent formalism family). **CONSTRAINS:** the paper must explicitly distinguish the Madelung/RN basins-of-attraction formulation from Nelson-stochastic relaxation; otherwise CC-1 risks being a re-derivation.
3. **Entropy 2021 (10.3390/e23111371):** Born's rule justified via deterministic chaos + decoherence in dBB — **CONSTRAINS** any claim that deterministic origins of the Born rule are unavailable.
4. **Aerts 2014 (10.1016/j.aop.2014.09.020):** hidden-measurement deterministic solution to the measurement problem — **CONSTRAINS** any claim that no deterministic resolution exists; the hidden-measurement algebra is a distinct mechanism family that must be cited.
5. **'t Hooft 2020 (10.3389/fphy.2020.00253):** deterministic quantum mechanics program — **CONSTRAINS** the "deterministic re-grounding is impossible" reading; the project tests one specific family, not the entire deterministic program.
6. **GRW 1986 / CSL 1989 / Gisin–Percival QSD:** the stochastic collapse family already supplies measurement dynamics with experimental bounds — **CONSTRAINS** the paper's positioning: CC-1's deterministic variant must explain why the stochastic family's bounds do not apply, or the comparison table must carry them.

**[NO CONSTRAINING EVIDENCE FOUND]** is **NOT** asserted anywhere in this triage — every premise of CC-1 has a named constraining or distinguishing reference. The symmetry template is fully loaded on both sides.

## 5. Gap analysis (updated)

- **Novelty:** now explicitly scoped (Section 2) — CC-1 occupies the specific cell (measurement-triggered, Madelung/RN formalism, basins-of-attraction, Wu-2013-consistent) that the found literature does not fill. **Phase 4 must verify no program in that exact cell exists before the pre-registration seal.**
- **Corpus gap:** no internal record covers Valentini/quantum-equilibrium/GRW-CSL mechanisms — the counterexample literature is external-only (confirmed by 4-formulation corpus sweep).
- **Evidence discipline:** every DOI in this triage has a saved evidence file; counts traceable.
