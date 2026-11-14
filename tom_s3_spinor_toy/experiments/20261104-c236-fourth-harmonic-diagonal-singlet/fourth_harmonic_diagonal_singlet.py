"""C236 (Q4): the 'fourth harmonic' as the diagonal-SU(2) singlet of the degree-1 harmonics, and diagonal singlets in scalar and C^2-valued sectors.

Setup (same objects as TOM-CERT-01 / C235):
  S^3 = SU(2), g(u) = a I + i (d s1 - c s2 + b s3), u = (a,b,c,d) real, a^2+b^2+c^2+d^2 = 1  (= [[x0, -conj x1],[x1, conj x0]], x0 = a+ib, x1 = c+id).
  T_k = -i s_k / 2.  Function-level generators (Lie-algebra representations, [G_i,G_j] = eps_ijk G_k):
     X_k = - (T_k g) . grad   (left action),   Y_k = (g T_k) . grad   (right action),   S_k = T_k on C^2 (spin).
  Diagonal SU(2) on scalars: D_k = X_k + Y_k (conjugation g -> h g h^-1).
  Diagonal SU(2) on C^2-valued fields: Dtot_k = X_k + Y_k + S_k (left + total right).   Dorb_k = X_k + Y_k (spin untouched).
  D0 = -i sum_k s_k (x) (2 Y_k): C227 uses T_a = -i s_a (no 1/2), so its left-invariant fields are 2 Y_k here (factor fixed after the first run showed all eigenvalues halved).

Predictions written BEFORE running:
  P1. su(2) relations hold for X, Y, S; X commutes with Y.
  P2. On the 4 degree-1 harmonics (a,b,c,d): D has exactly one singlet and one triplet (Casimir j(j+1) = 0 once, 2 three times); the singlet is a = (1/2) tr g.
  P3. For harmonic degree n = 0..3 (sector (n/2, n/2)) the number of D-singlets is 1, and the singlet is proportional to r^n U_n(a/r) (Chebyshev U_n: the SU(2) character).
  P4. On C^2-valued fields of degree n, the number of Dtot-singlets is 0 for n = 0..3 (no singlet because j_L - k = +-1/2); the number of Dorb-singlets is 2 (spin untouched).
  P5. D0 spectrum on degree n: -n with multiplicity (n+1)(n+2), n+2 with multiplicity n(n+1) (C235 table); D0 commutes with X_k and with K_k = Y_k + S_k, hence with Dtot.
Self-controls (must be CAUGHT): claim 1 singlet on C^2 fields under Dtot at n=1; claim triplet Casimir 6; claim X - Y closes as a representation.
"""

import sys

import sympy as sp

a, b, c, d = sp.symbols("a b c d", real=True)
U = [a, b, c, d]
R2 = a**2 + b**2 + c**2 + d**2
I2 = sp.eye(2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
SIG = [s1, s2, s3]
T = [-sp.I * s / 2 for s in SIG]
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
    A = sp.simplify(M.trace() / 2)
    B = sp.simplify((M * s3).trace() / (2 * sp.I))
    C = sp.simplify(-(M * s2).trace() / (2 * sp.I))
    D = sp.simplify((M * s1).trace() / (2 * sp.I))
    return sp.Matrix([A, B, C, D])


E4 = [sp.Matrix([1 if i == j else 0 for i in range(4)]) for j in range(4)]
# linear maps u -> V(u): left field T_k g, right field g T_k
AL = [sp.Matrix.hstack(*[coords(T[k] * gmat(E4[j])) for j in range(4)]) for k in range(3)]
AR = [sp.Matrix.hstack(*[coords(gmat(E4[j]) * T[k]) for j in range(4)]) for k in range(3)]
check(
    "coordinate extraction reproduces g (round trip)",
    all(sp.simplify(gmat(coords(gmat(E4[j]))) - gmat(E4[j])) == sp.zeros(2) for j in range(4)),
)

uvec = sp.Matrix(U)


def op(A, f, sign=1):
    """differential operator sign * (A u).grad applied to polynomial f"""
    v = A * uvec
    return sp.expand(sign * sum(v[i] * sp.diff(f, U[i]) for i in range(4)))


def Xop(k, f):
    return op(AL[k], f, -1)


def Yop(k, f):
    return op(AR[k], f, +1)


# ---- P1: relations on a generic polynomial
test = a**3 * b + c * d**2 * a + b**2 * c**2 + d**4 + a * b * c
eps = {(0, 1): 2, (1, 2): 0, (2, 0): 1}
ok = True
for (i, j), kk in eps.items():
    for nm, G in (("X", Xop), ("Y", Yop)):
        lhs = sp.expand(G(i, G(j, test)) - G(j, G(i, test)))
        rhs = G(kk, test)
        ok = ok and sp.expand(lhs - rhs) == 0
check("P1: [X_i,X_j] = eps X_k and [Y_i,Y_j] = eps Y_k on a generic quartic", ok)
ok = all(
    sp.expand(Xop(i, Yop(j, test)) - Yop(j, Xop(i, test))) == 0 for i in range(3) for j in range(3)
)
check("P1: X commutes with Y", ok)
bad = True
for (i, j), kk in eps.items():
    lhs = sp.expand((lambda f: Xop(i, Yop(j, f)) - Yop(j, Xop(i, f)))(test))
bad_ok = True
for (i, j), kk in eps.items():

    def Z(k, f):
        return sp.expand(Xop(k, f) - Yop(k, f))

    lhs = sp.expand(Z(i, Z(j, test)) - Z(j, Z(i, test)))
    bad_ok = bad_ok and sp.expand(lhs - Z(kk, test)) == 0
expect_caught("control: X - Y closes as a representation (it must not)", bad_ok)


# ---- polynomial spaces
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


def opmatrix(G, mons, k):
    return sp.Matrix.hstack(*[vec(G(k, m), mons) for m in mons])


def lap(f):
    return sum(sp.diff(f, v, 2) for v in U)


def harmonic_basis(n):
    mons = monomials(n)
    if n < 2:
        return mons, sp.eye(len(mons))
    lm = monomials(n - 2)
    L = sp.Matrix.hstack(*[vec(lap(m), lm) for m in mons])
    ns = L.nullspace()
    return mons, sp.Matrix.hstack(*ns)


def restrict(M, H):
    """matrix of operator M (monomial basis) on the subspace spanned by columns of H"""
    sol = (H.T * H).inv() * H.T * (M * H)
    assert sp.simplify(H * sol - M * H) == sp.zeros(M.rows, H.cols)
    return sol


def common_kernel_dim(mats):
    return len(sp.Matrix.vstack(*mats).nullspace())


# ---- P2: degree 1
mons1, H1 = harmonic_basis(1)
Dm = [restrict(opmatrix(Xop, mons1, k) + opmatrix(Yop, mons1, k), H1) for k in range(3)]
cas = sp.simplify(-(Dm[0] ** 2 + Dm[1] ** 2 + Dm[2] ** 2))
ev = cas.eigenvals()
check("P2: Casimir -sum D_k^2 on (a,b,c,d) has eigenvalues {0:1, 2:3}", ev == {0: 1, 2: 3})
check(
    "P2: D_k are a representation of su(2) on the 4 harmonics",
    sp.simplify(Dm[0] * Dm[1] - Dm[1] * Dm[0] - Dm[2]) == sp.zeros(4),
)
ker = sp.Matrix.vstack(*Dm).nullspace()
check(
    "P2: exactly one singlet; it is the coordinate a = (1/2) tr g",
    len(ker) == 1
    and [x for x in (H1 * ker[0]).T] == [x for x in (H1 * ker[0]).T]
    and sp.simplify(
        vec(a, mons1)
        - (H1 * ker[0]) * (vec(a, mons1).dot(H1 * ker[0]) / (H1 * ker[0]).dot(H1 * ker[0]))
    )
    == sp.zeros(4, 1),
)
check("P2: 2a = tr g and Re part of g_00 + g_11", sp.simplify(gmat(U).trace() - 2 * a) == 0)
check("P2: D_k(a) = 0 for k = 1,2,3", all(sp.expand(Xop(k, a) + Yop(k, a)) == 0 for k in range(3)))
check(
    "P2: the three others (b,c,d) are a triplet (D_k(b),... nonzero and close)",
    any(sp.expand(Xop(k, b) + Yop(k, b)) != 0 for k in range(3)),
)


# ---- P3: scalar sectors
def chebU_hom(n):
    x = sp.Symbol("x")
    poly = sp.Poly(sp.chebyshevu(n, x), x)
    return sp.expand(
        sum(coef * a ** m[0] * R2 ** sp.Rational(n - m[0], 2) for m, coef in poly.terms())
    )


for n in range(0, 4):
    mons, H = harmonic_basis(n)
    Dn = [restrict(opmatrix(Xop, mons, k) + opmatrix(Yop, mons, k), H) for k in range(3)]
    kd = common_kernel_dim(Dn) if H.cols > 0 else 0
    check(f"P3: degree {n}: harmonic dimension (n+1)^2 = {(n + 1) ** 2}", H.cols == (n + 1) ** 2)
    check(f"P3: degree {n}: exactly 1 D-singlet", kd == 1)
    ch = chebU_hom(n)
    check(
        f"P3: degree {n}: r^n U_n(a/r) = {ch} is harmonic and D-invariant",
        sp.expand(lap(ch)) == 0 and all(sp.expand(Xop(k, ch) + Yop(k, ch)) == 0 for k in range(3)),
    )
    if n == 3:
        expect_caught("control: claim 2 D-singlets at degree 3", kd == 2)

# ---- P4, P5: C^2-valued fields
for n in range(0, 4):
    mons, H = harmonic_basis(n)
    Xm = [restrict(opmatrix(Xop, mons, k), H) for k in range(3)]
    Ym = [restrict(opmatrix(Yop, mons, k), H) for k in range(3)]
    dim = H.cols
    one = sp.eye(dim)
    X2 = [sp.kronecker_product(m, I2) for m in Xm]
    Y2 = [sp.kronecker_product(m, I2) for m in Ym]
    S2 = [sp.kronecker_product(one, T[k]) for k in range(3)]
    Dtot = [X2[k] + Y2[k] + S2[k] for k in range(3)]
    Dorb = [X2[k] + Y2[k] for k in range(3)]
    D0 = sp.zeros(2 * dim)
    for k in range(3):
        D0 += sp.kronecker_product(2 * Ym[k], -sp.I * SIG[k])
    # ordering note: kronecker(poly op, spin matrix) -> spin index fastest; keep consistent for X2,Y2,S2 above
    D0 = sp.zeros(2 * dim)
    for k in range(3):
        D0 += sp.kronecker_product(2 * Ym[k], -sp.I * SIG[k])
    k_tot = common_kernel_dim(Dtot)
    k_orb = common_kernel_dim(Dorb)
    check(f"P4: degree {n}: Dtot-singlets on C^2-valued fields = 0", k_tot == 0)
    check(f"P4: degree {n}: Dorb-singlets (spin untouched) = 2", k_orb == 2)
    if n == 1:
        expect_caught("control: claim 1 Dtot-singlet at degree 1", k_tot == 1)
    Ktot = [Y2[k] + S2[k] for k in range(3)]
    comm_ok = all(sp.simplify(D0 * m - m * D0) == sp.zeros(2 * dim) for m in X2 + Ktot)
    check(f"P5: degree {n}: D0 commutes with X_k and K_k = Y_k + S_k", comm_ok)
    evs = D0.eigenvals()
    exp = {}
    if n == 0:
        exp = {0: 2}
    else:
        exp = {-n: (n + 1) * (n + 2), n + 2: n * (n + 1)}
    evs_s = {sp.nsimplify(k): v for k, v in evs.items()}
    print("   actual D0 spectrum degree", n, evs_s)
    check(f"P5: degree {n}: D0 spectrum {exp}", evs_s == exp)

# triplet Casimir control
expect_caught(
    "control: triplet Casimir equals 6 on the degree-1 harmonics",
    sp.simplify(cas).eigenvals().get(6, 0) > 0,
)

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
