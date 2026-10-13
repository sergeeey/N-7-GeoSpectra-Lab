"""C220 source checks (2026-10-13): what the reply states about McMurry (4.45), the 23/24 Sept
documents and the U of the 23 Sept message. Exact sympy, no numerics.

Run: python c220_source_checks.py   (exit code 1 if any check fails)
"""

import sys

import sympy as sp

IU = sp.I
X, Y, Z = sp.symbols("x y z")
TH, PH = sp.symbols("th ph", real=True)
SQ2 = sp.sqrt(2)
RESULTS: list[tuple[str, bool]] = []


def check(label: str, ok: bool) -> None:
    RESULTS.append((label, bool(ok)))
    print(("PASS  " if ok else "FAIL  ") + label)


def zero(expr) -> bool:
    return sp.simplify(sp.expand_complex(expr)) == 0


# ---- Cartesian and polar operators --------------------------------------------------
def lx(f):
    return IU * (Z * sp.diff(f, Y) - Y * sp.diff(f, Z))


def ly(f):
    return IU * (X * sp.diff(f, Z) - Z * sp.diff(f, X))


def lp(f):
    return sp.expand(lx(f) + IU * ly(f))


def lm(f):
    return sp.expand(lx(f) - IU * ly(f))


def lp_polar(f):
    return sp.exp(IU * PH) * (sp.diff(f, TH) + IU * sp.cot(TH) * sp.diff(f, PH))


def lm_polar(f):
    return sp.exp(-IU * PH) * (-sp.diff(f, TH) + IU * sp.cot(TH) * sp.diff(f, PH))


def matrix_of(op, basis):
    """Row = input: op(b_a) = sum_b M[a][b] b_b, by matching coefficients of x, y, z."""
    m = sp.zeros(3, 3)
    syms = sp.symbols("m0:3")
    for a in range(3):
        diff = sp.expand(op(basis[a]) - sum(syms[b] * basis[b] for b in range(3)))
        sol = sp.solve([diff.coeff(v) for v in (X, Y, Z)], syms, dict=True)[0]
        for b in range(3):
            m[a, b] = sol[syms[b]]
    return m


# ---- 1. McMurry (4.45) applied literally at m = -1 (p.91) ---------------------------
def ylm_445(l_val: int, m_val: int):
    """(4.45) as printed (no |m| in the factorials); P_l^m via (4.44) with |m|; theta in (0, pi)."""
    t = sp.symbols("t")
    plm = sp.sin(TH) ** abs(m_val) * sp.diff(sp.legendre(l_val, t), t, abs(m_val)).subs(
        t, sp.cos(TH)
    )
    pref = (-1) ** m_val * sp.sqrt(
        sp.Integer(2 * l_val + 1)
        * sp.factorial(l_val - m_val)
        / (4 * sp.pi * sp.factorial(l_val + m_val))
    )
    return sp.simplify(pref * plm * sp.exp(IU * m_val * PH))


y11, y10, y1m_lit = ylm_445(1, 1), ylm_445(1, 0), ylm_445(1, -1)
y1m_ours = sp.sqrt(3 / (8 * sp.pi)) * sp.sin(TH) * sp.exp(-IU * PH)
check(
    "(4.45) at m=+1 equals Y(1,1) = -sqrt(3/8pi) sin e^{i phi}",
    zero(y11 + sp.sqrt(3 / (8 * sp.pi)) * sp.sin(TH) * sp.exp(IU * PH)),
)
check(
    "(4.45) at m=0 equals Y(1,0) = sqrt(3/4pi) cos",
    zero(y10 - sp.sqrt(3 / (4 * sp.pi)) * sp.cos(TH)),
)
check("(4.45) literal at m=-1 is -2 times Y(1,-1)_ours (kappa = -2)", zero(y1m_lit + 2 * y1m_ours))
check("L- Y(1,0) = -(sqrt2/2) Y(1,-1)_literal", zero(lm_polar(y10) + (SQ2 / 2) * y1m_lit))
check("L+ Y(1,-1)_literal = -2 sqrt2 Y(1,0)", zero(lp_polar(y1m_lit) + 2 * SQ2 * y10))
check("L+ Y(1,0) = sqrt2 Y(1,1) (does not involve Y(1,-1))", zero(lp_polar(y10) - SQ2 * y11))
check(
    "L+- Y(1,-1)_literal products: L- L+ Y = 2 Y still holds (kappa cancels)",
    zero(lm_polar(lp_polar(y1m_lit)) - 2 * y1m_lit),
)

# ---- 2. U of the 23 Sept message, D of the reply ------------------------------------
mlz = sp.diag(1, 0, -1)
mlx = (SQ2 / 2) * sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
mly = (SQ2 / 2) * sp.Matrix([[0, IU, 0], [-IU, 0, IU], [0, -IU, 0]])
g12 = sp.diag(1, 0, -1)
g23 = sp.Matrix([[0, -1, 0], [-sp.Rational(1, 2), 0, sp.Rational(1, 2)], [0, 1, 0]])
g31 = sp.Matrix([[0, -IU, 0], [IU / 2, 0, IU / 2], [0, -IU, 0]])
u_mat = sp.diag(-1, SQ2 / 2, 1)
d_mat = sp.diag(-1 / SQ2, 1, 1 / SQ2)
zero3 = sp.zeros(3, 3)
check("U M(Lz) U^-1 = G12", sp.simplify(u_mat * mlz * u_mat.inv() - g12) == zero3)
check("U M(Lx) U^-1 = G23", sp.simplify(u_mat * mlx * u_mat.inv() - g23) == zero3)
check(
    "U M(Ly) U^-1 = G31 (row = input, no sign flip)",
    sp.simplify(u_mat * mly * u_mat.inv() - g31) == zero3,
)
check("U = (sqrt2/2) D^-1", sp.simplify(u_mat - (SQ2 / 2) * d_mat.inv()) == zero3)
check(
    "D G23 D^-1 = M(Lx) in the sphere-normalised basis",
    sp.simplify(d_mat * g23 * d_mat.inv() - mlx) == zero3,
)


def comm(a, b):
    return a * b - b * a


check("[G23,G31] = -i G12 (row = input)", sp.simplify(comm(g23, g31) + IU * g12) == zero3)
check(
    "[Lx,Ly] f = i Lz f on a degree-1 polynomial",
    zero(
        lx(ly(X + 2 * Y + 3 * Z))
        - ly(lx(X + 2 * Y + 3 * Z))
        - IU * IU * (Y * sp.diff(X + 2 * Y + 3 * Z, X) - X * sp.diff(X + 2 * Y + 3 * Z, Y))
    ),
)

# ---- 3. The 24 Sept letter: four matrices -------------------------------------------
real_basis = [X, Y, Z]
cx_basis = [X + IU * Y, Z, X - IU * Y]
claimed = {
    "real L+": (lp, real_basis, [[0, 0, 1], [0, 0, IU], [-1, -IU, 0]]),
    "real L-": (lm, real_basis, [[0, 0, -1], [0, 0, IU], [1, -IU, 0]]),
    "complex L+": (lp, cx_basis, [[0, 0, 0], [-1, 0, 0], [0, 2, 0]]),
    "complex L-": (lm, cx_basis, [[0, -2, 0], [0, 0, 1], [0, 0, 0]]),
}
for name, (op, basis, target) in claimed.items():
    check(
        f"24 Sept letter: {name} matrix",
        sp.simplify(matrix_of(op, basis) - sp.Matrix(target)) == zero3,
    )

# ---- 4. The 23 Sept notes: (9)-(18) and Part 1 --------------------------------------
rr = sp.sqrt(X**2 + Y**2 + Z**2)
eqs = {
    "(9) L+": (lp(X / rr), Z / rr),
    "(9) L-": (lm(X / rr), -Z / rr),
    "(10) L+": (lp(Y / rr), IU * Z / rr),
    "(10) L-": (lm(Y / rr), IU * Z / rr),
    "(11) L+": (lp(Z / rr), -(X + IU * Y) / rr),
    "(11) L-": (lm(Z / rr), (X - IU * Y) / rr),
    "(12)": (lp((X + IU * Y) / rr), 0),
    "(13)": (lp((X - IU * Y) / rr), 2 * Z / rr),
    "(14)": (lm((X + IU * Y) / rr), -2 * Z / rr),
    "(15)": (lm((X - IU * Y) / rr), 0),
}
check("23 Sept notes (9)-(15) reproduced", all(zero(a - b) for a, b in eqs.values()))
check(
    "linearity example L+(x-iy) = z - i(iz) = 2z",
    zero(lp(X - IU * Y) - (Z - IU * (IU * Z))) and zero(lp(X - IU * Y) - 2 * Z),
)
c_val = sp.sqrt(3 / (4 * sp.pi))
p1_10 = c_val * sp.cos(TH)
p1_11 = -c_val / SQ2 * sp.sin(TH) * sp.exp(IU * PH)
p1_1m = c_val / SQ2 * sp.sin(TH) * sp.exp(-IU * PH)
six = [
    lp_polar(p1_1m) - SQ2 * p1_10,
    lp_polar(p1_10) - SQ2 * p1_11,
    lp_polar(p1_11),
    lm_polar(p1_11) - SQ2 * p1_10,
    lm_polar(p1_10) - SQ2 * p1_1m,
    lm_polar(p1_1m),
]
check("23 Sept Part 1: six actions with its (3)-(5)", all(zero(e) for e in six))

failed = [lab for lab, ok in RESULTS if not ok]
print(f"\n{len(RESULTS) - len(failed)}/{len(RESULTS)} checks pass")
sys.exit(1 if failed else 0)
