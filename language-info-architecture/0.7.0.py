#!/usr/bin/env python3
"""
Deepening the Information Architecture: Mutual Exclusion + Scientific Register
===============================================================================
Version: 0.7.0
Paths A + B combined pipeline

Path A: Deepen Mutual Exclusion Finding
  - Add 4 new domains: tense, aspect, number, definiteness
  - Exhaustive pairwise testing: all 28 pairs of 8 domains
  - Permutation test: statistical significance of zero intersections
  - Obligatory-status co-occurrence matrix

Path B: Scientific Register Comparison
  - Generate scientific register frequency profiles (8 languages)
  - Compare H_entropy, mandatory architecture, Gricean surplus
  - Test the convergence hypothesis: do science registers converge?

Seed: 42 (data from 0.3_results.json and 0.5.0_results.json)
"""

import numpy as np
import json
import sys
import itertools
from collections import defaultdict

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

SEED = 42
np.random.seed(SEED)


# ============================================================================
# 0. LOAD EXISTING DATA
# ============================================================================

def load_data():
    print("=" * 70)
    print("PHASE 0: Loading existing data")
    print("=" * 70)
    
    with open(r"G:\My Drive\projects\Language-Info-Architecture\0.5.0_results.json", 'r', encoding='utf-8') as f:
        reframed = json.load(f)
    with open(r"G:\My Drive\projects\Language-Info-Architecture\0.3_results.json", 'r', encoding='utf-8') as f:
        original = json.load(f)
    
    per_lang = original["per_language"]
    
    print(f"  Loaded {len(per_lang)} languages")
    print(f"  Existing domains: epistemic, ontological, categorical, spatial")
    
    return per_lang, reframed


# ============================================================================
# PATH A: DEEPEN MUTUAL EXCLUSION
# ============================================================================

def define_new_domains():
    """
    Define 4 new mandatory information domains with LLM-informed estimates.
    
    Domain assignments are synthetic but based on known typological patterns:
    - Tense: obligatory in most IE, Turkic, Japonic, Koreanic, Quechuan
    - Aspect: obligatory in Slavic, Greek; grammaticalized in Mandarin, Japanese
    - Number: obligatory in IE, Afro-Asiatic, Uralic, Turkic; optional elsewhere
    - Definiteness: obligatory in IE (except Slavic, Hindi), Hebrew, Arabic;
      absent in most others
    """
    new_domains = {
        # (language, domain) = (percentage_load, is_obligatory)
        # ---- TENSE ----
        ("English", "tense"): (4.5, True),
        ("French", "tense"): (4.2, True),
        ("Spanish", "tense"): (4.0, True),
        ("German", "tense"): (4.3, True),
        ("Russian", "tense"): (4.0, True),
        ("Hindi", "tense"): (3.8, True),
        ("Mandarin", "tense"): (0.3, False),
        ("Cantonese", "tense"): (0.3, False),
        ("Turkish", "tense"): (3.5, True),
        ("Uzbek", "tense"): (3.2, True),
        ("Finnish", "tense"): (3.8, True),
        ("Hungarian", "tense"): (3.5, True),
        ("Japanese", "tense"): (2.8, True),
        ("Korean", "tense"): (3.0, True),
        ("Indonesian", "tense"): (0.5, False),
        ("Tagalog", "tense"): (0.2, False),
        ("Arabic", "tense"): (3.8, True),
        ("Hebrew", "tense"): (3.5, True),
        ("Greenlandic", "tense"): (1.5, True),
        ("Navajo", "tense"): (1.8, True),
        ("Quechua", "tense"): (3.5, True),
        ("Tibetan", "tense"): (2.8, True),
        
        # ---- ASPECT ----
        ("English", "aspect"): (2.5, True),
        ("French", "aspect"): (2.0, True),
        ("Spanish", "aspect"): (2.8, True),
        ("German", "aspect"): (1.5, False),
        ("Russian", "aspect"): (4.0, True),
        ("Hindi", "aspect"): (3.0, True),
        ("Mandarin", "aspect"): (2.5, True),
        ("Cantonese", "aspect"): (2.2, True),
        ("Turkish", "aspect"): (1.5, False),
        ("Uzbek", "aspect"): (1.3, False),
        ("Finnish", "aspect"): (1.0, False),
        ("Hungarian", "aspect"): (1.2, False),
        ("Japanese", "aspect"): (2.0, True),
        ("Korean", "aspect"): (1.8, True),
        ("Indonesian", "aspect"): (0.8, False),
        ("Tagalog", "aspect"): (3.5, True),
        ("Arabic", "aspect"): (1.0, False),
        ("Hebrew", "aspect"): (1.0, False),
        ("Greenlandic", "aspect"): (2.0, True),
        ("Navajo", "aspect"): (3.0, True),
        ("Quechua", "aspect"): (1.0, False),
        ("Tibetan", "aspect"): (1.5, True),
        
        # ---- NUMBER ----
        ("English", "number"): (3.5, True),
        ("French", "number"): (4.0, True),
        ("Spanish", "number"): (3.8, True),
        ("German", "number"): (4.2, True),
        ("Russian", "number"): (3.5, True),
        ("Hindi", "number"): (3.0, True),
        ("Mandarin", "number"): (0.2, False),
        ("Cantonese", "number"): (0.2, False),
        ("Turkish", "number"): (2.0, True),
        ("Uzbek", "number"): (1.8, True),
        ("Finnish", "number"): (2.5, True),
        ("Hungarian", "number"): (2.5, True),
        ("Japanese", "number"): (0.3, False),
        ("Korean", "number"): (0.3, False),
        ("Indonesian", "number"): (0.5, False),
        ("Tagalog", "number"): (1.0, True),
        ("Arabic", "number"): (3.5, True),
        ("Hebrew", "number"): (3.2, True),
        ("Greenlandic", "number"): (2.0, True),
        ("Navajo", "number"): (1.5, True),
        ("Quechua", "number"): (1.5, True),
        ("Tibetan", "number"): (0.5, False),
        
        # ---- DEFINITENESS ----
        ("English", "definiteness"): (5.0, True),
        ("French", "definiteness"): (4.8, True),
        ("Spanish", "definiteness"): (4.5, True),
        ("German", "definiteness"): (5.5, True),
        ("Russian", "definiteness"): (0.2, False),
        ("Hindi", "definiteness"): (0.3, False),
        ("Mandarin", "definiteness"): (0.1, False),
        ("Cantonese", "definiteness"): (0.1, False),
        ("Turkish", "definiteness"): (0.3, False),
        ("Uzbek", "definiteness"): (0.2, False),
        ("Finnish", "definiteness"): (0.3, False),
        ("Hungarian", "definiteness"): (1.5, True),
        ("Japanese", "definiteness"): (0.1, False),
        ("Korean", "definiteness"): (0.1, False),
        ("Indonesian", "definiteness"): (0.2, False),
        ("Tagalog", "definiteness"): (1.0, True),
        ("Arabic", "definiteness"): (4.0, True),
        ("Hebrew", "definiteness"): (3.5, True),
        ("Greenlandic", "definiteness"): (0.2, False),
        ("Navajo", "definiteness"): (0.2, False),
        ("Quechua", "definiteness"): (0.2, False),
        ("Tibetan", "definiteness"): (0.2, False),
    }
    
    return new_domains


def build_mandatory_matrix_8domain(reframed, new_domains, per_lang):
    """
    Build an 8-domain mandatory information matrix from existing 4 domains
    plus 4 new domains.
    """
    all_domains = ["epistemic", "ontological", "categorical", "spatial",
                   "tense", "aspect", "number", "definiteness"]
    
    names = sorted(reframed["entropy"].keys())
    
    matrix = {}  # language -> {domain: (load, obligatory)}
    
    for name in names:
        mand = reframed["mandatory_architecture"].get(name, {})
        matrix[name] = {}
        
        # Existing 4 domains
        for d in ["epistemic", "ontological", "categorical", "spatial"]:
            load = mand.get(f"{d}_load", 0.0)
            oblig = mand.get(f"{d}_oblig", False)
            matrix[name][d] = (load, oblig)
        
        # New 4 domains
        for d in ["tense", "aspect", "number", "definiteness"]:
            key = (name, d)
            if key in new_domains:
                load_pct, oblig = new_domains[key]
                matrix[name][d] = (load_pct/100.0, oblig)
            else:
                matrix[name][d] = (0.0, False)
    
    return matrix, all_domains


def pairwise_mutual_exclusion(matrix, domains, names):
    """
    Exhaustive pairwise testing: for all 28 pairs, count languages
    that have both obligatory, one obligatory, neither obligatory.
    """
    print("\n" + "=" * 70)
    print("PATH A.1: Exhaustive Pairwise Mutual Exclusion (8 domains)")
    print("=" * 70)
    
    pairs = list(itertools.combinations(range(len(domains)), 2))
    
    results = {}
    
    print(f"\n  {'Pair':<35s} {'Both':>6s} {'A-only':>7s} {'B-only':>7s} {'Neither':>8s} {'Status':<12s}")
    print(f"  {'-'*75}")
    
    for i, j in pairs:
        dA, dB = domains[i], domains[j]
        
        both = 0
        a_only = 0
        b_only = 0
        neither = 0
        
        for name in names:
            loadA, obligA = matrix[name][dA]
            loadB, obligB = matrix[name][dB]
            
            if obligA and obligB:
                both += 1
            elif obligA and not obligB:
                a_only += 1
            elif not obligA and obligB:
                b_only += 1
            else:
                neither += 1
        
        total = len(names)
        
        # Determine status
        if both == 0:
            status = "*** EMPTY ***"
        elif both <= 2:
            status = "Near-empty"
        elif both >= total * 0.5:
            status = "Co-occurring"
        else:
            status = "Partial"
        
        results[(dA, dB)] = {
            "both": both, "a_only": a_only, "b_only": b_only, "neither": neither,
            "status": status
        }
        
        marker = " !!!" if both == 0 else ""
        print(f"  {dA:15s} + {dB:15s} {both:>6d} {a_only:>7d} {b_only:>7d} {neither:>8d} {status:<12s}{marker}")
    
    return results


def permutation_test(mandatory, domains, names, n_perm=10000):
    """
    Permutation test: randomly shuffle obligatory status assignments
    and count how often we observe zero-intersections by chance.
    """
    print("\n" + "=" * 70)
    print("PATH A.2: Permutation Test for Mutual Exclusion")
    print("=" * 70)
    
    # Extract obligatory matrix
    n_lang = len(names)
    n_dom = len(domains)
    
    oblig_matrix = np.zeros((n_lang, n_dom), dtype=bool)
    for li, name in enumerate(names):
        for di, d in enumerate(domains):
            _, oblig = mandatory[name][d]
            oblig_matrix[li, di] = oblig
    
    # Count zero-intersections in real data
    pairs = list(itertools.combinations(range(n_dom), 2))
    real_zeros = 0
    for i, j in pairs:
        if np.sum(oblig_matrix[:, i] & oblig_matrix[:, j]) == 0:
            real_zeros += 1
    
    # Observed obligatory counts per domain
    oblig_counts = oblig_matrix.sum(axis=0)
    
    # Permutation: shuffle within each domain independently
    np.random.seed(SEED)
    perm_zeros = []
    
    for p in range(n_perm):
        perm_matrix = np.zeros_like(oblig_matrix)
        for di in range(n_dom):
            perm_matrix[:, di] = np.random.permutation(oblig_matrix[:, di])
        
        zeros = 0
        for i, j in pairs:
            if np.sum(perm_matrix[:, i] & perm_matrix[:, j]) == 0:
                zeros += 1
        perm_zeros.append(zeros)
    
    perm_zeros = np.array(perm_zeros)
    
    # Results
    mean_perm_zeros = np.mean(perm_zeros)
    p_value = np.mean(perm_zeros >= real_zeros)
    
    print(f"\n  Observed zero-intersections: {real_zeros} out of {len(pairs)} pairs")
    print(f"  Expected zero-intersections (null): {mean_perm_zeros:.1f}")
    print(f"  Permutation test p-value: {p_value:.4f}")
    
    if p_value < 0.05:
        print(f"  *** SIGNIFICANT: The observed mutual exclusion pattern")
        print(f"      is unlikely under random assignment (p = {p_value:.4f})")
    else:
        print(f"  Not significant: the observed pattern could arise by chance")
        print(f"  with random assignment of obligatory status (p = {p_value:.4f})")
    
    # Domain-pair specific permutation tests
    print(f"\n  Pair-Specific Permutation Tests:")
    pair_results = {}
    for i, j in pairs:
        dA, dB = domains[i], domains[j]
        real_both = np.sum(oblig_matrix[:, i] & oblig_matrix[:, j])
        
        # Only test pairs where real_both is small
        if real_both <= 2:
            perm_boths = []
            for p in range(min(n_perm, 5000)):
                permA = np.random.permutation(oblig_matrix[:, i])
                permB = np.random.permutation(oblig_matrix[:, j])
                perm_boths.append(np.sum(permA & permB))
            perm_boths = np.array(perm_boths)
            
            p_val = np.mean(perm_boths <= real_both)
            sig = "***" if p_val < 0.05 else ""
            pair_results[(dA, dB)] = {"real_both": int(real_both), 
                                       "exp_both": np.mean(perm_boths),
                                       "p_value": p_val}
            print(f"    {dA:15s} + {dB:15s}: both={real_both}, "
                  f"E[both]={np.mean(perm_boths):.1f}, p={p_val:.4f} {sig}")
    
    return {
        "real_zeros": int(real_zeros),
        "n_pairs": len(pairs),
        "mean_perm_zeros": float(mean_perm_zeros),
        "p_value": float(p_value),
        "pair_tests": pair_results,
    }


def expanded_correlation_matrix(mandatory, domains, names):
    """Compute 8x8 correlation matrix of mandatory loads."""
    print("\n" + "=" * 70)
    print("PATH A.3: Expanded Cross-Domain Correlation Matrix")
    print("=" * 70)
    
    n_dom = len(domains)
    load_matrix = np.zeros((len(names), n_dom))
    
    for li, name in enumerate(names):
        for di, d in enumerate(domains):
            load, _ = mandatory[name][d]
            load_matrix[li, di] = load
    
    corr = np.corrcoef(load_matrix.T)
    
    # Print
    print(f"\n  {'':<15s}", end="")
    for d in domains:
        print(f" {d[:8]:>8s}", end="")
    print()
    for i, dA in enumerate(domains):
        print(f"  {dA:<15s}", end="")
        for j in range(n_dom):
            r = corr[i, j]
            print(f" {r:>+7.3f} ", end="")
        print()
    
    # Count negative correlations
    neg_count = 0
    pos_count = 0
    for i in range(n_dom):
        for j in range(i+1, n_dom):
            if corr[i, j] < 0:
                neg_count += 1
            else:
                pos_count += 1
    
    print(f"\n  Negative cross-domain correlations: {neg_count}/{n_dom*(n_dom-1)//2}")
    print(f"  Positive cross-domain correlations: {pos_count}/{n_dom*(n_dom-1)//2}")
    print(f"  → {'Strong evidence for' if neg_count > pos_count else 'Mixed evidence regarding'} mutual constraints")
    
    return corr.tolist(), domains


# ============================================================================
# PATH B: SCIENTIFIC REGISTER COMPARISON
# ============================================================================

def generate_scientific_frequencies(per_lang, languages_subset):
    """
    Generate synthetic "scientific register" frequency profiles.
    
    Key differences from general register:
    - Flatter distributions (higher entropy): technical terminology introduces
      many mid-frequency terms
    - Higher epistemic load: hedging, citation markers, modal verbs
    - Lower ontological load: fewer everyday nouns with gender
    - Higher definiteness load: more definite articles for specific referents
    - More nominalizations, fewer personal pronouns
    """
    print("\n" + "=" * 70)
    print("PATH B.1: Generating Scientific Register Profiles")
    print("=" * 70)
    
    scientific = {}
    
    # Per-language register shifts (LLM-informed)
    register_shifts = {
        "English":    {"alpha_shift": -0.12, "epistemic_mult": 3.0, "ontological_mult": 0.6,
                       "definiteness_mult": 1.3, "tense_shift": -0.5},
        "German":     {"alpha_shift": -0.10, "epistemic_mult": 2.5, "ontological_mult": 0.5,
                       "definiteness_mult": 1.2, "tense_shift": -0.3},
        "French":     {"alpha_shift": -0.10, "epistemic_mult": 2.5, "ontological_mult": 0.5,
                       "definiteness_mult": 1.2, "tense_shift": -0.3},
        "Japanese":   {"alpha_shift": -0.08, "epistemic_mult": 2.0, "ontological_mult": 0.8,
                       "definiteness_mult": 1.0, "tense_shift": -0.2},
        "Mandarin":   {"alpha_shift": -0.08, "epistemic_mult": 2.5, "ontological_mult": 0.7,
                       "definiteness_mult": 1.0, "tense_shift": -0.1},
        "Russian":    {"alpha_shift": -0.10, "epistemic_mult": 2.8, "ontological_mult": 0.5,
                       "definiteness_mult": 1.0, "tense_shift": -0.4},
        "Arabic":     {"alpha_shift": -0.10, "epistemic_mult": 2.8, "ontological_mult": 0.5,
                       "definiteness_mult": 1.1, "tense_shift": -0.3},
        "Korean":     {"alpha_shift": -0.08, "epistemic_mult": 2.2, "ontological_mult": 0.8,
                       "definiteness_mult": 1.0, "tense_shift": -0.2},
    }
    
    for name in languages_subset:
        if name not in register_shifts:
            continue
        
        shifts = register_shifts[name]
        
        # Get baseline data
        base = per_lang[name]
        base_alpha = base["alpha_post_mean"]
        base_freq = np.array(base["mean_freq"])
        
        # Generate new frequency distribution
        # Lower alpha = flatter distribution
        sci_alpha = max(0.5, base_alpha + shifts["alpha_shift"])
        
        ranks = np.arange(1, len(base_freq) + 1, dtype=float)
        base_new = ranks ** (-sci_alpha)
        base_new = base_new / base_new.sum()
        noise = np.random.normal(0, 0.003, len(base_new))
        sci_freq = base_new + noise
        sci_freq = np.maximum(sci_freq, 0)
        sci_freq = sci_freq / sci_freq.sum()
        
        # Compute entropy
        H = -np.sum(sci_freq[sci_freq > 0] * np.log2(sci_freq[sci_freq > 0]))
        
        # Shifted mandatory loads
        sci_mandatory = {
            "epistemic_load": min(0.10, base.get("epistemic_load", 0.01) * shifts["epistemic_mult"]),
            "ontological_load": base.get("ontological_load", 0) * shifts["ontological_mult"],
            "categorical_load": base.get("categorical_load", 0) * shifts.get("categorical_mult", 0.9),
            "tense_load": max(0.01, base.get("tense_load", 0.03) + shifts["tense_shift"] / 100),
            "definiteness_load": min(0.08, base.get("definiteness_load", 0.02) * shifts["definiteness_mult"]),
        }
        sci_mandatory["total_load"] = sum(sci_mandatory.values())
        
        scientific[name] = {
            "alpha_sci": sci_alpha,
            "alpha_baseline": base_alpha,
            "entropy_H": H,
            "mandatory": sci_mandatory,
            "morph_type": base["morph_type"],
            "family": base["family"],
        }
        
        print(f"  {name:15s}: alpha {base_alpha:.2f}->{sci_alpha:.2f}, "
              f"H(sci)={H:.2f} bits")
    
    return scientific


def compare_registers(reframed, scientific, new_domains):
    """
    Compare baseline vs. scientific register information architecture.
    """
    print("\n" + "=" * 70)
    print("PATH B.2: Baseline vs. Scientific Register Comparison")
    print("=" * 70)
    
    languages = sorted(scientific.keys())
    
    # Extract baseline entropy
    baseline_entropy = {}
    for name in languages:
        baseline_entropy[name] = reframed["entropy"].get(name, {}).get("entropy_H", 0)
        if baseline_entropy[name] == 0:
            baseline_entropy[name] = 6.35  # fallback
    
    print(f"\n  {'Language':<15s} {'H(base)':>8s} {'H(sci)':>8s} {'Delta H':>8s} "
          f"{'Load(base)':>10s} {'Load(sci)':>10s}")
    print(f"  {'-'*65}")
    
    for name in languages:
        H_base = baseline_entropy.get(name, 0)
        H_sci = scientific[name]["entropy_H"]
        dH = H_sci - H_base
        
        # Baseline mandatory load from expanded matrix
        base_mand = reframed["mandatory_architecture"].get(name, {})
        base_load = base_mand.get("total_mandatory", 0)
        
        sci_load = scientific[name]["mandatory"]["total_load"]
        
        print(f"  {name:<15s} {H_base:8.2f} {H_sci:8.2f} {dH:>+7.2f} "
              f"{base_load*100:9.1f}% {sci_load*100:9.1f}%")
    
    # Convergence metrics
    H_bases = np.array([baseline_entropy[n] for n in languages])
    H_scis = np.array([scientific[n]["entropy_H"] for n in languages])
    
    sd_baseline = np.std(H_bases)
    sd_sci = np.std(H_scis)
    
    print(f"\n  Convergence Analysis:")
    print(f"    SD of baseline entropy: {sd_baseline:.4f}")
    print(f"    SD of scientific entropy: {sd_sci:.4f}")
    print(f"    {'→ Scientific registers ARE more converged' if sd_sci < sd_baseline else '→ No convergence detected'}")
    
    # Epistemic load convergence
    epi_bases = []
    epi_scis = []
    for name in languages:
        base_mand = reframed["mandatory_architecture"].get(name, {})
        epi_bases.append(base_mand.get("epistemic_load", 0))
        epi_scis.append(scientific[name]["mandatory"]["epistemic_load"])
    
    epi_bases = np.array(epi_bases)
    epi_scis = np.array(epi_scis)
    
    print(f"\n  Epistemic Load (hedging, citation, evidentials):")
    print(f"    Mean baseline: {np.mean(epi_bases)*100:.1f}%")
    print(f"    Mean scientific: {np.mean(epi_scis)*100:.1f}%")
    print(f"    Ratio sci/base: {np.mean(epi_scis)/max(np.mean(epi_bases), 0.001):.2f}x")
    
    return {
        "sd_baseline_H": float(sd_baseline),
        "sd_sci_H": float(sd_sci),
        "converged": sd_sci < sd_baseline,
        "epistemic_ratio": float(np.mean(epi_scis) / max(np.mean(epi_bases), 0.001)),
    }


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 70)
    print("DEEPENING THE INFORMATION ARCHITECTURE")
    print("Paths A + B: Mutual Exclusion + Scientific Register")
    print("=" * 70)
    
    # Load
    per_lang, reframed = load_data()
    
    # ---- PATH A ----
    print("\n" + "#" * 70)
    print("# PATH A: DEEPEN MUTUAL EXCLUSION")
    print("#" * 70)
    
    new_domains = define_new_domains()
    mandatory, all_domains = build_mandatory_matrix_8domain(reframed, new_domains, per_lang)
    names = sorted(reframed["entropy"].keys())
    
    # A.1: Pairwise exclusion
    pairwise = pairwise_mutual_exclusion(mandatory, all_domains, names)
    
    # A.2: Permutation test
    perm_results = permutation_test(mandatory, all_domains, names, n_perm=10000)
    
    # A.3: Expanded correlation matrix
    corr_matrix, corr_domains = expanded_correlation_matrix(mandatory, all_domains, names)
    
    # ---- PATH B ----
    print("\n" + "#" * 70)
    print("# PATH B: SCIENTIFIC REGISTER COMPARISON")
    print("#" * 70)
    
    sci_languages = ["English", "German", "French", "Japanese", "Mandarin", 
                     "Russian", "Arabic", "Korean"]
    
    scientific = generate_scientific_frequencies(per_lang, sci_languages)
    compare = compare_registers(reframed, scientific, new_domains)
    
    # ---- COUNT ZERO INTERSECTIONS ----
    zero_pairs = [(dA, dB) for (dA, dB), r in pairwise.items() if r["both"] == 0]
    
    print("\n" + "=" * 70)
    print("SYNTHESIS: Path A + B Key Findings")
    print("=" * 70)
    
    print(f"\n  PATH A — Mutual Exclusion:")
    print(f"    Zero-intersection pairs found: {len(zero_pairs)}")
    for dA, dB in zero_pairs:
        print(f"      → {dA} ∩ {dB} = EMPTY")
    print(f"    Permutation test p-value: {perm_results['p_value']:.4f}")
    print(f"    Negative cross-domain correlations: counted in A.3")
    
    print(f"\n  PATH B — Scientific Register:")
    print(f"    Baseline entropy SD: {compare['sd_baseline_H']:.4f}")
    print(f"    Scientific entropy SD: {compare['sd_sci_H']:.4f}")
    print(f"    Convergence: {'YES' if compare['converged'] else 'NO'}")
    print(f"    Epistemic load ratio (sci/base): {compare['epistemic_ratio']:.2f}x")
    
    # Save results
    output = {
        "version": "0.7.0",
        "paths": ["A: Mutual Exclusion Deepening", "B: Scientific Register Comparison"],
        "path_a": {
            "domains": all_domains,
            "zero_intersection_pairs": [list(p) for p in zero_pairs],
            "n_zero_pairs": len(zero_pairs),
            "n_pairs_total": len(pairwise),
            "pairwise": {f"{dA}+{dB}": v for (dA, dB), v in pairwise.items()},
            "permutation_test": {k: v for k, v in perm_results.items() if k != "pair_tests"},
            "correlation_matrix": corr_matrix,
        },
        "path_b": {
            "languages": sci_languages,
            "entropy_convergence": compare,
            "scientific_entropies": {n: s["entropy_H"] for n, s in scientific.items()},
            "baseline_entropies": {n: reframed["entropy"].get(n, {}).get("entropy_H", 0) 
                                   for n in sci_languages},
        },
    }
    
    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            if isinstance(obj, (np.integer,)):
                return int(obj)
            if isinstance(obj, (np.floating,)):
                return float(obj)
            if isinstance(obj, np.bool_):
                return bool(obj)
            return super().default(obj)
    
    with open(r"G:\My Drive\projects\Language-Info-Architecture\0.7.0_results.json", "w", encoding="utf-8") as f:
        json.dump(output, f, cls=NumpyEncoder, indent=2)
    print(f"\n  Results saved to 0.7.0_results.json")
    
    print("\n" + "=" * 70)
    print("PATHS A + B COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
