{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The paper “ASVRI‑Legal” demonstrates an engineering pattern where a high‑level legal ontology is re‑entered onto human conduct via a bounded retrieval‑augmented generation mechanism, showing that re‑entry maps can be implemented with concrete computational constraints [3].",
      "reason": "No excerpt from reference [3] is provided in the bibliography, so the specific claim cannot be verified from the supplied source.",
      "fix": "Remove the sentence or replace it with a claim supported by an existing cited work that has a provided excerpt."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "**Beables, primitive ontology and beyond.**",
      "reason": "Reference [5] is cited without any supporting excerpt, violating the requirement to cite a specific point from the work's full text.",
      "fix": "Delete the mention of [5] or replace it with a supported statement from a work that has an excerpt."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "**Ontology revision based on pre‑trained language models.**",
      "reason": "Reference [6] is cited without any supporting excerpt, so the claim lacks grounding.",
      "fix": "Remove the citation of [6] or substitute a supported claim from a cited work with an excerpt."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Autaxys Ontological Closure ... [9]",
      "reason": "Reference [9] is cited without any excerpt; the paper makes a claim about its content that cannot be verified.",
      "fix": "Delete the citation of [9] or replace it with a claim grounded in an excerpted source."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Ontological Re‑Entry: What Can We Say Exists? ... [10]",
      "reason": "Reference [10] is cited without an excerpt; the statement about its content is unsupported.",
      "fix": "Remove the citation of [10] or replace it with a claim supported by an excerpted reference."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Finite Specification, Ontological Indeterminism ... [11]",
      "reason": "Reference [11] is cited without an excerpt, so the claim lacks a verifiable source.",
      "fix": "Delete the reference to [11] or substitute a supported statement from an excerpted work."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Pattern‑Based Ontology (PBO) alignment ... [12]",
      "reason": "Reference [12] is cited without an excerpt; the claim cannot be derived from the supplied bibliography.",
      "fix": "Remove the citation of [12] or replace it with a claim that is supported by an excerpt."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "In Section 4.5 the probability that a given coarse ball receives exactly one object is computed as p_{1} ≈ 3.61×10^{-41}. Later, the table and subsequent sections report p_{1} ≈ 3.78×10^{-41}.",
      "reason": "The paper presents two different numerical values for the same probability without reconciling them; only one derived value can be correct.",
      "fix": "Re‑compute p_{1} consistently (using the Poisson or exact binomial formula) and use the same value throughout the manuscript."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "In Section 4.5 the expected number of coarse balls containing exactly one object is given as E_{single} ≈ 3.70×10^{-38}, while the summary table lists ≈0 (3.87×10^{-38}) and Section 5 repeats ≈0.",
      "reason": "Inconsistent values for the same expected quantity appear in different parts of the paper, violating quantitative honesty.",
      "fix": "Align the expected value with the correctly computed probability from H8 and update all occurrences to the consistent number."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The literature review in Section 2 mentions several works (e.g., “Beables, primitive ontology and beyond”) without detailed discussion of their methods or results.",
      "reason": "The treatment is superficial and could be expanded to meet depth expectations.",
      "fix": "Provide a brief, excerpt‑based description of each cited work’s specific contribution, or remove the uncited entries."
    }
  ]
}