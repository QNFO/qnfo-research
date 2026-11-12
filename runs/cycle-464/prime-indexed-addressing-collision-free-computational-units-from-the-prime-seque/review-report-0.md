```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Section 6, The retrieval bottleneck: \"and no source in this paper's corpus supplies an algorithm or hardware that performs prime-counting inversion at memory-bandwidth rates.\"",
      "reason": "Source-voice violation: the sentence refers to the paper's 'corpus' of sources, which is prohibited phrasing about how the sources reached the paper.",
      "fix": "Rewrite as: \"and no work cited here supplies an algorithm or hardware that performs prime-counting inversion at memory-bandwidth rates.\""
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Section 2: \"[3] also proves equivalence theorems (its Theorems 4.2 and 5.10) linking a conjecture on primes between consecutive squares to statements about $\\pi$ on short intervals\".",
      "reason": "The specific theorem numbers 4.2 and 5.10 are not stated in the cited work's entry; the entry's abstract supports only that a positive answer to the consecutive-squares question would imply Legendre's, Brocard's, Andrica's, and Oppermann's conjectures, not the numbered theorems.",
      "fix": "Drop the unverifiable theorem numbers and state only what the entry supports: \"[3] also proves that a positive answer to its question on primes between consecutive squares would imply Legendre's, Brocard's, Andrica's, and Oppermann's conjectures.\""
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Section 1, Introduction: \"collision resolution dominates the tail latency of in-memory caches, and address ambiguity forces capacity overheads that scale with the square of the load factor in open-addressed tables.\"",
      "reason": "Unsourced claims about the outside world: neither the load-factor-squared overhead nor tail-latency dominance is stated in any bibliography entry or derived in the paper.",
      "fix": "Remove the unsourced quantitative characterizations, e.g.: \"Hash tables pay for collisions in rehashing and probing, and distributed key-value stores pay for address ambiguity in consensus traffic and conflict resolution; large language models must keep $V$ token identities distinguishable as vocabularies and context lengths grow.\""
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Section 6: \"since consecutive reciprocals differ by about $\\alpha / p_{N-1}^2$; at $p_{N-1} \\approx 10^9$ this is a separation of order $10^{-18}\\alpha$, requiring of order $60$ decimal digits of precision to resolve.\" (repeated in Section 7(d): \"requiring of order $60$ decimal digits, which exceeds standard hardware floating-point formats.\")",
      "reason": "The '60 decimal digits' figure is not derived and contradicts the paper's own stated separation: a relative separation of order $10^{-18}$ requires of order 19 significant decimal digits to resolve, not 60.",
      "fix": "Replace 'of order $60$ decimal digits' with 'of order $19$ decimal digits' in both Section 6 and Section 7(d), consistent with the stated $10^{-18}$ separation."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Section 4.7: \"$\\log_2 9{,}699{,}690 = \\ln(9.69969 \\times 10^{6})/\\ln 2 = 16.087526 / 0.693147 = 23.2080$\"",
      "reason": "The intermediate natural-log value is slightly off ($\\ln 9.69969 \\times 10^{6} \\approx 16.087636$); the final result 23.2080 is unaffected, but the shown intermediate digit is not exact.",
      "fix": "Correct the intermediate to $16.087636$ and keep the result $23.2080$."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Section 6, hierarchical structure paragraph and Section 7(f) rely on [8]'s empirical fractal finding and [9]'s and [12]'s budgets and bottleneck claims.",
      "reason": "Depth: the paper's use of these works is specific and consistent with their titles and stated content, but the attribution rests entirely on those entries; a reader cannot cross-check the 1.3-billion-prime sample size or the budget values against the full texts here.",
      "fix": "No change required to the claims; optionally note in Section 6 that the budget values are adopted as stated in [9] rather than re-derived."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Section 7(c): \"we suggest a factor of $10$ as the threshold\"",
      "reason": "The falsification threshold of 10x latency is a stipulated choice, not derived; it is labeled as a suggestion but its sensitivity is not discussed.",
      "fix": "Add one sentence noting the conclusion is insensitive to the exact threshold as long as it is a small constant factor."
    }
  ]
}
```