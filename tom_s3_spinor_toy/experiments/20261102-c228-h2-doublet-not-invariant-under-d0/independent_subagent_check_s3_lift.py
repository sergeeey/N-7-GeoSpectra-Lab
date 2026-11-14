"""Independent R14 test: lift Psi, Phi to S^3 by (T psi)(g) = g^dag psi(pi(g)), apply D0 directly on S^3,
project onto span{T Psi, T Phi} with exact L2(S^3) monomial integrals. Plus premise checks on S^2.
"""

import itertools
import sympy as sp

X = sp.symbols("x0:4", real=True)
I = sp.I
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
x, y, z = sp.symbols("x y z", real=True)
r = [x, y, z]


def Lop(f, sign=1):
    # L = -i r x grad  (sign=-1 gives the flipped convention L = +i r x grad)
    gr = [sp.diff(f, v) for v in r]
    cr = [r[1] * gr[2] - r[2] * gr[1], r[2] * gr[0] - r[0] * gr[2], r[0] * gr[1] - r[1] * gr[0]]
    return [sp.expand(-I * sign * c) for c in cr]


def Lvec(F, sign=1):  # componentwise L on a C^2 spinor; returns list of 3 spinors
    out = [sp.zeros(2, 1) for _ in range(3)]
    for c in range(2):
        l = Lop(F[c], sign)
        for k in range(3):
            out[k][c] = l[k]
    return out


Psi = sp.Matrix([-(1 - z) / 2, (x + I * y) / 2])
Gam = x * sig[0] + y * sig[1] + z * sig[2]
Sm = (sig[0] - I * sig[1]) / 2


def onS2(e):
    return sp.simplify(sp.expand(e).subs(z**2, 1 - x**2 - y**2))


def Jm(F, sign=1):
    L = Lvec(F, sign)
    return (L[0] - I * L[1] + Sm * F).applyfunc(sp.expand)


Phi = Jm(Psi)
print("Phi =", list(Phi))
print("Gamma Psi + Psi on S2:", [onS2(e) for e in (Gam * Psi + Psi)])
print("Gamma Phi + Phi on S2:", [onS2(e) for e in (Gam * Phi + Phi)])
Phi_flip = Jm(Psi, sign=-1)
print(
    "flipped-L convention: Gamma Phi' + Phi' on S2:", [onS2(e) for e in (Gam * Phi_flip + Phi_flip)]
)


def A_S2(F):
    L = Lvec(F)
    sL = sig[0] * L[0] + sig[1] * L[1] + sig[2] * L[2]
    return (2 * (F + sL)).applyfunc(sp.expand)


# Theorem D on a generic polynomial spinor
G = sp.Matrix([x * y + 2 * z**2 - I * x, 3 * y - z * x + I * y * z])
anti = A_S2(Gam * G) + Gam * A_S2(G)
print("{A,Gamma} G on S2 (should be 0):", [onS2(e) for e in anti])

# ---- lift to S^3 ----
g = X[0] * sp.eye(2) + I * (X[1] * sig[0] + X[2] * sig[1] + X[3] * sig[2])
P = (g * sig[2] * g.H).applyfunc(sp.expand)
n = [sp.expand(sp.re(P[0, 1])), sp.expand(-sp.im(P[0, 1])), sp.expand(P[0, 0])]  # P = n.sigma
sub = {x: n[0], y: n[1], z: n[2]}


def T(F):
    return (g.H * F.subs(sub, simultaneous=True)).applyfunc(sp.expand)


def XR(a, f):
    M = g * (-I * sig[a])
    # coords: x0 = Re M00, x3 = Im M00 ; M01 = i x1 + x2 -> x1 = Im M01, x2 = Re M01
    v = [sp.re(M[0, 0]), sp.im(M[0, 1]), sp.re(M[0, 1]), sp.im(M[0, 0])]
    return sp.expand(sum(sp.expand(v[j]) * sp.diff(f, X[j]) for j in range(4)))


def D0(F):
    out = sp.zeros(2, 1)
    for a in range(3):
        out += -I * sig[a] * sp.Matrix([XR(a, F[0]), XR(a, F[1])])
    return out.applyfunc(sp.expand)


def J3(F):
    return (sp.Matrix([XR(2, F[0]), XR(2, F[1])]) - I * sig[2] * F).applyfunc(sp.expand)


def integ(f):  # exact integral over unit S^3 of a polynomial (normalised to vol=1)
    f = sp.expand(f)
    if f == 0:
        return 0
    tot = 0
    for mon, c in sp.Poly(f, *X).as_dict().items():
        if any(e % 2 for e in mon):
            continue
        val = (
            2
            * sp.prod([sp.gamma(sp.Rational(e + 1, 2)) for e in mon])
            / sp.gamma(sp.Rational(sum(mon) + 4, 2))
        )
        tot += c * val
    return sp.nsimplify(tot / (2 * sp.pi**2))


def ip(F, H):
    return sp.simplify(integ(sp.expand(sum(sp.conjugate(F[c]) * H[c] for c in range(2)))))


F1, F2 = T(Psi), T(Phi)
print("J3 T Psi =", list(J3(F1)), " J3 T Phi =", list(J3(F2)))
B = [F1, F2]
Gm = sp.Matrix(2, 2, lambda i, j: ip(B[i], B[j]))
print("Gram =", Gm)
for name, F in (("TPsi", F1), ("TPhi", F2)):
    DF = D0(F)
    b = sp.Matrix([ip(B[0], DF), ip(B[1], DF)])
    coef = Gm.inv() * b
    proj = coef[0] * F1 + coef[1] * F2
    R = (DF - proj).applyfunc(sp.expand)
    print(
        f"{name}: projection coeffs = {list(coef)}, ||D0F||^2/||F||^2 = {sp.simplify(ip(DF, DF) / ip(F, F))}, "
        f"||residual||^2/||F||^2 = {sp.simplify(ip(R, R) / ip(F, F))}"
    )
# control: a genuine eigenvector on S^3 must give residual 0 with the same code: constant spinor (D0 c = 0)
c0 = sp.Matrix([1, 0])
DF = D0(c0)
print("control constant spinor: D0 c =", list(DF))
# control 2: D0-invariant 2-dim space: span{T(e1), T(e2)}-type? use l=0 constant psi on S2: T psi lies in A=+2 eigenspace
cpsi = sp.Matrix([1, 0])
Fc = T(cpsi)
DFc = D0(Fc)
print("control T(const): D0 T c - 3 T c =", [sp.simplify(e) for e in (DFc - 3 * Fc)])
