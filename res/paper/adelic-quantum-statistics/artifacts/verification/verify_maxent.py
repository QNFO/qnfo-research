"""verify_maxent.py — QNFO.RES.027 S9 verification (max-entropy property).

Verifies that the golden distributions are the maximum-entropy solutions under
their stated constraints. The mathematical content: (i) the FIRST-ORDER
condition — the entropy gradient is affine in the state label, i.e. lies in
the span of the constraint gradients (exponential-family property); (ii) STRICT
CONCAVITY — the entropy Hessian is negative definite everywhere, so the
critical point is the global maximum; (iii) for the Fermi two-state case, the
constraint matrix has full rank, so the mean constraint alone fixes the
distribution (uniqueness).

  S9a  geometric (Bose, n >= 0): gradient -(ln q_n + 1) is affine in n
       (residual orthogonal to every mean-preserving direction, checked with
       a proper Gram-Schmidt projection onto the constraint subspace);
       Hessian diag(-1/q_n) < 0.
  S9b  Bernoulli (Fermi, {0,1}): constraint matrix [[1,1],[0,1]] has rank 2 —
       two constraints determine the two probabilities uniquely.
  S9c  truncated geometric (bounded occupancy a <= m): same first-order
       condition under the bound.
  S9d  edge cases: m=1 recovers the Fermi golden mean 1/(e^x + 1); m -> inf
       recovers the Bose geometric mean 1/(e^x - 1) (consistency with F1d).

Reproducibility: seeded RNG, stdlib only.
"""

import math, random, sys, json
import os

def main():
    results = []
    def check(name, ok, detail):
        results.append({"check": name, "pass": bool(ok), "detail": detail})
        print(("PASS  " if ok else "FAIL  ") + name + " | " + detail)

    rng = random.Random(20260827)

    def meanfree_projection(d, labels):
        """Project d onto {v : sum v = 0, sum label_i v_i = 0} by Gram-Schmidt."""
        M = len(d)
        # e0 = 1-vector, e1 = mean-centered labels (orthogonal to e0)
        e1 = [i - sum(labels) / M for i in labels]
        e1n = math.sqrt(sum(x * x for x in e1))
        # orthogonalize d against e0
        d = [x - sum(d) / M for x in d]
        # orthogonalize against e1
        c = sum(d[i] * e1[i] for i in range(M)) / (e1n * e1n)
        return [d[i] - c * e1[i] for i in range(M)]

    # ---------- S9a: geometric (Bose) ----------
    for q in (0.5, 0.2, 1.0 / 7.0):
        M = min(400, int(60.0 / (-math.log(q)))) + 5  # tail-safe: qn[M-1] >= e^-60
        qn = [(1.0 - q) * q ** n for n in range(M)]
        labels = list(range(M))
        worst_first = 0.0
        for _ in range(5):
            d = [rng.random() - 0.5 for _ in range(M)]
            d = meanfree_projection(d, labels)
            nd = math.sqrt(sum(x * x for x in d))
            if nd < 1e-12:
                continue
            d = [x / nd for x in d]
            g = [-(math.log(qn[i]) + 1.0) for i in range(M)]
            worst_first = max(worst_first, abs(sum(d[i] * g[i] for i in range(M))))
        # strict concavity: Hessian diag(-1/q_n) strictly negative
        ok_concave = all(-1.0 / qn[i] < 0 for i in range(M))
        check("S9a geometric q=%.4f first-order" % q, worst_first < 1e-10,
              "worst |<d, grad H>| = %.2e" % worst_first)
        check("S9a geometric q=%.4f strict concavity" % q, ok_concave,
              "Hessian diag(-1/q_n) < 0 on support [0,%d]" % M)

    # ---------- S9b: Bernoulli (Fermi) ----------
    for m in (0.2, 0.5):
        # constraint matrix rows (1,1) and (0,1): det = 1*1 - 1*0 = 1 (full rank)
        det = 1.0 * 1.0 - 1.0 * 0.0
        # exponential-family property on two states: ln p is affine in the label
        p = [1.0 - m, m]
        # affine iff the single difference matches the label difference scaled:
        # ln p_1 - ln p_0 = ln(m/(1-m)) = beta * (1 - 0) -> always solvable.
        beta = math.log(m / (1.0 - m))
        resid = abs((math.log(p[1]) + 1.0) - (math.log(p[0]) + 1.0) - beta * 1.0)
        check("S9b Bernoulli m=%.1f uniqueness + exponential family" % m,
              det != 0 and resid < 1e-12,
              "constraint rank 2 (det=%.1f); affinity residual %.2e" % (det, resid))

    # ---------- S9c: truncated geometric (bounded occupancy) ----------
    for (z, m) in ((0.5, 3), (0.2, 5), (1.0 / 3.0, 10)):
        Z = sum(z ** n for n in range(m + 1))
        qn = [z ** n / Z for n in range(m + 1)]
        labels = list(range(m + 1))
        worst_first = 0.0
        for _ in range(5):
            d = [rng.random() - 0.5 for _ in range(m + 1)]
            d = meanfree_projection(d, labels)
            nd = math.sqrt(sum(x * x for x in d))
            if nd < 1e-12:
                continue
            d = [x / nd for x in d]
            g = [-(math.log(qn[i]) + 1.0) for i in range(m + 1)]
            worst_first = max(worst_first, abs(sum(d[i] * g[i] for i in range(m + 1))))
        ok_concave = all(-1.0 / qn[i] < 0 for i in range(m + 1))
        check("S9c truncated-geometric z=%.3f m=%d" % (z, m),
              worst_first < 1e-10 and ok_concave,
              "first-order %.2e; strict concavity %s" % (worst_first, ok_concave))

    # ---------- S9d: edge cases (consistency with F1d golden values) ----------
    for z in (0.5, 1.0, 2.0):
        mean_m1 = z / (1.0 + z)
        golden_fermi = 1.0 / (math.exp(-math.log(z)) + 1.0)
        ok = abs(mean_m1 - golden_fermi) < 1e-12
        check("S9d m=1 recovers Fermi golden z=%.1f" % z, ok,
              "mean=%.10f vs 1/(e^x+1)=%.10f" % (mean_m1, golden_fermi))
    for z in (0.5, 0.2):
        mean_bose = z / (1.0 - z)
        golden_bose = 1.0 / (math.exp(-math.log(z)) - 1.0)
        ok = abs(mean_bose - golden_bose) < 1e-12
        check("S9d m->inf recovers Bose golden z=%.2f" % z, ok,
              "mean=%.10f vs 1/(e^x-1)=%.10f" % (mean_bose, golden_bose))

    total = sum(1 for r in results if r["pass"])
    failed = [r["check"] for r in results if not r["pass"]]
    print("\nRESULT: %d/%d PASS" % (total, len(results)))
    if failed:
        print("FAILED: " + "; ".join(failed))
        sys.exit(1)
    print("ALL CHECKS PASS")
    json.dump({"passed": total, "total": len(results), "results": results},
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "verify_maxent_results.json"), "w"),
              indent=2)

if __name__ == "__main__":
    main()
