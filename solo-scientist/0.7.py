"""
0.7.py — Extended Scale Ratio Scanning
Sprint 3, Task 3.2: Live Force-Multiplier Demonstration
Specification from 0.5.2.md Day 1 Afternoon

Assembles ≥100 known physical length/energy scales from particle physics,
computes all pairwise ratios, and finds the closest approach to each
mass ratio target (mp/me, mμ/me, mτ/me, mt/me, mb/me, mc/me).

Classifies matches as tautological (Compton ratios derived from masses)
vs. non-tautological (cross-domain ratios).
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
import json
import time

# ============================================================
# PART 1: Assemble Scale Library (≥100 physical length/energy scales)
# ============================================================

# Category legend:
#   E = elementary particle Compton wavelengths
#   H = hadronic/nuclear scales
#   W = electroweak scales
#   G = gravitational/Planck scales
#   A = atomic/molecular scales
#   C = cosmological scales
#   M = mesoscopic/human scales

# All values in METERS (converted from energies via λ = hc/E)

# Planck constant * speed of light
hc_eVs = 1.239841984e-6  # eV·m
hc_GeVm = 1.239841984e-15  # GeV·m

def energy_to_length(E_eV):
    """Convert energy in eV to Compton wavelength in meters."""
    return hc_eVs / E_eV

def energy_to_length_GeV(E_GeV):
    """Convert energy in GeV to Compton wavelength in meters."""
    return hc_GeVm / E_GeV

scales = []

# --- E: Elementary Particle Compton Wavelengths ---
# Electron
scales.append(("electron Compton λ", energy_to_length(0.510998950e6), "E", "CODATA 2018"))
scales.append(("electron reduced Compton λ̄", energy_to_length(0.510998950e6) / (2*np.pi), "E", "CODATA 2018"))
# Muon
scales.append(("muon Compton λ", energy_to_length(105.6583745e6), "E", "CODATA 2018"))
scales.append(("muon reduced Compton λ̄", energy_to_length(105.6583745e6) / (2*np.pi), "E", "CODATA 2018"))
# Tau
scales.append(("tau Compton λ", energy_to_length(1776.86e6), "E", "PDG 2022"))
scales.append(("tau reduced Compton λ̄", energy_to_length(1776.86e6) / (2*np.pi), "E", "PDG 2022"))
# Quarks (current masses, MS-bar at 2 GeV unless noted)
scales.append(("up quark Compton λ (~2.2 MeV)", energy_to_length(2.2e6), "E", "PDG 2022"))
scales.append(("down quark Compton λ (~4.7 MeV)", energy_to_length(4.7e6), "E", "PDG 2022"))
scales.append(("strange quark Compton λ (~96 MeV)", energy_to_length(96e6), "E", "PDG 2022"))
scales.append(("charm quark Compton λ (~1.27 GeV)", energy_to_length_GeV(1.27), "E", "PDG 2022"))
scales.append(("bottom quark Compton λ (~4.18 GeV)", energy_to_length_GeV(4.18), "E", "PDG 2022"))
scales.append(("top quark Compton λ (~172.5 GeV)", energy_to_length_GeV(172.5), "E", "PDG 2022"))
# Gauge bosons
scales.append(("W boson Compton λ", energy_to_length_GeV(80.377), "E", "PDG 2022"))
scales.append(("Z boson Compton λ", energy_to_length_GeV(91.1876), "E", "PDG 2022"))
scales.append(("Higgs boson Compton λ", energy_to_length_GeV(125.25), "E", "PDG 2022"))
# Neutrinos (upper limits on mass from cosmology/KATRIN)
scales.append(("neutrino mass limit Compton λ (~0.8 eV)", energy_to_length(0.8), "E", "KATRIN/cosmology upper bound"))
scales.append(("neutrino mass limit Compton λ (~0.12 eV)", energy_to_length(0.12), "E", "cosmology ∑m_ν upper bound"))

# --- H: Hadronic/Nuclear Scales ---
scales.append(("proton Compton λ", energy_to_length(938.272088e6), "H", "CODATA 2018"))
scales.append(("proton reduced Compton λ̄", energy_to_length(938.272088e6) / (2*np.pi), "H", "CODATA 2018"))
scales.append(("neutron Compton λ", energy_to_length(939.565420e6), "H", "CODATA 2018"))
scales.append(("pion (π±) Compton λ", energy_to_length(139.57039e6), "H", "PDG 2022"))
scales.append(("pion (π0) Compton λ", energy_to_length(134.9768e6), "H", "PDG 2022"))
scales.append(("kaon (K±) Compton λ", energy_to_length(493.677e6), "H", "PDG 2022"))
scales.append(("kaon (K0) Compton λ", energy_to_length(497.611e6), "H", "PDG 2022"))
scales.append(("eta meson Compton λ", energy_to_length(547.862e6), "H", "PDG 2022"))
scales.append(("rho meson Compton λ", energy_to_length(775.26e6), "H", "PDG 2022"))
scales.append(("omega meson Compton λ", energy_to_length(782.66e6), "H", "PDG 2022"))
scales.append(("phi meson Compton λ", energy_to_length(1019.461e6), "H", "PDG 2022"))
scales.append(("J/psi Compton λ", energy_to_length_GeV(3.0969), "H", "PDG 2022"))
scales.append(("Upsilon(1S) Compton λ", energy_to_length_GeV(9.4603), "H", "PDG 2022"))
scales.append(("Delta++ Compton λ", energy_to_length_GeV(1.232), "H", "PDG 2022"))
# Nuclear scales
scales.append(("pion decay constant f_π (~92.2 MeV)", energy_to_length(92.2e6), "H", "f_π from PDG"))
scales.append(("nucleon radius r_p (~0.84 fm)", 0.84e-15, "H", "CODATA/electron scattering"))
scales.append(("nuclear force range (~1.4 fm)", 1.4e-15, "H", "from pion Compton λ"))
scales.append(("QCD scale 1/Λ_QCD (~4.5e-16 m)", energy_to_length_GeV(0.217) * 2*np.pi, "H", "Λ_QCD ~ 217 MeV, λ = 2πħc/Λ"))
scales.append(("QCD string tension sqrt(σ) (~440 MeV)", energy_to_length(440e6), "H", "lattice QCD"))
scales.append(("Sommer scale r_0 (~0.47 fm)", 0.47e-15, "H", "lattice QCD"))
scales.append(("Sommer scale r_1 (~0.31 fm)", 0.31e-15, "H", "lattice QCD"))
scales.append(("deuteron binding energy Compton λ", energy_to_length(2.224566e6), "H", "nuclear"))
scales.append(("alpha particle binding energy Compton λ", energy_to_length(28.295673e6), "H", "nuclear"))
scales.append(("Fermi momentum k_F (~250 MeV)", energy_to_length(250e6), "H", "nuclear matter"))
scales.append(("hadronization scale ~1 GeV", energy_to_length_GeV(1.0), "H", "QCD"))

# --- W: Electroweak Scales ---
scales.append(("Fermi scale v = 246 GeV", energy_to_length_GeV(246.22), "W", "electroweak VEV"))
scales.append(("W mass scale 1/m_W", energy_to_length_GeV(80.377) / (2*np.pi), "W", "PDG 2022"))
scales.append(("Z mass scale 1/m_Z", energy_to_length_GeV(91.1876) / (2*np.pi), "W", "PDG 2022"))
scales.append(("Higgs mass scale 1/m_H", energy_to_length_GeV(125.25) / (2*np.pi), "W", "PDG 2022"))
scales.append(("electroweak unification scale ~100 GeV", energy_to_length_GeV(100), "W", "theory"))

# --- G: Gravitational/Planck Scales ---
scales.append(("Planck length l_P", 1.616255e-35, "G", "CODATA 2018"))
scales.append(("Planck mass M_P reduced Compton λ̄", energy_to_length_GeV(2.435e18) * 2*np.pi, "G", "M_P = 2.435e18 GeV/c²"))
scales.append(("Schwarzschild radius of proton (~2.5e-54 m)", 2.5e-54, "G", "r_S = 2GM/c² for m_p"))
scales.append(("Schwarzschild radius of electron (~1.35e-57 m)", 1.35e-57, "G", "r_S = 2GM/c² for m_e"))
scales.append(("gravitational coupling ~1/α_G scale", energy_to_length_GeV(1.22e19) * (1/137.036), "G", "α_G = Gm_p²/ħc"))

# --- A: Atomic/Molecular Scales ---
scales.append(("Bohr radius a_0", 5.29177210903e-11, "A", "CODATA 2018"))
scales.append(("classical electron radius r_e", 2.8179403262e-15, "A", "CODATA 2018"))
scales.append(("Rydberg energy Compton λ", energy_to_length(13.605693e6 * 0.5), "A", "CODATA 2018"))
scales.append(("Hartree energy Compton λ", energy_to_length(27.211386e6 * 0.5), "A", "CODATA 2018"))
scales.append(("hydrogen ground state size ~1 Å", 1.0e-10, "A", "atomic"))
scales.append(("fine-structure wavelength", energy_to_length(13.605693e6 * 0.5 * (1/137.036)**2), "A", "α²·Rydberg"))
scales.append(("Lamb shift energy ~1057 MHz => λ", energy_to_length(1057e6 * 4.135667e-15), "A", "QED"))
scales.append(("hyperfine splitting 21 cm line", 0.21, "A", "hydrogen 21cm"))
scales.append(("Thomson scattering cross-section sqrt", (6.652458e-29)**0.5, "A", "classical"))
scales.append(("positronium Bohr radius", 5.29177210903e-11 * 2, "A", "2a_0 for Ps"))
scales.append(("muonic hydrogen Lamb shift scale", energy_to_length(0.05e6), "A", "proton radius puzzle"))
scales.append(("electron g-2 anomaly energy ~1.16e-3", energy_to_length(0.001159652 * 0.511e6), "A", "QED anomalous moment"))
scales.append(("Casimir force scale ~1 μm", 1.0e-6, "A", "Casimir effect"))

# --- C: Cosmological Scales ---
scales.append(("Hubble radius c/H_0 (~1.3e26 m)", 1.3e26, "C", "H_0 ≈ 70 km/s/Mpc"))
scales.append(("dark energy scale (CC) λ", energy_to_length(2.3e-3), "C", "ρ_Λ^(1/4) ~ 2.3 meV"))
scales.append(("CMB temperature energy ~2.35e-4 eV", energy_to_length(2.35e-4), "C", "T_CMB = 2.725 K"))
scales.append(("recombination energy ~0.3 eV", energy_to_length(0.3), "C", "z ~ 1100"))
scales.append(("nucleosynthesis energy ~0.1 MeV", energy_to_length(0.1e6), "C", "BBN"))
scales.append(("GUT scale ~10^16 GeV", energy_to_length_GeV(1e16), "C", "theory"))
scales.append(("inflation scale ~10^16 GeV", energy_to_length_GeV(1e16), "C", "theory, r ~ 0.05"))
scales.append(("QCD phase transition ~150 MeV", energy_to_length(150e6), "C", "crossover"))
scales.append(("electroweak phase transition ~100 GeV", energy_to_length_GeV(100), "C", "theory"))

# --- M: Mesoscopic & Other ---
scales.append(("visible light ~550 nm", 5.5e-7, "M", "reference"))
scales.append(("X-ray ~0.1 nm", 1.0e-10, "M", "reference"))
scales.append(("gamma ray ~1 pm", 1.0e-12, "M", "reference"))
scales.append(("LHC collision energy 13 TeV Compton λ", energy_to_length_GeV(13000), "M", "accelerator"))
scales.append(("cosmic ray GZK cutoff ~5e19 eV", energy_to_length(5e19), "M", "astroparticle"))
scales.append(("neutron star density scale ~1 fm interparticle", 1.0e-15, "M", "nuclear density"))
scales.append(("axion mass ~1e-5 eV Compton λ", energy_to_length(1e-5), "E", "axion DM window"))
scales.append(("sterile neutrino ~7 keV Compton λ", energy_to_length(7e3), "E", "DM candidate"))
scales.append(("WIMP mass ~100 GeV Compton λ", energy_to_length_GeV(100), "E", "DM candidate"))
scales.append(("Planck mass M_P", energy_to_length_GeV(1.220890e19), "G", "CODATA 2018"))

# --- Additional length scales from CODATA/PDG ---
# Weak mixing angle scale
scales.append(("Fermi constant G_F^(1/2) scale", energy_to_length_GeV(292.8), "W", "G_F = 1.1663787e-5 GeV^-2"))
scales.append(("confinement scale Λ_QCD ~217 MeV (Compton)", energy_to_length(217e6), "H", "lattice"))
# More nuclear
scales.append(("nuclear saturation density n_0^(-1/3) (~1.1 fm)", 1.1e-15, "H", "n_0 = 0.16 fm^-3"))
scales.append(("delta-nucleon mass splitting Compton λ", energy_to_length(293e6), "H", "N-Δ splitting"))
# Atomic/Nuclear transitions
scales.append(("thorium-229 nuclear transition ~8.4 eV λ", energy_to_length(8.4), "A", "nuclear clock"))
# Condensed matter
scales.append(("superconducting gap ~1 meV Compton λ", energy_to_length(1e-3), "A", "BCS"))
scales.append(("Fermi wavelength in metal ~0.5 nm", 0.5e-9, "A", "condensed matter"))
# Additional mesonic scales  
scales.append(("eta_prime meson Compton λ", energy_to_length(957.78e6), "H", "PDG 2022"))
scales.append(("D0 meson Compton λ", energy_to_length_GeV(1.86484), "H", "PDG 2022"))
scales.append(("D± meson Compton λ", energy_to_length_GeV(1.86966), "H", "PDG 2022"))
scales.append(("B0 meson Compton λ", energy_to_length_GeV(5.27966), "H", "PDG 2022"))
scales.append(("B± meson Compton λ", energy_to_length_GeV(5.27934), "H", "PDG 2022"))
scales.append(("Bs meson Compton λ", energy_to_length_GeV(5.36692), "H", "PDG 2022"))
# Additional atomic
scales.append(("muonic atom 2P-2S transition ~0.05 eV λ", energy_to_length(0.05), "A", "muonic hydrogen"))
scales.append(("antihydrogen 1S-2S transition λ", energy_to_length(10.2) * 243e-9 / 10.2, "A", "CERN ALPHA"))
scales.append(("Z boson width Γ_Z ~2.5 GeV λ", energy_to_length_GeV(2.5), "E", "PDG 2022"))
scales.append(("W boson width Γ_W ~2.1 GeV λ", energy_to_length_GeV(2.1), "E", "PDG 2022"))
scales.append(("Higgs width Γ_H ~4.1 MeV λ", energy_to_length(4.1e6), "E", "SM prediction"))

# ============================================================
# Summary statistics
# ============================================================
n_scales = len(scales)
print(f"Scale library assembled: {n_scales} scales")
print(f"Categories: E={sum(1 for s in scales if s[2]=='E')}, "
      f"H={sum(1 for s in scales if s[2]=='H')}, "
      f"W={sum(1 for s in scales if s[2]=='W')}, "
      f"G={sum(1 for s in scales if s[2]=='G')}, "
      f"A={sum(1 for s in scales if s[2]=='A')}, "
      f"C={sum(1 for s in scales if s[2]=='C')}, "
      f"M={sum(1 for s in scales if s[2]=='M')}")

# Save scale library
scale_data = [{"name": s[0], "value_m": s[1], "category": s[2], "source": s[3]} for s in scales]
with open("outputs/scales.json", "w", encoding="utf-8") as f:
    json.dump({"n_scales": n_scales, "scales": scale_data}, f, indent=2)
print("Saved to outputs/scales.json")

# ============================================================
# PART 2: Compute All Pairwise Ratios
# ============================================================
print(f"\n{'='*60}")
print("PART 2: Pairwise Ratio Computation")
print(f"{'='*60}")

values = np.array([s[1] for s in scales])
names = [s[0] for s in scales]
categories = [s[2] for s in scales]

t_start = time.time()

# Compute all n²/2 pairwise ratios (upper triangle)
n = n_scales
ratios = []
for i in range(n):
    for j in range(i+1, n):
        # Always store the ratio > 1 (larger/smaller)
        if values[i] >= values[j]:
            r = values[i] / values[j]
            ri, rj = i, j
        else:
            r = values[j] / values[i]
            ri, rj = j, i
        ratios.append({
            "ratio": float(r),
            "log10_ratio": float(np.log10(r)),
            "numerator": names[ri],
            "denominator": names[rj],
            "cat_num": categories[ri],
            "cat_den": categories[rj],
            "idx_num": ri,
            "idx_den": rj
        })

n_ratios = len(ratios)
t_elapsed = time.time() - t_start
print(f"Computed {n_ratios:,} pairwise ratios in {t_elapsed:.2f}s")

# ============================================================
# PART 3: Compare Against Mass Ratio Targets
# ============================================================
print(f"\n{'='*60}")
print("PART 3: Target Mass Ratio Scan")
print(f"{'='*60}")

# Target mass ratios (from 0.5.2.md targets.json)
targets = {
    "m_p/m_e": 1836.15267343,
    "m_μ/m_e": 206.7682830,
    "m_τ/m_e": 3477.23,
    "m_t/m_e": 345000.0,  # approximate (top pole mass / electron)
    "m_b/m_e": 8270.0,     # approximate
    "m_c/m_e": 2060.0      # approximate
}

# Also add the yukawa/weak targets from Monte Carlo
yukawa_targets = {
    "y_e (2.94e-6)": 2.94e-6,
    "y_μ (6.07e-4)": 6.07e-4,
    "y_τ (0.01021)": 0.01021,
    "m_W/m_Z (0.8814)": 0.8814
}

all_targets = {**targets, **yukawa_targets}

print(f"\n{'Target':<25} {'Value':>15} {'Closest Ratio':>15} {'Rel Error':>12} {'Match Type':<25}")
print("-" * 100)

results_table = []

for tname, tval in all_targets.items():
    best = None
    best_error = float('inf')
    
    for r in ratios:
        error = abs(r["ratio"] - tval) / tval
        if error < best_error:
            best_error = error
            best = r
    
    # Classify match
    num_name = best["numerator"]
    den_name = best["denominator"]
    
    # Check if tautological: does the match explicitly involve the same particles?
    is_tautological = False
    tautology_reason = ""
    
    # Mass ratio matches: check if Compton wavelengths of same particles
    if "m_p/m_e" in tname or "mp/me" in tname.lower():
        if ("proton" in num_name.lower() and "electron" in den_name.lower()) or \
           ("electron" in num_name.lower() and "proton" in den_name.lower()):
            is_tautological = True
            tautology_reason = "proton/electron Compton ratio = mass ratio (tautological)"
    
    if "m_μ/m_e" in tname:
        if ("muon" in num_name.lower() and "electron" in den_name.lower()) or \
           ("electron" in num_name.lower() and "muon" in den_name.lower()):
            is_tautological = True
            tautology_reason = "muon/electron Compton ratio = mass ratio (tautological)"
    
    if "m_τ/m_e" in tname:
        if ("tau" in num_name.lower() and "electron" in den_name.lower()) or \
           ("electron" in num_name.lower() and "tau" in den_name.lower()):
            is_tautological = True
            tautology_reason = "tau/electron Compton ratio = mass ratio (tautological)"
    
    if "m_t/m_e" in tname:
        if ("top" in num_name.lower() and "electron" in den_name.lower()) or \
           ("electron" in num_name.lower() and "top" in den_name.lower()):
            is_tautological = True
            tautology_reason = "top/electron Compton ratio = mass ratio (tautological)"
    
    if "m_b/m_e" in tname:
        if ("bottom" in num_name.lower() and "electron" in den_name.lower()) or \
           ("electron" in num_name.lower() and "bottom" in den_name.lower()):
            is_tautological = True
            tautology_reason = "bottom/electron Compton ratio = mass ratio (tautological)"
    
    if "m_c/m_e" in tname:
        if ("charm" in num_name.lower() and "electron" in den_name.lower()) or \
           ("electron" in num_name.lower() and "charm" in den_name.lower()):
            is_tautological = True
            tautology_reason = "charm/electron Compton ratio = mass ratio (tautological)"
    
    # Yukawa targets
    if "y_e" in tname:
        if ("electron" in num_name.lower() and "higgs" in den_name.lower()) or \
           ("electron" in num_name.lower() and "fermi" in den_name.lower()) or \
           ("electron" in num_name.lower() and "electroweak" in den_name.lower()):
            is_tautological = True
            tautology_reason = "y_e ∝ m_e/v = Compton ratio (tautological by definition)"
    
    if "y_μ" in tname:
        if ("muon" in num_name.lower() and "higgs" in den_name.lower()) or \
           ("muon" in num_name.lower() and "fermi" in den_name.lower()):
            is_tautological = True
            tautology_reason = "y_μ ∝ m_μ/v = Compton ratio (tautological by definition)"
    
    if "y_τ" in tname:
        if ("tau" in num_name.lower() and "higgs" in den_name.lower()) or \
           ("tau" in num_name.lower() and "fermi" in den_name.lower()):
            is_tautological = True
            tautology_reason = "y_τ ∝ m_τ/v = Compton ratio (tautological by definition)"
    
    if "m_W/m_Z" in tname:
        if ("w" in num_name.lower() and "z" in den_name.lower()) or \
           ("z" in num_name.lower() and "w" in den_name.lower()):
            is_tautological = True
            tautology_reason = "W/Z mass ratio (tautological by definition)"
    
    match_type = "TAUTOLOGICAL" if is_tautological else "NON-TAUTOLOGICAL"
    if is_tautological:
        match_type += f" ({tautology_reason})"
    
    match_str = f"{best['numerator'][:40]} / {best['denominator'][:40]}"
    print(f"{tname:<25} {tval:>15.6g} {best['ratio']:>15.6g} {best_error:>11.4%} {match_type:<50}")
    
    results_table.append({
        "target": tname,
        "target_value": tval,
        "closest_ratio": best["ratio"],
        "relative_error": float(best_error),
        "numerator": best["numerator"],
        "denominator": best["denominator"],
        "num_category": best["cat_num"],
        "den_category": best["cat_den"],
        "match_type": "tautological" if is_tautological else "non-tautological",
        "tautology_reason": tautology_reason
    })

# ============================================================
# PART 4: Statistical Assessment
# ============================================================
print(f"\n{'='*60}")
print("PART 4: Statistical Assessment")
print(f"{'='*60}")

# Filter non-tautological matches
non_taut = [r for r in results_table if r["match_type"] == "non-tautological"]
taut = [r for r in results_table if r["match_type"] == "tautological"]

print(f"\nTautological matches: {len(taut)}")
for r in taut:
    print(f"  {r['target']}: {r['tautology_reason']}")

print(f"\nNon-tautological matches: {len(non_taut)}")
if non_taut:
    for r in non_taut:
        print(f"  {r['target']}: {r['numerator']} / {r['denominator']} (err={r['relative_error']:.4%})")
else:
    print("  NONE — all mass ratio matches are tautological")
    print("  (Compton wavelength ratios reproduce mass ratios by definition)")

# For non-tautological matches, compute empirical p-value via bootstrap
if non_taut:
    print(f"\nBootstrap p-value for non-tautological matches:")
    ratio_values = np.array([r["ratio"] for r in ratios])
    log_ratios = np.log10(ratio_values)
    
    for r in non_taut:
        tval = r["target_value"]
        tol = r["relative_error"]
        # Count how many ratios in the empirical distribution fall within the same relative error
        in_window = np.sum(np.abs(ratio_values - tval) / tval <= tol)
        p_empirical = in_window / len(ratio_values)
        print(f"  {r['target']}: {in_window} matches in {len(ratio_values):,} ratios, p = {p_empirical:.4g}")

# ============================================================
# PART 5: Full distribution statistics
# ============================================================
print(f"\n{'='*60}")
print("PART 5: Ratio Distribution Summary")
print(f"{'='*60}")

log_ratio_values = np.array([r["log10_ratio"] for r in ratios])
ratio_linear = np.array([r["ratio"] for r in ratios])

print(f"Log10 ratio range: [{log_ratio_values.min():.1f}, {log_ratio_values.max():.1f}]")
print(f"  (Linear range: [{ratio_linear.min():.3g}, {ratio_linear.max():.3g}])")
print(f"Number of ratios within 1% of each target:")
for tname, tval in all_targets.items():
    close = np.sum(np.abs(ratio_linear - tval) / tval <= 0.01)
    print(f"  {tname}: {close} ratios within 1%")

# Save full results
with open("outputs/scan_results.json", "w", encoding="utf-8") as f:
    json.dump({
        "n_scales": n_scales,
        "n_ratios": n_ratios,
        "targets": results_table,
        "tautological_count": len(taut),
        "non_tautological_count": len(non_taut),
        "log_ratio_range": [float(log_ratio_values.min()), float(log_ratio_values.max())]
    }, f, indent=2)

print(f"\nResults saved to outputs/scan_results.json")
print(f"\n{'='*60}")
print("EXTENDED SCAN COMPLETE")
print(f"{'='*60}")
