#!/usr/bin/env python3
"""RQ3 computational verification - QNFO.RES.022 Phase 4 (fixed v2).

Numeric check of the Archimedean-limit hypothesis (H2) on a toy ultrametric
model with an EXPLICIT averaging operation:

  Model: complete b-adic tree of depth D (leaves 0..b**D-1); the tree metric
  is the b-adic valuation distance d(i,j) = b^{-v_b(|i-j|)} (prime-valuation-
  depth object: shared trailing digits = shared low-order branches; this is
  the same construction as the program's b-adic valuation records). Leaves
  carry iid values x_i ~ N(0, sigma^2). The ergodic mean over leaves is the
  arithmetic mean of the n = b**D leaf values; by CLT its distribution is
  N(0, sigma^2/n) as D -> oo - the Archimedean limit object.

Checks (all seeded, deterministic):
  1. ultrametric inequality: d(i,k) <= max(d(i,j), d(j,k)) on 10k random
     triples (violations must be 0 - exact for the b-adic metric).
  2. golden value: var(mean) == sigma^2 / n (empirical over 2,000
     repetitions, relative error < 5%; the sampling error of the empirical
     variance at 2,000 reps is ~3.2% at 1 sigma, so 5% is a ~1.6 sigma bound).
  3. Gaussianity of the averaged quantity: |skew| < 0.15, |excess kurtosis|
     < 0.25 (finite-sample thresholds for n_reps=2000, ~3 sigma).
  4. b-adic valuation goldens: v_2(12)=2, v_2(8)=3, v_3(18)=2, v_5(100)=2.
"""
import json
import math
import random
import sys

SEED = 20260823
rng = random.Random(SEED)
OUT = sys.argv[1] if len(sys.argv) > 1 else "artifacts/verification/rq3_results.json"


def v_p(n, p):
    n = abs(int(n))
    v = 0
    while n and n % p == 0:
        n //= p
        v += 1
    return v


def tree_metric(i, j, p):
    """b-adic (p-adic) ultrametric tree distance d(i,j) = p^{-v_p(|i-j|)}."""
    if i == j:
        return 0.0
    return p ** (-v_p(abs(i - j), p))


def check_ultrametric_inequality(p, D, n_triples=10000):
    leaves = list(range(p ** D))
    violations = 0
    for _ in range(n_triples):
        i, j, k = rng.sample(leaves, 3)
        d_ik = tree_metric(i, k, p)
        d_ij = tree_metric(i, j, p)
        d_jk = tree_metric(j, k, p)
        if d_ik > max(d_ij, d_jk) + 1e-12:
            violations += 1
    return violations


def check_clt(p, D, sigma=1.0, n_reps=2000):
    n = p ** D
    means = []
    for _ in range(n_reps):
        xs = [rng.gauss(0.0, sigma) for _ in range(n)]
        means.append(sum(xs) / n)
    m = sum(means) / len(means)
    var = sum((x - m) ** 2 for x in means) / (len(means) - 1)
    s = math.sqrt(var)
    skew = sum(((x - m) / s) ** 3 for x in means) / len(means) if s else 0.0
    kurt = sum(((x - m) / s) ** 4 for x in means) / len(means) - 3.0 if s else 0.0
    golden = sigma ** 2 / n
    rel_err = abs(var - golden) / golden
    return {"n_leaves": n, "empirical_var": var, "golden_var": golden,
            "relative_error": rel_err, "skew": skew, "excess_kurtosis": kurt,
            "var_check": rel_err < 0.05,
            "gaussian_check": abs(skew) < 0.15 and abs(kurt) < 0.25}


goldens = {"v2(12)": v_p(12, 2), "v2(8)": v_p(8, 2), "v3(18)": v_p(18, 3),
           "v5(100)": v_p(100, 5)}
golden_ok = goldens == {"v2(12)": 2, "v2(8)": 3, "v3(18)": 2, "v5(100)": 2}

rows = []
for p, D in ((2, 10), (3, 6), (2, 14)):
    viol = check_ultrametric_inequality(p, D)
    clt = check_clt(p, D, n_reps=2000)
    rows.append({"b": p, "D": D, "ultrametric_violations": viol,
                 "ultrametric_ok": viol == 0, **clt})

results = {"seed": SEED,
           "model": "b-adic ultrametric tree (d = b^{-v_b(|i-j|)}), iid "
                    "N(0,sigma^2) leaves; ergodic mean over leaves; CLT "
                    "Archimedean limit",
           "b_adic_goldens": goldens, "b_adic_goldens_ok": golden_ok,
           "checks": rows,
           "verdict_h2_numeric": all(r["ultrametric_ok"] and r["var_check"]
                                     and r["gaussian_check"] for r in rows)}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("RQ3 Archimedean-limit numeric check v2 - seed", SEED)
print("b-adic goldens:", goldens, "->", "OK" if golden_ok else "FAIL")
for r in rows:
    print(f"b={r['b']} D={r['D']} n={r['n_leaves']}: "
          f"ultrametric violations={r['ultrametric_violations']}, "
          f"var rel_err={r['relative_error']:.4f} (golden sigma^2/n), "
          f"skew={r['skew']:.3f} kurt={r['excess_kurtosis']:.3f} -> "
          f"{'PASS' if r['ultrametric_ok'] and r['var_check'] and r['gaussian_check'] else 'FAIL'}")
print("H2 numeric verdict:", results["verdict_h2_numeric"])
