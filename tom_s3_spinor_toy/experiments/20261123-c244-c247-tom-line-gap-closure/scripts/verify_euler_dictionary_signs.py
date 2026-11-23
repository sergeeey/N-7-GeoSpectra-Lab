"""Directed check of the sign question raised by an external review (2026-10-17).

Claim under test (review): "K_z(D e_2) = +1/2 but the report says K_z = -1/2 for the same state -- both cannot hold; and
J^Euler_+(D e_2) = (-1/sqrt2, 0) differs from J^lab_+ eta = (1/(2 sqrt2), -1/(2 sqrt2)); the correspondence is not shown."

Hypothesis (written before the run): they are different objects. The COLUMN D e_2 (a vector of functions) has K_z = +1/2 and
transforms in the DUAL representation, J_a(D e_2) = -(sigma_a/2) D e_2. The STATE of the report is the function
f(D) = <D e_2 | Psi(n(D))> = (D e_2)^dagger Psi, antilinear in the column, hence K_z = -1/2. The map Psi -> f is an intertwiner:
f(J^lab Psi) = J^Euler f for ARBITRARY two-component fields Psi, with J^lab = L + sigma/2. The un-conjugated pairing
sum_r D_{r2} Psi_r must NOT be an intertwiner (negative control). The review's two numbers should reproduce.
"""

import random

import sympy as sp

th, ph, ps = sp.symbols("theta phi psi", real=True)
I = sp.I
random.seed(23)
pts = [
    (random.uniform(0.4, 2.7), random.uniform(0.1, 6.0), random.uniform(0.1, 6.0)) for _ in range(8)
]
OK = True


def report(name, good):
    global OK
    OK &= bool(good)
    print("PASS" if good else "FAIL", name)


def ev(e, p):
    return complex(sp.N(sp.sympify(e).subs({th: p[0], ph: p[1], ps: p[2]}), 25))


def close(e, tol=1e-9):
    return all(abs(ev(e, p)) < tol for p in pts)


sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
SIG = {"x": sx, "y": sy, "z": sz}
splus = sp.Matrix([[0, 1], [0, 0]])


def rot(axis, angle):
    return sp.cos(angle / 2) * sp.eye(2) - I * sp.sin(angle / 2) * axis


D = rot(sz, ph) * rot(sy, th) * rot(sz, ps)
q = [ph, th, ps]


def fields(side):
    out = {}
    for name, sig in SIG.items():
        a = sp.symbols("a0:3")
        gen = -I * sig / 2
        target = gen * D if side == "L" else D * gen
        eqs = [
            sum(a[i] * sp.diff(D[r, c], q[i]) for i in range(3)) - target[r, c]
            for r in range(2)
            for c in range(2)
        ]
        sol = sp.solve(eqs, a, dict=True)
        out[name] = tuple(sp.simplify(sol[0][x]) for x in a)
    return out


FL, FR = fields("L"), fields("R")


def Jop(a, f):  # left generator, J_a = -i X_a
    c = FL[a]
    return -I * (c[0] * sp.diff(f, ph) + c[1] * sp.diff(f, th) + c[2] * sp.diff(f, ps))


def Kz(f):  # right generator K_z = -i Y_z, derived from the right action
    c = FR["z"]
    return -I * (c[0] * sp.diff(f, ph) + c[1] * sp.diff(f, th) + c[2] * sp.diff(f, ps))


col = D * sp.Matrix([0, 1])  # the column D e_2, a vector of two functions on SU(2)
eta = sp.Matrix([-sp.exp(-I * ph / 2) * sp.sin(th / 2), sp.exp(I * ph / 2) * sp.cos(th / 2)])

# ---- A. the column: K_z = +1/2, and D e_2 = e^{i psi/2} eta
report(
    "A1 D e_2 = e^{i psi/2} eta", all(close((col - sp.exp(I * ps / 2) * eta)[r]) for r in range(2))
)
report(
    "A2 K_z acting on the entries of the COLUMN D e_2 gives +1/2 (the review is right about this)",
    all(close(Kz(col[r]) - col[r] / 2) for r in range(2)),
)
report(
    "A3 the column transforms in the DUAL representation: J_a (D e_2) = -(sigma_a/2) D e_2 (a = x, y, z)",
    all(close(Jop(a, col[r]) + (SIG[a] * col / 2)[r]) for a in "xyz" for r in range(2)),
)

# ---- B. the state of the report: f = <D e_2 | Psi> = (D e_2)^dagger Psi  (antilinear in the column)
Y = sp.sin(th) ** 3 * sp.exp(2 * I * ph) + sp.cos(th / 2)  # arbitrary amplitude


def Phi(Psi):
    return sp.expand((col.H * Psi)[0, 0])


f_eta = Phi(Y * eta)
report("B1 Phi(Y eta) = e^{-i psi/2} Y", close(f_eta - sp.exp(-I * ps / 2) * Y))
report(
    "B2 K_z Phi(Y eta) = -1/2 Phi(Y eta): the STATE has weight -1/2, the column +1/2 (conjugation flips the sign)",
    close(Kz(f_eta) + f_eta / 2),
)
report(
    "B3 so the two statements are about different objects and do not contradict each other",
    bool(close(Kz(f_eta) + f_eta / 2) and all(close(Kz(col[r]) - col[r] / 2) for r in range(2))),
)

# ---- C. the review's two numbers
pt = {th: sp.pi / 2, ph: 0, ps: 0}
JpCol = sp.Matrix([Jop("x", col[r]) + I * Jop("y", col[r]) for r in range(2)])
vC = [complex(sp.N(JpCol[r].subs(pt), 20)) for r in range(2)]
print(
    f"   J^Euler_+ (D e_2) at theta=pi/2, phi=psi=0: ({vC[0]:.6f}, {vC[1]:.6f})   (review: (-1/sqrt2, 0) = (-0.707107, 0))"
)
report(
    "C1 the review's first number reproduces: (-1/sqrt2, 0)",
    abs(vC[0] + 2**-0.5) < 1e-9 and abs(vC[1]) < 1e-9,
)
report(
    "C2 and equals -sigma_+ (D e_2) (dual representation)",
    all(close((JpCol + splus * col)[r]) for r in range(2)),
)

Lp = lambda g: sp.exp(I * ph) * (sp.diff(g, th) + I * sp.cot(th) * sp.diff(g, ph))
Lm = lambda g: sp.exp(-I * ph) * (-sp.diff(g, th) + I * sp.cot(th) * sp.diff(g, ph))
vec = lambda op, v: sp.Matrix([op(v[0]), op(v[1])])
Jlab_eta = vec(Lp, eta) + splus * eta
vD = [complex(sp.N(Jlab_eta[r].subs(pt), 20)) for r in range(2)]
print(
    f"   J^lab_+ eta at the same point: ({vD[0]:.6f}, {vD[1]:.6f})   (review: (1/(2 sqrt2), -1/(2 sqrt2)) = (0.353553, -0.353553))"
)
report(
    "C3 the review's second number reproduces",
    abs(vD[0] - 0.5 * 2**-0.5) < 1e-9 and abs(vD[1] + 0.5 * 2**-0.5) < 1e-9,
)
c = -sp.exp(I * ph) / (2 * sp.sin(th))
report(
    "C4 J^lab_+ eta = c eta with c = -e^{i phi}/(2 sin theta)",
    all(close((Jlab_eta - c * eta)[r]) for r in range(2)),
)

# ---- D. the explicit map Phi is an intertwiner for ARBITRARY fields
g1 = sp.sin(th) * sp.exp(I * ph) + sp.cos(th / 2) ** 2 + sp.exp(-I * ph) * sp.sin(th / 2)
g2 = sp.sin(th / 2) * sp.exp(-2 * I * ph) + sp.cos(th) + I * sp.sin(th) * sp.exp(I * ph)
Psi = sp.Matrix([g1, g2])
Lx = lambda g: (Lp(g) + Lm(g)) / 2
Ly = lambda g: (Lp(g) - Lm(g)) / (2 * I)
Lz = lambda g: -I * sp.diff(g, ph)
Lgen = {"x": Lx, "y": Ly, "z": Lz}
okD = True
for a in "xyz":
    Jlab_Psi = vec(Lgen[a], Psi) + (SIG[a] / 2) * Psi
    okD &= close(Phi(Jlab_Psi) - Jop(a, Phi(Psi)))
report(
    "D1 Phi(J^lab_a Psi) = J^Euler_a Phi(Psi) for a = x, y, z, for an ARBITRARY two-component field Psi (complex, not only eigenstates)",
    okD,
)

# negative control: the un-conjugated pairing sum_r D_{r2} Psi_r is NOT an intertwiner
Phi_naive = sp.expand((col.T * Psi)[0, 0])
fails = 0
for a in "xyz":
    Jlab_Psi = vec(Lgen[a], Psi) + (SIG[a] / 2) * Psi
    d = sp.expand((col.T * Jlab_Psi)[0, 0]) - Jop(a, Phi_naive)
    fails += 0 if close(d) else 1
report(
    f"D2 control: the un-conjugated pairing fails to intertwine for {fails} of 3 axes (must be > 0)",
    fails > 0,
)

# ---- E. what the sign of the Wigner coefficient depends on (phase of the second state)
f_up = Phi(sp.Matrix([-(sp.sin(th / 2) ** 2), sp.sin(th / 2) * sp.cos(th / 2) * sp.exp(I * ph)]))
f_dn = Phi(sp.Matrix([sp.sin(th / 2) * sp.cos(th / 2) * sp.exp(-I * ph), -(sp.cos(th / 2) ** 2)]))
Jm_ = lambda f: Jop("x", f) - I * Jop("y", f)
alpha = sp.Rational(7, 10)
report("E1 J_- f_up = +f_dn for the Condon-Shortley pair of C221(b)", close(Jm_(f_up) - f_dn))
report(
    "E2 rephasing the lower state by e^{i alpha} multiplies the coefficient by e^{-i alpha}: the sign is a phase CONVENTION",
    close(Jm_(f_up) - sp.exp(-I * alpha) * (sp.exp(I * alpha) * f_dn))
    and not close(Jm_(f_up) - (-1) * (sp.exp(I * alpha) * f_dn)),
)

print("ALL PASS" if OK else "SOME FAILED")
