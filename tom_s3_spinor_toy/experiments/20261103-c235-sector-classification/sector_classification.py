"""C235 (Q2): classification of the harmonic and spinor sectors of S^3 = SU(2) by SU(2)_L x SU(2)_R, exact.

Conventions are those of C227 (`weight_sectors_d0_check.py`): functions on S^3 are polynomials in x0..x3 modulo |x|^2 = 1, with
g = x0 A0 + x1 A1 + x2 A2 + x3 A3 (quaternion units, A1 = i sigma1, A2 = -i sigma2, A3 = i sigma3), C = -1,
X_a f = d/dt f(g e^{t C i sigma_a}) (left-invariant fields, the right action), D0 = -i sum_a sigma_a X_a on C^2-valued functions,
J_a = X_a + T_a with T_a = -i sigma_a (the spin index rotates with the right action), and the NEW left generators
Y_a f = d/dt f(e^{t C i sigma_a} g) (act on the argument only). With generators normalised as G_a = -i sigma_a ([G_a,G_b] = 2 eps G_c),
a representation of spin j has  sum_a (generator_a)^2 = -4 j (j+1).  The scalar part is the same machinery without the spin index.

Predictions written BEFORE running (Peter-Weyl; s = d/2 for harmonic degree d):
  P1 (scalars, degree <= 3): sectors (j_L, j_R) = (s, s) with dimension (2s+1)^2 = 1, 4, 9, 16.
  P2 (C^2-valued, degree <= 3): sectors (j_L, k) = (s, s + 1/2) with dimension (2s+1)(2s+2) and D0 = -2s;
      (s, s - 1/2) with dimension (2s+1)(2s) (s >= 1/2) and D0 = 2s + 2.   Total 2 + 8 + 18 + 32 = 60.
  P3 (commutation): [Y_a, X_b] = 0, [Y_a, J_b] = 0, [D0, Y_a] = 0, [D0, J_a] = 0.  So D0 commutes with SU(2)_L and with the total
      right SU(2), which is why a Dirac-type operator on S^3 acts within a fixed (j_L, k).
  P4 (labelling): scalar sectors have j_L - j_R = 0; spinor sectors have j_L - k = -+1/2 (half-integer); the (1/2,1/2) multiplet of
      TOM-CERT-01 is the d = 1 scalar sector.
  P5 (other trivialisation): with the right-invariant frame D0' = -i sum sigma_a Y_a the roles of L and R are mirrored:
      sectors (j_L, j_R) = (k, s) with the same dimensions, and D0' = -D0 on them (inversion maps X_a to -Y_a).
Self-controls: a wrong prediction (the (s, s) scalar sector with dimension (2s+1)(2s+2)) must be caught; the left Casimir computed
with the spin index added (J_L = Y + T) must NOT give the same sector table.
Exit 0 only if every asserted claim holds and every self-control is caught.
"""

import itertools
import sys

import sympy as sp

N = 3
x = sp.symbols("x0:4", real=True)
I = sp.I
A = [
    sp.eye(2),
    sp.Matrix([[0, I], [I, 0]]),
    sp.Matrix([[0, -1], [1, 0]]),
    sp.Matrix([[I, 0], [0, -I]]),
]
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
g = x[0] * A[0] + x[1] * A[1] + x[2] * A[2] + x[3] * A[3]
C = -1
REL = x[3] ** 2 + x[0] ** 2 + x[1] ** 2 + x[2] ** 2 - 1
FAILS = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def expect_caught(name, cond):
    print(("CAUGHT " if not cond else "MISSED ") + name)
    if cond:
        FAILS.append("self-control not caught: " + name)


def red(f):
    f = sp.expand(f)
    if f == 0:
        return sp.Integer(0)
    return sp.expand(sp.reduced(f, [REL], x[3], x[0], x[1], x[2], order="lex")[1])


def field_X(a, f):
    M = g * (C * I * sig[a])
    m = [sp.expand((M * A[j].H).trace() / 2) for j in range(4)]
    return red(sum(m[j] * sp.diff(f, x[j]) for j in range(4)))


def field_Y(a, f):
    M = (C * I * sig[a]) * g
    m = [sp.expand((M * A[j].H).trace() / 2) for j in range(4)]
    return red(sum(m[j] * sp.diff(f, x[j]) for j in range(4)))


MONOS = [e for e in itertools.product(range(N + 1), repeat=4) if sum(e) <= N and e[3] <= 1]
MIDX = {e: i for i, e in enumerate(MONOS)}
nm = len(MONOS)


def mono(e):
    return sp.Mul(*[x[i] ** e[i] for i in range(4)])


def scalar_matrix(op):
    """matrix of a scalar field operator on the monomial basis (columns = images of basis elements)"""
    M = sp.zeros(nm, nm)
    for j, e in enumerate(MONOS):
        img = op(mono(e))
        if img == 0:
            continue
        for mon, c in sp.Poly(img, *x).terms():
            if mon[3] > 1 or sum(mon) > N:
                raise ValueError("operator left the truncated basis")
            M[MIDX[mon], j] = c
    return M


def tensor_spin(Mscal, S):
    """C^2-valued: kron(spin matrix S, scalar matrix); the vector index is the outer one"""
    n = nm
    out = sp.zeros(2 * n, 2 * n)
    for p in range(2):
        for q in range(2):
            if S[p, q] != 0:
                out[p * n : (p + 1) * n, q * n : (q + 1) * n] = S[p, q] * Mscal
    return out


def kron_id(Mscal):
    return tensor_spin(Mscal, sp.eye(2))


XS = [scalar_matrix(lambda f, a=a: field_X(a, f)) for a in range(3)]
YS = [scalar_matrix(lambda f, a=a: field_Y(a, f)) for a in range(3)]
T = [C * I * s for s in sig]  # T_a = -i sigma_a with C = -1: C*I*sigma = -i sigma


# check the field algebra and commutation
def comm(P, Q):
    return P * Q - Q * P


def zero(M):
    return all(sp.simplify(e) == 0 for e in M)


eps = lambda a, b, c: sp.LeviCivita(a, b, c)  # noqa: E731
sx = {1: 1, -1: -1}
# sign of the algebra: [X_a,X_b] = s 2 eps X_c
sgnX = None
for s in (1, -1):
    if all(
        zero(
            comm(XS[a], XS[b]) - s * 2 * sum((eps(a, b, c) * XS[c] for c in range(3)), sp.zeros(nm))
        )
        for a in range(3)
        for b in range(3)
    ):
        sgnX = s
check("[X_a, X_b] = +-2 eps_abc X_c (sign %s)" % sgnX, sgnX is not None)
sgnY = None
for s in (1, -1):
    if all(
        zero(
            comm(YS[a], YS[b]) - s * 2 * sum((eps(a, b, c) * YS[c] for c in range(3)), sp.zeros(nm))
        )
        for a in range(3)
        for b in range(3)
    ):
        sgnY = s
check("[Y_a, Y_b] = +-2 eps_abc Y_c (sign %s)" % sgnY, sgnY is not None)
check(
    "P3: [Y_a, X_b] = 0 on scalar polynomials (left and right actions commute)",
    all(zero(comm(YS[a], XS[b])) for a in range(3) for b in range(3)),
)


# Casimirs
def casimir(gens):
    return sum((m * m for m in gens), sp.zeros(gens[0].shape[0]))


CAS_L_s = casimir(YS)
CAS_R_s = casimir(XS)
# C^2-valued operators
XV = [kron_id(m) for m in XS]
YV = [kron_id(m) for m in YS]
TV = [tensor_spin(sp.eye(nm), T[a]) for a in range(3)]
JV = [XV[a] + TV[a] for a in range(3)]
CAS_L_v = casimir(YV)
CAS_R_v = casimir(JV)
sigma_a_V = [tensor_spin(sp.eye(nm), sig[a]) for a in range(3)]
D0 = sum((-I * sigma_a_V[a] * XV[a] for a in range(3)), sp.zeros(2 * nm))


def cas(j):
    return -4 * j * (j + 1)


def nullity(M):
    return M.shape[1] - M.rank()


def sector_dim(CL, CR, jl, jr, extra=None):
    rows = [CL - cas(jl) * sp.eye(CL.shape[0]), CR - cas(jr) * sp.eye(CR.shape[0])]
    if extra is not None:
        rows.append(extra)
    stacked = sp.Matrix.vstack(*rows)
    return nullity(stacked)


half = sp.Rational(1, 2)
# P1 scalar sectors
tot = 0
okP1 = True
for d in range(N + 1):
    s = sp.Rational(d, 2)
    dim = sector_dim(CAS_L_s, CAS_R_s, s, s)
    okP1 &= dim == (2 * s + 1) ** 2
    tot += dim
check(
    f"P1: scalar sectors (s,s), s = 0..{sp.Rational(N, 2)}: dimensions (2s+1)^2, total {tot} = {sum((d + 1) ** 2 for d in range(N + 1))}",
    okP1 and tot == sum((d + 1) ** 2 for d in range(N + 1)),
)

# P3 commutation on C^2-valued fields
check(
    "P3: [Y_a, J_b] = 0 and [Y_a, X_b] = 0 on C^2-valued fields",
    all(zero(comm(YV[a], JV[b])) for a in range(3) for b in range(3)),
)
check(
    "P3: [D0, Y_a] = 0 and [D0, J_a] = 0",
    all(zero(comm(D0, YV[a])) for a in range(3)) and all(zero(comm(D0, JV[a])) for a in range(3)),
)
check(
    "J_a satisfy the same algebra as G_a (so J = X + T is the total right generator)",
    any(
        all(
            zero(
                comm(JV[a], JV[b])
                - s * 2 * sum((eps(a, b, c) * JV[c] for c in range(3)), sp.zeros(2 * nm))
            )
            for a in range(3)
            for b in range(3)
        )
        for s in (1, -1)
    ),
)

# P2 spinor sectors with D0 eigenvalues
tot = 0
okP2 = True
table = []
for d in range(N + 1):
    s = sp.Rational(d, 2)
    for k, dim_expect, d0 in (
        (s + half, (2 * s + 1) * (2 * s + 2), -2 * s),
        (s - half, (2 * s + 1) * (2 * s), 2 * s + 2),
    ):
        if k < 0:
            continue
        dim = sector_dim(CAS_L_v, CAS_R_v, s, k)
        dim_d0 = sector_dim(CAS_L_v, CAS_R_v, s, k, extra=D0 - d0 * sp.eye(2 * nm))
        okP2 &= dim == dim_expect and dim_d0 == dim
        tot += dim
        table.append((s, k, dim, d0))
print("  spinor sectors (j_L, k, dim, D0):", [(str(a), str(b), c, str(e)) for a, b, c, e in table])
check(
    f"P2: spinor sectors (s, s+1/2) and (s, s-1/2) have dimensions (2s+1)(2s+2), (2s+1)(2s) and D0 = -2s, 2s+2 exactly; total {tot} = {2 * sum((d + 1) ** 2 for d in range(N + 1))}",
    okP2 and tot == 2 * sum((d + 1) ** 2 for d in range(N + 1)),
)

# P4 labelling
check(
    "P4: scalar sectors have j_L - j_R = 0; spinor sectors have j_L - k = -+1/2 for every sector listed",
    all(abs(a - b) == half for a, b, _, _ in table),
)
check(
    "P4: the d = 1 scalar sector is (1/2,1/2) of dimension 4 (the multiplet of TOM-CERT-01)",
    sector_dim(CAS_L_s, CAS_R_s, half, half) == 4,
)

# P5: the other trivialisation (right-invariant frame) swaps the roles of L and R
D0p = sum((-I * sigma_a_V[a] * YV[a] for a in range(3)), sp.zeros(2 * nm))
found = None
for sgn in (1, -1):
    Jp = [YV[a] + sgn * TV[a] for a in range(3)]
    if all(zero(comm(D0p, Jp[a])) for a in range(3)) and all(zero(comm(D0p, XV[a])) for a in range(3)):
        found = sgn
check("P5: with the right-invariant frame D0' = -i sum sigma_a Y_a commutes with the right action X and with J'_L = Y + s T for s = %s" % found, found is not None)
CAS_Lp = casimir([YV[a] + (found or 1) * TV[a] for a in range(3)])
mirrored = all(sector_dim(CAS_Lp, casimir(XV), k, s_) == dim for s_, k, dim, _ in table)
check("P5: in that trivialisation the sector table is mirrored: (j_L, j_R) = (k, s) with the same dimensions", mirrored)
check("P5: D0' = -iota D0 iota (inversion g -> g^-1 maps X_a to -Y_a), so on the mirrored sector (j_L=k, j_R=s) D0' equals MINUS the D0 value of the original sector", all(sector_dim(CAS_Lp, casimir(XV), k, s_, extra=D0p + d0 * sp.eye(2 * nm)) == dim for s_, k, dim, d0 in table))

# self-controls
expect_caught(
    "scalar sector (1/2,1/2) has dimension (2s+1)(2s+2) = 6 instead of 4",
    sector_dim(CAS_L_s, CAS_R_s, half, half) == 6,
)
YT = [YV[a] + TV[a] for a in range(3)]
CAS_LT = casimir(YT)
same = all(sector_dim(CAS_LT, CAS_R_v, s, k) == dim for s, k, dim, _ in table)
expect_caught(
    "left generators with the spin index added (Y + T) reproduce the same (j_L, k) table", same
)
expect_caught(
    "the D0 eigenvalue +2 on the sector (1/2, 0) (wrong value; true value is 3)",
    sector_dim(CAS_L_v, CAS_R_v, half, 0, extra=D0 - 2 * sp.eye(2 * nm)) == 2,
)

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
