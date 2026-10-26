{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The References list contains only six entries ([1], [3], [4], [5], [9], [11]) and omits entries for works cited in the text such as [2], [6], [7], and [8].",
      "reason": "Citation integrity requires that every work cited in the manuscript appear in the References list, and the paper must contain at least eight references. The missing entries violate both requirements.",
      "fix": "Add the missing bibliography entries for [2], [6], [7], and [8] in the References section, preserving the original numbering order and exact titles/identifiers from the provided bibliography."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Citations to works [2], [6], [7], and [8] appear in Section 2 but those works are not listed in the References section.",
      "reason": "Every in‑text citation must correspond to a full reference entry; absent entries break citation integrity.",
      "fix": "Insert the full reference entries for [2] arXiv:hep-ex/9605011v1, [6] arXiv:2512.25072v1, [7] arXiv:1311.3888v1, and [8] arXiv:2404.10736v2 into the References list, maintaining the original numbering sequence."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The literature review in Section 2 provides brief one‑sentence descriptions of many works without deeper critical analysis.",
      "reason": "While the paper meets the minimum requirement of citing at least eight works, the treatment is superficial and could be expanded to better contextualize each contribution.",
      "fix": "Enrich each cited work’s discussion with an additional sentence that explains how its specific result supports the paper’s argument, staying within the constraints of the supplied excerpts."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "The discussion of limitations in Section 6 lists several constraints but does not quantify their impact on the main results.",
      "reason": "Providing quantitative sensitivity estimates would strengthen the assessment of robustness.",
      "fix": "Add brief quantitative estimates (e.g., how a ±5 % change in ε alters w_cd/R) to the sensitivity analysis paragraph."
    }
  ]
}