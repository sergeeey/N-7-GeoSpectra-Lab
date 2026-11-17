"""C243: for u in SU(2), u^T = sigma2 u^{-1} sigma2 and u^T e1 = i sigma2 u^{-1} e2; inversion on S^3 and left/right translations.

Exact sympy primary (a, b and their conjugates as independent symbols), numeric (numpy) secondary.
No correspondent's text is used. Negative controls are included on purpose:
  - the relation xi' = sigma3 conj(xi) between the two doublets of C242 is NOT a general SU(2) identity (holds for n3 = 0 only);
  - for ONE pair of doublets an SU(2) element mapping one to the other exists (SU(2) is transitive); what does not exist is a FIXED
    element realising the map xi_+(p) -> xi_-(p) at all points p, because the induced action on V would be in SO(3) and the
    required map V -> (-V1, V2, V3) has determinant -1.
"""

import numpy as np
import sympy as sp

passes = 0
fails = 0


def check(name, cond):
    global passes, fails
    ok = bool(cond)
    passes += ok
    fails += not ok
    print(f"{'PASS' if ok else 'FAIL'} {name}")


S = [
    np.array([[0, 1], [1, 0]], complex),
    np.array([[0, -1j], [1j, 0]], complex),
    np.array([[1, 0], [0, -1]], complex),
]
e1 = np.array([1, 0], complex)
e2 = np.array([0, 1], complex)
rng = np.random.default_rng(23)


def su2(x):
    """SU(2) element from a unit quaternion x = (x0, x1, x2, x3): x0 I + i x.sigma."""
    return x[0] * np.eye(2) + 1j * (x[1] * S[0] + x[2] * S[1] + x[3] * S[2])


def rand_su2():
    x = rng.normal(size=4)
    return su2(x / np.linalg.norm(x))


# ---- exact identities, a, b, conj a, conj b independent ----
a, b, ac, bc = sp.symbols("a b ac bc")
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
u = sp.Matrix([[a, -bc], [b, ac]])
ud = sp.Matrix([[ac, bc], [-b, a]])
c0 = a * ac + b * bc
check(
    "E1 u u^dagger = (a conj a + b conj b) I, so u^dagger = u^{-1} on the unit sphere",
    sp.simplify(u * ud - c0 * sp.eye(2)) == sp.zeros(2, 2),
)
check(
    "E2 u^T = sigma2 u^dagger sigma2 (identity in a, b, conj a, conj b)",
    sp.simplify(u.T - s2 * ud * s2) == sp.zeros(2, 2),
)
check(
    "E3 u^T e1 = i sigma2 u^dagger e2",
    sp.simplify(u.T * sp.Matrix([1, 0]) - sp.I * s2 * ud * sp.Matrix([0, 1])) == sp.zeros(2, 1),
)
check(
    "E3b conj(u) = sigma2 u sigma2 (the same fact for the conjugate matrix)",
    sp.simplify(u.conjugate() - s2 * u * s2) == sp.zeros(2, 2)
    or sp.simplify(sp.Matrix([[ac, -b], [bc, a]]) - s2 * u * s2) == sp.zeros(2, 2),
)

# ---- numeric secondary on random SU(2) ----
worst = 0.0
for _ in range(500):
    U = rand_su2()
    worst = max(
        worst,
        np.abs(U.T - S[1] @ np.linalg.inv(U) @ S[1]).max(),
        np.abs(U.T @ e1 - 1j * S[1] @ np.linalg.inv(U) @ e2).max(),
        np.abs(U.conj() - S[1] @ U @ S[1]).max(),
    )
check(f"E4 numeric, 500 random SU(2) elements, worst residual {worst:.1e} < 1e-12", worst < 1e-12)

# ---- inversion on S^3 ----
worst = 0.0
for _ in range(200):
    x = rng.normal(size=4)
    x /= np.linalg.norm(x)
    xi = np.array([x[0], -x[1], -x[2], -x[3]])
    worst = max(worst, np.abs(np.linalg.inv(su2(x)) - su2(xi)).max())
check(
    f"E5a g^{{-1}} has quaternion coordinates (x0, -x1, -x2, -x3) (worst {worst:.1e})",
    worst < 1e-12,
)
check(
    "E5b the map (x0, x1, x2, x3) -> (x0, -x1, -x2, -x3) has determinant -1: inversion reverses the orientation of S^3",
    round(np.linalg.det(np.diag([1.0, -1.0, -1.0, -1.0]))) == -1,
)
worst = 0.0
for _ in range(200):
    h, g, k = rand_su2(), rand_su2(), rand_su2()
    worst = max(
        worst,
        np.abs(
            np.linalg.inv(h @ g @ k) - np.linalg.inv(k) @ np.linalg.inv(g) @ np.linalg.inv(h)
        ).max(),
    )
check(
    f"E6 (h g k)^{{-1}} = k^{{-1}} g^{{-1}} h^{{-1}}: inversion turns left translation by h into right translation by h^{{-1}} (worst {worst:.1e})",
    worst < 1e-12,
)


# ---- negative controls ----
def xi_plus(t, f):
    return np.array([np.cos(t / 2), np.exp(1j * f) * np.sin(t / 2)])


def xi_minus(t, f):
    return np.array([np.cos(t / 2), -np.exp(-1j * f) * np.sin(t / 2)])


def Vof(x):
    return np.array([0.5 * (x.conj() @ si @ x).real for si in S])


def col_to_su2(x):
    return np.array([[x[0], -np.conj(x[1])], [x[1], np.conj(x[0])]])


worst = 0.0
for _ in range(200):
    t, f = rng.uniform(0.1, 3.0), rng.uniform(-3.1, 3.1)
    g = col_to_su2(xi_minus(t, f)) @ col_to_su2(xi_plus(t, f)).conj().T
    worst = max(
        worst,
        np.abs(g @ g.conj().T - np.eye(2)).max(),
        abs(np.linalg.det(g) - 1),
        np.abs(g @ xi_plus(t, f) - xi_minus(t, f)).max(),
    )
check(
    f"N1 for ONE pair (theta, phi) an SU(2) element g with g xi_+ = xi_- exists (SU(2) is transitive; worst {worst:.1e})",
    worst < 1e-12,
)

pts = [(0.9, 0.3), (1.7, 2.0), (2.4, -1.1)]
Vp = np.array([Vof(xi_plus(*p)) for p in pts]).T
Vm = np.array([Vof(xi_minus(*p)) for p in pts]).T
M = Vm @ np.linalg.inv(Vp)
check(
    "N2 three independent points fix the linear map V_+ -> V_- uniquely: M = diag(-1, 1, 1)",
    np.abs(M - np.diag([-1, 1, 1])).max() < 1e-12,
)
check(
    "N3 det M = -1, so M is not in SO(3): no FIXED SU(2) element realises xi_+(p) -> xi_-(p) at all points",
    round(np.linalg.det(M)) == -1,
)

worst0, worst3 = [], []
for _ in range(300):
    t = rng.uniform(0.2, 3.0)
    al = rng.uniform(0, 2 * np.pi)
    q = rng.normal(size=3)
    q /= np.linalg.norm(q)
    for n, lst in ((np.array([np.cos(al), np.sin(al), 0.0]), worst0), (q, worst3)):
        w, v = np.linalg.eigh(t / 2 * (n[0] * S[0] + n[1] * S[1] + n[2] * S[2]))
        U = (v * np.exp(1j * w)) @ v.conj().T
        lst.append(np.abs(U.T @ e1 - S[2] @ (U @ e1).conj()).max())
check(f"N4a xi' = sigma3 conj(xi) holds for n3 = 0 (worst {max(worst0):.1e})", max(worst0) < 1e-12)
check(
    f"N4b and fails for generic n3 (median residual {np.median(worst3):.2f}): not a general SU(2) identity",
    np.median(worst3) > 1e-2,
)

print(f"\n{passes} PASS, {fails} FAIL")
print("FAILS: none" if not fails else f"FAILS: {fails}")
