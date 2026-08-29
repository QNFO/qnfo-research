"""verify-suite-p3.py — QNFO.RES.031 P3 computational verification suite (VERIFY-IN-CODE-1).

Closes the coverage gaps pre-declared in docs/corrected-dictionary.md §X:
  explicit-formula psi_0 (zeros as fluctuations); GUE pair correlation /
  number variance (seeded Monte Carlo); Sigma^2 exact vs Dyson; exact-Li
  unfolding via scipy.special.expi; Fermi observables; level-count C3(a);
  operator attribution C3(h)/(i) (Lambda = coefficients of -zeta'/zeta);
  zeta^k = k species C3(j); hard-core first-bin-zero as a computed bin count
  C3(f)/(k); deposited-artifact precision cross-check (BP-10).

Deterministic (fixed seeds). Reproducibility header printed at start.
"""
import math, time, sys
from math import log, pi

import numpy as np
import scipy.special
import scipy.integrate

print("=" * 70)
print("QNFO.RES.031 P3 suite  |  python", sys.version.split()[0],
      "| numpy", np.__version__, "| scipy", scipy.__version__)
print("seed (GUE MC): 20260829   runtime:", time.strftime("%Y-%m-%d %H:%M:%S"))
print("=" * 70)

results = []
def check(name, got, want, tol):
    if isinstance(got, (bool, np.bool_)):
        ok = bool(got) == bool(want)
    else:
        # ABSOLUTE tolerance (red-team A-6 fix, 2026-08-29): the check names
        # state absolute windows; relative semantics silently widened
        # large-magnitude guardrails (e.g. "311.9 tol 0.5" -> +-156, would have
        # accepted 316.3). All tolerances below are absolute.
        ok = abs(float(got) - float(want)) <= tol
    results.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} want={want!r} tol={tol}")

def sieve_upto(N):
    s = bytearray([1]) * (N + 1)
    if N >= 0: s[0] = 0
    if N >= 1: s[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(2, N + 1) if s[i]]

# ---------------------------------------------------------------- helpers ----
def von_mangoldt_sum(x):
    """psi(x) = sum_{n<=x} Lambda(n), exact."""
    total = 0.0
    for p in sieve_upto(int(x)):
        pk = p
        while pk <= x:
            total += log(p)
            pk *= p
    return total

# ============================================================================
# 1. Explicit formula psi_0(x): zeros enter as oscillatory corrections.
#    psi(x) = x - sum_rho x^rho/rho - ln(2 pi) - 1/2 ln(1 - x^-2)
#    Accurate zeros via mpmath.zetazero (exact), NOT the deposited cache.
#    Cached to gammas-120.npy (our computed artifact; mpmath-derived).
# ============================================================================
import os
GAMMAS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gammas-120.npy')
if os.path.exists(GAMMAS_PATH):
    GAMMAS = np.load(GAMMAS_PATH).tolist()
    print(f"[INFO] loaded {len(GAMMAS)} cached accurate zeros")
else:
    from mpmath import zetazero
    GAMMAS = [float(zetazero(k).imag) for k in range(1, 121)]
    np.save(GAMMAS_PATH, np.array(GAMMAS))
T_USE = GAMMAS[-1]
print(f"[INFO] {len(GAMMAS)} accurate zeros (mpmath.zetazero), T = {T_USE:.1f}")

def explicit_psi(x, gammas):
    out = x - log(2 * pi) - 0.5 * log(1.0 - x ** (-2))
    acc = 0.0 + 0.0j
    for g in gammas:
        rho_p = 0.5 + 1j * g
        rho_m = 0.5 - 1j * g
        acc += x ** rho_p / rho_p + x ** rho_m / rho_m
    return out - acc.real

for x in (20.0, 30.0):
    exact = von_mangoldt_sum(x)
    approx = explicit_psi(x, GAMMAS)
    resid = abs(exact - approx)
    print(f"[INFO] explicit formula x={x:g}: psi_exact={exact:.6f} psi_zeros={approx:.6f} residual={resid:.4f}")
    check(f"explicit formula psi({x:g}) matches to {0.5} (zeros = corrections)", approx, exact, 0.5)

# ============================================================================
# 2. Deposited-artifact precision cross-check (BP-10: citation != verification)
# ============================================================================
import hashlib, struct, re, os
NPY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'external-datasets', 'riemann-zeros-3000.npy')
raw = open(NPY_PATH, 'rb').read()
hdr_end = raw.index(b'\n') + 1
hdr = raw[10:raw.index(b'\n', 10)].decode()
n = int(re.search(r"'shape': \(([^)]*)\)", hdr).group(1).split(',')[0])
stored = np.frombuffer(raw[hdr_end:], dtype='<f8')
print(f"[INFO] deposited cache: n={n}, sha256={hashlib.sha256(raw).hexdigest()[:16]}")
K = 50
errs = [abs(float(stored[k]) - GAMMAS[k]) for k in range(K)]
print(f"[INFO] first {K} deposited vs true zero ordinates: max|err|={max(errs):.4f} mean|err|={sum(errs)/K:.4f}")
check("deposited cache is a coarse approximation (max err > 1e-3)", max(errs) > 1e-3, True, 0)
check("deposited cache errors are bounded (< 0.5, grossly right)", max(errs) < 0.5, True, 0)

# ============================================================================
# 3. GUE Monte Carlo (seeded): pair correlation -> R2(s) = 1 - (sin pi s/pi s)^2
#    and number variance Sigma^2(L) -> exact two-point reduction.
# ============================================================================
rng = np.random.default_rng(20260829)
m, M = 150, 120
pair_counts = None
bin_edges = np.arange(0.0, 3.01, 0.1)
bin_w = 0.1
n_over_total = 0
numvar = {L: [] for L in (5.0, 10.0, 20.0)}
for _ in range(M):
    H = np.zeros((m, m), dtype=complex)
    H[np.triu_indices(m, 1)] = (rng.standard_normal(m * (m - 1) // 2)
                                + 1j * rng.standard_normal(m * (m - 1) // 2)) / np.sqrt(2.0)
    H = H + H.conj().T
    H[np.diag_indices(m)] = rng.standard_normal(m)
    ev = np.linalg.eigvalsh(H)
    # unfold via the semicircle mean density (analytic CDF) — no rank unfolding
    # F(lambda) = lambda*sqrt(4m-lambda^2)/(4 pi) + (m/pi)*arcsin(lambda/(2 sqrt m)) + m/2
    # clip finite-m edge overshoot (Tracy-Widom) to the edge to avoid NaN in sqrt/arcsin
    edge = 2.0 * np.sqrt(m)
    n_over_total += int(np.sum(np.abs(ev) > edge))
    ev = np.clip(ev, -edge, edge)
    u = (ev * np.sqrt(4 * m - ev ** 2) + 4 * m * np.arcsin(ev / (2 * np.sqrt(m))) + 2 * pi * m) / (4 * pi)
    # interior points (drop the 2 edge points)
    ui = u[1:-1]
    # ---- two-point (all-pairs) correlation: R2(s) = 1 - (sin pi s/pi s)^2 ----
    iu = np.triu_indices(len(ui), 1)
    d = np.abs(ui[iu[0]] - ui[iu[1]])
    hc, _ = np.histogram(d, bins=bin_edges)
    pair_counts = hc if pair_counts is None else pair_counts + hc
    # ---- number variance: windows centered on a GRID (arbitrary positions), not
    # at data points (the Palm count has mean 2*int_0^(L/2) R2, not L) ----
    for L in numvar:
        grid = np.arange(L / 2.0, m - L / 2.0, 0.5)
        dd = np.abs(grid[:, None] - ui[None, :])
        n_x = np.sum(dd < L / 2.0, axis=1)
        numvar[L].append(float(np.mean((n_x - L) ** 2)))   # Sigma^2 = Var of count

n_int = m - 2
centers = (bin_edges[:-1] + bin_edges[1:]) / 2
# two-point correlation normalization: expected pairs per matrix per bin at
# density 1 = n_int * bin_w (each point sees bin_w neighbors per unit distance)
r2_est = pair_counts / (M * (n_int * bin_w))
print(f"[INFO] GUE MC edge-clip: mean {n_over_total / M:.1f} eigenvalues/matrix beyond +/-2*sqrt(m) (Tracy-Widom overshoot)")
r2_closed = 1.0 - (np.sin(pi * centers) / (pi * centers)) ** 2
bulk = (centers >= 0.4) & (centers <= 2.4)
maxdev = float(np.max(np.abs(r2_est[bulk] - r2_closed[bulk])))
print(f"[INFO] GUE MC: {M} matrices x m={m}; all-pairs R2 estimator; max |R2_est - closed| (bulk bins) = {maxdev:.4f}")
check("GUE two-point correlation matches 1-(sin pi s/pi s)^2 (max bulk dev < 0.05)", maxdev < 0.05, True, 0)

def sigma2_exact(L):
    """Exact two-point reduction, composite quadrature over unit intervals
    (the integrand oscillates; scipy.quad with a single interval fails at
    large L with the default 50-subdivision limit). L is integer here, so the
    unit intervals tile [0, L] up to a 1e-12 sliver (negligible)."""
    n_int = int(L)
    total = 0.0
    for k in range(n_int):
        f = lambda s, k=k: (L - s) * (np.sin(pi * s) / (pi * s)) ** 2
        total += scipy.integrate.quad(f, k + 1e-12, k + 1.0 - 1e-12, limit=100)[0]
    return L - 2 * total

for L in (5.0, 10.0, 20.0):
    mc = float(np.mean(numvar[L]))
    ex = sigma2_exact(L)
    print(f"[INFO] Sigma^2(L={L:g}): MC={mc:.4f} exact={ex:.4f}")
    check(f"GUE number variance Sigma^2({L:g}) matches exact reduction", mc, ex, 0.15)

# form factor: single-realization, report-only at fixed tau (non-self-averaging)
rng2 = np.random.default_rng(777)
H2 = np.zeros((m, m), dtype=complex)
H2[np.triu_indices(m, 1)] = (rng2.standard_normal(m * (m - 1) // 2)
                             + 1j * rng2.standard_normal(m * (m - 1) // 2)) / np.sqrt(2.0)
H2 = H2 + H2.conj().T
H2[np.diag_indices(m)] = rng2.standard_normal(m)
ev2 = np.linalg.eigvalsh(H2)
edge2 = 2.0 * np.sqrt(m)
ev2 = np.clip(ev2, -edge2, edge2)
u2 = (ev2 * np.sqrt(4 * m - ev2 ** 2) + 4 * m * np.arcsin(ev2 / (2 * np.sqrt(m))) + 2 * pi * m) / (4 * pi)
tau = 0.5
K1 = abs(np.sum(np.exp(2j * pi * tau * u))) ** 2 / m
K2 = abs(np.sum(np.exp(2j * pi * tau * u2))) ** 2 / m
print(f"[INFO] form factor K(tau={tau}), single realizations (report-only, non-self-averaging): seed1={K1:.3f} seed2={K2:.3f}")

# ============================================================================
# 4. Sigma^2 exact vs Dyson asymptotic (Dyson converges from below)
# ============================================================================
EULER = 0.5772156649015329
def dyson(L):
    return (1.0 / pi ** 2) * (log(2 * pi * L) + 1 + EULER - pi ** 2 / 8)
for L, e_expect, d_expect in ((20.0, 0.649546, 0.524552), (3400.0, 1.169918, 1.044918)):
    ex = sigma2_exact(L)
    dy = dyson(L)
    check(f"Sigma^2({L:g}) exact (quad)", ex, e_expect, 1e-3)
    check(f"Sigma^2({L:g}) Dyson asymptotic", dy, d_expect, 1e-3)
    check(f"Dyson < exact at L={L:g} (converges from below)", dy < ex, True, 0)

# misfit sweep over L <= 50 (dictionary Sec V item 3: "mis-fit 20-33% at L <= 50",
# defined as (exact - Dyson)/Dyson — red-team F2 remediation, computed not asserted)
mf_min, mf_max = 9.0, 0.0
for L in (5.0, 10.0, 20.0, 30.0, 40.0, 50.0):
    ex = sigma2_exact(L)
    dy = dyson(L)
    mf = (ex - dy) / dy
    mf_min = min(mf_min, mf)
    mf_max = max(mf_max, mf)
    assert dy < ex
print(f"[INFO] Dyson misfit (exact-Dyson)/Dyson over L=5..50: min {mf_min*100:.1f}% max {mf_max*100:.1f}%")
check("Dyson misfit in [20%,33%] over L<=50 (swept)", 0.20 <= mf_min and mf_max <= 0.33, True, 0)

# ============================================================================
# 5. Exact Li unfolding via scipy.special.expi(log x); asymptotic series diverges
# ============================================================================
def Li(x):
    return float(scipy.special.expi(log(x)))
check("Li(2) via expi", Li(2.0), 1.0451637801174928, 1e-9)
check("Li(10) via expi", Li(10.0), 6.165599504787298, 1e-9)
check("Li(1e6) via expi", Li(1e6), 78627.54916, 1e-5)

# asymptotic series Li(x) ~ (x/ln x) sum k!/(ln x)^k — diverges for small x
best_err = min(abs((2.0 / log(2.0)) * sum(math.factorial(k) / log(2.0) ** k for k in range(N + 1)) - Li(2.0))
               for N in range(0, 15))
print(f"[INFO] asymptotic series at x=2: best truncation error = {best_err:.3f} (true Li(2)={Li(2.0):.3f})")
check("asymptotic Li series unusable at small x (best err > 1)", best_err > 1.0, True, 0)

# ============================================================================
# 6. Fermi observables (coverage gap): U_F, C_V^F, S^F
# ============================================================================
BETA, P = 2.0, 10 ** 6
primes = sieve_upto(P)
UF = sum(log(p) / (p ** BETA + 1.0) for p in primes)
CVF = BETA * BETA * sum(log(p) ** 2 * p ** BETA / (p ** BETA + 1.0) ** 2 for p in primes)
h = 1e-6
def UF_b(b):
    return sum(log(p) / (p ** b + 1.0) for p in primes)
CVF_fd = -(BETA * BETA) * (UF_b(BETA + h) - UF_b(BETA - h)) / (2 * h)
ZF = 1.0
for p in primes:
    ZF *= 1.0 + p ** (-BETA)
SF_formula = sum(log(1 + p ** (-BETA)) + BETA * log(p) * p ** (-BETA) / (1 + p ** (-BETA)) for p in primes)
check("C_V^F = -beta^2 dU_F/dbeta (finite-diff)", CVF, CVF_fd, 1e-6)
check("C_V^F(2) = 2.6409738 (independent slot value)", CVF, 2.6409738, 1e-6)
check("S^F = ln Z_F + beta U_F", SF_formula, log(ZF) + BETA * UF, 1e-9)

# ============================================================================
# 7. Level counts C3(a): many-body count = integers; single-particle = primes
# ============================================================================
E = log(100.0)
many_body = math.floor(math.exp(E))
single_part = sum(1 for p in primes if p <= math.exp(E))
print(f"[INFO] E=ln(100): many-body states = floor(e^E) = {many_body}; single-particle prime modes = pi(100) = {single_part}")
check("many-body level count = integers (100 at E=ln 100)", many_body, 100, 0)
check("single-particle mode count = primes (25 at E=ln 100)", single_part, 25, 0)
check("integer count != prime count (C3(a) separation)", many_body != single_part, True, 0)

# ============================================================================
# 8. Operator attribution C3(h)/(i): Lambda = coefficients of -zeta'/zeta;
#    Tr e^{-beta H} = sum_n n^-beta = zeta(beta)
# ============================================================================
N = 10 ** 7
zeta2_sum = sum(n ** (-2.0) for n in range(1, N + 1))
tail = 1.0 / N - 0.5 / (N * N)   # Euler-Maclaurin remainder of sum_{n>N} n^-2
check("Tr e^{-beta H} = sum n^-2 = zeta(2) (tail-corrected)", zeta2_sum + tail, pi ** 2 / 6.0, 1e-8)

def mobius_sieve(N):
    mu = [1] * (N + 1)
    is_comp = [False] * (N + 1)
    primes_l = []
    for i in range(2, N + 1):
        if not is_comp[i]:
            primes_l.append(i)
            mu[i] = -1
        for p in primes_l:
            if i * p > N:
                break
            is_comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu
mu = mobius_sieve(200)
def Lambda_conv(n):
    return sum(mu[d] * log(n / d) for d in range(1, n + 1) if n % d == 0)
def Lambda_def(n):
    for p in range(2, n + 1):
        if n % p == 0:
            pk = p
            while pk <= n:
                if pk == n:
                    return log(p)
                pk *= p
            return 0.0
    return 0.0
ok_lambda = all(abs(Lambda_conv(n) - Lambda_def(n)) < 1e-9 for n in range(2, 201))
check("Lambda(n) = convolution coefficients of -zeta'/zeta (n<=200)", ok_lambda, True, 0)
check("Lambda(p)=ln p, Lambda(composite non-prime-power)=0: Lambda(7),Lambda(12)", (abs(Lambda_conv(7) - log(7)) < 1e-9 and Lambda_conv(12) < 1e-9), True, 0)

# ============================================================================
# 9. zeta^k = k independent species C3(j)
# ============================================================================
k = 3
prod_k = 1.0
prod_1 = 1.0
for p in primes:
    x = p ** (-BETA)
    prod_1 *= 1.0 / (1.0 - x)
    prod_k *= 1.0 / (1.0 - x) ** k
check("prod_p (1-p^-2)^-k = (prod_p (1-p^-2)^-1)^k (k=3, float-accum tol)", prod_k, prod_1 ** k, 1e-9)
check("zeta^k = exp(k ln Z): k=3 species not k-body interactions", prod_k, np.exp(k * log(prod_1)), 1e-9)

# ============================================================================
# 10. Hard-core first-bin-zero as COMPUTED bin count C3(f)/(k) + z-statistics
# ============================================================================
window = [p for p in primes if 3 <= p <= 10 ** 6]
gaps = [window[i + 1] - window[i] for i in range(len(window) - 1)]
spac = np.array([g / log(window[i]) for i, g in enumerate(gaps)])
check("min prime gap = 2 (computed, p>=3)", min(gaps), 2, 0)
w = 0.1
bin0 = int(np.sum(spac < w))
n_sp = len(spac)
poisson_expected = n_sp * (1 - np.exp(-w))
z_hard = (bin0 - poisson_expected) / np.sqrt(poisson_expected)
print(f"[INFO] unfolded spacings n={n_sp}; bin[0,{w}) count={bin0} (Poisson expected {poisson_expected:.0f}); z = {z_hard:.1f}")
check("first bin count == 0 (computed, not INFO-only)", bin0, 0, 0)
check("hard-core z-statistic is large (z < -50)", z_hard < -50, True, 0)
# unfolding sanity: mean unfolded spacing ~ 1
mean_sp = float(np.mean(spac))
check("unfolding sanity: mean unfolded spacing ~ 1", mean_sp, 1.0, 0.02)
# mid-range structure: prime gaps are even and mod-6-alternating, so a naive
# continuous-Poisson null is the WRONG reference there (report, not a claim)
mid = int(np.sum((spac >= 0.9) & (spac < 1.1)))
mid_exp = n_sp * (np.exp(-0.9) - np.exp(-1.1))
z_mid = (mid - mid_exp) / np.sqrt(mid_exp)
print(f"[INFO] mid-range bin [0.9,1.1): count={mid} vs continuous-Poisson expected {mid_exp:.0f}; z = {z_mid:.1f} —"
      f" the deviation is the even-gap/mod-6 structure of prime gaps, NOT a defect: the correct nulls for mid-range"
      f" statistics are the matched-level-density ensembles of RES.030, out of P3 scope (declared).")

print()
print(f"SUMMARY: {sum(results)}/{len(results)} checks passed")
print("reproducibility: seed 20260829 (GUE MC); mpmath.zetazero exact zeros;")
print("deposited cache cross-checked against mpmath (approximation quantified, not trusted).")
exit(0 if all(results) else 1)
