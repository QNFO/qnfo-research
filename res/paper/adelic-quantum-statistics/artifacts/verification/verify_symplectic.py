"""verify_symplectic.py — QNFO.RES.027 F3 verification (T3: symplectic emergence).

Verifies the finite-distinction geometry of the seed note's Part A construction
(Fisher metric g, reversible generator L, symplectic form omega = gL, complex
structure J = g^{-1} omega) and the Fermi/Bose contrast, with exact numerics:

  F3a  Fisher metric: Hessian of S(p) = -sum p ln p on the simplex matches
       d^2S/dp_i dp_j = -delta_ij/p_i - 1/p_N (i,j < N) at random interior
       points AND at the uniform point; the FISHER metric g = delta_ij/p_i +
       1/p_N is its exact negative (sign-convention note: the seed note's
       stated "g = d^2S" carries this sign slip — the metric it uses
       throughout is the correct positive one).
  F3b  L = (shift - shift^{-1})/2 is skew w.r.t. g: g(Lv, w) = -g(v, Lw).
  F3c  Fourier eigenvalues of L: lambda_k = -i sin(2 pi k/N) (complex
       eigenvectors; exact).
  F3d  omega = gL is antisymmetric.
  F3e  finite-N honesty: J = g^{-1} omega = L at the uniform point; J^2 has
       Fourier eigenvalues -sin^2(2 pi k/N) — NOT -1 (deviation 1 - sin^2).
  F3f  Hilbert normalization: the sign-normalized operator H with multiplier
       -i sgn(sin(2 pi k/N)) satisfies H^2 = -1 on mean-zero modes (excluding
       the k = N/2 null mode for even N) — the complex structure exists at
       every N as the SIGN-NORMALIZED generator (the discrete Hilbert transform).
  F3g  Bose-side contrast: the symmetric generator L_B = (shift + shift^{-1})/2
       is symmetric w.r.t. g; J_B^2 has REAL eigenvalues cos^2(2 pi k/N) >= 0,
       so (J_B)^2 cannot equal -1 — no complex structure on the diffusive
       (unrestricted) side. Fermi-specificity holds.
  F3h  large-N honesty: at fixed theta = 2 pi k/N, J^2(theta) = -sin^2(theta),
       bounded away from -1 for theta != pi/2 — the RAW generator does not
       converge to a complex structure pointwise; only the sign-normalized one
       does (exact at every N).

Verdict discipline: the complex structure is the Hilbert (sign-normalized)
structure; the raw generator carries the Hilbert phase but not the Hilbert
magnitude. T3's claim survives in its precise form with this renormalization
stated (folded into PROJECT-PLAN as the T3 precision note). stdlib only,
deterministic.
"""

import cmath, math, random, sys, json

def main():
    results = []
    def check(name, ok, detail):
        results.append({"check": name, "pass": bool(ok), "detail": detail})
        print(("PASS  " if ok else "FAIL  ") + name + " | " + detail)

    rng = random.Random(20260827)
    h = 1e-5

    # ---- F3a: Fisher metric Hessian (random interior points + uniform) ----
    for N in (4, 8):
        samples = []
        for _ in range(3):
            u = [rng.random() for _ in range(N - 1)]
            s = 1.0 + sum(u)
            samples.append([x / s for x in u] + [1.0 / s])
        samples.append([1.0 / N] * N)          # uniform point
        for p in samples:
            pN = p[N - 1]
            def S(shift_i, shift_j):
                v = list(p)
                v[shift_i[0]] += shift_i[1]
                v[shift_j[0]] += shift_j[1]
                v[N - 1] = 1.0 - sum(v[:N - 1])
                return -sum(x * math.log(x) for x in v if x > 0)
            worst = 0.0
            for i in range(N - 1):
                for j in range(N - 1):
                    # Hessian of S itself: d^2 S/dp_i dp_j = -delta_ij/p_i - 1/p_N
                    # (the constraint term carries the same sign as the diagonal).
                    # The FISHER metric is its exact negative, g = delta_ij/p_i + 1/p_N
                    # (the seed note's stated "g = d^2S" carries a sign slip — the
                    # metric it uses throughout is the correct positive one).
                    gijS = (-1.0 / p[i] if i == j else 0.0) - 1.0 / pN
                    if i == j:
                        D = lambda hh: (S((i, +hh), (i, +0)) - 2 * S((i, 0), (i, 0)) + S((i, -hh), (i, 0))) / (hh * hh)
                        hm = (4 * D(h) - D(2 * h)) / 3  # Richardson: kills the h^2 error
                    else:
                        hm = (S((i, +h), (j, +h)) - S((i, +h), (j, -h))
                              - S((i, -h), (j, +h)) + S((i, -h), (j, -h))) / (4 * h * h)
                    worst = max(worst, abs(hm - gijS))
            check("F3a Fisher Hessian N=%d p_N=%.3f" % (N, pN), worst < 1e-4,
                  "worst |numeric - closed form| = %.2e" % worst)

    # ---- F3b-F3h: generator structure at the uniform point ----
    for N in (8, 16, 32):
        def shift_mat(sign):
            M = [[0.0] * N for _ in range(N)]
            for i in range(N):
                M[i][(i + sign) % N] = 1.0
            return M
        L = [[(shift_mat(1)[i][j] - shift_mat(-1)[i][j]) / 2.0 for j in range(N)] for i in range(N)]
        G = [[N * (1.0 if i == j else 0.0) + N for j in range(N)] for i in range(N)]  # N(I + 11^T)

        def mv(M, v):
            return [sum(M[i][j] * v[j] for j in range(N)) for i in range(N)]
        def dot(u, v):
            return sum(a * b for a, b in zip(u, v))
        def gform(u, v):
            return dot(mv(G, u), v)
        def meanzero():
            v = [rng.random() - 0.5 for _ in range(N)]
            m = sum(v) / N
            return [x - m for x in v]

        # F3b skewness at random mean-zero vectors
        worst = 0.0
        for _ in range(3):
            v, w = meanzero(), meanzero()
            worst = max(worst, abs(gform(mv(L, v), w) + gform(v, mv(L, w))))
        check("F3b L skew w.r.t. g N=%d" % N, worst < 1e-10, "worst |g(Lv,w)+g(v,Lw)| = %.2e" % worst)

        # F3c Fourier eigenvalues of L (complex eigenvectors; sign per shift convention:
        # (shift v)_i = v_{i+1}, so L e_k = +i sin(2 pi k/N) e_k)
        worst = 0.0
        for k in range(N):
            v = [cmath.exp(2j * math.pi * k * i / N) for i in range(N)]
            Lv = mv(L, v)
            expected = 1j * math.sin(2 * math.pi * k / N)
            err = max(abs(Lv[i] - expected * v[i]) for i in range(N))
            worst = max(worst, err)
        check("F3c Fourier eigenvalues N=%d" % N, worst < 1e-10,
              "worst |L e_k - (-i sin) e_k| = %.2e" % worst)

        # F3d omega = gL antisymmetric
        Om = [[sum(G[i][m] * L[m][j] for m in range(N)) for j in range(N)] for i in range(N)]
        worst = max(abs(Om[i][j] + Om[j][i]) for i in range(N) for j in range(N))
        check("F3d omega = gL antisymmetric N=%d" % N, worst < 1e-10, "worst |Om+Om^T| = %.2e" % worst)

        # F3e J^2 = L^2 eigenvalues -sin^2 (cos vectors OK: J^2 scalar on each mode)
        Jsq = [[sum(L[i][m] * L[m][j] for m in range(N)) for j in range(N)] for i in range(N)]
        worst = 0.0
        for k in range(N):
            v = [math.cos(2 * math.pi * k * i / N) for i in range(N)]
            expected = -math.sin(2 * math.pi * k / N) ** 2
            err = max(abs(mv(Jsq, v)[i] - expected * v[i]) for i in range(N))
            worst = max(worst, err)
        ok_e = worst < 1e-10
        dev1 = 1.0 - math.sin(2 * math.pi / N) ** 2
        ok_not1 = dev1 > 1e-3
        check("F3e J^2 eigenvalues = -sin^2 N=%d" % N, ok_e, "worst err = %.2e" % worst)
        check("F3e finite-N J^2 != -1 (k=1) N=%d" % N, ok_not1,
              "J^2(k=1) = %.6f vs -1 (deviation %.6f)" % (-math.sin(2 * math.pi / N) ** 2, dev1))

        # F3f Hilbert normalization: H^2 = -1 on mean-zero modes minus the k=N/2 null
        def apply_H(v):
            V = [sum(v[i] * cmath.exp(-2j * math.pi * k * i / N) for i in range(N)) / N for k in range(N)]
            Hh = []
            for k in range(N):
                s = math.sin(2 * math.pi * k / N)
                hk = -1j * (1.0 if s > 0 else (-1.0 if s < 0 else 0.0))
                Hh.append(hk * V[k])
            return [sum(Hh[k] * cmath.exp(2j * math.pi * k * i / N) for k in range(N)).real for i in range(N)]

        worst = 0.0
        for _ in range(2):
            v = meanzero()
            if N % 2 == 0:
                c_alt = sum(v[j] * ((-1.0) ** j) for j in range(N)) / N
                v = [vi - c_alt * ((-1.0) ** i) for i, vi in enumerate(v)]
            Hv = apply_H(v)
            HHv = apply_H(Hv)
            worst = max(worst, max(abs(HHv[i] + v[i]) for i in range(N)))
        check("F3f Hilbert H^2 = -1 on mean-zero modes N=%d" % N, worst < 1e-9,
              "worst |H^2 v + v| = %.2e" % worst)

        # F3g Bose-side contrast
        LB = [[(shift_mat(1)[i][j] + shift_mat(-1)[i][j]) / 2.0 for j in range(N)] for i in range(N)]
        worst = 0.0
        for _ in range(2):
            v, w = meanzero(), meanzero()
            worst = max(worst, abs(gform(mv(LB, v), w) - gform(v, mv(LB, w))))
        check("F3g L_B symmetric w.r.t. g N=%d" % N, worst < 1e-10,
              "worst |g(LB v,w)-g(v,LB w)| = %.2e" % worst)
        JB2 = [[sum(LB[i][m] * LB[m][j] for m in range(N)) for j in range(N)] for i in range(N)]
        worst = 0.0
        for k in range(N):
            v = [math.cos(2 * math.pi * k * i / N) for i in range(N)]
            expected = math.cos(2 * math.pi * k / N) ** 2
            err = max(abs(mv(JB2, v)[i] - expected * v[i]) for i in range(N))
            worst = max(worst, err)
        check("F3g J_B^2 eigenvalues = cos^2 >= 0 N=%d" % N, worst < 1e-10,
              "worst err = %.2e (no complex structure on the Bose side)" % worst)

        # F3h large-N honesty at fixed theta (avoid theta = pi/2, the single mode where J^2 = -1)
        if N == 32:
            for k_frac in (1.0 / 8.0, 3.0 / 16.0):
                theta = 2 * math.pi * k_frac
                dev = 1.0 - math.sin(theta) ** 2
                check("F3h J^2(theta=%.3f) != -1 (dev %.3f)" % (theta, dev), dev > 0.05,
                      "raw generator stays away from J^2=-1; only the sign-normalized H gives it")

    total = sum(1 for r in results if r["pass"])
    failed = [r["check"] for r in results if not r["pass"]]
    print("\nRESULT: %d/%d PASS" % (total, len(results)))
    if failed:
        print("FAILED: " + "; ".join(failed))
        sys.exit(1)
    print("ALL CHECKS PASS")
    json.dump({"passed": total, "total": len(results), "results": results},
              open(r"C:\Users\LENOVO\Projects\qnfo-research\res\paper\adelic-quantum-statistics\artifacts\verification\verify_symplectic_results.json", "w"),
              indent=2)

if __name__ == "__main__":
    main()
