```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Heading '## 7. Extended Derivations and Worked Examples' (second occurrence), '## 9. Practical Implications and Engineering Pathways', '## 10. Conclusion'",
      "reason": "Required structure demands '## 7. Practical Implications and Engineering Pathways' as Section 7 and Conclusion as Section 8. The paper instead places a second section headed 'Extended Derivations and Worked Examples' at position 7 (duplicating the Section 6 heading verbatim), renumbers Practical Implications to 9 and Conclusion to 10, so the required heading order is violated and two sections share an identical title.",
      "fix": "Renumber: merge or retitle Sections 6 and 7 distinctly, make Practical Implications Section 7 and Conclusion Section 8, and update the Introduction contributions list ('Section 9', 'Section 8') to the corrected numbers."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "'## References' lists [1]–[6] (six entries)",
      "reason": "The References section contains fewer than 8 entries, and the Discussion nowhere states the limitation that the cited literature set is smaller than the required minimum.",
      "fix": "State explicitly in Section 8 (Discussion) that the paper cites only the six available works and that the literature treatment is limited accordingly; do not invent additional references."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "'Existence of prime‑specific phase transitions analogous to the p‑adic Potts model result [3] in radiative equilibrium.' and 'The analysis rests on the geometric weighting postulate of Section 3.3 and on ultrametric embedding and extension theorems [2], [5].'",
      "reason": "[3] is cited only for existence/framing with no specific point from its text, and [5] appears only in a bundled Conclusion citation with no stated content anywhere in the paper. Both are bare citations.",
      "fix": "Either discuss [3] and [5] through specific statements their texts make (e.g., what the distinction-based ultrametric constructs and tests; what the p-adic metrology proposal claims), or delete the citations and rephrase without them."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Section 9(e): 'amounting to a **10 %** relative excess near \\(\\nu\\approx 10^{15}\\) Hz. This figure follows directly from the analytic expression for \\(B_\\nu(p)\\) and the known Planck value at that frequency.'",
      "reason": "Section 7 (E.2) explicitly withdraws this figure: 'The earlier 10 % figure is therefore withdrawn as unsupported.' The two passages contradict each other, and the 10 % number is neither derived with shown arithmetic nor labeled a projection with stated assumptions.",
      "fix": "Delete the 10 % claim from Section 9(e) and replace it with the frequency-dependent relative excess R(ν) = (e^{βhν}-1)/(p-1) - 1 derived in E.2, noting R(ν₀)=0 at βhν₀=ln p and R(2ν₀)=p."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Section 5.5: 'For a temperature \\(T=3000\\) K, \\(P_{\\text{SB}}\\approx4.6\\times10^{5}\\,\\text{W·m}^{-2}\\). The ultrametric projection therefore predicts a radiated power roughly three orders of magnitude larger'",
      "reason": "Arithmetic error in a headline comparison: with σ=5.67×10⁻⁸ and T⁴=(3000)⁴=8.10×10¹³, P_SB=4.59×10⁶ W·m⁻², not 4.6×10⁵. The paper's own Section 7 (E.1) corrects this to 4.59×10⁶ and a ratio of about 4.0×10², so Section 5.5 and E.1 contradict each other.",
      "fix": "Correct Section 5.5 to P_SB ≈ 4.59×10⁶ W·m⁻² and state the ratio as approximately 4.0×10² (between two and three orders of magnitude), matching E.1."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Section 7 E.1: 'not \"roughly three orders of magnitude\" with \\(P_{\\text{SB}}\\approx4.6\\times10^{5}\\,\\text{W·m}^{-2}\\) as previously stated. The earlier figure under-counted \\(T^{4}\\) by one power of ten' and E.2: 'Section 7(e) previously quoted a \"10 % relative excess\"... The earlier 10 % figure is therefore withdrawn as unsupported.'",
      "reason": "Meta-commentary about the paper's own earlier draft state ('as previously stated', 'The earlier figure', 'previously quoted', 'withdrawn'). The reconciled preprint must present one consistent voice, not narrate its own revisions.",
      "fix": "Rewrite E.1 and E.2 as direct derivations stating the corrected values (P_SB = 4.59×10⁶ W·m⁻², ratio ≈ 4.0×10²; R(ν) frequency-dependent with R(2ν₀)=p), removing all references to earlier or withdrawn figures."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Section 3.2: 'Detailed balance then forces the stationary probability \\(\\pi_n\\) to be constant within each ball \\(\\mathcal{B}_{p^{-k}}\\), i.e. \\(\\pi_n\\) depends only on \\(v_p(n)\\).'",
      "reason": "This contradicts the paper's own distribution π_n = (1-1/p)p^{-n} of Section 3.3, which depends on n itself, not only on v_p(n): for p=3, π_1=(2/3)/3 and π_4=(2/3)/81 differ although v_3(1)=v_3(4)=0, so π is not constant within the ball B_{1/3}.",
      "fix": "Delete or correct the detailed-balance claim so the stationary distribution stated is the geometric one of Section 3.3; if a ball-constancy property is wanted, derive it explicitly or drop it."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Section 5.4: 'An analytic subgroup argument states that a p‑adic analytic subgroup of a commutative algebraic group contains a non‑trivial algebraic point if and only if it contains a non‑trivial algebraic subgroup.' and 'the stationary Markov kernel on the ultrametric space \\(\\mathbb{U}\\) (Section 3.2) defines a p‑adic analytic subgroup of the space of probability measures.'",
      "reason": "The theorem is stated with no citation, and the translation ('the Markov kernel defines a p-adic analytic subgroup of the space of probability measures') is an unsupported claim about the outside world; neither is derivable from any cited work or computed in the paper.",
      "fix": "Either cite a work from the References that states the analytic-subgroup result and justify the translation from its text, or remove Section 5.4 and relabel the uniqueness question as an open question in Section 8."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Section 2 closing: 'These works collectively supply the mathematical foundation (ultrametric embeddings, Markov dynamics, p‑adic geometry) and the statistical‑mechanical bridge (maximum‑entropy ↔ Bose–Einstein) required for the present analysis.'",
      "reason": "No cited work is shown to supply 'Markov dynamics' or a 'maximum-entropy ↔ Bose–Einstein bridge'; this attributes content to the cited set that its entries do not state, and bundles works as collective framing.",
      "fix": "Replace with per-work statements of what [1] and [2] actually prove, and state the Markov and maximum-entropy ingredients as this paper's own modeling assumptions."
    },
    {
      "id": "H10",
      "severity": "HARD",
      "claim": "Section 7 E.3: 'the derived upper bounds are \\(\\varepsilon_p<2.5\\) at 95 % CL for every radix... the bispectrum bound is about \\(830\\) times weaker than the two-point bound \\(A_{\\mathrm{LPO}}<3\\times10^{-3}\\)... only the \\(p=2\\) radix is cleanly identifiable at Planck resolution' and E.4: '[6] argues that the renormalization group and harmonic quantum mechanics share a mathematical isomorphism... identifies as its first pillar the exact correspondence between the equally spaced oscillator spectrum... and Wilson's integration of a momentum shell [Λ/b, Λ]'",
      "reason": "These specific numbers and characterizations attributed to [4] and [6] cannot be verified against the supplied text of those works; statements about what a cited work found must be derivable from that work's own text.",
      "fix": "Retain only statements about [4] and [6] that their supplied texts support; for the unverifiable numbers (ε_p bounds, factor 830, A_LPO bound, identifiability claim, isomorphism details) either source them from the works' texts or remove the sentences."
    },
    {
      "id": "H11",
      "severity": "HARD",
      "claim": "Section 9(d): '**Spectral resolution**: Must resolve differences of order \\(10^{-2}\\) W·m^{-2}·sr^{-1}·Hz^{-1}.',
      "reason": "This resolution requirement is neither derived in the paper nor labeled a projection with stated assumptions; the only computed radiance is B_ν(3)=9.20×10⁻⁷ W·m⁻²·sr⁻¹·Hz⁻¹ at ν=5×10¹⁴ Hz, which is inconsistent with a 10⁻² requirement.",
      "fix": "Either derive the required resolution from the computed radiance values and the claimed excess R(ν), or relabel the figure as an assumed design target with stated assumptions."
    },
    {
      "id": "H12",
      "severity": "HARD",
      "claim": "Section 5: 'Hence \\[ B_\\nu(p)=\\frac{2h\\nu^{3}}{c^{2}}\\;\\frac{1}{p-1}, \\] showing that the ultrametric occupation factor removes the exponential suppression, so the spectral radiance scales as \\(\\nu^{3}/(p-1)\\) without any exponential decay.'",
      "reason": "This frequency-independent occupation factor contradicts the paper's own E.2, which shows the two laws agree only at the single frequency βhν₀=ln p and that the relative excess R(ν)=(e^{βhν}-1)/(p-1)-1 is frequency-dependent and grows without bound. Presenting 1/(p-1) as the occupation factor at all ν is internally inconsistent.",
      "fix": "State in Section 5 that the algebraic form holds under the fugacity identification at the reference frequency (or as the high-frequency asymptotic assumption of the model), and cross-reference the frequency-dependent R(ν) treatment so the two passages agree."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Section 2 contains two near-identical bullets beginning 'Ultrametric spaces admit isometric embeddings and extensions: [2] proves...'",
      "reason": "Duplicate bullet restating the same citation adds no content and suggests unreconciled text.",
      "fix": "Merge the two bullets into one statement of what [2] proves and how it is used."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Abstract: 'requiring an explicit frequency cutoff to avoid divergence, but the total radiated power still diverges, so an explicit frequency cutoff remains necessary.'",
      "reason": "Redundant double statement of the cutoff requirement weakens the abstract.",
      "fix": "Keep one statement: the tail grows as ν³ and a cutoff ν_max is required for finite total power."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Section 6 E.1 uses 'first Zagreb index' and '4-tree' without definition at first use; 'fugacity' in Section 3.3 is used before any explanation.",
      "reason": "Unexplained jargon for an adjacent-field reader.",
      "fix": "Define M_1 = Σ d(v)² at first use and gloss fugacity as the exponential weight parameter z = e^{-βhν}."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "Conclusion: 'Immediate experimental falsification is feasible with existing spectroscopic equipment.'",
      "reason": "An unsupported feasibility claim about equipment the paper does not specify or derive requirements for.",
      "fix": "Soften to a conditional proposal referencing the Section 7(c) experiment design and its stated resolution and stability requirements."
    }
  ]
}
```