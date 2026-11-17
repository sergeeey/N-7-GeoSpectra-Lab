"""C242: second component of the doublet representative, derived two ways, and the relation between two sign versions.

Exact sympy primary, numeric (numpy, matrix exponential) secondary. No correspondent's text is used.
INPUT assumptions, stated and not derived here:
  (R)  standard coordinates t1, t2 relate to spherical angles by sin(phi) = t1/th, cos(phi) = -t2/th, th = sqrt(t1^2 + t2^2)
  (N)  th * n = (t1, t2, 0) for the unit vector n in u = cos(th/2) I + i sin(th/2) n.sigma
Standard Pauli matrices, V^i = (1/2) xi^dagger sigma^i xi, xi = u (r, 0)^T.
"""

import numpy as np
import sympy as sp

th = sp.symbols("theta", positive=True)
ph = sp.symbols("phi", real=True)
r = sp.symbols("r", positive=True)
a = sp.symbols("alpha", real=True)
p1, p2 = sp.symbols("p1 p2")
S = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
c, s = sp.cos(th / 2), sp.sin(th / 2)
e1 = sp.Matrix([r, 0])
passes = 0
fails = 0


def check(name, cond):
    global passes, fails
    ok = bool(cond)
    passes += ok
    fails += not ok
    print(f"{'PASS' if ok else 'FAIL'} {name}")


def simp(m):
    return m.applyfunc(lambda z: sp.simplify(sp.expand_complex(z)))


def V(x):
    return sp.Matrix([sp.simplify(sp.expand_complex((x.H * si * x)[0] / 2)) for si in S])


cart = (r**2 / 2) * sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])

# ---- A: from a point on the 2-sphere ----
psi = sp.Matrix([p1, p2])
Vg = [sp.expand((psi.H * si * psi)[0] / 2) for si in S]
check(
    "A1 V1 + i V2 = conj(p1) p2",
    sp.simplify(sp.expand_complex(Vg[0] + sp.I * Vg[1] - sp.conjugate(p1) * p2)) == 0,
)
check(
    "A1b V3 = (1/2)(|p1|^2 - |p2|^2)",
    sp.simplify(sp.expand_complex(Vg[2] - (sp.conjugate(p1) * p1 - sp.conjugate(p2) * p2) / 2))
    == 0,
)
x2 = sp.symbols("x2")
sol = sp.solve(sp.Eq(r * c * x2, (r**2 / 2) * sp.sin(th) * sp.exp(sp.I * ph)), x2)
xiA = sp.Matrix([r * c, r * sp.exp(sp.I * ph) * s])
check(
    "A2 xi^1 = r cos(th/2) real: conj(xi^1) xi^2 = (r^2/2) sin th e^{i phi} has the unique solution xi^2 = r e^{i phi} sin(th/2)",
    len(sol) == 1 and sp.simplify(sol[0] - xiA[1]) == 0,
)
check(
    "A2b V(xi_A) = (r^2/2)(sin th cos ph, sin th sin ph, cos th)",
    simp(V(xiA) - cart) == sp.zeros(3, 1),
)
vs = sp.sin(th) * sp.cos(ph) * S[0] + sp.sin(th) * sp.sin(ph) * S[1] + sp.cos(th) * S[2]
check(
    "A3 (v.sigma) xi_A = xi_A and xi xi^dagger = (r^2/2)(I + v.sigma)",
    simp(vs * xiA - xiA) == sp.zeros(2, 1)
    and simp(xiA * xiA.H - (r**2 / 2) * (sp.eye(2) + vs)) == sp.zeros(2, 2),
)

# ---- B: from the group element u ----
n1, n2 = sp.cos(a), sp.sin(a)
ug = c * sp.eye(2) + sp.I * s * (n1 * S[0] + n2 * S[1])
check(
    "B1 u_21 = i s (n1 + i n2) and u_12 = i s (n1 - i n2)",
    sp.simplify(ug[1, 0] - sp.I * s * (n1 + sp.I * n2)) == 0
    and sp.simplify(ug[0, 1] - sp.I * s * (n1 - sp.I * n2)) == 0,
)
nR = (sp.sin(ph), -sp.cos(ph))  # (N) with (R)
uR = c * sp.eye(2) + sp.I * s * (nR[0] * S[0] + nR[1] * S[1])
check(
    "B2 u unitary with det 1",
    simp(uR * uR.H - sp.eye(2)) == sp.zeros(2, 2) and sp.simplify(uR.det()) == 1,
)
check("B3 u (r,0)^T = xi_A (with R and N)", simp(uR * e1 - xiA) == sp.zeros(2, 1))
Vgen = V(ug * e1)
tgt = sp.Matrix([-n2 * sp.sin(th), n1 * sp.sin(th), sp.cos(th)]) * r**2 / 2
check(
    "B4 any unit n = (n1, n2, 0): V = (r^2/2)(-n2 sin th, n1 sin th, cos th)",
    simp(Vgen - tgt) == sp.zeros(3, 1),
)
check(
    "B5a (t1 + i t2)/th = sin ph - i cos ph = -i e^{i ph}",
    sp.simplify(sp.expand_complex(sp.sin(ph) - sp.I * sp.cos(ph) + sp.I * sp.exp(sp.I * ph))) == 0,
)
check(
    "B5b (t1 - i t2)/th = sin ph + i cos ph = i e^{-i ph}",
    sp.simplify(sp.expand_complex(sp.sin(ph) + sp.I * sp.cos(ph) - sp.I * sp.exp(-sp.I * ph))) == 0,
)

# ---- C: the second sign version and its relation to the first ----
xiP = sp.Matrix([r * c, sp.I * r * s * (sp.sin(ph) + sp.I * sp.cos(ph))])  # (t1 - i t2)/th with (R)
check(
    "C1 xi' second component = -r e^{-i phi} sin(th/2)",
    sp.simplify(sp.expand_complex(xiP[1] + r * sp.exp(-sp.I * ph) * s)) == 0,
)
check(
    "C2 V(xi') = (-V1, V2, V3) of the standard vector",
    simp(V(xiP) - sp.diag(-1, 1, 1) * cart) == sp.zeros(3, 1),
)
check("C3 xi' = u^T (r,0)^T for n = (t1, t2)/th", simp(xiP - uR.T * e1) == sp.zeros(2, 1))
uM = c * sp.eye(2) + sp.I * s * (nR[0] * S[0] - nR[1] * S[1])  # n = (t1, -t2)/th
check("C3b xi' = u (r,0)^T for n = (t1, -t2)/th", simp(xiP - uM * e1) == sp.zeros(2, 1))
check("C4 xi' = sigma3 conj(xi_A)", simp(xiP - S[2] * xiA.conjugate()) == sp.zeros(2, 1))
check(
    "C5a conjugation alone: V -> diag(1,-1,1) V",
    simp(V(xiA.conjugate()) - sp.diag(1, -1, 1) * cart) == sp.zeros(3, 1),
)
i3 = sp.I * S[2]
check(
    "C5b i sigma3 is in SU(2) (det 1) and acts on V as diag(-1,-1,1)",
    sp.simplify(i3.det()) == 1 and simp(V(i3 * xiA) - sp.diag(-1, -1, 1) * cart) == sp.zeros(3, 1),
)
check("C5c det diag(-1,1,1) = -1", sp.diag(-1, 1, 1).det() == -1)
check(
    "C6 xi' = conj(u^{-1}) (r,0)^T, and conj(u) = (u^{-1})^T",
    simp(xiP - uR.inv().conjugate() * e1) == sp.zeros(2, 1)
    and simp(uR.conjugate() - uR.inv().T) == sp.zeros(2, 2),
)
check(
    "C7 phi = 0: u is the real matrix [[c, -s], [s, c]] and xi = r (c, s) while xi' = r (c, -s)",
    simp(uR.subs(ph, 0) - sp.Matrix([[c, -s], [s, c]])) == sp.zeros(2, 2)
    and simp(xiA.subs(ph, 0) - r * sp.Matrix([c, s])) == sp.zeros(2, 1)
    and simp(xiP.subs(ph, 0) - r * sp.Matrix([c, -s])) == sp.zeros(2, 1),
)
check(
    "C8 phi = pi/2: both versions coincide",
    simp(xiA.subs(ph, sp.pi / 2) - xiP.subs(ph, sp.pi / 2)) == sp.zeros(2, 1),
)

# ---- numeric secondary: matrix exponential, no closed form for u ----
rng = np.random.default_rng(11)
Sn = [np.array(m.tolist(), dtype=complex) for m in S]
worst = 0.0
for _ in range(500):
    t, f, rr = rng.uniform(0.05, np.pi - 0.05), rng.uniform(-np.pi, np.pi), rng.uniform(0.5, 3)
    t1, t2 = t * np.sin(f), -t * np.cos(f)
    n = np.array([t1, t2, 0]) / t
    H = t / 2 * (n[0] * Sn[0] + n[1] * Sn[1])
    w, vv = np.linalg.eigh(H)
    u = (vv * np.exp(1j * w)) @ vv.conj().T
    xi = u @ np.array([rr, 0])
    Vn = lambda x: np.array([0.5 * (x.conj() @ si @ x).real for si in Sn])
    std = (rr**2 / 2) * np.array([np.sin(t) * np.cos(f), np.sin(t) * np.sin(f), np.cos(t)])
    xip = np.array([rr * np.cos(t / 2), 1j * rr * np.sin(t / 2) * (t1 - 1j * t2) / t])
    worst = max(
        worst,
        np.abs(Vn(xi) - std).max(),
        np.abs(Vn(xip) - std * np.array([-1, 1, 1])).max(),
        np.abs(xip - Sn[2] @ xi.conj()).max(),
        np.abs(xip - u.T @ np.array([rr, 0])).max(),
    )
check(f"N1 numeric, 500 random points, worst abs residual {worst:.1e} < 1e-12", worst < 1e-12)

print(f"\n{passes} PASS, {fails} FAIL")
print("FAILS: none" if not fails else f"FAILS: {fails}")
