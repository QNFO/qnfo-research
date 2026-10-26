{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Error‑rate‑agnostic decoding (EWD) is discussed in [3].",
      "reason": "The bibliography excerpt for entry [3] is not provided, so the claim cannot be verified against the source text.",
      "fix": "Remove or replace the statement with a claim that is supported by an available excerpt, or add a proper citation to a work whose excerpt includes this point."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Simple decoder for topological codes is described in [4].",
      "reason": "No excerpt for entry [4] is supplied; the statement lacks source support.",
      "fix": "Delete the sentence or cite a work whose excerpt confirms the existence of such a decoder."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "SC‑Flip improvements are reported in [5].",
      "reason": "The bibliography does not include an excerpt for entry [5]; the claim is unsupported.",
      "fix": "Remove the sentence or replace it with a claim that can be directly sourced from an available excerpt."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Neural‑network decoder training is mentioned in [6].",
      "reason": "No excerpt for entry [6] is provided; the claim cannot be verified.",
      "fix": "Delete or rephrase the sentence to reflect only information present in the supplied excerpts."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Graph Neural Network (GNN) decoder is mentioned in [7].",
      "reason": "Entry [7] lacks an excerpt; the statement is not grounded in the supplied text.",
      "fix": "Remove the claim or replace it with a citation that has supporting excerpt."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Ambiguity Clustering (AC) demonstrates an operation‑count advantage for $n=1023$ qubits [9].",
      "reason": "No excerpt for entry [9] is provided; the claim cannot be substantiated.",
      "fix": "Delete the sentence or provide a verifiable excerpt from [9] that contains the claimed operation‑count advantage."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Regular ternary tree codes introduce a symmetric exponential energy barrier $B(d)=2^{d}$ ... and report a logical‑failure probability $P_{\\mathrm{pass}}\\approx9.98\\times10^{-6}$ under independent depolarizing noise $\\varepsilon=10^{-3}$ [10].",
      "reason": "No excerpt for entry [10] is supplied; the specific numerical claim is not verifiable.",
      "fix": "Remove or rephrase the statement to only include information that can be sourced from an available excerpt."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Five Pillars Convergence argues that ultrametric mathematics is a unifying structure across quantum computation, cryptography, and physics [11].",
      "reason": "Entry [11] lacks an excerpt; the claim cannot be confirmed.",
      "fix": "Delete the sentence or replace it with a claim supported by an available excerpt."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Finite‑Distinction Quantum Mechanics proposes that state‑space geometry is ultrametric in a finite‑distinction world [12].",
      "reason": "No excerpt for entry [12] is provided; the claim is unsupported.",
      "fix": "Remove the sentence or cite a source with a verifiable excerpt."
    },
    {
      "id": "H10",
      "severity": "HARD",
      "claim": "Abstract: \"implying a $4.07\\times10^{3}$‑fold speedup\".",
      "reason": "The speedup value $4.07\\times10^{3}$ is not derived in the paper; Section 4 derives $4.05\\times10^{3}$ (and the correct division yields $4.0645\\times10^{3}$). This quantitative claim is inconsistent and not labeled as a projection.",
      "fix": "Replace the abstract speedup figure with the correctly derived value $4.06\\times10^{3}$ (rounded to three significant figures) and ensure it matches the value reported in Section 4."
    },
    {
      "id": "H11",
      "severity": "HARD",
      "claim": "Section 4.5 arithmetic: \"\\frac{C_{\\mathrm{TN}}}{C_{\\mathrm{DP}}}=\\frac{4.35\\times10^{12}}{1.07\\times10^{9}}=\\frac{4.35}{1.07}\\times10^{3}\\approx 4.05\\times10^{3}.\"",
      "reason": "The division $4.35/1.07$ equals $4.0645$, not $4.05$; the rounding is inaccurate and constitutes an arithmetic error.",
      "fix": "Correct the computation to $\\approx 4.06\\times10^{3}$ (or $4.0645\\times10^{3}$) and update all downstream mentions of the speedup accordingly."
    }
  ],
  "soft": []
}