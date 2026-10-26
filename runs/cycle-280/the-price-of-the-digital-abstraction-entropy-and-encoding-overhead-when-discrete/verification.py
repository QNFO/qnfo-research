import math

def approx_equal(a, b, rel_tol=1e-9, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

# Inputs
d = 12
gamma = 1e-3
n_bar = 0.1
M1 = 1000
N1 = 10**9
M2 = 10**4
N2 = 10**10
log2e = 1 / math.log(2)  # ≈1.4426950408889634

# Claim computations
results = {}

# Q1
H_reg = math.log2(d)
results['Q1'] = H_reg

# Q2
S_base_nats = math.log(d / 2)
S_base_bits = S_base_nats * log2e
results['Q2_nats'] = S_base_nats
results['Q2_bits'] = S_base_bits

# Q3
m = math.ceil(math.log2(d))
results['Q3'] = m

# Q4
dim = 2 ** m
results['Q4'] = dim

# Q5
wasted = dim - d
results['Q5'] = wasted

# Q6
overhead = dim / d
results['Q6'] = overhead

# Q7
eta = math.log2(d) / m
results['Q7'] = eta

# Q8
idle = 1 - eta
results['Q8'] = idle

# Q9
p_X = gamma / 4
p_Y = gamma / 4
p_Z = gamma / 2
p_I = 1 - gamma
results['Q9'] = (p_X, p_Y, p_Z, p_I)

# Q10
h2 = -gamma * math.log2(gamma) - (1 - gamma) * math.log2(1 - gamma)
results['Q10'] = h2

# Q11
def entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)

H_twirl = entropy([p_I, p_X, p_Y, p_Z])
results['Q11'] = H_twirl

# Q12
delta_H = H_twirl - h2
results['Q12'] = delta_H

# Q13
ratio = H_twirl / h2
results['Q13'] = ratio

# Q14
p_disc = (n_bar / (1 + n_bar)) ** d
results['Q14'] = p_disc

# Q15
bookkeeping1 = N1 * M1 * H_reg
results['Q15'] = bookkeeping1

# Q16
bookkeeping2 = N2 * M2 * H_reg
results['Q16'] = bookkeeping2

# Expected values extracted from the paper
expected = {
    'Q1': 3.584963,
    'Q2_nats': 1.791759,
    'Q2_bits': 2.584963,
    'Q3': 4,
    'Q4': 16,
    'Q5': 4,
    'Q6': 1.333333,
    'Q7': 0.896241,
    'Q8': 0.103759,
    'Q9': (2.5e-4, 2.5e-4, 5e-4, 0.999),
    'Q10': 1.140776e-2,
    'Q11': 1.290776e-2,
    'Q12': 1.5e-3,
    'Q13': 1.131489,
    'Q14': 3.186308e-13,
    'Q15': 3.584963e12,
    'Q16': 3.584963e14,
}

# Verification and printing
def fmt(val):
    if isinstance(val, float):
        return f"{val:.12g}"
    if isinstance(val, tuple):
        return "(" + ", ".join(fmt(v) for v in val) + ")"
    return str(val)

for cid in ['Q1','Q2_nats','Q2_bits','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16']:
    comp = results[cid]
    exp = expected[cid]
    if isinstance(comp, tuple):
        match = all(approx_equal(c, e, rel_tol=1e-9) for c, e in zip(comp, exp))
    else:
        match = approx_equal(comp, exp, rel_tol=1e-9)
    print(f"CLAIM {cid}: computed={fmt(comp)} expected={fmt(exp)} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for cid in expected if (approx_equal(results[cid], expected[cid], rel_tol=1e-9) if not isinstance(results[cid], tuple) else all(approx_equal(c, e, rel_tol=1e-9) for c, e in zip(results[cid], expected[cid]))))} match, {len(expected) - sum(1 for cid in expected if (approx_equal(results[cid], expected[cid], rel_tol=1e-9) if not isinstance(results[cid], tuple) else all(approx_equal(c, e, rel_tol=1e-9) for c, e in zip(results[cid], expected[cid]))))} mismatch")
