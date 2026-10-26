```json
{
  "verdict": "pass",
  "hard": [],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Candidate chiral central charges c_- in {1/2, 3/2, 5/2} are 'inferred from standard fusion structures' of taxonomy families.",
      "reason": "The central-charge assignments are asserted by analogy to known categories (Ising-type, doubled-flux type) rather than derived from the paper's own flux-attachment framework; the Discussion admits a full derivation is deferred. The numerical thermal Hall targets therefore rest on borrowed identifications, weakening the pre-registered projection's independence.",
      "fix": "Either derive c_- for at least one family from the effective gravitational Chern-Simons term within the paper's framework, or explicitly downgrade the family-specific projections to analogies with established MTCs and state that the falsification criterion tests the analogy, not the taxonomy."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Appendix A documenting points of disagreement between underlying drafts is referenced in the Abstract ('we document all points on which the underlying drafts disagreed') but no Appendix A appears in the paper.",
      "reason": "The drafts diverged (e.g., the Fibonacci/Jones computation is explicitly flagged as single-source), so divergence documentation is required; its absence leaves the single-source material uncontextualized by a systematic record.",
      "fix": "Add an Appendix A listing all draft disagreements, which draft each resolution favors, and the rationale for retaining single-source items such as the level-3 Jones computation."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Refs. [5] and [6] are invoked as methodological support for the pre-registered test and the rigidity of the c_-=3/2 class.",
      "reason": "The connections are analogical rather than substantive: a permutation test statistic for block designs supplies no actual statistical machinery used in Section 5 (no test statistic, power, or sample size is defined), and tight contact structures on Sigma_2 x I have no demonstrated bearing on gluing of topological order in 2+1D. The literature treatment of these two citations is superficial relative to the weight placed on them.",
      "fix": "Either specify the concrete permutation-test procedure (statistic, null region, significance threshold) actually used, or drop Ref. [5]; similarly, substantiate or soften the contact-topology rigidity claim for Ref. [6]."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "The paper claims flux attachment is 'complete only relative to the choice of G' yet does not state how G is chosen or constrained for each taxonomy family.",
      "reason": "The mapping from physical platforms (FQH, moire systems) to a flux group G is never specified, so the realizability claim underwritten by Ref. [4] is formal rather than physical; the reader cannot verify that the projected platform realizes any quadruple in the taxonomy.",
      "fix": "Add a subsection stating, for each family, the candidate G, the expected homomorphism phi: B_N -> G, and the physical mechanism (e.g., Chern-Simons level, Berry matrix) that implements phi."
    }
  ]
}
```