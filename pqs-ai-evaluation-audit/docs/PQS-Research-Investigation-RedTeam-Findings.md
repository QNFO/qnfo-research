---
title: "Red-Team Findings: PQS Research Investigation"
created: 2026-07-24
tags: [red-team, PQS, research-investigation, audit]
---

# Red-Team Findings: PQS Research Investigation

Audit target: `PQS-Research-Investigation.md` (written 2026-07-24)
Method: Direct re-verification of claims via independent API queries (Zenodo, arXiv) in this session — not simply re-reading the document.

---

## Finding 1 — DOI Precision Error

**Severity: MINOR**

**Claim in document:** "DOI: 10.5281/zenodo.17184229" (cited under Sub-Pillar 1 and in the Broader Research Program table)

**Verification:** Querying `https://zenodo.org/api/records/17184229` returns a record whose actual resolvable DOI is `10.5281/zenodo.17184230`. The number `17184229` is the **conceptrecid** (the stable concept-level identifier that stays constant across versions), not the version-specific DOI that actually resolves.

**Fix:** Cite `10.5281/zenodo.17184230` as the version DOI, or explicitly label `17184229` as "concept DOI" if referring to the paper generically across versions. This distinction matters for anyone trying to verify the citation independently.

---

## Finding 2 — Unverifiable Internal Citation Passed Through Without Flagging

**Severity: MODERATE**

**Claim in document:** "Integrates Stergios Pellis's dimensionless theory with temporal quantization via fractal geometry" (quoted directly from the PQS abstract, Sub-Pillar 2)

**Verification attempted:**
- Zenodo search for "Stergios Pellis dimensionless" → 5 hits, **none relevant**. Top hits are unrelated botany taxonomy papers (a different "Stergios B." who catalogs Andean *Pilea* plant species) and an unrelated Portuguese-language physics paper.
- arXiv search for "Stergios Pellis" → 1 hit: "Fractal Schrödinger Equation: Implications for Fractal Sets" — **plausible partial match** (fractal + Schrödinger is thematically adjacent to "fractal geometry" and "temporal quantization"), but I could not confirm this is the same "Stergios Pellis" or that it constitutes a "dimensionless theory" as characterized in the PQS abstract.

**Issue:** The original document passed this named citation through in the "Source Claims" section without independently verifying it exists as a citable, discoverable prior work. This is exactly the kind of unverified specific-sounding attribution that should be flagged rather than silently repeated. A reader could reasonably assume "Stergios Pellis's dimensionless theory" is an established, findable body of work; the honest state is: **partially traceable to one arXiv preprint, unconfirmed identity match, no confirmed connection to "dimensionless theory" as a named framework.**

**Fix:** Add `[UNVERIFIED: could not independently confirm "Stergios Pellis's dimensionless theory" as a distinct citable work beyond one thematically-adjacent arXiv preprint of uncertain authorship match]` to the document.

---

## Finding 3 — Material Omission: Bell Test Falsification Context

**Severity: BLOCKING (for a document claiming to be free of editorial bias in either direction)**

**Issue:** The document's "External Literature — Notable Convergence Points" section lists four ways external literature "aligns with PQS claims" but the parallel "Where External Literature Contradicts PQS Claims" section is **absent**. The only contradicting evidence appears as a single soft line: "This is an active research area, not a closed question" (Sub-Pillar 1).

**Verification:** A live arXiv search for "loophole-free Bell" returns substantial literature (5+ papers on the first page alone: randomly-chosen measurement settings, homodyne detection, precertification methods, single-atom tests) confirming this is a large, well-established experimental literature — the same literature that includes Hensen et al. (2015), Giustina et al. (2015), Shalm et al. (2015), and underlies the 2022 Nobel Prize in Physics (Aspect, Clauser, Zeilinger), all of which were extensively documented in the **source conversation files** (`_26205145852.md`, `_26205150012.md`) that this investigation is built from.

**Problem:** The new investigation document silently drops this counter-evidence that was present and well-articulated in the original source material. A "neutral investigation, no editorializing" framing requires presenting BOTH the measurement-independence-loophole literature (which is genuinely supportive of local-deterministic-model possibility under specific technical conditions) AND the loophole-free experimental literature (which specifically targets and closes the most common such loopholes). Omitting the latter is a one-sided edit, even if unintentional — it shifts the document from "neutral" toward "credulous."

**Fix:** Add a "Where External Literature Constrains PQS Claims" subsection presenting the loophole-free Bell test literature (Hensen 2015, Giustina 2015, Shalm 2015, 2022 Nobel Prize) alongside the measurement-independence-loophole literature, and note the actual scientific relationship between them: the measurement-independence loophole is a specific, narrow technical gap that remains technically open in the literature, but the loophole-free experiments were specifically designed to close the two most operationally accessible loopholes (locality, detection) — they do not close the measurement-independence loophole, which requires assuming free choice of measurement settings is itself constrained. This is a real, nuanced, unresolved technical point — not evidence either strongly for or against PQS, but it must be presented completely.

---

## Finding 4 — Overstated Relationship Language ("Directly Parallel" / "Directly Relevant")

**Severity: MODERATE**

**Claims in document:**
- "Directly relevant — Hall shows that <1/15 bit of prior correlation... suffices for a local deterministic model" (Sub-Pillar 1)
- "**Directly parallel to PQS's dimensionless physics claim.**" (Volovik, Sub-Pillar 2, bolded in original)
- "**Directly relevant — provides quantum mechanical model based on golden ratio geometry.**" (Pashaev, Sub-Pillar 3, bolded in original)
- "**directly relevant to thermodynamic management in superconducting circuits**" (Aamir/Gasparinetti, Sub-Pillar 4, bolded in original)

**Issue:** These four claims are bolded for emphasis in the original document, which itself functions as an editorial signal even without discursive commentary — bolding IS a form of editorializing. More substantively:
- Hall's measurement-independence loophole is a formal, narrow result about the mathematical conditions under which SOME local deterministic models can reproduce singlet correlations. It does NOT establish that the universe IS local/deterministic (PQS's actual claim) — it establishes only that this is not mathematically excluded under a specific, itself-debated relaxation of an assumption (measurement independence). Calling this "directly relevant" without qualifying that it addresses a narrow mathematical possibility, not an empirical demonstration, risks the reader over-crediting the connection.
- Volovik's dimensionless-physics program derives dimensionless quantities from a SPECIFIC mechanism (emergent gravity, metric dimension 1/[L]²). PQS's dimensionless physics derives them from a DIFFERENT and unspecified mechanism ("deeper causal network of wave correlations," Stergios Pellis's unverified theory, "temporal quantization via fractal geometry"). Sharing the word "dimensionless" and the general conclusion (constants aren't fundamental) is a **structural** parallel, not a **mechanistic** one. Calling it "directly parallel" conflates these.
- Similarly for Pashaev's golden oscillator (Sub-Pillar 3) — it is a genuine φ-based quantum oscillator, but it does not address 720° spinor rotation, non-orientable manifolds, or "generative aperiodicity" as PQS specifically claims. It shares the golden ratio + quantum mechanics theme, not the specific mechanism.

**Fix:** Replace "directly relevant"/"directly parallel" with more precise language distinguishing **thematic overlap** (shares vocabulary/goals) from **mechanistic overlap** (shares the actual causal/mathematical mechanism). E.g.: "Thematically adjacent — shares the goal of deriving dimensionless constants from a deeper structure, though the specific mechanism (emergent metric dimension vs. wave-correlation network) differs and is not shown to be equivalent."

---

## Finding 5 — Numerical Claims Not Independently Verified in This Session

**Severity: MODERATE**

**Claim in document (Sub-Pillar 4, "Supporting Numerical Analysis"):** Aluminum gap 180 μeV → 43.5 GHz → 86-87 GHz; k_BT at 4K ≈ 83 GHz; Nb ~700 GHz; NbN ~1.2 THz.

**Issue:** These figures are explicitly labeled "(from AI conversation verification)" in the document, which is honest sourcing — but the document's own framing elsewhere implies these numbers are established facts supporting the 4K qubit thermodynamic argument. In truth:
- These specific numbers were computed/verified by a DIFFERENT AI system (Claude, in the source conversation `_26205145852.md`) using its own internal calculation, not retrieved from a citable published source with a DOI.
- I did not independently re-derive or verify k_BT(4K) = 83 GHz, or the aluminum 2Δ = 86-87 GHz figure, in THIS session using a primary source.
- The BCS relation Δ ≈ 1.76 k_BT_c is a real, textbook relation, but applying it to get "Nb ~700 GHz" and "NbN ~1.2 THz" was not re-verified against a specific measured T_c value with a citation in this investigation.

**Fix:** Either (a) independently re-derive these numbers from k_B = 8.617×10⁻⁵ eV/K and published T_c values with citations, or (b) explicitly relabel the entire subsection `[CARRIED OVER, UNVERIFIED IN THIS SESSION: figures originate from a separate AI system's calculation in a prior conversation, not independently re-derived here]`.

---

## Finding 6 — Conflation of "Related Literature Exists" with "Claim Is Validated"

**Severity: MODERATE (systemic, cuts across all 4 sub-pillars)**

**Issue:** The document's structure (Source Claims → External Literature Context → "Notable" convergence paragraph) creates an implicit narrative arc of claim → supporting evidence, even where the external literature is adjacent-but-distinct rather than confirmatory. This is a structural/framing issue rather than a single quotable claim: by placing external literature immediately after each specific PQS claim and describing it as "context," the document invites the reader to read the juxtaposition as support, regardless of the hedging language used.

**Fix:** Consider restructuring so that for each sub-pillar, there is an explicit, separate line stating what the external literature does NOT establish (e.g., "This literature does not confirm that PQS's specific mechanism — X — is correct; it establishes only that Y is a live, unresolved question in an adjacent area.").

---

## Finding 7 — SSRN Abstract Quotes: Verification Status

**Severity: MINOR — CLEARS with caveat**

**Check:** Are the SSRN abstract quotes in the document exact or paraphrased?

**Verification:** Cross-checked the document's quoted text for all 4 papers against the live SSRN page text captured in this session (via browser `Runtime.evaluate` on papers.ssrn.com). All four core-thesis abstracts in the document **match the live SSRN abstract text closely** (Post-Quantum Synthesis, Dimensionless Physics, Generative Spiral, Thermodynamic Imperative) — this is a genuine strength of the current document; the abstracts were not paraphrased loosely or embellished.

**Minor issue:** The document's bullet-point "Core Thesis" summaries are compressions/rewordings of the full-paragraph abstracts, not verbatim quotes, though they preserve the substantive claims accurately on inspection. This is standard practice but should be labeled as "paraphrased from abstract" rather than implied to be exact quotes.

---

## Finding 8 — Zenodo File Listing Claim (PDF/MD sizes)

**Severity: MINOR — CLEARS**

**Check:** Document states PQS paper has "Files: Post-Quantum Synthesis.pdf (776900 bytes), Post-Quantum Synthesis.md (135254 bytes)".

**Verification:** Re-queried in this session against `zenodo.org/api/records/17184229` (resolving to 17184230) — file listing **independently reconfirmed**, same byte counts returned. This claim is accurate and was genuinely verified via a live API call, not fabricated.

---

## Summary Table

| # | Finding | Severity | Status |
|---|---------|----------|--------|
| 1 | DOI precision (concept vs. version DOI) | MINOR | Needs fix |
| 2 | Unverifiable "Stergios Pellis" citation passed through | MODERATE | Needs flag |
| 3 | Bell-test falsification literature omitted | **BLOCKING** | Needs new section |
| 4 | Overstated "directly parallel/relevant" language + bolding | MODERATE | Needs rewording |
| 5 | 4K qubit numbers not independently re-verified this session | MODERATE | Needs relabel |
| 6 | Structural conflation of "adjacent" with "supportive" | MODERATE | Needs restructure |
| 7 | SSRN abstract quotes | MINOR | Clears (accurate) |
| 8 | Zenodo file listing | MINOR | Clears (accurate) |

**Net assessment:** The document is NOT fabricated — all citations trace to real, independently-verifiable external papers, and the core SSRN/Zenodo source material is accurately represented. However, it has a **credulity skew**: supportive-sounding adjacent literature is emphasized and bolded, while directly falsifying/constraining literature (loophole-free Bell tests) that was present in the ORIGINAL source conversations is silently dropped from this new synthesis. This is the single most important fix required (Finding 3) to make the document genuinely neutral rather than selectively neutral.
