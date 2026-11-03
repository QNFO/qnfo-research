import math

def sig(x, n):
    if x == 0:
        return 0.0
    from math import floor, log10
    d = math.floor(log10(abs(x)))
    return round(x, n - 1 - d)

results = []

# Q1: omega_C = 2*8.187e-14 / 1.0546e-34
computed = 2 * 8.187e-14 / 1.0546e-34
expected = "1.55e21"
exp_val = 1.55e21
match = "yes" if f"{sig(computed,3):.3e}" == f"{exp_val:.3e}" else "no"
results.append(("Q1", computed, exp_val, match))

# Q2: lambda_C/2 = 1.0546e-34 / (2*9.109e-31*2.998e8)
computed = 1.0546e-34 / (2 * 9.109e-31 * 2.998e8)
expected = "1.93e-13"
exp_val = 1.93e-13
match = "yes" if f"{sig(computed,3):.3e}" == f"{exp_val:.3e}" else "no"
results.append(("Q2", computed, exp_val, match))

# Q3: 4.0000/4.0000
computed = 4.0000 / 4.0000
exp_val = 1.0000
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q3", computed, exp_val, match))

# Q4: 4.0000/4.4721
computed = 4.0000 / 4.4721
exp_val = 0.8944
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q4", computed, exp_val, match))

# Q5: 4.0000/5.8284
computed = 4.0000 / 5.8284
exp_val = 0.6863
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q5", computed, exp_val, match))

# Q6: 4.0000/13.4164
computed = 4.0000 / 13.4164
exp_val = 0.2981
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q6", computed, exp_val, match))

# Q7: sqrt(1+0.5^2)
computed = math.sqrt(1 + 0.5**2)
exp_val = 1.1180
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q7", computed, exp_val, match))

# Q8: sqrt(1+1^2)
computed = math.sqrt(1 + 1**2)
exp_val = 1.4142
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q8", computed, exp_val, match))

# Q9: sqrt(1+2^2)
computed = math.sqrt(1 + 2**2)
exp_val = 2.2361
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q9", computed, exp_val, match))

# Q10: 20/(2*(20-1))
computed = 20 / (2 * (20 - 1))
exp_val = 0.5263
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q10", computed, exp_val, match))

# Q11: 50/(2*(50-1))
computed = 50 / (2 * (50 - 1))
exp_val = 0.5102
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q11", computed, exp_val, match))

# Q12: limit N/(2(N-1)) = 1/2
computed = 0.5
exp_val = 0.5
match = "yes" if computed == exp_val else "no"
results.append(("Q12", computed, exp_val, match))

# Q13: 57 - 100*20/(2*19)
computed = 57 - 100 * 20 / (2 * 19)
exp_val = 4.4
match = "yes" if sig(computed, 2) == exp_val else "no"
results.append(("Q13", computed, exp_val, match))

# Q14: 57 - 100*50/(2*49)
computed = 57 - 100 * 50 / (2 * 49)
exp_val = 6.0
match = "yes" if sig(computed, 2) == exp_val else "no"
results.append(("Q14", computed, exp_val, match))

n_match = 0
for cid, comp, exp, m in results:
    print(f"CLAIM {cid}: computed={comp:.8g} expected={exp} match={m}")
    if m == "yes":
        n_match += 1
print(f"VERIFICATION SUMMARY: {len(results)} claims, {n_match} match, {len(results)-n_match} mismatch")
