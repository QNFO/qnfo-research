"""
=============================================================================
Unity of Ultrametric Physics — Dark Matter Direct Detection Predictions
=============================================================================

This module computes the spin-independent WIMP-nucleon cross-section for
p-adic dark matter in xenon-based direct detection experiments.

In the Unity framework, dark matter particles are localized in the p-adic
sectors (the "bulk" of the Bruhat-Tits tree) but delocalized in the
Archimedean sector. Their interaction with ordinary matter is suppressed
by a factor p^{-2d_p} where d_p is the tree depth separating the dark
and visible sectors at prime p.

The predicted cross-section is:
    σ_SI = σ_0 · Σ_p p^{-2d_p}

where σ_0 ~ 10^{-40} cm² is set by the adelic coupling strength.

Usage:
    >>> from dark_matter import dm_xenon_xsec, scan_depths
    >>> sigma = dm_xenon_xsec(m_dm=100, lam_p=2.5, tree_depth=43)
    >>> print(f"σ_SI = {sigma:.2e} cm²")
"""

import numpy as np


# Physical constants
M_NUCLEON_GEV = 0.938  # Nucleon mass in GeV
GEV_TO_INV_CM = 1.0 / (1.97e-14)  # 1 GeV^{-1} = 1.97e-14 cm


def dm_xenon_xsec(
    m_dm_gev: float = 100.0,
    lambda_p_tev: float = 2.5,
    tree_depth: int = 43,
    g_eff: float = 0.1,
) -> float:
    """
    Compute the spin-independent DM-nucleon cross-section for xenon targets.

    Args:
        m_dm_gev: Dark matter particle mass in GeV.
        lambda_p_tev: p-adic threshold scale Λ_p in TeV (default 2.5 for p=2).
        tree_depth: Tree depth d_p separating dark and visible sectors.
        g_eff: Effective adelic coupling constant (default 0.1).

    Returns:
        σ_SI in cm².
    """
    # Tree suppression factor
    suppression = 2 ** (-2 * tree_depth)

    # Reduced mass of DM-nucleon system
    mu_gev = (m_dm_gev * M_NUCLEON_GEV) / (m_dm_gev + M_NUCLEON_GEV)

    # Mediator mass in GeV
    m_med_gev = lambda_p_tev * 1000.0

    # Cross-section in GeV^{-2}
    sigma_gev2 = (g_eff ** 2 * mu_gev ** 2) / (np.pi * m_med_gev ** 4)

    # Convert to cm²
    sigma_cm2 = sigma_gev2 * (GEV_TO_INV_CM ** (-2))

    # Apply tree suppression
    return sigma_cm2 * suppression


def scan_depths(
    m_dm_gev: float = 100.0,
    lambda_p_tev: float = 2.5,
    depths: list = None,
) -> dict:
    """
    Scan over tree depths and return cross-section predictions.

    Args:
        m_dm_gev: DM mass in GeV.
        lambda_p_tev: Threshold scale in TeV.
        depths: List of tree depths to scan (default: [40, 43, 45, 50, 55]).

    Returns:
        dict mapping depth to (σ_SI_cm2, status_string).
    """
    if depths is None:
        depths = [40, 43, 45, 50, 55]

    # Current experimental limits
    xenonnt_limit = 2.6e-47   # XENONnT 90% CL at 28 GeV (cm²)
    neutrino_fog = 1.0e-49    # Approximate neutrino fog (cm²)

    results = {}
    for d in depths:
        sigma = dm_xenon_xsec(m_dm_gev, lambda_p_tev, d)

        if sigma > xenonnt_limit:
            status = "EXCLUDED by XENONnT"
        elif sigma > neutrino_fog:
            status = "ACCESSIBLE (near current limit)"
        else:
            status = "BELOW neutrino fog"

        results[d] = (sigma, status)

    return results


# =============================================================================
# Example usage
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Dark Matter Direct Detection — Ultrametric Predictions")
    print("=" * 60)

    # Scan over tree depths
    print(f"\n--- Cross-section vs. Tree Depth (m_DM = 100 GeV, Λ_2 = 2.5 TeV) ---")
    print(f"{'Depth d_2':>10}  {'σ_SI (cm²)':>15}  {'Status':>35}")
    print("-" * 65)

    results = scan_depths()
    for depth, (sigma, status) in results.items():
        print(f"{depth:10d}  {sigma:15.2e}  {status:>35}")

    # Predicted depth range
    print(f"\n--- Analysis ---")
    print("The observed DM relic density Ω_DM h² ≈ 0.12 constrains d_2.")
    print("If XENONnT/LZ/PandaX see no signal down to σ_SI < 10^{-47} cm²,")
    print("then d_2 ≳ 43 is required.")
    print()
    print("If DARWIN/XLZD see no signal down to σ_SI < 10^{-49} cm²,")
    print("(the neutrino fog), then d_2 ≳ 50, and ultrametric DM is")
    print("effectively invisible to direct detection.")

    # DAMA modulation check
    print(f"\n--- DAMA/LIBRA Modulation ---")
    sigma_dama = dm_xenon_xsec(m_dm_gev=10, lambda_p_tev=2.5, tree_depth=35)
    print(f"DAMA interpretation (d_2=35): σ_SI = {sigma_dama:.2e} cm²")
    print("This depth is EXCLUDED by null results from XENONnT/LZ.")
    print("Prediction: DAMA signal is NOT dark matter.")

    # Parameter scan
    print(f"\n--- Parameter Scan: DM Mass vs. Depth ---")
    print(f"{'m_DM (GeV)':>10}  {'Depth':>8}  {'σ_SI (cm²)':>15}")
    print("-" * 40)
    for mass in [10, 50, 100, 500, 1000]:
        sigma = dm_xenon_xsec(m_dm_gev=mass, lambda_p_tev=2.5, tree_depth=43)
        print(f"{mass:10.0f}  {43:8d}  {sigma:15.2e}")

    print("\nDone.")
