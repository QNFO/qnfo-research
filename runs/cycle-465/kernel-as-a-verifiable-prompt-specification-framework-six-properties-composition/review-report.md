```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Section 4.3: 'So: $$\\frac{P_c}{P_m} = \\frac{1}{0.77378094} \\approx 1.2920.$$' and Section 8: 'dominates a monolithic prompt by $\\alpha^{-5} \\approx 1.2920$'",
      "reason": "Arithmetic error and cross-section inconsistency. 1/0.7737809375 = 1.29232, which rounds to 1.2924 at four decimal places, not 1.2920. Section 5 (R3) states '$\\alpha^{-5} \\approx 1.2924$', so the paper states two different four-decimal values for the same headline quantity in Sections 4.3, 5, and 8 (Abstract uses 1.292, consistent with either).",
      "fix": "Replace 1.2920 with 1.2924 in Section 4.3 and Section 8 (or use 1.2923 consistently everywhere) so that the derived value, Results R3, the Abstract, and the Conclusion all agree."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Section 2: 'its limitation section concedes that manifesto-derived constraints are enforced primarily at the prompt level with only partial runtime verification.'",
      "reason": "The supplied excerpt of [2] ends mid-sentence in its Discussion ('The current implementation h') and does not contain the limitation-section statement; the claim should be confirmed against the full entry text before publication.",
      "fix": "Verify the limitation-section wording against the full text of [2]; if unsupported, reword to what the Discussion excerpt states (phase-ordered execution, bounded repair loops, deterministic validation gates)."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "References entry [10] (Exact Maximum-Likelihood Quantum Decoding beyond Treewidth) is listed but never cited in the body.",
      "reason": "The rule is to cite a work for a specific point or not at all; an uncited reference entry is dead weight and invites the appearance of padding.",
      "fix": "Either cite [10] for a specific point (e.g., structural-analysis methodology parallel in Section 2) or remove it from the References list."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Section 1: 'the KERNEL discipline, a six-property prompt methodology recorded in practitioner notes'.",
      "reason": "The provenance ('practitioner notes') is a claim about the world with no cited source; it should be stated as the paper's own framing or an assumption.",
      "fix": "Reword to 'the KERNEL discipline, a six-property prompt methodology we treat here as a practitioner tradition' or explicitly label the characterization as the paper's own framing."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "QNFO consistency check: the paper's uses of [9] (soundness deg(P_E) <= B(E), B(E)=5, D(pq)=10, looseness overestimate of 4), [11] (contract extraction/discharge, labeled projections), and [12] ((2/3)^k completeness, f(5)=32/243, 57.7x gap at k=10, Rice's-theorem undecidability) are internally consistent and consistent with each other, but the supplied excerpt set does not include these entries' full text for independent attribution.",
      "reason": "No contradiction, inversion, or overstatement is detectable from the material provided; the check is recorded as agreeing in substance, with attribution verifiable only against the full entries.",
      "fix": "No change required; retain the current characterizations, which restate rather than extend the cited QNFO works' claims."
    }
  ]
}
```