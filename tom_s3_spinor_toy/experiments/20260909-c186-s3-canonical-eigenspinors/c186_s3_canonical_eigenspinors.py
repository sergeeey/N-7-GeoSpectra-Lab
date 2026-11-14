"""C186 -- exact S^3 eigenspinors at k = 2 and 3, in a basis that is not arbitrary.

The letter to Tom declines to send the k >= 2 eigen-objects, and gives two
reasons: the exact arithmetic was never run, and even if it were, a vector
inside a degenerate eigenspace is a choice rather than an object. Only the first
is about effort. This script removes the second first.

D_0 does not act alone. It commutes with J_3^L and with the TOTAL right angular
momentum J_3^R = orbital + spin (checked in claim.md Step 0a, where neither
piece commutes on its own). Diagonalising the three together labels every
eigenspinor by a weight (m_L, m_R); when the joint cells come out
one-dimensional, that label fixes the eigenspinor up to a scalar and the
arbitrariness is gone. Those are the labels Tom's own four S^3 states are read
in, so this is his coordinate system.

Everything is exact over Q(i). No floating point enters any verdict.

Run:  python c186_s3_canonical_eigenspinors.py
"""

import sympy as sp

# ---------------------------------------------------------------------------
# bookkeeping
# ---------------------------------------------------------------------------
PASS, FAIL = [], []


def check(label, condition, detail=""):
    (PASS if condition else FAIL).append(label)
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    if detail:
        print(f"         {detail}")


x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
X = [x0, x1, x2, x3]
I2 = sp.eye(2)
PAULI = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]

# quaternion multiplication table, (a,b) -> (coefficient, unit index), 0 = real
MUL = {
    (0, 0): (-1, 0), (0, 1): (1, 3), (0, 2): (-1, 2),
    (1, 0): (-1, 3), (1, 1): (-1, 0), (1, 2): (1, 1),
    (2, 0): (1, 2), (2, 1): (-1, 1), (2, 2): (-1, 0),
}  # fmt: skip


def right_mult_components(a):
    """Components of q * e_a as coefficients of d/dx_m."""
    out = [sp.Integer(0)] * 4
    out[a + 1] += x0
    for b in range(3):
        c, idx = MUL[(b, a)]
        out[idx] += c * X[b + 1]
    return out


def left_mult_components(a):
    """Components of e_a * q."""
    out = [sp.Integer(0)] * 4
    out[a + 1] += x0
    for b in range(3):
        c, idx = MUL[(a, b)]
        out[idx] += c * X[b + 1]
    return out


def as_operator(components):
    def op(f):
        return sp.expand(sum(components[m] * sp.diff(f, X[m]) for m in range(4)))

    return op


XR = [as_operator(right_mult_components(a)) for a in range(3)]
XL = [as_operator(left_mult_components(a)) for a in range(3)]


def harmonic_basis(k):
    """Harmonic homogeneous polynomials of degree k in x0..x3, exact."""
    monos = []
    for a in range(k + 1):
        for b in range(k + 1 - a):
            for c in range(k + 1 - a - b):
                monos.append(x0**a * x1**b * x2**c * x3 ** (k - a - b - c))
    coeffs = sp.symbols(f"c0:{len(monos)}")
    gen = sum(co * m for co, m in zip(coeffs, monos))
    lap = sp.expand(sum(sp.diff(gen, v, 2) for v in X))
    eqs = sp.Poly(lap, *X).coeffs() if lap != 0 else []
    sol = sp.solve(eqs, coeffs, dict=True)
    sol = sol[0] if sol else {}
    free = [c for c in coeffs if c not in sol]
    out = []
    for fc in free:
        sub = {c: (sp.Integer(1) if c == fc else sp.Integer(0)) for c in coeffs}
        expr = sp.expand(gen.subs(sol).subs(sub))
        if expr != 0:
            out.append(expr)
    return out


def op_matrix(op, basis):
    """Matrix of a linear operator in the given polynomial basis."""
    lam = sp.symbols(f"L0:{len(basis)}")
    cols = []
    for b in basis:
        img = sp.expand(op(b))
        eq = sp.expand(img - sum(lc * bb for lc, bb in zip(lam, basis)))
        sol = sp.solve(sp.Poly(eq, *X).coeffs(), lam, dict=True)
        sol = sol[0] if sol else {}
        cols.append([sp.nsimplify(sol.get(lc, 0)) for lc in lam])
    return sp.Matrix(cols).T


def closes_as_su2(J):
    """[J_a, J_b] = i eps_abc J_c for all a,b -- the only test of the sign."""
    z = sp.zeros(*J[0].shape)
    return all(
        sp.expand(J[a] * J[b] - J[b] * J[a])
        == sp.expand(sp.I * sum((sp.LeviCivita(a, b, c) * J[c] for c in range(3)), z))
        for a in range(3)
        for b in range(3)
    )


class NotPreserved(Exception):
    """A does not map span(P) into itself, so it has no restriction to it."""


def restrict(P, A, guard=True):
    """A restricted to the column span of P, in the basis of P's columns.

    P.H, not P.T: these vectors are complex and P.T*P is not the Gram matrix.

    The guard is not decoration. This formula COMPRESSES A onto the subspace --
    it silently discards whatever part of A*P points out of span(P) -- and a
    compression is a perfectly good operator that can have one-dimensional
    eigenspaces even when A does not preserve the subspace at all. The first
    draft of the negative control below expected the cell structure to collapse
    under an injected error and it did not, for exactly this reason: the check
    was wrong, not the object. So the assumption is now explicit and loud.
    """
    C = (P.H * P).inv() * P.H * (A * P)
    if guard and sp.expand(A * P - P * C) != sp.zeros(*(A * P).shape):
        raise NotPreserved
    return C


def joint_cells(P, AL, AR, guard=True):
    """Simultaneously diagonalise two commuting operators on span(P).

    Returns {(m_L, m_R): [column vectors in the ambient space]}.
    Raises NotPreserved if either operator does not actually preserve span(P).
    """
    cells = {}
    for lL, _, vL in restrict(P, AL, guard).eigenvects():
        Q = P * sp.Matrix.hstack(*vL)  # lift back to the ambient space
        for lR, _, vR in restrict(Q, AR, guard).eigenvects():
            key = (sp.nsimplify(lL), sp.nsimplify(lR))
            cells.setdefault(key, [])
            for v in vR:
                cells[key].append(sp.expand(Q * v))
    return cells


def joint_cells_unguarded(P, AL, AR):
    return joint_cells(P, AL, AR, guard=False)


# ---------------------------------------------------------------------------
print("=" * 78)
print("C186  exact S^3 eigenspinors at k = 2, 3, labelled by (m_L, m_R)")
print("=" * 78)

# --- A. the generators, and the signs that are not a matter of taste --------
print()
print("A  generators and signs  [substrate]")

B1 = harmonic_basis(1)
XR1 = [op_matrix(o, B1) for o in XR]
XL1 = [op_matrix(o, B1) for o in XL]

sR = +1 if closes_as_su2([+sp.I / 2 * m for m in XR1]) else -1
sL = +1 if closes_as_su2([+sp.I / 2 * m for m in XL1]) else -1
check(
    "A1 exactly one sign of (i/2)X closes as su(2) on each side",
    closes_as_su2([sR * sp.I / 2 * m for m in XR1])
    and closes_as_su2([sL * sp.I / 2 * m for m in XL1])
    and not closes_as_su2([-sR * sp.I / 2 * m for m in XR1])
    and not closes_as_su2([-sL * sp.I / 2 * m for m in XL1]),
    f"right {sR:+d}, left {sL:+d} -- opposite, which is the trap C184 fell into",
)


def build(k, spin_sign=+1):
    """D_0, J_3^L, J_3^R(total) at level k. spin_sign=-1 is the injected error."""
    B = harmonic_basis(k)
    n = len(B)
    XRm = [op_matrix(o, B) for o in XR]
    XLm = [op_matrix(o, B) for o in XL]
    D0 = sp.zeros(2 * n)
    for a in range(3):
        D0 += -sp.I * sp.Matrix(sp.kronecker_product(PAULI[a], XRm[a]))
    JL3 = sp.Matrix(sp.kronecker_product(I2, sL * sp.I / 2 * XLm[2]))
    JR3 = sp.Matrix(
        sp.kronecker_product(I2, sR * sp.I / 2 * XRm[2])
    ) + spin_sign * sp.Matrix(sp.kronecker_product(PAULI[2] / 2, sp.eye(n)))
    return B, D0, JL3, JR3


# --- B. main run -----------------------------------------------------------
PRE = {  # pre-registered in claim.md BEFORE running
    2: {"dim": 9, "minus": 12, "plus": 6},
    3: {"dim": 16, "minus": 20, "plus": 12},
}
EXAMPLES = {}

for k in (2, 3):
    print()
    print("-" * 78)
    print(f"B  level k = {k}")
    print("-" * 78)
    B, D0, JL3, JR3 = build(k)
    n = len(B)
    check(
        f"B0 k={k} harmonic basis dim = {PRE[k]['dim']}", n == PRE[k]["dim"], f"got {n}"
    )

    check(
        f"B1 k={k} [D_0, J_3^L] = 0 and [D_0, J_3^R total] = 0",
        sp.expand(D0 * JL3 - JL3 * D0) == sp.zeros(2 * n)
        and sp.expand(D0 * JR3 - JR3 * D0) == sp.zeros(2 * n),
    )
    check(
        f"B2 k={k} the two Cartan operators commute with each other",
        sp.expand(JL3 * JR3 - JR3 * JL3) == sp.zeros(2 * n),
    )

    # spectrum WITHOUT charpoly: prove containment, then count by nullspace.
    lo, hi = sp.Integer(-k), sp.Integer(k + 2)
    ann = sp.expand((D0 - lo * sp.eye(2 * n)) * (D0 - hi * sp.eye(2 * n)))
    check(
        f"B3 k={k} (D_0 + {k})(D_0 - {k + 2}) = 0, so the spectrum is inside {{{-k}, {k + 2}}}",
        ann == sp.zeros(2 * n),
    )

    Nlo = sp.Matrix.hstack(*(D0 - lo * sp.eye(2 * n)).nullspace())
    Nhi = sp.Matrix.hstack(*(D0 - hi * sp.eye(2 * n)).nullspace())
    mlo, mhi = Nlo.shape[1], Nhi.shape[1]
    print(f"    multiplicities: D_0 = {-k} -> {mlo},  D_0 = {k + 2} -> {mhi}")
    check(
        f"B4 k={k} multiplicities are the pre-registered {PRE[k]['minus']} and {PRE[k]['plus']}",
        (mlo, mhi) == (PRE[k]["minus"], PRE[k]["plus"]),
        "k=2 is C184's control; k=3 was never computed in this project before",
    )
    check(f"B5 k={k} multiplicities exhaust 2(k+1)^2", mlo + mhi == 2 * (k + 1) ** 2)

    for lam, P, mult in ((lo, Nlo, mlo), (hi, Nhi, mhi)):
        cells = joint_cells(P, JL3, JR3)
        dims = sorted({len(v) for v in cells.values()})
        mLs = sorted({c[0] for c in cells})
        mRs = sorted({c[1] for c in cells})
        print(f"    D_0 = {lam}: {len(cells)} weight cells, dimensions {dims}")
        print(f"       m_L in {mLs}")
        print(f"       m_R in {mRs}")
        check(
            f"B6 k={k} lambda={lam}: EVERY joint cell is 1-dimensional "
            f"(the basis is canonical, not arbitrary)",
            dims == [1],
        )
        check(
            f"B7 k={k} lambda={lam}: cells account for the whole eigenspace",
            len(cells) == mult,
        )
        check(
            f"B8 k={k} lambda={lam}: m_L runs over j_L = {sp.Rational(k, 2)}",
            mLs == [sp.Rational(i, 2) for i in range(-k, k + 1, 2)],
            f"got {mLs}",
        )
        jr = sp.Rational(k + 1, 2) if lam == lo else sp.Rational(k - 1, 2)
        want_R = [-jr + i for i in range(int(2 * jr) + 1)]
        check(
            f"B9 k={k} lambda={lam}: m_R runs over j_R = {jr}",
            mRs == want_R,
            f"got {mRs}",
        )
        EXAMPLES[(k, lam)] = (B, cells)

# --- C. the eigenspinors themselves, verified as polynomials ---------------
print()
print("-" * 78)
print("C  the objects, re-verified against the DIFFERENTIAL operator")
print("-" * 78)
print("  (matrix algebra could be self-consistent and still wrong; this applies")
print("   -i sum_a sigma_a X_a^R to the polynomial pair directly)")


def as_spinor(B, vec):
    """Column vector in the kron(spin, poly) basis -> polynomial 2-spinor."""
    n = len(B)
    return sp.Matrix(
        [sp.expand(sum(vec[i * n + m] * B[m] for m in range(n))) for i in range(2)]
    )


def apply_D(psi):
    """D_0 psi = -i sum_a sigma_a (X_a^R psi), on a polynomial 2-spinor."""
    out = sp.zeros(2, 1)
    for a in range(3):
        img = sp.Matrix([XR[a](psi[0]), XR[a](psi[1])])
        out += -sp.I * PAULI[a] * img
    return sp.expand(out)


bad = []
for (k, lam), (B, cells) in EXAMPLES.items():
    for key, vecs in cells.items():
        psi = as_spinor(B, vecs[0])
        if sp.expand(apply_D(psi) - lam * psi) != sp.zeros(2, 1):
            bad.append((k, lam, key))
check(
    "C1 every produced eigenspinor satisfies D_0 psi = lambda psi as a differential identity",
    not bad,
    f"{sum(len(c) for _, c in EXAMPLES.values())} objects checked; failures: {bad}",
)

print()
print("  sample -- k=2, D_0 = -2, the two extreme weights:")
B2, cells2 = EXAMPLES[(2, sp.Integer(-2))]
for key in (
    sorted(cells2, key=lambda t: (t[0], t[1]))[:1]
    + sorted(cells2, key=lambda t: (t[0], t[1]))[-1:]
):
    psi = as_spinor(B2, cells2[key][0])
    print(f"    (m_L, m_R) = {key}:  ({psi[0]},  {psi[1]})")

# --- D. negative control ---------------------------------------------------
print()
print("-" * 78)
print("D  negative control -- the injected error goes where the old bug lived")
print("-" * 78)

_, D0b, JL3b, JR3b = build(2, spin_sign=-1)
nb = 2 * PRE[2]["dim"]
commutes = sp.expand(D0b * JR3b - JR3b * D0b) == sp.zeros(nb)
check(
    "D1 with J_3^R built as orbital MINUS spin, it no longer commutes with D_0",
    not commutes,
    "so the joint decomposition is not even well posed -- the check can fail",
)

Nlo_b = sp.Matrix.hstack(*(D0b + 2 * sp.eye(nb)).nullspace())

refused = False
try:
    joint_cells(Nlo_b, JL3b, JR3b)
except NotPreserved:
    refused = True
check(
    "D2 the injected error is DETECTED: the bad J_3^R does not preserve the "
    "D_0 eigenspace, so it has no restriction to it and joint_cells refuses",
    refused,
)

# The first draft of this control expected the CELL STRUCTURE to collapse. It
# does not, and that is worth stating rather than hiding, because it says
# something about how the main criterion must be read.
cells_b = joint_cells_unguarded(Nlo_b, JL3b, JR3b)
dims_b = sorted({len(v) for v in cells_b.values()})
check(
    "D3 without the guard the bad operator ALSO yields 1-dimensional cells -- "
    "so B6 alone is not sufficient and must be read together with B1",
    dims_b == [1],
    f"compressed-bad-operator cell dimensions: {dims_b}, {len(cells_b)} cells "
    f"for a 12-dimensional eigenspace. Being 1-dimensional is necessary, not "
    f"sufficient; what makes the basis canonical is that the labelling "
    f"operator genuinely commutes with D_0 (B1), which this one does not (D1).",
)

mR_bad = sorted({c[1] for c in cells_b})
mR_good = [sp.Rational(i, 2) for i in (-3, -1, 1, 3)]
check(
    "D4 and the labels it produces are not the representation-theoretic "
    "weights, which is what a reader would actually notice",
    mR_bad != mR_good,
    f"bad m_R = {mR_bad}   correct m_R = {mR_good}",
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print(f"C186: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for f in FAIL:
        print(f"  FAILED: {f}")
print("=" * 78)
