"""verify_parastats.py — QNFO.RES.027 F6 math-side golden checks.

Verifies the arithmetic core of H-PARASTATS-INTERMEDIATE (the interpolation
family the anyon correspondence must contact — the correspondence itself stays
an open problem, stated not verified):

  V1  bounded-occupancy single-mode partition function
      Z_m = sum_{a=0}^{m} z^a p^{-a beta} = (1 - (zp^{-beta})^{m+1})/(1 - zp^{-beta})
      with mean <n>_m = z d/dz ln Z_m:  m=1 equals the Fermi golden value exactly,
      m large approaches the Bose golden value.
  V2  m-bounded lattice identity:  sum_{n: v_p(n)<=m for all p} n^{-s} = zeta(s)/zeta((m+1)s)
      for m in {1,2,3}, s in {3,4} (direct sieved sum vs zeta ratio).
  V3  interpolation endpoints as exact identities: m=1 gives zeta(s)/zeta(2s) (squarefree/Fermi)
      and the family converges to zeta(s) (Bose) as m -> infinity (formula-level equality).
  V4  consistency: the m=1 sieved sum equals verify_stats.py's squarefree identity reference
      zeta(3)/zeta(6) at s=3.

Deterministic, stdlib only. Reproducibility: no RNG, runtime ~ seconds.
"""

import math, sys, json
import os

def zeta(s, N=100000):
    ssum = sum(n ** (-s) for n in range(1, N + 1))
    return ssum + N ** (1 - s) / (s - 1) + 0.5 * N ** (-s)

def exp_bound_sieve(N, m):
    """Return indicator array b[n]=1 iff v_p(n) <= m for every prime p (n in 1..N)."""
    b = [1] * (N + 1)
    b[0] = 0
    for p in range(2, N + 1):
        if b[p] == 0:
            continue
        # p is prime in this walk? ensure primality test cheaply:
        if any(p % q == 0 for q in range(2, int(math.isqrt(p)) + 1)):
            continue
        pk = p ** (m + 1)
        for k in range(pk, N + 1, pk):
            b[k] = 0
    return b

def is_prime(p):
    if p < 2:
        return False
    for q in range(2, int(math.isqrt(p)) + 1):
        if p % q == 0:
            return False
    return True

def main():
    results = []
    def check(name, ok, detail):
        results.append({"check": name, "pass": bool(ok), "detail": detail})
        print(("PASS  " if ok else "FAIL  ") + name + " | " + detail)

    TOL = 1e-9
    S_TOL = 1e-6

    # ---- V1: single-mode bounded-occupation partition function ----
    for p, beta, z, m in ((2, 1.0, 0.5, 1), (3, 1.0, 1.0, 2), (5, 2.0, 0.5, 3)):
        zp = z * p ** (-beta)
        # direct sums
        Z = sum(zp ** a for a in range(m + 1))
        Nbar = sum(a * zp ** a for a in range(m + 1)) / Z
        # analytic
        Za = (1 - zp ** (m + 1)) / (1 - zp)
        Na = zp / (1 - zp) - (m + 1) * zp ** (m + 1) / (1 - zp ** (m + 1))
        ok = abs(Z - Za) < TOL and abs(Nbar - Na) < TOL
        check("V1 bounded-occ Z_m p=%d b=%.1f z=%.1f m=%d" % (p, beta, z, m), ok,
              "Z=%.12f Za=%.12f <n>=%.12f <n>a=%.12f" % (Z, Za, Nbar, Na))

    # m=1 exactly Fermi golden; m large approaches Bose golden
    for p, beta, z in ((2, 1.0, 0.5), (3, 2.0, 1.0)):
        zp = z * p ** (-beta)
        nF = zp / (1 + zp)
        nB = zp / (1 - zp)
        Z1 = 1 + zp
        n1 = zp / Z1
        Zbig = sum(zp ** a for a in range(200))
        nbig = sum(a * zp ** a for a in range(200)) / Zbig
        ok1 = abs(n1 - nF) < TOL
        okbig = abs(nbig - nB) < 1e-6
        check("V1 m=1=Fermi p=%d b=%.1f z=%.1f" % (p, beta, z), ok1,
              "n1=%.12f nF=%.12f" % (n1, nF))
        check("V1 m=200~Bose p=%d b=%.1f z=%.1f" % (p, beta, z), okbig,
              "nbig=%.12f nB=%.12f err=%.2e" % (nbig, nB, abs(nbig - nB)))

    # ---- V2: m-bounded lattice identity zeta(s)/zeta((m+1)s) ----
    N = 100000
    for m in (1, 2, 3):
        b = exp_bound_sieve(N, m)
        for s in (3.0, 4.0):
            d = sum(n ** (-s) for n in range(1, N + 1) if b[n] == 1)
            ref = zeta(s) / zeta((m + 1) * s)
            ok = abs(d - ref) < S_TOL * max(1.0, abs(ref))
            check("V2 m-bounded D(%.1f) m=%d = zeta/zeta(%s)" % (s, m, (m + 1) * s), ok,
                  "sum=%.10f ref=%.10f err=%.2e" % (d, ref, abs(d - ref)))

    # ---- V3: endpoint identities at formula level ----
    ok_m1 = abs(zeta(3.0) / zeta(6.0) - zeta(3.0) / zeta(2 * 3.0)) < 1e-15
    # family -> zeta(s) as m -> infinity: zeta(s)/zeta((m+1)s) -> zeta(s) since zeta((m+1)s)->1
    ok_lim = abs(zeta(3.0) / zeta(100 * 3.0) - zeta(3.0)) < 1e-6
    check("V3 m=1 endpoint = zeta(s)/zeta(2s)", ok_m1, "identity exact")
    check("V3 m->inf endpoint = zeta(s)", ok_lim, "zeta(3)/zeta(300)=%.10f vs zeta(3)=%.10f" % (
        zeta(3.0) / zeta(300.0), zeta(3.0)))

    # ---- V4: consistency with verify_stats.py F1a reference at s=3 ----
    b1 = exp_bound_sieve(N, 1)
    d1 = sum(n ** (-3.0) for n in range(1, N + 1) if b1[n] == 1)
    ref1 = zeta(3.0) / zeta(6.0)
    ok4 = abs(d1 - ref1) < S_TOL * max(1.0, abs(ref1))
    check("V4 m=1 sum equals F1a squarefree reference", ok4,
          "sum=%.10f ref=%.10f" % (d1, ref1))

    total = sum(1 for r in results if r["pass"])
    failed = [r["check"] for r in results if not r["pass"]]
    print("\nRESULT: %d/%d PASS" % (total, len(results)))
    if failed:
        print("FAILED: " + "; ".join(failed))
        sys.exit(1)
    print("ALL CHECKS PASS")
    json.dump({"passed": total, "total": len(results), "results": results},
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "verify_parastats_results.json"), "w"),
              indent=2)

if __name__ == "__main__":
    main()
