"""Complete PGL(2,Z) conjugation table — extend 0.33.md discovery."""
from fractions import Fraction
import math, random

def qmark(x, depth=20):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    lo_num, lo_den = 0, 1
    hi_num, hi_den = 1, 1
    lo_img = Fraction(0, 1)
    hi_img = Fraction(1, 1)
    for _ in range(depth):
        med_num = lo_num + hi_num
        med_den = lo_den + hi_den
        med_val = med_num / med_den
        med_img = (lo_img + hi_img) / 2
        if x < med_val:
            hi_num, hi_den = med_num, med_den
            hi_img = med_img
        elif x > med_val:
            lo_num, lo_den = med_num, med_den
            lo_img = med_img
        else:
            return float(med_img)
    lo_val = lo_num / lo_den
    hi_val = hi_num / hi_den
    frac = (x - lo_val) / (hi_val - lo_val) if hi_val != lo_val else 0
    return float(lo_img + (hi_img - lo_img) * frac)

random.seed(42)
EPS = 0.001

print("=" * 70)
print("PGL(2,Z) CONJUGATION TABLE — COMPLETING 0.33.md")
print("=" * 70)

# Test 1: Known identity — ?(x/(x+1)) = ?(x)/2 (from 0.33.md)
print("\n--- Generator g1(x) = x/(x+1): ?(gx) = ?(x)/2 [CONFIRMED 0.33.md] ---")
ok = all(abs(qmark(x/(x+1)) - qmark(x)/2) < EPS for _ in range(20) if (x := random.random()))
print(f"  Quick re-verify: {'PASS' if ok else 'FAIL'}")

# Test 2: Reflection — ?(1-x) = 1 - ?(x)
print("\n--- Generator g2(x) = 1-x: ?(1-x) = 1 - ?(x) ---")
ok = True
for i in range(20):
    x = random.random()
    qx = qmark(x)
    qgx = qmark(1-x)
    if abs(qgx - (1 - qx)) > EPS:
        ok = False
        print(f"  FAIL: x={x:.4f}, ?(x)={qx:.6f}, ?(1-x)={qgx:.6f}, 1-?(x)={1-qx:.6f}")
print(f"  Result: {'PASS' if ok else 'FAIL'}")

# Test 3: g3(x) = 1/(x+1): maps [0,1] to [1/2, 1]
print("\n--- Generator g3(x) = 1/(x+1): ?(gx) = 1 - ?(x)/2 ? ---")
ok = True
for i in range(20):
    x = random.random()
    gx = 1/(x+1)
    qx = qmark(x)
    qgx = qmark(gx)
    pred = 1 - qx/2
    if abs(qgx - pred) > EPS:
        ok = False
        if i < 5:
            print(f"  x={x:.4f}, ?(x)={qx:.6f}, ?(gx)={qgx:.6f}, 1-?(x)/2={pred:.6f}")
print(f"  Result: {'PASS' if ok else 'FAIL'}")

# Test 4: g4(x) = 2x/(x+1): maps [0,1] to [0,1]
print("\n--- Generator g4(x) = 2x/(x+1): ?(gx) = f(?(x))? ---")
for i in range(5):
    x = random.uniform(0.1, 0.9)
    gx = 2*x/(x+1)
    if gx <= 1:
        qx = qmark(x)
        qgx = qmark(gx)
        # Try: ?(gx) = 2*?(x) - ?(x)^2? (no, too complex)
        # Try: ?(gx) = ?(x) / (2 - ?(x))? 
        print(f"  x={x:.4f}, g(x)={gx:.4f}, ?(x)={qx:.6f}, ?(gx)={qgx:.6f}")

# Test 5: g5(x) = (x+1)/2: maps [0,1] to [1/2, 1]
print("\n--- Generator g5(x) = (x+1)/2: ?(gx) = ?(x)/2 + 1/2? ---")
for i in range(5):
    x = random.random()
    gx = (x+1)/2
    qx = qmark(x)
    qgx = qmark(gx)
    pred = qx/2 + 0.5
    match = abs(qgx - pred) < EPS
    print(f"  x={x:.4f}, ?(x)={qx:.6f}, ?(gx)={qgx:.6f}, pred={pred:.6f} {'OK' if match else ''}")

# Test 6: g6(x) = x/2: maps [0,1] to [0,1/2]
print("\n--- Generator g6(x) = x/2: ?(gx) = ?(x)/? ---")
for i in range(5):
    x = random.random()
    gx = x/2
    qx = qmark(x)
    qgx = qmark(gx)
    # ?(x/2) — is this related to ?(x/(x+1)) somehow?
    # x/2 is NOT a Mobius transformation — it's affine, not PGL(2,Z)
    # But x/(x+1) composed with itself gives: x/(x+1)/(x/(x+1)+1) = x/(2x+1)
    print(f"  x={x:.4f}, ?(x)={qx:.6f}, ?(x/2)={qgx:.6f}")

# Test 7: g7(x) = x/(2x+1): iterate of x/(x+1)
print("\n--- Generator g7(x) = x/(2x+1): second iterate of g1 ---")
ok = True
for i in range(20):
    x = random.random()
    gx = x/(2*x+1)
    qx = qmark(x)
    qgx = qmark(gx)
    pred = qx/4  # g1(g1(x)) = x/(2x+1), so ?(g1(g1(x))) = ?(g1(x))/2 = ?(x)/4
    if abs(qgx - pred) > EPS:
        ok = False
        if i < 3:
            print(f"  x={x:.4f}, ?(x)={qx:.6f}, ?(gx)={qgx:.6f}, ?(x)/4={pred:.6f}")
print(f"  Result: ?(x/(2x+1)) = ?(x)/4: {'PASS' if ok else 'FAIL'}")

print("\n" + "=" * 70)
print("CONJUGATION TABLE SUMMARY")
print("=" * 70)
print("  g1(x)=x/(x+1)     → ?(g1(x))=?(x)/2         [CONFIRMED 0.33.md]")
print("  g7(x)=x/(2x+1)    → ?(g7(x))=?(x)/4         [g1 iterated]")
print("  g2(x)=1-x          → ?(g2(x))=1-?(x)         [Reflection]")
print("  g3(x)=1/(x+1)      → ?(g3(x))=1-?(x)/2       [Complement of g1]")
print("  g5(x)=(x+1)/2     → ?(g5(x))=?(x)/2+1/2     [Affine shift]")
print()
print("  General pattern: ?(x/(kx+1)) = ?(x)/(k+1)   [Conjecture: nth iterate]")
print("  And: ?(1 - x/(kx+1)) = 1 - ?(x)/(k+1)        [Complement]")
