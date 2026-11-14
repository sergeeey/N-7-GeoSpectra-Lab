r"""
C184b -- deriving the S^2 spinor harmonics instead of writing them down.

The main script states chi = (e^{-i phi/2} cos(theta/2), e^{+i phi/2} sin(theta/2))
by hand and then checks its properties. That is the weaker of the two things a
reader can ask for, and the correspondent asking the question said explicitly he
would rather see functional forms come out of the theory than be supplied ready-
made and verified afterwards.

So here nothing is supplied. The route is:

  1. take the k=1 harmonic level on S^3 -- span{x_0,x_1,x_2,x_3}, no spinor
     anywhere yet, just scalar functions;
  2. diagonalise the U(1) fibre generator X_3^R on it, by matrix, and READ OFF
     the eigenvectors (not guess them);
  3. substitute the Hopf/Euler coordinates;
  4. observe that the fibre coordinate psi enters each eigenvector only as an
     overall phase e^{-i m psi} -- which is what "fixed weight along the fibre"
     means, and is the reason the object descends at all;
  5. strip that phase. What remains is a function of (theta, phi) only.

Whatever comes out at weight -1/2 IS the spinor doublet; whatever comes out at
weight 0 (checked at k=2) is an ordinary function on S^2. Same machinery, two
sectors, opposite answers -- that contrast is the negative control, and it is
what makes the half-integer case a result rather than an assertion.
"""

import sympy as sp

x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
X = (x0, x1, x2, x3)
th, ph, ps = sp.symbols("theta phi psi", real=True)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
PAULI = (s1, s2, s3)

OK = []


def check(label, cond, detail=""):
    OK.append((label, bool(cond)))
    print(
        f"  [{'PASS' if cond else 'FAIL'}] {label}{('  ' + detail) if detail else ''}"
    )


# The Hopf/Euler coordinates, exactly as Part F of the main script produced them.
HOPF = {
    x0: sp.cos(th / 2) * sp.cos((ph + ps) / 2),
    x1: sp.sin(th / 2) * sp.sin((ph - ps) / 2),
    x2: -sp.sin(th / 2) * sp.cos((ph - ps) / 2),
    x3: -sp.cos(th / 2) * sp.sin((ph + ps) / 2),
}
check(
    "H0 the substitution really lands on the sphere",
    sp.simplify(sum(v**2 for v in HOPF.values()) - 1) == 0,
)

# The anti-isomorphism, checked rather than asserted.
_I2 = sp.eye(2)
_s = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
_qi, _qj, _qk = (sp.I * _s[0], sp.I * _s[1], sp.I * _s[2])
check(
    "H1 the quaternion->Pauli map is an ANTI-isomorphism: image(i)image(j) = -image(k)",
    sp.simplify(_qi * _qj + _qk) == sp.zeros(2, 2),
)
check(
    "H2 and the reversed product is the homomorphic one: image(j)image(i) = +image(k)",
    sp.simplify(_qj * _qi - _qk) == sp.zeros(2, 2),
)


# WHY X_3^L and not X_3^R -- a real subtlety, found by this script failing.
#
# The bug was: the first draft descended along X_3^R (right multiplication by
# the quaternion unit k), on the assumption that it generates the psi fibre of
# the Euler parameterisation U = e^{-i phi s3/2} e^{-i theta s2/2} e^{-i psi s3/2}.
# It does not, and the symptom was unmistakable: the two vectors of a single
# J_3^R weight sector came out with OPPOSITE psi phases, which a genuine weight
# sector cannot do.
#
# Why: the map q -> x0 I + i(x.sigma) sending (1,i,j,k) to (I, i s1, i s2, i s3)
# is an ANTI-isomorphism, not an isomorphism -- (i s1)(i s2) = -i s3 while
# i*j = k maps to +i s3. So quaternionic RIGHT multiplication becomes matrix
# LEFT multiplication, and vice versa. The generator of the psi fibre (which is
# matrix-right multiplication) is therefore the quaternionic-LEFT field X_3^L.
# Verified below rather than asserted.
#
# This is worth noting outside the code as well: it is the same order-reversal
# phenomenon as the transpose/anti-homomorphism point under discussion in the
# correspondence, showing up a second time in a different guise.
def X3R(f):
    """right multiplication by the quaternion unit k."""
    return sp.expand(
        -x3 * sp.diff(f, x0)
        + x2 * sp.diff(f, x1)
        - x1 * sp.diff(f, x2)
        + x0 * sp.diff(f, x3)
    )


def X3L(f):
    """left multiplication by the quaternion unit k -- the psi-fibre generator."""
    return sp.expand(
        -x3 * sp.diff(f, x0)
        - x2 * sp.diff(f, x1)
        + x1 * sp.diff(f, x2)
        + x0 * sp.diff(f, x3)
    )


FIBRE = X3L  # the one that actually generates the psi circle


def weight_sectors(basis):
    """Diagonalise J_3 = (i/2) FIBRE on the given basis; return {weight: vectors}."""
    n = len(basis)
    cols = []
    for b in basis:
        img = FIBRE(b)
        lam = sp.symbols(f"L0:{n}")
        eq = sp.expand(img - sum(lc * bb for lc, bb in zip(lam, basis)))
        sol = sp.solve(sp.Poly(eq, *X).coeffs(), lam, dict=True)
        sol = sol[0] if sol else {}
        cols.append([sp.simplify(sol.get(lc, 0)) for lc in lam])
    M = sp.Rational(1, 2) * sp.I * sp.Matrix(cols).T
    out = {}
    for w, _mult, vecs in M.eigenvects():
        out[sp.nsimplify(w)] = [
            sp.expand(sum(v[i] * basis[i] for i in range(n))) for v in vecs
        ]
    return out


print()
print("=" * 78)
print("STEP 1-2  k=1 scalar harmonics on S^3, diagonalised by the fibre generator")
print("=" * 78)
LEVEL1 = [x0, x1, x2, x3]
sectors = weight_sectors(LEVEL1)
for w in sorted(sectors, key=lambda z: sp.re(z)):
    print(f"  fibre weight {w}: {[sp.simplify(v) for v in sectors[w]]}")
check(
    "D1 the k=1 level splits into exactly two half-integer fibre weights, 2 vectors each",
    set(sectors) == {sp.Rational(1, 2), sp.Rational(-1, 2)}
    and all(len(v) == 2 for v in sectors.values()),
)

print()
print("=" * 78)
print("STEP 3  split the degenerate fibre sector with the SECOND generator")
print("=" * 78)
# The fibre eigenspace is 2-dimensional, so eigenvects() hands back an ARBITRARY
# basis inside it -- the same degeneracy trap that makes an individual
# eigenvector of a degenerate level meaningless. The fix is the standard one: add
# a second commuting operator. Here that is X_3^R, the generator of the OTHER
# SU(2), whose eigenvalue is exactly the label m the correspondent asked about.
W = sp.Rational(-1, 2)
sector = sectors[W]


def restrict_and_split(vectors, op):
    """Diagonalise op inside the span of `vectors`; return [(eigenvalue, vector)]."""
    n = len(vectors)
    cols = []
    for b in vectors:
        img = op(b)
        lam = sp.symbols(f"M0:{n}")
        eq = sp.expand(img - sum(lc * bb for lc, bb in zip(lam, vectors)))
        sol = sp.solve(sp.Poly(eq, *X).coeffs(), lam, dict=True)
        sol = sol[0] if sol else {}
        cols.append([sp.simplify(sol.get(lc, 0)) for lc in lam])
    M = sp.Rational(1, 2) * sp.I * sp.Matrix(cols).T
    out = []
    for w, _m, vs in M.eigenvects():
        for v in vs:
            out.append(
                (sp.nsimplify(w), sp.expand(sum(v[i] * vectors[i] for i in range(n))))
            )
    return sorted(out, key=lambda z: -sp.re(z[0]))


labelled = restrict_and_split(sector, X3R)
check(
    "D2 the second generator splits the sector into two DISTINCT labels m = ±1/2",
    sorted(sp.nsimplify(m) for m, _ in labelled)
    == [sp.Rational(-1, 2), sp.Rational(1, 2)],
)
for m, v in labelled:
    print(f"  fibre weight {W}, m = {m!s:>4}:  {sp.simplify(v)}")

print()
print("=" * 78)
print("STEP 4-5  substitute Hopf, confirm psi is a pure phase, strip it")
print("=" * 78)
stripped = []
for m, v in labelled:
    r = sp.simplify(sp.expand(v.subs(HOPF).rewrite(sp.exp)))
    alpha = sp.simplify(sp.diff(r, ps) / (sp.I * r))  # r = f(th,ph) * e^{i alpha psi}
    q = sp.simplify(sp.powsimp(sp.expand(r * sp.exp(-sp.I * alpha * ps)), force=True))
    stripped.append((m, alpha, q))
    print(f"  m={m!s:>4}:  psi-exponent alpha = {alpha}   ->  {q}")
check(
    "D3 psi enters each labelled vector as a PURE phase (alpha constant)",
    all(
        sp.simplify(sp.diff(a, th)) == 0
        and sp.simplify(sp.diff(a, ph)) == 0
        and sp.simplify(sp.diff(a, ps)) == 0
        for _, a, _ in stripped
    ),
)
check(
    "D4 and the stripped functions depend on (theta, phi) only",
    all(sp.simplify(sp.diff(q, ps)) == 0 for _, _, q in stripped),
)

chi_hand = {
    sp.Rational(1, 2): sp.exp(-sp.I * ph / 2) * sp.cos(th / 2),
    sp.Rational(-1, 2): sp.exp(sp.I * ph / 2) * sp.sin(th / 2),
}
consts = {}
for m, _a, q in stripped:
    for mm, c in chi_hand.items():
        r = sp.simplify(sp.powsimp(sp.expand(q / c), force=True))
        if sp.simplify(sp.diff(r, th)) == 0 and sp.simplify(sp.diff(r, ph)) == 0:
            consts[(m, mm)] = sp.simplify(r)
print(f"  constant ratios (derived m, hand m) -> factor: {consts}")
check(
    "D5 each DERIVED component is a constant multiple of a hand-written one, "
    "and the m labels line up one-to-one",
    len(consts) == 2
    and {k[0] for k in consts} == {sp.Rational(1, 2), sp.Rational(-1, 2)}
    and {k[1] for k in consts} == {sp.Rational(1, 2), sp.Rational(-1, 2)},
)

print()
print("=" * 78)
print("STEP 6  the properties, on the DERIVED and LABELLED doublet")
print("=" * 78)
by_m = {m: q for m, _a, q in stripped}
chi = sp.Matrix([by_m[sp.Rational(1, 2)], by_m[sp.Rational(-1, 2)]])
nrm = sp.simplify(sp.trigsimp(sum(sp.Abs(c) ** 2 for c in chi)))
print(f"  |chi|^2 = {nrm}")
chi = sp.simplify(chi / sp.sqrt(nrm)) if nrm != 1 else chi
check(
    "D6 the DERIVED doublet is double-valued: chi(phi+2pi) = -chi(phi)",
    sp.simplify(chi.subs(ph, ph + 2 * sp.pi) + chi) == sp.zeros(2, 1),
)
bil = [sp.simplify(chi[a] * sp.conjugate(chi[b])) for a in range(2) for b in range(2)]
check(
    "D7 every bilinear of the DERIVED doublet is single-valued in phi",
    all(sp.simplify(e.subs(ph, ph + 2 * sp.pi) - e) == 0 for e in bil),
)


def to_trig(e):
    """Force an exp-form expression back to real trigonometric form."""
    return sp.simplify(
        sp.trigsimp(sp.expand(sp.simplify(sp.expand_complex(sp.expand(e)))))
    )


vec = [to_trig((chi.H * P * chi)[0, 0]) for P in PAULI]
print(f"  chi^dag sigma chi = {vec}")
check(
    "D8 the bilinear is a UNIT vector identically",
    sp.simplify(sp.trigsimp(sum(v**2 for v in vec) - 1)) == 0,
)
want = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
exact = all(to_trig(v - w) == 0 for v, w in zip(vec, want))
print(f"  equals the radial vector exactly, component by component: {exact}")

# The derived doublet is the hand-written one composed with a CONSTANT 2x2
# matrix M -- and the m labels came out crossed, so M swaps the components.
# A component swap is a rotation, which is why the bilinear vector is rotated
# rather than equal. The honest check is therefore not "component by component"
# (the first draft's D9, which a rotation must fail) but: M is unitary, and the
# induced SO(3) matrix R maps the radial vector onto what we computed.
M = sp.zeros(2, 2)
LAB = [sp.Rational(1, 2), sp.Rational(-1, 2)]
for (m_der, m_hand), c in consts.items():
    M[LAB.index(m_der), LAB.index(m_hand)] = c
print(f"  M (derived = M . hand) = {M.tolist()}")
check(
    "D9 M is a constant unitary -- a basis choice, not a discrepancy",
    sp.simplify(M * M.H - sp.eye(2)) == sp.zeros(2, 2)
    and all(
        sp.simplify(sp.diff(M[i, j], v)) == 0
        for i in range(2)
        for j in range(2)
        for v in (th, ph, ps)
    ),
)
R = sp.Matrix(
    3,
    3,
    lambda a, b: sp.simplify(
        sp.Rational(1, 2) * (PAULI[a] * M * PAULI[b] * M.H).trace()
    ),
)
print(f"  induced SO(3) matrix R = {R.tolist()}")
check(
    "D10 R is orthogonal with det +1 (a genuine rotation)",
    sp.simplify(R.T * R - sp.eye(3)) == sp.zeros(3, 3)
    and sp.simplify(R.det() - 1) == 0,
)
rotated = [
    sp.simplify(sp.expand_trig(sum(R[a, b] * want[b] for b in range(3))))
    for a in range(3)
]
check(
    "D11 the DERIVED bilinear equals exactly R applied to the radial vector "
    "-- so the only difference from the hand-written version is that basis choice",
    all(sp.simplify(sp.trigsimp(sp.expand(v - r))) == 0 for v, r in zip(vec, rotated)),
)

print()
print("=" * 78)
print("NEGATIVE CONTROL  the weight-0 sector: same machinery, opposite answer")
print("=" * 78)
# k=2 harmonics: degree-2 harmonic polynomials in four variables, dim 9.
MON2 = [X[a] * X[b] for a in range(4) for b in range(a, 4)]
cf = sp.symbols(f"a0:{len(MON2)}")
gen = sum(c * m for c, m in zip(cf, MON2))
lap = sp.expand(sum(sp.diff(gen, v, 2) for v in X))
sol = sp.solve(sp.Poly(lap, *X).coeffs(), cf, dict=True)
sol = sol[0] if sol else {}
free = [c for c in cf if c not in sol]
LEVEL2 = []
for fcv in free:
    e = sp.expand(gen.subs(sol).subs({c: (1 if c == fcv else 0) for c in cf}))
    if e != 0:
        LEVEL2.append(e)
check("N0 the k=2 level has dimension 9", len(LEVEL2) == 9)
sec2 = weight_sectors(LEVEL2)
print(f"  k=2 weights present: {sorted(sec2, key=lambda z: sp.re(z))}")
check(
    "N1 k=2 carries INTEGER fibre weights only (so a weight-0 sector exists here)",
    all(sp.nsimplify(w).q == 1 for w in sec2),
)
w0 = [sp.simplify(sp.expand_trig(sp.expand(v.subs(HOPF)))) for v in sec2[sp.Integer(0)]]
check(
    "N2 the weight-0 vectors are psi-independent with NO phase to strip",
    all(sp.simplify(sp.diff(v, ps)) == 0 for v in w0),
)
check(
    "N3 and they are SINGLE-valued in phi -- genuine functions on S^2, "
    "the exact opposite of the half-integer sector",
    all(sp.simplify(v.subs(ph, ph + 2 * sp.pi) - v) == 0 for v in w0),
)

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
failed = [lab for lab, ok in OK if not ok]
for lab, ok in OK:
    print(f"  {'PASS' if ok else 'FAIL'}  {lab}")
print(f"\n{len(OK) - len(failed)} of {len(OK)} checks passed")
print(
    "FAILED: " + "; ".join(failed)
    if failed
    else "the S^2 doublet is derived, not assumed; the weight-0 control gives the "
    "opposite answer with the same machinery"
)
