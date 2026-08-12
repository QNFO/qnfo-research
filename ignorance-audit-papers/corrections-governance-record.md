---
title: "Corrections and Governance Record for the Analyzed Paper: The Qudit Advantage"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-12"
license: "CC BY-NC-SA 4.0"
doi: "10.5281/zenodo.21901930"
status: "published"
---

## Purpose

This record documents the corrections and governance response for the analyzed paper
*The Qudit Advantage: System-Level Joules-per-Solution Comparison of a Qudit Architecture
Against 17 Conventional Qubit Quantum Computing Platforms* (v0.4, DOI
10.5281/zenodo.21827737). It exists so that the citation *Quni-Gudzinas 2026c* in the
companion synthesis *Knowing What We Do Not Know* (DOI 10.5281/zenodo.21878977) resolves
to a findable, DOI-bearing artifact, and so that the correction trail is documented in a
single governance record.

## 1. The AI-Generation Finding (9 August 2026)

On the evening of 9 August 2026, two independent AI-assisted forensic analyses of the v0.4
text concluded that the paper was AI-generated. Their convergent evidence, as reported in
the companion synthesis, included:

1. **Structural markers** — inlined meta-tags (`[PHILOSOPHY]`, `[speculative]`,
   `[CHECK: 2027]`, `Strength: [STRONG] | Status: [PENDING]`) characteristic of prompt
   templates that instruct a model to label its own cognitive modes; rigid scaffold
   structures mimicking popular synthetic-evaluation frameworks.
2. **Synthetic citation anchors** — inline keys such as `@C5_jpcub_p0` and
   `@B1_shannon1948` with custom prefixes, which do not resolve to standard bibliographic
   entries. The v0.4 text's References section was empty.
3. **A decoder-energy direction error** — the paper set the decoder power
   `$P_{\text{decode}}^{\text{qudit}} \approx 0$`, justified by the algorithmic complexity
   `$O(\log_p N)$` of tree-traversal decoding, and labeled this a "conservative upper
   bound." Zero is a lower bound, not an upper bound, and the assertion ignores the real
   classical ASIC and control-logic power required to run hierarchical decoders in real
   time.
4. **A Landauer temperature conflation** — computing the bound at room temperature
   (`$T = 300\text{ K}$`) versus cryogenic temperature (`$T = 10\text{ mK}$`) in Planck
   units, and conflating thermodynamic erasure-energy floors with room-temperature
   operational coherence without proposing a physical hardware mechanism for suppressing
   thermal noise.
5. **Self-disclosure** — the paper candidly disclosed that its performance metric had zero
   external citations or independent validations as of 2026-08-06.

## 2. The Disclosure Decision

The organization did not delete, retract, or conceal the AI-generated paper, nor did it
relabel the paper as human-written. Instead it:

1. Disclosed AI involvement explicitly in the paper's metadata and body.
2. Classified the paper's authorship transparently in its corpus metadata.
3. Published corrections to the identified errors.

The disclosure decision was grounded in the empirical literature on AI-text reception:
readers are poor at detecting AI-generated text absent labels, and credibility judgments
are strongly label-dependent (Kreps, McCain, and Brundage 2020), while trust asymmetries
penalize deception more than disclosure (Dietvorst, Simmons, and Massey 2015).

## 3. The Correction Trail

The corrections were published as sequential versions of the same concept, each applying
the AI-QUALITY-GATE fixes:

| Version | DOI | Date | Content |
|:--------|:----|:-----|:--------|
| v0.4 | 10.5281/zenodo.21827737 | 2026-08-06 | Analyzed version (errors documented above) |
| v0.5 | 10.5281/zenodo.21878856 | 2026-08-10 | JPCUB framework extended; caveats added; body corrected |
| v0.6 | 10.5281/zenodo.21879110 | 2026-08-10 | Further corrections |
| v0.6.1 | 10.5281/zenodo.21879117 | 2026-08-10 | Corrected paper body with self-DOI fix |
| v0.7 | 10.5281/zenodo.21880104 | 2026-08-10 | Canonical current version (md/html/pdf) |

The ERRATA.md attached to this record consolidates the specific error corrections.

## 4. Forensic Quality Gate (adopted after the finding)

For AI-generated and AI-assisted papers, the publication pipeline now enforces a forensic
quality gate:

1. No elementary physics or energy-budget errors.
2. No synthetic or unresolvable citation anchors in the published body.
3. No scaffold overload (meta-tag echo, rigid template boxes).
4. No over-explaining textbook foundations while hand-waving the novel integration.
5. No self-referential metric claims without external validation.

## 5. Governance Principles

1. **Disclosure rather than concealment** — AI involvement disclosed is a quality signal;
   concealed AI involvement is an integrity violation.
2. **Quality gates rather than denial** — errors are corrected and versioned, not denied.
3. **Adversarial validation rather than self-confirmation** — disconfirmation conditions
   are published; independent analysis is solicited.
4. **Auditing the auditors** — verification layers are themselves subject to the failure
   modes they diagnose; the Universal Ignorance Audit (DOI 10.5281/zenodo.21878976) is
   applied to the audit process itself.

## 6. Note on the Forensic Analyses

The two forensic analyses were conducted by independent AI-assisted analysts and are
preserved in the author's research notes (9 August 2026). They are not deposited here
because they are narrative artifacts of an AI-assisted analysis session rather than
independent machine-readable datasets; their convergent findings are reported in the
companion synthesis (DOI 10.5281/zenodo.21878977). The forensic analyses themselves
were not free of the failure modes they diagnosed: both asserted that the organization
and its platform were "fabricated institutions," and one asserted that the author's name
was a "portmanteau" of the words quantum and gibberish. Both claims are false — the
organization is a real research entity and the author is a real person. The auditors
treated unknown proper names as evidence of fabrication, committing the scaffold-confusion
error (treating the map of "what I recognize" as the territory of "what exists").

## References

Dietvorst, Berkeley J., Joseph P. Simmons, and Cade Massey. 2015. "Algorithm Aversion:
People Erroneously Avoid Algorithms after Seeing Them Err." *Journal of Experimental
Psychology: General* 144 (1): 114--126. https://doi.org/10.1037/xge0000033

Kreps, Sarah, R. Miles McCain, and Miles Brundage. 2020. "All the News That's Fit to
Fabricate: AI-Generated Text as a Tool of Media Misinformation." *Journal of Experimental
Political Science* 9 (1): 104--117. https://doi.org/10.1017/xps.2020.37

Quni-Gudzinas, Rowan Brad. 2026. "The Qudit Advantage: System-Level Joules-per-Solution
Comparison of a Qudit Architecture Against 17 Conventional Qubit Quantum Computing
Platforms." Zenodo preprint. https://doi.org/10.5281/zenodo.21827737
