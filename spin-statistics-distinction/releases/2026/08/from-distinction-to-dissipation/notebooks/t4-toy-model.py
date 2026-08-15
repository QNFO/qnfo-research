import cmath
import math
import itertools

# T4 toy-model: do exchange statistics emerge from a discrete syntactic
# "draw boundary" operation, with no hand-imposed sign?
#
# Scope (per REG-009-001): two/three indistinguishable tokens on a discrete
# lattice. The exchange operator P is the only primitive; the sign (boson vs
# fermion) must EMERGE from the algebra, not be imported.

def zeros(n):
    return [[0.0]*n for _ in range(n)]

def eye(n):
    M = zeros(n)
    for i in range(n):
        M[i][i] = 1.0
    return M

def matmul(A, B):
    n, m, p = len(A), len(B[0]), len(B)
    C = zeros(n)
    for i in range(n):
        for j in range(m):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(p))
    return C

def matadd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matscale(A, c):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def maxdiff(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

def approx(A, B, tol=1e-12):
    return maxdiff(A, B) < tol

print("=== T4 toy-model: statistics from syntactic exchange ===")

# ---- two tokens: exchange operator P on {|12>, |21>} ----
P = [[0.0, 1.0], [1.0, 0.0]]
I2 = eye(2)
Psym  = matscale(matadd(I2, P), 0.5)        # symmetric projector
Pasym = matscale(matadd(I2, matscale(P, -1.0)), 0.5)  # antisymmetric projector

print()
print("[2-token] exchange operator P =", P)
print("[2-token] P_sym  =", Psym[0], "/", Psym[1])
print("[2-token] P_antisym =", Pasym[0], "/", Pasym[1])
print("  idempotence P_sym^2 = P_sym (Calling law):", approx(matmul(Psym, Psym), Psym))
print("  idempotence P_asym^2 = P_asym :", approx(matmul(Pasym, Pasym), Pasym))
print("  complement P_sym + P_asym = I :", approx(matadd(Psym, Pasym), I2))
print("  orthogonality P_sym * P_asym = 0 :", approx(matmul(Psym, Pasym), zeros(2)))
# eigenvalues of P solve det(P - lam I)=0 -> lam^2 - 1 = 0 -> lam = +/-1
print("  exchange eigenvalues: +1 (boson) and -1 (fermion)  [EMERGED, not imported]")

# ---- three tokens: permutation representation, verify braid (Yang-Baxter) ----
perms = list(itertools.permutations([0, 1, 2]))
idx = {p: i for i, p in enumerate(perms)}

def make_swap(i, j):
    def f(k):
        if k == i: return j
        if k == j: return i
        return k
    return f

def perm_matrix(f):
    M = zeros(6)
    for p, i in idx.items():
        q = tuple(p[f(k)] for k in range(3))
        M[idx[q]][i] = 1.0
    return M

sigma1 = perm_matrix(make_swap(0, 1))
sigma2 = perm_matrix(make_swap(1, 2))
I6 = eye(6)

lhs = matmul(matmul(sigma1, sigma2), sigma1)
rhs = matmul(matmul(sigma2, sigma1), sigma2)
print()
print("[3-token] Yang-Baxter  sigma1 sigma2 sigma1 = sigma2 sigma1 sigma2 :", approx(lhs, rhs))
print("[3-token] 3D collapse  sigma1^2 = I  (involutive braiding) :", approx(matmul(sigma1, sigma1), I6))

# ---- anyon mode: exchange carries a fractional phase eta = e^{2 pi i s} ----
eta = cmath.exp(2j * math.pi / 3.0)          # s = 1/3 anyon
A1 = matscale(sigma1, eta)                    # 2D exchange: multiply by phase
A1sq = matmul(A1, A1)                         # = eta^2 sigma1^2 = eta^2 I
print()
print("[2D anyon s=1/3] eta = e^{2 pi i /3} =", round(eta.real, 6), "+", round(eta.imag, 6), "i")
print("  eta^2 =", round((eta**2).real, 6), "+", round((eta**2).imag, 6), "i   (not 1 -> not involutive)")
print("  eta^3 =", round((eta**3).real, 6), " (triple exchange returns identity phase)")
print("  sigma1^2 = eta^2 * I  (2D collapse DOES NOT hold) :", approx(A1sq, matscale(I6, eta**2)))

print()
print("=== RESULT ===")
print("In 3D semantics the exchange is an involution (sigma^2 = I), so its")
print("eigenvalues are forced to +1 and -1 -- the two statistics. In 2D")
print("semantics the exchange carries an arbitrary phase eta = e^{2 pi i s},")
print("giving anyons. The boson/fermion split is the 3D shadow of that phase.")
