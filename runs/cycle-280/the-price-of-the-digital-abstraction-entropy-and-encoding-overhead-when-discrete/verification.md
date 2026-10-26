# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Register entropy of digitization for a qudit of dimension 12 is $H_{\\mathrm{reg}} = \\log_2 12 = 3.584963$ bits.",
    "inputs": "d = 12",
    "formula": "H_{\\mathrm{reg}} = \\log_2 d"
  },
  {
    "id": "Q2",
    "statement": "Base truncation entropy for $d=12$ is $S_{\\mathrm{Base}} = \\ln(12/2) = \\ln 6 = 1.791759$ nats, which equals $2.584963$ bits.",
    "inputs": "d = 12, \\log_2 e = 1.442695",
    "formula": "S_{\\mathrm{Base}} = \\ln(d/2); \\text{bits} = S_{\\mathrm{Base}} \\times \\log_2 e"
  },
  {
    "id": "Q3",
    "statement": "Number of qubits required to binary‑encode a $d=12$ qudit is $m = \\lceil\\log_2 12\\rceil = 4$.",
    "inputs": "d = 12",
    "formula": "m = \\lceil\\log_2 d\\rceil"
  },
  {
    "id": "Q4",
    "statement": "Encoded Hilbert‑space dimension using $m=4$ qubits is $2^{m}=16$.",
    "inputs": "m = 4",
    "formula": "2^{m}"
  },
  {
    "id": "Q5",
    "statement": "Wasted levels after binary encoding are $2^{m} - d = 16 - 12 = 4$.",
    "inputs": "2^{m}=16, d=12",
    "formula": "2^{m} - d"
  },
  {
    "id": "Q6",
    "statement": "Dimension‑overhead ratio is $\\frac{2^{m}}{d}=\\frac{16}{12}=\\frac{4}{3}\\approx1.333333$.",
    "inputs": "2^{m}=16, d=12",
    "formula": "(2^{m})/d"
  },
  {
    "id": "Q7",
    "statement": "Encoding efficiency is $\\eta = \\frac{\\log_2 d}{m}=\\frac{3.584963}{4}=0.896241$.",
    "inputs": "d = 12, m = 4",
    "formula": "\\eta = \\frac{\\log_2 d}{m}"
  },
  {
    "id": "Q8",
    "statement": "Idle fraction of the binary encoding is $1-\\eta = 0.103759 \\approx 10.4\\%$.",
    "inputs": "\\eta = 0.896241",
    "formula": "1 - \\eta"
  },
  {
    "id": "Q9",
    "statement": "Pauli‑twirl probabilities for amplitude‑damping rate $\\gamma=10^{-3}$ are $p_X=p_Y=\\gamma/4=2.5\\times10^{-4}$, $p_Z=\\gamma/2=5\\times10^{-4}$, $p_I=1-\\gamma=0.999$.",
    "inputs": "\\gamma = 10^{-3}",
    "formula": "p_X=p_Y=\\gamma/4;\\; p_Z=\\gamma/2;\\; p_I=1-\\gamma"
  },
  {
    "id": "Q10",
    "statement": "Physical environment entropy for amplitude damping at $\\gamma=10^{-3}$ is $H_{\\mathrm{env}}^{\\mathrm{phys}} = h_2(\\gamma)=1.140776\\times10^{-2}$ bits.",
    "inputs": "\\gamma = 10^{-3}",
    "formula": "H_{\\mathrm{env}}^{\\mathrm{phys}} = -\\gamma\\log_2\\gamma-(1-\\gamma)\\log_2(1-\\gamma)"
  },
  {
    "id": "Q11",
    "statement": "Environment entropy of the Pauli‑twirled surrogate at $\\gamma=10^{-3}$ is $H_{\\mathrm{env}}^{\\mathrm{twirl}} = 1.290776\\times10^{-2}$ bits.",
    "inputs": "p_I=0.999, p_X=p_Y=2.5\\times10^{-4}, p_Z=5\\times10^{-4}",
    "formula": "H_{\\mathrm{env}}^{\\mathrm{twirl}} = -\\sum_{i} p_i \\log_2 p_i"
  },
  {
    "id": "Q12",
    "statement": "Entropy distortion caused by Pauli twirling is $\\Delta H = H_{\\mathrm{env}}^{\\mathrm{twirl}}-H_{\\mathrm{env}}^{\\mathrm{phys}} = 1.5\\times10^{-3}$ bits.",
    "inputs": "H_{\\mathrm{env}}^{\\mathrm{twirl}}=1.290776\\times10^{-2}, H_{\\mathrm{env}}^{\\mathrm{phys}}=1.140776\\times10^{-2}",
    "formula": "\\Delta H = H_{\\mathrm{env}}^{\\mathrm{twirl}} - H_{\\mathrm{env}}^{\\mathrm{phys}}"
  },
  {
    "id": "Q13",
    "statement": "Ratio of twirled to physical environment entropy is $\\frac{H_{\\mathrm{env}}^{\\mathrm{twirl}}}{H_{\\mathrm{env}}^{\\mathrm{phys}}}=1.131489$.",
    "inputs": "H_{\\mathrm{env}}^{\\mathrm{twirl}}=1.290776\\times10^{-2}, H_{\\mathrm{env}}^{\\mathrm{phys}}=1.140776\\times10^{-2}",
    "formula": "H_{\\mathrm{env}}^{\\mathrm{twirl}} / H_{\\mathrm{env}}^{\\mathrm{phys}}"
  },
  {
    "id": "Q14",
    "statement": "Discarded Hilbert‑space weight for a thermal mode with $\\bar n=0.1$ and cutoff $d=12$ is $p_{\\mathrm{disc}} = (\\frac{\\bar n}{1+\\bar n})^{d} \\approx 3.186308\\times10^{-13}$.",
    "inputs": "\\bar n = 0.1, d = 12",
    "formula": "p_{\\mathrm{disc}} = (\\frac{\\bar n}{1+\\bar n})^{d}"
  },
  {
    "id": "Q15",
    "statement": "Cumulative register bookkeeping for $M=1000$ modes over $N_{\\mathrm{cycles}}=10^{9}$ cycles is $3.584963\\times10^{12}$ bits.",
    "inputs": "M = 1000, N_{\\mathrm{cycles}} = 10^{9}, H_{\\mathrm{reg}} = 3.584963",
    "formula": "N_{\\mathrm{cycles}} \\times M \\times H_{\\mathrm{reg}}"
  },
  {
    "id": "Q16",
    "statement": "Projected cumulative bookkeeping for $M=10^{4}$ modes over $N_{\\mathrm{cycles}}=10^{10}$ cycles is $3.584963\\times10^{14}$ bits.",
    "inputs": "M = 10^{4}, N_{\\mathrm{cycles}} = 10^{10}, H_{\\mathrm{reg}} = 3.584963",
    "formula": "N_{\\mathrm{cycles}} \\times M \\times H_{\\mathrm{reg}}"
  }
]

## Script
```python
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

```

## Execution output
```
CLAIM Q1: computed=3.58496250072 expected=3.584963 match=no
CLAIM Q2_nats: computed=1.79175946923 expected=1.791759 match=no
CLAIM Q2_bits: computed=2.58496250072 expected=2.584963 match=no
CLAIM Q3: computed=4 expected=4 match=yes
CLAIM Q4: computed=16 expected=16 match=yes
CLAIM Q5: computed=4 expected=4 match=yes
CLAIM Q6: computed=1.33333333333 expected=1.333333 match=no
CLAIM Q7: computed=0.89624062518 expected=0.896241 match=no
CLAIM Q8: computed=0.10375937482 expected=0.103759 match=no
CLAIM Q9: computed=(0.00025, 0.00025, 0.0005, 0.999) expected=(0.00025, 0.00025, 0.0005, 0.999) match=yes
CLAIM Q10: computed=0.0114077577375 expected=0.01140776 match=no
CLAIM Q11: computed=0.0129077577375 expected=0.01290776 match=no
CLAIM Q12: computed=0.0015 expected=0.0015 match=yes
CLAIM Q13: computed=1.13148946835 expected=1.131489 match=no
CLAIM Q14: computed=3.1863081771e-13 expected=3.186308e-13 match=no
CLAIM Q15: computed=3.58496250072e+12 expected=3.584963e+12 match=no
CLAIM Q16: computed=3.58496250072e+14 expected=3.584963e+14 match=no
VERIFICATION SUMMARY: 17 claims, 5 match, 12 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 3.58496250072 | 3.584963 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q2_nats | 1.79175946923 | 1.791759 | no | match | 7 significant digits (as printed, at least 3) |
| Q2_bits | 2.58496250072 | 2.584963 | no | match | 7 significant digits (as printed, at least 3) |
| Q3 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 16 | 16 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 1.33333333333 | 1.333333 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q7 | 0.89624062518 | 0.896241 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q8 | 0.10375937482 | 0.103759 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q10 | 0.0114077577375 | 0.01140776 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q11 | 0.0129077577375 | 0.01290776 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q12 | 0.0015 | 0.0015 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 1.13148946835 | 1.131489 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q14 | 3.1863081771e-13 | 3.186308e-13 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q15 | 3.58496250072e+12 | 3.584963e+12 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q16 | 3.58496250072e+14 | 3.584963e+14 | no | match | 7 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
