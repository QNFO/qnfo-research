"""FQ1-FULL-SCAN: confirmation of the v_2(A_j) enumerator-parity invariant (Avenue A1).

Upgrades FQ1-EXP-001 (1 code/family) to bulk families with the distance confound
explicitly controlled. Re-specified REG-RES006-001 (the original Kodaira-Neron leg
is BLOCKED on NTOF source under-specification: Mahler target function, I_C ideal).

Families (deterministic seed 20260814):
  CSS     : random CSS [[n,1]] codes with d >= 3, 5 each at n = 7, 9, 11
  Optimal : [[5,1,3]] (perfect), [[7,1,3]] (Steane), [[9,1,3]] (Shor)
  Surface : [[8,2,2]], [[18,2,3]] (toric L = 2, 3)
  Hamming : [[15,7,3]]
  Random  : controls at each matched (n,k) - 20 each for (5,1),(7,1),(8,2),(9,1),
            (11,1); 10 each for (15,7),(18,2); split d=1 vs d>=2 for the
            distance-confound analysis.

Tests:
  1. Per-code percentile of max_v2 vs matched random controls (all, and d>=2-only)
  2. Pooled classifier: 1-sided threshold (max_v2 <= t) and 2-sided fingerprint
     (max_v2 <= 1 or max_v2 >= 5); balanced accuracy vs 50% baseline.
  3. Confound: do d>=2 random controls also sit at the extremes?
"""
import random
from itertools import combinations

SEED = 20260814
rng = random.Random(SEED)


# ---------- GF(2) basis helpers ----------
def basis_reduce(basis, v):
    w = v
    for b in basis:
        lb = b.bit_length() - 1
        if (w >> lb) & 1:
            w ^= b
    return w


def basis_add(basis, v):
    w = basis_reduce(basis, v)
    if w == 0:
        return False
    lb = w.bit_length() - 1
    new_basis = []
    for b in basis:
        if (b >> lb) & 1:
            b ^= w
        if b != 0:
            new_basis.append(b)
    new_basis.append(w)
    new_basis.sort(key=lambda b: b.bit_length(), reverse=True)
    basis[:] = new_basis
    return True


# ---------- Pauli helpers ----------
def v2(x):
    c = 0
    while x % 2 == 0 and x > 0:
        x //= 2
        c += 1
    return c


def weight(x, z):
    return bin(x | z).count("1")


def symplectic(x, z, x2, z2):
    return (bin(x & z2).count("1") + bin(z & x2).count("1")) % 2 == 0


def weight_enumerator(gx, gz, n):
    m = len(gx)
    A = [0] * (n + 1)
    A[0] += 1
    for mask in range(1, 1 << m):
        x = 0
        z = 0
        mm = mask
        i = 0
        while mm:
            if mm & 1:
                x ^= gx[i]
                z ^= gz[i]
            mm >>= 1
            i += 1
        A[weight(x, z)] += 1
    return A


def features(A, n):
    vals = [v2(a) for a in A[1:]]
    return (max(vals) if vals else 0), sum(1 for a in A[1:] if a % 2 == 0)


# ---------- random valid stabilizer code (commuting + independent, GF(2)-fast) ----------
def rand_stabilizer_code(n, m, rng, max_tries=200000):
    gx = []
    gz = []
    basis = []
    for _ in range(m):
        accepted = False
        for _attempt in range(max_tries):
            x = 0
            z = 0
            for i in range(n):
                t = rng.randrange(4)
                if t in (1, 3):
                    x |= (1 << i)
                if t in (2, 3):
                    z |= (1 << i)
            if not all(symplectic(x, z, gxx, gzz) for gxx, gzz in zip(gx, gz)):
                continue
            vec = (z << n) | x
            if not basis_add(basis, vec):
                continue
            gx.append(x)
            gz.append(z)
            accepted = True
            break
        if not accepted:
            raise RuntimeError(f"could not extend stabilizer code n={n} m={m} at gen {len(gx)}")
    return gx, gz, basis


# ---------- distance helpers ----------
def logical_weight(gx, gz, basis, n, w):
    """Smallest weight <= w of a logical operator N(S)\\S, or None if none exists."""
    for ww in range(1, w + 1):
        for pos in combinations(range(n), ww):
            for assign in range(3 ** ww):
                x = 0
                z = 0
                a = assign
                for p in pos:
                    t = a % 3
                    a //= 3
                    if t == 0:
                        x |= (1 << p)
                    elif t == 1:
                        z |= (1 << p)
                    else:
                        x |= (1 << p)
                        z |= (1 << p)
                if not all(symplectic(x, z, gxx, gzz) for gxx, gzz in zip(gx, gz)):
                    continue
                vec = (z << n) | x
                if basis_reduce(basis, vec) != 0:
                    return ww
    return None


def is_d1(gx, gz, basis, n):
    """True if d == 1 (a weight-1 logical exists), else False (d >= 2)."""
    return logical_weight(gx, gz, basis, n, 1) == 1


# ---------- CSS family ----------
def null_space_basis(rows, n):
    """Basis of { v in F2^n : row . v = 0 for all rows }."""
    r = len(rows)
    M = [[(row >> j) & 1 for j in range(n)] for row in rows]
    piv = []
    rowi = 0
    for col in range(n):
        pivot = None
        for i in range(rowi, r):
            if M[i][col]:
                pivot = i
                break
        if pivot is None:
            continue
        M[rowi], M[pivot] = M[pivot], M[rowi]
        for i in range(r):
            if i != rowi and M[i][col]:
                for j in range(n):
                    M[i][j] ^= M[rowi][j]
        piv.append(col)
        rowi += 1
        if rowi == r:
            break
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for pi, pc in enumerate(piv):
            v[pc] = M[pi][f]
        basis.append(v)
    return [sum((1 << j) for j in range(n) if v[j]) for v in basis]


def rand_css_code(n, r1, r2, rng, max_tries=3000):
    """Random CSS [[n, n-r1-r2]] code with d >= 3 (C1 dim r1; D = C2^perp dim r2 <= C1^perp)."""
    for _ in range(max_tries):
        c1 = []
        cbasis = []
        for _ in range(r1):
            row = rng.getrandbits(n)
            while not basis_add(cbasis, row):
                row = rng.getrandbits(n)
            c1.append(row)
        ns = null_space_basis(c1, n)
        dvecs = []
        dbasis = []
        ok = True
        for _ in range(r2):
            v = 0
            for b in ns:
                if rng.randrange(2):
                    v ^= b
            if v == 0 or not basis_add(dbasis, v):
                ok = False
                break
            dvecs.append(v)
        if not ok or len(dvecs) != r2:
            continue
        gx = list(c1)
        gz = [0] * r1
        for v in dvecs:
            gx.append(0)
            gz.append(v)
        basis = []
        for i in range(len(gx)):
            basis_add(basis, (gz[i] << n) | gx[i])
        d = logical_weight(gx, gz, basis, n, 2)
        if d is None:  # d >= 3
            return gx, gz, basis
    return None


# ---------- structured codes ----------
def five_one_three():
    specs = ["XZZXI", "IXZZX", "XIXZZ", "ZXIXZ"]
    gx = []
    gz = []
    for s in specs:
        xm = 0
        zm = 0
        for i, c in enumerate(s):
            if c == "X":
                xm |= (1 << i)
            elif c == "Z":
                zm |= (1 << i)
        gx.append(xm)
        gz.append(zm)
    return gx, gz


def steane():
    rows = [(0, 3, 5, 6), (1, 3, 4, 6), (2, 4, 5, 6)]
    gx = []
    gz = []
    for r in rows:
        xm = 0
        for p in r:
            xm |= (1 << p)
        gx.append(xm)
        gz.append(0)
    for r in rows:
        zm = 0
        for p in r:
            zm |= (1 << p)
        gx.append(0)
        gz.append(zm)
    return gx, gz


def shor9():
    gx = []
    gz = []
    for a in range(3):
        for b in range(2):
            zm = 0
            i = 3 * a + b
            zm |= (1 << i)
            zm |= (1 << (i + 1))
            gx.append(0)
            gz.append(zm)
    xm1 = 0
    xm2 = 0
    for i in range(6):
        xm1 |= (1 << i)
    for i in range(3, 9):
        xm2 |= (1 << i)
    gx.append(xm1)
    gz.append(0)
    gx.append(xm2)
    gz.append(0)
    return gx, gz


def hamming15():
    gx = []
    gz = []
    for b in range(4):
        xm = 0
        for p in range(15):
            if ((p + 1) >> b) & 1:
                xm |= (1 << p)
        gx.append(xm)
        gz.append(0)
    for b in range(4):
        zm = 0
        for p in range(15):
            if ((p + 1) >> b) & 1:
                zm |= (1 << p)
        gx.append(0)
        gz.append(zm)
    return gx, gz


def toric(L):
    def eid(i, j, kind):
        return i * L + j if kind == 0 else L * L + i * L + j
    gx = []
    gz = []
    for i in range(L):
        for j in range(L):
            if i == 0 and j == 0:
                continue
            xm = 0
            xm |= (1 << eid((i - 1) % L, j, 0))
            xm |= (1 << eid(i, j, 0))
            xm |= (1 << eid(i, (j - 1) % L, 1))
            xm |= (1 << eid(i, j, 1))
            gx.append(xm)
            gz.append(0)
    for i in range(L):
        for j in range(L):
            if i == 0 and j == 0:
                continue
            zm = 0
            zm |= (1 << eid(i, j, 0))
            zm |= (1 << eid(i, (j + 1) % L, 0))
            zm |= (1 << eid(i, j, 1))
            zm |= (1 << eid((i + 1) % L, j, 1))
            gx.append(0)
            gz.append(zm)
    return gx, gz


# ---------- scan ----------
def scan():
    print("=" * 78)
    print("FQ1-FULL-SCAN: v_2(A_j) enumerator-parity invariant - bulk confirmation")
    print(f"Seed: {SEED} | structured vs random AT SAME (n,k) | distance confound split")
    print("=" * 78)

    structured = []  # (name, n, m, gx, gz, basis, known_d)

    # CSS family (random CSS with d >= 3), 5 each at n = 7, 9, 11
    for n in (7, 9, 11):
        r1 = (n - 1) // 2
        r2 = (n - 1) // 2
        cnt = 0
        tries = 0
        while cnt < 5 and tries < 300:
            tries += 1
            res = rand_css_code(n, r1, r2, rng)
            if res is None:
                continue
            gx, gz, basis = res
            structured.append((f"CSS[{n},1] #{cnt + 1}", n, len(gx), gx, gz, basis, 3))
            cnt += 1
        print(f"CSS[{n},1]: generated {cnt} codes in {tries} tries (d>=3 filter)")

    # Optimal + Hamming
    for name, n, fn in [
        ("[[5,1,3]] perfect", 5, five_one_three),
        ("[[7,1,3]] Steane", 7, steane),
        ("[[9,1,3]] Shor", 9, shor9),
        ("[[15,7,3]] Hamming", 15, hamming15),
    ]:
        gx, gz = fn()
        m = len(gx)
        basis = []
        for i in range(m):
            basis_add(basis, (gz[i] << n) | gx[i])
        structured.append((name, n, m, gx, gz, basis, 3))

    # Surface (toric)
    for L in (2, 3):
        gx, gz = toric(L)
        n = 2 * L * L
        m = len(gx)
        basis = []
        for i in range(m):
            basis_add(basis, (gz[i] << n) | gx[i])
        structured.append((f"toric L={L} [[{n},2]]", n, m, gx, gz, basis, L))

    # controls per (n,k)
    nctrl_for = {}
    for name, n, m, gx, gz, basis, d in structured:
        key = (n, m)
        if key not in nctrl_for:
            nctrl_for[key] = 10 if n >= 15 else 20

    controls = {}
    for key, nctrl in nctrl_for.items():
        n, m = key
        ctrl = []
        for _ in range(nctrl):
            cgx, cgz, cbasis = rand_stabilizer_code(n, m, rng)
            cA = weight_enumerator(cgx, cgz, n)
            cv, ce = features(cA, n)
            d1b = is_d1(cgx, cgz, cbasis, n)
            ctrl.append((cv, ce, d1b))
        controls[key] = ctrl

    all_struct_v2 = []
    all_rand_v2 = []
    all_rand_d2_v2 = []
    print()
    for name, n, m, gx, gz, basis, d in structured:
        A = weight_enumerator(gx, gz, n)
        max_v2, n_even = features(A, n)
        all_struct_v2.append(max_v2)
        ctrl = controls[(n, m)]
        for cv, ce, d1b in ctrl:
            all_rand_v2.append(cv)
            if not d1b:
                all_rand_d2_v2.append(cv)
        ctrl_v2 = [c[0] for c in ctrl]
        ctrl_v2_d2 = [c[0] for c in ctrl if not c[2]]

        def pct(v, dist):
            return (100.0 * sum(1 for x in dist if x < v) / len(dist)) if dist else float("nan")

        p_all = pct(max_v2, ctrl_v2)
        p_d2 = pct(max_v2, ctrl_v2_d2) if ctrl_v2_d2 else float("nan")
        prof = ", ".join(f"w{j}:{A[j]}" for j in range(n + 1) if A[j])
        print(f"{name}: n={n} k={n - m} m={m} d~{d} max_v2={max_v2} n_even={n_even}")
        print(f"  profile: {prof}")
        print(f"  control max_v2: min={min(ctrl_v2)} med={sorted(ctrl_v2)[len(ctrl_v2) // 2]} max={max(ctrl_v2)}")
        print(f"  pct(all controls): {p_all:.0f}%  |  pct(d>=2 controls, n={len(ctrl_v2_d2)}): {p_d2:.0f}%")
        print(f"  control d>=2 fraction: {len(ctrl_v2_d2)}/{len(ctrl_v2)}")

    # pooled classifier
    print()
    print("=" * 78)
    print("POOLED CLASSIFIER (max_v2 threshold vs 50% balanced baseline)")
    n_s = len(all_struct_v2)
    n_r = len(all_rand_v2)
    print(f"structured n={n_s} | random n={n_r} | random d>=2 n={len(all_rand_d2_v2)}")
    print(f"structured max_v2 values: {sorted(all_struct_v2)}")
    print(f"random max_v2 dist: min={min(all_rand_v2)} med={sorted(all_rand_v2)[len(all_rand_v2) // 2]} max={max(all_rand_v2)}")
    for t in range(0, 6):
        sens = sum(1 for v in all_struct_v2 if v <= t) / n_s
        spec = sum(1 for v in all_rand_v2 if v > t) / n_r
        print(f" 1-sided (max_v2 <= {t}): sensitivity={sens:.2f} specificity={spec:.2f} balanced={0.5 * (sens + spec):.2f}")

    def rule(v):
        return v <= 1 or v >= 5

    sens = sum(1 for v in all_struct_v2 if rule(v)) / n_s
    spec = sum(1 for v in all_rand_v2 if not rule(v)) / n_r
    print(f" 2-sided fingerprint (<=1 or >=5): sensitivity={sens:.2f} specificity={spec:.2f} balanced={0.5 * (sens + spec):.2f}")
    frac_struct = sum(1 for v in all_struct_v2 if rule(v)) / n_s
    frac_rand = sum(1 for v in all_rand_v2 if rule(v)) / n_r
    frac_rand_d2 = (sum(1 for v in all_rand_d2_v2 if rule(v)) / len(all_rand_d2_v2)) if all_rand_d2_v2 else float("nan")
    print(f"at extremes (<=1 or >=5): structured={frac_struct:.2f} random_all={frac_rand:.2f} random_d>=2={frac_rand_d2:.2f}")
    print("=" * 78)
    print("VERDICT_KEYS: percentile extremes / balanced accuracy vs 50% / confound check")


if __name__ == "__main__":
    scan()
