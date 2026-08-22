#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QNFO.RES.018 — REG-RES018-002 sealed harness: minimal stochastic extension.
Seal commit + sha256 recorded in artifacts/pre-registration-002.md (KIF-60 HARD).
DO NOT MODIFY after seal; any edit requires a new pre-registration.

Design (sealed decisions, per the scaffold):
  - Noise: additive WHITE noise on the z-coordinate ONLY, active ONLY during the
    measurement window (Wu-2013 consistency: noise off outside measurement).
    Per RK4 relaxation step: z += sigma * sqrt(dt) * xi, xi ~ N(0,1) i.i.d.
  - Analytic primary computation (exact for the sealed family):
    The z-drift of variants A/B/C is LINEAR in z with deterministic coefficients
    (x,y are unaffected by z-noise). The discrete relaxation map is therefore
    z_{k+1} = A_k z_k + b_k (+ noise), with A_k the exact z-Jacobian of the RK4
    update (finite-difference probe; exact because the map is affine in z).
    z_final = z_det + sum_j S_j sigma sqrt(dt) xi_j, a Gaussian with variance
    sigma^2 * V,  V = sum_j S_j^2 dt,  S_j = prod_{k>j} A_k.
    P(+) = Phi(z_det / (sigma * sqrt(V))).
  - Monte Carlo VALIDATION (implementation check): 3 (variant, sigma) configs x
    14 states x N=1e5 independent shot noise-paths, propagated through the SAME
    A_k/b_k discrete map; assert |P_MC - P_analytic| < MC_TOL = 5e-3
    (sampling-limited: binomial std ~1.6e-3 at p~0.5; ~3-sigma budget).
  - sigma grid: logspace(-3, 0, 21). sigma_min = smallest grid sigma with
    max_dev < EPS, then log-bisection (20 iterations) to 2 significant figures.
  - RNG: fixed seeds; random test states reproduced EXACTLY from the sealed
    SEED=20260819 draw (asserted against the REG-RES018-001 verdict-input.json).
Produces: artifacts/verdict-input-002.json
"""
import json
import hashlib
import numpy as np
from scipy.special import erf

from relaxation_sim import (TEST_STATES, EPS, N_SHOTS, DT_FACTOR, SEED,
                            bloch_to_rho, rho_to_bloch, unitary_step,
                            relaxation_A, relaxation_B, relaxation_C,
                            rk4_relax)

SEED_EXT = 20260821
SIGMA_GRID = list(np.logspace(-3.0, 0.0, 21))
MC_CHECK_CONFIGS = [('A', 0.01, 0.5), ('B', 0.1, 5.0), ('C', 0.1, 5.0)]  # (variant, sigma, gamma_tau); gamma_m = gamma_tau / tau_m
MC_CHECK_STATES = list(range(9)) + [9, 15, 30, 45, 58]
MC_TOL = 5e-3
BISECT_ITERS = 20
PROBE_DELTA = 1e-7


def deterministic_path(x0, y0, z0, t_m, gamma_m, variant, alpha):
    """Unitary evolution + relaxation; returns (z_det, V, A_list, b_list)
    for the discrete map z_{k+1} = A_k z_k + b_k. Exact for the sealed family
    (affine-in-z RK4 update)."""
    rho = bloch_to_rho(x0, y0, z0)
    dt_u = t_m / 100
    for _ in range(100):
        rho = unitary_step(rho, dt_u)
    x, y, z = rho_to_bloch(rho)
    dt_r = t_m / DT_FACTOR
    if variant == 'A':
        relax = relaxation_A
        params = (gamma_m,)
    elif variant == 'B':
        relax = relaxation_B
        params = (gamma_m, alpha)
    elif variant == 'C':
        relax = relaxation_C
        params = (gamma_m, z0)
    else:
        raise ValueError(variant)

    A_list = []
    b_list = []
    for _ in range(DT_FACTOR):
        nx, ny, nz = rk4_relax(x, y, z, dt_r, relax, params)
        _, _, nz_p = rk4_relax(x, y, z + PROBE_DELTA, dt_r, relax, params)
        A_k = (nz_p - nz) / PROBE_DELTA
        A_list.append(float(A_k))
        b_list.append(float(nz - A_k * z))
        x, y, z = nx, ny, nz
    V = 0.0
    S = 1.0
    for A_k in reversed(A_list):
        S = S * A_k
        V += S * S * dt_r
    return float(z), float(V), A_list, b_list


def analytic_p_plus(z_det, V, sigma):
    if V <= 0.0:
        return 1.0 if z_det >= 0.0 else 0.0
    return 0.5 * (1.0 + erf(z_det / (sigma * np.sqrt(2.0 * V))))


def mc_p_plus(A_list, b_list, z_start, dt_r, sigma, seed):
    """Monte Carlo through the SAME discrete map z_{k+1} = A_k z + b_k + noise."""
    rng = np.random.default_rng(seed)
    zvec = np.full(N_SHOTS, z_start, dtype=float)
    for A_k, b_k in zip(A_list, b_list):
        zvec = A_k * zvec + b_k
        zvec = zvec + sigma * np.sqrt(dt_r) * rng.standard_normal(N_SHOTS)
    return float(np.mean(zvec >= 0.0))


def random_test_states(n=50, seed=SEED):
    rng = np.random.default_rng(seed)
    return [tuple(float(c) for c in (rng.standard_normal(3) / np.linalg.norm(rng.standard_normal(3)))) for _ in range(n)]


def load_sealed_states():
    with open('artifacts/verdict-input.json', encoding='utf-8') as f:
        v1 = json.load(f)
    first = next(iter(v for v in v1.values() if isinstance(v, dict) and 'results' in v))
    return [tuple(r['state']) for r in first['results']]


def main():
    sealed_states = load_sealed_states()
    mine = list(TEST_STATES) + random_test_states(50)
    assert all(np.allclose(np.array(a), np.array(b)) for a, b in zip(sealed_states, mine)), \
        "state-set reproduction mismatch vs sealed REG-RES018-001"
    print(f"state-set reproduction: OK ({len(mine)} states match the sealed draw)")

    summary = {}
    configs = [('A', g_tau, 1.0, 0.0) for g_tau in (0.5, 5.0, 50.0)] + \
              [('B', 5.0, 1.0, a) for a in (0.01, 0.1, 1.0)] + \
              [('C', 5.0, 1.0, 0.0)]
    dt_r = 1.0 / DT_FACTOR

    # Precompute deterministic paths per config x state (shared across sigma)
    paths = {}
    for ci, (variant, gamma_tau, tau_m, alpha) in enumerate(configs):
        gamma_m = gamma_tau / tau_m
        for si, (x0, y0, z0) in enumerate(mine):
            paths[(ci, si)] = deterministic_path(x0, y0, z0, tau_m, gamma_m, variant, alpha)

    for ci, (variant, gamma_tau, tau_m, alpha) in enumerate(configs):
        per_sigma = {}
        for sigma in SIGMA_GRID:
            devs = []
            for si, (x0, y0, z0) in enumerate(mine):
                z_det, V, _, _ = paths[(ci, si)]
                p = analytic_p_plus(z_det, V, sigma)
                devs.append(abs(p - (1 + z0) / 2.0))
            per_sigma[str(float(sigma))] = {'max_deviation': float(max(devs)),
                                            'pass': max(devs) < EPS}
        passing = [s for s in SIGMA_GRID if per_sigma[str(float(s))]['pass']]
        sigma_min = None
        if passing:
            s_hi = min(passing)
            s_lo = max([s for s in SIGMA_GRID if s < s_hi], default=None)
            s_lo = s_lo if s_lo is not None else 1e-6
            for _ in range(BISECT_ITERS):
                s_mid = np.sqrt(s_lo * s_hi)
                devs = []
                for si, (x0, y0, z0) in enumerate(mine):
                    z_det, V, _, _ = paths[(ci, si)]
                    devs.append(abs(analytic_p_plus(z_det, V, s_mid) - (1 + z0) / 2.0))
                if max(devs) < EPS:
                    s_hi = s_mid
                else:
                    s_lo = s_mid
            sigma_min = float(s_hi)
        name = f"{variant}_gamma_tau_{gamma_tau}_alpha_{alpha}" if variant == 'B' else \
               (f"{variant}_gamma_tau_{gamma_tau}" if variant == 'A' else "C")
        summary[name] = {'variant': variant, 'gamma_tau': gamma_tau,
                         'tau_m': tau_m, 'alpha': alpha,
                         'per_sigma': per_sigma, 'sigma_min': sigma_min,
                         'cc2_pass': sigma_min is not None}
        print(f"{name}: sigma_min={sigma_min} cc2_pass={sigma_min is not None}")

    # ---- MC validation layer ----
    mc = {}
    for (variant, sigma, gamma_tau) in MC_CHECK_CONFIGS:
        tau_m = 1.0
        ci = configs.index((variant, gamma_tau, tau_m, 0.1 if variant == 'B' else 0.0))
        for idx in MC_CHECK_STATES:
            z_det, V, A_list, b_list = paths[(ci, idx)]
            p_an = analytic_p_plus(z_det, V, sigma)
            x0, y0, z0 = mine[idx]
            rho = bloch_to_rho(x0, y0, z0)
            dt_u = tau_m / 100
            for _ in range(100):
                rho = unitary_step(rho, dt_u)
            _, _, z_start = rho_to_bloch(rho)
            p_mc = mc_p_plus(A_list, b_list, z_start, dt_r, sigma, seed=SEED_EXT + idx)
            assert abs(p_mc - p_an) < MC_TOL, \
                f"MC validation failed {variant} sigma={sigma} idx={idx}: {p_mc} vs {p_an}"
            mc[f"{variant}_{sigma}_{idx}"] = {'p_analytic': float(p_an), 'p_mc': float(p_mc)}
        print(f"MC validation OK: variant={variant} sigma={sigma} ({len(MC_CHECK_STATES)} states, tol {MC_TOL})")

    summary['_mc_validation'] = mc
    summary['_seal_sha256'] = hashlib.sha256(open(__file__, encoding='utf-8').read().encode('utf-8')).hexdigest()

    with open('artifacts/verdict-input-002.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=1)
    print('seal_sha256:', summary['_seal_sha256'])


if __name__ == '__main__':
    main()
