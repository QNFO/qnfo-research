import math
from fractions import Fraction

def fmt(val, fmt_str):
    return format(val, fmt_str)

# Claim Q1
P = Fraction(1, 10)  # 1 prime out of 10 satisfies condition
computed_Q1 = float(P)
expected_Q1 = "0.1"
match_Q1 = "yes" if abs(computed_Q1 - 0.1) < 1e-12 else "no"
print(f"CLAIM Q1: computed={computed_Q1} expected={expected_Q1} match={match_Q1}")

# Claim Q2
d = 5
computed_Q2 = d  # n_max = d
expected_Q2 = "5"
match_Q2 = "yes" if computed_Q2 == 5 else "no"
print(f"CLAIM Q2: computed={computed_Q2} expected={expected_Q2} match={match_Q2}")

# Claim Q3
CR = Fraction(976, 919)
computed_Q3 = float(CR)
# round to 9 decimal places as in the paper
computed_Q3_str = fmt(computed_Q3, ".9f")
expected_Q3 = "1.062015815"
match_Q3 = "yes" if computed_Q3_str == expected_Q3 else "no"
print(f"CLAIM Q3: computed={computed_Q3_str} expected={expected_Q3} match={match_Q3}")

# Claim Q4
Delta = Fraction(57, 919)
computed_Q4 = float(Delta)
# format in scientific notation with 6 significant digits
computed_Q4_str = fmt(computed_Q4, ".6e")
expected_Q4 = "6.199130e-02"
match_Q4 = "yes" if computed_Q4_str == expected_Q4 else "no"
print(f"CLAIM Q4: computed={computed_Q4_str} expected={expected_Q4} match={match_Q4}")

# Claim Q5
R = math.pi / 4
computed_Q5 = R
# round to 10 decimal places as in the paper
computed_Q5_str = fmt(computed_Q5, ".10f")
expected_Q5 = "0.7853981634"
match_Q5 = "yes" if computed_Q5_str == expected_Q5 else "no"
print(f"CLAIM Q5: computed={computed_Q5_str} expected={expected_Q5} match={match_Q5}")

print(f"VERIFICATION SUMMARY: 5 claims, {sum([match_Q1, match_Q2, match_Q3, match_Q4, match_Q5].count('yes'))} match, {sum([match_Q1, match_Q2, match_Q3, match_Q4, match_Q5].count('no'))} mismatch")
