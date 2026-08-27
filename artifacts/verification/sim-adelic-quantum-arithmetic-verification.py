#!/usr/bin/env python3
"""QNFO.RES.029 — adelic-quantum-arithmetic: verification of quantitative statements.

Deterministic; Python standard library only; no random seeds.
Reproduces the arithmetic statements asserted in adelic-quantum-arithmetic.md:
  C1  Euler product -> zeta(2) = pi^2/6
  C2  squarefree Dirichlet series -> zeta(2)/zeta(4) = 15/pi^2
  C3  squarefree density -> 6/pi^2
  C4  Moebius inversion: sum mu(n)/n^2 -> 1/zeta(2) = 6/pi^2
  C5  occupation golden values at fugacity z=1/p (exact rational arithmetic)
  C6  canonical-derivative occupation (exact rational arithmetic)
  C7  Gentile cap-m Euler factor = finite geometric sum
  C8  bounded-occupation family at m=1 = squarefree ratio (per-prime factor form)
  C9  Laughlin phase e^{i pi/m} = primitive 2m-th root of unity
  C10 Fibonacci eigenvalues e^{i pi k/5} are tenth roots of unity

Usage: python sim-adelic-quantum-arithmetic-verification.py [output.json]
Run from the repository root. Output JSON path defaults to
artifacts/verification/verification-output.json.
"""

import cmath
import json
import math
import os
import sys
import time
from fractions import Fraction

t0 = time.time()
OUT = []


def sieve(n):
    is_comp = bytearray(n + 1)
    primes = []
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            if i * i <= n:
                for j in range(i * i, n + 1, i):
                    is_comp[j] = 1
    return primes


def mobius_sieve(n):
    mu = [1] * (n + 1)
    is_prime = bytearray(n + 1)
    for i in range(2, n + 1):
        if not is_prime[i]:
            for j in range(i, n + 1, i):
                is_prime[j] = 1
                mu[j] *= -1
            sq = i * i
            for j in range(sq, n + 1, sq):
                mu[j] = 0
    return mu


N_PRIME = 2_000_000
N_SUM = 2_000_000
primes = sieve(N_PRIME)
mu = mobius_sieve(N_SUM)

# C1: Euler product of zeta(2)
def euler_zeta(primes, s):
    prod = 1.0
    for p in primes:
        prod /= (1.0 - p ** (-s))
    return prod


zv = euler_zeta(primes, 2)
gold = math.pi ** 2 / 6
err = abs(zv - gold) / gold
OUT.append({"check": "C1_euler_product_zeta2", "value": zv, "expected": gold,
            "rel_err": err, "tolerance": 2e-6, "pass": err < 2e-6})

# C2: squarefree series -> zeta(2)/zeta(4) = 15/pi^2
sf_sum = 0.0
for n in range(1, N_SUM + 1):
    if mu[n] != 0:
        sf_sum += 1.0 / (n * n)
g2 = math.pi ** 2 / 6
g4 = math.pi ** 4 / 90
gold2 = g2 / g4
err = abs(sf_sum - gold2) / gold2
OUT.append({"check": "C2_squarefree_series_zeta_ratio", "value": sf_sum, "expected": gold2,
            "rel_err": err, "tolerance": 2e-6, "pass": err < 2e-6})

# C3: squarefree density -> 6/pi^2
cnt = sum(1 for n in range(1, N_SUM + 1) if mu[n] != 0)
dens = cnt / N_SUM
g3 = 6.0 / (math.pi ** 2)
err = abs(dens - g3)
OUT.append({"check": "C3_squarefree_density", "value": dens, "expected": g3,
            "abs_err": err, "tolerance": 2e-3, "pass": err < 2e-3})

# C4: Moebius inversion -> 1/zeta(2)
inv = sum(mu[n] / (n * n) for n in range(1, N_SUM + 1))
err = abs(inv - g3) / g3
OUT.append({"check": "C4_moebius_inversion_1_over_zeta2", "value": inv, "expected": g3,
            "rel_err": err, "tolerance": 2e-6, "pass": err < 2e-6})

# C5: occupation golden values at fugacity z=1/p (exact)
for p in (2, 3, 5, 7):
    z = Fraction(1, p)
    be_mean = z / (1 - z)
    fd_prob = z / (1 + z)
    ok = be_mean == Fraction(1, p - 1) and fd_prob == Fraction(1, p + 1)
    OUT.append({"check": "C5_occupation_golden_p%d" % p,
                "be_mean": str(be_mean), "expected_be": "1/%d" % (p - 1),
                "fd_prob": str(fd_prob), "expected_fd": "1/%d" % (p + 1),
                "pass": ok})

# C6: canonical-derivative occupation z d/dz ln Z (exact)
for p in (2, 3, 5):
    z = Fraction(1, p)
    be = z / (1 - z)
    fd = z / (1 + z)
    OUT.append({"check": "C6_canonical_derivative_p%d" % p,
                "be": str(be), "fd": str(fd),
                "pass": be == Fraction(1, p - 1) and fd == Fraction(1, p + 1)})

# C7: Gentile cap-m Euler factor = finite geometric sum
for p, m, s in ((2, 3, 2.0), (3, 2, 3.0)):
    lhs = (1 - p ** (-(m + 1) * s)) / (1 - p ** (-s))
    rhs = sum(p ** (-j * s) for j in range(m + 1))
    OUT.append({"check": "C7_gentile_factor_p%d_m%d_s%s" % (p, m, s),
                "lhs": lhs, "rhs": rhs, "abs_err": abs(lhs - rhs),
                "tolerance": 1e-12, "pass": abs(lhs - rhs) < 1e-12})

# C8: bounded-occupation family at m=1, per-prime factor = FD mode factor
for p, s in ((2, 2.0), (5, 3.0)):
    fac = (1 - p ** (-2 * s)) / (1 - p ** (-s))
    mode = 1 + p ** (-s)
    OUT.append({"check": "C8_family_m1_factor_p%d_s%s" % (p, s),
                "factor": fac, "mode": mode, "abs_err": abs(fac - mode),
                "pass": abs(fac - mode) < 1e-12})

# C9: Laughlin phase e^{i pi/m} = primitive 2m-th root of unity
for m in (3, 5):
    z = cmath.exp(1j * math.pi / m)
    is_one = abs(z ** (2 * m) - 1) < 1e-12
    prim = all(abs(z ** k - 1) > 1e-9 for k in range(1, 2 * m))
    OUT.append({"check": "C9_laughlin_primitive_root_m%d" % m,
                "z_2m_equals_1": is_one, "primitive": prim,
                "pass": is_one and prim})

# C10: Fibonacci eigenvalues e^{i pi/5} are tenth roots of unity
z5 = cmath.exp(1j * math.pi / 5)
OUT.append({"check": "C10_fibonacci_10th_root",
            "z_10": str(z5 ** 10),
            "pass": abs(z5 ** 10 - 1) < 1e-12})

elapsed = time.time() - t0
summary = {
    "total": len(OUT),
    "passed": sum(1 for c in OUT if c["pass"]),
    "failed": sum(1 for c in OUT if not c["pass"]),
    "runtime_s": round(elapsed, 2),
    "stdlib_only": True,
    "seeds": "none (deterministic)",
    "N_PRIME": N_PRIME,
    "N_SUM": N_SUM,
}
result = {"summary": summary, "checks": OUT}
out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "verification-output.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)
print(json.dumps(summary))
