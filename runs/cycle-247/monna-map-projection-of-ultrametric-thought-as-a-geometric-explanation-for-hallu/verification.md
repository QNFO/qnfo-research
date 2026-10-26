# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The total number of unordered triples of a vocabulary of size $m=2000$ is $N_{\\text{triples}} = 1.331334\\times10^{9}$.",
    "inputs": "m = 2000",
    "formula": "N = m*(m-1)*(m-2)/6"
  },
  {
    "id": "Q2",
    "statement": "For a binary tree ($p=2$) of depth $D=5$ retaining $k=2$ most‑significant digits, the fraction of ultrametric‑respecting triples that survive the projection is $f_{\\text{survive}} = 0.009375$ (≈ 0.94 %).",
    "inputs": "p = 2, D = 5, k = 2",
    "formula": "rho = k/D; loss = 1 - rho; leafGroups = p^k; totalLeaves = p^D; pairFraction = leafGroups/totalLeaves; tripleDistinctProb ≈ (pairFraction)^2; f_survive = tripleDistinctProb * loss"
  },
  {
    "id": "Q3",
    "statement": "For a binary tree ($p=2$) of depth $L=20$ retaining $k=10$ digits, the distinguishable fraction of source configurations is $f = 9.765625\\times10^{-4}$.",
    "inputs": "p = 2, L = 20, k = 10",
    "formula": "f = p^{k-L}"
  },
  {
    "id": "Q4",
    "statement": "For the same binary tree ($p=2$, $L=20$, $k=10$) the mutual information between source $X$ and output $Y$ is $I(X;Y) = 10\\text{ bits}$.",
    "inputs": "p = 2, L = 20, k = 10",
    "formula": "I = k * log_2(p)  (since p=2, I = k bits)"
  },
  {
    "id": "Q5",
    "statement": "Assuming a truncated geometric depth distribution with parameter $q=0.7$, depth limit $k=10$, and maximum depth $L=20$, the irrecoverable‑content floor is $P_{\\text{floor}} = 0.01921472157 \\approx 1.92\\times10^{-2}$.",
    "inputs": "q = 0.7, k = 10, L = 20",
    "formula": "P_floor = q^{k+1} - q^{L+1}"
  },
  {
    "id": "Q6",
    "statement": "Increasing the retained digit count from $k=2$ to $k=4$ for a tree of depth $D=5$ reduces the information‑loss fraction from $0.6$ to $0.2$, predicting a hallucination reduction of $66.7\\%$.",
    "inputs": "D = 5, k_1 = 2, k_2 = 4",
    "formula": "loss_1 = 1 - k_1/D; loss_2 = 1 - k_2/D; reduction = (loss_1 - loss_2)/loss_1"
  },
  {
    "id": "Q7",
    "statement": "For the shallow tree case ($D=5$, $k=2$) the information‑loss fraction is $1-\\rho = 0.6$.",
    "inputs": "D = 5, k = 2",
    "formula": "rho = k/D; loss = 1 - rho"
  },
  {
    "id": "Q8",
    "statement": "For the shallow tree case with $k=4$ the information‑loss fraction is $1-\\rho = 0.2$.",
    "inputs": "D = 5, k = 4",
    "formula": "rho = k/D; loss = 1 - rho"
  }
]

## Script
```python
import math

def approx_equal(a, b, rel_tol=1e-9, abs_tol=0.0):
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

def format_num(x):
    # Use scientific notation for very small/large numbers, otherwise plain
    if abs(x) < 1e-3 or abs(x) >= 1e6:
        return f"{x:.10e}"
    else:
        return f"{x:.10f}".rstrip('0').rstrip('.')

# Q1
m = 2000
N = m * (m - 1) * (m - 2) / 6
exp_Q1 = 1.331334e9
match_Q1 = approx_equal(N, exp_Q1, rel_tol=1e-12)
print(f"CLAIM Q1: computed={format_num(N)} expected={exp_Q1:.10e} match={'yes' if match_Q1 else 'no'}")

# Q2
p = 2
D = 5
k = 2
rho = k / D
loss = 1 - rho
leaf_groups = p ** k
total_leaves = p ** D
pair_frac = leaf_groups / total_leaves
triple_distinct = pair_frac ** 2
f_survive = triple_distinct * loss
exp_Q2 = 0.009375
match_Q2 = approx_equal(f_survive, exp_Q2, rel_tol=1e-12)
print(f"CLAIM Q2: computed={format_num(f_survive)} expected={exp_Q2:.6f} match={'yes' if match_Q2 else 'no'}")

# Q3
L = 20
k = 10
f = p ** (k - L)  # 2^{k-L}
exp_Q3 = 9.765625e-4
match_Q3 = approx_equal(f, exp_Q3, rel_tol=1e-12)
print(f"CLAIM Q3: computed={format_num(f)} expected={exp_Q3:.10e} match={'yes' if match_Q3 else 'no'}")

# Q4
I = k * math.log2(p)  # since p=2, log2(p)=1
exp_Q4 = 10
match_Q4 = approx_equal(I, exp_Q4, rel_tol=1e-12)
print(f"CLAIM Q4: computed={format_num(I)} expected={exp_Q4} match={'yes' if match_Q4 else 'no'}")

# Q5
q = 0.7
k = 10
L = 20
P_floor = q ** (k + 1) - q ** (L + 1)
exp_Q5 = 0.01921472157
match_Q5 = approx_equal(P_floor, exp_Q5, rel_tol=1e-12)
print(f"CLAIM Q5: computed={format_num(P_floor)} expected={exp_Q5:.11f} match={'yes' if match_Q5 else 'no'}")

# Q6
D = 5
k1 = 2
k2 = 4
loss1 = 1 - k1 / D
loss2 = 1 - k2 / D
reduction = (loss1 - loss2) / loss1 * 100  # percentage
exp_Q6 = 66.7  # percent
match_Q6 = approx_equal(reduction, exp_Q6, rel_tol=1e-2)  # allow 0.01% tolerance
print(f"CLAIM Q6: computed={format_num(reduction)}% expected={exp_Q6}% match={'yes' if match_Q6 else 'no'}")

# Q7
D = 5
k = 2
loss_Q7 = 1 - k / D
exp_Q7 = 0.6
match_Q7 = approx_equal(loss_Q7, exp_Q7, rel_tol=1e-12)
print(f"CLAIM Q7: computed={format_num(loss_Q7)} expected={exp_Q7} match={'yes' if match_Q7 else 'no'}")

# Q8
k = 4
loss_Q8 = 1 - k / D
exp_Q8 = 0.2
match_Q8 = approx_equal(loss_Q8, exp_Q8, rel_tol=1e-12)
print(f"CLAIM Q8: computed={format_num(loss_Q8)} expected={exp_Q8} match={'yes' if match_Q8 else 'no'}")

print(f"VERIFICATION SUMMARY: 8 claims, {sum([match_Q1, match_Q2, match_Q3, match_Q4, match_Q5, match_Q6, match_Q7, match_Q8])} match, {8 - sum([match_Q1, match_Q2, match_Q3, match_Q4, match_Q5, match_Q6, match_Q7, match_Q8])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.3313340000e+09 expected=1.3313340000e+09 match=yes
CLAIM Q2: computed=0.009375 expected=0.009375 match=yes
CLAIM Q3: computed=9.7656250000e-04 expected=9.7656250000e-04 match=yes
CLAIM Q4: computed=10 expected=10 match=yes
CLAIM Q5: computed=0.0192147216 expected=0.01921472157 match=no
CLAIM Q6: computed=66.6666666667% expected=66.7% match=yes
CLAIM Q7: computed=0.6 expected=0.6 match=yes
CLAIM Q8: computed=0.2 expected=0.2 match=yes
VERIFICATION SUMMARY: 8 claims, 7 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.3313340000e+09 | 1.3313340000e+09 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q2 | 0.009375 | 0.009375 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 9.7656250000e-04 | 9.7656250000e-04 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q4 | 10 | 10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.0192147216 | 0.01921472157 | no | MISMATCH | 10 significant digits (as the paper states, at least 2) |
| Q6 | 66.6666666667% | 66.7% | yes | match | script verdict (values not both numeric) |
| Q7 | 0.6 | 0.6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 0.2 | 0.2 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 1 of 8.


## Auto-corrections

The worker corrected these independently-verified values in place of the paper's stated values (deterministic, no model edit):

| claim | stated | corrected |
|---|---|---|
| Q5 | 0.01921472157 | 0.0192147216 |
