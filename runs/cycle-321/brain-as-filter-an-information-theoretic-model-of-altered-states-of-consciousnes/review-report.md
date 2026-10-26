{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Efficient embedding networks for 3D brain‑tumor segmentation compress high‑dimensional data while discarding redundancy, mirroring the brain’s need to compress an informational ground into a tractable channel [3].",
      "reason": "The excerpt for reference [3] contains only the title and no statement about compressing high‑dimensional data or discarding redundancy; the cited claim is not supported by the supplied text.",
      "fix": "Remove or replace the sentence with a claim directly supported by the excerpt, or omit the citation."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Estimation‑aware optimal control of mobile sensors incorporates measurement‑dependent uncertainty into trajectory planning, explicitly modeling how sensor dynamics affect information acquisition; this parallels thalamic gating that controls neural information flow [4].",
      "reason": "The excerpt for reference [4] provides only the title; it does not contain the described detail about measurement‑dependent uncertainty or its parallel to thalamic gating.",
      "fix": "Remove or replace the sentence with a claim directly supported by the excerpt, or omit the citation."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Federated learning for brain‑tumor segmentation must operate under limited communication bandwidth, illustrating how performance degrades when channel capacity is reduced, analogous to reduced neural capacity in ASCs [7].",
      "reason": "The excerpt for reference [7] includes only the title; it does not mention limited communication bandwidth or performance degradation.",
      "fix": "Remove or replace the sentence with a claim directly supported by the excerpt, or omit the citation."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The Bekenstein bound states that the maximum amount of information \\(I_{\\max }\\) that can be stored in a physical system of radius \\(R\\) and total energy \\(E\\) is \\(I_{\\max }=\\frac{2\\pi R E}{\\hbar c\\,\\ln 2}\\) bits, where \\(\\hbar\\) is the reduced Planck constant and \\(c\\) the speed of light \\([9]\\).",
      "reason": "The excerpt for reference [9] is only a URL and does not contain the Bekenstein bound formula; the claim is not grounded in the supplied text.",
      "fix": "Remove the citation or replace the statement with a claim supported by the excerpt."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "If the brain’s filter were to incorporate deterministic non‑linear transformations that preserve hidden variables, the effective channel could be modeled as a cascade of linear and deterministic non‑linear stages. The overall capacity would then be bounded by the linear stage, reinforcing the relevance of the Shannon bound even in a deterministic universe \\([10]\\).",
      "reason": "The excerpt for reference [10] does not contain any discussion of deterministic non‑linear transformations or their effect on channel capacity; the citation is unsupported.",
      "fix": "Remove or replace the sentence with a claim directly supported by the excerpt, or omit the citation."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The filtered information substrate is represented by a covariance matrix \\(\\Sigma\\). In many high‑dimensional systems the eigenvalue spectrum exhibits a hierarchical clustering that can be modeled as an ultrametric space \\([11]\\).",
      "reason": "The excerpt for reference [11] is only a URL and does not provide the described statement about ultrametric spaces; the citation is unsupported.",
      "fix": "Remove or replace the sentence with a claim directly supported by the excerpt, or omit the citation."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "The filter operator \\(F\\) introduced in Section 3.4 is linear and can be expressed as a matrix acting on the informational vector \\(\\mathbf{I}\\). The topological extension framework (TEF) models physical entities as finite‑volume stable modes rather than point‑like objects \\([12]\\). Within TEF, stability of a mode is guaranteed when the operator governing its evolution is contractive, i.e., its spectral radius \\(\\rho(F)\\) satisfies \\(\\rho(F) < 1\\).",
      "reason": "The excerpt for reference [12] does not contain the described TEF concepts; the citation is unsupported.",
      "fix": "Remove or replace the sentence with a claim directly supported by the excerpt, or omit the citation."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "A direct falsification would occur if simultaneous MEG‑derived capacity estimates \\(C_{1}\\) show **no** correlation (Pearson \\(|r|<0.1\\)) with reported timelessness, unity, or presence across a cohort of meditators.",
      "reason": "The quantitative threshold \\(|r|<0.1\\) is presented without derivation or labeling as a projection; it is a quantitative claim that is not derived in the paper.",
      "fix": "Label the statement as a proposed falsification criterion (a projection) and explicitly state it as an assumption, or remove the specific numeric threshold."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The literature review touches on many works but does not deeply explain how each cited result quantitatively informs the model parameters.",
      "reason": "Depth of literature treatment could be expanded.",
      "fix": "Provide brief quantitative links where possible."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Appendix A states no divergent claims were identified, but the paper does not discuss any limitations of the derivations beyond the listed ones.",
      "reason": "More thorough discussion of limitations would strengthen the paper.",
      "fix": "Add a paragraph acknowledging potential model simplifications."
    }
  ]
}