"""
=============================================================================
Unity of Ultrametric Physics — Collider Step Predictor
=============================================================================

This module predicts p-adic step-like corrections to Standard Model cross
sections at current and future colliders (LHC, HL-LHC, FCC-hh, Muon Collider).

In the Unity framework, each p-adic tree level that unfreezes at energy
E ∼ p^n Λ_0 produces a step in the cross section. The corrections are:

    σ(s)/σ_SM(s) - 1 = Σ_p ε_p · Θ_smeared(√s / Λ_p)

where Θ_smeared is a step function smoothed by experimental resolution.

Usage:
    >>> from collider_predictor import predict_lhc_steps, predict_fcc_steps
    >>> sqrts, sigma = predict_lhc_steps()
    >>> sqrts_fcc, sigma_fcc = predict_fcc_steps()
"""

import numpy as np
from typing import Dict, Tuple


def smeared_step(x: float, x0: float, resolution: float = 0.05) -> float:
    """
    Smoothed step function using tanh.

    Args:
        x: The variable (e.g., √s).
        x0: The threshold value (e.g., Λ_p).
        resolution: Relative resolution Δx/x (default 5%).

    Returns:
        Value in [0, 1] representing the smoothed step.
    """
    return 0.5 * (1.0 + np.tanh((x - x0) / (resolution * x0)))


def collider_step_predictor(
    sqrts_values: np.ndarray,
    sigma_sm: np.ndarray,
    lambda_p_dict: Dict[int, float],
    epsilon_p_dict: Dict[int, float],
    resolution: float = 0.05,
) -> np.ndarray:
    """
    Compute p-adic step corrections to a cross section.

    Args:
        sqrts_values: Array of √s values in GeV.
        sigma_sm: Standard Model cross section at each √s.
        lambda_p_dict: Dict mapping prime p → threshold Λ_p in GeV.
        epsilon_p_dict: Dict mapping prime p → step size ε_p.
        resolution: Experimental resolution Δ√s/√s.

    Returns:
        Corrected cross section array.
    """
    sigma_corrected = sigma_sm.copy()

    for p, Lam in lambda_p_dict.items():
        eps = epsilon_p_dict.get(p, 0.0)

        for i, sqrts in enumerate(sqrts_values):
            # Number of unfrozen tree levels at this energy
            if sqrts > Lam:
                n_max = int(np.floor(np.log(sqrts / Lam) / np.log(p)))
                # Each unfrozen level contributes ε_p · p^{-n}
                corr = eps * sum(p ** (-n) for n in range(1, max(0, n_max) + 1))
            else:
                corr = 0.0

            # Smear with experimental resolution
            smearing = smeared_step(sqrts, Lam, resolution)
            sigma_corrected[i] *= (1.0 + corr * smearing)

    return sigma_corrected


def predict_lhc_steps(
    n_points: int = 200,
    resolution: float = 0.05,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Predict p-adic step corrections for LHC energies (1-14 TeV).

    Args:
        n_points: Number of √s points.
        resolution: Experimental resolution.

    Returns:
        (sqrts_gev, sigma_sm, sigma_corrected) arrays.
    """
    sqrts_gev = np.logspace(3, 4.15, n_points)  # 1 TeV to ~14 TeV

    # Rough SM cross-section scaling: σ ∼ 1/s
    sigma_sm = 1.0 / sqrts_gev ** 2 * 1e8

    lambda_p = {
        2: 2500.0,   # Λ_2 = 2.5 TeV
        3: 7000.0,   # Λ_3 = 7 TeV
    }
    epsilon_p = {
        2: 3.0e-3,
        3: 2.0e-3,
    }

    sigma_corr = collider_step_predictor(sqrts_gev, sigma_sm, lambda_p, epsilon_p, resolution)

    return sqrts_gev, sigma_sm, sigma_corr


def predict_fcc_steps(
    n_points: int = 200,
    resolution: float = 0.05,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Predict p-adic step corrections for FCC-hh energies (1-100 TeV).

    Args:
        n_points: Number of √s points.
        resolution: Experimental resolution.

    Returns:
        (sqrts_gev, sigma_sm, sigma_corrected) arrays.
    """
    sqrts_gev = np.logspace(3, 5, n_points)  # 1 TeV to 100 TeV

    sigma_sm = 1.0 / sqrts_gev ** 2 * 1e8

    lambda_p = {
        2: 2500.0,    # Λ_2 = 2.5 TeV
        3: 7000.0,    # Λ_3 = 7 TeV
        5: 25000.0,   # Λ_5 = 25 TeV  ← FCC target
    }
    epsilon_p = {
        2: 3.0e-3,
        3: 2.0e-3,
        5: 1.0e-3,
    }

    sigma_corr = collider_step_predictor(sqrts_gev, sigma_sm, lambda_p, epsilon_p, resolution)

    return sqrts_gev, sigma_sm, sigma_corr


def predict_muon_collider_steps(
    n_points: int = 100,
    resolution: float = 0.01,  # Muon collider has better resolution
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Predict p-adic step corrections for a Muon Collider (1-10 TeV).

    The muon collider can scan √s in fine steps, directly mapping the
    staircase pattern at Λ_2 and Λ_3.

    Args:
        n_points: Number of √s points.
        resolution: Experimental resolution (better than hadron colliders).

    Returns:
        (sqrts_gev, sigma_sm, sigma_corrected) arrays.
    """
    sqrts_gev = np.linspace(1000, 10000, n_points)  # 1-10 TeV

    # μ⁺μ⁻ → qq̄ cross section (rough scaling)
    sigma_sm = 1.0 / sqrts_gev ** 2 * 1e6

    lambda_p = {
        2: 2500.0,
        3: 7000.0,
    }
    epsilon_p = {
        2: 3.0e-3,
        3: 2.0e-3,
    }

    sigma_corr = collider_step_predictor(sqrts_gev, sigma_sm, lambda_p, epsilon_p, resolution)

    return sqrts_gev, sigma_sm, sigma_corr


# =============================================================================
# Example usage
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Collider Step Predictor — Ultrametric Signatures")
    print("=" * 60)

    # LHC predictions
    print("\n--- LHC (1-14 TeV) ---")
    sqrts, sm, corr = predict_lhc_steps()
    # Find the biggest deviation
    ratio = corr / sm
    max_dev = np.max(np.abs(ratio - 1.0))
    max_idx = np.argmax(np.abs(ratio - 1.0))
    print(f"Maximum deviation: {max_dev * 100:.3f}% at √s = {sqrts[max_idx]:.0f} GeV")
    print(f"Λ_2 step expected at: 2500 GeV")
    print(f"Λ_3 step expected at: 7000 GeV")

    # FCC-hh predictions
    print("\n--- FCC-hh (1-100 TeV) ---")
    sqrts_fcc, sm_fcc, corr_fcc = predict_fcc_steps()
    ratio_fcc = corr_fcc / sm_fcc
    max_dev_fcc = np.max(np.abs(ratio_fcc - 1.0))
    max_idx_fcc = np.argmax(np.abs(ratio_fcc - 1.0))
    print(f"Maximum deviation: {max_dev_fcc * 100:.3f}% at √s = {sqrts_fcc[max_idx_fcc]:.0f} GeV")
    print(f"Λ_5 step expected at: 25000 GeV (primary FCC target)")

    # Muon Collider predictions
    print("\n--- Muon Collider (1-10 TeV) ---")
    sqrts_mc, sm_mc, corr_mc = predict_muon_collider_steps()
    ratio_mc = corr_mc / sm_mc
    # Find steps
    for i in range(1, len(sqrts_mc) - 1):
        diff = ratio_mc[i] - ratio_mc[i-1]
        if abs(diff) > 5e-5:  # Significant step
            print(f"Step detected at √s ≈ {sqrts_mc[i]:.0f} GeV: Δσ/σ = {diff * 100:.4f}%")
            break

    print("\nDone.")
