# QNFO.RES.030 P4 red-team diagnostic: number-variance estimator edge effects
# + N1-vs-stochastic-null cross-check from the committed P3 outputs.
import json, math, os
import numpy as np

SEED = 20260829
ver_dir = os.path.dirname(os.path.abspath(__file__))

def number_variance(u, L, lo_margin=0.0, hi_margin=0.0):
    u = np.sort(np.asarray(u, dtype=float))
    lo, hi = u[0], u[-1]
    lo_eff = lo + lo_margin
    hi_eff = hi - hi_margin
    nwin = int((hi_eff - lo_eff) // L)
    if nwin < 4:
        return float("nan"), int(nwin)
    starts = lo_eff + np.arange(nwin) * L
    cnt = np.array([((u >= s) & (u < s + L)).sum() for s in starts])
    return float(cnt.var(ddof=1)), int(nwin)

def dyson_sigma2(L):
    gamma = 0.5772156649015329
    return (1.0 / np.pi ** 2) * (np.log(2.0 * np.pi * L) + 1.0 + gamma - np.pi ** 2 / 8.0)

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

out = {}

# 1. uniform grid sanity
ug = np.arange(800.0)
out["uniform_grid_L10"] = number_variance(ug, 10.0)[0]

# 2. exact Poisson sanity (cumsum of exponential spacings)
g = np.random.default_rng(SEED)
up = np.cumsum(g.exponential(1.0, 900))
up = up[up <= 800.0]
out["poisson_L10"] = number_variance(up, 10.0)[0]
out["poisson_L10_expect"] = 10.0

# 3. GUE n=800, M=16: full-range vs interior (edge margin 2L)
for L in (10.0, 20.0):
    vals_full, vals_in = [], []
    for i in range(16):
        uu = gue_sample(800, SEED + 100 + i)
        vals_full.append(number_variance(uu, L)[0])
        vals_in.append(number_variance(uu, L, lo_margin=2 * L, hi_margin=2 * L)[0])
    out[f"GUE800_L{int(L)}"] = {
        "full_range_mean": round(float(np.mean(vals_full)), 6),
        "interior_mean": round(float(np.mean(vals_in)), 6),
        "interior_std": round(float(np.std(vals_in, ddof=1)), 6),
        "dyson": round(dyson_sigma2(L), 6),
        "interior_ratio": round(float(np.mean(vals_in)) / dyson_sigma2(L), 4)}

# 4. GUE n=2000, M=4, interior
for L in (10.0, 20.0):
    vals = [number_variance(gue_sample(2000, SEED + 200 + i), L, 2 * L, 2 * L)[0] for i in range(4)]
    out[f"GUE2000_L{int(L)}"] = {
        "interior_mean": round(float(np.mean(vals)), 6),
        "dyson": round(dyson_sigma2(L), 6),
        "interior_ratio": round(float(np.mean(vals)) / dyson_sigma2(L), 4)}

# 5. N1-vs-stochastic-null cross-check from committed P3 outputs
data = json.load(open(os.path.join(ver_dir, "sim-arithmetic-cut-discrimination-output.json")))
sw = data["discrimination_sweep"]
out["N1_cross_check_Bose"] = {}
for Pmax in ("256", "4096", "65536"):
    row = sw[Pmax]["B"]
    n1d = row["N1_cv_distance"]
    z2 = (n1d - row["N2"]["mean_self_cv"]) / row["N2"]["sig_self_cv"]
    z3 = (n1d - row["N3"]["mean_self_cv"]) / row["N3"]["sig_self_cv"]
    out["N1_cross_check_Bose"][Pmax] = {
        "N1_distance": n1d,
        "z_vs_N2_self": round(z2, 2),
        "z_vs_N3_self": round(z3, 2)}

print(json.dumps(out, indent=1))
