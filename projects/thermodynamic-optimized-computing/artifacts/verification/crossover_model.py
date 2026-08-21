#!/usr/bin/env python3
"""Protection-vs-QEC energy crossover model for QNFO.JPC.002 (P3).

Models the trade-off surface of the paper's central hypothesis:
active error correction (surface-code family, overhead ~ distance^2, logical
error falling with distance) versus hardware protection (thermal-activation
logical error ~ A exp(-Delta/k_B T), no correction block).

Standard library only. Seeded. Run: python crossover_model.py
Output: artifacts/verification/outputs/crossover_results.csv,
        artifacts/verification/outputs/mc_winner_samples.csv + console.
"""
import math, csv, os, random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
os.makedirs(OUT, exist_ok=True)

K_B = 1.380649e-23

# --- Model parameters ---
E_OP   = 8.21e-25   # J per physical gate (Rosetta constant, corpus anchor)
N_OPS  = 1e6        # logical operations in the benchmark computation
P_TH   = 1.1e-2     # surface-code circuit-level threshold (published ~1e-2)

def exp_safe(x: float) -> float:
    """Bounded exponential: return inf instead of overflowing."""
    return math.exp(x) if x < 700.0 else float("inf")

def distance_of(p: float) -> float:
    """Heuristic code distance for physical error rate p below threshold."""
    if p >= P_TH:
        return 0.0
    return max(3.0, 3.0 + 2.0 * math.log(P_TH / p))

def surface_overhead(p: float, delta: float = 1.0) -> float:
    """Physical-qubits-per-logical-qubit overhead, ~d^2, decoder efficiency delta."""
    d = distance_of(p)
    if d == 0.0:
        return float("inf")
    return 10.0 * d * d / delta

def logical_error_qec(p: float) -> float:
    """Logical error rate under surface-code QEC (heuristic exponential in d)."""
    d = distance_of(p)
    if d == 0.0:
        return 1.0
    return 0.1 * (p / P_TH) ** (d / 2.0)

def E_qec(p: float, delta: float = 1.0) -> float:
    eta = surface_overhead(p, delta)
    L   = logical_error_qec(p)
    return E_OP * eta * N_OPS * exp_safe(N_OPS * L)

def E_passive(Delta: float, T: float, A: float = 1.0) -> float:
    L = min(A * math.exp(-Delta / (K_B * T)), 0.5)
    return E_OP * 1.0 * N_OPS * exp_safe(N_OPS * L)

def main():
    header = ["delta_decoder", "T_K", "Delta_J", "p_best_QEC",
              "E_QEC_J", "E_passive_J", "winner", "E_passive_over_E_QEC"]
    P_SWEEP = [1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 5e-3]

    with open(os.path.join(OUT, "crossover_results.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        print(",".join(header))
        for delta in (0.5, 1.0):
            for T in (0.015, 0.1, 1.0, 4.0):
                for Delta in (1e-22, 5e-23, 2e-23, 1e-23):
                    E_pass = E_passive(Delta, T)
                    p_star, E_qec_star = min(((p, E_qec(p, delta)) for p in P_SWEEP),
                                             key=lambda t: t[1])
                    winner = "PASSIVE" if E_pass < E_qec_star else "QEC"
                    ratio = E_pass / E_qec_star
                    row = [delta, T, f"{Delta:.2e}", f"{p_star:.2e}",
                           f"{E_qec_star:.3e}", f"{E_pass:.3e}", winner, f"{ratio:.3e}"]
                    w.writerow(row)
                    print(",".join(map(str, row)))

    # Seeded Monte Carlo: P(passive beats QEC) under log-uniform p uncertainty
    # at the flagship operating point (T = 15 mK, Delta = 1e-22 J).
    random.seed(20260821)
    T0, D0 = 0.015, 1e-22
    E_pass0 = E_passive(D0, T0)
    n_pass = 0
    with open(os.path.join(OUT, "mc_winner_samples.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["p_physical", "E_QEC_J", "passive_wins"])
        for _ in range(1000):
            p = 10.0 ** random.uniform(-5.0, -2.0)
            E_qec_sample = E_qec(p, 1.0)
            wins = 1 if E_pass0 < E_qec_sample else 0
            n_pass += wins
            w.writerow([f"{p:.4e}", f"{E_qec_sample:.4e}", wins])
    print(f"\nMC (seed 20260821, n=1000): P(passive beats QEC | T={T0}K, "
          f"Delta={D0:.1e}J, log10(p)~U[-5,-2]) = {n_pass/1000:.3f}")

if __name__ == "__main__":
    main()
