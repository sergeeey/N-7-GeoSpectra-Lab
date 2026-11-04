"""C237 (Q5): choice of a vacuum point on S^3 = SU(2) under SU(2)_L x SU(2)_R, stabilizer, tangent (Goldstone-type) and normal modes.

Same setup as C236: u = (a,b,c,d) real, g(u) = a I + i (d s1 - c s2 + b s3), T_k = -i s_k/2.
  Vector fields on R^4 (linear): V^L_k(u) = T_k g(u)  (left),  V^R_k(u) = g(u) T_k  (right), coordinates read from the 2x2 matrix.
  The group acts g -> h g k^-1; infinitesimally (alpha, beta) in R^3 x R^3 moves u by sum alpha_k V^L_k - sum beta_k V^R_k.

Predictions written BEFORE running:
  Q5-1. At every sampled point u the six fields span a 3-dimensional space (the tangent space of S^3, orthogonal to u): the action is transitive,
        the stabilizer algebra is 3-dimensional and equals {(alpha, beta): Ad-relation beta = g^-1 alpha g}; at u = (1,0,0,0) it is the diagonal alpha = beta.
  Q5-2. SU(2)_L alone and SU(2)_R alone act freely (rank 3, trivial stabilizer algebra): no left-only or right-only unbroken generator at any point.
  Q5-3. Polynomial invariants of the linear action of SU(2)_L x SU(2)_R on R^4 (= the 4 degree-1 harmonics) have dimension 0,1,0,1 in degrees 1,2,3,4:
        only powers of r^2 = a^2+b^2+c^2+d^2.
  Q5-4. For V = lam (r^2 - v^2)^2, the Hessian at (v,0,0,0) is diag(8 lam v^2, 0, 0, 0): its kernel is exactly the span of the broken-generator directions
        (the tangent space of the orbit), and the one massive direction is the stabilizer singlet 'a' (the fourth harmonic of C236).
  Q5-5. The stabilizer (diagonal SU(2)) acts on the tangent space at (1,0,0,0) as a triplet (Casimir 2) and trivially on the normal direction (Casimir 0).
  Q5-6. The orbit of one point is all of S^3, so the choice of the point is a choice of gauge for SU(2)_L x SU(2)_R: all points have conjugate stabilizers.
Self-controls (must be CAUGHT): stabilizer dimension 2; a cubic invariant; Hessian rank 2; claim L-only stabilizer nonzero.
"""

import sys

import sympy as sp

a, b, c, d = sp.symbols("a b c d", real=True)
U = [a, b, c, d]
lam, v = sp.symbols("lam v", positive=True)
I2 = sp.eye(2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
SIG = [s1, s2, s3]
T = [-sp.I * s / 2 for s in SIG]
R = sp.Rational
FAILS = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def expect_caught(name, cond):
    print(("CAUGHT " if not cond else "MISSED ") + name)
    if cond:
        FAILS.append("self-control not caught: " + name)


def gmat(u):
    return u[0] * I2 + sp.I * (u[3] * s1 - u[2] * s2 + u[1] * s3)


def coords(M):
    return sp.Matrix(
        [
            sp.simplify(M.trace() / 2),
            sp.simplify((M * s3).trace() / (2 * sp.I)),
            sp.simplify(-(M * s2).trace() / (2 * sp.I)),
            sp.simplify((M * s1).trace() / (2 * sp.I)),
        ]
    )


E4 = [sp.Matrix([1 if i == j else 0 for i in range(4)]) for j in range(4)]
AL = [sp.Matrix.hstack(*[coords(T[k] * gmat(E4[j])) for j in range(4)]) for k in range(3)]
AR = [sp.Matrix.hstack(*[coords(gmat(E4[j]) * T[k]) for j in range(4)]) for k in range(3)]
uvec = sp.Matrix(U)


def point(*vals):
    return sp.Matrix(vals)


def motion_matrix(u):
    """4x6: column k = V^L_k(u) (k<3), column 3+k = - V^R_k(u)"""
    cols = [AL[k] * u for k in range(3)] + [-(AR[k] * u) for k in range(3)]
    return sp.Matrix.hstack(*cols)


PTS = {
    "P0 (1,0,0,0)": point(1, 0, 0, 0),
    "P1 (1/2,1/2,1/2,1/2)": point(R(1, 2), R(1, 2), R(1, 2), R(1, 2)),
    "P3 (1/3,2/3,2/3,0)": point(R(1, 3), R(2, 3), R(2, 3), 0),
    "P4 (0,0,0,1)": point(0, 0, 0, 1),
}

# ---- Q5-1, Q5-2, Q5-6
for name, u in PTS.items():
    check(f"{name}: lies on S^3", sp.simplify((u.T * u)[0] - 1) == 0)
    M = motion_matrix(u)
    check(
        f"{name}: all six fields are orthogonal to u (tangent)",
        sp.simplify(u.T * M) == sp.zeros(1, 6),
    )
    check(f"{name}: rank of the six fields = 3 (transitive)", M.rank() == 3)
    ker = M.nullspace()
    check(f"{name}: stabilizer algebra dimension = 3", len(ker) == 3)
    g = gmat(u)
    ok = True
    for kv in ker:
        al = sum((kv[k] * T[k] for k in range(3)), sp.zeros(2))
        be = sum((kv[3 + k] * T[k] for k in range(3)), sp.zeros(2))
        # delta g = al g - g be = 0  <=>  be = g^-1 al g
        ok = (
            ok
            and sp.simplify(al * g - g * be) == sp.zeros(2)
            and sp.simplify(be - g.inv() * al * g) == sp.zeros(2)
        )
    check(
        f"{name}: every stabilizer vector satisfies beta = g^-1 alpha g (Ad-conjugate of diagonal)",
        ok,
    )
    check(f"{name}: SU(2)_L alone acts freely (rank 3)", M[:, :3].rank() == 3)
    check(f"{name}: SU(2)_R alone acts freely (rank 3)", M[:, 3:].rank() == 3)
    if name.startswith("P1"):
        expect_caught("control: claim stabilizer algebra dimension 2 at P1", len(ker) == 2)
        expect_caught(
            "control: claim a nonzero L-only stabilizer vector at P1", len(M[:, :3].nullspace()) > 0
        )

M0 = motion_matrix(PTS["P0 (1,0,0,0)"])
ker0 = M0.nullspace()
check(
    "P0: stabilizer is exactly the diagonal alpha = beta",
    all(sp.simplify(kv[:3, 0] - kv[3:, 0]) == sp.zeros(3, 1) for kv in ker0) and len(ker0) == 3,
)
broken0 = sp.Matrix.hstack(*[AL[k] * PTS["P0 (1,0,0,0)"] for k in range(3)])
check(
    "P0: the three broken (axial) directions span the tangent space (b,c,d)",
    broken0.rank() == 3 and sp.simplify(broken0[0, :]) == sp.zeros(1, 3),
)


# ---- Q5-3: polynomial invariants
def monomials(n):
    out = []
    for i in range(n + 1):
        for j in range(n + 1 - i):
            for k in range(n + 1 - i - j):
                out.append(a**i * b**j * c**k * d ** (n - i - j - k))
    return out


def vec(f, mons):
    P = sp.Poly(f, *U)
    return sp.Matrix([P.coeff_monomial(m) for m in mons])


def op_lin(A, f, sign):
    w = A * uvec
    return sp.expand(sign * sum(w[i] * sp.diff(f, U[i]) for i in range(4)))


def inv_dim(n):
    mons = monomials(n)
    mats = []
    for k in range(3):
        mats.append(sp.Matrix.hstack(*[vec(op_lin(AL[k], m, -1), mons) for m in mons]))
        mats.append(sp.Matrix.hstack(*[vec(op_lin(AR[k], m, +1), mons) for m in mons]))
    return len(sp.Matrix.vstack(*mats).nullspace())


dims = [inv_dim(n) for n in range(1, 5)]
check(
    f"Q5-3: invariant polynomials of degree 1..4 have dimensions {dims} = [0, 1, 0, 1]",
    dims == [0, 1, 0, 1],
)
expect_caught("control: claim a cubic invariant exists", dims[2] == 1)

# ---- Q5-4: Hessian
r2 = a**2 + b**2 + c**2 + d**2
V = lam * (r2 - v**2) ** 2
Hs = sp.hessian(V, U).subs({a: v, b: 0, c: 0, d: 0})
Hs = sp.simplify(Hs)
check(
    "Q5-4: Hessian at (v,0,0,0) = diag(8 lam v^2, 0, 0, 0)", Hs == sp.diag(8 * lam * v**2, 0, 0, 0)
)
check("Q5-4: Hessian rank 1 (three zero modes)", Hs.rank() == 1)
expect_caught("control: Hessian rank 2", Hs.rank() == 2)
kerH = Hs.nullspace()
KH = sp.Matrix.hstack(*kerH)
# kernel of Hessian == column space of the broken directions at P0 (as subspaces of R^4)
same = sp.Matrix.hstack(KH, broken0).rank() == 3 and KH.rank() == 3 and broken0.rank() == 3
check("Q5-4: kernel of the Hessian equals the span of the broken-generator directions at P0", same)
check(
    "Q5-4: the massive direction is the stabilizer singlet 'a' of C236",
    sp.simplify(Hs[0, 0]) != 0 and all(Hs[0, j] == 0 for j in range(1, 4)),
)

# ---- Q5-5: stabilizer action on tangent vs normal at P0
Dst = [AL[k] - AR[k] for k in range(3)]
for k in range(3):
    pass
cas = sp.simplify(-(Dst[0] ** 2 + Dst[1] ** 2 + Dst[2] ** 2))
check(
    "Q5-5: stabilizer generators close as su(2) on R^4",
    sp.simplify(Dst[0] * Dst[1] - Dst[1] * Dst[0] - Dst[2]) == sp.zeros(4)
    or sp.simplify(Dst[0] * Dst[1] - Dst[1] * Dst[0] + Dst[2]) == sp.zeros(4),
)
check(
    "Q5-5: Casimir on R^4 has eigenvalues {0 once, 2 three times} (tangent triplet + normal singlet)",
    cas.eigenvals() == {0: 1, 2: 3} or cas.eigenvals() == {0: 1, R(1, 2) * 4: 3},
)
tang = cas[1:, 1:]
norm = cas[0, 0]
check(
    "Q5-5: normal direction (a): Casimir 0",
    sp.simplify(norm) == 0 and sp.simplify(cas[0, 1:]) == sp.zeros(1, 3),
)
check(
    "Q5-5: tangent block (b,c,d): Casimir matrix = 2 * identity (triplet)",
    sp.simplify(tang - 2 * sp.eye(3)) == sp.zeros(3),
)

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
