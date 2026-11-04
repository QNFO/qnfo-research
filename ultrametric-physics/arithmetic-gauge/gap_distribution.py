"""
Probabilistic Gap Distribution Investigation
Tests the Projection Principle (0.31.md):
  Do Stern-Brocot tree-adjacent points (Farey neighbors)
  have heavy-tailed Euclidean distances?

If tree-adjacent pairs have power-law Euclidean distance distribution,
the apparent randomness of prime gaps follows from metric mismatch alone.
"""
from fractions import Fraction
from collections import defaultdict
import math, random

def generate_farey_neighbors(max_den=200):
    """
    Generate all Farey neighbor pairs (a/b, c/d) with bc-ad=1
    and denominators <= max_den.
    
    Farey neighbors are exactly the tree-adjacent boundary points
    of the Stern-Brocot tree.
    """
    pairs = []
    
    # Generate all reduced fractions with den <= max_den
    fracs = []
    for den in range(1, max_den + 1):
        for num in range(0, den + 1):
            if math.gcd(num, den) == 1:
                fracs.append(Fraction(num, den))
    
    fracs.sort(key=lambda f: float(f))
    
    # Adjacent fractions in the sorted list that are Farey neighbors
    # satisfy bc - ad = 1
    for i in range(len(fracs) - 1):
        a, b = fracs[i].numerator, fracs[i].denominator
        c, d = fracs[i+1].numerator, fracs[i+1].denominator
        if b * c - a * d == 1 or a * d - b * c == 1:
            pairs.append((fracs[i], fracs[i+1]))
    
    return pairs

def analyze_distribution(pairs, label="Farey neighbors"):
    """Analyze the Euclidean distance distribution."""
    distances = [abs(float(a) - float(b)) for a, b in pairs]
    distances.sort()
    
    n = len(distances)
    if n == 0:
        return
    
    print(f"=== {label} ===")
    print(f"  Pairs: {n}")
    print(f"  Min distance: {distances[0]:.6e}")
    print(f"  Max distance: {distances[-1]:.6e}")
    print(f"  Median: {distances[n//2]:.6e}")
    print(f"  Mean: {sum(distances)/n:.6e}")
    
    # Log-spaced histogram bins
    if distances[0] == 0:
        distances = [d for d in distances if d > 0]
    
    if len(distances) < 10:
        return None
    
    # Log-log analysis
    log_d = [math.log10(d) for d in distances]
    log_rank = [math.log10((i+1)/len(distances)) for i in range(len(distances))]
    
    # Linear regression on log-log (power law test)
    n_pts = len(log_d)
    sum_x = sum(log_d)
    sum_y = sum(log_rank)
    sum_xy = sum(log_d[i] * log_rank[i] for i in range(n_pts))
    sum_xx = sum(x * x for x in log_d)
    
    slope = (n_pts * sum_xy - sum_x * sum_y) / (n_pts * sum_xx - sum_x * sum_x)
    intercept = (sum_y - slope * sum_x) / n_pts
    
    print(f"  Log-log slope (power law exponent): {slope:.3f}")
    print(f"  R^2 would indicate fit quality")
    
    # Percentile breakdown
    percentiles = [10, 25, 50, 75, 90, 95, 99]
    print(f"  Percentiles:")
    for p in percentiles:
        idx = int(n * p / 100)
        if idx < n:
            print(f"    {p}%: {distances[idx]:.6e}")
    
    return {
        'distances': distances,
        'slope': slope,
        'n': n
    }

# ===== MAIN INVESTIGATION =====
print("=" * 70)
print("PROBABILISTIC GAP DISTRIBUTION INVESTIGATION")
print("Testing Projection Principle (0.31.md):")
print("  Do tree-adjacent points have heavy-tailed Euclidean distances?")
print("=" * 70)

# Test 1: Farey neighbors (tree-adjacent)
print("\n--- Test 1: Farey neighbors (Stern-Brocot tree-adjacent) ---")
pairs = generate_farey_neighbors(max_den=200)
result_farey = analyze_distribution(pairs, "Farey neighbors")

# Test 2: Random rational pairs (baseline)
print("\n--- Test 2: Random rational pairs (baseline) ---")
random.seed(42)
random_pairs = []
for _ in range(len(pairs)):
    den1 = random.randint(1, 200)
    num1 = random.randint(0, den1)
    while math.gcd(num1, den1) != 1:
        den1 = random.randint(1, 200)
        num1 = random.randint(0, den1)
    
    den2 = random.randint(1, 200)
    num2 = random.randint(0, den2)
    while math.gcd(num2, den2) != 1:
        den2 = random.randint(1, 200)
        num2 = random.randint(0, den2)
    
    f1 = Fraction(num1, den1)
    f2 = Fraction(num2, den2)
    if f1 != f2:
        random_pairs.append((f1, f2))

result_random = analyze_distribution(random_pairs, "Random pairs")

# Test 3: Scale with denominator
print("\n--- Test 3: Distance vs. denominator scale ---")
# For Farey neighbors with denominators around d, 
# the typical distance is ~ 1/d^2
# Check if this holds
by_den = defaultdict(list)
for a, b in pairs:
    avg_den = (a.denominator + b.denominator) / 2
    dist = abs(float(a) - float(b))
    # Bin by log2 of denominator
    bin_idx = int(math.log2(max(avg_den, 1)))
    by_den[bin_idx].append(dist)

print("  Bin (log2 den)  |  Count  |  Mean distance  |  Predicted ~1/d^2")
for bin_idx in sorted(by_den.keys()):
    dists = by_den[bin_idx]
    d = 2 ** bin_idx
    mean_dist = sum(dists) / len(dists)
    predicted = 1.0 / (d * d)
    print(f"  {bin_idx:3d}  (d~{d:4d})  |  {len(dists):5d}  |  {mean_dist:.6e}  |  {predicted:.6e}")

# Test 4: Compare with prime gaps
print("\n--- Test 4: Qualitative comparison with prime gaps ---")
print("  Prime gaps are known to be heavy-tailed (follow Cramer model ~ Poisson)")
print("  If Farey neighbor distances are also heavy-tailed,")
print("  the apparent randomness of prime gaps follows from")
print("  the metric mismatch between tree and Euclidean metrics.")

# Statistical test: are distances heavy-tailed?
if result_farey and result_random:
    # Check if Farey distances have higher variance than random
    var_farey = sum((d - sum(result_farey['distances'])/len(result_farey['distances']))**2 
                    for d in result_farey['distances']) / len(result_farey['distances'])
    var_random = sum((d - sum(result_random['distances'])/len(result_random['distances']))**2 
                     for d in result_random['distances']) / len(result_random['distances'])
    
    print(f"\n  Variance (Farey):  {var_farey:.6e}")
    print(f"  Variance (Random): {var_random:.6e}")
    print(f"  Ratio: {var_farey/var_random:.3f}")
    
    # Kurtosis (excess) — measures tail weight
    def kurtosis(data):
        n = len(data)
        mean = sum(data) / n
        var = sum((x - mean)**2 for x in data) / n
        std = math.sqrt(var)
        if std == 0:
            return 0
        m4 = sum((x - mean)**4 for x in data) / n
        return m4 / (var * var) - 3  # excess kurtosis
    
    k_farey = kurtosis(result_farey['distances'])
    k_random = kurtosis(result_random['distances'])
    print(f"  Excess kurtosis (Farey):  {k_farey:.3f}")
    print(f"  Excess kurtosis (Random): {k_random:.3f}")
    print(f"  (Positive = heavier tails than normal)")

print("\n" + "=" * 70)
print("INVESTIGATION COMPLETE")
print("=" * 70)
