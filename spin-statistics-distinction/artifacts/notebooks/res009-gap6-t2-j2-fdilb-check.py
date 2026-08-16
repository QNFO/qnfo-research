"""
RES.009 GAP-6 T2 -- J2 (Transposition) executable check in FdHilb
CODE-EXECUTED evidence for the "so-what / depth-of-premises" synthesis (2026-08-16).

Verdict being evidenced: the mark calculus is two-valued (Boolean) logic on the
classical sector. Its categorical realization in a Hilbert space requires the
classical structure (special dagger Frobenius, Coecke-Duncan 0906.4725) PLUS an
involutive braiding PLUS complementarity. The naive operator-level Boolean gates
collapse -- which is precisely WHY the resolution law is not an operator identity
and why "derive fermions from the mark" fails at the logic-to-Hilbert-space step.

Checks:
 (1)  Classical structure axioms (Frobenius/special/commutative/unit/counit): PASS
 (2)  Canonical braiding involutivity  sigma^2 = id:  PASS
 (3)  J2 (resolution law) with merge-as-AND:          FAIL (term == ZERO map)
 (4)  J2 with bilinear Boolean-AND:                   FAIL (term == ZERO map)
 (5)  J2 on the classical sector (Boolean functions): PASS (two-valued identity)
 (6)  Non-involutive candidate S: S^2 != I  -- involutivity is a specialization
 (6b) TL braid  sigma_TL = A*I + A^{-1}*U  satisfies
        sigma_TL^2 = A^2 I + (2 + 2 A^{-2}) U  !=  I   (Claim C, quantitative)
"""
import numpy as np

I2 = np.eye(2)
I4 = np.eye(4)

def delta():
    D = np.zeros((4, 2)); D[0, 0] = 1.0; D[3, 1] = 1.0; return D   # e0->|00>, e1->|11>

def merge():
    M = np.zeros((2, 4)); M[0, 0] = 1.0; M[1, 3] = 1.0; return M   # |00>->e0, |11>->e1

eps   = np.array([[1.0, 1.0]])                       # discard: eps(ei)=1
u     = np.array([[1.0], [1.0]])                     # unit: 1 -> e0+e1
sigma = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], dtype=float)  # flip
NOT   = np.array([[0,1],[1,0]], dtype=float)         # basis negation

def kron(*ms):
    r = ms[0]
    for m in ms[1:]:
        r = np.kron(r, m)
    return r

ok = True
def check(name, A, B, tol=1e-12, expect=True):
    global ok
    passed = float(np.max(np.abs(A - B))) < tol
    if passed != expect:
        ok = False
    print(f"[{'PASS' if passed else 'FAIL'}] {name} (expected {'PASS' if expect else 'FAIL'})")
    return passed

D, M = delta(), merge()

# (1) classical structure axioms -- operator identities
check("(1a) Frobenius (m id)(id d) = (id m)(d id)", kron(M, I2) @ kron(I2, D), kron(I2, M) @ kron(D, I2), expect=True)
check("(1b) Special m d = id", M @ D, I2, expect=True)
check("(1c) Commutative m sigma = m", M @ sigma, M, expect=True)
check("(1d) Unit m (u id) = id", M @ kron(u, I2), I2, expect=True)
check("(1e) Counit (eps id) d = id", kron(eps, I2) @ D, I2, expect=True)

# (2) canonical braiding involutivity (Claim A/C condition)
check("(2) Involutivity sigma^2 = id", sigma @ sigma, I4, expect=True)

# J2 term: t(a,b) = NOT ( m( NOT(m(a,b)) x NOT(m(a,NOT(b))) ) ) with duplication via delta
def j2(AND, BR):
    N1 = NOT @ AND                       # NOT(a AND b)
    N2 = NOT @ AND @ kron(I2, NOT)       # NOT(a AND NOT b)
    return NOT @ M @ kron(N1, N2) @ kron(kron(I2, BR), I2) @ kron(D, D)

P1 = np.zeros((2, 4)); P1[0, 0] = 1.0; P1[0, 1] = 1.0; P1[1, 2] = 1.0; P1[1, 3] = 1.0  # first projection

# (3) merge-as-AND (classical-structure merge is NOT Boolean AND on mixed inputs)
t = j2(M, sigma)
check("(3) J2(merge-as-AND) = pi1", t, P1, expect=False)
print(f"    |01> -> {t[:, 1].tolist()} (expected e0=[1,0]);  J2(merge) is the ZERO map")

# (4) bilinear Boolean AND (multiplication: only |11> -> e1)
Mb = np.zeros((2, 4)); Mb[1, 3] = 1.0
tb = j2(Mb, sigma)
check("(4) J2(Boolean-AND) = pi1", tb, P1, expect=False)
print(f"    |11> -> {tb[:, 3].tolist()} (expected e1=[0,1]);  J2(Boolean-AND) is the ZERO map")

# (5) classical sector (two-valued Boolean identity)
cl = all(((a and b) or (a and (not b))) == a for a in (0, 1) for b in (0, 1))
print(f"[{'PASS' if cl else 'FAIL'}] (5) J2 on classical sector: (a&b)|(a&~b) = a for all a,b")
if not cl:
    ok = False

# (6) involutivity is a genuine specialization
ph = np.exp(1j * 0.7)
S = sigma @ np.diag([1.0, ph, ph, 1.0])               # unitary, S^2 != I
d6 = float(np.max(np.abs((S @ S) - I4)))
print(f"[{'PASS' if d6 > 1e-9 else 'FAIL'}] (6) non-involutive candidate S: S^2 != I (max|diff|={d6:.3e}) -- involutivity is a specialization")
if d6 <= 1e-9:
    ok = False

# (6b) TL braid on self-dual M = C^2 (cup-cap U = Bell projector), Claim C quantitative
A = np.exp(1j * np.pi / 5)                            # A^4 != 1 (anyon regime)
v = np.array([1.0 + 0j, 0, 0, 1.0 + 0j])              # Bell vector |00>+|11>
U = np.outer(v, v)                                    # uncrossing, U^2 = 2 U (delta = dim = 2)
dU = float(np.max(np.abs((U @ U) - 2.0 * U)))
print(f"[{'PASS' if dU < 1e-12 else 'FAIL'}] (6b.1) TL uncrossing U: U^2 = delta*U (delta=2)")
if dU >= 1e-12:
    ok = False
sTL = A * I4 + (1.0 / A) * U                          # sigma_TL = A I + A^{-1} U
lhs = sTL @ sTL
rhs = (A ** 2) * I4 + (2.0 + 2.0 / (A ** 2)) * U
dTL = float(np.max(np.abs(lhs - rhs)))
print(f"[{'PASS' if dTL < 1e-12 else 'FAIL'}] (6b.2) TL braid: sigma^2 = A^2 I + (2+2A^{-2}) U (verified)")
if dTL >= 1e-12:
    ok = False
dTLinv = float(np.max(np.abs((sTL @ sTL) - I4)))
print(f"[{'PASS' if dTLinv > 1e-9 else 'FAIL'}] (6b.3) TL braid sigma^2 != I for A^4 != 1 (max|diff|={dTLinv:.3e}) -- non-involutive (anyon)")
if dTLinv <= 1e-9:
    ok = False

print()
print("SUMMARY: classical-structure axioms PASS; sigma^2=id PASS;")
print("naive operator-level J2 = ZERO map (fails both merge and Boolean-AND readings);")
print("classical-sector J2 PASS (two-valued Boolean identity);")
print("involutivity is a genuine specialization (S^2 != I); TL braid formula sigma^2 = A^2 I + (2+2A^{-2}) U verified (Claim C).")
print("CONCLUSION: Boolean logic is two-valued ON the classical sector only; operator-level J2")
print("needs complementarity (ZX classical fragment) -- an ADDITIONAL external input.")
print("The mark calculus contributes two-valued logic + involutive-quotient syntax, nothing more.")
print("OVERALL:", "CONSISTENT (expected failures documented)" if ok else "UNEXPECTED RESULT -- review")
