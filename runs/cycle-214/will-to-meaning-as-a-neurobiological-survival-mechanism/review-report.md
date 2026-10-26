{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The model predicts that a unit increase in $p$ raises expected survival time by roughly $23\\%$ when normalized to the error regime defined by $\\epsilon_{\\text{pt}}$ and $\\rho$.",
      "reason": "The 23 % figure is presented as a quantitative result but is neither derived with shown arithmetic nor labeled as a projection with explicit assumptions.",
      "fix": "Label the 23 % figure as a projection and explicitly state the assumptions used to obtain it, or remove the claim if no justification is provided."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Differential‑evolution theory specifies that a population size $m$ of $10D$ balances exploration and exploitation, where $D$ is the dimensionality of the decision vector [4].",
      "reason": "Citation [4] is used to support a specific methodological claim, but no excerpt from the bibliography entry for [4] is provided; therefore the claim is not verifiable from the supplied source.",
      "fix": "Replace the statement with a claim that can be supported by an available excerpt, or remove the citation."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Crossing‑point analysis in survival studies derives the crossing time $t_{\\chi}= \\exp\\!\\bigl[-(k_{1}\\log\\lambda_{1}-k_{0}\\log\\lambda_{0})/(k_{1}-k_{0})\\bigr]$, revealing exponential sensitivity of survival intersections to underlying curve parameters [5].",
      "reason": "Citation [5] is used to substantiate a specific formula, but no excerpt from the bibliography entry for [5] is supplied; the claim cannot be verified from the provided material.",
      "fix": "Either provide a verifiable excerpt from [5] that contains the crossing‑point formula or remove/replace the statement."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Two‑scale optimization of graded lattice structures shows how micro‑ and macro‑scale buckling constraints can be homogenized, suggesting a multiscale approach to modeling physiological resilience [6].",
      "reason": "Citation [6] is invoked without any supporting excerpt; the specific point about buckling constraints is not present in the supplied bibliography excerpts.",
      "fix": "Remove the statement or replace it with a claim that can be directly supported by an available excerpt."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The Gumbel‑Softmax method enables gradient‑based optimization of categorical design variables, offering a technique for learning discrete purpose states within continuous control policies [7].",
      "reason": "Citation [7] is used to support a methodological claim, but no excerpt from the bibliography entry for [7] is provided; the claim lacks verifiable grounding.",
      "fix": "Delete the sentence or substitute it with a claim backed by an available excerpt."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Measurement of purpose: requires validated psychometric scales or neuroimaging proxies; current literature [8] provides qualitative descriptions but no standardized quantitative metric.",
      "reason": "The statement attributes a specific assessment of the literature to citation [8], yet no excerpt from [8] is supplied; the claim cannot be verified from the provided sources.",
      "fix": "Remove the claim or rephrase it as an assumption without citing [8]."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Section 2 discusses only six works with verifiable excerpts ([2]–[5]) and fails to meet the requirement of discussing at least eight bibliography works with specific points.",
      "reason": "The paper must cite at least eight works with substantive points drawn from their supplied excerpts; currently only six such citations are supported.",
      "fix": "Add discussion of two additional bibliography entries (e.g., [1] and another entry with an available excerpt) each providing a specific point, or remove unsupported citations to reduce the count to six while meeting the minimum requirement."
    }
  ],
  "soft": []
}