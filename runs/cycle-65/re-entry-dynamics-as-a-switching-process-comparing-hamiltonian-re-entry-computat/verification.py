import math
from fractions import Fraction

# Stated inputs from the paper (Section 4: Inputs 1 and 2)
k_acc = 4        # memory accesses per operation (structural integer)
t_mem = 16       # time units per memory access (assumed)
t_alu = 1        # time units for logical work (assumed normalization)
t_dyn = 4        # time units per useful dynamical segment (assumed)
t_re = 1         # time units re-entry overhead (assumed)
N_op = 10**6     # operations in Derivation 5

results = []

def check(cid, computed, expected):
    if expected is None:
        match = "n/a"
    else:
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    results.append(match)
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: c_sw = k_acc*t_mem + t_alu
c_sw = k_acc * t_mem + t_alu
check("Q1", c_sw, 65)

# Q2: f_sw = (k_acc*t_mem)/(k_acc*t_mem + t_alu)
f_sw = Fraction(k_acc * t_mem, k_acc * t_mem + t_alu)
check("Q2", float(f_sw), 64 / 65)

# Q3: c_re = t_dyn + t_re
c_re = t_dyn + t_re
check("Q3", c_re, 5)

# Q4: f_re = t_re/(t_dyn + t_re)
f_re = Fraction(t_re, t_dyn + t_re)
check("Q4", float(f_re), 0.2)

# Q5: T_sw = N_op * c_sw
T_sw = N_op * c_sw
check("Q5", T_sw, 6.5e7)

# Q6: T_re = N_op * c_re
T_re = N_op * c_re
check("Q6", T_re, 5.0e6)

# Q7: ratio = c_sw / c_re
ratio = Fraction(c_sw, c_re)
check("Q7", float(ratio), 13.0)

# Q8: t_mem* = (t_dyn + t_re - t_alu)/k_acc
t_mem_star = Fraction(t_dyn + t_re - t_alu, k_acc)
check("Q8", float(t_mem_star), 1)

n = len(results)
m = sum(1 for r in results if r == "yes")
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")
