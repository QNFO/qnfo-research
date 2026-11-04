"""
Extend Farey neighbor analysis to higher denominators.
Tests: Does kurtosis 951.5 from d <= 200 stabilize at higher d?
"""
import math

def generate_farey_neighbors(max_den):
    """Generate all Farey neighbor pairs with denominators <= max_den."""
    # Generate all reduced fractions
    fracs = []
    for den in range(1, max_den + 1):
        for num in range(0, den + 1):
            if math.gcd(num, den) == 1:
                fracs.append((num, den))
    
    fracs.sort(key=lambda f: f[0]/f[1])
    
    pairs = []
    for i in range(len(fracs) - 1):
        a, b = fracs[i]
        c, d = fracs[i+1]
        if b * c - a * d == 1:
            pairs.append((a/b, c/d))
    
    return pairs

def kurtosis(data):
    n = len(data)
    mean = sum(data) / n
    var = sum((x - mean)**2 for x in data) / n
    if var == 0: return 0
    m4 = sum((x - mean)**4 for x in data) / n
    return m4 / (var * var) - 3

# Test at increasing denominator limits
den_limits = [50, 100, 200, 500, 1000, 2000]
print('=' * 80)
print('EXTENDED FAREY NEIGHBOR ANALYSIS')
print('Testing: Does kurtosis stabilize or grow with denominator limit?')
print('=' * 80)
print()
print(f'{"Max den":>8s} | {"Pairs":>9s} | {"Mean gap":>10s} | {"Kurtosis":>10s} | {"Log-log slope":>14s}')
print('-'*8 + '-+-' + '-'*9 + '-+-' + '-'*10 + '-+-' + '-'*10 + '-+-' + '-'*14)

for max_den in den_limits:
    pairs = generate_farey_neighbors(max_den)
    distances = [abs(a - b) for a, b in pairs]
    k = kurtosis(distances)
    
    # Log-log slope
    vals = sorted([d for d in distances if d > 0])
    n = len(vals)
    if n > 3:
        log_v = [math.log10(v) for v in vals]
        log_r = [math.log10((i+1)/n) for i in range(n)]
        sx = sum(log_v); sy = sum(log_r)
        sxy = sum(log_v[i]*log_r[i] for i in range(n))
        sxx = sum(x*x for x in log_v)
        denom = n*sxx - sx*sx
        slope = (n*sxy - sx*sy)/denom if abs(denom) > 1e-15 else 0
    else:
        slope = 0
    
    mean_gap = sum(distances)/len(distances)
    print(f'{max_den:>8d} | {len(pairs):>9,} | {mean_gap:>10.6f} | {k:>10.2f} | {slope:>14.3f}')

print()
print('Key question: Does kurtosis approach a limit as d -> infinity?')
print('If kurtosis GROWS with d, the heavy-tail is a power law with infinite kurtosis.')
print('If kurtosis STABILIZES around 950, the distribution has finite 4th moment.')

# Also test: what fraction of gaps are within different distance ranges?
print()
print('--- Distance distribution at max_den=2000 ---')
pairs = generate_farey_neighbors(2000)
distances = sorted([abs(a - b) for a, b in pairs])
n = len(distances)
print(f'Total pairs: {n:,}')
for pct in [50, 90, 99, 99.9, 99.99]:
    idx = int(n * pct / 100)
    if idx < n:
        print(f'  {pct}th percentile: {distances[idx]:.6e}')

print()
print('=' * 80)
print('ANALYSIS COMPLETE')
print('=' * 80)
