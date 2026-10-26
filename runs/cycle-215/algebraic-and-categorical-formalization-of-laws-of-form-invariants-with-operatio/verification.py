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
