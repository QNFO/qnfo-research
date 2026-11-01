```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Section 2: \"[2] predicts a geometric‑code logical error rate $p_L^{\\mathrm{geom}} = 7.1\\times10^{-5}$ for $d = 5$ versus a surface‑code rate $p_L^{\\mathrm{SC}} = 5.1\\times10^{-9}$, a separation of three orders of magnitude [2].\"",
      "reason": "Arithmetic error in a stated quantitative comparison. The ratio of the two cited rates is 7.1e-5 / 5.1e-9 = 1.39e4, i.e. a separation of about 4.1 orders of magnitude (log10(1.39e4) = 4.14), not three. The two endpoint values are correctly quoted from [2], but the derived separation stated in this paper's own voice is wrong.",
      "fix": "Replace 'a separation of three orders of magnitude' with 'a separation of approximately four orders of magnitude' (or state the ratio 1.4e4 explicitly)."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Section 3, Corrections paragraph: \"...while $I_6$ compares resource counts across platforms at fixed $p_L$, and no supplied or derived relation connects them.\"",
      "reason": "Prose gate violation: the sentence uses the banned source-voice term 'supplied', describing a relation as 'supplied', which speaks to how source material reached the paper. The same point is correctly phrased elsewhere (Section 4.5: 'no relation stated in [5] or derived here connects them').",
      "fix": "Reword to 'and no relation stated in [5] or derived here connects them', matching the phrasing already used in Section 4.5."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "References section contains 5 entries.",
      "reason": "Fewer than 8 references. However, the provided bibliography itself contains only 5 works, the paper cites all of them, and the limitation is explicitly stated in Section 6 ('The bibliography of this version contains five works, all of which are cited...'). Inventing additional references would violate citation integrity, so this is not actionable as a hard defect.",
      "fix": "No fix possible within the given bibliography; the stated limitation in Section 6 is the correct handling."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Section 6: \"a reset of $100~\\mu\\mathrm{s}$ would raise the per-cycle error to roughly $0.199$, ten times the reported value.\"",
      "reason": "The computed value 0.199 is correct (1 - exp(-0.22173) = 0.19895), but 0.199 / 0.0219 = 9.1, so 'ten times' slightly overstates the factor; 'roughly' partially mitigates.",
      "fix": "State 'about nine times the reported value' or 'roughly a tenfold increase'."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Section 2 statements about [3], [4] and [5] (e.g., [3]'s §4.5 and §2 content, [4]'s 241:1 to 4:1 overhead reduction, [5]'s 5–40× photon ratio, 12 dB squeezing caveat and 2028–2030 horizon).",
      "reason": "These claims are consistent with the titles and with the paper's internal framing, and [4]'s figures are explicitly labeled an unverified external claim, but the review excerpts provided cover only [1] and [2], so the attributions to [3], [4] and [5] could not be independently checked against full-text excerpts in this audit.",
      "fix": "Ensure the pipeline's attribution check confirms these section-level attributions against the full entries for [3], [4] and [5]."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "Section 2 opening: \"This corrected version cites the five works of its bibliography, in the bibliography's own numbering; because the list contains fewer than eight works, all of them are cited and the limitation is stated in Section 6.\"",
      "reason": "The sentence is meta-commentary about the paper's own reference list rather than about the literature; the same information is already carried in Section 6.",
      "fix": "Trim to a brief statement that all five referenced works are discussed below, or move the count entirely to Section 6."
    }
  ]
}
```