```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Abstract: \"the $(m,n) = (3,1)$ mode closes after $m = 3$ toroidal turns and admits $N = 13$ phase periods, for which $k L_{3,1} = 2\\pi N$\"; Section 4.2: \"The equality $kL_{3,1}=2\\pi N$ holds to machine precision, confirming the constructive-interference condition.\"",
      "reason": "Cross-section inconsistency and a circular derivation. Section 4.2 itself derives that the phase-accumulation and eigenvalue conditions do NOT coincide for this mode (\"the left side evaluates to $3\\times\\sqrt{13/9}\\times\\sqrt{1.027778}=3\\times1.201850\\times1.013794=3.655\\neq1$\"). Moreover, the geometric helix length from the paper's own metric is $L = 3 \\times 2\\pi\\sqrt{1 + 0.25/9} = 3 \\times 6.3701 = 19.110$ m, not 22.654 m; $k L_{\\text{geo}}/(2\\pi) = 3.605551 \\times 19.110 / 6.283185 = 10.97$, not the integer 13. The quoted length $L_{3,1} = 2\\pi N/k = 22.654$ m is defined circularly as the length that makes the phase condition hold, so \"holds to machine precision\" is a tautology, and the Abstract's claim that the (3,1) mode admits N=13 in-phase periods is contradicted by the paper's own arithmetic.",
      "fix": "Recompute the geometric helix length for (3,1) (19.110 m), report $kL_{\\text{geo}}/(2\\pi) = 10.97 \\notin \\mathbb{Z}$, and state in Abstract, Introduction and Results that the (3,1) eigenmode does NOT satisfy the integer phase-period condition; present $N=13$, $L=22.654$ m only as the hypothetical drive wavenumber/length pair that would satisfy $kL=2\\pi N$, clearly separated from the eigenmode value."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Section 4.1: \"A spectral degeneracy between distinct harmonics of the flat torus exists if and only if $A^2$ is rational.\"",
      "reason": "Only the 'only-if' direction is derived (degeneracy implies $A^2$ equals a ratio of integers). The 'if' direction — that rational $A^2 = p/q$ guarantees the existence of integers with $m'^2 - m^2 = (p/q)(n^2 - n'^2)$ — is never proven; the paper only exhibits two examples ($A^2=4$ and $A^2=2$), and a difference-of-squares argument shows the naive construction can fail (e.g. $pq \\equiv 2 \\pmod 4$), so the general claim is not established by what is shown.",
      "fix": "Either prove the 'if' direction with an explicit integer construction valid for all rational $A^2$, or weaken the headline statement to the proven direction ('degeneracy implies rational $A^2$') and label the converse a conjecture supported by the two worked examples."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Section 4.3: \"A tighter bound that accounts for the integer $m$ of the toroidal turns is $|\\Delta\\alpha|<\\frac{1}{2mN}$.\"",
      "reason": "This bound is asserted, not derived. The only derived inequality in the section is $2\\pi N|\\Delta\\alpha| < \\pi/2$, which yields $|\\Delta\\alpha| < 1/(4N)$; no step connects the toroidal turn count $m$ to the tolerance, so $1/(2mN)$ is a quantitative claim without shown arithmetic (and the Abstract and Results table propagate it).",
      "fix": "Either derive $1/(2mN)$ from a stated additional condition linking the phase error per toroidal turn to $m$, or replace the bound everywhere (Abstract, Section 4.3, Results, Section 7d) with the derived $|\\Delta\\alpha| < 1/(4N)$ and recompute the quoted tolerance."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Section 7(d): \"The tolerance $\\Delta\\alpha<1/(2mN)$ (Section 4.3) implies that for low-order rational windings ($m\\le 5$, $N\\le 20$) the aspect ratio must be controlled to better than $10^{-3}$.\"",
      "reason": "Arithmetic contradiction with the paper's own bound: for the worst case in the stated range, $1/(2 \\times 5 \\times 20) = 5 \\times 10^{-3}$, which is looser than $10^{-3}$, so 'better than $10^{-3}$' does not follow; the figure is neither derived nor labeled a projection.",
      "fix": "Recompute the tolerance over the stated parameter range (giving $5 \\times 10^{-3}$ at $m=5$, $N=20$) and state the correct bound, or restrict the claim to the case actually computed ($m=3$, $N=100$, $1.67 \\times 10^{-3}$)."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Section 7(d): \"High-resolution spectral solvers must resolve eigenvalue differences on the order of $10^{-6}$ m$^{-1}$ to detect degeneracies.\"",
      "reason": "The figure $10^{-6}$ m$^{-1}$ is stated with no derivation, no stated assumptions, and no projection label anywhere in the paper; Section 4 derives no eigenvalue-splitting scale.",
      "fix": "Either derive the required resolution from the degeneracy splittings the analysis actually predicts, or relabel the sentence as an explicit assumption/projection with its basis, or delete it."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Section 2: \"Their Brieskorn graph criterion — the link $L(\\mathbf{a})$ is homeomorphic to a sphere exactly when a graph built from the $\\gcd(a_i, a_j)$ satisfies one of two combinatorial conditions — is a clean instance of integer-arithmetic data selecting global geometric structure [3].\" and \"their construction of all toric 3-Sasakian manifolds in dimension 7 gave the first Einstein metrics on compact simply-connected manifolds with arbitrary second Betti number [3].\"",
      "reason": "The supplied text of [3] states only that the paper is \"a report on our joint work with János Kollár concerning the existence of an abundance of Einstein metrics on odd dimensional spheres, including exotic\"; the Brieskorn graph criterion, the dimension-7 toric 3-Sasakian construction, and the second Betti number claim are not derivable from what the entry states.",
      "fix": "Restrict the discussion of [3] to what its text states (abundance of Einstein metrics on odd-dimensional spheres, including exotic ones, via joint work with Kollár), or drop the unsupported specifics."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Section 4.3: \"$\\delta =\\alpha-\\frac{34}{55}=0.6180339887-0.6181818182=-1.477\\times10^{-4}$\"",
      "reason": "Arithmetic slip in a stated input: the difference is $-1.4783 \\times 10^{-4}$, not $-1.477 \\times 10^{-4}$; the downstream $\\Delta\\Phi = -0.0511$ rad is consistent with the correct value, so only the intermediate digit is wrong.",
      "fix": "Correct $\\delta$ to $-1.478 \\times 10^{-4}$ (or carry more digits) and confirm $\\Delta\\Phi = -0.0511$ rad."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Section 4.1, $A=\\sqrt{2}$ bullet: \"e.g. $(m,n) = (0,1)$, $(m',n') = (2,0)$: $4 - 0 = 2(1 - 0) = 2$? No: $4 \\neq 2$. Try $(m,n)=(1,1)$, $(m',n')=(3,0)$: ... Take $(m,n) = (3,3)$, $(m',n') = (9,0)$: ...\"",
      "reason": "Scratch-work residue (a chain of failed trial guesses with 'No:' interjections) is left in the body text; it reads as an unfinished search rather than a derivation and obscures the one valid example.",
      "fix": "Delete the failed trials and present only the valid degenerate pair $(m,n)=(1,5)$, $(m',n')=(7,1)$ with its check $49-1 = 48 = 2(25-1)$."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Section 4.2: \"\\]\\nis an integer: this additional integer phase-period condition selects...\"",
      "reason": "Broken display-math delimiter leaves a stray '\\]' and glues the closing of an equation to the following sentence.",
      "fix": "Repair the LaTeX so the equation closes cleanly and 'is an integer' begins a new sentence."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "Section 2, paragraphs on [8], [9], [10], [11] (e.g. \"it states a concrete falsifiable resonance condition for electron channeling, $d/v = \\pi\\hbar/(mc^2)$, together with an explicit table of falsification conditions [8]\").",
      "reason": "The QNFO works are characterized in specific detail, but no excerpt of these entries is available in this audit context, so agreement of the paper's use with what those works say could not be positively verified; no contradiction is evident from the paper's text itself.",
      "fix": "On revision, re-check each QNFO characterization ([8] resonance condition and falsification table; [9] $\\pi_1(S^1)\\cong\\mathbb{Z}$ and winding number as invariant; [10] Lyapunov contrast islands vs sea and scarred-state Poisson statistics; [11] GUE statistics of high zeta zeros near the $10^{20}$-th zero) against the works' own texts and keep only supported specifics."
    },
    {
      "id": "S5",
      "severity": "SOFT",
      "claim": "Section 4.2: \"$k^{2}= \\frac{m^{2}}{R^{2}}\\Bigl(1+\\alpha^{2}A^{2}\\Bigr) =\\frac{m^{2}}{R^{2}}\\Bigl(1+\\alpha^{2}\\frac{R^{2}}{r^{2}}\\Bigr) =\\frac{m^{2}}{R^{2}}\\Bigl(1+\\alpha^{2}\\frac{R^{2}}{r^{2}}\\Bigr)$\"",
      "reason": "The same expression is written twice identically in an apparent substitution chain, and the intermediate step does not show the substitution $A^2 = R^2/r^2$ being applied to $\\alpha^2 A^2$ in a distinguishable way.",
      "fix": "Write the chain as $\\frac{m^2}{R^2}(1+\\alpha^2 A^2) = \\frac{m^2}{R^2}\\left(1 + \\alpha^2 \\frac{R^2}{r^2}\\right) = \\frac{m^2 + n^2/r^2 \\cdot r^2}{R^2}$-style distinct steps, or remove the duplicated factor."
    }
  ]
}
```