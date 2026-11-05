{
 "verdict": "revise",
 "hard": [
 {
 "id": "Section 2",
 "severity": "HARD",
 "claim": "Section 2 discusses at least 8 works from the Bibliography but fails to cite them with specific points from their entries.",
 "reason": "The section lists topics like 'graph braid groups as non-geometric families' and 'DAHA-induced braid actions' without citing the corresponding Bibliography entries [3] and [4], respectively. Each cited work must be discussed with a specific point from its full-text excerpts, but the paper instead lists works only to acknowledge them or frame a research direction.",
 "fix": "Cite each discussed work with a specific point from its full-text excerpt, ensuring all 8 required works are addressed with their exact numbering."
 },
 {
 "id": "Section 2",
 "severity": "HARD",
 "claim": "The paper cites QNFO work [9] but contradicts its own claims about the Ising deformation family.",
 "reason": "The paper states that the deformation family Ising(7) 'shares all fusion rules with Ising but has θσ=e^{7iπ/8}' and 'its B3 representation is inequivalent to Ising's.' However, the companion analysis [9] explicitly notes that 'its unitarity as a Galois conjugate is not established' and 'no chiral central charge is assigned.' The paper's claim about the deformation family's distinct B3 representation is not supported by [9], which only mentions it as a formal deformation.",
 "fix": "Revise the discussion of Ising(7) to reflect that [9] treats it as a formal deformation without establishing its unitarity or distinct B3 representation."
 }
 ],
 "soft": [
 {
 "id": "Section 2",
 "severity": "SOFT",
 "claim": "Section 2's literature treatment is superficial and lacks depth.",
 "reason": "The section lists research directions (e.g., 'numerical extraction of modular data') without elaborating on their relevance or specific contributions from the cited works. For example, the 'DAHA-induced braid actions' are mentioned but not tied to [4]'s content about the DAHA of type C∨C1.",
 "fix": "Expand the discussion to connect each listed topic to specific findings or methods from the cited works."
 },
 {
 "id": "Section 7",
 "severity": "SOFT",
 "claim": "Section 7's practical implications lack explicit quantification of engineering constraints.",
 "reason": "While the section lists constraints (e.g., 'phase coherence time'), it does not derive them from the paper's analysis or cite the Bibliography for their origin. For example, 'decoherence time of ~100 μs' is stated without reference to [8] or [12].",
 "fix": "Quantify constraints using derived values or cite the Bibliography for their origin."
 }
 ]
}