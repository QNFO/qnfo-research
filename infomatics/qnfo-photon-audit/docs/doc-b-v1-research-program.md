---
modified: 2026-07-18T13:53:31Z
---
# A Falsifiability-First Research Program on Photonic Substrate Hypotheses for Emergent Spacetime

## Abstract

A recurring informal claim — that photons, as bosons exempt from Pauli exclusion, constitute a pre-geometric information substrate more fundamental than 3D space, with electrons as "knotted" or self-trapped photonic configurations — draws vocabulary from several genuine, active research programs: classical electromagnetic knot solitons (Rañada, Trueba, Bouwmeester), spinning-soliton models of the electron (Kerr–Newman solitons, Mie–Born–Infeld nonlinear electrodynamics), holographic emergence of geometry from entanglement (Ryu–Takayanagi and tensor-network reconstructions), and adelic/p-adic approaches to quantum field theory. However, in its informally circulated form the claim substitutes analogy for derivation at exactly the three junctures where these literatures diverge from popular retellings: (1) recovering fermionic spin-1/2 statistics from a spin-1 bosonic field configuration, (2) deriving — rather than asserting — the emergence of a Pauli-exclusion-shaped 3D metric from an entanglement or informational substrate, and (3) using p-adic/adelic structures for a specific, checkable calculation rather than as vocabulary. This program proposes a bounded, six-month, LLM-orchestrated literature synthesis and calculation-replication project. Its output is not a new physical theory but a structured technical audit: for each of the three junctures, either (a) a citation to existing peer-reviewed work that closes the gap, (b) a demonstration that the gap is a known open problem, with the state of the art quantified, or (c) a derivation showing the specific claim as stated is inconsistent with established results. The deliverable is a technical report suitable for a physics-literate but non-specialist audience, with all quantitative claims traceable to primary sources or original, checked calculation.

---

## Research Thesis

**Thesis statement:** The claim "photons are pre-geometrically prior to 3D space, and electrons are photonic knots, therefore the primacy of 3D space is falsified" is not evaluable as stated because it conflates three logically independent and unequally supported sub-claims. This program's thesis is that disaggregating the claim into its sub-claims, and testing each against the existing peer-reviewed literature, will show a consistent pattern: the _representational_ claims (electrons can be modeled as topological EM solitons; geometry can be derived from entanglement structure in certain toy models) have real, citable support with explicit domains of validity; the _ontological_ claims (photons are literally more fundamental than space; 3D space is "falsified") are not supported by, and in some cases are not well-posed within, the cited formalisms. The value of the program is in producing a defensible map of exactly where rigorous science ends and rhetorical extrapolation begins — which is generally more useful than either fully endorsing or fully dismissing a synthetic claim of this kind.

**Sub-hypotheses to be tested:**

- **H1 (soliton–spin):** Existing classical/semiclassical EM-knot and spinning-soliton models (Rañada–Trueba Hopf-fibration knots; Kerr–Newman spinning solitons; Mie–Born–Infeld nonlinear electrodynamics) reproduce the electron's charge quantization and magnetic moment in some regime, but do _not_ independently derive spin-1/2 (double-cover/SU(2)) statistics from a spin-1 bosonic starting point without additional postulated structure. Test: locate and evaluate the specific derivations claiming to close this gap (e.g., Burinskii's Kerr-Newman soliton spin quantization via Wilson loop) and determine what is assumed versus derived.
- **H2 (entanglement–geometry):** Holographic constructions (Ryu–Takayanagi, tensor-network/MERA models) do derive an emergent metric-like structure (area law, minimal surfaces) from entanglement entropy, but only within specific settings (AdS/CFT boundary theories, or engineered toy lattice models) — not for our universe's actual (non-AdS, non-conformal) spacetime, and not from photon statistics specifically. Test: characterize precisely which emergence claims are established (with citation) versus aspirational, and whether "Pauli exclusion → space" is a claim anyone has actually derived versus asserted by analogy.
- **H3 (adelic relevance):** p-adic/adelic quantum mechanics and string theory (Volovich program) provide a well-defined, checkable formalism, but its application in the original document is nominal (names invoked, no formula used). Test: attempt one small original calculation (e.g., a p-adic propagator or local zeta function relevant to a toy photon/electron model) to determine whether the adelic framework says anything nontrivial about photon/electron structure, or whether it is orthogonal to the claim.
- **H4 (falsification claim):** "The primacy of 3D space is falsified" is a strong empirical/logical claim. Test: determine whether any result in H1–H3 constitutes a falsification in the Popperian sense (a prediction that contradicts observation) as opposed to a reinterpretation or alternative formalism consistent with existing observations. Expectation, to be confirmed or overturned: no falsification exists; at best, alternative formalisms are mathematically legitimate but observationally equivalent to standard QFT-in-3+1D at current experimental precision.

---

## Work Breakdown Structure (WBS)

**Orchestration model:** An LLM (or LLM team) acts as literature synthesizer, citation-checker, and calculation scaffolder under human supervision. All numerical/symbolic derivations are re-run independently (not merely LLM-asserted) using a CAS (e.g., SymPy) where feasible, and flagged as "LLM-derived, human-unverified" until checked.

### Phase 0 — Scoping and Claim Decomposition (Week 1)

- 0.1 Formalize H1–H4 as individually falsifiable statements with explicit success/failure criteria.
- 0.2 Build an annotated bibliography seed set (≥40 primary sources) across the four sub-literatures.
- 0.3 Define the audit rubric: for every claim in the final report, tag as [Established/cited], [Open problem/cited], or [Unsupported/original reasoning].
- _Deliverable:_ Scoping memo + rubric.

### Phase 1 — Literature Synthesis per Sub-Hypothesis (Weeks 2–6)

- 1.1 **H1 track:** Systematic review of EM-knot solitons (Rañada, Trueba, Bouwmeester, Arrayás), spinning-soliton electron models (Burinskii Kerr–Newman, Chernitskii Mie–Born–Infeld), and the general spin-statistics theorem's constraints on any classical-field-only account of spin-1/2.
- 1.2 **H2 track:** Review of RT-formula derivations, tensor-network/MERA holographic models, causal set theory, and explicit statements (from primary sources) about domain of applicability (AdS boundary CFTs, not de Sitter/flat space without extension).
- 1.3 **H3 track:** Review of the adelic/p-adic QM and string theory literature (Volovich, Vladimirov, Freund–Olson) sufficient to identify one candidate calculation.
- 1.4 **H4 track:** Review of what would constitute an actual empirical falsification of 3+1D spacetime primacy (e.g., Lorentz-violation bounds, tests of exclusion-principle violations such as VIP/VIP-2 experiments) as a reality check against any "falsified" language.
- _Deliverable:_ Four literature synthesis memos, each with an [Established/Open/Unsupported] tag per claim and full citations.

### Phase 2 — Gap Analysis and Original Calculation (Weeks 5–8, overlapping)

- 2.1 For H1: reconstruct (symbolically) the Wilson-loop spin-quantization argument in the Kerr–Newman soliton literature; identify exactly which step, if any, derives (rather than assumes) half-integer spin.
- 2.2 For H2: reconstruct a minimal tensor-network toy model (e.g., HaPPY code) and verify the RT area-law relation numerically/symbolically in that toy model, to ground "emergent geometry" in something checked rather than cited-and-trusted.
- 2.3 For H3: attempt the identified p-adic calculation from 1.3; report result whether or not it supports the informal claim.
- _Deliverable:_ Worked calculation notebooks (checked), each with a plain-language summary of what was and wasn't shown.

### Phase 3 — Synthesis and Audit Report (Weeks 8–10)

- 3.1 Cross-reference H1–H3 outcomes against H4's falsification criteria.
- 3.2 Draft the technical report: claim-by-claim verdict table, full citation list, and an explicit "what would need to be true for the original claim to hold" section.
- 3.3 Independent human review pass (adversarial read specifically hunting for LLM-hallucinated citations or unchecked derivation steps).
- _Deliverable:_ Draft report v1.

### Phase 4 — External Sanity Check and Finalization (Weeks 10–12)

- 4.1 Circulate draft to at least one subject-matter reader per sub-literature (soliton physics, holography, p-adic physics) if accessible; otherwise run a structured self-critique pass explicitly checking each derivation against textbook results (spin-statistics theorem, standard RT formula statement).
- 4.2 Revise; finalize verdict table.
- 4.3 Publish as a technical report / preprint-style document with full reproducibility (calculation notebooks attached).
- _Deliverable:_ Final report.

### Cross-cutting

- **Citation integrity control:** every citation used in the final report must trace to a real, checkable source (DOI/arXiv ID); any LLM-suggested citation is verified against the actual source text before inclusion, given known LLM citation-fabrication risk.
- **Verdict transparency:** the final table explicitly separates "the metaphor is evocative" from "the physics is established," since this is where the original informal document failed.

---

## Expected Outcome

The most likely result, based on the literature surveyed above, is that H1 and H2 will each resolve to "the representational/toy-model version is established; the strong ontological claim is not," H3 will resolve to "adelic structures are a legitimate but currently unconnected formalism," and H4 will resolve to "no falsification of 3D-space primacy currently exists in the peer-reviewed literature." That itself is a useful, honest deliverable — it tells you precisely which parts of the original synthetic essay are worth pursuing further (the soliton-electron and holographic-geometry literatures are real and interesting) and which parts were rhetorical overreach dressed in real vocabulary.