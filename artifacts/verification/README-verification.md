# Verification Suite README — adelic-quantum-arithmetic (QNFO.RES.029)

- **Script:** `sim-adelic-quantum-arithmetic-verification.py` (in this directory)
- **Environment:** Python 3, standard library only (no third-party dependencies), no random seeds — the run is fully deterministic.
- **Run (from the repository root):**

      python artifacts/verification/sim-adelic-quantum-arithmetic-verification.py artifacts/verification/verification-output.json

  In the flat Zenodo deposit the same files live at the top level: `python sim-adelic-quantum-arithmetic-verification.py` — the output path defaults to the script's own directory, so the deposit layout and the repository layout both work without changes.

- **Measured run (2026-08-27):** 18/18 checks pass; runtime 1.77 s (consumer laptop, Windows 11, CPython 3.x). Sieve depth: 2,000,000 primes; sum depth: 2,000,000 integers.
- **Output contract:** `verification-output.json` carries a summary (total / passed / failed / runtime) and one entry per check with the fields `check`, `value`, `expected`, the relevant error bound, its `tolerance`, and `pass`.
- **Checks:**
  - C1 Euler product of the zeta function at s = 2 versus pi^2/6
  - C2 squarefree Dirichlet series versus zeta(2)/zeta(4) = 15/pi^2
  - C3 squarefree density versus 6/pi^2
  - C4 Moebius inversion sum mu(n)/n^2 versus 1/zeta(2)
  - C5 occupation golden values at fugacity 1/p (exact rational arithmetic)
  - C6 canonical-derivative occupation (exact rational arithmetic)
  - C7 Gentile cap-m Euler factors versus finite geometric sums
  - C8 bounded-occupation factor at m = 1 versus the fermionic mode factor
  - C9 Laughlin phase at filling 1/m as a primitive 2m-th root of unity
  - C10 Fibonacci eigenvalues e^{i pi/5} as tenth roots of unity
- **Tolerances:** stated per check in the output file (analytic truncation bounds: Euler-product and series tails bounded by the sieved depth).
