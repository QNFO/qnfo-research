```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Section 2: \"Landauer's principle, stating that erasing a bit at temperature $T_{\\mathrm{env}}$ costs at least $E_{\\mathrm{bit}}=k_{B}T_{\\mathrm{env}}\\ln2$, is presented in [7] as a bound on the energy consumption of distinction maintenance.\" Also \"[8] analyzes the energy complexity of regular languages, providing bounds that are relevant to the cost of maintaining binary distinctions over a finite state space\" and \"The finite-distinction program defining admissible existence claims and deriving combinatorial and thermodynamic bounds is described in [10]\". Section 1 and Section 7(a) also cite \"[8]\" for decentralization ontology work.",
      "reason": "References [7], [8] and [10] are cited in the body but do not exist in the bibliography or in the '## References' list (which contains only [1]-[6]). They are invented references. Additionally, two unrelated topics (regular-language energy complexity and decentralization definitional fragmentation) are attributed to the same nonexistent [8].",
      "fix": "Delete every sentence citing [7], [8] or [10], or restate the content as the paper's own assumption/derivation (Landauer's principle is already derived in Section 4.3 from $k_B$, $T$ and $\\ln 2$ and needs no citation). Remove the [8] citations from Section 1 contribution 5 and Section 7(a)."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Section 2: \"[2] defines \\\"operator-blindness\\\" and proves (Prop. 1) that generic top-1 ranking cannot detect mismatched physical operators, while introducing a contrastive learning objective (Prop. 2) that makes the failure observable.\"",
      "reason": "Reference [2] is the DRHBc nuclear mass table (arXiv:2402.02935v4). Nothing in its supplied text mentions operator-blindness, top-1 ranking, physical operators, or contrastive learning; the attribution contradicts the actual content of the cited work.",
      "fix": "Delete the sentence, or rewrite the re-entry-mismatch point as the paper's own observation without attributing propositions to [2]."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Section 2: \"[5] discusses the role of primitive ontology in quantum foundations and argues that ontological clarity is required for theoretical frameworks.\"",
      "reason": "Reference [5] is the ignorance-audit paper on AI-assisted science. Its supplied title and text say nothing about primitive ontology or quantum foundations; the attribution contradicts the cited work's subject matter.",
      "fix": "Delete the sentence; the paper's premise that existence claims should be explicit can stand as the paper's own premise without citation."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Section 2 makes specific content attributions to [3], [4], [5] and [6] that are not supported by any supplied text of those works, e.g.: \"if measuring a quantity $Q$ to precision $\\varepsilon$ requires $\\mu(-\\log_{2}\\varepsilon)$ steps and each step costs $E$ joules, the total energy is $E\\cdot\\mu(n)$\" ([3]); \"Its central claim---that a pipeline cannot govern what it cannot see---... records a case in which a flagship paper produced inside an AI-assisted pipeline was separately identified as AI-generated through structural markers and synthetic citation anchors\" ([5]); \"That work's cross-domain analysis finds the same structural dynamic... Its red-team finding R5---that neither the finite-precision program nor the closure framework has produced a differential empirical prediction\" ([6]); \"The errata paper [4] corrects two load-bearing sentences... an erratum that silently rewrote more than the flagged sentences would itself introduce unverifiable content\" ([4]).",
      "reason": "No full text, abstract or excerpt of [3], [4], [5] or [6] is available to verify these specific methods, findings, numbered results or arguments; per the source-support rule, statements about what a cited work did or found must be derivable from that work's supplied entry. Only the titles of these works are verifiable.",
      "fix": "Restrict statements about [3]-[6] to what their titles state (e.g., [3] concerns when a physical quantity is computationally real; [4] is two errata correcting a Godel-completeness attribution and a flatness-to-zero-energy inference; [5]