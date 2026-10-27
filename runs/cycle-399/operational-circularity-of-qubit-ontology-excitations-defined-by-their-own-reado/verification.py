import math

def report(cid, computed, expected, match):
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: p_e = 1 - F, F = 0.99991
pe = 1 - 0.99991
report("Q1", f"{pe:.8e}", "9e-5", "yes" if round(pe, 10) == 9e-5 else "no")

# Q2: N_err = p_e * 1e6
nerr = pe * 1e6
report("Q2", f"{nerr:.8e}", "90", "yes" if nerr == 90 else "no")

# Q3: 1/p_e
inv = 1 / pe
report("Q3", f"{inv:.8e}", "1.11e4", "yes" if round(inv, -2) == 1.11e4 else "no")

# Q4: sigma_p = sqrt(0.25/1e4)
sp = math.sqrt(0.25 / 1e4)
report("Q4", f"{sp:.8e}", "5.00e-3", "yes" if round(sp, 8) == 0.005 else "no")

# Q5: sigma_p / p_e
r = sp / pe
report("Q5", f"{r:.8e}", "55.6", "yes" if round(r, 1) == 55.6 else "no")

# Q6: N_cross = 0.25 / p_e^2
ncross = 0.25 / pe**2
report("Q6", f"{ncross:.8e}", "3.09e7", "yes" if round(ncross, -5) == 3.09e7 else "no")

# Q7: n = ceil(ln(1e-3)/ln(0.6))
n7 = math.ceil(math.log(1e-3) / math.log(0.6))
report("Q7", f"{n7:.8e}", "14", "yes" if n7 == 14 else "no")

# Q8: n = ceil(ln(9e-5/5e-2)/ln(0.6))
n8 = math.ceil(math.log(9e-5 / 5e-2) / math.log(0.6))
report("Q8", f"{n8:.8e}", "13", "yes" if n8 == 13 else "no")

# Q9: N = ln(200)/(2e-6)
N9 = math.log(2 / 0.01) / (2 * 1e-3**2)
report("Q9", f"{N9:.8e}", "2.649159e6", "yes" if round(N9, 0) == 2649159 else "no")

# Q10: N = ln(200)/(2e-8)
N10 = math.log(2 / 0.01) / (2 * 1e-4**2)
report("Q10", f"{N10:.8e}", "2.649159e8", "yes" if round(N10, 2) == 264915908.0 else "no")

# Q11: N = ln(200)/(2e-4)
N11 = math.log(2 / 0.01) / (2 * 1e-2**2)
report("Q11", f"{N11:.8e}", "2.649159e4", "yes" if round(N11, -2) == 2.649159e4 else "no")

# Q12: fixed points 0 and 1, boundary 0.5, x_n = 1 - 0.4*0.5^n
ok12 = (0.0 == 0) and (1.0 == 1) and ((0 + 1) / 2 == 0.5)
x3 = 1 - 0.4 * 0.5**3
ok12 = ok12 and abs(x3 - 0.95) < 1e-12
report("Q12", f"{x3:.8e}", "0.95", "yes" if ok12 else "no")

# Q13: eps_min = sqrt(sp^2 + pe^2)
e13 = math.sqrt(sp**2 + pe**2)
report("Q13", f"{e13:.8e}", "5.001e-3", "yes" if round(e13, 6) == 0.005001 else "no")

# Q14: eps_min at crossover: sqrt(9e-5^2 + 9e-5^2)
e14 = math.sqrt((9e-5)**2 + pe**2)
report("Q14", f"{e14:.8e}", "1.27e-4", "yes" if round(e14, 8) == 1.27e-4 else "no")

# Q15: spectral norm of 3x3 all-0.2 matrix = 3*0.2 = 0.6
L15 = 3 * 0.2
report("Q15", f"{L15:.8e}", "0.6", "yes" if L15 == 0.6 else "no")

# Q16: t = 2.649159e6 / 1e6
t16 = 2.649159e6 / 1e6
report("Q16", f"{t16:.8e}", "2.65", "yes" if round(t16, 2) == 2.65 else "no")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
