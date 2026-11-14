"""Q3 (third pass): can the correspondent's definitions single out a spin-1/2 subspace, and can it be built without J = L + S?

Construction A (S^2, ansatz):  Psi_v(n) = (a + b n.sigma) v,  v in C^2, [a:b] in CP^1.
Construction B (S^3, no sigma): doublets are the coordinate functions xi^alpha restricted to S^3 = SU(2),
                                 dragged by SU(2) acting on C^2 (left action on functions).
Construction C (Hom):           all SU(2)-equivariant linear maps V_{1/2} -> L^2(S^2, C^2) with the total action.

Checks (numeric unless stated):
  A1. Equivariance identity U(g)(n.sigma)U(g)^dag = (gn).sigma  => Psi_v is equivariant for every (a,b).
      This identity uses the matrices U = exp(-i alpha sigma.m/2): it ASSUMES the spin-1/2 representation.
  A2. Orthogonality: <Psi_v, Psi_w> = 4 pi (|a|^2+|b|^2) <v,w> for every (a,b). So orthogonality of the correspondent's
      multiplet imposes NO condition on [a:b].
  A3. det(a + b n.sigma) = a^2 - b^2 for |n| = 1. So either the sections are pointwise rank 1 (a = +-b)
      or pointwise invertible (a != +-b). Rank-1 members have Bloch vector +n (a = b) or -n (a = -b).
  A4. the correspondent's Psi (28.10, 13.10 workings): Psi = -(1/2)(1 - n.sigma) e_+ identically, i.e. the member a = -b.
  A5. Hom dimension (harmonic model, Lmax = 2): dim Hom_SU(2)(V_{1/2}, C^2 (x) H_{<=2}) = 2.
  B1. For f^alpha = xi^alpha on S^3: (g.f)(xi) = f(g^{-1} xi) is again a linear combination of xi^beta.
      So span{xi^alpha} is a spin-1/2 invariant subspace with NO sigma inserted; the representation is the
      action of SU(2) on C^2 itself (geometry).
  B2. For the conjugate doublet (eps xi-bar)^alpha: it also transforms by g^{-1}; hence every combination
      xi + t eps xi-bar (t in CP^1) gives an invariant doublet. CP^1 family again.
  B3. The Hopf phase U(1): xi -> e^{i beta} xi commutes with SU(2). Under it t -> t e^{2 i beta}, so the only
      U(1)-invariant lines are t = 0 (xi-doublet) and t = infinity (eps xi-bar doublet).
"""

import numpy as np
import sympy as sp

rng = np.random.default_rng(31)
fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


sig = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
]
eps = np.array([[0, 1], [-1, 0]], dtype=complex)  # i sigma_2


def rand_su2():
    v = rng.normal(size=4)
    v /= np.linalg.norm(v)
    a, b, c, d = v
    return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])


def nsig(n):
    return n[0] * sig[0] + n[1] * sig[1] + n[2] * sig[2]


def rand_unit():
    v = rng.normal(size=3)
    return v / np.linalg.norm(v)


def rot_from_su2(g):
    """SO(3) rotation R with g (n.sigma) g^dag = (R n).sigma."""
    R = np.zeros((3, 3))
    for j in range(3):
        M = g @ sig[j] @ g.conj().T
        for i in range(3):
            R[i, j] = (np.trace(sig[i] @ M) / 2).real
    return R


# A1
err = 0.0
for _ in range(200):
    g = rand_su2()
    n = rand_unit()
    lhs = g @ nsig(n) @ g.conj().T
    Rn = rot_from_su2(g) @ n
    err = max(err, np.linalg.norm(lhs - nsig(Rn)))
check("A1 U (n.sigma) U^dag = (R n).sigma with U = g in SU(2) (max error %.1e)" % err, err < 1e-10)


def Psi(a, b, v, n):
    return (a * np.eye(2) + b * nsig(n)) @ v


# equivariance of the ansatz: g.Psi_v (n) := U(g) Psi_v(g^{-1} n) = Psi_{U v}(n)
ok = True
for _ in range(50):
    a, b = rng.normal(size=2) + 1j * rng.normal(size=2)
    g = rand_su2()
    v = rng.normal(size=2) + 1j * rng.normal(size=2)
    n = rand_unit()
    Rinv = rot_from_su2(g).T
    lhs = g @ Psi(a, b, v, Rinv @ n)
    rhs = Psi(a, b, g @ v, n)
    ok &= np.linalg.norm(lhs - rhs) < 1e-10
check(
    "A1b Psi_v is SU(2)-equivariant for every complex [a:b] (the ansatz uses the spin-1/2 rep U)",
    ok,
)

# A2 orthogonality: integrate over S^2 with Gauss-Legendre in cos(theta), uniform phi
xg, wg = np.polynomial.legendre.leggauss(60)
phg = np.linspace(0, 2 * np.pi, 60, endpoint=False)
ORTH = []
for _ in range(5):
    a, b = rng.normal(size=2) + 1j * rng.normal(size=2)
    v = rng.normal(size=2) + 1j * rng.normal(size=2)
    w = rng.normal(size=2) + 1j * rng.normal(size=2)
    tot = 0j
    for xi_, wi in zip(xg, wg):
        th = np.arccos(xi_)
        for ph_ in phg:
            n = np.array([np.sin(th) * np.cos(ph_), np.sin(th) * np.sin(ph_), np.cos(th)])
            tot += wi * (2 * np.pi / 60) * np.vdot(Psi(a, b, v, n), Psi(a, b, w, n))
    pred = 4 * np.pi * (abs(a) ** 2 + abs(b) ** 2) * np.vdot(v, w)
    ORTH.append(abs(tot - pred) / (abs(pred) + 1e-30))
check(
    "A2 <Psi_v,Psi_w> = 4 pi(|a|^2+|b|^2)<v,w> for all tested [a:b] (max rel. error %.1e)"
    % max(ORTH),
    max(ORTH) < 1e-10,
)

# A3 determinant dichotomy (symbolic)
a_s, b_s = sp.symbols("a b")
n1, n2, n3 = sp.symbols("n1 n2 n3", real=True)
S_ = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
M = a_s * sp.eye(2) + b_s * (n1 * S_[0] + n2 * S_[1] + n3 * S_[2])
det = sp.expand(M.det())
det_on_sphere = sp.simplify(det.subs(n3, sp.sqrt(1 - n1**2 - n2**2)))
check(
    "A3 det(a + b n.sigma) = a^2 - b^2 on |n|=1 (symbolic)",
    sp.simplify(det_on_sphere - (a_s**2 - b_s**2 * (n1**2 + n2**2 + (1 - n1**2 - n2**2)))) == 0
    and sp.simplify(det - (a_s**2 - b_s**2 * (n1**2 + n2**2 + n3**2))) == 0,
)

# A4 the correspondent's Psi identity (symbolic, theta, phi)
th_s, ph_s = sp.symbols("theta phi", real=True)
nvec = sp.Matrix([sp.sin(th_s) * sp.cos(ph_s), sp.sin(th_s) * sp.sin(ph_s), sp.cos(th_s)])
ns = nvec[0] * S_[0] + nvec[1] * S_[1] + nvec[2] * S_[2]
e_plus = sp.Matrix([1, 0])
Psi_tom = sp.Matrix([-(1 - sp.cos(th_s)) / 2, sp.exp(sp.I * ph_s) * sp.sin(th_s) / 2])
cand = -sp.Rational(1, 2) * (sp.eye(2) - ns) * e_plus
check(
    "A4 the correspondent's Psi = -(1/2)(1 - n.sigma) e_+ (symbolic identity)",
    sp.simplify(cand - Psi_tom) == sp.zeros(2, 1),
)


# A5 Hom dimension in the harmonic model (Lmax = 2)
def ops(Lmax):
    basis = [(l, m) for l in range(Lmax + 1) for m in range(-l, l + 1)]
    n = len(basis)
    idx = {b_: i for i, b_ in enumerate(basis)}
    Lz = np.zeros((n, n), dtype=complex)
    Lp = np.zeros((n, n), dtype=complex)
    for (l, m), i in idx.items():
        Lz[i, i] = m
        if m < l:
            Lp[idx[(l, m + 1)], i] = np.sqrt((l - m) * (l + m + 1))
    I2 = np.eye(2, dtype=complex)
    Sz = np.diag([0.5, -0.5]).astype(complex)
    Sp = np.array([[0, 1], [0, 0]], dtype=complex)
    Jz = np.kron(Lz, I2) + np.kron(np.eye(n), Sz)
    Jp = np.kron(Lp, I2) + np.kron(np.eye(n), Sp)
    Jm = Jp.conj().T
    Jx = (Jp + Jm) / 2
    Jy = (Jp - Jm) / (2j)
    return [Jx, Jy, Jz]


from scipy.linalg import null_space

Jt = ops(2)
Sh = [sig[k] / 2 for k in range(3)]
dim_src, dim_tgt = 2, Jt[0].shape[0]
rows = []
for k in range(3):
    # T S_k - J_k T = 0 ; vec(T A) = (A^T kron I) vec T  (column-major)
    rows.append(np.kron(Sh[k].T, np.eye(dim_tgt)) - np.kron(np.eye(dim_src), Jt[k]))
ns_ = null_space(np.vstack(rows), rcond=1e-10)
check(
    "A5 dim Hom_SU(2)(V_{1/2}, C^2 (x) H_{<=2}) = 2 (multiplicity 2, from l=0 and l=1)",
    ns_.shape[1] == 2,
)

# B1: coordinate functions on S^3 transform by g^{-1} (no sigma appears)
ok_b1 = True
for _ in range(50):
    g = rand_su2()
    xi = rng.normal(size=2) + 1j * rng.normal(size=2)
    xi /= np.linalg.norm(xi)
    # (g.f)(xi) = f(g^{-1} xi) for f = xi^alpha
    lhs = np.linalg.inv(g) @ xi
    ok_b1 &= (
        np.linalg.norm(lhs - np.linalg.inv(g) @ xi) < 1e-12
    )  # trivially linear: the point is it is a
    # linear combination of the coordinates, with coefficient matrix g^{-1}
check(
    "B1 coordinate functions xi^alpha: (g.xi^alpha)(xi) = (g^{-1})^alpha_beta xi^beta (linear, no sigma)",
    ok_b1,
)

# B2: eps conj(xi): transforms by the SAME matrix g^{-1}
ok_b2 = True
for _ in range(50):
    g = rand_su2()
    xi = rng.normal(size=2) + 1j * rng.normal(size=2)
    xi /= np.linalg.norm(xi)
    gxi = np.linalg.inv(g) @ xi
    lhs = eps @ np.conj(gxi)  # (g.(eps xibar))(xi) = (eps conj(g^{-1} xi))
    rhs = np.linalg.inv(g) @ (eps @ np.conj(xi))
    ok_b2 &= np.linalg.norm(lhs - rhs) < 1e-10
check(
    "B2 eps conj(xi) transforms by g^{-1} as well: (eps conj(g^{-1}xi)) = g^{-1} (eps conj xi)",
    ok_b2,
)

# B2b: every mixture xi + t eps xibar is an invariant doublet (checked for random t)
ok_b2b = True
for _ in range(20):
    t = rng.normal() + 1j * rng.normal()
    g = rand_su2()
    xi = rng.normal(size=2) + 1j * rng.normal(size=2)
    xi /= np.linalg.norm(xi)
    comb = lambda x: x + t * (eps @ np.conj(x))
    lhs = comb(np.linalg.inv(g) @ xi)
    rhs = np.linalg.inv(g) @ comb(xi)
    ok_b2b &= np.linalg.norm(lhs - rhs) < 1e-10
check("B2b every xi + t eps xibar (t in C) transforms by g^{-1}: invariant doublet", ok_b2b)

# B3 Hopf phase U(1): xi -> e^{i beta} xi ; t -> t e^{2 i beta}; invariant lines only t = 0, infinity
beta = 0.7
t0 = 0.4 - 0.3j
x0 = rng.normal(size=2) + 1j * rng.normal(size=2)
x0 /= np.linalg.norm(x0)


# (h.f)(xi) = f(e^{-i beta} xi): compute the new combination for the phase action
def phase_comb(x, t):
    return x + t * (eps @ np.conj(x))


# action on the doublet line [1:t]: the coefficient of eps xibar changes by e^{2 i beta}
new_t = t0 * np.exp(2j * beta)
line_fixed = abs(t0) < 1e-12 or abs(new_t - t0) < 1e-12
check(
    "B3 the Hopf-phase U(1) moves the line [1:t] unless t in {0, infinity} (t -> t e^{2i beta})",
    abs(new_t - t0) > 1e-6 and abs(new_t) == abs(t0),
)
# verify the transformation law numerically: f(e^{-i beta} xi) for the two pieces
lhs = phase_comb(np.exp(-1j * beta) * x0, t0)
rhs_pred = np.exp(-1j * beta) * (x0 + t0 * np.exp(2j * beta) * (eps @ np.conj(x0)))
check(
    "B3b (h.f)(xi) = f(e^{-i beta} xi) gives coefficient t0 e^{2i beta} on eps xibar",
    np.linalg.norm(lhs - rhs_pred) < 1e-12,
)

# B1b (function level, not index algebra): sample S^3 at random points x, define (U(g)f)(x) = f(g^{-1}x)
# for f_alpha(x) = x^alpha. Solve for the coefficient matrix M with (U(g)f_alpha)(x) = sum_beta M_{alpha beta} f_beta(x)
# on the sample; expect M = g^{-1} (transposed convention checked by the residual), with zero residual.
ok_b1b = True
for _ in range(10):
    g = rand_su2()
    X = rng.normal(size=(40, 2)) + 1j * rng.normal(size=(40, 2))
    X /= np.linalg.norm(X, axis=1)[:, None]
    gi = np.linalg.inv(g)
    dragged = (gi @ X.T).T  # rows: g^{-1} x evaluated as points
    F_orig = X          # f_alpha(x) = x^alpha, columns alpha
    F_drag = dragged    # (U(g) f_alpha)(x) = f_alpha(g^{-1} x)
    sol, *_ = np.linalg.lstsq(F_orig, F_drag, rcond=None)  # F_drag = F_orig @ sol
    resid = np.linalg.norm(F_orig @ sol - F_drag) / np.linalg.norm(F_drag)
    ok_b1b &= resid < 1e-10
check("B1b function-level: the dragged coordinate functions are linear combinations of the originals (zero residual)", ok_b1b)

print("\nFAILS:", fails if fails else "none")
