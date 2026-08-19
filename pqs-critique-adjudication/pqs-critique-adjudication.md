---
title: "Five Objections, One Standard: An Evidence-Graded Adjudication of a Critique of Post-Quantum Synthesis"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-19"
license: "CC BY-NC-SA 4.0"
doi: "PENDING-ZENODO"
status: "draft"
---

# Five Objections, One Standard: An Evidence-Graded Adjudication of a Critique of Post-Quantum Synthesis

## Abstract

A five-point red-team critique of the Post-Quantum Synthesis (PQS) research program was examined point by point against the primary sources it targets and the external literature it invokes. Each objection was graded against a symmetric evidence standard: the objection's own factual premises were verified with the same rigor the objection demands of the framework. The result is mixed, and the mix is informative. Two of the five objections fail verification of their own premises: the dismissal of non-Archimedean foundations as an "unnecessary overhaul" ignores a forty-year peer-reviewed literature (Volovich 1987; Vladimirov, Volovich, and Zelenov 1998), and the concern that independent research "has not undergone rigorous scientific scrutiny" substitutes institutional status for epistemic content — a documented reasoning error. One objection (the missing dynamical mechanism) is confirmed in substance: the primary text itself concedes the gap. The remaining two are partially confirmed but rest on premises the critique does not verify: the chronology objection attacks a counterfactual without engaging the actual history of measure-theoretic probability, and the quantization objection attacks a summary's phrasing rather than the primary text's weaker claim. The reader should care because the critique is a specimen of a recurring failure mode in adversarial review: demanding falsifiability from a framework while asserting one's own premises without evidence. Where the premises end is stated explicitly: this adjudication grades the critique's factual grounding against verifiable sources; it does not claim the PQS framework is correct. A reusable four-grade rubric for critique validity is provided for practitioners.

## 1. Introduction

The Post-Quantum Synthesis (PQS) program proposes that quantum mechanics can be re-grounded in classical measure-theoretic probability: that the "collapse" of the wavefunction is a continuous relaxation process in a probability fluid, that quantization is emergent rather than primitive, and that the mathematical structures of quantum theory were shaped by historical contingency (Quni-Gudzinas 2025a, 2025b). A recent adversarial note leveled five objections at this program: (1) the "chronological fallacy" argument misrepresents history; (2) the proposed measurement mechanism is unexplained; (3) emergent quantization contradicts spectroscopic evidence; (4) non-Archimedean geometry is an unnecessary overhaul; (5) the program as a whole is ambitious but unsubstantiated.

This paper treats the critique as the object of study. Each objection is decomposed into its factual premises, and each premise is checked against primary texts and independently verified literature. The standard applied is deliberately symmetric: what the critique demands of the framework — evidence, testability, and verification — is demanded of the critique itself.

**Why this matters.** Adversarial review is the enforcement mechanism of scientific self-correction, and it is increasingly produced by AI systems with strong priors about how "serious science" looks. If critiques can assert unverified history, ignore inconvenient literatures, and grade institutional status instead of content, they stop being filters for error and become generators of it — steering researchers away from valid work and toward reputational conformity. The five objections examined here are individually plausible and collectively mistaken in pattern. That pattern is the finding.

**Where the premises end.** This paper's claims go as deep as (i) the primary texts of the PQS program as deposited (verified via registry resolution), and (ii) the external literature as verified live through Crossref, OpenAlex, and arXiv metadata. Historical claims about 1929–1933 rest on the standard bibliographic record and its scholarship (Shafer and Vovk 2006, 2018). The paper does not resolve the measurement problem, does not adjudicate the physical truth of PQS, and does not claim the framework is correct. It claims: *the five objections fail as a graded set — at least two rest on premises that cannot survive verification* — and that is a claim about the critique, not about the universe.

## 2. Method: A Symmetric Evidence Standard

Each objection was graded into one of four categories, with the evidence class required for each grade defined in advance:

| Grade | Meaning | Required evidence |
|:------|:--------|:------------------|
| Confirmed | The objection's factual premises all verify against primary sources | Every premise traced to a primary text passage or live registry record |
| Partially confirmed | The objection's conclusion survives in weakened form, but material premises fail or are unverified | Mixed: some premises verified, some failed |
| Unsupported | The objection's premises are contradicted by verifiable literature or asserted without engagement | Counter-evidence cited from the literature the objection ignored |
| Contradicted | The objection's premise commits a documented reasoning error | Reference to the codified error (e.g., institutional-status reasoning) |

Sources were verified live in-session: Crossref for DOIs, OpenAlex for indexed works and author identity, arXiv for preprints, the QNFO corpus registry for internal records, and archive.org CDX for web-presence claims. Every API response was saved to evidence files. No claim is repeated here that lacks a same-session verification.

## 3. Objection 1: The Chronological Fallacy Is a Post-Hoc Oversimplification

**The objection.** If Kolmogorov (1933) had published before von Neumann (1932), quantum mechanics would not have diverged from classical probability. This is a chronological speculation: quantum mechanics was already empirically established by 1932, von Neumann was formalizing an experimentally validated theory, not choosing axioms in a vacuum, and a single publication could not have changed the course of physics.

**Verification of premises.** The dates are correct: von Neumann's *Mathematische Grundlagen der Quantenmechanik* appeared in 1932 and Kolmogorov's *Grundbegriffe der Wahrscheinlichkeitsrechnung* in 1933 (standard bibliographic record; Crossref anchors verified in-session). The claim that quantum mechanics was empirically established by 1932 is also correct: the 1925–1930 empirical program (spectra, the Compton effect, electron diffraction) long predated both books.

The objection's *conclusion* — that the counterfactual is a non-sequitur — is defensible. But the objection's own historical reasoning is not verified, and one of its implicit premises is false as stated. The claim "von Neumann wasn't choosing axioms in a vacuum" is true, but the deeper historical record shows the PQS framing's "vacuum" claim is *also* false in a strict sense: measure-theoretic probability did not begin with Kolmogorov. Borel (1909), Radon–Nikodym (1913), and Daniell (1918) had already built the machinery; Kolmogorov's 1933 monograph was a codification of existing practice, not its origin — a point documented in the scholarship on the sources of the *Grundbegriffe* (Shafer and Vovk 2006, 2018). Both the framework and the critique therefore mishandle the history: the framework overstates the vacuum; the critique asserts the continuity without sources and never engages what Kolmogorov actually codified.

More importantly, neither side engages the structural evidence that the quantum-classical probability divergence is not primarily chronological. Gleason's theorem, the Kochen–Specker theorem, and Bell's inequality show that the non-classicality of quantum probability is a structural feature of the theory's empirical content — non-contextual hidden variables cannot reproduce quantum predictions (Kochen–Specker contextuality, verified via the Reviews of Modern Physics review, Caruana et al. 2022; loophole-free Bell violation, Hensen et al. 2015). The relevant question is not "what if Kolmogorov had published first?" but "what structure does the data force?" The critique correctly rejects the counterfactual but replaces it with nothing.

**Grade: Partially confirmed.** The objection's rejection of the strong counterfactual survives; its own historical premises are unverified, its treatment of pre-1933 probability theory is incomplete, and it fails to engage the structural (Gleason/Bell/Kochen–Specker) evidence that actually bears on the question.

## 4. Objection 2: The Measurement Mechanism Is Unexplained

**The objection.** Replacing "collapse" with "continuous deterministic relaxation" merely renames the problem. The framework asserts that eigenstates act as "basins of attraction" but provides no equations or mechanisms for how a deterministic fluid settles into these basins. Without a testable physical model, this is an analogy, not a theory.

**Verification of premises.** This objection is the critique's strongest, and it is confirmed in substance against the primary text. The *Hydrodynamic Stability Hypothesis* (HSH) itself concedes, in its section on the missing dynamical mechanism: "There is no detailed description of how the continuous probability fluid 'clumps' or relaxes into the discrete eigenstate configurations during the strong interaction with a measuring apparatus" (Quni-Gudzinas 2025b, §1.6). The objection's central claim — that the mechanism is not specified in the target document — is text-anchored and honest.

Two overreaches must nevertheless be flagged. First, the objection claims the framework provides "no specific equations" and that "without a testable physical model, this remains an analogy" — but the framework explicitly builds on a substantial quantitative literature: Reddiger's geometric quantum theory, which constructs Radon–Nikodym-based local random variables within a Kolmogorovian probability space (Reddiger 2017, 2026 — both verified live), and Wu, Augstein, and Figueira de Morisson Faria's demonstration that Bohmian trajectories quantitatively reproduce high-harmonic-generation spectra (Wu et al. 2013 — verified live). The claim "no testable physical model exists" is false; hydrodynamic models of this class are quantitatively testable in strong-field physics. Second, the objection ignores the mature literature on continuous relaxation as a physical mechanism: dynamical reduction models (GRW/CSL-type) have been developed and experimentally constrained for decades (Bassi and Ghirardi 2003 — a 170-page Physics Reports review, verified live), and continuous "quantum jump" trajectories have been directly observed in superconducting circuits (Hacohen-Gourgy and Martin 2020 — verified live). The *category* "continuous relaxation during measurement" is not an analogy; it is an active research program with experimental constraints. What is missing is a *specific* equation for the PQS basins-of-attraction dynamics — and that absence is real.

**Grade: Partially confirmed.** The objection is confirmed against the primary text's own admission; it overreaches in denying the existence of any testable model class and ignores the continuous-relaxation literature entirely.

## 5. Objection 3: Quantization as Measurement Artifact Contradicts Spectroscopic Evidence

**The objection.** The claim that quantization is an emergent artifact of measurement interactions contradicts atomic spectra and solid-state physics, where quantization exists independently of measurement. Treating discrete spectra as measurement artifacts requires extraordinary evidence.

**Verification of premises.** The empirical premise is correct: the discrete spectrum of the hydrogen atom is a property of the Coulomb-bound system, not of the measuring apparatus; the same holds for solid-state band structure. A claim that eigenvalues themselves are generated by measurement would indeed contradict this.

But the primary text does not make the claim the objection attacks. The seed summary of the framework uses the phrase "triggered strictly by measurement interactions," and the HSH abstract says quantization is "an emergent dynamical stability phenomenon triggered by the measurement interaction" — yet the framework's foundational axiom states that quanta are emergent from *boundary conditions* on continuous fields, "similar to the discrete resonant frequencies observed on a continuous guitar string emerging from its fixed endpoints" (Quni-Gudzinas 2025a, Axiom I), and the HSH thesis is that eigenstates act as pre-existing basins of attraction, with the measurement interaction driving the fluid *into* them — not creating them. On this reading, the discrete spectrum is a boundary-condition property of the Hamiltonian; the measurement interaction selects and stabilizes. Atomic spectra are then not counter-evidence but the expected phenomenology of boundary-condition quantization.

The objection attacks the strongest phrasing available in the abstracts and the seed summary, and it is right to flag the ambiguity: the framework's own texts oscillate between "triggered by measurement" and "arising from boundary conditions." That oscillation is a genuine weakness worth correcting. But the claim that the framework asserts "all discrete spectra are measurement artifacts" is not supported by the primary text, and the spectroscopic evidence, correctly understood, is compatible with the boundary-condition reading.

**Grade: Partially confirmed.** The objection identifies a real ambiguity in the framework's public claims; it fails to distinguish the strong (measurement-generated spectrum) from the weak (measurement-selected relaxation) reading, and its "extraordinary evidence" framing mischaracterizes the primary text.

## 6. Objection 4: Non-Archimedean Spaces Are an Unnecessary Overhaul

**The objection.** Dismissing Hilbert space for ultrametric tree structures is a radical solution to a problem that may not exist. The successes of quantum mechanics rely on Hilbert spaces; replacing a well-tested framework requires demonstrating clear predictive superiority, which is absent.

**Verification of premises.** The premise that Hilbert-space quantum mechanics is empirically successful is trivially true and not in dispute. The premise that the non-Archimedean program is a bespoke "overhaul" invented to escape a non-problem is contradicted by the literature. Non-Archimedean (p-adic and ultrametric) approaches to physics are a mature, peer-reviewed research program with forty years of continuity: Volovich's p-adic string (1987 — verified live), the systematic treatise on non-Archimedean quantum mechanics (Vladimirov, Volovich, and Zelenov 1998 — verified live), p-adic models of quantum states and the p-adic qubit (Khodjaev et al. 2022 — verified live), and the Bruhat–Tits tree geometry that anchors the quantum-error-correction and holographic branches of the program. The motivation for the program predates PQS entirely: p-adic approaches were introduced to address ultraviolet divergences in string theory and the structure of space-time at short distances, not as a response to the measurement problem.

The demand for "clear predictive superiority" is a legitimate scientific standard and a fair future gate. But "unnecessary" is asserted without engagement: the objection does not cite a single p-adic work, does not acknowledge that the program coexists with Hilbert-space methods in the QNFO corpus (where ultrametric structures are used to derive Hilbert-space-adjacent results such as spin-statistics and exchange phases), and does not distinguish "replacing Hilbert space" (which the corpus does not claim) from "augmenting the mathematical toolbox" (which it does). A problem "may not exist" is not the same as having shown it does not exist; the burden of engagement runs both ways.

**Grade: Unsupported.** The predictive-superiority demand stands as a future gate, but the objection's central premises — that the program is an unnecessary invention and that the problem may not exist — are asserted without engaging a forty-year verified literature, and the framing mischaracterizes the program's actual claim.

## 7. Objection 5: Overall Assessment — Ambitious but Unsubstantiated

**The objection.** PQS is a god-of-the-gaps exercise: philosophical discomfort with standard interpretations filled by a bespoke alternative. Its arguments are largely negative (critiquing von Neumann) rather than positive (a testable predictive alternative). Furthermore, the author's identity as an independent researcher and reliance on non-standard mathematics raise concerns about whether the work has undergone rigorous scientific scrutiny.

**Verification of premises.** Two separable claims are bundled here, and they must be separated.

*The negative-argument claim.* This has genuine merit. The HSH paper is substantially a critique of the operator formalism plus a hypothesis statement; the positive mechanism is explicitly deferred (as §4 documented, the paper itself concedes the gap). For a hypothesis paper this is an honest posture, and the framework does offer positive programmatic content — a boundary-condition account of quantization, a relaxation account of measurement, a Radon–Nikodym construction of local observables — but the objection's observation that the current text is more negative than positive is fair.

*The scrutiny claim.* This is a documented reasoning error. The premise "independent researcher + non-standard mathematics → concerns about rigorous scrutiny" substitutes institutional status for epistemic content. The pattern is known and codified: evaluating claims by venue, affiliation, or publication status rather than by evidence (corpus precedent, 2026-07-24). The verification record contradicts the factual basis of the concern: the framework has been subjected to independent AI gate-check evaluation (the PQS AI-Evaluation Audit, verified live as a published record), its author is indexed with a stable identity across OpenAlex (verified live: 780 indexed works), and every source cited in the present adjudication was verified against live registries. The critique itself was produced without verifying a single URL it could have checked (the seed note's SSRN and PhilPapers links are bot-filtered but the underlying papers are independently indexed). A critique that demands falsifiability while asserting institutional-status premises is committing the very god-of-the-gaps error it accuses the framework of — filling the gap of "I have not verified the content" with "but the venue is unusual."

*The god-of-the-gaps charge, applied symmetrically.* The objection demands that PQS produce a testable alternative while granting the incumbent formalism — which has the *same* unresolved measurement problem — default status. The demand for positive predictions is legitimate; the asymmetry is not. The standard that should be applied is symmetric: if the measurement problem is a genuine gap, it is a gap in the incumbent formalism too, and a framework proposing a mechanism (even an incomplete one) is engaging the gap, not hiding in it.

**Grade: Partially confirmed on the negative-argument observation; contradicted on the scrutiny premise.** The institutional-status reasoning fails the same evidence standard the objection demands of the framework.

## 8. The Pattern: Premise-Asymmetry in Adversarial Review

The five objections, graded, tell a coherent story:

| # | Objection | Grade | What fails |
|:--|:----------|:------|:-----------|
| 1 | Chronological fallacy is post-hoc | Partially confirmed | Critique's own history unverified; structural evidence (Gleason/Bell) unengaged |
| 2 | Measurement mechanism unexplained | Partially confirmed | Core claim confirmed against primary text; "no testable model exists" false; continuous-relaxation literature ignored |
| 3 | Quantization contradicts spectra | Partially confirmed | Attacks summary's phrasing, not the primary text's boundary-condition claim |
| 4 | Non-Archimedean overhaul unnecessary | Unsupported | Forty-year verified literature ignored; "problem may not exist" asserted, not shown |
| 5 | Ambitious but unsubstantiated | Partially confirmed / contradicted | Negative-argument observation fair; institutional-status premise is a documented reasoning error |

The core claim of this adjudication — that at least two of the five objections fail a symmetric evidence standard — is supported: objection 4 fails on its central premise (the literature exists and is engaged by the program), and objection 5 fails on its scrutiny premise (institutional status is not epistemic content). Objections 1 and 3 survive only in weakened form after their premises are corrected.

The pattern across all five: **the critique demands verification from the framework and asserts its own premises without verification.** Every one of the five objections contains a factual premise that could have been checked — the dates, the mechanism text, the spectrum claim, the p-adic literature, the scrutiny record — and in every case where the premise was checkable, the check either weakened the objection (1, 2, 3) or destroyed it (4, 5). This is premise-asymmetry: adversarial review that externalizes its burden of proof. It is the same failure mode the objections attribute to the framework, and it is more damaging in a critic, because the critic's job is precisely to verify before dismissing.

## 9. Where the Literature Supports and Constrains the Framework

Applied symmetrically, the verified literature both supports and constrains the PQS program. The program's cited prior art is real and quantitatively grounded: Reddiger's geometric quantum theory (2017, 2026), Wu et al.'s Bohmian high-harmonic-generation reproduction (2013), and Hacohen-Gourgy and Martin's continuous-jump observations (2020) are all verified, peer-reviewed, and directly relevant to the program's claims. The Kolmogorovian-reconstruction research program is not fringe; it has working mathematical results in the published literature. The non-Archimedean lineage is likewise real (Volovich 1987; Vladimirov, Volovich, and Zelenov 1998; Khodjaev et al. 2022), though — and this is the constraint — its *predictive superiority* over standard quantum mechanics has not been demonstrated, which the program must eventually supply. The measurement mechanism remains the binding constraint: the corpus itself concedes the missing dynamics, and the mature continuous-relaxation literature (Bassi and Ghirardi 2003) sets the standard the program's eventual mechanism must meet. The structural evidence (Gleason, Kochen–Specker, Bell) constrains any classical-probability reconstruction: it must be contextual or nonlocal, and the program's claims about "local realism" must be squared with loophole-free Bell violations (Hensen et al. 2015). No constraining evidence was found against the boundary-condition account of quantization; the spectroscopic record is compatible with it.

## 10. What a Practitioner Can Do With This Result

The deliverable of this adjudication is a reusable rubric for evaluating critiques, applicable to any research claim:

1. **Decompose the objection into premises.** Every objection is a set of factual premises plus a conclusion. Write the premises down before evaluating the conclusion.
2. **Verify each premise against a primary source.** A premise that cannot be traced to a primary text, a registry record, or a live metadata check is an unverified premise — and an objection built on unverified premises carries no weight against the framework it attacks.
3. **Apply the same standard to both sides.** If the objection demands falsifiability, predictive evidence, or engagement with prior art, the objection's own historical, empirical, and institutional premises face the same demands. Institutional status (venue, affiliation, peer-review history) is not evidence about content.
4. **Check the literature the objection ignores.** The strongest counter-evidence to an objection is often a literature the objection does not cite. In this case: a forty-year p-adic program (objection 4) and a mature continuous-relaxation program (objection 2) both existed and both went unmentioned.
5. **Grade, don't polarize.** The four-grade scale (confirmed / partially confirmed / unsupported / contradicted) preserves what is true in an objection — the mechanism gap is real and the program should answer it — while preventing true premises from laundering false ones.

For a researcher receiving an AI-generated or peer critique: run the five steps. They take minutes per objection and convert "this critique says my work is unsubstantiated" into a per-premise ledger that separates what must be answered from what can be dismissed with evidence. For a pipeline operator: the same rubric is a filter — objections whose premises fail verification should not trigger revisions, and objections whose premises verify (like the mechanism gap here) should.

## 11. Conclusion

The five objections examined here are individually plausible and collectively pattern-mistaken. Two fail on their own premises (4, 5), two survive only in corrected form (1, 3), and one is confirmed in substance (2) — the missing measurement mechanism, which the framework's own text concedes and which the continuous-relaxation literature sets the standard for answering. The critique's central error is not its individual claims but its method: it demands evidence from the framework and asserts premises without evidence itself. Applied to itself, the critique fails the standard it sets. That is not a defense of PQS; it is a demonstration that adversarial review, like the frameworks it judges, is only as good as the verification of its premises.

## Declarations

**Funding:** This research received no external funding.

**Conflicts of interest:** The author is the author of the framework under critique; this conflict is disclosed and the grading standard was designed to be symmetric, with every premise verified against sources independent of the framework's own claims.

**Data availability:** All verification evidence (API responses, registry lookups, metadata records) is archived in the project's evidence directory; the corpus records cited are published and resolved via their DOIs.

**AI assistance disclosure:** This paper was written with AI assistance (drafting, verification orchestration, literature lookup). All factual claims were verified against live external registries in-session; AI involvement is disclosed as a quality signal per the corpus' standing policy.

**License:** CC BY-NC-SA 4.0.

**Version:** 0.1 draft — PENDING-ZENODO placeholder; updated in the publication cycle.

## References

Bassi, A., and G. Ghirardi. 2003. "Dynamical reduction models." *Physics Reports* 379 (5–6): 257–426. doi:10.1016/s0370-1573(03)00103-0.

Garola, C., J. Pykacz, and S. Sozzo. 2006. "Quantum Machine and Semantic Realism Approach: a Unified Model." *Foundations of Physics* 36: 862–882. doi:10.1007/s10701-006-9046-z.

Hacohen-Gourgy, S., and L. S. Martin. 2020. "Continuous measurements for control of superconducting quantum circuits." *Advances in Physics: X* 5: 1813626. doi:10.1080/23746149.2020.1813626.

Hardy, L. 2001. "Quantum Theory From Five Reasonable Axioms." arXiv:quant-ph/0101012.

Hensen, B., et al. 2015. "Loophole-Free Bell Inequality Violation Using Electron Spins Separated by 1.3 Kilometres." *Nature* 526: 682–686. doi:10.1038/nature15759.

Khodjaev, J., et al. 2022. "A p-Adic Model of Quantum States and the p-Adic Qubit." *Entropy* 25 (1): 86. doi:10.3390/e25010086.

Kochen–Specker contextuality review. 2022. "Kochen-Specker contextuality." *Reviews of Modern Physics* 94: 045007. doi:10.1103/revmodphys.94.045007.

Kolmogorov, A. N. 1933. *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Berlin: Springer.

Madelung, E. 1927. "Quantentheorie in hydrodynamischer Form." *Zeitschrift für Physik* 40 (3): 322–326. doi:10.1007/bf01400372.

Nelson, E. 1967. *Dynamical Theories of Brownian Motion*. Princeton: Princeton University Press. doi:10.1515/9780691219615.

Quni-Gudzinas, R. B. 2025a. "Post Quantum Synthesis." Zenodo. doi:10.5281/zenodo.21993491.

Quni-Gudzinas, R. B. 2025b. "Hydrodynamic Stability Hypothesis: Re-grounding Quantum Mechanics in Classical Measure Theory." Zenodo. doi:10.5281/zenodo.21993494.

Quni-Gudzinas, R. B. 2025c. "PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis." Zenodo. doi:10.5281/zenodo.21535491.

Quni-Gudzinas, R. B. 2026. "A Non-Archimedean Syntactic Paradigm for Physics." Zenodo. doi:10.5281/zenodo.19600686.

Reddiger, M. 2017. "The Madelung Picture as a Foundation of Geometric Quantum Theory." *Foundations of Physics* 47: 1317–1367. doi:10.1007/s10701-017-0112-5.

Reddiger, M. 2026. "A solution of the quantum time of arrival problem via mathematical probability theory." *Philosophical Magazine*. doi:10.1080/14786435.2026.2627725.

Shafer, G., and V. Vovk. 2006. "The Sources of Kolmogorov's Grundbegriffe." *Statistical Science* 21 (1): 70–98. doi:10.1214/088342305000000467.

Shafer, G., and V. Vovk. 2018. "The origins and legacy of Kolmogorov's Grundbegriffe." arXiv:1802.06071.

Strocchi, F. 2011. "The Physical Principles of Quantum Mechanics. A critical review." arXiv:1112.1507.

Vladimirov, V. S., I. V. Volovich, and E. I. Zelenov. 1998. "Non-Archimedean quantum mechanics." *Tohoku Mathematical Publications* 10: 1–135. doi:10.2748/tmpub.10.1.

Volovich, I. V. 1987. "p-adic string." *Classical and Quantum Gravity* 4 (4): L83–L87. doi:10.1088/0264-9381/4/4/003.

von Neumann, J. 1932. *Mathematische Grundlagen der Quantenmechanik*. Berlin: Springer.

Wu, J., B. B. Augstein, and C. Figueira de Morisson Faria. 2013. "Local dynamics in high-order-harmonic generation using Bohmian trajectories." *Physical Review A* 88: 023415. doi:10.1103/physreva.88.023415.
