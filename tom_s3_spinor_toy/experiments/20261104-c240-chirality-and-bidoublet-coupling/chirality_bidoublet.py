"""C240 (Q6): chirality of D0 and the coupling of the SO(4)-spinor sectors (0,1/2) and (1/2,0) through the degree-1 harmonics (1/2,1/2).

Setup identical to C236 (u = (a,b,c,d), g(u), X_k left, Y_k right, S_k = T_k spin, D0 = -i sum sigma_k (x) (2 Y_k), spin index fastest in kron).
Sectors (j_L, k): j_L from the Casimir of X, k from the Casimir of K = Y + S. Functions of degree <= 1 only (all harmonic): 2 + 8 = 10 states.

Predictions written BEFORE running:
  R1. On C^2 the only matrices commuting with all sigma_k are the scalars: there is no chirality (gamma5-like) operator on spin-1/2 fields of S^3 itself (odd dimension). So 'left/right-handed' on the poster is the SO(4)-spinor label of a sector, not a property of D0 or of C^2.
  R2. Degree 0 (x) C^2 is the sector (0,1/2) with D0 = 0; degree 1 (x) C^2 splits into (1/2,0) [2 states, D0 = 3] and (1/2,1) [6 states, D0 = -1].
  R3. D0 commutes with X_k and K_k, so it is block-diagonal in (j_L,k): it cannot connect (0,1/2) with (1/2,0).
  R4. Multiplication by the four degree-1 harmonics (the (1/2,1/2) multiplet) maps (0,1/2) isomorphically (rank 8) onto degree 1 (x) C^2 = (1/2,0) + (1/2,1), and its (1/2,0) component is nonzero: (0,1/2) (x) (1/2,1/2) contains (1/2,0). This is the representation-theory pattern of a left-right bidoublet coupling a doublet of one SU(2) to a doublet of the other (the left-right Higgs bidoublet pattern [MEMORY, source not opened here]); an analogy, NOT an identification with Tom's Higgs.
Self-controls (must be CAUGHT): claim a nontrivial chirality operator on C^2; claim D0 connects (0,1/2) and (1/2,0); claim the multiplication map has rank 7.
"""

import sys

import sympy as sp

a, b, c, d = sp.symbols("a b c d", real=True)
U = [a, b, c, d]
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
uv = sp.Matrix(U)


def Xop(k, f):
    w = AL[k] * uv
    return sp.expand(-sum(w[i] * sp.diff(f, U[i]) for i in range(4)))


def Yop(k, f):
    w = AR[k] * uv
    return sp.expand(sum(w[i] * sp.diff(f, U[i]) for i in range(4)))


# ---- R1: commutant of the spin generators on C^2
unk = sp.symbols("m0:4")
Mgen = sp.Matrix([[unk[0], unk[1]], [unk[2], unk[3]]])
eqs = []
for sg in SIG:
    cm = Mgen * sg - sg * Mgen
    eqs += list(cm)
sol = sp.solve(eqs, unk, dict=True)[0]
free = [u_ for u_ in unk if u_ not in sol]
check(
    "R1: matrices commuting with sigma_1, sigma_2, sigma_3 form a 1-dimensional space (scalars): no chirality operator on C^2",
    len(free) == 1,
)
expect_caught(
    "R1 control: a 2-dimensional commutant (a nontrivial chirality operator exists)", len(free) == 2
)

# ---- spaces: degree 0 (1 function) and degree 1 (4 functions), each (x) C^2
f0 = [sp.Integer(1)]
f1 = [a, b, c, d]


def vec(f, mons):
    return sp.Matrix([sp.Poly(f, *U).coeff_monomial(m) if f != 0 else 0 for m in mons])


def op_matrix(G, k, mons):
    return sp.Matrix.hstack(*[vec(G(k, m), mons) for m in mons])


# full space: degree-0 block (1) then degree-1 block (4); operators are block diagonal (degree preserved)
mons0, mons1 = [sp.Integer(1)], [a, b, c, d]


def block_op(G, k):
    m0 = sp.zeros(1)
    m1 = op_matrix(G, k, mons1)
    return sp.diag(m0, m1)


Xm = [block_op(Xop, k) for k in range(3)]
Ym = [block_op(Yop, k) for k in range(3)]
one5 = sp.eye(5)
X2 = [sp.kronecker_product(Xm[k], I2) for k in range(3)]
Y2 = [sp.kronecker_product(Ym[k], I2) for k in range(3)]
S2 = [sp.kronecker_product(one5, T[k]) for k in range(3)]
K2 = [Y2[k] + S2[k] for k in range(3)]
D0 = sp.zeros(10)
for k in range(3):
    D0 += sp.kronecker_product(2 * Ym[k], -sp.I * SIG[k])
casL = -sum((m * m for m in X2), sp.zeros(10))
casK = -sum((m * m for m in K2), sp.zeros(10))
check(
    "R3: D0 commutes with X_k and K_k (block-diagonal in (j_L,k))",
    all(sp.simplify(D0 * m - m * D0) == sp.zeros(10) for m in X2 + K2),
)

# joint diagonalisation: eigenspaces of casL + 7 casK (distinct values separate (jL,k))
tot = casL + sp.Rational(7, 1) * casK
evs = tot.eigenvects()
sector = {}
for val, mult, vs in evs:
    jl_c = sp.simplify((vs[0].T * casL * vs[0])[0] / (vs[0].T * vs[0])[0]) if False else None
    sector[val] = (mult, vs)
rows = []
for val, (mult, vs) in sector.items():
    v = vs[0]
    cl = sp.simplify((v.H * casL * v)[0] / (v.H * v)[0])
    ck = sp.simplify((v.H * casK * v)[0] / (v.H * v)[0])
    d0 = sp.simplify((v.H * D0 * v)[0] / (v.H * v)[0])
    rows.append((cl, ck, mult, d0))
print("   (casL, casK, dim, D0):", rows)
jl_k = {(sp.sqrt(1 + 4 * cl) - 1) / 2: None for cl, ck, m, d0 in rows}
table = sorted(
    [
        (
            sp.simplify((sp.sqrt(1 + 4 * cl) - 1) / 2),
            sp.simplify((sp.sqrt(1 + 4 * ck) - 1) / 2),
            m,
            d0,
        )
        for cl, ck, m, d0 in rows
    ],
    key=lambda t: (t[0], t[1]),
)
print("   sectors (j_L, k, dim, D0):", table)
expected = sorted(
    [(0, sp.Rational(1, 2), 2, 0), (sp.Rational(1, 2), 0, 2, 3), (sp.Rational(1, 2), 1, 6, -1)],
    key=lambda t: (t[0], t[1]),
)
check(
    "R2: degrees 0..1 give sectors (0,1/2)[2, D0=0], (1/2,0)[2, D0=3], (1/2,1)[6, D0=-1]",
    table == expected,
)


# basis of sector (1/2,0) and (0,1/2)
def sector_basis(jl, k):
    for val, (mult, vs) in sector.items():
        v = vs[0]
        cl = sp.simplify((v.H * casL * v)[0] / (v.H * v)[0])
        ck = sp.simplify((v.H * casK * v)[0] / (v.H * v)[0])
        if (
            sp.simplify((sp.sqrt(1 + 4 * cl) - 1) / 2 - jl) == 0
            and sp.simplify((sp.sqrt(1 + 4 * ck) - 1) / 2 - k) == 0
        ):
            return sp.Matrix.hstack(*vs)
    raise RuntimeError("sector not found")


B0 = sector_basis(0, sp.Rational(1, 2))
Bhalf0 = sector_basis(sp.Rational(1, 2), 0)
Bhalf1 = sector_basis(sp.Rational(1, 2), 1)
check(
    "R3: D0 maps each of the sectors into itself: D0 B = lambda B, so (0,1/2) -> (1/2,0) matrix elements vanish",
    sp.simplify((Bhalf0.H * D0 * B0)) == sp.zeros(2, 2)
    or all(sp.simplify(x) == 0 for x in (Bhalf0.H * D0 * B0)),
)
bad_conn = not all(sp.simplify(x) == 0 for x in (Bhalf0.H * D0 * B0))
expect_caught("R3 control: claim D0 connects (0,1/2) and (1/2,0)", bad_conn)


# ---- R4: multiplication by degree-1 harmonics, from degree-0 (x) C^2 (the (0,1/2) sector) into degree-1 (x) C^2
# degree-0 (x) C^2 vectors: e_i placed in block 0 (rows 0,1 of the 10-dim space); product with u_j: function u_j (x) e_i in block 1.
def deg1_vec(j, i):
    v = sp.zeros(10, 1)
    v[2 + 2 * j + i] = (
        1  # function index j in block of 4 (offset 1 function in block 0 -> positions 2..9), spin index i
    )
    return v


cols = []
for j in range(4):
    for i in range(2):
        cols.append(deg1_vec(j, i))
Mmul = sp.Matrix.hstack(*cols)
check(
    "R4: multiplication by (a,b,c,d) of the (0,1/2) sector gives 8 independent vectors (rank 8) filling degree 1 (x) C^2",
    Mmul.rank() == 8,
)
expect_caught("R4 control: the multiplication map has rank 7", Mmul.rank() == 7)
# components in (1/2,0) and (1/2,1)
P_half0 = Bhalf0 * (Bhalf0.H * Bhalf0).inv() * Bhalf0.H
P_half1 = Bhalf1 * (Bhalf1.H * Bhalf1).inv() * Bhalf1.H
img0 = P_half0 * Mmul
img1 = P_half1 * Mmul
check(
    "R4: the (1/2,0) component of the images has rank 2 (nonzero: (0,1/2) x (1/2,1/2) contains (1/2,0))",
    img0.rank() == 2,
)
check(
    "R4: the (1/2,1) component has rank 6 ((0,1/2) x (1/2,1/2) = (1/2,0) + (1/2,1))",
    img1.rank() == 6,
)
check(
    "R4: the two components exhaust the image (2 + 6 = 8)",
    sp.simplify(P_half0 * Mmul + P_half1 * Mmul - Mmul) == sp.zeros(10, 8),
)

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
