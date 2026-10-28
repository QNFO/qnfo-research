import math

def claim_Q1():
    n = 10
    m = (n - 2) // 2
    M1 = m * 4**2 + n * 1**2
    return M1

def claim_Q2():
    n = 10
    return 9 * n - 16

def claim_Q3():
    n = 9
    m = (n - 1) // 2
    M1 = (m - 1) * 4**2 + 1 * 3**2 + n * 1**2
    return M1

def claim_Q4():
    n = 9
    return 9 * n - 15

def claim_Q5():
    n = 8
    return 11 * n - 27

def claim_Q6():
    n = 9
    return 11 * n - 27

def claim_Q7():
    n = 10
    return 11 * n - 27

def claim_Q8():
    n = 12
    return 11 * n - 27

def claim_Q9():
    # m = (n-2)/2 derived from 4m + n = 2(m+n-1)
    # verify symbolically at a sample even n: solve 4m + n - (2m + 2n - 2) = 0
    n = 10
    # 4m + n = 2m + 2n - 2  =>  2m = n - 2  =>  m = (n-2)/2
    m = (n - 2) / 2
    lhs = 4 * m + n
    rhs = 2 * (m + n - 1)
    ok = abs(lhs - rhs) < 1e-12
    return m if ok else None

def claim_Q10():
    # m = (n-1)/2 derived from 4(m-1) + 3 + n = 2(m+n-1)
    n = 9
    m = (n - 1) / 2
    lhs = 4 * (m - 1) + 3 + n
    rhs = 2 * (m + n - 1)
    ok = abs(lhs - rhs) < 1e-12
    return m if ok else None

def claim_Q11():
    # 3*4 + r*3 + 9 = 2(3 + r + 9 - 1) => 21 + 3r = 2r + 22 => r = 1; s = n/3
    n = 9
    # solve 21 + 3r = 2r + 22
    r = 22 - 21  # 3r - 2r = 22 - 21
    s = n / 3
    return (s, r)

def claim_Q12():
    m = 4
    n = 10
    N = m + n
    lhs = 4 * 4 + 10 * 1
    rhs = 2 * (N - 1)
    return (lhs, rhs)

def claim_Q13():
    m = 4
    n = 9
    N = m + n
    lhs = 3 * 4 + 3 + 9
    rhs = 2 * (N - 1)
    return (lhs, rhs)

def fmt(v):
    if isinstance(v, tuple):
        return "(" + ", ".join(fmt(x) for x in v) + ")"
    if v is None:
        return "None"
    if isinstance(v, int):
        return str(v)
    return f"{v:.8f}"

results = [
    ("Q1", claim_Q1(), "74"),
    ("Q2", claim_Q2(), "74"),
    ("Q3", claim_Q3(), "66"),
    ("Q4", claim_Q4(), "66"),
    ("Q5", claim_Q5(), "61"),
    ("Q6", claim_Q6(), "72"),
    ("Q7", claim_Q7(), "83"),
    ("Q8", claim_Q8(), "105"),
    ("Q9", claim_Q9(), "4"),
    ("Q10", claim_Q10(), "4"),
    ("Q11", claim_Q11(), "(3, 1)"),
    ("Q12", claim_Q12(), "(26, 26)"),
    ("Q13", claim_Q13(), "(24, 24)"),
]

match_count = 0
for cid, computed, expected in results:
    comp_str = fmt(computed)
    match = comp_str == expected
    if match:
        match_count += 1
    print(f"CLAIM {cid}: computed={comp_str} expected={expected} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
