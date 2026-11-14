"""C189 -- derive the 3/2 shift between D_0 and the true covariant Dirac
operator on S^3, from this project's own geometry. Do not fit it against
the literature (Camporesi-Higuchi, gr-qc/9505009), as the letter to Tom
explicitly flagged: "the 3/2 in the previous message is matched, not
derived. The spectrum it is matched against I took from the literature."

D_0 = -i sum_a sigma_a X_a^R (built in C184/C188) omits the spin-connection
term that a genuinely covariant Dirac operator carries. This round builds
that term from the actual Levi-Civita connection -- via Cartan's structure
equation, in the coframe dual to {X_a^R} -- and shows the omitted term is a
CONSTANT scalar matrix on S^3 (as the letter's own homogeneity argument
predicts), reads off its exact value, and cross-checks the resulting full
spectrum against the general +-(l+3/2), mult (l+1)(l+2) formula -- computed
by combining C184/C188's own D_0 spectrum with the derived shift, not
quoted from Camporesi-Higuchi.

Run:  python c189_derive_32_shift.py
"""

import sympy as sp

PASS, FAIL = [], []


def check(label, condition, detail=""):
    (PASS if condition else FAIL).append(label)
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    if detail:
        print(f"         {detail}")


th, ph, ps = sp.symbols("theta phi psi", real=True)
COORDS = [th, ph, ps]

# ---------------------------------------------------------------------------
# A. X_a^R is an EXACTLY orthonormal frame on the unit S^3 -- verified, not
#    assumed. The induced metric IS the restriction of the flat R^4 metric
#    (same x0..x3 embedding used throughout this project).
# ---------------------------------------------------------------------------
print("=" * 78)
print("A  X_a^R is orthonormal w.r.t. the metric this project already uses")
print("=" * 78)

x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
X4 = [x0, x1, x2, x3]
MUL = {
    (0, 0): (-1, 0), (0, 1): (1, 3), (0, 2): (-1, 2),
    (1, 0): (-1, 3), (1, 1): (-1, 0), (1, 2): (1, 1),
    (2, 0): (1, 2), (2, 1): (-1, 1), (2, 2): (-1, 0),
}  # fmt: skip


def right_mult_components(a):
    out = [sp.Integer(0)] * 4
    out[a + 1] += X4[0]
    for b in range(3):
        c, idx = MUL[(b, a)]
        out[idx] += c * X4[b + 1]
    return out


XR_amb = [right_mult_components(a) for a in range(3)]
G_amb = sp.Matrix(
    [
        [sp.expand(sum(XR_amb[a][m] * XR_amb[b][m] for m in range(4))) for b in range(3)]
        for a in range(3)
    ]
)
sphere = sp.expand(sum(v**2 for v in X4))
check(
    "P1 g(X_a^R, X_b^R) = delta_ab * (x0^2+..+x3^2) identically -- ON THE "
    "UNIT SPHERE this is exactly delta_ab, no rescaling needed",
    all(
        sp.expand(G_amb[a, b] - (sphere if a == b else 0)) == 0 for a in range(3) for b in range(3)
    ),
)

# ---------------------------------------------------------------------------
# B. the dual coframe, and the genuine Levi-Civita connection via Cartan
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("B  dual coframe + Cartan's structure equation for the REAL connection")
print("=" * 78)

XR_coeffs = sp.Matrix(
    [
        [0, 0, 2],
        [2 * sp.cos(ps), 2 * sp.sin(ps) / sp.sin(th), -2 * sp.sin(ps) / sp.tan(th)],
        [-2 * sp.sin(ps), 2 * sp.cos(ps) / sp.sin(th), -2 * sp.cos(ps) / sp.tan(th)],
    ]
)  # confirmed exact in C188, P2a-P4b there

M_inv = sp.simplify(XR_coeffs.inv())
E = [list(M_inv[:, a]) for a in range(3)]

check(
    "P2 the dual coframe satisfies e^a(X_b) = delta_ab exactly",
    all(
        sp.simplify(sum(E[a][mu] * XR_coeffs[b, mu] for mu in range(3))) == (1 if a == b else 0)
        for a in range(3)
        for b in range(3)
    ),
)


def dext(a_coeffs):
    return {
        (i, j): sp.expand(sp.diff(a_coeffs[j], COORDS[i]) - sp.diff(a_coeffs[i], COORDS[j]))
        for i, j in [(0, 1), (0, 2), (1, 2)]
    }


def wedge(a_coeffs, b_coeffs):
    return {
        (i, j): sp.expand(a_coeffs[i] * b_coeffs[j] - a_coeffs[j] * b_coeffs[i])
        for i, j in [(0, 1), (0, 2), (1, 2)]
    }


def add2(*ds):
    out = {(0, 1): 0, (0, 2): 0, (1, 2): 0}
    for d in ds:
        for k in out:
            out[k] += d[k]
    return out


dE = [dext(e) for e in E]
w01_sym = sp.Matrix(sp.symbols("w01_0 w01_1 w01_2"))
w02_sym = sp.Matrix(sp.symbols("w02_0 w02_1 w02_2"))
w12_sym = sp.Matrix(sp.symbols("w12_0 w12_1 w12_2"))

eqA = add2(dE[0], wedge(list(w01_sym), E[1]), wedge(list(w02_sym), E[2]))
eqB = add2(dE[1], wedge(list(-w01_sym), E[0]), wedge(list(w12_sym), E[2]))
eqC = add2(dE[2], wedge(list(-w02_sym), E[0]), wedge(list(-w12_sym), E[1]))
unknowns = list(w01_sym) + list(w02_sym) + list(w12_sym)
eqs = [eq[k] for eq in (eqA, eqB, eqC) for k in [(0, 1), (0, 2), (1, 2)]]
sol = sp.solve(eqs, unknowns, dict=True)
check("P3 Cartan's structure equation has a unique solution", len(sol) == 1)
sol = sol[0]

# cleaned closed form (the raw solve() output has un-reduced sin^2+cos^2=1
# denominators -- this is the same trigsimp fragility noted in C187b/C188;
# stated here explicitly and then verified to satisfy Cartan's equation
# EXACTLY, independent of how it was obtained)
w01 = [sp.sin(ps) / 2, -sp.sin(th) * sp.cos(ps) / 2, sp.Integer(0)]
w02 = [sp.cos(ps) / 2, sp.sin(ps) * sp.sin(th) / 2, sp.Integer(0)]
w12 = [sp.Integer(0), -sp.cos(th) / 2, sp.Rational(-1, 2)]

eqA2 = add2(dE[0], wedge(w01, E[1]), wedge(w02, E[2]))
eqB2 = add2(dE[1], wedge([-c for c in w01], E[0]), wedge(w12, E[2]))
eqC2 = add2(dE[2], wedge([-c for c in w02], E[0]), wedge([-c for c in w12], E[1]))
resid = [sp.trigsimp(eq[k]) for eq in (eqA2, eqB2, eqC2) for k in [(0, 1), (0, 2), (1, 2)]]
check(
    "P4 the closed-form connection satisfies Cartan's equation IDENTICALLY "
    "(residuals exactly zero)",
    all(r == 0 for r in resid),
    f"omega_01={w01}, omega_02={w02}, omega_12={w12}",
)

# ---------------------------------------------------------------------------
# C. the spin connection term, and the shift D_full - D_0
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("C  D_full - D_0: is the omitted term genuinely a constant?")
print("=" * 78)

PAULI = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]

Gamma = [
    (sp.I / 2) * (w01[mu] * PAULI[2] - w02[mu] * PAULI[1] + w12[mu] * PAULI[0]) for mu in range(3)
]
GammaX = [sum((Gamma[mu] * XR_coeffs[a, mu] for mu in range(3)), sp.zeros(2, 2)) for a in range(3)]
extra = sp.simplify(-sp.I * sum((PAULI[a] * GammaX[a] for a in range(3)), sp.zeros(2, 2)))

check(
    "P5 D_full - D_0 is a SCALAR matrix (proportional to identity), "
    "position-independent -- exactly the homogeneity argument the letter "
    "made, now verified by direct computation, not asserted",
    extra == extra[0, 0] * sp.eye(2) and extra[0, 1] == 0,
    f"D_full - D_0 = {list(extra)}",
)
shift = sp.nsimplify(extra[0, 0])
check(
    "P6 the constant is exactly -3/2 (magnitude 3/2, as the letter's fitted "
    "value said -- but this one is COMPUTED, not fitted)",
    shift == sp.Rational(-3, 2),
    f"computed shift = {shift}",
)

# ---------------------------------------------------------------------------
# D. cross-check: does D_0's OWN spectrum (C184/C188), shifted by this
#    DERIVED constant, reproduce the standard +-(l+3/2), mult (l+1)(l+2)
#    pattern for BOTH signs -- computed here, not quoted from the paper
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("D  cross-check: does the derived shift reproduce +-(l+3/2), (l+1)(l+2)?")
print("=" * 78)

N = 12
d0_neg = {-k: (k + 1) * (k + 2) for k in range(N)}  # C184/C188's own -k branch
d0_pos = {k + 2: k * (k + 1) for k in range(N) if k * (k + 1) > 0}  # +(k+2) branch
full = dict(d0_neg)
for v, m in d0_pos.items():
    full[v] = full.get(v, 0) + m

shifted = {sp.Rational(v) + shift: m for v, m in full.items()}
expected = {}
for lvl in range(N - 2):
    expected[sp.Rational(-(lvl + sp.Rational(3, 2)))] = (lvl + 1) * (lvl + 2)
    expected[sp.Rational(lvl + sp.Rational(3, 2))] = (lvl + 1) * (lvl + 2)

common = sorted(set(shifted) & set(expected), key=float)
mismatches = [(v, shifted.get(v), expected.get(v)) for v in common if shifted[v] != expected[v]]
check(
    f"P7 all {len(common)} common eigenvalues (well inside the truncation "
    f"range, boundary effects excluded) match +-(l+3/2) with multiplicity "
    f"(l+1)(l+2) EXACTLY",
    len(common) >= 15 and not mismatches,
    f"mismatches: {mismatches}",
)

# ---------------------------------------------------------------------------
# E. negative control -- does a wrong connection also give a constant, and
#    does a genuinely structure-breaking one give a non-constant leftover?
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("E  negative control: value-discriminating, and genuinely falsifiable")
print("=" * 78)


def build_extra(w01_, w02_, w12_):
    G = [
        (sp.I / 2) * (w01_[mu] * PAULI[2] - w02_[mu] * PAULI[1] + w12_[mu] * PAULI[0])
        for mu in range(3)
    ]
    GX = [sum((G[mu] * XR_coeffs[a, mu] for mu in range(3)), sp.zeros(2, 2)) for a in range(3)]
    return sp.simplify(-sp.I * sum((PAULI[a] * GX[a] for a in range(3)), sp.zeros(2, 2)))


zero_conn = build_extra([sp.Integer(0)] * 3, [sp.Integer(0)] * 3, [sp.Integer(0)] * 3)
check(
    "P8 with NO connection at all, the extra term is 0 (i.e. D_full=D_0 "
    "identically) -- the shift genuinely comes from the connection",
    zero_conn == sp.zeros(2, 2),
)

flipped = build_extra(w01, w02, [-c for c in w12])
check(
    "P9 flipping the sign of omega_12 gives a DIFFERENT constant (-1/2, not "
    "-3/2) -- the check discriminates by VALUE, not merely by 'is it "
    "constant' (several wrong connections still happen to give constants)",
    flipped == sp.Rational(-1, 2) * sp.eye(2) and flipped != extra,
    f"got {list(flipped)}",
)

w12_broken = [w12[0], w12[1] + sp.sin(2 * th), w12[2]]
broken = build_extra(w01, w02, w12_broken)
check(
    "P10 a GENUINELY structure-breaking connection (extra position-dependent "
    "term added) gives a NON-constant, non-diagonal leftover -- 'constant' "
    "is not a free/forced outcome of this computation",
    broken != broken[0, 0] * sp.eye(2) or broken[0, 1] != 0,
    f"got {list(broken)}",
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print(f"C189: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for f in FAIL:
        print(f"  FAILED: {f}")
print("=" * 78)
