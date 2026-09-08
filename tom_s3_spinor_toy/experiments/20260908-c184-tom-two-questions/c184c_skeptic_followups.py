r"""
C184c -- the three things an adversarial pass found missing, closed by computing
rather than by arguing.

  G3  C180 states [X_a^R, X_b^R] = -2 eps X_c^R; C184 verified +2 eps. Both
      rounds define X^R the same way (right multiplication by the quaternion
      unit). Contradiction, or two different objects?
  F   Part F of the main script establishes that Hopf coordinates parameterise
      S^3, but never substitutes them into any spinor. So "the spinors in Hopf
      coordinates" was not actually delivered. Delivered here.
  G1  claim.md said every prediction is paired with an injected-error control.
      Only four were. P1, P2 and P3 get theirs here.
"""

import sympy as sp

x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
X = (x0, x1, x2, x3)
th, ph, ps = sp.symbols("theta phi psi", real=True)
PAULI = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
OK = []


def check(label, cond, detail=""):
    OK.append((label, bool(cond)))
    print(
        f"  [{'PASS' if cond else 'FAIL'}] {label}{('  ' + detail) if detail else ''}"
    )


MUL = {
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
    out = [sp.Integer(0)] * 4
    out[a + 1] += x0
    for b in range(3):
        c, idx = MUL[(b, a)]
        out[idx] += c * X[b + 1]
    return out


def as_operator(comp):
    return lambda f: sp.expand(sum(comp[m] * sp.diff(f, X[m]) for m in range(4)))


XR = [as_operator(right_mult_components(a)) for a in range(3)]

# ===========================================================================
print("=" * 78)
print("G3  the sign conflict with C180 -- two different objects, not a conflict")
print("=" * 78)
# C180 builds the 4x4 MATRIX R[a] with R[a] x = components of (q * e_a) and
# takes matrix commutators. C184 builds the same data as a VECTOR FIELD and
# takes Lie brackets. These necessarily differ in sign, because
# R_a R_b (q) = R_a(q e_b) = q e_b e_a -- composition of right multiplications
# reverses the order, so a -> R_a is an ANTI-homomorphism of the quaternion
# algebra, while a -> X_a^R is a homomorphism of vector fields.
Rmat = [
    sp.Matrix(4, 4, lambda i, j, a=a: sp.diff(right_mult_components(a)[i], X[j]))
    for a in range(3)
]
mat_sign, op_sign = set(), set()
probe = x0 * x1 + x2**2 + x3 * x0 + x1 * x2 * x3
for a in range(3):
    for b in range(3):
        e = sum((sp.LeviCivita(a, b, c) * Rmat[c] for c in range(3)), sp.zeros(4, 4))
        if e == sp.zeros(4, 4):
            continue
        commat = Rmat[a] * Rmat[b] - Rmat[b] * Rmat[a]
        for s in (2, -2):
            if sp.simplify(commat - s * e) == sp.zeros(4, 4):
                mat_sign.add(s)
        cop = sp.expand(XR[a](XR[b](probe)) - XR[b](XR[a](probe)))
        for s in (2, -2):
            tgt = sp.expand(
                s * sum(sp.LeviCivita(a, b, c) * XR[c](probe) for c in range(3))
            )
            if sp.expand(cop - tgt) == 0:
                op_sign.add(s)
print(
    f"  matrix commutator  [R_a, R_b]      = {mat_sign.pop() if len(mat_sign) == 1 else mat_sign} eps_abc R_c   (C180's object)"
)
print(
    f"  vector-field bracket [X_a^R,X_b^R] = {op_sign.pop() if len(op_sign) == 1 else op_sign} eps_abc X_c^R (C184's object)"
)
mat_sign, op_sign = set(), set()
for a in range(3):
    for b in range(3):
        e = sum((sp.LeviCivita(a, b, c) * Rmat[c] for c in range(3)), sp.zeros(4, 4))
        if e == sp.zeros(4, 4):
            continue
        commat = Rmat[a] * Rmat[b] - Rmat[b] * Rmat[a]
        mat_sign |= {
            s for s in (2, -2) if sp.simplify(commat - s * e) == sp.zeros(4, 4)
        }
        cop = sp.expand(XR[a](XR[b](probe)) - XR[b](XR[a](probe)))
        op_sign |= {
            s
            for s in (2, -2)
            if sp.expand(
                cop - s * sum(sp.LeviCivita(a, b, c) * XR[c](probe) for c in range(3))
            )
            == 0
        }
check(
    "G3a the two signs are opposite -- so C180 and C184 do NOT contradict",
    mat_sign == {-2} and op_sign == {2},
    f"matrix {sorted(mat_sign)}, operator {sorted(op_sign)}",
)
check(
    "G3b and the reason is order reversal: R_a R_b = R_{e_b e_a}",
    all(
        sp.simplify(
            Rmat[a] * Rmat[b]
            - sp.Matrix(
                4,
                4,
                lambda i, j, a=a, b=b: sp.diff(
                    sp.expand(
                        sum(
                            sp.diff(right_mult_components(a)[i], X[m])
                            * right_mult_components(b)[m]
                            for m in range(4)
                        )
                    ),
                    X[j],
                ),
            )
        )
        == sp.zeros(4, 4)
        for a in range(3)
        for b in range(3)
    ),
)

# ===========================================================================
print()
print("=" * 78)
print("F  the S^3 spinors actually written in Hopf coordinates")
print("=" * 78)
HOPF = {
    x0: sp.cos(th / 2) * sp.cos((ph + ps) / 2),
    x1: sp.sin(th / 2) * sp.sin((ph - ps) / 2),
    x2: -sp.sin(th / 2) * sp.cos((ph - ps) / 2),
    x3: -sp.cos(th / 2) * sp.sin((ph + ps) / 2),
}


def D0_on(psi_pair):
    """D_0 = -i sum_a sigma_a X_a^R applied to a 2-component polynomial spinor."""
    out = [sp.Integer(0), sp.Integer(0)]
    for a in range(3):
        img = [XR[a](psi_pair[0]), XR[a](psi_pair[1])]
        for r in range(2):
            out[r] += -sp.I * sum(PAULI[a][r, c] * img[c] for c in range(2))
    return [sp.expand(o) for o in out]


# One eigenspinor from each k=1 block, obtained by SOLVING the eigenproblem.
# The first draft probed a hand-written list of candidate pairs and happened to
# contain none from the +3 block -- a defect of the probe list, not of the
# mathematics. Replaced by an actual solve.
def solve_eigenspinors(level, lam):
    """All 2-component polynomial spinors over `level` with D_0 psi = lam psi."""
    n = len(level)
    co = sp.symbols(f"u0:{2 * n}")
    pair = [
        sum(co[i] * level[i] for i in range(n)),
        sum(co[n + i] * level[i] for i in range(n)),
    ]
    img = D0_on(pair)
    eqs = []
    for r in range(2):
        e = sp.expand(img[r] - lam * pair[r])
        eqs += sp.Poly(e, *X).coeffs() if e != 0 else []
    sol = sp.solve(eqs, co, dict=True)
    sol = sol[0] if sol else {}
    free = [c for c in co if c not in sol]
    out = []
    for fc in free:
        sub = {c: (sp.Integer(1) if c == fc else sp.Integer(0)) for c in co}
        cand = [sp.expand(pair[r].subs(sol).subs(sub)) for r in range(2)]
        if any(c != 0 for c in cand):
            out.append(cand)
    return out


LEVEL1 = [x0, x1, x2, x3]
found = {}
for lam in (-1, 3):
    sols = solve_eigenspinors(LEVEL1, lam)
    found[lam] = sols
    print(f"  D_0 = {lam:>2}: eigenspace dimension {len(sols)}")
check(
    "F1 both k=1 blocks are found by solving, with dimensions 6 and 2",
    len(found[-1]) == 6 and len(found[3]) == 2,
    f"dims {{-1: {len(found[-1])}, 3: {len(found[3])}}}",
)

for lam in (-1, 3):
    pair = found[lam][0]  # any member; the eigenspace is degenerate, so this
    # particular vector is basis-dependent -- the point here is the substitution
    hop = [
        sp.simplify(sp.powsimp(sp.expand(c.subs(HOPF).rewrite(sp.exp)), force=True))
        for c in pair
    ]
    print()
    print(
        f"  a D_0 = {lam:>2} eigenspinor, in x-coordinates : {[sp.simplify(c) for c in pair]}"
    )
    print(f"                     the same one in Hopf : {hop}")
    back = D0_on(pair)
    check(
        f"F2 the D_0={lam} eigenvalue survives the Hopf substitution identically",
        all(
            sp.simplify(sp.expand((back[r] - lam * pair[r]).subs(HOPF))) == 0
            for r in range(2)
        ),
    )

# ===========================================================================
print()
print("=" * 78)
print("G1  the injected-error controls P1, P2 and P3 never had")
print("=" * 78)


def harmonic_basis(k):
    monos = [
        x0**a * x1**b * x2**c * x3 ** (k - a - b - c)
        for a in range(k + 1)
        for b in range(k + 1 - a)
        for c in range(k + 1 - a - b)
    ]
    cf = sp.symbols(f"z0:{len(monos)}")
    gen = sum(c * m for c, m in zip(cf, monos))
    lap = sp.expand(sum(sp.diff(gen, v, 2) for v in X))
    sol = sp.solve(sp.Poly(lap, *X).coeffs(), cf, dict=True) if lap != 0 else []
    sol = sol[0] if sol else {}
    out = []
    for fc in [c for c in cf if c not in sol]:
        e = sp.expand(gen.subs(sol).subs({c: (1 if c == fc else 0) for c in cf}))
        if e != 0:
            out.append(e)
    return out


def op_matrix(op, basis):
    cols = []
    for b in basis:
        img = sp.expand(op(b))
        lam = sp.symbols(f"W0:{len(basis)}")
        eq = sp.expand(img - sum(lc * bb for lc, bb in zip(lam, basis)))
        s = sp.solve(sp.Poly(eq, *X).coeffs(), lam, dict=True)
        s = s[0] if s else {}
        cols.append([sp.simplify(s.get(lc, 0)) for lc in lam])
    return sp.Matrix(cols).T


def left_mult_components(a):
    out = [sp.Integer(0)] * 4
    out[a + 1] += x0
    for b in range(3):
        c, idx = MUL[(a, b)]
        out[idx] += c * X[b + 1]
    return out


XL = [as_operator(left_mult_components(a)) for a in range(3)]

# P1 control: apply the SAME (j,j) test to an object known to be OFF-diagonal --
# the C^2-valued functions at k=0, which are (0,1/2). The test must FAIL there.
B0 = harmonic_basis(0)
n0 = len(B0)
JL0 = [
    sp.Matrix(
        sp.kronecker_product(sp.eye(2), sp.Rational(1, 2) * sp.I * op_matrix(o, B0))
    )
    for o in XL
]
JR0 = [
    sp.Matrix(
        sp.kronecker_product(sp.eye(2), sp.Rational(1, 2) * sp.I * op_matrix(o, B0))
    )
    + sp.Matrix(sp.kronecker_product(sp.Rational(1, 2) * PAULI[a], sp.eye(n0)))
    for a, o in enumerate(XL)
]
CL0 = sum((m * m for m in JL0), sp.zeros(2 * n0))
CR0 = sum((m * m for m in JR0), sp.zeros(2 * n0))
print(
    f"  spinor k=0: Casimir_L {dict(CL0.eigenvals())}  Casimir_R {dict(CR0.eigenvals())}"
)
check(
    "G1-P1 the (j,j) test FAILS on the spinor space, which is genuinely (0,1/2) "
    "-- so P1 is not a check that passes on anything",
    CL0.eigenvals() != CR0.eigenvals(),
)

# P2 control: mis-normalise the spin operator (sigma instead of sigma/2). The
# (0,1/2) identification must break.
JR0bad = [
    sp.Matrix(
        sp.kronecker_product(sp.eye(2), sp.Rational(1, 2) * sp.I * op_matrix(o, B0))
    )
    + sp.Matrix(sp.kronecker_product(PAULI[a], sp.eye(n0)))
    for a, o in enumerate(XL)
]
CR0bad = sum((m * m for m in JR0bad), sp.zeros(2 * n0))
print(f"  with S = sigma (wrong by a factor 2): Casimir_R {dict(CR0bad.eigenvals())}")
check(
    "G1-P2 a mis-normalised spin operator no longer gives j_R = 1/2 -- so P2 can fail",
    CR0bad.eigenvals() != {sp.Rational(3, 4): 2},
)

# P3 control: an operator that does NOT commute with the Casimir cannot be
# sorted by irrep at all. Build one and show the commutator is nonzero.
B1 = harmonic_basis(1)
n1 = len(B1)
XLm = [op_matrix(o, B1) for o in XL]
XRm = [op_matrix(o, B1) for o in XR]
JR1 = [
    sp.Matrix(sp.kronecker_product(sp.eye(2), sp.Rational(1, 2) * sp.I * m))
    + sp.Matrix(sp.kronecker_product(sp.Rational(1, 2) * PAULI[a], sp.eye(n1)))
    for a, m in enumerate(XRm)
]
CR1 = sum((m * m for m in JR1), sp.zeros(2 * n1))
Dmix = sum(
    (-sp.I * sp.Matrix(sp.kronecker_product(PAULI[a], XLm[a])) for a in range(3)),
    sp.zeros(2 * n1),
)
print("  a deliberately mixed operator -i sum sigma_a (x) X_a^L:")
check(
    "G1-P3 it does NOT commute with the J^R Casimir, so the sort-by-irrep step "
    "is not something every operator passes",
    sp.simplify(Dmix * CR1 - CR1 * Dmix) != sp.zeros(2 * n1, 2 * n1),
)

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
failed = [lab for lab, ok in OK if not ok]
for lab, ok in OK:
    print(f"  {'PASS' if ok else 'FAIL'}  {lab}")
print(f"\n{len(OK) - len(failed)} of {len(OK)} checks passed")
print("FAILED: " + "; ".join(failed) if failed else "all three follow-ups closed")
