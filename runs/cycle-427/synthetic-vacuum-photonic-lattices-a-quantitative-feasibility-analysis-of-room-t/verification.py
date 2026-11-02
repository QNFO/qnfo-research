import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

kB = 8.617333e-5
T = 300.0
h = 4.135668e-15
c = 2.99792458e8

# Q1
q1 = kB * T
print(f"CLAIM Q1: computed={q1:.8g} expected=0.02585 match={'yes' if sig(q1,4)==0.02585 else 'no'}")

# Q2
q2 = 15 * kB * T
print(f"CLAIM Q2: computed={q2:.8g} expected=0.388 match={'yes' if sig(q2,3)==0.388 else 'no'}")

# Q3
Delta = 15 * kB * T  # 0.38778 eV
q3 = Delta / h
q3_THz = q3 / 1e12
print(f"CLAIM Q3: computed={q3_THz:.8g} expected=93.76 match={'yes' if sig(q3_THz,4)==93.76 else 'no'}")

# Q4
nu = Delta / h
q4 = c / nu
q4_um = q4 * 1e6
print(f"CLAIM Q4: computed={q4_um:.8g} expected=3.20 match={'yes' if sig(q4_um,3)==3.20 else 'no'}")

# Q5
q5 = 2000 / (math.exp(10) - 1)
print(f"CLAIM Q5: computed={q5:.8g} expected=9.08e-2 match={'yes' if sig(q5,3)==9.08e-2 else 'no'}")

# Q6
q6 = 2000 / (math.exp(15) - 1)
print(f"CLAIM Q6: computed={q6:.8g} expected=6.12e-4 match={'yes' if sig(q6,3)==6.12e-4 else 'no'}")

# Q7
phi = (1 + math.sqrt(5)) / 2
q7 = phi ** 100
print(f"CLAIM Q7: computed={q7:.8g} expected=7.93e20 match={'yes' if sig(q7,3)==7.93e20 else 'no'}")

# Q8
q8 = 1e-4 / (2/3)
print(f"CLAIM Q8: computed={q8:.8g} expected=1.5e-4 match={'yes' if sig(q8,2)==1.5e-4 else 'no'}")

# Q9
q9 = 1e-6 / (100 / 30)
print(f"CLAIM Q9: computed={q9:.8g} expected=3e-7 match={'yes' if sig(q9,1)==3e-7 else 'no'}")

# Q10
q10 = 1e-4 / 3e-3
print(f"CLAIM Q10: computed={q10:.8g} expected=0.033333333 match={'yes' if abs(q10 - 1/30) < 1e-12 else 'no'}")

# Q11
q11 = 3e-7 / 1e-5
print(f"CLAIM Q11: computed={q11:.8g} expected=3e-2 match={'yes' if sig(q11,1)==3e-2 else 'no'}")

# Q12
q12 = 15 * kB * 77
print(f"CLAIM Q12: computed={q12:.8g} expected=9.95e-2 match={'yes' if sig(q12,3)==9.95e-2 else 'no'}")

claims = [q1==q1, True]*0  # placeholder no-op
results = []
# summary
matches = 0
total = 12
# recompute match flags
m = []
m.append(sig(q1,4)==0.02585)
m.append(sig(q2,3)==0.388)
m.append(sig(q3_THz,4)==93.76)
m.append(sig(q4_um,3)==3.20)
m.append(sig(q5,3)==9.08e-2)
m.append(sig(q6,3)==6.12e-4)
m.append(sig(q7,3)==7.93e20)
m.append(sig(q8,2)==1.5e-4)
m.append(sig(q9,1)==3e-7)
m.append(abs(q10-1/30)<1e-12)
m.append(sig(q11,1)==3e-2)
m.append(sig(q12,3)==9.95e-2)
print(f"VERIFICATION SUMMARY: {total} claims, {sum(m)} match, {total - sum(m)} mismatch")
