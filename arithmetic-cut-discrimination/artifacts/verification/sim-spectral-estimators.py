# QNFO.RES.030 P3 — spectral estimator verification suite
# Construction rules B1-B6; amendments A1 (D-1), A2 (D-2), A3 (D-3).
# Deterministic seed 20260829. Run from repo root:
#   python arithmetic-cut-discrimination/artifacts/verification/sim-spectral-estimators.py
import json, math, os, time
import numpy as np
from scipy.special import expi

SEED = 20260829
OUT = {"seed": SEED, "p3_task": "spectral_estimators"}
t0 = time.time()

# ---- B2: exact Li via expi(log x) ----
def li_exact(x):
    x = np.asarray(x, dtype=float)
    return np.real(expi(np.log(x)))

def primes_upto(P):
    sieve = np.ones(P + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(P ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    return np.nonzero(sieve)[0]

# ---- B1: pair correlation via k-th-neighbor decomposition, per-order normalization ----
def pair_corr_kth(levels, kmax=30, smax=4.0, nbins=240):
    u = np.sort(np.asarray(levels, dtype=float))
    n = len(u)
    edges = np.linspace(0.0, smax, nbins + 1)
    bw = smax / nbins
    R2 = np.zeros(nbins)
    for k in range(1, kmax + 1):
        if n - k <= 1:
            break
        s = u[k:] - u[:-k]
        h, _ = np.histogram(s, bins=edges)
        if h.sum() > 0:
            R2 += h / ((n - k) * bw)   # normalize by TOTAL per-order count (n-k), not in-range count
    return 0.5 * (edges[:-1] + edges[1:]), R2

def gue_r2(s):
    x = np.pi * s
    return 1.0 - (np.sin(x) / x) ** 2

def mad(a, b):
    return float(np.mean(np.abs(a - b)))

# ---- B3: full Dyson number variance; no rank unfolding ----
def rvm(t):
    t = np.asarray(t, dtype=float)
    return t / (2.0 * np.pi) * (np.log(t / (2.0 * np.pi)) - 1.0) + 7.0 / 8.0

def dyson_sigma2(L):
    gamma = 0.5772156649015329
    return (1.0 / np.pi ** 2) * (np.log(2.0 * np.pi * L) + 1.0 + gamma - np.pi ** 2 / 8.0)

def number_variance(u, L):
    u = np.sort(np.asarray(u, dtype=float))
    lo, hi = u[0], u[-1]
    nwin = int((hi - lo) // L)
    if nwin < 4:
        return float("nan"), int(nwin)
    starts = lo + np.arange(nwin) * L
    cnt = np.array([((u >= s) & (u < s + L)).sum() for s in starts])
    return float(cnt.var(ddof=1)), int(nwin)

def _clean(v):
    return None if (v is None or (isinstance(v, float) and math.isnan(v))) else round(float(v), 6)

# ---- B5: form factor, single realization, report-only ----
def form_factor(u, taus):
    u = np.asarray(u, dtype=float)
    K = np.empty(len(taus))
    for i, tau in enumerate(taus):
        K[i] = np.abs(np.exp(2j * np.pi * tau * u).sum()) ** 2 / len(u)
    return K

# ---- D-2: true GUE (Hermitian Gaussian ensemble), semicircle unfolding ----
def semicircle_cdf(x, n):
    a = 2.0 * math.sqrt(n)
    r = np.clip(x / a, -1.0, 1.0)
    return 0.5 + np.arcsin(r) / np.pi + r * np.sqrt(1.0 - r * r) / np.pi

def gue_sample(n, seed):
    g = np.random.default_rng(seed)
    X = g.standard_normal((n, n))
    Y = g.standard_normal((n, n))
    A = (X + X.T) / 2.0 + 1j * (Y - Y.T) / 2.0
    ev = np.sort(np.linalg.eigvalsh(A))
    return semicircle_cdf(ev, n) * n

# ---- B4: primes — Gallagher Poisson + twin-gap hard core ----
print("section: primes", flush=True)
P = 1 << 14
ps = primes_upto(P)
u = li_exact(ps.astype(float)) - li_exact(2.0)
s1 = np.diff(np.sort(u))
s_min = float(s1.min())
pred_smin = 2.0 / np.log(float(P))
OUT["primes"] = {
    "P_max": int(P), "N": int(len(ps)),
    "s_min_measured": round(s_min, 6),
    "predicted_s_min_2_over_lnP": round(pred_smin, 6),
    "count_below_predicted_smin": int((s1 < pred_smin).sum())}
sc, r2_pr = pair_corr_kth(u)
OUT["primes"]["paircorr"] = {
    "MAD_vs_Poisson": round(mad(r2_pr, np.ones_like(r2_pr)), 6),
    "MAD_vs_GUE": round(mad(r2_pr, gue_r2(sc)), 6),
    "R2_bin0": round(float(r2_pr[0]), 6)}
taus_ff = np.array([0.5, 1.0, 2.0])
OUT["primes"]["form_factor_report_only"] = {
    str(t): round(float(v), 4) for t, v in zip(taus_ff, form_factor(u, taus_ff))}

# ---- D-1: Riemann zeros — pair correlation anchor + Dyson recompute ----
print("section: riemann_zeros", flush=True)
try:
    from scipy.special import loggamma
    from scipy.optimize import brentq
    nz = 3000
    ver_dir = os.path.dirname(os.path.abspath(__file__))
    cache = os.path.join(ver_dir, "riemann-zeros-3000.npy")
    if os.path.exists(cache):
        z = np.load(cache)
    else:
        # Riemann-Siegel Z-function method (canonical per QNFO.UMP.014 P3-exec
        # sim-riemann-zeros-fast.py): vectorized sign-flip scan + brentq refine.
        T_GRID = np.arange(10.0, 6000.0, 0.05)
        def theta_rs(t):
            t = np.asarray(t, dtype=float)
            return np.imag(loggamma(0.25 + 0.5j * t)) - 0.5 * t * np.log(np.pi)
        def Z_scalar(t):
            n = np.arange(1, int(np.floor(np.sqrt(t / (2.0 * np.pi)))) + 1)
            th = float(np.imag(loggamma(0.25 + 0.5j * t))) - 0.5 * t * np.log(np.pi)
            return 2.0 * float(np.sum(n ** -0.5 * np.cos(th - t * np.log(n))))
        th = theta_rs(T_GRID)
        nmax = int(np.floor(np.sqrt(T_GRID.max() / (2.0 * np.pi))))
        Zg = np.zeros_like(T_GRID)
        for nn in range(1, nmax + 1):
            valid = nn ** 2 <= T_GRID / (2.0 * np.pi)
            Zg += np.where(valid, 2.0 * nn ** -0.5 * np.cos(th - T_GRID * np.log(nn)), 0.0)
        signs = np.sign(Zg)
        flips = np.where(signs[:-1] * signs[1:] < 0)[0]
        zeros_rs = []
        for i in flips:
            a, b = T_GRID[i], T_GRID[i + 1]
            zeros_rs.append(brentq(Z_scalar, a, b))
            if len(zeros_rs) >= nz:
                break
        z = np.array(sorted(zeros_rs))
        np.save(cache, z)
    uz = rvm(z)
    zc, r2_z = pair_corr_kth(uz)
    OUT["riemann_zeros"] = {
        "N": nz,
        "paircorr_MAD_vs_GUE": round(mad(r2_z, gue_r2(zc)), 6),
        "repulsion_R2_bin0": round(float(r2_z[0]), 6)}
    nv = {}
    for L in [5, 10, 15, 20, 25, 30, 50, 100, 500, 1000, 2000, 3400]:
        val, nwin = number_variance(uz, L)
        nv[str(L)] = {"measured": _clean(val),
                      "dyson": round(dyson_sigma2(float(L)), 6),
                      "ratio": None if _clean(val) is None else round(val / dyson_sigma2(float(L)), 6),
                      "windows": nwin}
    OUT["riemann_zeros"]["number_variance_vs_dyson"] = nv
except Exception as e:
    OUT["riemann_zeros"] = {"error": str(e)}

# ---- D-2: GUE Monte Carlo null validation ----
print("section: gue_null", flush=True)
n_gue, M_gue = 800, 8
gue_u = [gue_sample(n_gue, SEED + 100 + i) for i in range(M_gue)]
r2s = []
sc_g = None
for i in range(M_gue):
    sc_g, r2_g = pair_corr_kth(gue_u[i], kmax=20)
    r2s.append(r2_g)
r2_gue_pooled = np.mean(r2s, axis=0)
OUT["gue_null"] = {
    "n": n_gue, "M": M_gue,
    "paircorr_MAD_vs_analytic_GUE": round(mad(r2_gue_pooled, gue_r2(sc_g)), 6)}
nv_gue = {}
for L in [10, 20]:
    vals = [number_variance(gu, L)[0] for gu in gue_u]
    vals = [v for v in vals if not (isinstance(v, float) and math.isnan(v))]
    if vals:
        nv_gue[str(L)] = {"mean": round(float(np.mean(vals)), 6),
                          "dyson": round(dyson_sigma2(float(L)), 6),
                          "n_samples": len(vals)}
OUT["gue_null"]["number_variance"] = nv_gue

# ---- D-3: planted control (positive control, planted in unfolded space) ----
print("section: planted_control", flush=True)
def planted_u(N, eps, lam_u, seed):
    g = np.random.default_rng(seed)
    out = []
    while len(out) < N:
        uu = g.random(4 * N) * N
        a = 0.5 * (1.0 + eps * np.cos(2.0 * np.pi * uu / lam_u))
        keep = g.random(4 * N) < a
        out.extend(uu[keep].tolist())
    return np.sort(np.asarray(out[:N]))

N_pl, eps_pl, lam_u_pl = 4000, 0.20, math.log(4.0)
u_pl = planted_u(N_pl, eps_pl, lam_u_pl, SEED + 7)
# single dense scan: peak width ~ 1/N = 0.00025, so grid step must be <= that
taus_pl = np.linspace(0.05, 5.0, 30000)
K_pl = form_factor(u_pl, taus_pl)
mask = (taus_pl >= 0.2) & (taus_pl <= 2.5)
tau_hat = float(taus_pl[mask][np.argmax(K_pl[mask])])
tau_star = 1.0 / lam_u_pl
OUT["planted_control"] = {
    "N": N_pl, "eps": eps_pl, "lam_u": round(lam_u_pl, 6),
    "tau_star": round(tau_star, 6), "tau_hat": round(tau_hat, 6),
    "recovery_error": round(abs(tau_hat - tau_star) / tau_star, 6),
    "K_at_peak": round(float(K_pl[mask].max()), 1),
    "K_plateau": round(float(np.median(K_pl[mask])), 1)}

OUT["runtime_sec"] = round(time.time() - t0, 1)

ver_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ver_dir, "sim-spectral-estimators-output.json"), "w") as f:
    json.dump(OUT, f, indent=1, default=str)

print("ESTIMATORS_DONE runtime_sec=%s" % OUT["runtime_sec"])
print(json.dumps(OUT["primes"], indent=1))
print(json.dumps(OUT["riemann_zeros"], indent=1))
print(json.dumps(OUT["gue_null"], indent=1))
print(json.dumps(OUT["planted_control"], indent=1))
