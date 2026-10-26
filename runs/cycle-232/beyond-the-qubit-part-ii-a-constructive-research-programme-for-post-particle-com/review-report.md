[
  {
    "find": "per-frame bias must be below $10^{-4}$ m to keep linear drift under the gate within a minute.",
    "replace": "If the per-frame bias were $10^{-4}$ m, the linear drift over one minute would be $3.6$ m, which exceeds the admissibility gate; this illustrates the sensitivity of the drift bound to bias magnitude (a projection based on the assumptions of Section 4.4)."
  },
  {
    "find": "a tracker update rate of at least $720$ Hz is required (derived from $\\theta_{\\mathrm{sample}}=\\omega/f_t$).",
    "replace": "Achieving an inter‑sample angular travel of $0.5^\\circ$ at $\\omega=360\\ \\mathrm{deg/s}$ would require a tracker update rate of $f_t = \\omega/0.5^\\circ = 720\\ \\mathrm{Hz}$ (a projection based on the angular‑travel formula in Section 4.5)."
  },
  {
    "find": "The paper’s statement that anchoring error is the fundamental per‑frame quantity is the basis for the drift model in Section 4.4; the reported frame rate informs the discussion of required tracker bandwidth in Section 4.5.",
    "replace": "The drift model in Section 4.4 treats anchoring error as a per‑frame quantity, following the modeling approach of the instant motion tracking work [6]; the frame‑rate value $f=60$ Hz from that work is used in the bandwidth discussion of Section 4.5."
  }
]