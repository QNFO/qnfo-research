{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Step 6: continuous‑optimum bracket. ... $0.7^{K}\bigl(0.0356675\,K+0.456675\bigr)=0.1$.",
      "reason": "The constant term 0.456675 is incorrect; it should be $0.3566749$ (i.e., $-\ln\\alpha$). This arithmetic error invalidates the subsequent claim that the continuous optimum lies between $K=5$ and $K=6$.",
      "fix": "Replace the equation with $0.7^{K}\\bigl(0.0356675\\,K+0.3566749\\bigr)=0.1$ and recompute the left‑hand side for $K=5$ and $K=6$ to determine the correct interval for the continuous optimum."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Section 3.1 cites \"moment‑based ensemble‑control literature [6]\" and \"ensemble control on Lie groups [8]\" as supporting background.",
      "reason": "No excerpt for references [6] or [8] is provided in the bibliography; therefore the statement cannot be verified against the supplied source text, violating citation integrity.",
      "fix": "Remove or rephrase the sentence to avoid citing [6] and [8] unless a supporting excerpt is added; alternatively replace with a statement that does not require external citation."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Section 3.3: \"Following the spanning‑set design principle of [7] — a basis in which each element is matched to exactly one problem region while the remainder stays finite — we assign each drafter to cover a distinct region...\"",
      "reason": "No excerpt for reference [7] is supplied; the claim about the spanning‑set principle cannot be derived from the provided source, violating citation integrity.",
      "fix": "Delete the reference to [7] and instead describe the drafter specialization without attributing it to an unsupported source."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Section 3.4: \"This contrasts with verification frameworks that must prove well‑foundedness explicitly, as in the constructive consistency proof of [3].\"",
      "reason": "No excerpt for reference [3] is supplied; the claim about the constructive consistency proof cannot be verified, violating citation integrity.",
      "fix": "Remove the citation to [3] or replace it with a statement that does not rely on an unsupported source."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Section 3.5: \"As a control‑theoretic abstraction, consider the linear broadcast‑controlled ensemble ...\" (no citation needed) but the discussion of Vandermonde controllability is linked to \"the spanning‑set principle of [7]\" earlier, which is unsupported.",
      "reason": "The earlier unsupported citation propagates into this section, making the justification for the Vandermonde analysis ungrounded.",
      "fix": "Ensure that any reference to external works in this section is supported by supplied excerpts; otherwise remove the citation."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Section 2: \"[3] ... shows that higher pseudo‑label classification accuracy does not necessarily translate into better downstream performance and that scaling the ZUPT covariance reduces drift.\"",
      "reason": "No excerpt for reference [3] is provided; the described findings cannot be verified, violating citation integrity.",
      "fix": "Delete or replace the statement with content that can be directly supported by the supplied excerpts for [3], or remove the citation."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Section 2: \"[4] ... addresses contact detection for legged odometry, showing that higher pseudo‑label classification accuracy does not necessarily translate into better downstream performance and that scaling the ZUPT covariance reduces drift.\"",
      "reason": "No excerpt for reference [4] is provided; the claim cannot be verified against the supplied source text.",
      "fix": "Remove the citation to [4] or replace the sentence with a verifiable claim based on provided excerpts."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Section 2: \"[5] ... analogous to the parity and harmonic‑number decoupling of perturbation modes in [5].\"",
      "reason": "No excerpt for reference [5] is supplied; the analogy cannot be verified, violating citation integrity.",
      "fix": "Delete the citation to [5] or rephrase the sentence without attributing the claim to an unsupported source."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Section 2: \"[9] ... we adopt the same practice by listing assumptions A1–A4 in a table‑like form, ensuring transparent grounding of our analytical model.\"",
      "reason": "No excerpt for reference [9] is provided; the claim about its practice cannot be verified, violating citation integrity.",
      "fix": "Remove the citation to [9] or replace the sentence with a description that does not rely on an unsupported source."
    },
    {
      "id": "H10",
      "severity": "HARD",
      "claim": "Section 6: \"whether the multi‑axis evaluation style of [10] can be operationalized for drafting ensembles...\"",
      "reason": "No excerpt for reference [10] is supplied; the statement cannot be verified against the source, violating citation integrity.",
      "fix": "Delete the citation to [10] or rephrase the open question without referencing an unsupported source."
    }
  ],
  "soft": []
}