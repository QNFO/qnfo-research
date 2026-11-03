```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Abstract: 'The Koide ratio evaluates to $0.6665$, matching the exact value $2/3$ within experimental uncertainties'; Results table: 'Koide ratio $R_{\\text{Koide}}$ | $0.6665$ | Matches $2/3$ within $2.5\\times10^{-4}$ relative error'; Section 4.1: 'differs from $R_{\\text{Koide}}$ by $1.7\\times10^{-4}$'.",
      "reason": "Cross-section inconsistency and stale headline numbers. Section 6 (E.1) recomputes the ratio at full precision as 0.66665864 with deviation 8.03e-6 from 2/3, and explicitly states that the 1.7e-4 figure 'inherited the rounding of (4.5) and the addition slip in (4.8)'. The Abstract, Results table and Section 4.1 still carry the superseded value 0.6665 and the wrong deviation, so the paper contradicts itself between Abstract/Results and Section 6.",
      "fix": "Update the Abstract, the Results table row, and Section 4.1 to the corrected value R_Koide = 0.66665864 with deviation 8.03e-6 (relative 1.2e-5), or state in each location that the full-precision value of Section 6 supersedes the rounded one."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Section 4.1, Eq. (4.8): '$S_{m}=0.511+105.66+1776.86 = 1882.031$' and Eq. (4.9): '$R_{\\text{Koide}} = \\frac{1882.031}{2825.12} = 0.6665$'.",
      "reason": "Arithmetic error, doubled. First, 0.511+105.66+1776.86 = 1883.031, not 1882.031 (Section 6 E.1 itself flags this as an 'addition slip'). Second, even with the wrong numerator, 1882.031/2825.12 = 0.66619, not 0.6665; the quoted ratio does not follow from the quoted inputs by any arithmetic.",
      "fix": "Correct Eq. (4.8) to S_m = 1883.031 and recompute Eq. (4.9) from the actual inputs (full-precision value 0.66665864 per Section 6 E.1), so every headline number follows from shown arithmetic."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Abstract: 'the free‑streaming horizon is $0.014\\,\\text{pc}$'; Eq. (3.4): '$\\approx 0.014\\,\\text{pc}$'; Results table: '$4.2\\times10^{11}\\,\\text{m}\\;(0.014\\,\\text{pc})$'; Section 7.2: '$\\ell_{\\text{FS}}\\approx0.014\\,\\text{pc}$'; Conclusion: 'free‑streaming horizon ... placing the effect at the edge of LSST’s observational reach'.",
      "reason": "Cross-section inconsistency and unit-conversion error. Section 6 (E.3) converts 4.21546e11 m with 1 pc = 3.0857e16 m and obtains 1.3662e-5 pc, explicitly stating 'This corrects the value $0.014\\,\\text{pc}$ quoted in (3.4), (4.11), the Results table and Section 6.2 ... three orders of magnitude smaller'. The Abstract, Results, Section 7.2 and Conclusion still carry the wrong 0.014 pc.",
      "fix": "Replace 0.014 pc with 1.37e-5 pc (or 4.2e11 m) in the Abstract, Eq. (3.4), the Results table, Section 7.2 and the Conclusion, and remove or requalify the LSST-resolution comparison accordingly."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Heading '## 6. Extended Derivations and Worked Examples' followed by '## 7. Discussion', '## 8. Practical Implications and Engineering Pathways', '## 9. Conclusion'; Introduction contribution 5: 'practical pathways for experimental verification (Sections 7–7)'; Section 6 E.2: 'The falsifiability criterion of Section 6.2 states...'; Section 6 E.3: 'the falsification window of Section 6.2 shifts accordingly'.",
      "reason": "Required heading order violated (Discussion must be Section 6, Practical Implications Section 7, Conclusion Section 8) and broken cross-references: 'Sections 7–7' points at a non-existent range, and 'Section 6.2' points at a subsection that does not exist (the falsifiability criterion actually sits in Section 7.2).",
      "fix": "Renumber the sections to the required order (Discussion = 6, Practical Implications = 7, Conclusion = 8, with the extended derivations as an unnumbered or internally placed extension before the Discussion), and repair 'Sections 7–7' and every 'Section 6.2' reference to point at the section that actually contains the falsifiability criterion."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Section 2, item 3: '**Spectral asymptotics for Robin problems** show that the difference of resolvents of two elliptic realizations can be expressed via singular Green operators ([3], § 2). The techniques for handling discontinuous coefficients inspire our treatment of the non‑associative Dirac operator’s spectrum.'",
      "reason": "The supplied entry for [3] (arXiv:1009.0997v3) contains only the truncated opening 'The spectral behavio'; no statement about resolvent differences or singular Green operators is present in the supplied text, so the attribution is not derivable from the source as supplied.",
      "fix": "Either remove the sentence about [3], or restrict the claim to what the entry supports; if the full text of [3] is available to the pipeline, reinstate only the specific point its own sections state."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Section 2 items 4–8 and Section 6 E.5–E.8 attribute specific section-level results to [4], [5], [6], [7], [8], [9], [10], [11], [12] (e.g. '[4], § 2' decomposition into $m^{+}$ series with 'superpolynomial‑decay error', '[6], § 3.3' Spin(9)-invariant valuations, '[7], § 1' torsion as Lorentz vector, '[9], § 11' five named inputs, '[10] Theorem 1/Theorem 2', '[11] § 5 R1/R2' with $p_{\\text{joint}}=4.194304\\times10^{-27}$ and $\\lambda_{\\text{tree}}=1.008652$, '[12] § II.A, § V').",
      "reason": "The supplied excerpts cover only [1], [2] and a truncated [3]; for [4]–[12] no full-text sections are available in the audit context, so each of these specific attributions (methods, theorems, numbers, quoted phrases) cannot be verified against the works' own text as required. This includes the QNFO works [9]–[12]: the paper's use of their conclusions, falsification records and scope statements cannot be confirmed and must not stand unverifiable.",
      "fix": "For every citation of [4]–[12], retain only statements that the corresponding entry's own sections state; where the entry supplies no such detail, delete the attribution or reduce the citation to nothing. Re-verify each QNFO claim ([9] five-input scope, [10] relative-consistency theorems, [11] p_joint and Efimov falsification numbers, [12] four-sector critique) against that work's actual text before keeping it."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Section 8(e): 'Assuming a symbolic‑algebra implementation costing \\$150 k in development time and \\$30 k in compute resources, the total projected expense is approximately \\$180 k (projection, based on typical software‑engineering rates).'",
      "reason": "Invented cost figures. Neither \\$150 k nor \\$30 k is derived anywhere in the paper, and the stated assumption ('typical software‑engineering rates') names no source or derivable input; the sum 150+30=180 is trivially consistent but its inputs are fabricated.",
      "fix": "Remove the cost projection, or restate it with every input either derived in Section 4 or cited, with assumptions and uncertainty bounds explicitly listed."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Section 1: 'the SM requires more than two‑hundred free numerical inputs'; Section 5 table: 'Near LSST small‑scale resolution limit'; Section 8(a): 'refine forecasts for LSST and low‑frequency gravitational‑wave experiments'; Section 9: 'within low‑frequency gravitational‑wave search bands'.",
      "reason": "Claims about the outside world (the count of SM parameters, LSST's resolution characteristics, low-frequency gravitational-wave detector bands) that are stated nowhere in the grounding or bibliography and are not computed in the paper.",
      "fix": "Either source these claims from the bibliography or restate them as the paper's own assumptions ('We assume ...'), or delete the specific figures (e.g. the two-hundred count) and keep only the qualitative parameter-proliferation problem."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Section 4.1: 'well within the experimental uncertainties of $m_{\\tau}$'.",
      "reason": "No experimental uncertainty value for m_tau is stated or cited anywhere in the paper, so the comparison to uncertainties is unsubstantiated.",
      "fix": "State the assumed or cited uncertainty on m_tau, or rephrase as a purely numerical deviation."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Section 4.3 / Results table: 'guaranteeing a non‑trivial spectral gap needed for the resonance condition' from the bound $\\|T\\|/8 \\le w_{\\mathbb{O}}(T)$.",
      "reason": "The inequality of [2] is proved for finite octonionic matrices $T\\in M_n(\\mathbb{O})$; the paper applies it to an unbounded Dirac operator and infers a spectral gap, an inference the cited theorem does not deliver.",
      "fix": "State the finite-dimensional restriction and present the gap claim as a conjecture or assumption, not as guaranteed."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Section 1: 'The framework may also impact quantum‑information engineering (through the joint‑tree conjecture) and parameter‑free machine‑learning encoders'.",
      "reason": "Speculative applications with no derivation or grounding in the paper; the link to [8] (relational-database encoders) and to [11] is asserted, not shown.",
      "fix": "Delete or explicitly label as ungrounded speculation."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "Section 3.5: '$a_{\\text{eq}}\\approx1/3400$', the masses of Eq. (4.4), and the constants $h$ and $hc$ are used without provenance.",
      "reason": "Physical constants and measured masses enter the derivations as bare numbers with no source or explicit assumption label.",
      "fix": "Label each as an assumed input ('We assume ...') or cite a source for each."
    },
    {
      "id": "S5",
      "severity": "SOFT",
      "claim": "The term 'autaxys' is used from the Abstract onward but is never defined beyond the parenthetical '(self‑consistency)'.",
      "reason": "Unexplained jargon for an adjacent-field reader.",
      "fix": "Define the term once, explicitly, at first use."
    }
  ]
}
```