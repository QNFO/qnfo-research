"""
0.6.py — Monte Carlo p-value assessment for near-matches
Sprint 3, Task 3.1: Live Force-Multiplier Demonstration
Specification from 0.5.2.md Day 1 Morning

Null hypothesis: ratios are uniformly distributed in log space
over the range ln(1e-6) to ln(1e22) ~ [-13.8, 50.7].

For each of 1M trials:
  - Generate 600 random log-uniform ratios
  - For each of 4 targets (ye, ymu, ytau, mW/mZ),
    count how many ratios fall within the target's relative tolerance
  - Sum counts across targets

p-value = fraction of trials where total matches >= 5 (the observed number)

Outputs:
  - p-value, mean matches, standard deviation
  - Histogram of match counts
  - Cumulative distribution
"""

import sys
import io
# Force UTF-8 to avoid cp1252 UnicodeEncodeError on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
import json
import time
import os
from scipy import stats

# ============================================================
# Parameters (from 0.5.2.md specification)
# ============================================================

# Targets: yukawa couplings and weak mixing ratio
targets = np.array([2.94e-6, 6.07e-4, 0.01021, 0.8814])
target_names = ["y_e", "y_μ", "y_τ", "m_W/m_Z"]

# Relative tolerances for each target
tolerances = np.array([0.0093, 0.0082, 0.0089, 0.0089])

# Number of random ratios per trial
n_ratios = 600

# Number of targets
n_targets = 4

# Log range bounds
log_min = np.log(1e-6)   # ≈ -13.816
log_max = np.log(1e22)   # ≈ 50.657

# Number of Monte Carlo trials
n_trials = 1_000_000

# Observed number of near-matches (from the physics case study)
observed_matches = 5

# Random seed for reproducibility
SEED = 42

print("=" * 60)
print("MONTE CARLO p-VALUE ASSESSMENT — NEAR-MATCHES")
print("=" * 60)
print(f"\nParameters:")
print(f"  Targets: {dict(zip(target_names, targets))}")
print(f"  Tolerances: {dict(zip(target_names, tolerances))}")
print(f"  n_ratios per trial: {n_ratios}")
print(f"  Log range: [{log_min:.3f}, {log_max:.3f}]")
print(f"  n_trials: {n_trials:,}")
print(f"  Observed matches: {observed_matches}")
print(f"  Seed: {SEED}")
print()

# ============================================================
# Monte Carlo Simulation
# ============================================================

np.random.seed(SEED)

# Pre-compute tolerance bounds for each target: [t*(1-tol), t*(1+tol)]
lower_bounds = targets * (1 - tolerances)
upper_bounds = targets * (1 + tolerances)

print("Target tolerance windows:")
for name, t, lb, ub, tol in zip(target_names, targets, lower_bounds, upper_bounds, tolerances):
    print(f"  {name}: [{lb:.6g}, {ub:.6g}] (±{tol*100:.2f}%)")

print(f"\nRunning {n_trials:,} trials...")
t_start = time.time()

# Store match counts for each trial
match_counts = np.zeros(n_trials, dtype=np.int32)

# Process in batches to avoid memory issues
batch_size = 10_000
n_batches = n_trials // batch_size

for batch in range(n_batches):
    if batch % 10 == 0:
        elapsed = time.time() - t_start
        progress = (batch * batch_size) / n_trials
        print(f"  Batch {batch}/{n_batches} ({progress*100:.0f}%) — elapsed: {elapsed:.1f}s")
    
    # Generate batch_size × n_ratios random values in log space
    log_random = np.random.uniform(log_min, log_max, size=(batch_size, n_ratios))
    linear_random = np.exp(log_random)
    
    # For each target, count matches per trial
    batch_counts = np.zeros(batch_size, dtype=np.int32)
    for i in range(n_targets):
        matches = (linear_random >= lower_bounds[i]) & (linear_random <= upper_bounds[i])
        batch_counts += matches.sum(axis=1)
    
    match_counts[batch * batch_size:(batch + 1) * batch_size] = batch_counts

t_elapsed = time.time() - t_start
print(f"\nCompleted in {t_elapsed:.1f}s ({t_elapsed/60:.1f} min)")

# ============================================================
# Statistical Analysis
# ============================================================

# p-value: fraction of trials with matches >= observed
n_extreme = np.sum(match_counts >= observed_matches)
p_value = n_extreme / n_trials

mean_matches = np.mean(match_counts)
std_matches = np.std(match_counts)
median_matches = np.median(match_counts)
max_matches = np.max(match_counts)
min_matches = np.min(match_counts)

# Expected matches per target under null
expected_per_target = n_ratios * (2 * tolerances)  # probability of falling in tolerance window
expected_total = np.sum(expected_per_target)

print(f"\n{'='*60}")
print("RESULTS")
print(f"{'='*60}")
print(f"\nMatch count distribution:")
print(f"  Mean:   {mean_matches:.3f}")
print(f"  Median: {median_matches:.0f}")
print(f"  Std:    {std_matches:.3f}")
print(f"  Min:    {min_matches}")
print(f"  Max:    {max_matches}")
print(f"\nExpected matches per target (naive uniform):")
for name, exp in zip(target_names, expected_per_target):
    print(f"  {name}: {exp:.4f}")
print(f"  Total expected: {expected_total:.4f}")
print(f"\np-value (P(matches ≥ {observed_matches})): {p_value:.6g}")
print(f"  Trials with ≥{observed_matches} matches: {n_extreme:,} / {n_trials:,}")

# Statistical significance
if p_value < 0.001:
    significance = "p < 0.001 (highly significant)"
elif p_value < 0.01:
    significance = "p < 0.01 (significant)"
elif p_value < 0.05:
    significance = "p < 0.05 (marginally significant)"
else:
    significance = "NOT significant (p ≥ 0.05)"

print(f"  Interpretation: {significance}")

# Poisson approximation check
# Under null, expected matches per trial ≈ expected_total
from scipy.stats import poisson
poisson_p = 1 - poisson.cdf(observed_matches - 1, expected_total)
print(f"\nPoisson approximation p-value: {poisson_p:.6g}")
print(f"  (Expected λ = {expected_total:.4f})")

# ============================================================
# Save results
# ============================================================

results = {
    "parameters": {
        "targets": {name: float(val) for name, val in zip(target_names, targets)},
        "tolerances": {name: float(val) for name, val in zip(target_names, tolerances)},
        "n_ratios": n_ratios,
        "log_range": [float(log_min), float(log_max)],
        "linear_range": [1e-6, 1e22],
        "n_trials": n_trials,
        "observed_matches": observed_matches,
        "seed": SEED
    },
    "results": {
        "p_value": float(p_value),
        "p_value_poisson_approx": float(poisson_p),
        "n_extreme_trials": int(n_extreme),
        "mean_matches": float(mean_matches),
        "median_matches": float(median_matches),
        "std_matches": float(std_matches),
        "min_matches": int(min_matches),
        "max_matches": int(max_matches),
        "expected_matches_per_target": [float(e) for e in expected_per_target],
        "expected_total": float(expected_total),
        "significance": significance,
        "computation_time_seconds": float(t_elapsed)
    }
}

# Create outputs directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

with open("outputs/mc_results.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to outputs/mc_results.json")

# ============================================================
# Generate plots
# ============================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histogram of match counts
ax1 = axes[0]
bins = np.arange(min_matches - 0.5, max_matches + 1.5, 1)
ax1.hist(match_counts, bins=bins, density=True, alpha=0.7, color='steelblue', edgecolor='white')
ax1.axvline(observed_matches, color='red', linestyle='--', linewidth=2, 
            label=f'Observed: {observed_matches}')
ax1.axvline(mean_matches, color='orange', linestyle='-', linewidth=1.5,
            label=f'Mean: {mean_matches:.2f}')
ax1.set_xlabel('Number of matches per trial')
ax1.set_ylabel('Probability density')
ax1.set_title(f'Distribution of Match Counts\n({n_trials:,} trials, {n_ratios} ratios/trial)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Cumulative distribution (survival function)
ax2 = axes[1]
sorted_counts = np.sort(match_counts)
cumulative = np.arange(1, n_trials + 1) / n_trials
# P(matches >= k) = 1 - CDF(k-1)
survival = 1.0 - np.searchsorted(sorted_counts, np.arange(0, max_matches + 2), side='right') / n_trials
k_values = np.arange(0, max_matches + 2)

ax2.step(k_values, survival, where='post', color='steelblue', linewidth=2)
ax2.axvline(observed_matches, color='red', linestyle='--', linewidth=2,
            label=f'Observed: {observed_matches}')
ax2.axhline(0.05, color='gray', linestyle=':', linewidth=1, label='α = 0.05')
ax2.set_xlabel('Match count threshold k')
ax2.set_ylabel('P(matches ≥ k)')
ax2.set_title(f'Survival Function\np-value = {p_value:.6g} ({significance})')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.set_yscale('log')
ax2.set_ylim(1e-6, 1.1)

plt.tight_layout()
plt.savefig('outputs/mc_histogram.png', dpi=150, bbox_inches='tight')
print("Histogram saved to outputs/mc_histogram.png")
plt.close()

print(f"\n{'='*60}")
print("MONTE CARLO COMPLETE")
print(f"{'='*60}")
