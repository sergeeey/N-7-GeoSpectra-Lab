r"""
C184 -- the five things Tom's two questions need, computed rather than promised.

Everything below is exact (sympy rationals and Q(i)); no floating point enters
any verdict. Each part ends with a check that could have failed, and Part H
injects errors and requires every check to flip.

  A  quaternion <-> SU(2), and the "complex or quaternionic" answer      [P6]
  B  the vector fields of the letter, re-derived and cross-checked
  C  L^2(S^3) carries only (j,j) -- the no-go, a second way              [P1]
  D  D_0 spectrum, reproducing C180                                       [control]
  E  spinor levels labelled by (j_L,j_R), and D_0 sorted by irrep        [P2,P3]
  F  Hopf/Euler coordinates
  G  S^2: explicit psi_{±1/2}, double-valuedness, and the sting          [P4,P5]
  H  injected-error controls
"""

import sympy as sp

x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
X = (x0, x1, x2, x3)
I2 = sp.eye(2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
PAULI = (s1, s2, s3)

OK = []


def check(label, condition, detail=""):
    OK.append((label, bool(condition)))
    print(
        f"  [{'PASS' if condition else 'FAIL'}] {label}{('  ' + detail) if detail else ''}"
    )
    return bool(condition)


# ===========================================================================
print("=" * 78)
print("A  quaternion <-> SU(2), and which basis makes the projection real  [P6]")
print("=" * 78)
# The letter's own basis: sigma_mu = (I, i s1, i s2, i s3) -- quaternionic.
SIG_Q = (I2, sp.I * s1, sp.I * s2, sp.I * s3)
SIG_P = (I2, s1, s2, s3)  # the plain Pauli basis, for contrast

U = sp.simplify(x0 * SIG_Q[0] + x1 * SIG_Q[1] + x2 * SIG_Q[2] + x3 * SIG_Q[3])
print(f"  U(q) = {U.tolist()}")
det = sp.simplify(U.det())
check(
    "det U = x0^2+x1^2+x2^2+x3^2 (so U in SU(2) on the sphere)",
    sp.simplify(det - (x0**2 + x1**2 + x2**2 + x3**2)) == 0,
    f"det = {sp.factor(det)}",
)

proj_q = [sp.simplify(sp.Rational(1, 2) * (S.H * U).trace()) for S in SIG_Q]
proj_p = [sp.simplify(sp.Rational(1, 2) * (S.H * U).trace()) for S in SIG_P]
print(f"  quaternionic basis: (1/2)Tr(sigma_mu^dag U) = {proj_q}")
print(f"  plain Pauli basis : (1/2)Tr(sigma_mu^dag U) = {proj_p}")
check(
    "P6a quaternionic basis returns (x0,x1,x2,x3) exactly", proj_q == [x0, x1, x2, x3]
)
check(
    "P6b plain Pauli basis returns (x0, i*x1, i*x2, i*x3) -- the unwelcome i",
    proj_p == [x0, sp.I * x1, sp.I * x2, sp.I * x3],
)

# ===========================================================================
print()
print("=" * 78)
print("B  the letter's vector fields, re-derived from quaternion multiplication")
print("=" * 78)
# Right multiplication q -> q*e_a  and left multiplication q -> e_a*q, read off
# as coefficient vectors, then turned into first-order operators.
QUAT_UNITS = ["i", "j", "k"]
MUL = {  # (a,b) -> (coefficient, unit index) for quaternion units, 0 = real
    (0, 0): (-1, 0),
    (0, 1): (1, 3),
    (0, 2): (-1, 2),
    (1, 0): (-1, 3),
    (1, 1): (-1, 0),
    (1, 2): (1, 1),
    (2, 0): (1, 2),
    (2, 1): (-1, 1),
    (2, 2): (-1, 0),
}


def right_mult_components(a):
    """components of q * e_a, as a list of 4 expressions in x0..x3."""
    out = [sp.Integer(0)] * 4
    out[a + 1] += x0  # x0 * e_a
    for b in range(3):  # x_{b+1} e_b * e_a
        c, idx = MUL[(b, a)]
        out[idx] += c * X[b + 1]
    return out


def left_mult_components(a):
    """components of e_a * q."""
    out = [sp.Integer(0)] * 4
    out[a + 1] += x0
    for b in range(3):  # e_a * x_{b+1} e_b
        c, idx = MUL[(a, b)]
        out[idx] += c * X[b + 1]
    return out


def as_operator(components):
    def op(f):
        return sp.expand(sum(components[m] * sp.diff(f, X[m]) for m in range(4)))

    return op


XR = [as_operator(right_mult_components(a)) for a in range(3)]
XL = [as_operator(left_mult_components(a)) for a in range(3)]

LETTER_XR = [  # exactly as printed in the sent letter
    -x1 * sp.Symbol("d0")
    + x0 * sp.Symbol("d1")
    + x3 * sp.Symbol("d2")
    - x2 * sp.Symbol("d3"),
    -x2 * sp.Symbol("d0")
    - x3 * sp.Symbol("d1")
    + x0 * sp.Symbol("d2")
    + x1 * sp.Symbol("d3"),
    -x3 * sp.Symbol("d0")
    + x2 * sp.Symbol("d1")
    - x1 * sp.Symbol("d2")
    + x0 * sp.Symbol("d3"),
]
d = sp.symbols("d0 d1 d2 d3")
mine = [sum(right_mult_components(a)[m] * d[m] for m in range(4)) for a in range(3)]
check(
    "B1 the re-derived X_a^R match the letter's printed forms verbatim",
    all(sp.expand(mine[a] - LETTER_XR[a]) == 0 for a in range(3)),
)


# su(2) brackets and L-R commutation
def comm(A, B, f):
    return sp.expand(A(B(f)) - B(A(f)))


probe = x0 * x1 + x2**2 + x3 * x0 + x1 * x2 * x3
br_ok = all(
    sp.expand(
        comm(XR[a], XR[b], probe)
        - 2 * sum(sp.LeviCivita(a, b, c) * XR[c](probe) for c in range(3))
    )
    == 0
    for a in range(3)
    for b in range(3)
)
check("B2 [X_a^R, X_b^R] = 2 eps_abc X_c^R", br_ok)
check(
    "B3 [X_a^L, X_b^R] = 0 (left and right actions commute)",
    all(sp.expand(comm(XL[a], XR[b], probe)) == 0 for a in range(3) for b in range(3)),
)

# ===========================================================================
print()
print("=" * 78)
print("C  L^2(S^3) carries only (j,j) -- the no-go by direct decomposition  [P1]")
print("=" * 78)


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
    basis = []
    for fc in free:
        sub = {c: (sp.Integer(1) if c == fc else sp.Integer(0)) for c in coeffs}
        expr = sp.expand(gen.subs(sol).subs(sub))
        if expr != 0:
            basis.append(expr)
    return basis


def op_matrix(op, basis):
    """Matrix of a linear operator in the given polynomial basis."""
    cols = []
    for b in basis:
        img = sp.expand(op(b))
        # solve img = sum lambda_i basis_i
        lam = sp.symbols(f"L0:{len(basis)}")
        eq = sp.expand(img - sum(lc * bb for lc, bb in zip(lam, basis)))
        sol = sp.solve(sp.Poly(eq, *X).coeffs(), lam, dict=True)
        sol = sol[0] if sol else {}
        cols.append([sp.simplify(sol.get(lc, 0)) for lc in lam])
    return sp.Matrix(cols).T


def casimir_eigs(ops, basis):
    """Eigenvalues of sum_a J_a^2, as a multiset.

    The overall sign of J_a = +-(i/2) X_a is irrelevant here because a Casimir
    is quadratic -- which is exactly why this part could not catch the sign bug
    that Part E did. Kept as +-(i/2) deliberately, with the note.
    """
    mats = [sp.Rational(-1, 2) * sp.I * op_matrix(o, basis) for o in ops]
    C = sum((m * m for m in mats), sp.zeros(len(basis)))
    return C.eigenvals()


for k in range(4):
    B = harmonic_basis(k)
    assert len(B) == (k + 1) ** 2, f"level {k}: dim {len(B)} != {(k + 1) ** 2}"
    eL = casimir_eigs(XL, B)
    eR = casimir_eigs(XR, B)
    j = sp.Rational(k, 2)
    want = {j * (j + 1): (k + 1) ** 2}
    print(f"  k={k}: dim {len(B):>2}   Casimir_L {dict(eL)}   Casimir_R {dict(eR)}")
    check(f"P1 level k={k} is exactly (j,j) with j={j}", eL == want and eR == want)

# ===========================================================================
print()
print("=" * 78)
print("D  D_0 spectrum on C^2-valued functions -- reproducing C180  [control]")
print("=" * 78)


def spinor_basis(k):
    B = harmonic_basis(k)
    return [(p, i) for p in B for i in (0, 1)]


def D0_matrix(k):
    """D_0 = -i sum_a sigma_a (x) X_a^R, in the basis {p (x) e_i}."""
    B = harmonic_basis(k)
    n = len(B)
    M = sp.zeros(2 * n, 2 * n)
    XRm = [op_matrix(o, B) for o in XR]
    for a in range(3):
        M += -sp.I * sp.Matrix(sp.kronecker_product(PAULI[a], XRm[a]))
    return M


spec = {}
for k in range(3):
    M = D0_matrix(k)
    e = M.eigenvals()
    spec[k] = e
    print(f"  k={k}: {dict(e)}")

check("D1 k=0 -> eigenvalue 0 with multiplicity 2", spec[0] == {sp.Integer(0): 2})
check(
    "D2 k=1 -> {-1 (mult 6), +3 (mult 2)} as C180 and the letter report",
    spec[1] == {sp.Integer(-1): 6, sp.Integer(3): 2},
)
check(
    "D3 k=2 -> {-2 (mult 12), +4 (mult 6)}",
    spec[2] == {sp.Integer(-2): 12, sp.Integer(4): 6},
)

# ===========================================================================
print()
print("=" * 78)
print("E  spinor levels labelled by (j_L, j_R), and D_0 sorted by irrep  [P2,P3]")
print("=" * 78)
# J^L acts only on the function; J^R acts on function AND fibre.
for k in (0, 1):
    B = harmonic_basis(k)
    n = len(B)
    XLm = [op_matrix(o, B) for o in XL]
    XRm = [op_matrix(o, B) for o in XR]
    # WHY the +i/2 and not -i/2: B2 established [X_a, X_b] = 2 eps_abc X_c, so
    # J_a = c X_a obeys [J_a, J_b] = 2c eps_abc J_c, and the angular-momentum
    # normalisation [J_a,J_b] = i eps_abc J_c forces c = +i/2.
    # The bug was: the first draft used -i/2 here while keeping S_a = +sigma_a/2,
    # so J_tot = J_orb + S had its two terms in opposite conventions and the
    # cross term came out -2 J.S instead of +2 J.S. Part C never caught it
    # because a Casimir is quadratic and blind to the overall sign; only the SUM
    # in JR is sensitive to it. Symptom: Casimir_R = {3:2, 1:6} (which is
    # 3/2 - 2*(J.S) evaluated with the wrong sign) instead of {0:2, 2:6}.
    # Fixed by using +i/2 for both orbital operators.
    JL = [
        sp.Matrix(sp.kronecker_product(I2, sp.Rational(1, 2) * sp.I * m)) for m in XLm
    ]
    JR = [
        sp.Matrix(sp.kronecker_product(I2, sp.Rational(1, 2) * sp.I * m))
        + sp.Matrix(sp.kronecker_product(sp.Rational(1, 2) * PAULI[a], sp.eye(n)))
        for a, m in enumerate(XRm)
    ]
    # The check that would have caught the sign bug above on sight: a genuine
    # total angular momentum must close on su(2) with [J_a,J_b] = i eps_abc J_c.
    # The mis-signed J_tot does NOT -- it is orbital minus spin, not a sum.
    algebra_ok = all(
        sp.simplify(
            JR[a] * JR[b]
            - JR[b] * JR[a]
            - sp.I
            * sum((sp.LeviCivita(a, b, c) * JR[c] for c in range(3)), sp.zeros(2 * n))
        )
        == sp.zeros(2 * n, 2 * n)
        for a in range(3)
        for b in range(3)
    )
    check(f"E{k}c total J^R closes on su(2): [J_a,J_b] = i eps_abc J_c", algebra_ok)

    CL = sum((m * m for m in JL), sp.zeros(2 * n))
    CR = sum((m * m for m in JR), sp.zeros(2 * n))
    D = D0_matrix(k)
    print(
        f"  k={k}: Casimir_L {dict(CL.eigenvals())}   Casimir_R {dict(CR.eigenvals())}"
    )
    check(
        f"E{k}a D_0 commutes with the total J^R Casimir",
        sp.simplify(D * CR - CR * D) == sp.zeros(2 * n, 2 * n),
    )
    check(
        f"E{k}b D_0 commutes with the J^L Casimir",
        sp.simplify(D * CL - CL * D) == sp.zeros(2 * n, 2 * n),
    )
    if k == 0:
        want_R = {sp.Rational(3, 4): 2}  # j_R = 1/2
        check(
            "P2 k=0 is (j_L,j_R) = (0, 1/2), dim 2, D_0 = 0",
            CL.eigenvals() == {sp.Integer(0): 2}
            and CR.eigenvals() == want_R
            and D.eigenvals() == {sp.Integer(0): 2},
        )
    if k == 1:
        # sort D_0 eigenvalues by the j_R block they live in
        sorted_by_irrep = {}
        for jr_val, mult in CR.eigenvals().items():
            # projector onto that Casimir eigenspace
            ns = (CR - jr_val * sp.eye(2 * n)).nullspace()
            P = sp.Matrix.hstack(*ns)
            block = sp.simplify(P.pinv() * D * P)
            evs = block.eigenvals()
            jr = sp.nsimplify((sp.sqrt(1 + 4 * jr_val) - 1) / 2)
            sorted_by_irrep[jr] = (mult, dict(evs))
            print(f"      j_R = {jr}  (dim {mult})  ->  D_0 = {dict(evs)}")
        check(
            "P3 j_R=0 block has dim 2 and D_0 = +3",
            sorted_by_irrep.get(sp.Integer(0), (None, None))[0] == 2
            and sorted_by_irrep[sp.Integer(0)][1] == {sp.Integer(3): 2},
        )
        check(
            "P3 j_R=1 block has dim 6 and D_0 = -1",
            sorted_by_irrep.get(sp.Integer(1), (None, None))[0] == 6
            and sorted_by_irrep[sp.Integer(1)][1] == {sp.Integer(-1): 6},
        )

# ===========================================================================
print()
print("=" * 78)
print("F  Hopf / Euler coordinates")
print("=" * 78)
th, ph, ps = sp.symbols("theta phi psi", real=True)
# Euler parameterisation of SU(2): U = e^{-i phi s3/2} e^{-i theta s2/2} e^{-i psi s3/2}
Uh = sp.simplify(
    sp.Matrix([[sp.exp(-sp.I * ph / 2), 0], [0, sp.exp(sp.I * ph / 2)]])
    * sp.Matrix([[sp.cos(th / 2), -sp.sin(th / 2)], [sp.sin(th / 2), sp.cos(th / 2)]])
    * sp.Matrix([[sp.exp(-sp.I * ps / 2), 0], [0, sp.exp(sp.I * ps / 2)]])
)
print(f"  U(theta,phi,psi) = {Uh.tolist()}")
check("F1 det U = 1 identically", sp.simplify(Uh.det() - 1) == 0)
check("F2 U is unitary identically", sp.simplify(Uh.H * Uh - I2) == sp.zeros(2, 2))
hopf_x = [
    sp.simplify(sp.expand_trig(sp.Rational(1, 2) * (S.H * Uh).trace())) for S in SIG_Q
]
print("  x_mu in Euler/Hopf coordinates:")
for m, e in enumerate(hopf_x):
    print(
        f"     x{m} = {sp.simplify(sp.trigsimp(sp.re(sp.expand(e)) + sp.I * sp.im(sp.expand(e))))}"
    )
check(
    "F3 sum x_mu^2 = 1 identically in the Hopf coordinates",
    sp.simplify(sum(e**2 for e in hopf_x) - 1) == 0,
)

# ===========================================================================
print()
print("=" * 78)
print("G  S^2: the explicit psi_{±1/2}, and the sting in the tail  [P4,P5]")
print("=" * 78)
# Fixing the fibre index (right index m' = +1/2) leaves the first column of
# D^{1/2}, i.e. the first column of U with the psi-dependence stripped.
chi = sp.Matrix(
    [sp.exp(-sp.I * ph / 2) * sp.cos(th / 2), sp.exp(sp.I * ph / 2) * sp.sin(th / 2)]
)
print(f"  chi(theta,phi) = {chi.T.tolist()[0]}")
chi_shift = sp.simplify(chi.subs(ph, ph + 2 * sp.pi))
check(
    "P4 chi(phi + 2pi) = -chi(phi) exactly -- double-valued, hence not a function",
    sp.simplify(chi_shift + chi) == sp.zeros(2, 1),
)

bil = [
    sp.simplify(sp.expand(chi[a] * sp.conjugate(chi[b])))
    for a in range(2)
    for b in range(2)
]
bil_shift = [sp.simplify(e.subs(ph, ph + 2 * sp.pi) - e) for e in bil]
check(
    "P5a every bilinear chi_a chi_b^* IS single-valued in phi",
    all(e == 0 for e in bil_shift),
    f"differences {bil_shift}",
)

vec = [sp.simplify(sp.expand_trig(sp.simplify((chi.H * P * chi)[0, 0]))) for P in PAULI]
want_vec = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
print(f"  chi^dag sigma chi = {vec}")
check(
    "P5b chi^dag sigma chi is exactly the unit vector (sin th cos ph, sin th sin ph, cos th)",
    all(sp.simplify(v - w) == 0 for v, w in zip(vec, want_vec)),
)
check(
    "P5c and it has unit length identically",
    sp.simplify(sum(v**2 for v in vec) - 1) == 0,
)

# ===========================================================================
print()
print("=" * 78)
print("H  injected-error controls -- every check above must be able to fail")
print("=" * 78)
bad_chi = sp.Matrix(
    [sp.exp(-sp.I * ph) * sp.cos(th / 2), sp.exp(sp.I * ph) * sp.sin(th / 2)]
)
check(
    "H1 an integer-weight chi (phase e^{-i phi}) is single-valued -- so P4 CAN fail",
    sp.simplify(bad_chi.subs(ph, ph + 2 * sp.pi) - bad_chi) == sp.zeros(2, 1),
)
bad_vec = [sp.simplify((bad_chi.H * P * bad_chi)[0, 0]) for P in PAULI]
check(
    "H2 that same chi does NOT give the unit vector -- so P5b CAN fail",
    any(sp.simplify(v - w) != 0 for v, w in zip(bad_vec, want_vec)),
)
bad_proj = [sp.simplify(sp.Rational(1, 2) * (S.H * U).trace()) for S in SIG_P]
check(
    "H3 the plain Pauli basis fails the P6a identity -- so P6a CAN fail",
    bad_proj != [x0, x1, x2, x3],
)
Bc = harmonic_basis(1)
XRm = [op_matrix(o, Bc) for o in XR]
Mbad = sum(
    (-sp.I * sp.Matrix(sp.kronecker_product(PAULI[a], XRm[a])) for a in range(3)),
    sp.zeros(8),
) + sp.eye(8)  # deliberately shifted by +1
check(
    "H4 a D_0 shifted by +1 no longer matches C180 -- so D2 CAN fail",
    Mbad.eigenvals() != {sp.Integer(-1): 6, sp.Integer(3): 2},
)

# ===========================================================================
print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
failed = [lab for lab, ok in OK if not ok]
for lab, ok in OK:
    print(f"  {'PASS' if ok else 'FAIL'}  {lab}")
print(f"\n{len(OK) - len(failed)} of {len(OK)} checks passed")
if failed:
    print("FAILED: " + "; ".join(failed))
else:
    print("all predictions held, and all four injected-error controls flipped")
