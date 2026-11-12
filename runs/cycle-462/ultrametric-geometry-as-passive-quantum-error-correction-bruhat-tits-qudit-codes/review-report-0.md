```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Section 2 contains five consecutive placeholder paragraphs: '**Continuous-time QEC [1].** (already covered above)', '**Entanglement-assisted codes [2].** (already covered above)', '**Qudit algorithms [3].** (already covered above)', '**Classical-to-quantum coding surveys [4].** (already covered above)', '**Foundations of QEC [5].** (already covered above)'",
      "reason": "Placeholder text in the body violates the prose gate; the duplicated blocks add no content and read as unfinished drafting artifacts.",
      "fix": "Delete the five '(already covered above)' paragraphs entirely; the substantive discussions of [1]-[5] earlier in Section 2 already stand on their own."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "In the Section 2 summary: 'the active-QEC canon [4]–[6] defines the syndrome-based baseline'",
      "reason": "Reference [6] (arXiv:1910.03672v1) is cited only through a range, for its existence and framing; no specific method, result or argument from [6] is stated anywhere in the paper, which the citation-integrity rule forbids.",
      "fix": "Either state a specific point from [6]'s full text (as done for [4] and [5]) or remove '[6]' from the range and from the References-adjacent framing sentence."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Detailed attributions to the QNFO works, e.g. 'derives, for the same tree geometry, energy barrier heights $B(3)=8$ and $B(4)=16$, logical error bounds $p_L(3)=6.5536\\times10^{-4}$ and $p_L(4)=4.295\\times10^{-7}$ at a per-vertex error probability $p_{\\mathrm{err}}=0.40$' [8]; 'reports suppression factors of $\\approx6.10\\times10^{2}$ at depth 3 and $\\approx9.31\\times10^{5}$ at depth 4' [10]; 'reports for the same ball-code model the values $P_{\\mathrm{pass}}=5.992003\\times10^{-6}$ at $t=1$, suppression factor $S=166.9$' [11]; 'the active logical failure probability is $P_{\\mathrm{act}}\\approx3.98\\times10^{-5}$, not $4.07\\times10^{-5}$' attributed to [9]",
      "reason": "The supplied entries for [8], [9], [10] and [11] contain only titles and URLs; none of the numbers, falsification criteria, experiment designs or arithmetic-error claims attributed to these works is stated in their supplied text, so these statements about what the cited works did, found or argued are unverifiable against the sources (citation-consistency check for QNFO works cannot confirm agreement).",
      "fix": "Support each attribution with the corresponding work's own full-text content, or rewrite the sentences to present these numbers as this paper's own assumptions/projections ('We assume/We take as a reported figure of the prior version...') without attributing specific derived values to works whose text is not available for verification."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Lemma 1 proof step: 'The tree metric inherited from the $p$-adic valuation satisfies the strong triangle inequality $\\operatorname{dist}(v,v')\\le\\max(\\operatorname{dist}(v,w),\\operatorname{dist}(w,v'))\\le t$'",
      "reason": "The ultrametric (strong triangle) property of the tree distance is invoked without derivation; graph distance on a homogeneous tree is not ultrametric in general, so the leap from $s\\le 2t$ to $s\\le t$ needs justification (e.g. via the median/branch-point structure already introduced).",
      "fix": "Add a short derivation showing $s=\\operatorname{dist}(v,m)+\\operatorname{dist}(m,v')\\le t$ directly from the two ball-membership inequalities and the position of the median $m$, or state explicitly the ultrametric property being used and why it holds here."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Section 4.3 contains the duplicated line '**Input.** $\\varepsilon=10^{-3}$.' twice in a row",
      "reason": "Duplicated input statement is a drafting artifact that could suggest two distinct inputs.",
      "fix": "Delete one of the two identical 'Input' lines."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Section 4.3, t=2 case: 'The first product is $0.992027944070\\times0.996005996001=0.988065684\\ldots$'",
      "reason": "Intermediate products are given with ellipses rather than full digits, leaving the final multiplication $0.988065684\\ldots\\times0.998001=0.986090532\\ldots$ not fully checkable to the stated precision.",
      "fix": "Carry the intermediate products to full stated precision (e.g. 0.988065684566 and 0.986090532...) so every arithmetic step is exactly reproducible."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "Section 6 limitation (v) and Section 4.3 reconciliation both discuss the divergence with [11] at length but the paper never quantifies how sensitive the headline suppression factor is to the unresolved modelling detail",
      "reason": "The sensitivity is described only as a range ('would move between 100.2 and 166.9') without stating what modelling difference would produce each value.",
      "fix": "State explicitly which modelling difference (e.g. a different per-epoch definition or a different failure-event definition) would correspond to each endpoint of the range, or mark the range itself as a projection with stated assumptions."
    }
  ]
}
```