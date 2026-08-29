# QNFO.RES.030 P3 — arithmetic cut thermodynamics + matched-density null discrimination
# Golden anchors (limits, Bost-Connes, three-quarters deviation, prime zeta),
# null ensembles N1/N2/N3, D1/D2/D3 discrimination sweep.
# Deterministic seed 20260829. Run from repo root:
#   python arithmetic-cut-discrimination/artifacts/verification/sim-arithmetic-cut-discrimination.py
import json, math, os, time
import numpy as np
from scipy.special import expi

SEED = 20260829
OUT = {"seed": SEED, "p3_task": "cut_discrimination"}
t0 = time.time()

def primes_upto(P):
    sieve = np.ones(P + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(P ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    return np.nonzero(sieve)[0]

def li_exact(x):
    x = np.asarray(x, dtype=float)
    return np.real(expi(np.log(x)))

BETAS = np.logspace(np.log10(0.02), np.log10(12.0), 100)

def cv_mode(betas, lp, stat):
    lp2 = lp * lp
    out = np.empty(len(betas))
    for i, b in enumerate(betas):
        t = np.exp(-b * lp)
        if stat == "B":
            out[i] = b * b * (lp2 * t / (1.0 - t) ** 2).sum()
        elif stat == "F":
            out[i] = b * b * (lp2 * t / (1.0 + t) ** 2).sum()
        else:
            out[i] = b * b * (lp2 * t).sum()
    return out

def rel_l2(a, b, norm):
    return float(np.sqrt(np.mean(((a - b) / norm) ** 2)))

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
            R2 += h / ((n - k) * bw)  # normalize by TOTAL per-order count (n-k), not in-range count
    return 0.5 * (edges[:-1] + edges[1:]), R2

def r2_l2(a, b):
    return float(np.sqrt(np.mean((a - b) ** 2)))

# ---- Golden anchors on the cut ----
P_lim = 1 << 16
ps = primes_upto(P_lim)
lp = np.log(ps.astype(float))
N = len(ps)

cvB_hi = cv_mode(np.array([1e-3]), lp, "B")[0]
b60 = 60.0
ref = b60 ** 2 * math.log(2.0) ** 2 * 2.0 ** (-b60)
OUT["limits"] = {
    "P_max": int(P_lim), "N": int(N),
    "highT_CVB_over_N": round(float(cvB_hi / N), 6), "highT_expectation": 1.0,
    "lowT_collapse_ratio": {
        s: round(float(cv_mode(np.array([b60]), lp, s)[0] / ref), 6)
        for s in ("B", "F", "MB")}}

pole_amp = 1.06 ** 2 / 0.06 ** 2
bc = {}
for Pmax in (10_000, 100_000, 1_000_000):
    pps = primes_upto(Pmax)
    bc[str(Pmax)] = round(float(cv_mode(np.array([1.06]), np.log(pps.astype(float)), "B")[0]), 3)
bc["pole_amplitude"] = round(float(pole_amp), 3)
bc["prime_zeta_P2_truncated"] = round(float((ps.astype(float) ** (-2.0)).sum()), 8)
bc["prime_zeta_P2_known"] = 0.4522474200410655
OUT["bost_connes"] = bc

D = (N - cv_mode(BETAS, lp, "B")) / N
D_F = (N - cv_mode(BETAS, lp, "F")) / N
mask75 = (D >= 0.70) & (D <= 0.80)
OUT["deviation"] = {
    "Bose": {"max_D": round(float(D.max()), 4),
             "beta_where_D_in_070_080": [round(float(b), 3) for b in BETAS[mask75][::15]],
             "n_grid_points_in_070_080": int(mask75.sum()),
             "D_at_beta5": round(float(D[np.argmin(np.abs(BETAS - 5.0))]), 4)},
    "Fermi": {"max_D": round(float(D_F.max()), 4),
              "D_at_beta5": round(float(D_F[np.argmin(np.abs(BETAS - 5.0))]), 4)}}

# ---- Null ensembles ----
def null_smooth(Nn, lo, hi):
    return lo + np.arange(Nn) * (hi - lo) / (Nn - 1.0)

def null_fixed_random(Nn, lo, hi, seed):
    g = np.random.default_rng(seed)
    return np.sort(lo + g.random(Nn) * (hi - lo))

def null_poisson(lo, hi, rate, seed):
    g = np.random.default_rng(seed)
    n = g.poisson(rate * (hi - lo))
    return np.sort(lo + g.random(n) * (hi - lo))

# ---- D1/D2/D3 discrimination sweep ----
M_null = 30
sweep = {}
for Pmax in (1 << 8, 1 << 12, 1 << 16):
    ps_s = primes_upto(Pmax)
    lp_s = np.log(ps_s.astype(float))
    Ns = len(ps_s)
    lo, hi = math.log(2.0), math.log(float(Pmax))
    rate = Ns / (hi - lo)

    # two-point channel: cut level set unfolded by the common li staircase
    u_cut = li_exact(ps_s.astype(float)) - li_exact(2.0)
    _, r2_cut = pair_corr_kth(u_cut)

    entry = {"N": Ns}
    for s in ("B", "F", "MB"):
        cv_cut = cv_mode(BETAS, lp_s, s)
        row = {}
        # N1 deterministic
        n1 = null_smooth(Ns, lo, hi)
        row["N1_cv_distance"] = round(rel_l2(cv_cut, cv_mode(BETAS, n1, s), Ns), 6)
        u_n1 = Ns * (n1 - lo) / (hi - lo)   # N1's own staircase (linear in ln-level)
        _, r2_n1 = pair_corr_kth(u_n1)
        row["N1_r2_distance"] = round(r2_l2(r2_cut, r2_n1), 6)
        # N2, N3 stochastic
        for fam, gen in (("N2", null_fixed_random), ("N3", null_poisson)):
            reals = []
            for i in range(M_null):
                if fam == "N2":
                    lv = gen(Ns, lo, hi, SEED + 1000 * Pmax.bit_length() + i)
                else:
                    lv = gen(lo, hi, rate, SEED + 2000 * Pmax.bit_length() + i)
                reals.append(lv)
            cv_nulls = [cv_mode(BETAS, lv, s) for lv in reals]
            d_cut = np.mean([rel_l2(cv_cut, cvn, Ns) for cvn in cv_nulls])
            d_self = [rel_l2(cv_nulls[i], cv_nulls[j], Ns)
                      for i in range(M_null) for j in range(i + 1, M_null)]
            mean_self = float(np.mean(d_self))
            sig_self = float(np.std(d_self, ddof=1))
            z_cv = (d_cut - mean_self) / sig_self if sig_self > 0 else float("nan")
            r2_nulls = []
            for lv in reals:
                # family smooth staircase: linear in ln-level (the nulls' own mean count)
                u_lv = Ns * (lv - lo) / (hi - lo)
                _, r2_lv = pair_corr_kth(u_lv)
                r2_nulls.append(r2_lv)
            d2_cut = np.mean([r2_l2(r2_cut, r2n) for r2n in r2_nulls])
            d2_self = [r2_l2(r2_nulls[i], r2_nulls[j])
                       for i in range(M_null) for j in range(i + 1, M_null)]
            mean2_self = float(np.mean(d2_self))
            sig2_self = float(np.std(d2_self, ddof=1))
            z_r2 = (d2_cut - mean2_self) / sig2_self if sig2_self > 0 else float("nan")
            row[fam] = {"z_cv": round(float(z_cv), 3),
                        "z_r2": round(float(z_r2), 3),
                        "d_cut_cv": round(float(d_cut), 6),
                        "mean_self_cv": round(float(mean_self), 6),
                        "mean_self_r2": round(mean2_self, 6),
                        "sig_self_cv": round(sig_self, 6),
                        "sig_self_r2": round(sig2_self, 6)}
        entry[s] = row
    sweep[str(Pmax)] = entry
OUT["discrimination_sweep"] = sweep

# ---- hard-core structural discriminator at the largest P_max ----
ps_m = primes_upto(1 << 16)
u_m = li_exact(ps_m.astype(float)) - li_exact(2.0)
s1_m = np.diff(np.sort(u_m))
OUT["hard_core"] = {"P_max": 1 << 16,
                    "cut_s_min": round(float(s1_m.min()), 6),
                    "predicted_2_over_lnP": round(2.0 / math.log(1 << 16), 6),
                    "N2_s_min_typical": round(float(np.diff(null_fixed_random(len(ps_m), math.log(2.0), math.log(1 << 16), SEED + 9)).min()), 6)}

# ---- focused hard-core mass discriminator (nearest-neighbor spacings) ----
thr = 2.0 / math.log(1 << 16)
f_cut = float((s1_m < thr).mean())
fs = []
for i in range(30):
    lv = null_fixed_random(len(ps_m), math.log(2.0), math.log(1 << 16), SEED + 500 + i)
    u_lv = len(ps_m) * (lv - math.log(2.0)) / (math.log(1 << 16) - math.log(2.0))
    s_lv = np.diff(np.sort(u_lv))
    fs.append(float((s_lv < thr).mean()))
fs = np.array(fs)
OUT["hard_core_mass_test"] = {
    "thr_2_over_lnP": round(thr, 6),
    "cut_fraction_below": f_cut,
    "N2_mean_fraction_below": round(float(fs.mean()), 6),
    "N2_std": round(float(fs.std(ddof=1)), 6),
    "z": round(float((f_cut - fs.mean()) / fs.std(ddof=1)), 3)}

OUT["runtime_sec"] = round(time.time() - t0, 1)

ver_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ver_dir, "sim-arithmetic-cut-discrimination-output.json"), "w") as f:
    json.dump(OUT, f, indent=1, default=str)

print("CUT_DISCRIMINATION_DONE runtime_sec=%s" % OUT["runtime_sec"])
print(json.dumps(OUT["limits"], indent=1))
print(json.dumps(OUT["bost_connes"], indent=1))
print(json.dumps(OUT["deviation"], indent=1))
print(json.dumps(OUT["discrimination_sweep"], indent=1))
print(json.dumps(OUT["hard_core"], indent=1))
