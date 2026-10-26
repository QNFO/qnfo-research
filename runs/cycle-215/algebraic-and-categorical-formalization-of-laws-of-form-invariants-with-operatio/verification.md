# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Any expression of symbol weight $w$ normalizes in at most $w-1$ reduction steps.",
    "inputs": "symbol weight $w$ (integer)",
    "formula": "steps_max = w - 1"
  },
  {
    "id": "Q2",
    "statement": "An expression $E$ with weight $w_0=7$ normalizes in at most $6$ steps.",
    "inputs": "initial weight $w_0 = 7$",
    "formula": "steps_max = w_0 - 1 = 7 - 1 = 6"
  },
  {
    "id": "Q3",
    "statement": "The decoder speedup factor $s$ due to pruning is $1.43$ (i.e., a $43\\%$ increase).",
    "inputs": "pruning speedup percentage $43\\%$",
    "formula": "s = 1 + 0.43"
  },
  {
    "id": "Q4",
    "statement": "The new decoder processing rate $R_1$ is $1{,}430$ tokens per second.",
    "inputs": "baseline rate $R_0 = 1000$ tokens·s$^{-1}$, speedup factor $s = 1.43$",
    "formula": "R_1 = s \\times R_0 = 1.43 \\times 1000 = 1430"
  },
  {
    "id": "Q5",
    "statement": "The increase in processing speed is $430$ tokens per second.",
    "inputs": "new rate $R_1 = 1430$, baseline $R_0 = 1000$",
    "formula": "\\Delta R = R_1 - R_0 = 1430 - 1000 = 430"
  },
  {
    "id": "Q6",
    "statement": "The average BLEU improvement on low‑resource German→English is $4.97$ points.",
    "inputs": "BLEU improvements $8.53$ and $1.40$ points",
    "formula": "\\Delta B_{avg} = (8.53 + 1.40) / 2 = 4.965 \\approx 4.97"
  },
  {
    "id": "Q7",
    "statement": "After sentence‑level weighting, $51\\%$ of the original sentences remain.",
    "inputs": "original sentences $N_{orig}=5.15$ M, reduced sentences $N_{red}=2.63$ M",
    "formula": "r_N = N_{red} / N_{orig} = 2.63 / 5.15 \\approx 0.5107 \\approx 51\\%"
  },
  {
    "id": "Q8",
    "statement": "After weighting, $28\\%$ of the original tokens remain.",
    "inputs": "original tokens $T_{orig}=93.4$ M, reduced tokens $T_{red}=26.3$ M",
    "formula": "r_T = T_{red} / T_{orig} = 26.3 / 93.4 \\approx 0.2816 \\approx 28\\%"
  },
  {
    "id": "Q9",
    "statement": "The quadratic refinement $\\tau(1)$ equals $0$.",
    "inputs": "quadratic form $\\lambda(c,c)=c^2$, signature $=1$, $c=1$",
    "formula": "\\tau(1) = (1^2 - 1) / 8 \\equiv 0 \\pmod{2}"
  },
  {
    "id": "Q10",
    "statement": "The constant $16/\\pi^{2}$ evaluates to approximately $1.6211$.",
    "inputs": "pi $\\pi = 3.14159265$",
    "formula": "16 / \\pi^{2} = 16 / (3.14159265)^2 \\approx 1.6211389 \\approx 1.6211"
  },
  {
    "id": "Q11",
    "statement": "The Catalan number $C_n$ is given by $C_n = \\frac{1}{n+1}\\binom{2n}{n}$.",
    "inputs": "integer $n \\ge 0$",
    "formula": "C_n = (1/(n+1)) * (2n choose n)"
  },
  {
    "id": "Q12",
    "statement": "For $n=0$ to $6$, the Catalan numbers are $1,1,2,5,14,42,132$ respectively.",
    "inputs": "values of $n$ from $0$ to $6$",
    "formula": "C_0=1; C_1=1; C_2=2; C_3=5; C_4=14; C_5=42; C_6=132"
  }
]

## Script
```python
import math

def round_sig(x, sig):
    """Round x to sig significant digits."""
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

results = []

# Q1: formula, no numeric expected
computed_q1 = "w - 1"
expected_q1 = "none"
match_q1 = "yes" if expected_q1 == "none" else "no"
results.append(("Q1", computed_q1, expected_q1, match_q1))

# Q2
w0 = 7
computed_q2 = w0 - 1
expected_q2 = "6"
match_q2 = "yes" if computed_q2 == int(expected_q2) else "no"
results.append(("Q2", computed_q2, expected_q2, match_q2))

# Q3
s = 1 + 0.43
computed_q3 = round(s, 2)  # two decimal places as in paper
expected_q3 = "1.43"
match_q3 = "yes" if f"{computed_q3:.2f}" == expected_q3 else "no"
results.append(("Q3", f"{computed_q3:.2f}", expected_q3, match_q3))

# Q4
R0 = 1000
R1 = s * R0
computed_q4 = int(round(R1))  # should be exactly 1430
expected_q4 = "1430"
match_q4 = "yes" if computed_q4 == int(expected_q4) else "no"
results.append(("Q4", computed_q4, expected_q4, match_q4))

# Q5
delta_R = computed_q4 - R0
computed_q5 = delta_R
expected_q5 = "430"
match_q5 = "yes" if computed_q5 == int(expected_q5) else "no"
results.append(("Q5", computed_q5, expected_q5, match_q5))

# Q6
bleu1 = 8.53
bleu2 = 1.40
avg_bleu = (bleu1 + bleu2) / 2
computed_q6 = round(avg_bleu, 2)  # round to two decimal places
expected_q6 = "4.97"
match_q6 = "yes" if f"{computed_q6:.2f}" == expected_q6 else "no"
results.append(("Q6", f"{computed_q6:.2f}", expected_q6, match_q6))

# Q7
N_orig = 5.15
N_red = 2.63
r_N = N_red / N_orig * 100  # percent
computed_q7 = int(round(r_N))  # nearest percent
expected_q7 = "51"
match_q7 = "yes" if computed_q7 == int(expected_q7) else "no"
results.append(("Q7", computed_q7, expected_q7, match_q7))

# Q8
T_orig = 93.4
T_red = 26.3
r_T = T_red / T_orig * 100
computed_q8 = int(round(r_T))
expected_q8 = "28"
match_q8 = "yes" if computed_q8 == int(expected_q8) else "no"
results.append(("Q8", computed_q8, expected_q8, match_q8))

# Q9
tau = (1**2 - 1) // 8  # integer division gives 0
computed_q9 = tau
expected_q9 = "0"
match_q9 = "yes" if computed_q9 == int(expected_q9) else "no"
results.append(("Q9", computed_q9, expected_q9, match_q9))

# Q10
pi = 3.14159265
const = 16 / (pi ** 2)
computed_q10 = round(const, 4)  # four decimal places
expected_q10 = "1.6211"
match_q10 = "yes" if f"{computed_q10:.4f}" == expected_q10 else "no"
results.append(("Q10", f"{computed_q10:.4f}", expected_q10, match_q10))

# Q11: formula, no numeric expected
computed_q11 = "C_n = (1/(n+1)) * binomial(2n, n)"
expected_q11 = "none"
match_q11 = "yes"
results.append(("Q11", computed_q11, expected_q11, match_q11))

# Q12
def catalan(n):
    return math.comb(2*n, n) // (n+1)

catalans = [catalan(i) for i in range(0, 7)]
computed_q12 = ",".join(str(c) for c in catalans)
expected_q12 = "1,1,2,5,14,42,132"
match_q12 = "yes" if computed_q12 == expected_q12 else "no"
results.append(("Q12", computed_q12, expected_q12, match_q12))

# Print results
for cid, comp, exp, mat in results:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={mat}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(1 for r in results if r[3]=='yes')} match, {sum(1 for r in results if r[3]=='no')} mismatch")

```

## Execution output
```
CLAIM Q1: computed=w - 1 expected=none match=yes
CLAIM Q2: computed=6 expected=6 match=yes
CLAIM Q3: computed=1.43 expected=1.43 match=yes
CLAIM Q4: computed=1430 expected=1430 match=yes
CLAIM Q5: computed=430 expected=430 match=yes
CLAIM Q6: computed=4.96 expected=4.97 match=no
CLAIM Q7: computed=51 expected=51 match=yes
CLAIM Q8: computed=28 expected=28 match=yes
CLAIM Q9: computed=0 expected=0 match=yes
CLAIM Q10: computed=1.6211 expected=1.6211 match=yes
CLAIM Q11: computed=C_n = (1/(n+1)) * binomial(2n, n) expected=none match=yes
CLAIM Q12: computed=1,1,2,5,14,42,132 expected=1,1,2,5,14,42,132 match=yes
VERIFICATION SUMMARY: 12 claims, 11 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q2 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 1.43 | 1.43 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 1430 | 1430 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 430 | 430 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 4.96 | 4.97 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 51 | 51 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 28 | 28 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 0 | 0 | yes | match | stated value is zero |
| Q10 | 1.6211 | 1.6211 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q12 | 1,1,2,5,14,42,132 | 1,1,2,5,14,42,132 | yes | match | script verdict (values not both numeric) |

Mismatches: 0 of 10.
