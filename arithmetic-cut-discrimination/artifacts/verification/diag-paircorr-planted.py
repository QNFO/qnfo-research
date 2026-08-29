# QNFO.RES.030 P3 — micro-diagnostic for pair_corr_kth and planted control
import math
import numpy as np
from scipy.special import expi

SEED = 20260829

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
            R2 += h / (h.sum() * bw)
    return 0.5 * (edges[:-1] + edges[1:]), R2

# --- A: exact Poisson sanity: k-th-neighbor spacing densities must sum to 1 ---
g = np.random.default_rng(SEED)
pois = np.sort(g.exponential(1.0, 800))
sc, r2 = pair_corr_kth(pois)
print("A: Poisson N=800  MAD_vs_1 =", round(float(np.mean(np.abs(r2 - 1.0))), 4),
      "  mean_R2 =", round(float(r2.mean()), 4))
print("A: first 8 bins R2:", np.round(r2[:8], 3))

# --- B: GUE n=800 control vs analytic GUE ---
def semicircle_cdf(x, n):
    a = 2.0 * math.sqrt(n)
    r = np.clip(x / a, -1.0, 1.0)
    return 0.5 + np.arcsin(r) / np.pi + r * np.sqrt(1.0 - r * r) / np.pi

def gue_sample(n, seed):
    g2 = np.random.default_rng(seed)
    X = g2.standard_normal((n, n))
    Y = g2.standard_normal((n, n))
    A = (X + X.T) / 2.0 + 1j * (Y - Y.T) / 2.0
    ev = np.sort(np.linalg.eigvalsh(A))
    return semicircle_cdf(ev, n) * n

def gue_r2(s):
    x = np.pi * s
    return 1.0 - (np.sin(x) / x) ** 2

gu = gue_sample(800, SEED + 100)
sc, r2g = pair_corr_kth(gu, kmax=20)
print("B: GUE n=800 MAD_vs_analytic =", round(float(np.mean(np.abs(r2g - gue_r2(sc)))), 4))
print("B: R2 at s=0.1,0.5,1.0,2.0:", np.round([r2g[np.argmin(abs(sc-s))] for s in (0.1,0.5,1.0,2.0)], 3))
print("B: analytic:", np.round([gue_r2(np.array([0.1,0.5,1.0,2.0]))], 3))

# --- C: planted sample — density check + form factor at specific tau ---
def planted_u(N, eps, lam_u, seed):
    g3 = np.random.default_rng(seed)
    out = []
    while len(out) < N:
        uu = g3.random(4 * N) * N
        a = 0.5 * (1.0 + eps * np.cos(2.0 * np.pi * uu / lam_u))
        keep = g3.random(4 * N) < a
        out.extend(uu[keep].tolist())
    return np.sort(np.asarray(out[:N]))

N, eps, lam_u = 4000, 0.2, math.log(4.0)
upl = planted_u(N, eps, lam_u, SEED + 7)
# density histogram: 40 bins over [0, N]
h, edges = np.histogram(upl, bins=40, range=(0, N))
d = h / (h.sum() * (N / 40.0))
print("C: density bins (first 10):", np.round(d[:10], 3), " min/max:", round(d.min(),3), round(d.max(),3))

def form_factor(u, taus):
    K = np.empty(len(taus))
    for i, tau in enumerate(taus):
        K[i] = np.abs(np.exp(2j * np.pi * tau * u).sum()) ** 2 / len(u)
    return K

for tau in (0.4, 0.7213, 1.0, 1.4, 2.03):
    K = form_factor(upl, np.array([tau]))[0]
    print("C: K(tau=%.3f) = %.2f" % (tau, K))

# FFT of the histogram: dominant period
print("C: histogram FFT peak (bin, period):", end=" ")
hh = d - d.mean()
ff = np.abs(np.fft.rfft(hh))
top = np.argsort(ff)[-3:]
for t in top:
    print("(k=%d, period_u=%.3f)" % (t, N / max(t, 1)), end=" ")
print()
