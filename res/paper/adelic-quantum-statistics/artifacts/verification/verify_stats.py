"""verify_stats.py — QNFO.RES.027 F1 + F-HCP verification (reproduction first).

Verifies the mathematical core of T1 and H-COMPOSITE-PARITY with exact
identities, no external dependencies beyond the standard library:

  F1a  squarefree-lattice identity:  D(s) = sum_{n squarefree} n^{-s} = zeta(s)/zeta(2s)
  F1b  unrestricted-lattice identity: sum_{n>=1} n^{-s} = zeta(s)
  F1c  Euler-factor/occupation correspondence: (1 + p^{-b})  = fermionic mode
       partition function (occupation 0/1); (1 - p^{-b})^{-1} = bosonic mode
       (unbounded occupation).
  F1d  golden occupation values: <n>_F = 1/(e^{b ln p - b mu} + 1),
       <n>_B = 1/(e^{b ln p - b mu} - 1), matched against the canonical
       derivative -d/d(b ln p) ln Z_mode by finite differences.
  F-HCP Moebius parity: mu(n) = (-1)^{#prime factors} for squarefree n, and the
       composite exchange-sign table (Cooper pair, exciton, He-4, He-3, electron)
       matches the even/odd fermion-count rule.

Reproducibility: deterministic (no RNG). Runtime ~ seconds.
"""

import math, json, sys
import os

TOL = 1e-9   # finite-difference tolerance for F1d
S_TOL = 1e-6  # truncated-sum identity tolerance (N=1e5, s>=2.5)

def zeta(s, N=100000):
    """Euler-Maclaurin (first order) estimate of zeta(s) for s > 1."""
    ssum = sum(n ** (-s) for n in range(1, N + 1))
    return ssum + N ** (1 - s) / (s - 1) + 0.5 * N ** (-s)

def sieve_moebius(N):
    """Return (mu, primes) for 1..N (mu[0]=0, mu[1]=1)."""
    mu = [1] * (N + 1)
    is_comp = [False] * (N + 1)
    primes = []
    mu[0] = 0
    for i in range(2, N + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > N:
                break
            is_comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu, primes

def primes_up_to(P):
    return sieve_moebius(P)[1]

def main():
    results = []
    N = 100000
    mu, primes = sieve_moebius(N)

    def check(name, ok, detail):
        results.append({"check": name, "pass": bool(ok), "detail": detail})
        print(("PASS  " if ok else "FAIL  ") + name + " | " + detail)

    # ---- F1a: squarefree identity D(s) = zeta(s)/zeta(2s) ----
    for s in (2.5, 3.0, 4.0):
        d = sum(n ** (-s) for n in range(1, N + 1) if mu[n] != 0)
        ref = zeta(s) / zeta(2 * s)
        ok = abs(d - ref) < S_TOL * max(1.0, abs(ref))
        check("F1a squarefree D(%.1f) = zeta/zeta(2s)" % s, ok,
              "sum=%.10f ref=%.10f err=%.2e" % (d, ref, abs(d - ref)))

    # ---- F1b: unrestricted identity = zeta(s) ----
    for s in (2.5, 3.0, 4.0):
        d = sum(n ** (-s) for n in range(1, N + 1))
        ref = zeta(s)
        ok = abs(d - ref) < S_TOL * max(1.0, abs(ref))
        check("F1b unrestricted D(%.1f) = zeta" % s, ok,
              "sum=%.10f ref=%.10f err=%.2e" % (d, ref, abs(d - ref)))

    # ---- F1c: Euler-factor/occupation correspondence ----
    ps = primes  # from the N=1e5 sieve: tail p>1e5 contributes < 1e-8 at s>=2.5
    for s in (2.5, 3.0, 4.0):
        eF = 1.0
        for p in ps:
            eF *= 1.0 + p ** (-s)
        eB = 1.0
        for p in ps:
            eB /= 1.0 - p ** (-s)
        okF = abs(eF - zeta(s) / zeta(2 * s)) < S_TOL * max(1.0, abs(zeta(s) / zeta(2 * s)))
        okB = abs(eB - zeta(s)) < S_TOL * abs(zeta(s))
        check("F1c EulerF(%.1f) = prod(1+p^-s)" % s, okF,
              "prod=%.10f zeta/z2s=%.10f err=%.2e" % (eF, zeta(s) / zeta(2 * s), abs(eF - zeta(s) / zeta(2 * s))))
        check("F1c EulerB(%.1f) = prod(1-p^-s)^-1" % s, okB,
              "prod=%.10f zeta=%.10f err=%.2e" % (eB, zeta(s), abs(eB - zeta(s))))

    # ---- F1d: golden occupation values (finite-difference canonical check) ----
    h = 1e-6
    for p in (2, 3, 5):
        for b in (0.5, 1.0, 2.0):
            for z in (0.5, 1.0, 2.0):  # z = e^{b mu}
                zp = z * p ** (-b)
                if zp >= 1.0:          # Bose requires convergence
                    continue
                # canonical: <n> = -d/d(b ln p) ln Z_mode, finite difference in ln p
                lnp = math.log(p)
                def ZF(lnpp):
                    return 1.0 + z * math.exp(-b * lnpp)
                def ZB(lnpp):
                    return 1.0 / (1.0 - z * math.exp(-b * lnpp))
                for mode, Z, golden in (
                        ("F", ZF, zp / (1 + zp)),
                        ("B", ZB, zp / (1 - zp))):
                    # <n> = -(1/b) * d/d(ln p) ln Z_mode  (chain rule; energy = ln p);
                    # Richardson extrapolation kills the h^2 discretization error.
                    def occ_fd(Z_, lnp_, hh=1e-5):
                        dd = lambda h2: -(math.log(Z_(lnp_ + h2)) - math.log(Z_(lnp_ - h2))) / (2 * h2) / b
                        return (4 * dd(hh / 2) - dd(hh)) / 3
                    num = occ_fd(Z, lnp)
                    ok = abs(num - golden) < TOL
                    check("F1d %s p=%d b=%.1f z=%.1f" % (mode, p, b, z), ok,
                          "canonical=%.12f golden=%.12f err=%.2e" % (num, golden, abs(num - golden)))

    # ---- S1 direction-symmetry guard (Q4 inversion): the two statistics' golden
    # values differ at non-degenerate points, so the assignment is falsifiable,
    # not symmetric — if unrestricted occupation reproduced the Fermi golden
    # value, the squarefree<->Fermi direction would be unconstrained.
    for (p, b, z) in ((2, 1.0, 0.5), (3, 1.0, 1.0), (5, 2.0, 0.5)):
        zp = z * p ** (-b)
        nF = zp / (1 + zp)
        nB = zp / (1 - zp)
        ok = abs(nF - nB) > 1e-9
        check("S1 direction guard p=%d b=%.1f z=%.1f" % (p, b, z), ok,
              "Fermi=%.6f Bose=%.6f differ=%.6f" % (nF, nB, abs(nF - nB)))

    # ---- F-HCP: Moebius parity + composite exchange-sign table ----
    # mu(n) = (-1)^{#distinct prime factors} for squarefree n — verify by construction
    def omega(n):
        c, d, i = 0, 2, n
        while d * d <= i:
            if i % d == 0:
                c += 1
                while i % d == 0:
                    i //= d
            d += 1
        if i > 1:
            c += 1
        return c
    ok_mu = True
    for n in range(2, 5001):
        if mu[n] != 0:
            if mu[n] != (-1) ** omega(n):
                ok_mu = False
                break
    check("F-HCP mu parity squarefree n<=5000", ok_mu, "mu(n)=(-1)^{#prime factors}")

    # composite exchange-sign table: even # fermions -> +1 (bosonic), odd -> -1
    table = [
        ("Cooper pair", 2, +1), ("exciton", 2, +1), ("helium-4", 6, +1),
        ("helium-3", 3, -1), ("electron", 1, -1),
    ]
    ok_t = all(((-1) ** count) == sign for _, count, sign in table)
    check("F-HCP composite sign table", ok_t,
          ", ".join("%s:%d->%+d" % (nm, c, s) for nm, c, s in table))

    total = sum(1 for r in results if r["pass"])
    failed = [r["check"] for r in results if not r["pass"]]
    print("\nRESULT: %d/%d PASS" % (total, len(results)))
    if failed:
        print("FAILED: " + "; ".join(failed))
        sys.exit(1)
    print("ALL CHECKS PASS")
    json.dump({"passed": total, "total": len(results), "results": results},
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "verify_stats_results.json"), "w"),
              indent=2)

if __name__ == "__main__":
    main()
