#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QNFO.RES.018 — Sealed simulation harness (REG-RES018-001)
Measurement-triggered relaxation dynamics, 2-level system, Bloch sphere.

DO NOT MODIFY: any edit invalidates the pre-registration seal (KIF-60 HARD).
Run: python relaxation_sim.py  (produces artifacts/verdict-input.json only;
the verdict analysis is a separate sealed analysis script.)
"""
import json
import hashlib
import numpy as np

# ---------- Sealed parameters (REG-RES018-001) ----------
OMEGA = 1.0            # H = omega * sigma_z / 2
EPS = 1e-2             # Born-rule tolerance
N_SHOTS = 100_000      # shots per state
DT_FACTOR = 500        # RK4 steps per tau_m
SEED = 20260819        # fixed RNG seed (reproducibility)

TEST_STATES = [
    (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0),
    (-1.0, 0.0, 0.0), (0.0, -1.0, 0.0), (0.0, 0.0, -1.0),
    (1 / np.sqrt(2), 1 / np.sqrt(2), 0.0),
    (1 / np.sqrt(2), 0.0, 1 / np.sqrt(2)),
    (0.0, 1 / np.sqrt(2), 1 / np.sqrt(2)),
]


# ---------- Pauli matrix helpers ----------
def hamiltonian_matrix():
    return np.diag([OMEGA / 2.0, -OMEGA / 2.0])


def bloch_to_rho(x, y, z):
    return 0.5 * np.array([[1 + z, x - 1j * y],
                           [x + 1j * y, 1 - z]], dtype=complex)


def rho_to_bloch(rho):
    x = 2 * rho[0, 1].real
    y = -2 * rho[0, 1].imag
    z = 2 * rho[0, 0].real - 1
    return x, y, z


# ---------- Relaxation operators (sealed family) ----------
def relaxation_A(x, y, z, gamma_m):
    """Variant A: pure eigenbasis attraction. Preserves z exactly."""
    return -gamma_m * x, -gamma_m * y, 0.0


def relaxation_B(x, y, z, gamma_m, alpha):
    """Variant B: xy attraction + generic dissipative z-perturbation."""
    dx = -gamma_m * x
    dy = -gamma_m * y
    dz = -alpha * (x * x + y * y) * z
    return dx, dy, dz


def relaxation_C(x, y, z, gamma_m, z0):
    """Variant C: radial-basis basins toward the eigenbasis equator,
    weights fixed from the PRE-relaxation state only (sealed rule)."""
    target_z = np.tanh(z0)  # fixed function of initial z0; no per-shot inputs
    return -gamma_m * x, -gamma_m * y, -gamma_m * (z - target_z)


# ---------- Unitary evolution (Schroedinger) ----------
def unitary_step(rho, dt):
    H = hamiltonian_matrix()
    U = np.linalg.expm(-1j * H * dt)
    return U @ rho @ U.conj().T


# ---------- RK4 relaxation step ----------
def rk4_relax(x, y, z, dt, relax_fn, params):
    def f(xx, yy, zz):
        return relax_fn(xx, yy, zz, *params)

    k1x, k1y, k1z = f(x, y, z)
    k2x, k2y, k2z = f(x + 0.5 * dt * k1x, y + 0.5 * dt * k1y, z + 0.5 * dt * k1z)
    k3x, k3y, k3z = f(x + 0.5 * dt * k2x, y + 0.5 * dt * k2y, z + 0.5 * dt * k2z)
    k4x, k4y, k4z = f(x + dt * k3x, y + dt * k3y, z + dt * k3z)
    nx = x + dt / 6.0 * (k1x + 2 * k2x + 2 * k3x + k4x)
    ny = y + dt / 6.0 * (k1y + 2 * k2y + 2 * k3y + k4y)
    nz = z + dt / 6.0 * (k1z + 2 * k2z + 2 * k3z + k4z)
    return nx, ny, nz


# ---------- Single-shot outcome ----------
def single_shot(x0, y0, z0, t_m, gamma_m, variant, alpha=0.0):
    """Evolve unitarily to t_m, then relax for t_m, then threshold."""
    rho = bloch_to_rho(x0, y0, z0)
    dt_u = t_m / 100
    for _ in range(100):
        rho = unitary_step(rho, dt_u)

    x, y, z = rho_to_bloch(rho)
    dt_r = t_m / DT_FACTOR
    steps = DT_FACTOR

    if variant == 'A':
        relax = relaxation_A
        params = (gamma_m,)
    elif variant == 'B':
        relax = relaxation_B
        params = (gamma_m, alpha)
    elif variant == 'C':
        relax = relaxation_C
        params = (gamma_m, z0)  # z0 = pre-relaxation z (sealed rule)
    else:
        raise ValueError(f'unknown variant {variant}')

    for _ in range(steps):
        x, y, z = rk4_relax(x, y, z, dt_r, relax, params)

    return 1 if z >= 0.0 else 0


# ---------- Batch run ----------
def run_variant(variant, gamma_m, tau_m, alpha=0.0, random_states=50, seed=SEED):
    rng = np.random.default_rng(seed)
    states = list(TEST_STATES)
    for _ in range(random_states):
        v = rng.standard_normal(3)
        v = v / np.linalg.norm(v)
        states.append(tuple(v))

    results = []
    for (x0, y0, z0) in states:
        p_born = (1 + z0) / 2.0
        rng_local = np.random.default_rng(seed + int(round((x0 + 2) * 1e4)))
        hits = sum(
            single_shot(x0, y0, z0, tau_m, gamma_m, variant, alpha)
            for _ in range(N_SHOTS)
        )
        p_meas = hits / N_SHOTS
        dev = abs(p_meas - p_born)
        results.append({'state': [x0, y0, z0], 'p_born': p_born,
                        'p_measured': p_meas, 'deviation': dev})

    max_dev = max(r['deviation'] for r in results)
    return {'variant': variant, 'gamma_m': gamma_m, 'tau_m': tau_m,
            'alpha': alpha, 'max_deviation': max_dev, 'eps': EPS,
            'pass': max_dev < EPS, 'results': results}


# ---------- Main ----------
def main():
    summary = {}
    for gamma_m_tau in [0.5, 5.0, 50.0]:
        tau_m = 1.0
        gamma_m = gamma_m_tau / tau_m
        summary[f'A_gamma_tau_{gamma_m_tau}'] = run_variant('A', gamma_m, tau_m)
    for alpha in [0.01, 0.1, 1.0]:
        summary[f'B_alpha_{alpha}'] = run_variant('B', 5.0, 1.0, alpha=alpha)
    summary['C'] = run_variant('C', 5.0, 1.0)

    # Seal hash self-check
    code = open(__file__, encoding='utf-8').read()
    h = hashlib.sha256(code.encode('utf-8')).hexdigest()
    summary['_seal_sha256'] = h

    with open('artifacts/verdict-input.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=1)
    print('seal_sha256:', h)
    for k, v in summary.items():
        if not k.startswith('_'):
            print(f"{k}: max_dev={v['max_deviation']:.6f} PASS={v['pass']}")


if __name__ == '__main__':
    main()
