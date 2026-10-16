r"""C220: sphere normalisation of the l=1 harmonics, ladder operators on the normalised set,
and "discovering" the harmonics from the ladder operators.

Everything is exact (sympy) with every intermediate step printed, then cross-checked by an
independent numerical route (scipy quadrature, numpy finite differences) that shares no code
with the symbolic route.  Predictions P1-P7 are in claim.md and were written before this ran.

Conventions (claim.md): L_z = -i d_phi; L_+ = e^{i phi}(d_theta + i cot(theta) d_phi);
L_- = e^{-i phi}(-d_theta + i cot(theta) d_phi); Cartesian L_x = i(z d_y - y d_z),
L_y = i(x d_z - z d_x), L_z = i(y d_x - x d_y), L_+- = L_x +- i L_y; matrices are in the
row = input convention, operator(b_a) = sum_b M[a][b] b_b.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy import integrate

HERE = Path(__file__).resolve().parent
IU = sp.I
r = sp.symbols("r", positive=True)
th, ph = sp.symbols("theta phi", real=True)
X, Y, Z = sp.symbols("x y z", real=True)
SQ2 = sp.sqrt(2)

RES: dict = {}
CHECKS: list[tuple[str, str, bool, str]] = []


def check(cid: str, text: str, ok: bool, kind: str = "main") -> None:
    """kind='main': an independent check, ok must be True.
    kind='control': ok means the control behaved as it must (the wrong thing was detected).
    kind='restatement': follows from other checks or compares two typings of one formula; kept
    for the reader but NOT counted as independent evidence."""
    CHECKS.append((cid, text, bool(ok), kind))
    tag = {
        "control": "   (negative control)",
        "restatement": "   (restatement, not counted)",
    }
    print(f"  [{'PASS' if ok else 'FAIL'}] {cid}  {text}" + tag.get(kind, ""))


def sec(title: str) -> None:
    print("\n" + "=" * 100 + f"\n{title}\n" + "=" * 100)


def zero(expr) -> bool:
    """Exact zero test; works for scalars and for sympy matrices (all entries)."""
    if isinstance(expr, sp.MatrixBase):
        return all(zero(e) for e in expr)
    return sp.simplify(sp.expand_complex(sp.simplify(expr))) == 0


# ---------------------------------------------------------------------------------------
# spherical coordinates on the sphere of radius r
# ---------------------------------------------------------------------------------------
xs = r * sp.sin(th) * sp.cos(ph)
ys = r * sp.sin(th) * sp.sin(ph)
zs = r * sp.cos(th)
dS = r**2 * sp.sin(th)  # area element of S^2_r; the r**2 is the whole r-bookkeeping


def surface_integral(f) -> sp.Expr:
    return sp.simplify(
        sp.integrate(
            sp.integrate(sp.expand(f * dS), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)
        )
    )


def r_degree(expr) -> sp.Expr:
    """Homogeneity degree in r of a monomial c*r**k (this is the 'dimension' of the quantity)."""
    return sp.simplify(r * sp.diff(sp.log(sp.simplify(expr)), r))


# =======================================================================================
sec("PART A  Real harmonics: is  int x*x dS  proportional to r^2 or to r^4?")
# =======================================================================================
print(
    "Set-up: x = r sin(th) cos(ph), y = r sin(th) sin(ph), z = r cos(th);  dS = r^2 sin(th) dth dph."
)
print("So   x^2 dS = r^4 sin^3(th) cos^2(ph) dth dph   (r^2 from x^2, r^2 from dS).\n")

# identity (2): d/dphi ( phi/2 + sin(phi)cos(phi)/2 ) = cos^2(phi)
F2 = ph / 2 + sp.sin(ph) * sp.cos(ph) / 2
check(
    "A1",
    "identity (2): d/dphi[phi/2 + sin(phi)cos(phi)/2] = cos^2(phi)",
    zero(sp.diff(F2, ph) - sp.cos(ph) ** 2),
)
I_cos2 = sp.simplify(F2.subs(ph, 2 * sp.pi) - F2.subs(ph, 0))
I_sin2 = sp.simplify(2 * sp.pi - I_cos2)  # sin^2 = 1 - cos^2
print(
    f"  int_0^2pi cos^2(phi) dphi = F2(2pi)-F2(0) = {I_cos2};   int_0^2pi sin^2(phi) dphi = 2pi - {I_cos2} = {I_sin2}"
)

# identity (3): d/dtheta ( cos(3 th)/12 - 3 cos(th)/4 ) = sin^3(th)   [reading of the garbled printed form]
F3 = sp.cos(3 * th) / 12 - sp.Rational(3, 4) * sp.cos(th)
check(
    "A2",
    "identity (3) as read: d/dtheta[cos(3th)/12 - 3cos(th)/4] = sin^3(th)",
    zero(sp.diff(F3, th) - sp.sin(th) ** 3),
)
I_sin3 = sp.simplify(F3.subs(th, sp.pi) - F3.subs(th, 0))
print(f"  int_0^pi sin^3(theta) dtheta = F3(pi)-F3(0) = {I_sin3}")

F4 = -(sp.cos(th) ** 3) / 3
check(
    "A3",
    "d/dtheta[-cos^3(th)/3] = cos^2(th) sin(th)",
    zero(sp.diff(F4, th) - sp.cos(th) ** 2 * sp.sin(th)),
)
I_c2s = sp.simplify(F4.subs(th, sp.pi) - F4.subs(th, 0))
print(f"  int_0^pi cos^2(theta) sin(theta) dtheta = {I_c2s}")

Ixx = sp.simplify(r**4 * I_sin3 * I_cos2)
Iyy = sp.simplify(r**4 * I_sin3 * I_sin2)
Izz = sp.simplify(r**4 * I_c2s * 2 * sp.pi)
print(
    f"\n  int x^2 dS = r^4 * (int sin^3) * (int cos^2) = r^4 * {I_sin3} * {I_cos2} = {Ixx}"
)
print(
    f"  int y^2 dS = r^4 * (int sin^3) * (int sin^2) = r^4 * {I_sin3} * {I_sin2} = {Iyy}"
)
print(
    f"  int z^2 dS = r^4 * (int cos^2 sin) * (2 pi)  = r^4 * {I_c2s} * 2pi        = {Izz}"
)

# mixed integrals
mixed = {
    "xy": sp.integrate(sp.sin(ph) * sp.cos(ph), (ph, 0, 2 * sp.pi)),
    "xz": sp.integrate(sp.cos(ph), (ph, 0, 2 * sp.pi)),
    "yz": sp.integrate(sp.sin(ph), (ph, 0, 2 * sp.pi)),
}
print(
    f"  mixed: int xy dS ~ int_0^2pi sin(ph)cos(ph) = {mixed['xy']};  xz ~ int cos(ph) = {mixed['xz']};  yz ~ int sin(ph) = {mixed['yz']}"
)

full = [surface_integral(a * b) for a in (xs, ys, zs) for b in (xs, ys, zs)]
gram_real_raw = sp.Matrix(3, 3, full)
print(
    f"\n  Full double integrals (sympy, independent of the step-by-step route), Gram of (x,y,z) on S^2_r:\n  {gram_real_raw}"
)
target_raw = sp.Rational(4, 3) * sp.pi * r**4 * sp.eye(3)
check(
    "P1",
    "int x^2 dS = int y^2 dS = int z^2 dS = 4 pi r^4/3 and all mixed integrals vanish (step route)",
    zero(Ixx - target_raw[0, 0])
    and zero(Iyy - target_raw[0, 0])
    and zero(Izz - target_raw[0, 0])
    and all(v == 0 for v in mixed.values()),
)
check(
    "P1b",
    "full double-integral Gram matrix of (x,y,z) = (4 pi r^4/3) * identity",
    zero(gram_real_raw - target_raw),
)

# dimension check and the two competing candidates
deg_integrand = r_degree(xs**2) + r_degree(dS)
print(
    f"\n  Dimension check: x^2 has degree {r_degree(xs**2)} in r, dS has degree {r_degree(dS)}  => int x^2 dS must have degree {deg_integrand}."
)
cand_r2 = 4 * sp.pi * r**2 / 3
cand_r4 = 4 * sp.pi * r**4 / 3
print(
    f"  candidate 4 pi r^2/3 has degree {r_degree(cand_r2)};  candidate 4 pi r^4/3 has degree {r_degree(cand_r4)}"
)
check(
    "A4",
    "r^4 version passes the dimension test",
    r_degree(cand_r4) == deg_integrand,
    "restatement",
)
check(
    "A5",
    "NEGATIVE CONTROL: r^2 version FAILS the dimension test for x",
    r_degree(cand_r2) != deg_integrand,
    "restatement",
)
Ixr = surface_integral((xs / r) ** 2)
Ixo = sp.simplify(
    sp.integrate(
        sp.integrate(sp.expand(xs**2 * sp.sin(th)), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)
    )
)
print("  The r^2 value 4 pi r^2/3 arises from EITHER of two different integrals:")
print(
    f"    route 1:  int (x/r)^2 dS = {Ixr}   (degree {r_degree(Ixr)}): the integral of x/r, not of x;"
)
print(
    f"    route 2:  int x^2 dOmega = {Ixo}   (degree {r_degree(Ixo)}): x^2 with the r^2 of dS left out."
)
print(
    "  This script does not decide which route anyone's calculation took; it shows both give r^2."
)
check("A6", "route 1: int (x/r)^2 dS = 4 pi r^2/3", zero(Ixr - cand_r2))
check(
    "A6b", "route 2: int x^2 dOmega (no r^2 from dS) = 4 pi r^2/3", zero(Ixo - cand_r2)
)

# normalisation
Nreal = sp.sqrt(3 / (4 * sp.pi)) / r**2
check(
    "P2a",
    "N = sqrt(3/(4pi))/r^2 equals (1/2) sqrt(3/pi)/r^2",
    zero(Nreal - sp.Rational(1, 2) * sp.sqrt(3 / sp.pi) / r**2),
)
gram_real = sp.Matrix(
    3,
    3,
    [
        surface_integral(Nreal * a * Nreal * b)
        for a in (xs, ys, zs)
        for b in (xs, ys, zs)
    ],
)
print(f"\n  Gram matrix of x'_i = N x_i with N = sqrt(3/(4 pi))/r^2:\n  {gram_real}")
check(
    "P2",
    "normalised real harmonics x'_i = (1/2) sqrt(3/pi) x_i/r^2 have Gram matrix = identity",
    gram_real == sp.eye(3),
)
print(
    "\n  Other normalisations of the same three functions on S^2_r (what each needs):"
)
for name, fac in (("x_i", 1), ("x_i/r", 1 / r), ("x_i/r^2", 1 / r**2)):
    n2 = surface_integral((fac * xs) ** 2)
    print(
        f"    int ({name})^2 dS = {n2}   =>  normalising constant {sp.simplify(1 / sp.sqrt(n2))}"
    )
RES["partA"] = {
    "Ixx": str(Ixx),
    "Iyy": str(Iyy),
    "Izz": str(Izz),
    "gram_raw": str(gram_real_raw),
    "gram_normalised": str(gram_real),
    "N": str(Nreal),
}

# numeric cross-check (independent route)
sec("PART A (numeric)  independent quadrature at r = 2")
r0 = 2.0


def quad(fun):
    val, _err = integrate.dblquad(
        lambda p, t: fun(t, p), 0.0, np.pi, 0.0, 2 * np.pi, epsabs=1e-11, epsrel=1e-11
    )
    return val


def sph(t, p):
    return r0 * np.sin(t) * np.cos(p), r0 * np.sin(t) * np.sin(p), r0 * np.cos(t)


num_xx = quad(lambda t, p: sph(t, p)[0] ** 2 * r0**2 * np.sin(t))
num_zz = quad(lambda t, p: sph(t, p)[2] ** 2 * r0**2 * np.sin(t))
num_xy = quad(lambda t, p: sph(t, p)[0] * sph(t, p)[1] * r0**2 * np.sin(t))
print(
    f"  numeric int x^2 dS = {num_xx:.10f};  4 pi r^4/3 = {4 * np.pi * r0**4 / 3:.10f};  4 pi r^2/3 = {4 * np.pi * r0**2 / 3:.10f}"
)
print(f"  numeric int z^2 dS = {num_zz:.10f};  numeric int xy dS = {num_xy:.2e}")
check(
    "A7",
    "numeric quadrature at r=2 agrees with 4 pi r^4/3 (rel. 1e-9) and not with 4 pi r^2/3",
    abs(num_xx / (4 * np.pi * r0**4 / 3) - 1) < 1e-9
    and abs(num_zz / (4 * np.pi * r0**4 / 3) - 1) < 1e-9
    and abs(num_xx / (4 * np.pi * r0**2 / 3) - 1) > 0.5
    and abs(num_xy) < 1e-9,
)

# =======================================================================================
sec("PART B  Complex harmonics normalised by the same method")
# =======================================================================================
pp = xs + IU * ys  # x + i y
mm = xs - IU * ys  # x - i y
raw = [pp, zs, mm]
gram_raw_c = sp.Matrix(
    3, 3, [surface_integral(sp.conjugate(a) * b) for a in raw for b in raw]
)
print(
    "Raw functions  p = x+iy, z, m = x-iy.   Gram matrix <f_a, f_b> = int conj(f_a) f_b dS:"
)
print(f"  {gram_raw_c}")
print(
    "  (|x+iy|^2 = x^2+y^2 gives 8 pi r^4/3;  z^2 gives 4 pi r^4/3: squared norms in the ratio 2 : 1 : 2.)"
)
check(
    "P3a",
    "raw complex functions are mutually orthogonal with squared norms 8pi r^4/3, 4pi r^4/3, 8pi r^4/3",
    zero(
        gram_raw_c
        - sp.diag(8 * sp.pi * r**4 / 3, 4 * sp.pi * r**4 / 3, 8 * sp.pi * r**4 / 3)
    ),
)

n_pm = sp.sqrt(3 / (8 * sp.pi)) / r**2
n_0 = sp.sqrt(3 / (4 * sp.pi)) / r**2
Y1c = -n_pm * pp  # Condon-Shortley phase on m=+1
Y0c = n_0 * zs
Ym1c = n_pm * mm
Yc = [Y1c, Y0c, Ym1c]
gram_Y = sp.Matrix(
    3, 3, [surface_integral(sp.conjugate(a) * b) for a in Yc for b in Yc]
)
print(
    "\n  Normalised: Y'_(1,1) = -sqrt(3/8pi) (x+iy)/r^2, Y'_(1,0) = sqrt(3/4pi) z/r^2, Y'_(1,-1) = +sqrt(3/8pi) (x-iy)/r^2"
)
print(f"  Gram matrix of (Y'_(1,1), Y'_(1,0), Y'_(1,-1)) =\n  {gram_Y}")
check(
    "P3b",
    "Gram matrix of the normalised complex harmonics = identity",
    gram_Y == sp.eye(3),
)

# polar forms and the positive control against sympy's own Ynm
y11 = -sp.sqrt(3 / (8 * sp.pi)) * sp.sin(th) * sp.exp(IU * ph)
y10 = sp.sqrt(3 / (4 * sp.pi)) * sp.cos(th)
y1m1 = sp.sqrt(3 / (8 * sp.pi)) * sp.sin(th) * sp.exp(-IU * ph)
for lab, expr_cart, expr_pol in (
    ("(1,1)", Y1c, y11),
    ("(1,0)", Y0c, y10),
    ("(1,-1)", Ym1c, y1m1),
):
    check(
        f"P3-{lab}",
        f"Y'_{lab} on S^2_r = Y_{lab}(theta,phi)/r",
        zero(sp.simplify(expr_cart - expr_pol / r)),
        "restatement",
    )
for m_, mine in ((1, y11), (0, y10), (-1, y1m1)):
    ref = sp.Ynm(1, m_, th, ph).expand(func=True)
    check(
        f"P3-pos{m_}",
        f"POSITIVE CONTROL: sympy Ynm(1,{m_}) equals the Y_(1,{m_}) used here",
        zero(sp.simplify(ref - mine)),
    )
RES["partB"] = {
    "gram_raw_complex": str(gram_raw_c),
    "gram_normalised": str(gram_Y),
    "Y11": str(y11),
    "Y10": str(y10),
    "Y1m1": str(y1m1),
}

# =======================================================================================
sec(
    "PART C  Ladder operators on the sphere-normalised complex harmonics (polar and Cartesian)"
)
# =======================================================================================


def lz_polar(f):
    return -IU * sp.diff(f, ph)


def lp_polar(f):
    return sp.exp(IU * ph) * (sp.diff(f, th) + IU * sp.cot(th) * sp.diff(f, ph))


def lm_polar(f):
    return sp.exp(-IU * ph) * (-sp.diff(f, th) + IU * sp.cot(th) * sp.diff(f, ph))


def show_polar(label, op, sign, f, target, tlabel):
    """print the two pieces of the operator, their sum, the prefactor and the comparison."""
    a = sign * sp.diff(f, th)
    b = IU * sp.cot(th) * sp.diff(f, ph)
    pref = sp.exp(IU * ph) if sign > 0 else sp.exp(-IU * ph)
    total = sp.simplify(sp.expand_complex(pref * (a + b)))
    print(f"  {label}:  f = {sp.simplify(f)}")
    print(
        f"      ({'+' if sign > 0 else '-'}d_theta) f = {sp.simplify(a)};   i cot(theta) d_phi f = {sp.simplify(b)}"
    )
    print(
        f"      sum = {sp.simplify(a + b)};   times e^({'+' if sign > 0 else '-'}i phi) => {total}"
    )
    ok = zero(total - target)
    print(
        f"      target {tlabel} = {sp.simplify(target)};   difference = {sp.simplify(total - target)}  -> {'OK' if ok else 'MISMATCH'}"
    )
    return ok


YP = {1: y11, 0: y10, -1: y1m1}
polar_cases = [
    ("L+ Y(1,-1)", +1, YP[-1], SQ2 * YP[0], "sqrt2 Y(1,0)"),
    ("L+ Y(1,0)", +1, YP[0], SQ2 * YP[1], "sqrt2 Y(1,1)"),
    ("L+ Y(1,1)", +1, YP[1], sp.Integer(0), "0"),
    ("L- Y(1,1)", -1, YP[1], SQ2 * YP[0], "sqrt2 Y(1,0)"),
    ("L- Y(1,0)", -1, YP[0], SQ2 * YP[-1], "sqrt2 Y(1,-1)"),
    ("L- Y(1,-1)", -1, YP[-1], sp.Integer(0), "0"),
]
print(
    "Polar form (operators as used in C201/C206, attributed there to McMurry p.144 and not re-checked against the book; unit sphere, the 1/r of Y' passes through, see below):\n"
)
polar_ok = [show_polar(c[0], None, c[1], c[2], c[3], c[4]) for c in polar_cases]
check(
    "P4-polar",
    "all six polar ladder relations: coefficient sqrt(2) (0 at the ends)",
    all(polar_ok),
)

print(
    "\nr-dependence: apply the operators to Y'(r,theta,phi) = Y(theta,phi)/r.  The operators contain no d_r, so"
)
rdep_ok = []
for c in polar_cases:
    op = lp_polar if c[1] > 0 else lm_polar
    lhs = sp.simplify(op(c[2] / r))
    rhs = sp.simplify(c[3] / r)
    rdep_ok.append(zero(lhs - rhs))
    print(
        f"  {c[0]}:  L(Y/r) = {sp.simplify(lhs)}   vs   target/r = {sp.simplify(rhs)}"
    )
check("P4-r", "ladder coefficients are independent of r", all(rdep_ok), "restatement")

# Cartesian
RR2 = X**2 + Y**2 + Z**2


def lx_c(f):
    return IU * (Z * sp.diff(f, Y) - Y * sp.diff(f, Z))


def ly_c(f):
    return IU * (X * sp.diff(f, Z) - Z * sp.diff(f, X))


def lz_c(f):
    return IU * (Y * sp.diff(f, X) - X * sp.diff(f, Y))


def lp_c(f):
    return lx_c(f) + IU * ly_c(f)


def lm_c(f):
    return lx_c(f) - IU * ly_c(f)


c8 = sp.sqrt(3 / (8 * sp.pi))
c4 = sp.sqrt(3 / (4 * sp.pi))
YC = {1: -c8 * (X + IU * Y) / RR2, 0: c4 * Z / RR2, -1: c8 * (X - IU * Y) / RR2}
print(
    "\nCartesian form: Y'_(1,m)(x,y,z) with 1/(x^2+y^2+z^2) = 1/r^2 (rational functions, no square roots)."
)
for m_, f in YC.items():
    print(f"  Y'_(1,{m_:+d}) = {f}")
print("  L_x f = i(z f_y - y f_z),  L_y f = i(x f_z - z f_x),  L_+- = L_x +- i L_y.\n")
cart_cases = [
    ("L+ Y'(1,-1)", lp_c, YC[-1], SQ2 * YC[0]),
    ("L+ Y'(1,0)", lp_c, YC[0], SQ2 * YC[1]),
    ("L+ Y'(1,1)", lp_c, YC[1], sp.Integer(0)),
    ("L- Y'(1,1)", lm_c, YC[1], SQ2 * YC[0]),
    ("L- Y'(1,0)", lm_c, YC[0], SQ2 * YC[-1]),
    ("L- Y'(1,-1)", lm_c, YC[-1], sp.Integer(0)),
]
cart_ok = []
for lab, op, f, target in cart_cases:
    lxf, lyf = lx_c(f), ly_c(f)
    res = sp.simplify(op(f))
    ok = zero(res - target)
    cart_ok.append(ok)
    print(f"  {lab}:  L_x f = {sp.simplify(lxf)};   L_y f = {sp.simplify(lyf)}")
    print(
        f"      L_{'+' if op is lp_c else '-'} f = {res};   target = {sp.simplify(target)}  -> {'OK' if ok else 'MISMATCH'}"
    )
check(
    "P4-cart",
    "all six Cartesian ladder relations: coefficient sqrt(2) (0 at the ends)",
    all(cart_ok),
)
check(
    "P4-Lz",
    "L_z (Cartesian) has eigenvalues m on Y'(1,m)",
    all(zero(lz_c(f) - m_ * f) for m_, f in YC.items()),
)

# norm-forced magnitude
sec("PART C2  Why the magnitude is sqrt(2): it is forced by the norm")
print(
    "With L_+^dagger = L_-, <L_- Y, L_- Y> = <Y, L_+ L_- Y> = l(l+1) - m(m-1) for |l=1,m>.  Direct integral on S^2_r:\n"
)
norms = {}
for lab, op, f in (
    ("L- Y'(1,1)", lm_polar, y11),
    ("L- Y'(1,0)", lm_polar, y10),
    ("L- Y'(1,-1)", lm_polar, y1m1),
    ("L+ Y'(1,-1)", lp_polar, y1m1),
    ("L+ Y'(1,0)", lp_polar, y10),
    ("L+ Y'(1,1)", lp_polar, y11),
):
    g = sp.simplify(op(f / r))
    nrm = surface_integral(sp.conjugate(g) * g)
    norms[lab] = nrm
    print(f"  int |{lab}|^2 dS = {nrm}")
expected = {
    "L- Y'(1,1)": 2,
    "L- Y'(1,0)": 2,
    "L- Y'(1,-1)": 0,
    "L+ Y'(1,-1)": 2,
    "L+ Y'(1,0)": 2,
    "L+ Y'(1,1)": 0,
}
check(
    "P4-norm",
    "int |L_pm Y'|^2 dS = l(l+1) - m(m pm 1) = 2,2,0,2,2,0 for every r",
    all(zero(norms[k] - v) for k, v in expected.items()),
)

# =======================================================================================
sec("PART C3  Dependence of the coefficients on the normalisation and the phase (P5)")
# =======================================================================================
kappa = sp.symbols("kappa", nonzero=True)
Y_m1_k = kappa * y1m1
c_minus = sp.simplify(
    sp.simplify(lm_polar(y10)) / Y_m1_k
)  # L- Y10 = c_minus * (kappa Y_{1,-1})
c_plus = sp.simplify(
    sp.simplify(lp_polar(Y_m1_k)) / y10
)  # L+ (kappa Y_{1,-1}) = c_plus * Y10
print(
    f"  Replace Y(1,-1) by kappa*Y(1,-1):  L- Y(1,0) = ({c_minus}) * [kappa Y(1,-1)];   L+ [kappa Y(1,-1)] = ({c_plus}) * Y(1,0)"
)
check(
    "P5a",
    "coefficients become sqrt(2)/kappa and kappa*sqrt(2)",
    zero(c_minus - SQ2 / kappa) and zero(c_plus - kappa * SQ2),
)
print(
    "\n  kappa      L- Y(1,0) coefficient     L+ Y(1,-1) coefficient   (illustration only: NOT a claim about any particular text)"
)
for kv in (1, -1, 2, sp.Rational(1, 2), 1 / SQ2, SQ2):
    print(
        f"  {kv!s:<9} {sp.simplify(c_minus.subs(kappa, kv))!s:<25} {sp.simplify(c_plus.subs(kappa, kv))!s:<25}"
    )
y11_noCS = +sp.sqrt(3 / (8 * sp.pi)) * sp.sin(th) * sp.exp(IU * ph)
c_noCS = sp.simplify(sp.simplify(lp_polar(y10)) / y11_noCS)
print(
    f"\n  Drop the Condon-Shortley sign of Y(1,1):  L+ Y(1,0) = ({c_noCS}) * Y(1,1)_noCS"
)
check(
    "P5b",
    "NEGATIVE CONTROL: without the CS sign of Y(1,1) the coefficient is -sqrt(2), not +sqrt(2)",
    zero(c_noCS + SQ2),
    "control",
)
y1m1_wrongphase = -y1m1
c_wp = sp.simplify(sp.simplify(lm_polar(y10)) / y1m1_wrongphase)
check(
    "P5c",
    "NEGATIVE CONTROL: Y(1,-1) with the opposite sign gives -sqrt(2) for L- Y(1,0)",
    zero(c_wp + SQ2),
    "control",
)
RES["partC"] = {
    "kappa_minus": str(c_minus),
    "kappa_plus": str(c_plus),
    "noCS_coeff": str(c_noCS),
    "norms": {k: str(v) for k, v in norms.items()},
}

# =======================================================================================
sec("PART D  Matrices (row = input):  operator(b_a) = sum_b M[a][b] b_b")
# =======================================================================================
th_, ph_ = th, ph


def inner(f, g):
    return sp.simplify(
        sp.integrate(
            sp.integrate(
                sp.expand(sp.conjugate(f) * g * sp.sin(th_)), (ph_, 0, 2 * sp.pi)
            ),
            (th_, 0, sp.pi),
        )
    )


def matrix_of(op, basis):
    """M with op(b_a) = sum_b M[a][b] b_b, via Gram: H[c][a] = <b_c, op b_a> = sum_b M[a][b] G[c][b]."""
    n = len(basis)
    G = sp.Matrix(n, n, lambda i, j: inner(basis[i], basis[j]))
    H = sp.Matrix(n, n, lambda c, a: inner(basis[c], sp.simplify(op(basis[a]))))
    M = (G.inv() * H).T
    return sp.simplify(M), G


e1, e2, e3 = (
    sp.sin(th) * sp.exp(IU * ph),
    sp.cos(th),
    sp.sin(th) * sp.exp(-IU * ph),
)  # (x+iy)/r, z/r, (x-iy)/r on the unit sphere
bases = {
    "e   = ((x+iy)/r, z/r, (x-iy)/r)   [raw complex, norms^2 2:1:2]": [e1, e2, e3],
    "u   = ((x+iy)/(sqrt2 r), z/r, (x-iy)/(sqrt2 r))   [unitary, no CS phase]": [
        e1 / SQ2,
        e2,
        e3 / SQ2,
    ],
    "Y'  = (Y'(1,1), Y'(1,0), Y'(1,-1))   [sphere-normalised, CS phase]": [
        y11,
        y10,
        y1m1,
    ],
}
mats: dict = {}
for name, b in bases.items():
    Mp, G = matrix_of(lp_polar, b)
    Mm, _ = matrix_of(lm_polar, b)
    Mz, _ = matrix_of(lz_polar, b)
    mats[name] = {
        "G": G,
        "Lp": Mp,
        "Lm": Mm,
        "Lz": Mz,
        "Lx": sp.simplify((Mp + Mm) / 2),
        "Ly": sp.simplify((Mp - Mm) / (2 * IU)),
    }
    print(
        f"\n  basis {name}\n    Gram = {G}\n    L+ = {Mp}\n    L- = {Mm}\n    Lz = {Mz}"
    )
    print(
        f"    Lx = (L+ + L-)/2 = {mats[name]['Lx']}\n    Ly = (L+ - L-)/(2i) = {mats[name]['Ly']}"
    )

kE, kU, kY = list(bases)
check(
    "P6a",
    "basis e: M(L+) = [[0,0,0],[-1,0,0],[0,2,0]] and M(L-) = [[0,-2,0],[0,0,1],[0,0,0]] (C206)",
    mats[kE]["Lp"] == sp.Matrix([[0, 0, 0], [-1, 0, 0], [0, 2, 0]])
    and mats[kE]["Lm"] == sp.Matrix([[0, -2, 0], [0, 0, 1], [0, 0, 0]]),
)
check(
    "P6b",
    "basis Y': both non-zero entries of M(L+) and of M(L-) are sqrt(2)",
    mats[kY]["Lp"] == sp.Matrix([[0, 0, 0], [SQ2, 0, 0], [0, SQ2, 0]])
    and mats[kY]["Lm"] == sp.Matrix([[0, SQ2, 0], [0, 0, SQ2], [0, 0, 0]]),
)
check(
    "P6c",
    "basis u (unitary, no CS phase): entries are -sqrt(2) and +sqrt(2): the CS phase is what makes both +sqrt(2)",
    mats[kU]["Lp"] == sp.Matrix([[0, 0, 0], [-SQ2, 0, 0], [0, SQ2, 0]]),
)

# the correspondent's complex-basis generator matrices, as encoded (and verified) in C205 step 3
G12 = sp.diag(1, 0, -1)
G23 = sp.Matrix([[0, -1, 0], [sp.Rational(-1, 2), 0, sp.Rational(1, 2)], [0, 1, 0]])
G31 = sp.Matrix([[0, -IU, 0], [IU / 2, 0, IU / 2], [0, -IU, 0]])
print(
    f"\n  Gamma'(T12) = {G12};  Gamma'(T23) = {G23};  Gamma'(T31) = {G31}   (C205 step 3, basis e)"
)
check(
    "P6d",
    "basis e: M(Lz) = Gamma'(T12), M(Lx) = Gamma'(T23), M(Ly) = Gamma'(T31)",
    mats[kE]["Lz"] == G12 and mats[kE]["Lx"] == G23 and mats[kE]["Ly"] == G31,
)
check(
    "P6e",
    "basis e: M(L+) = Gamma'(T23) + i Gamma'(T31)  and  M(L-) = Gamma'(T23) - i Gamma'(T31)",
    sp.simplify(mats[kE]["Lp"] - (G23 + IU * G31)) == sp.zeros(3)
    and sp.simplify(mats[kE]["Lm"] - (G23 - IU * G31)) == sp.zeros(3),
    "restatement",
)
# negative control: wrong ordering of the basis
swapped = [e3, e2, e1]
Mx_sw, _ = matrix_of(lambda f: (lp_polar(f) + lm_polar(f)) / 2, swapped)
check(
    "P6f",
    "NEGATIVE CONTROL: with e1 and e3 swapped, M(Lx) no longer equals Gamma'(T23)",
    not zero(Mx_sw - G23),
    "control",
)

# basis change e -> Y'
Dm = sp.diag(
    -sp.sqrt(3 / (8 * sp.pi)), sp.sqrt(3 / (4 * sp.pi)), sp.sqrt(3 / (8 * sp.pi))
)  # Y'_a = sum_b D[a][b] e_b
Dn = sp.simplify(Dm / sp.sqrt(3 / (4 * sp.pi)))
print(
    f"\n  Y'_a = sum_b D[a][b] e_b with D = sqrt(3/4pi) * {Dn}  (the overall scalar cancels in D M D^-1)"
)
check(
    "P6g",
    "D proportional to diag(-1/sqrt2, 1, 1/sqrt2)",
    Dn == sp.diag(-1 / SQ2, 1, 1 / SQ2),
    "restatement",
)
GG = {"T12": G12, "T23": G23, "T31": G31}
GGp = {k: sp.simplify(Dm * v * Dm.inv()) for k, v in GG.items()}
for k, v in GGp.items():
    print(f"  Gamma''({k}) = D Gamma'({k}) D^-1 = {v}")
check(
    "P6h",
    "in basis Y': D Gamma'(T12,T23,T31) D^-1 = M(Lz), M(Lx), M(Ly)",
    GGp["T12"] == mats[kY]["Lz"]
    and GGp["T23"] == mats[kY]["Lx"]
    and GGp["T31"] == mats[kY]["Ly"],
)
check(
    "P6i",
    "in basis Y' the CONJUGATED Gamma'' (not the printed Gamma') satisfy L+- = Gamma''(T23) +- i Gamma''(T31) (linearity, follows from P6h)",
    sp.simplify(mats[kY]["Lp"] - (GGp["T23"] + IU * GGp["T31"])) == sp.zeros(3)
    and sp.simplify(mats[kY]["Lm"] - (GGp["T23"] - IU * GGp["T31"])) == sp.zeros(3),
    "restatement",
)
check(
    "P6k",
    "NEGATIVE CONTROL: the PRINTED Gamma'(T23) +- i Gamma'(T31) do NOT give M(L+-) in the sphere-normalised basis Y'",
    (not zero(mats[kY]["Lp"] - (G23 + IU * G31)))
    and (not zero(mats[kY]["Lm"] - (G23 - IU * G31))),
    "control",
)
print(
    f"    printed Gamma'(T23)+iGamma'(T31) = {sp.simplify(G23 + IU * G31)}   vs   M_Y'(L+) = {mats[kY]['Lp']}"
)
_alpha = sp.Integer(7)
M_scaled_e, _ = matrix_of(lp_polar, [_alpha * b for b in (e1, e2, e3)])
M_scaled_e_m, _ = matrix_of(lm_polar, [_alpha * b for b in (e1, e2, e3)])
check(
    "P6l",
    "a COMMON rescaling (alpha = 7) of the three basis functions of e leaves M(L+-) unchanged, so the printed Gamma' still apply",
    M_scaled_e == mats[kE]["Lp"] and M_scaled_e_m == mats[kE]["Lm"],
)
M_scaled_y, _ = matrix_of(lp_polar, [_alpha * b for b in (y11, y10, y1m1)])
u_cs = [
    -e1 / SQ2,
    e2,
    e3 / SQ2,
]  # equal norms (Gram 4 pi/3 * I), CS phase, NOT unit-normalised
M_ucs, G_ucs = matrix_of(lp_polar, u_cs)
check(
    "P5d",
    "equal norms (any common scale) + CS phase already give sqrt(2), sqrt(2): alpha*Y' and (-e1/sqrt2, e2, e3/sqrt2)",
    M_scaled_y == mats[kY]["Lp"]
    and M_ucs == mats[kY]["Lp"]
    and G_ucs == (4 * sp.pi / 3) * sp.eye(3),
)
print(f"    Gram of (-e1/sqrt2, e2, e3/sqrt2) = {G_ucs};   M(L+) = {M_ucs}")
herm = all(
    sp.simplify(m_ - m_.H) == sp.zeros(3) for m_ in (GGp["T12"], GGp["T23"], GGp["T31"])
)
print(
    f"  Hermitian in the orthonormal basis Y' (as they must be): {herm};  not Hermitian in basis e: {sp.simplify(G23 - G23.H) != sp.zeros(3)}"
)
check(
    "P6j",
    "generator matrices are Hermitian in the orthonormal basis Y' and not Hermitian in basis e",
    herm and sp.simplify(G23 - G23.H) != sp.zeros(3),
)
RES["partD"] = {k: {kk: str(vv) for kk, vv in v.items()} for k, v in mats.items()}
RES["partD"]["Gamma_in_Yprime"] = {k: str(v) for k, v in GGp.items()}

# =======================================================================================
sec("PART E  'Discover' the complex harmonics from the ladder operators")
# =======================================================================================
chi = sp.Function("chi")
print(
    "Step 1.  L_z = -i d_phi.  Eigenfunctions of L_z with eigenvalue m: psi = g(r) chi_m(theta) e^{i m phi}."
)
g = sp.Function("g")
psi_phi = sp.Function("F")
dsol = sp.dsolve(
    sp.Eq(-IU * sp.diff(psi_phi(ph), ph), sp.Symbol("m") * psi_phi(ph)), psi_phi(ph)
)
print(
    f"  dsolve(-i F' = m F) = {dsol}   (single-valuedness F(phi+2pi) = F(phi) forces m integer; l = 1 allows m = -1, 0, 1)"
)
check(
    "E1",
    "L_z eigenfunctions have the phi-dependence e^{i m phi}",
    dsol.rhs.has(sp.exp(IU * sp.Symbol("m") * ph)),
)

print("\nStep 2.  Highest weight: L_+ [chi(theta) e^{i phi}] = 0.")
expr_plus = sp.simplify(lp_polar(chi(th) * sp.exp(IU * ph)) * sp.exp(-2 * IU * ph))
print(f"  L_+ [chi e^(i phi)] = e^(2 i phi) * ({expr_plus})  => ODE: {expr_plus} = 0")
sol_plus = sp.dsolve(sp.Eq(expr_plus, 0), chi(th))
print(f"  dsolve => {sol_plus}")
C1 = sp.symbols("C1")
check(
    "E2",
    "L_+[chi e^{i phi}] = 0 gives chi = C sin(theta)",
    zero(sol_plus.rhs - C1 * sp.sin(th)),
)

print("\nStep 3.  Lowest weight: L_- [chi(theta) e^{-i phi}] = 0.")
expr_minus = sp.simplify(lm_polar(chi(th) * sp.exp(-IU * ph)) * sp.exp(2 * IU * ph))
print(
    f"  L_- [chi e^(-i phi)] = e^(-2 i phi) * ({expr_minus})  => ODE: {expr_minus} = 0"
)
sol_minus = sp.dsolve(sp.Eq(expr_minus, 0), chi(th))
print(f"  dsolve => {sol_minus}")
check(
    "E3",
    "L_-[chi e^{-i phi}] = 0 gives chi = C' sin(theta)",
    zero(sol_minus.rhs - C1 * sp.sin(th)),
)

print("\nNegative controls: the wrong annihilation conditions.")
expr_bad1 = sp.simplify(lm_polar(chi(th) * sp.exp(IU * ph)))
sol_bad1 = sp.dsolve(sp.Eq(expr_bad1, 0), chi(th))
expr_bad2 = sp.simplify(lp_polar(chi(th) * sp.exp(-IU * ph)))
sol_bad2 = sp.dsolve(sp.Eq(expr_bad2, 0), chi(th))
print(f"  L_- [chi e^(i phi)] = 0   => {sol_bad1}")
print(f"  L_+ [chi e^(-i phi)] = 0  => {sol_bad2}")
eps = sp.symbols("epsilon", positive=True)
div = sp.integrate(
    1 / sp.sin(th), (th, eps, sp.pi - eps)
)  # int |chi|^2 sin(theta) with chi = 1/sin
lim = sp.limit(sp.simplify(div), eps, 0)
print(
    f"  norm of chi = C/sin(theta): int |chi|^2 sin(theta) dtheta = int dtheta/sin(theta) = {sp.simplify(div)}  ->  {lim} as epsilon -> 0"
)
check(
    "E4",
    "NEGATIVE CONTROL: wrong annihilation conditions give chi = C/sin(theta), which is not normalisable",
    lim == sp.oo
    and zero(sol_bad1.rhs - C1 / sp.sin(th))
    and zero(sol_bad2.rhs - C1 / sp.sin(th)),
    "control",
)

print(
    "\nStep 4.  Normalise on S^2_r with the radial factor 1/r (so that Y' = Y(theta,phi)/r, as in Part B)."
)
C, Cp = sp.symbols("C Cp")
Y11d = C * sp.sin(th) * sp.exp(IU * ph)
Ym1d = Cp * sp.sin(th) * sp.exp(-IU * ph)
nrm = sp.simplify(
    sp.integrate(
        sp.integrate(
            sp.expand(Y11d * sp.conjugate(Y11d) * sp.sin(th)), (ph, 0, 2 * sp.pi)
        ),
        (th, 0, sp.pi),
    )
)
print(
    f"  int |Y11|^2 dOmega = {nrm}  =>  |C|^2 = 3/(8 pi),  |C| = sqrt(3/(8 pi))   (and likewise |C'|)"
)
absC = sp.sqrt(sp.Rational(3, 8) / sp.pi)
check(
    "E5",
    "normalisation fixes |C| = |C'| = sqrt(3/(8 pi))",
    zero(nrm.subs(C, absC) - 1)
    and zero(
        sp.simplify(
            sp.integrate(
                sp.integrate(
                    sp.expand(Ym1d * sp.conjugate(Ym1d) * sp.sin(th)),
                    (ph, 0, 2 * sp.pi),
                ),
                (th, 0, sp.pi),
            ).subs(Cp, absC)
            - 1
        )
    ),
)

print("\nStep 5.  Get Y(1,0) two ways and require agreement.")
Lm_Y11 = sp.simplify(lm_polar(Y11d))
Lp_Ym1 = sp.simplify(lp_polar(Ym1d))
print(f"  L_- Y11 = {Lm_Y11}      L_+ Y(1,-1) = {Lp_Ym1}")
nL = sp.simplify(
    sp.integrate(
        sp.integrate(
            sp.expand(sp.conjugate(Lm_Y11) * Lm_Y11 * sp.sin(th)), (ph, 0, 2 * sp.pi)
        ),
        (th, 0, sp.pi),
    ).subs(C, absC)
)
print(
    f"  ||L_- Y11||^2 = {nL}  => the normalised Y(1,0) is L_- Y11 / sqrt(2): the coefficient sqrt(2) is forced by the norm"
)
Y10_a = sp.simplify(Lm_Y11 / SQ2)
Y10_b = sp.simplify(Lp_Ym1 / SQ2)
print(
    f"  Y10 (route 1) = L_- Y11/sqrt2 = {Y10_a};   Y10 (route 2) = L_+ Y(1,-1)/sqrt2 = {Y10_b}"
)
eqn = sp.Eq(Y10_a, Y10_b)
relation = sp.solve(sp.simplify((Y10_a - Y10_b) / sp.cos(th)), Cp)
print(f"  routes agree iff C' = {relation}")
check(
    "E6",
    "taking both ladder coefficients +sqrt(2), the two routes give the same Y(1,0) only if C' = -C",
    relation == [-C],
)
_al = sp.symbols("alpha", real=True)
_Y10_b_al = sp.simplify(Lp_Ym1 / (SQ2 * sp.exp(IU * _al)))
_rel_al = sp.solve(sp.simplify((Y10_a - _Y10_b_al) / sp.cos(th)), Cp)
print(
    f"  If instead L_+ Y(1,-1) = sqrt2 e^(i alpha) Y(1,0): routes agree iff C' = {_rel_al}"
)
check(
    "E6c",
    "the relation C' = -C is conditional on the +sqrt(2) convention: with a phase e^(i alpha) it becomes C' = -C e^(i alpha)",
    len(_rel_al) == 1 and zero(sp.simplify(_rel_al[0] + C * sp.exp(IU * _al))),
)
check("E6b", "the norm of L_- Y11 is 2, so dividing by sqrt(2) is forced", zero(nL - 2))

print("\nStep 6.  What is fixed and what is a convention.")
print(
    "  * Fixed: chi_(1,+-1) ~ sin(theta); chi_(1,0) ~ cos(theta); |C| from the norm; C' = -C from the two routes, GIVEN that both ladder coefficients are taken +sqrt(2)."
)
print(
    "  * Convention: the overall phase of C (one phase per multiplet).  Requiring Y(1,0) > 0 at theta = 0 gives C < 0:"
)
Csol = None
for _s in (1, -1):
    _val = sp.simplify(Y10_a.subs(C, _s * absC).subs(th, 0))
    print(
        f"    sign test: C = {_s:+d}*|C| gives Y(1,0)(theta=0) = {_val}  (positive: {bool(sp.N(_val) > 0)})"
    )
    if sp.N(_val) > 0:
        Csol = _s * absC
assert Csol is not None
Cpsol = relation[0].subs(C, Csol)  # C' taken from the E6 relation, not typed by hand
Y11f = Y11d.subs(C, Csol)
Y10f = sp.simplify(Y10_a.subs(C, Csol))
Ym1f = Ym1d.subs(Cp, Cpsol)
print(
    f"    Y(1,1) = {sp.simplify(Y11f)};  Y(1,0) = {Y10f};  Y(1,-1) = {sp.simplify(Ym1f)}"
)
check(
    "E7",
    "the discovered harmonics equal the Part B harmonics (CS phase, equal to sympy Ynm)",
    zero(Y11f - y11) and zero(Y10f - y10) and zero(Ym1f - y1m1),
)
RES["partE"] = {"relation": str(relation), "norm_Lm_Y11": str(nL), "Y10": str(Y10f)}

# =======================================================================================
sec(
    "PART F  Independent numerical cross-check (quadrature + finite differences, no sympy)"
)
# =======================================================================================
rng = np.random.default_rng(220)
r0 = 2.0


def Ynum(m, x, y, z):
    rr2 = x * x + y * y + z * z
    c8n = np.sqrt(3 / (8 * np.pi))
    c4n = np.sqrt(3 / (4 * np.pi))
    if m == 1:
        return -c8n * (x + 1j * y) / rr2
    if m == 0:
        return c4n * z / rr2
    return c8n * (x - 1j * y) / rr2


def Lnum(comp, fun, p, h=1e-5):
    x, y, z = p

    def d(i):
        e = np.zeros(3)
        e[i] = h
        return (fun(*(p + e)) - fun(*(p - e))) / (2 * h)

    dx, dy, dz = d(0), d(1), d(2)
    if comp == "x":
        return 1j * (z * dy - y * dz)
    if comp == "y":
        return 1j * (x * dz - z * dx)
    return 1j * (y * dx - x * dy)


worst = 0.0
for _ in range(6):
    v = rng.normal(size=3)
    p = r0 * v / np.linalg.norm(v)
    for m in (1, 0, -1):

        def f(x, y, z, m=m):
            return Ynum(m, x, y, z)

        lp = Lnum("x", f, p) + 1j * Lnum("y", f, p)
        lm = Lnum("x", f, p) - 1j * Lnum("y", f, p)
        tp = np.sqrt(2) * Ynum(m + 1, *p) if m < 1 else 0.0
        tm = np.sqrt(2) * Ynum(m - 1, *p) if m > -1 else 0.0
        worst = max(worst, abs(lp - tp), abs(lm - tm))
print(
    f"  finite-difference check at 6 random points on S^2_(r=2): max |L_pm Y' - sqrt2 Y'_(m pm 1)| = {worst:.2e}"
)
check(
    "F1",
    "numerical Cartesian ladder action reproduces the sqrt(2) coefficients (|err| < 1e-7)",
    worst < 1e-7,
)


def gram_num(fa, fb):
    re = quad(
        lambda t, p: (np.conj(fa(*sph(t, p))) * fb(*sph(t, p))).real * r0**2 * np.sin(t)
    )
    im = quad(
        lambda t, p: (np.conj(fa(*sph(t, p))) * fb(*sph(t, p))).imag * r0**2 * np.sin(t)
    )
    return re + 1j * im


Gn = np.array(
    [
        [
            gram_num(
                lambda x, y, z, a=a: Ynum(a, x, y, z),
                lambda x, y, z, b=b: Ynum(b, x, y, z),
            )
            for b in (1, 0, -1)
        ]
        for a in (1, 0, -1)
    ]
)
print(f"  numerical Gram matrix of Y' on S^2_(r=2):\n{np.round(Gn, 9)}")
check(
    "F2",
    "numerical Gram matrix of the normalised complex harmonics = identity (|err| < 1e-8)",
    np.max(np.abs(Gn - np.eye(3))) < 1e-8,
)
raw_f = [
    lambda x, y, z: (x + 1j * y) / (x * x + y * y + z * z) ** 0.5,
    lambda x, y, z: z / (x * x + y * y + z * z) ** 0.5,
    lambda x, y, z: (x - 1j * y) / (x * x + y * y + z * z) ** 0.5,
]
diag_raw = [gram_num(f, f).real for f in raw_f]
ratio = [d / diag_raw[1] for d in diag_raw]
print(
    f"  numerical squared norms of (x+iy)/r, z/r, (x-iy)/r at r=2: {np.round(diag_raw, 8)}  ratio {np.round(ratio, 8)}"
)
check(
    "F3",
    "raw complex basis has squared-norm ratio 2 : 1 : 2",
    np.allclose(ratio, [2, 1, 2], atol=1e-8),
)

# =======================================================================================
sec(
    "PART F2  Numerical matrices in bases e and Y' (Gauss-Legendre quadrature + finite differences)"
)
# =======================================================================================
# Independent of sympy differentiation and integration; NOT independent of the definitions
# (the basis functions and the L convention are retyped above), so it can catch a calculus error,
# not a convention error.
_nu, _nphi = 24, 48
_xg, _wg = np.polynomial.legendre.leggauss(_nu)
_phis = np.linspace(0.0, 2 * np.pi, _nphi, endpoint=False)
_U, _PH = np.meshgrid(_xg, _phis, indexing="ij")
_S = np.sqrt(1 - _U**2)
PTS = r0 * np.stack([_S * np.cos(_PH), _S * np.sin(_PH), _U], axis=-1).reshape(-1, 3)
WTS = (np.outer(_wg, np.full(_nphi, 2 * np.pi / _nphi)) * r0**2).reshape(-1)


def vec_L(comp, fun, h=1e-5):
    x, y, z = PTS.T

    def d(i):
        e = np.zeros(3)
        e[i] = h
        return (fun(*(PTS + e).T) - fun(*(PTS - e).T)) / (2 * h)

    dx, dy, dz = d(0), d(1), d(2)
    if comp == "x":
        return 1j * (z * dy - y * dz)
    if comp == "y":
        return 1j * (x * dz - z * dx)
    return 1j * (y * dx - x * dy)


def num_matrix(opfun, basis):
    B = np.array([b(*PTS.T) for b in basis])
    LB = np.array([opfun(b) for b in basis])
    G = np.einsum("cn,bn,n->cb", B.conj(), B, WTS)
    H = np.einsum("cn,an,n->ca", B.conj(), LB, WTS)
    return (np.linalg.solve(G, H)).T


def _rr(x, y, z):
    return np.sqrt(x * x + y * y + z * z)


basis_e_num = [
    lambda x, y, z: (x + 1j * y) / _rr(x, y, z),
    lambda x, y, z: z / _rr(x, y, z),
    lambda x, y, z: (x - 1j * y) / _rr(x, y, z),
]
basis_y_num = [lambda x, y, z, m=m: Ynum(m, x, y, z) for m in (1, 0, -1)]
ops_num = {
    "Lp": lambda b: vec_L("x", b) + 1j * vec_L("y", b),
    "Lm": lambda b: vec_L("x", b) - 1j * vec_L("y", b),
    "Lz": lambda b: vec_L("z", b),
}
for tag, bnum, key in (("e", basis_e_num, kE), ("Y'", basis_y_num, kY)):
    worst_m = 0.0
    for opn, opf in ops_num.items():
        Mn = num_matrix(opf, bnum)
        Ms = np.array(mats[key][opn].evalf(), dtype=complex)
        worst_m = max(worst_m, float(np.max(np.abs(Mn - Ms))))
    print(
        f"  basis {tag}: max |M_numeric - M_symbolic| over L+, L-, Lz = {worst_m:.2e}"
    )
    check(
        f"F4-{tag}",
        f"numerical row-input matrices of L+, L-, Lz in basis {tag} equal the symbolic ones (|err| < 1e-7)",
        worst_m < 1e-7,
    )

# =======================================================================================
sec(
    "PART G  Cross-round consistency with the saved C205 / C206 results (loaded, not retyped)"
)
# =======================================================================================
_root = HERE.parent
c206 = json.loads(
    (
        _root
        / "20260923-c206-ladder-operators-polar-and-cartesian"
        / "results_c206.json"
    ).read_text(encoding="utf-8")
)
c205 = json.loads(
    (
        _root
        / "20260923-c205-cartesian-l1-derivation-tom-eq67-69"
        / "results_c205.json"
    ).read_text(encoding="utf-8")
)
cl = c206["part_d_explicit_matrices"]["complex_ladder"]
Mp_saved = sp.sympify(cl["L_plus_tom_row_input"])
Mm_saved = sp.sympify(cl["L_minus_tom_row_input"])
print(f"  C206 saved complex-ladder matrices: L+ = {Mp_saved};  L- = {Mm_saved}")
check(
    "G1",
    "this round's M(L+-) in basis e equal the matrices saved in C206 results",
    Mp_saved == mats[kE]["Lp"] and Mm_saved == mats[kE]["Lm"],
)
rb = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
Mrb_p, _ = matrix_of(lp_polar, rb)
Mrb_m, _ = matrix_of(lm_polar, rb)
Mrb_z, _ = matrix_of(lz_polar, rb)
Mrb = {
    "Lx": sp.simplify((Mrb_p + Mrb_m) / 2),
    "Ly": sp.simplify((Mrb_p - Mrb_m) / (2 * IU)),
    "Lz": Mrb_z,
}
saved_real = {
    k: sp.sympify(c205["step1_matrices"][f"M_{k}_tom_convention"])
    for k in ("Lx", "Ly", "Lz")
}
print(f"  this round, real basis (x,y,z)/r:  {Mrb}")
check(
    "G2",
    "this round's real-basis M(Lx), M(Ly), M(Lz) equal the matrices saved in C205 results",
    all(Mrb[k] == saved_real[k] for k in Mrb),
)
z_e = sp.Matrix(
    [[1, IU, 0], [0, 0, 1], [1, -IU, 0]]
)  # e = z_e * (x, y, z)/r : defined by the basis e itself
conj_saved = {k: sp.simplify(z_e * saved_real[k] * z_e.inv()) for k in saved_real}
print(
    f"  z M_saved z^-1 :  Lz = {conj_saved['Lz']};  Lx = {conj_saved['Lx']};  Ly = {conj_saved['Ly']}"
)
check(
    "G3",
    "the typed Gamma'(T12,T23,T31) equal z * (saved C205 real-basis matrices) * z^-1",
    conj_saved["Lz"] == G12 and conj_saved["Lx"] == G23 and conj_saved["Ly"] == G31,
)

# =======================================================================================
sec("SUMMARY")
# =======================================================================================
mains = [c for c in CHECKS if c[3] == "main"]
ctrls = [c for c in CHECKS if c[3] == "control"]
rests = [c for c in CHECKS if c[3] == "restatement"]
print(
    f"  independent main checks: {sum(c[2] for c in mains)}/{len(mains)} pass;  "
    f"negative controls: {sum(c[2] for c in ctrls)}/{len(ctrls)} behaved as required;  "
    f"restatements (not counted): {sum(c[2] for c in rests)}/{len(rests)} hold"
)
for cid, text, ok, kind in CHECKS:
    if not ok:
        print(f"  FAILED: {cid} {text} ({kind})")
RES["checks"] = [{"id": c[0], "text": c[1], "ok": c[2], "kind": c[3]} for c in CHECKS]
RES["all_main_pass"] = all(c[2] for c in mains)
RES["all_controls_ok"] = all(c[2] for c in ctrls)
RES["all_restatements_hold"] = all(c[2] for c in rests)
(HERE / "results_c220.json").write_text(
    json.dumps(RES, indent=2, ensure_ascii=False), encoding="utf-8"
)
print("  wrote results_c220.json")
