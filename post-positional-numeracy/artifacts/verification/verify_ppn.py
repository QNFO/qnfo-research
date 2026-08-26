#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_ppn.py — QNFO.RES.024 post-positional-numeracy verification suite.

Executes the pre-registered hypothesis cards (PROJECT-PLAN §3, amended 2026-08-26):
  H-PPN-1: truncated product formula (S-smooth domain) + general identity
  H-PPN-2: Ostrowski instance checks (strong triangle, integer bound, full product)
  H-PPN-3: finite-adele injectivity on the two-sided Farey window
  Round-trip: componentwise {+,-,*,/} exactness + reconstruction round-trips
Reproducibility: seed 20260826, Python 3.8+, stdlib only.
Exit code 0 iff ALL checks pass.
"""
import json, math, os, random, sys
from fractions import Fraction

SEED = 20260826

# ---------- number-theoretic primitives ----------

def vp(n, p):
    """p-adic valuation of integer n (0 for n=0)."""
    if n == 0:
        return 0
    n = abs(n)
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c

def abs_p(x, p):
    """p-adic absolute value of rational x."""
    f = Fraction(x)
    if f == 0:
        return 0.0
    return float(p ** -(vp(f.numerator, p) - vp(f.denominator, p)))

def abs_inf(x):
    return abs(float(x))

def prod_S(x, S):
    """Truncated product over S U {inf}."""
    out = abs_inf(x)
    for p in S:
        out *= abs_p(x, p)
    return out

def supp(x):
    """Set of primes dividing numerator or denominator of rational x."""
    def factors(n):
        n = abs(n)
        s = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                s.add(d)
                n //= d
            d += 1
        if n > 1:
            s.add(n)
        return s
    f = Fraction(x)
    return factors(f.numerator) | factors(f.denominator)

def encode(x, S, k):
    """Finite-adele image of x: residues mod p^k for p in S."""
    f = Fraction(x)
    return tuple((f.numerator * pow(f.denominator % (p ** k), -1, p ** k)) % (p ** k) for p in S)

def crt(residues, moduli):
    """Garner-style CRT combine."""
    x, M = 0, 1
    for (r, m) in zip(residues, moduli):
        x = (x + (r - x) * pow(M % m, -1, m) * M) % (M * m)
        M *= m
    return x

def rat_reconstruct(r, M, B):
    """Two-step Euclid rational reconstruction: (a, b) reduced with a/b = r mod M,
    |a|, |b| <= B, or None.  (Wang-Guy-Davenport / Dixon algorithm.)"""
    if r == 0:
        return (0, 1)
    r0, r1 = M, r % M
    t0, t1 = 0, 1
    while r1 > B:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
    if abs(t1) <= B:
        a, b = r1, t1
    else:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
        if abs(t1) <= B:
            a, b = r0, t0
        else:
            return None
    if b < 0:
        a, b = -a, -b
    g = math.gcd(abs(a), abs(b)) if b != 0 else 1
    return (a // g, b // g)

# ---------- check machinery ----------

results = {}

def check(name, ok, detail):
    results[name] = {"pass": bool(ok), "detail": str(detail)}
    print(("PASS" if ok else "FAIL"), name, "-", detail)
    return bool(ok)

def main():
    random.seed(SEED)
    all_ok = True

    # --- H-PPN-1 golden values (S = {2,3}) ---
    S23 = [2, 3]
    for name, x, expect in [("6", Fraction(6), 1.0), ("2/3", Fraction(2, 3), 1.0), ("12", Fraction(12), 1.0)]:
        v = prod_S(x, S23)
        all_ok &= check("HPPN1-golden-" + name.replace("/", "over"), abs(v - expect) < 1e-9,
                        "prod_S=%r expect=%r" % (v, expect))
    x = Fraction(5, 2)
    v = prod_S(x, S23)
    inv = 1.0 / abs_p(x, 5)
    all_ok &= check("HPPN1-boundary-5over2", abs(v - 5.0) < 1e-9 and abs(v - inv) < 1e-9,
                    "prod_S=%.12f general_identity=%.12f" % (v, inv))

    # --- H-PPN-1 S-smooth random trials + general identity (S = {2,3,5,7}) ---
    S4 = [2, 3, 5, 7]
    n_smooth = n_general = 0
    max_err = 0.0
    for _ in range(10000):
        x = Fraction(1)
        for p in S4:
            x *= Fraction(p) ** random.randint(-8, 8)
        v = prod_S(x, S4)
        max_err = max(max_err, abs(v - 1.0))
        if abs(v - 1.0) < 1e-9:
            n_smooth += 1
        y = x * Fraction(11) ** random.randint(-6, 6)
        v2 = prod_S(y, S4)
        if abs(v2 - (1.0 / abs_p(y, 11))) < 1e-9:
            n_general += 1
    all_ok &= check("HPPN1-smooth-10k", n_smooth == 10000, "%d/10000 max_err=%.3e" % (n_smooth, max_err))
    all_ok &= check("HPPN1-general-identity-10k", n_general == 10000, "%d/10000" % n_general)

    # --- H-PPN-2 Ostrowski instance checks ---
    n_st = ok_st = 0
    for _ in range(10000):
        a = random.randint(-10 ** 6, 10 ** 6)
        b = random.randint(-10 ** 6, 10 ** 6)
        for p in (2, 3):
            n_st += 1
            if abs_p(a + b, p) <= max(abs_p(a, p), abs_p(b, p)) + 1e-15:
                ok_st += 1
    all_ok &= check("HPPN2-strong-triangle-20k", ok_st == n_st, "%d/%d non-Archimedean" % (ok_st, n_st))
    ok_int = all(abs_p(n, 2) <= 1.0 for n in range(1, 200))
    all_ok &= check("HPPN2-integer-bound", ok_int, "|n|_2 <= 1 for n=1..199")
    for x in [Fraction(6), Fraction(12), Fraction(2, 3), Fraction(9, 4)]:
        v = abs_inf(x)
        for p in supp(x):
            v *= abs_p(x, p)
        all_ok &= check("HPPN2-full-product-" + str(x).replace("/", "over"),
                        abs(v - 1.0) < 1e-9, "prod over all places = %.12f" % v)

    # --- H-PPN-3 injectivity: brute force on small windows ---
    for (S, k) in [([2, 3], 2), ([2, 3], 3), ([2, 3, 5], 1)]:
        M = 1
        for p in S:
            M *= p ** k
        B = math.isqrt(M // 2)
        seen = {}
        n_pairs = 0
        for b in range(1, B + 1):
            if math.gcd(b, M) != 1:
                continue
            for a in range(-B, B + 1):
                n_pairs += 1
                img = encode(Fraction(a, b), S, k)
                seen.setdefault(img, set()).add(Fraction(a, b))
        n_coll = sum(1 for imgs in seen.values() if len(imgs) > 1)
        all_ok &= check("HPPN3-bruteforce-S%s-k%d" % ("".join(map(str, S)), k), n_coll == 0,
                        "M=%d B=%d pairs=%d distinct_rationals=%d distinct_images=%d colliding=%d"
                        % (M, B, n_pairs, sum(len(v) for v in seen.values()), len(seen), n_coll))

    # --- Amendment counterexample (documented, expected collision in the OLD window) ---
    S = [2, 3, 5]
    img17 = encode(Fraction(1, 7), S, 1)
    img13 = encode(Fraction(13), S, 1)
    all_ok &= check("AMENDMENT-counterexample", img17 == img13 and abs(float(Fraction(1, 7))) <= 15 and 13 <= 15,
                    "1/7 and 13 share image %s mod 30; both |x|<=15 -> one-sided window non-injective (amended)" % (img17,))

    # --- H-PPN-3 injectivity: 10^5 seeded random trials (large M) ---
    S = [2, 3, 5]
    k = 4
    mods = [p ** k for p in S]
    M = 1
    for m in mods:
        M *= m
    B = math.isqrt(M // 2)
    coll = failed = accepted = 0
    for _ in range(100000):
        while True:
            b = random.randint(1, B)
            if math.gcd(b, M) == 1:
                break
        a = random.randint(-B, B)
        if math.gcd(a, b) != 1:
            continue
        accepted += 1
        x = Fraction(a, b)
        r = crt(encode(x, S, k), mods)
        rec = rat_reconstruct(r, M, B)
        if rec is None:
            failed += 1
            continue
        if Fraction(*rec) != x:
            coll += 1
    all_ok &= check("HPPN3-random-100k", coll == 0 and failed == 0,
                    "M=%d B=%d accepted=%d collisions=%d recon_failures=%d" % (M, B, accepted, coll, failed))

    # --- Reconstruction algorithm validated against brute force (small window) ---
    S = [2, 3]
    mods = [8, 27]
    M = 216
    B = math.isqrt(M // 2)
    ok_rec = total_rec = 0
    for b in range(1, B + 1):
        if math.gcd(b, M) != 1:
            continue
        for a in range(-B, B + 1):
            total_rec += 1
            r = crt(encode(Fraction(a, b), S, 3), mods)
            rec = rat_reconstruct(r, M, B)
            if rec is not None and Fraction(*rec) == Fraction(a, b):
                ok_rec += 1
    all_ok &= check("RECON-validate-small", ok_rec == total_rec, "euclid reconstruction vs brute force %d/%d" % (ok_rec, total_rec))

    # --- Round-trip: componentwise arithmetic exactness (window operands) ---
    S = [2, 3, 5]
    k = 4
    mods = [p ** k for p in S]
    M = 1
    for m in mods:
        M *= m
    B = math.isqrt(M // 2)

    def rand_operand():
        while True:
            a = random.randint(-B, B)
            b = random.randint(1, B)
            if math.gcd(a, M) == 1 and math.gcd(b, M) == 1:
                return Fraction(a, b)

    ok_ops = total_ops = 0
    n_roundtrip = 0
    for _ in range(20000):
        x, y = rand_operand(), rand_operand()
        ex, ey = encode(x, S, k), encode(y, S, k)
        ops = [("+", x + y, lambda i: (ex[i] + ey[i]) % mods[i]),
               ("-", x - y, lambda i: (ex[i] - ey[i]) % mods[i]),
               ("*", x * y, lambda i: (ex[i] * ey[i]) % mods[i]),
               ("/", x / y, lambda i: (ex[i] * pow(ey[i], -1, mods[i])) % mods[i])]
        for _name, exact, lam in ops:
            total_ops += 1
            if tuple(lam(i) for i in range(len(S))) == encode(exact, S, k):
                ok_ops += 1
        z = x + y
        if abs(z.numerator) <= B and abs(z.denominator) <= B and math.gcd(z.denominator, M) == 1:
            rec = rat_reconstruct(crt(encode(z, S, k), mods), M, B)
            if rec is not None and Fraction(*rec) == z:
                n_roundtrip += 1
    all_ok &= check("RT-componentwise-80k", ok_ops == total_ops, "%d/%d op-exactness" % (ok_ops, total_ops))
    all_ok &= check("RT-reconstruct-roundtrips", n_roundtrip > 0, "%d full round-trips exact" % n_roundtrip)

    # ---------- write evidence ----------
    out = {
        "date": "2026-08-26",
        "project": "QNFO.RES.024 post-positional-numeracy",
        "seed": SEED,
        "python": sys.version.split()[0],
        "hypothesis_cards": ["H-PPN-1 (truncated product formula + general identity)",
                             "H-PPN-2 (Ostrowski instance checks)",
                             "H-PPN-3 (two-sided Farey window injectivity)"],
        "windows": {"M216": {"S": [2, 3], "k": 3, "B": math.isqrt(108)},
                    "M36": {"S": [2, 3], "k": 2, "B": math.isqrt(18)},
                    "M30": {"S": [2, 3, 5], "k": 1, "B": math.isqrt(15)}},
        "all_pass": all_ok,
        "results": results,
    }
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "ppn-verification-results.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print("WROTE ppn-verification-results.json; ALL PASS =", all_ok)
    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()
