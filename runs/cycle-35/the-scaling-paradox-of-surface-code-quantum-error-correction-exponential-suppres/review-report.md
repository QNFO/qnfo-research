```json
{
  "verdict": "pass",
  "hard": [],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Literature treatment of surface-code QEC itself (threshold fits, circuit-level noise simulations, decoder throughput results) is absent; the bibliography consists almost entirely of tangential analogies (cosmic distances, coronal field reconstruction, antihydrogen).",
      "reason": "The paper's central quantitative inputs (A=0.1, p_th=1e-2, n_tot=2d^2) rest on 'widely adopted' folklore with no citation to the actual QEC literature; the heterogeneous citations are used only as rhetorical analogies, which is a superficial treatment of the relevant field.",
      "fix": "Cite standard surface-code scaling/simulation literature (e.g. Fowler et al., Dennis et al., Google Quantum AI experiments) to source A, p_th, and the 2d^2 overhead convention, and demote the analogical citations to a short methodological note."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Step 8 compares a syndrome bit rate (1.62e14 bits/s) to the ATLAS pixel 'event rate' (4.0e7 s^-1), a dimensionally inconsistent ratio (bits/s vs events/s).",
      "reason": "The arithmetic is shown, but the yardstick conflates collision events with data volume; the honest ATLAS comparator is the pixel detector's data rate (~TB/s scale), which would change the headline 'four million times' figure.",
      "fix": "Re-express the comparison against ATLAS pixel readout data throughput in bits/s, or explicitly state that the ratio compares bits/s to events/s and is illustrative only."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "The phenomenological fit p_L = A(p/p_th)^((d+1)/2) with A=0.1 is used for all headline numbers despite being acknowledged as 'a crude approximation'.",
      "reason": "Circuit-level noise is known to alter both the exponent structure and effective threshold; the sensitivity analysis (Step 11) varies only A, not the threshold or the (d+1)/2 exponent, so the stated d_min=9 has unquantified model risk.",
      "fix": "Extend the sensitivity analysis to vary p_th (e.g. 5e-3 to 2e-2) and note the impact on d_min and n_tot, or cite circuit-level simulation results to justify the fit."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "The bandwidth reduction projection for bosonic codes (Step 10) assumes one readout channel per mode at unchanged cycle time.",
      "reason": "The projection is labeled as such, but the assumption that high-occupancy bosonic modes can be read out non-destructively at 1 MHz with single-channel bandwidth is unstated and nontrivial (e.g. GKP readout typically requires repeated photon counting).",
      "fix": "State the readout-time and measurement-backaction assumptions for the bosonic comparison explicitly, or mark the bandwidth-reduction projection as weaker than the photon-count projection."
    }
  ]
}
```