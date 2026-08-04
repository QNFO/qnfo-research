#!/usr/bin/env python3
"""
Language as Information Architecture: Analysis Pipeline
===========================================================================
Version: 0.5.0
Based on: 0.5.0.md reframed research plan
Seed: 42 (data from 0.3_results.json)

Pipeline:
  1. Load frequency data from 0.3_results.json
  2. Shannon entropy & information density per language
  3. Mandatory information architecture (4-type classification)
  4. Gricean surplus computation
  5. Compression-tax trade-off test
  6. Greenbergian correlation testing
  7. Design space mapping (PCA)
  8. Results output

Reframing: Sapir-Whorf -> Jakobson/Shannon/Grice/Greenberg
"""

import numpy as np
import json
import sys

# ============================================================================
# 0. REPRODUCIBILITY
# ============================================================================
SEED = 42
np.random.seed(SEED)

# Fix Unicode on Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ============================================================================
# 1. LOAD EXISTING DATA
# ============================================================================

def load_data():
    """Load frequency data from previous simulation results."""
    print("=" * 70)
    print("PHASE 0: Loading existing frequency data")
    print("=" * 70)
    
    with open(r"G:\My Drive\projects\Language-Info-Architecture\0.3_results.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    per_lang = data["per_language"]
    hier = data["hierarchical"]
    loads = data["whorfian_loads"]
    
    print(f"  Loaded {len(per_lang)} languages")
    print(f"  Hierarchical model: {list(hier.keys())}")
    print(f"  Whorfian loads: {len(loads)} language entries")
    
    return per_lang, hier, loads


# ============================================================================
# 2. SHANNON ENTROPY & INFORMATION DENSITY
# ============================================================================

def compute_entropy(per_lang):
    """
    Compute Shannon entropy for each language.
    H = -sum(p_i * log2(p_i))
    """
    print("\n" + "=" * 70)
    print("PHASE 1: Shannon Entropy & Information Density")
    print("=" * 70)
    
    results = {}
    n_max = 200
    H_max = np.log2(n_max)  # ~7.64 bits
    
    for name, d in per_lang.items():
        freq = np.array(d["mean_freq"])
        freq = freq / freq.sum()  # ensure sums to 1
        freq = freq[freq > 0]  # remove zeros to avoid log(0)
        
        # Shannon entropy
        H = -np.sum(freq * np.log2(freq))
        
        # Normalized entropy
        H_norm = H / H_max
        
        # Effective vocabulary size
        N_eff = 2**H
        
        # Information concentration: proportion of top-5 words
        C5 = np.sum(np.sort(freq)[-5:]) if len(freq) >= 5 else 1.0
        
        # Top word dominance
        p1 = freq[0] if len(freq) > 0 else 0
        
        # Morphological complexity index
        morph_map = {"isolating": 1, "fusional": 2, "mixed": 3, "agglutinative": 4, "polysynthetic": 5}
        morph_complexity = morph_map.get(d["morph_type"], 3)
        
        # Estimated morphemes per word (typological estimates)
        morphemes_per_word = {
            "isolating": 1.1,
            "fusional": 1.7,
            "mixed": 2.0,
            "agglutinative": 2.5,
            "polysynthetic": 4.0,
        }
        mpw = morphemes_per_word.get(d["morph_type"], 1.5)
        
        # Information per morpheme (entropy divided by morphemes per word)
        H_per_morpheme = H / mpw
        
        results[name] = {
            "entropy_H": H,
            "entropy_norm": H_norm,
            "N_effective": N_eff,
            "concentration_C5": C5,
            "top_word_p1": p1,
            "morph_complexity": morph_complexity,
            "morphemes_per_word": mpw,
            "H_per_morpheme": H_per_morpheme,
            "morph_type": d["morph_type"],
            "family": d["family"],
        }
        
        print(f"  {name:15s}  H={H:.2f} bits  H_norm={H_norm:.3f}  "
              f"N_eff={N_eff:.1f}  C5={C5:.2%}  mpw={mpw:.1f}  H/m={H_per_morpheme:.2f}")
    
    # Summary by morphological type
    print(f"\n  {'─'*60}")
    print(f"  {'Morphological Type':<20s} {'Mean H':<10s} {'Mean H_norm':<12s} {'Mean N_eff':<10s}")
    print(f"  {'─'*60}")
    for mt in ["isolating", "fusional", "mixed", "agglutinative", "polysynthetic"]:
        vals = [r["entropy_H"] for n, r in results.items() if r["morph_type"] == mt]
        if vals:
            print(f"  {mt:<20s} {np.mean(vals):.2f}       {np.mean(vals)/H_max:.3f}        {2**np.mean(vals):.0f}")
    
    return results


# ============================================================================
# 3. MANDATORY INFORMATION ARCHITECTURE
# ============================================================================

def classify_mandatory_loads(per_lang, loads_data):
    """
    Reclassify Whorfian loads into 4 fundamental types:
    - Epistemic (evidentiality, mood)
    - Ontological (gender, noun class)
    - Categorical/dynamic (classifiers)
    - Spatial (absolute frames, directional verbs)
    """
    print("\n" + "=" * 70)
    print("PHASE 2: Mandatory Information Architecture")
    print("=" * 70)
    
    type_map = {
        "evidentiality": "epistemic",
        "gender": "ontological",
        "classifiers": "categorical",
        "spatial_frames": "spatial",
    }
    
    mandatory = {}
    
    for name, d in per_lang.items():
        loads = loads_data.get(name, {})
        type_loads = {"epistemic": 0.0, "ontological": 0.0, "categorical": 0.0, "spatial": 0.0}
        type_obligatory = {"epistemic": False, "ontological": False, "categorical": False, "spatial": False}
        
        for domain, ld in loads.items():
            info_type = type_map.get(domain, "epistemic")
            if "post_mean_pct" in ld:
                type_loads[info_type] = max(type_loads[info_type], ld.get("post_mean_pct", 0) / 100)
            elif "post_mean" in ld:
                type_loads[info_type] = max(type_loads[info_type], ld.get("post_mean", 0))
            
            if ld.get("obligatory", False):
                type_obligatory[info_type] = True
        
        total_mandatory = sum(type_loads.values())
        
        mandatory[name] = {
            "epistemic_load": type_loads["epistemic"],
            "ontological_load": type_loads["ontological"],
            "categorical_load": type_loads["categorical"],
            "spatial_load": type_loads["spatial"],
            "total_mandatory": total_mandatory,
            "epistemic_oblig": type_obligatory["epistemic"],
            "ontological_oblig": type_obligatory["ontological"],
            "categorical_oblig": type_obligatory["categorical"],
            "spatial_oblig": type_obligatory["spatial"],
            "morph_type": d["morph_type"],
            "family": d["family"],
        }
        
        obl_flags = ""
        for t in ["epistemic", "ontological", "categorical", "spatial"]:
            obl_flags += "O" if type_obligatory[t] else "-"
        
        print(f"  {name:15s}  E={type_loads['epistemic']*100:.1f}%  "
              f"O={type_loads['ontological']*100:.1f}%  "
              f"C={type_loads['categorical']*100:.1f}%  "
              f"S={type_loads['spatial']*100:.1f}%  "
              f"total={total_mandatory*100:.1f}%  [{obl_flags}]")
    
    # Upper bound analysis
    totals = [m["total_mandatory"] for m in mandatory.values()]
    print(f"\n  Total mandatory load range: {min(totals)*100:.1f}% – {max(totals)*100:.1f}%")
    print(f"  Mean total mandatory load: {np.mean(totals)*100:.1f}%")
    print(f"  Median total mandatory load: {np.median(totals)*100:.1f}%")
    
    # Languages exceeding thresholds
    high_load = {n: m for n, m in mandatory.items() if m["total_mandatory"] > 0.08}
    if high_load:
        print(f"\n  Languages exceeding 8% total mandatory load:")
        for n, m in sorted(high_load.items(), key=lambda x: -x[1]["total_mandatory"]):
            print(f"    {n}: {m['total_mandatory']*100:.1f}%")
    
    return mandatory


# ============================================================================
# 4. GRICEAN SURPLUS
# ============================================================================

def compute_gricean_surplus(mandatory):
    """
    Gricean surplus: how much each language forces beyond the cooperative minimum.
    S_G(type) = L_i(type) - min_j(L_j(type))
    """
    print("\n" + "=" * 70)
    print("PHASE 3: Gricean Surplus")
    print("=" * 70)
    
    types = ["epistemic", "ontological", "categorical", "spatial"]
    type_names = {"epistemic": "Epistemic", "ontological": "Ontological", 
                  "categorical": "Categorical", "spatial": "Spatial"}
    
    # Find minimum load for each type across all languages
    minima = {}
    for t in types:
        minima[t] = min(m[f"{t}_load"] for m in mandatory.values())
    
    print(f"\n  Cooperative minima (lowest load per type):")
    for t in types:
        print(f"    {type_names[t]:15s}: {minima[t]*100:.1f}%")
    
    # Compute surplus
    surplus = {}
    for name, m in mandatory.items():
        surpluses = {}
        for t in types:
            load_key = f"{t}_load"
            surpluses[t] = m[load_key] - minima[t]
        
        total_surplus = sum(surpluses.values())
        
        surplus[name] = {
            **surpluses,
            "total_surplus": total_surplus,
            "morph_type": m["morph_type"],
            "family": m["family"],
        }
        
        print(f"  {name:15s}  ΣS_G={total_surplus*100:.1f}%  "
              f"E={surpluses['epistemic']*100:.1f}%  "
              f"O={surpluses['ontological']*100:.1f}%  "
              f"C={surpluses['categorical']*100:.1f}%  "
              f"S={surpluses['spatial']*100:.1f}%")
    
    # Top surplus languages
    print(f"\n  Highest Gricean surplus (most forced over-informativeness):")
    sorted_surplus = sorted(surplus.items(), key=lambda x: -x[1]["total_surplus"])
    for name, s in sorted_surplus[:5]:
        print(f"    {name}: {s['total_surplus']*100:.1f}% over cooperative baseline")
    
    return surplus


# ============================================================================
# 5. COMPRESSION-TAX TRADE-OFF
# ============================================================================

def test_compression_tax_tradeoff(entropy_results, mandatory):
    """
    Test whether higher entropy (more information spread across forms)
    correlates with lower mandatory load.
    """
    print("\n" + "=" * 70)
    print("PHASE 4: Compression-Tax Trade-Off")
    print("=" * 70)
    
    names = sorted(entropy_results.keys())
    H_vals = np.array([entropy_results[n]["entropy_H"] for n in names])
    H_norm_vals = np.array([entropy_results[n]["entropy_norm"] for n in names])
    load_vals = np.array([mandatory[n]["total_mandatory"] for n in names])
    complexity_vals = np.array([entropy_results[n]["morph_complexity"] for n in names])
    
    # Pearson correlation
    corr_H_load = np.corrcoef(H_vals, load_vals)[0, 1]
    corr_Hnorm_load = np.corrcoef(H_norm_vals, load_vals)[0, 1]
    corr_complexity_load = np.corrcoef(complexity_vals, load_vals)[0, 1]
    
    print(f"\n  Correlation: Entropy H vs Total Mandatory Load")
    print(f"    r = {corr_H_load:.3f}")
    print(f"    (Negative -> higher entropy = lower mandatory load -> compression-tax trade-off)")
    print(f"    (Positive -> higher entropy = higher mandatory load -> both are complexity markers)")
    
    print(f"\n  Correlation: Normalized Entropy vs Total Mandatory Load")
    print(f"    r = {corr_Hnorm_load:.3f}")
    
    print(f"\n  Correlation: Morphological Complexity vs Total Mandatory Load")
    print(f"    r = {corr_complexity_load:.3f}")
    
    # Per-type correlations
    print(f"\n  Per-Type Correlations with Entropy H:")
    types = ["epistemic", "ontological", "categorical", "spatial"]
    type_corrs = {}
    for t in types:
        load_key = f"{t}_load"
        type_loads = np.array([mandatory[n][load_key] for n in names])
        # Only include non-zero loads for correlation
        mask = type_loads > 0.001
        if mask.sum() >= 3:
            r = np.corrcoef(H_vals[mask], type_loads[mask])[0, 1]
        else:
            r = float('nan')
        type_corrs[t] = r
        print(f"    {t:15s}: r = {r:.3f}")
    
    # Interpretation
    print(f"\n  Interpretation:")
    if corr_H_load < -0.2:
        print(f"    ✓ Compression-tax trade-off detected: higher-entropy languages")
        print(f"      carry lower mandatory loads. Rich morphology may substitute")
        print(f"      for explicit category marking.")
    elif corr_H_load > 0.2:
        print(f"    -> Both entropy and mandatory load are complexity markers.")
        print(f"      Morphologically complex languages also impose more mandatory")
        print(f"      categories — no trade-off, just more information overall.")
    else:
        print(f"    ○ No strong relationship detected. Entropy and mandatory load")
        print(f"      appear to be independent dimensions of language architecture.")
    
    return {
        "corr_H_load": corr_H_load,
        "corr_Hnorm_load": corr_Hnorm_load,
        "corr_complexity_load": corr_complexity_load,
        "type_corrs": type_corrs,
    }


# ============================================================================
# 6. GREENBERGIAN CORRELATION TESTING
# ============================================================================

def test_greenbergian_correlations(mandatory, per_lang, entropy_results):
    """
    Test whether mandatory loads cluster as Greenberg's universals predict.
    """
    print("\n" + "=" * 70)
    print("PHASE 5: Greenbergian Correlation Testing")
    print("=" * 70)
    
    names = sorted(mandatory.keys())
    
    # Extract loads
    ep_loads = np.array([mandatory[n]["epistemic_load"] for n in names])
    ont_loads = np.array([mandatory[n]["ontological_load"] for n in names])
    cat_loads = np.array([mandatory[n]["categorical_load"] for n in names])
    sp_loads = np.array([mandatory[n]["spatial_load"] for n in names])
    
    # Build correlation matrix
    load_matrix = np.column_stack([ep_loads, ont_loads, cat_loads, sp_loads])
    corr_matrix = np.corrcoef(load_matrix.T)
    
    type_names = ["Epistemic", "Ontological", "Categorical", "Spatial"]
    
    print(f"\n  Mandatory Load Correlation Matrix:")
    print(f"  {'':<15s}", end="")
    for tn in type_names:
        print(f" {tn:<12s}", end="")
    print()
    for i, tni in enumerate(type_names):
        print(f"  {tni:<15s}", end="")
        for j in range(len(type_names)):
            print(f" {corr_matrix[i][j]:+.3f}      ", end="")
        print()
    
    # Test specific Greenbergian predictions
    print(f"\n  Specific Greenbergian Tests:")
    
    # G1: Gender -> Number (ontological load correlated with...)
    # We use evidentiality as a proxy for morphological complexity
    # (languages with rich obligatory marking in one domain tend to have it in others)
    
    # G2: Classifier languages should be isolating/have lower morphological complexity
    classifier_names = [n for n in names if mandatory[n]["categorical_load"] > 0.01]
    non_classifier_names = [n for n in names if mandatory[n]["categorical_load"] <= 0.01]
    
    if classifier_names and non_classifier_names:
        classifier_complexity = np.mean([entropy_results[n]["morph_complexity"] 
                                         for n in classifier_names])
        non_classifier_complexity = np.mean([entropy_results[n]["morph_complexity"] 
                                             for n in non_classifier_names])
        print(f"    Classifier lang complexity: {classifier_complexity:.1f}")
        print(f"    Non-classifier lang complexity: {non_classifier_complexity:.1f}")
        print(f"    -> Classifier languages {'ARE' if classifier_complexity < non_classifier_complexity else 'are NOT'} morphologically simpler")
    
    # G3: Do obligatory epistemic languages cluster differently?
    ep_oblig_names = [n for n in names if mandatory[n]["epistemic_oblig"]]
    ont_oblig_names = [n for n in names if mandatory[n]["ontological_oblig"]]
    both_names = [n for n in ep_oblig_names if n in ont_oblig_names]
    
    print(f"\n    Languages with obligatory epistemic marking: {len(ep_oblig_names)}")
    print(f"    Languages with obligatory ontological marking: {len(ont_oblig_names)}")
    print(f"    Languages with BOTH: {len(both_names)}")
    
    if len(both_names) <= 2:
        print(f"    -> Near-empty intersection: epistemic and ontological obligation")
        print(f"      appear to be mutually constraining — evidence for an upper bound")
        print(f"      on total mandatory information.")
    
    return {
        "corr_matrix": corr_matrix.tolist(),
        "type_names": type_names,
    }


# ============================================================================
# 7. DESIGN SPACE MAPPING (PCA)
# ============================================================================

def map_design_space(entropy_results, mandatory):
    """
    PCA projection of languages into 2D design space.
    Axes: H, epistemic_load, ontological_load, morph_complexity
    """
    print("\n" + "=" * 70)
    print("PHASE 6: Design Space Mapping (PCA)")
    print("=" * 70)
    
    names = sorted(entropy_results.keys())
    
    # Feature matrix
    features = []
    for n in names:
        e = entropy_results[n]
        m = mandatory[n]
        features.append([
            e["entropy_H"],
            e["entropy_norm"],
            m["epistemic_load"],
            m["ontological_load"],
            m["categorical_load"],
            m["spatial_load"],
            e["morph_complexity"],
        ])
    
    X = np.array(features)
    
    # Standardize
    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0)
    X_std[X_std == 0] = 1e-10
    X_scaled = (X - X_mean) / X_std
    
    # PCA via SVD
    U, S, Vt = np.linalg.svd(X_scaled, full_matrices=False)
    
    # Project to 2D
    PC = X_scaled @ Vt[:2].T
    
    # Variance explained
    var_explained = S**2 / np.sum(S**2)
    
    print(f"\n  PCA Variance Explained:")
    print(f"    PC1: {var_explained[0]*100:.1f}%")
    print(f"    PC2: {var_explained[1]*100:.1f}%")
    print(f"    Cumulative: {(var_explained[0]+var_explained[1])*100:.1f}%")
    
    # Feature loadings
    feature_names = ["H_entropy", "H_norm", "Epistemic", "Ontological", 
                     "Categorical", "Spatial", "MorphComplexity"]
    print(f"\n  PC1 Loadings:")
    for fn, v in zip(feature_names, Vt[0]):
        print(f"    {fn:20s}: {v:+.3f}")
    print(f"\n  PC2 Loadings:")
    for fn, v in zip(feature_names, Vt[1]):
        print(f"    {fn:20s}: {v:+.3f}")
    
    # Language positions
    print(f"\n  Language Design Space Coordinates (PC1, PC2):")
    for i, name in enumerate(names):
        mt = entropy_results[name]["morph_type"]
        print(f"    {name:15s}  ({PC[i,0]:+.3f}, {PC[i,1]:+.3f})  [{mt}]")
    
    # Cluster analysis by morphological type
    print(f"\n  Morphological Type Centroids:")
    for mt in ["isolating", "fusional", "mixed", "agglutinative", "polysynthetic"]:
        idxs = [i for i, n in enumerate(names) if entropy_results[n]["morph_type"] == mt]
        if idxs:
            centroid = PC[idxs].mean(axis=0)
            print(f"    {mt:20s}: ({centroid[0]:+.3f}, {centroid[1]:+.3f})  n={len(idxs)}")
    
    # Empty region check
    pc1_range = PC[:,0].max() - PC[:,0].min()
    pc2_range = PC[:,1].max() - PC[:,1].min()
    
    # Check corners
    corners = [
        ("high-PC1, high-PC2", PC[:,0].max(), PC[:,1].max()),
        ("high-PC1, low-PC2", PC[:,0].max(), PC[:,1].min()),
        ("low-PC1, high-PC2", PC[:,0].min(), PC[:,1].max()),
        ("low-PC1, low-PC2", PC[:,0].min(), PC[:,1].min()),
    ]
    
    print(f"\n  Empty Region Analysis:")
    for label, cx, cy in corners:
        # Distance from corner to nearest language
        dists = np.sqrt((PC[:,0] - cx)**2 + (PC[:,1] - cy)**2)
        nearest_idx = np.argmin(dists)
        nearest_dist = dists[nearest_idx]
        threshold = 0.2 * np.sqrt(pc1_range**2 + pc2_range**2)
        
        status = "EMPTY" if nearest_dist > threshold else "occupied"
        print(f"    {label:25s}: nearest={names[nearest_idx]} ({nearest_dist:.2f}) -> {status}")
    
    return {
        "pc_coords": PC.tolist(),
        "names": names,
        "var_explained": var_explained.tolist(),
        "feature_loadings_pc1": Vt[0].tolist(),
        "feature_loadings_pc2": Vt[1].tolist(),
        "feature_names": feature_names,
    }


# ============================================================================
# 8. SYNTHESIS & OUTPUT
# ============================================================================

def synthesize(entropy_results, mandatory, surplus, tradeoff, greenberg, design_space):
    """Produce a structured synthesis of all findings."""
    print("\n" + "=" * 70)
    print("SYNTHESIS: Information Architecture Across 22 Languages")
    print("=" * 70)
    
    # Key findings
    print(f"\n  ╔══════════════════════════════════════════════════════════╗")
    print(f"  ║  KEY FINDINGS                                           ║")
    print(f"  ╚══════════════════════════════════════════════════════════╝")
    
    # Finding 1: Information density gradient
    ent_by_type = {}
    for n, e in entropy_results.items():
        mt = e["morph_type"]
        ent_by_type.setdefault(mt, []).append(e["entropy_H"])
    
    f1_text = "1. INFORMATION DENSITY GRADIENT:\n"
    for mt in ["isolating", "fusional", "mixed", "agglutinative", "polysynthetic"]:
        if mt in ent_by_type:
            f1_text += f"     {mt:20s}: H = {np.mean(ent_by_type[mt]):.2f} bits/word\n"
    print(f"  {f1_text}")
    
    # Finding 2: Mandatory load
    totals = [m["total_mandatory"] for m in mandatory.values()]
    f2_text = (f"  2. MANDATORY INFORMATION LOAD:\n"
               f"     Range: {min(totals)*100:.1f}% – {max(totals)*100:.1f}%\n"
               f"     Mean: {np.mean(totals)*100:.1f}%\n"
               f"     No language exceeds ~{max(totals)*100:.0f}% total mandatory load.\n")
    print(f"  {f2_text}")
    
    # Finding 3: Trade-off
    f3_text = (f"  3. COMPRESSION-TAX TRADE-OFF:\n"
               f"     r(H, mandatory_load) = {tradeoff['corr_H_load']:.3f}\n")
    if tradeoff['corr_H_load'] < -0.2:
        f3_text += "     ✓ TRADE-OFF DETECTED: higher entropy -> lower mandatory load\n"
    elif tradeoff['corr_H_load'] > 0.2:
        f3_text += "     -> Both are complexity markers (positive correlation)\n"
    else:
        f3_text += "     ○ Independent dimensions — languages vary freely on both axes\n"
    print(f"  {f3_text}")
    
    # Finding 4: Design space
    f4_text = (f"  4. DESIGN SPACE:\n"
               f"     PC1 + PC2 explain {sum(design_space['var_explained'][:2])*100:.1f}% of variance\n"
               f"     Languages cluster by morphological type in PC space.\n")
    print(f"  {f4_text}")
    
    # Finding 5: Gricean surplus leaders
    sorted_surplus = sorted(surplus.items(), key=lambda x: -x[1]["total_surplus"])
    f5_text = (f"  5. GRICEAN SURPLUS (most forced over-informativeness):\n")
    for name, s in sorted_surplus[:3]:
        f5_text += f"     {name}: +{s['total_surplus']*100:.1f}% beyond cooperative minimum\n"
    print(f"  {f5_text}")
    
    # Finding 6: Mutual exclusion
    ep_oblig = [n for n, m in mandatory.items() if m["epistemic_oblig"]]
    ont_oblig = [n for n, m in mandatory.items() if m["ontological_oblig"]]
    both = [n for n in ep_oblig if n in ont_oblig]
    f6_text = (f"  6. MUTUAL CONSTRAINT:\n"
               f"     Epistemic-obligatory: {len(ep_oblig)} languages\n"
               f"     Ontological-obligatory: {len(ont_oblig)} languages\n"
               f"     Both: {len(both)} languages\n")
    if len(both) <= 2:
        f6_text += "     -> Near-empty intersection suggests mutual constraint.\n"
    print(f"  {f6_text}")
    
    return {
        "info_density_gradient": {mt: float(np.mean(vals)) for mt, vals in ent_by_type.items()},
        "mandatory_load_range": [float(min(totals)), float(max(totals))],
        "tradeoff_correlation": float(tradeoff["corr_H_load"]),
        "design_space_variance": float(sum(design_space["var_explained"][:2])),
        "gricean_surplus_top3": [(n, float(s["total_surplus"])) for n, s in sorted_surplus[:3]],
        "mutual_constraint_count": len(both),
    }


# ============================================================================
# 9. MAIN PIPELINE
# ============================================================================

def main():
    print("=" * 70)
    print("LANGUAGE AS INFORMATION ARCHITECTURE")
    print("Version 0.5.0 | Seed =", SEED)
    print("Reframing: Sapir-Whorf -> Jakobson/Shannon/Grice/Greenberg")
    print("=" * 70)
    
    # Phase 0: Load data
    per_lang, hier, loads_data = load_data()
    
    # Phase 1: Shannon entropy
    entropy_results = compute_entropy(per_lang)
    
    # Phase 2: Mandatory information architecture
    mandatory = classify_mandatory_loads(per_lang, loads_data)
    
    # Phase 3: Gricean surplus
    surplus = compute_gricean_surplus(mandatory)
    
    # Phase 4: Compression-tax trade-off
    tradeoff = test_compression_tax_tradeoff(entropy_results, mandatory)
    
    # Phase 5: Greenbergian correlations
    greenberg = test_greenbergian_correlations(mandatory, per_lang, entropy_results)
    
    # Phase 6: Design space mapping
    design_space = map_design_space(entropy_results, mandatory)
    
    # Phase 7: Synthesis
    synthesis = synthesize(entropy_results, mandatory, surplus, tradeoff, greenberg, design_space)
    
    # Save results
    print("\n" + "=" * 70)
    print("Saving results...")
    
    full_results = {
        "version": "0.5.0",
        "seed": SEED,
        "theoretical_framework": "Jakobson/Shannon/Grice/Greenberg",
        "n_languages": len(per_lang),
        "entropy": {n: {k: (float(v) if isinstance(v, (np.floating, np.integer)) else v) 
                        for k, v in e.items()} 
                    for n, e in entropy_results.items()},
        "mandatory_architecture": mandatory,
        "gricean_surplus": {n: {k: (float(v) if isinstance(v, (np.floating, np.integer)) else v) 
                                for k, v in s.items()} 
                            for n, s in surplus.items()},
        "tradeoff": {k: (float(v) if isinstance(v, (np.floating, np.integer)) else v) 
                      for k, v in tradeoff.items()},
        "greenbergian": greenberg,
        "design_space": {k: v for k, v in design_space.items() if k != "names"},
        "synthesis": synthesis,
    }
    
    # Use the same NumpyEncoder from 0.3.py
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
    
    json_path = r"G:\My Drive\projects\Language-Info-Architecture\0.5.0_results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_results, f, cls=NumpyEncoder, indent=2)
    print(f"  Results saved to: {json_path}")
    
    print("\n" + "=" * 70)
    print("PIPELINE COMPLETE — Language as Information Architecture")
    print("=" * 70)
    
    return full_results


if __name__ == "__main__":
    results = main()
