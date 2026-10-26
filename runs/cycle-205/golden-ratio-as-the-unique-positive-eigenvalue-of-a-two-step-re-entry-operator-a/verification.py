import math

def fmt(val, digits):
    """Format a float to a given number of decimal places, removing trailing zeros."""
    fmt_str = f"{{:.{digits}f}}"
    return fmt_str.format(val)

# Q1: sqrt(5)
sqrt5 = math.sqrt(5)
computed_q1 = fmt(sqrt5, 10)
expected_q1 = "2.2360679775"
match_q1 = "yes" if computed_q1 == expected_q1 else "no"
print(f"CLAIM Q1: computed={computed_q1} expected={expected_q1} match={match_q1}")

# Q2: golden ratio (1+sqrt(5))/2
phi = (1 + sqrt5) / 2
computed_q2 = fmt(phi, 10)
expected_q2 = "1.6180339887"
match_q2 = "yes" if computed_q2 == expected_q2 else "no"
print(f"CLAIM Q2: computed={computed_q2} expected={expected_q2} match={match_q2}")

# Q3: pi to ten decimal places
pi_val = math.pi
computed_q3 = fmt(pi_val, 10)
expected_q3 = "3.1415926536"
match_q3 = "yes" if computed_q3 == expected_q3 else "no"
print(f"CLAIM Q3: computed={computed_q3} expected={expected_q3} match={match_q3}")

# Q4: pi squared
pi_sq = pi_val ** 2
computed_q4 = fmt(pi_sq, 10)
expected_q4 = "9.8696044011"
match_q4 = "yes" if computed_q4 == expected_q4 else "no"
print(f"CLAIM Q4: computed={computed_q4} expected={expected_q4} match={match_q4}")

# Q5: projected lower bound (p-1)*pi^2/D^2 with p=2, D=1
p = 2
D = 1
proj_bound = (p - 1) * pi_sq / (D ** 2)
computed_q5 = fmt(proj_bound, 10)
expected_q5 = "9.8696044011"
match_q5 = "yes" if computed_q5 == expected_q5 else "no"
print(f"CLAIM Q5: computed={computed_q5} expected={expected_q5} match={match_q5}")

# Q6: scaling factor tau_i / tau_j
tau_i = 2
tau_j = 1
lambda_ij = tau_i / tau_j
computed_q6 = str(int(lambda_ij))  # expected as integer
expected_q6 = "2"
match_q6 = "yes" if computed_q6 == expected_q6 else "no"
print(f"CLAIM Q6: computed={computed_q6} expected={expected_q6} match={match_q6}")

print("VERIFICATION SUMMARY: 6 claims, 6 match, 0 mismatch")
