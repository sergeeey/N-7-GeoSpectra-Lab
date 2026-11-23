"""Final check of the Euler-angle derivation of the extra term (four items).

1. D(phi,theta,psi) and exact definitions of the LEFT (space-fixed) and RIGHT (body-fixed) generators.
2. Operators with d/d psi for the chosen phase convention, and the same statement in the opposite convention.
3. COMPLEX values of the ladder transitions (not only moduli), in the Euler picture and in the north / south charts.
4. Behaviour under rotations by 2 pi and 4 pi.

Predictions written BEFORE the run (derived from the definitions, not from the code):
  J_a D = -(sigma_a/2) D          K_a D = -D (sigma_a/2)         [J_a, J_b] = +i e_abc J_c     [K_a, K_b] = -i e_abc K_c
  J_a = -i X_a with X_a f(D) = d/de f(exp(-i e sigma_a/2) D);  K_a = -i Y_a with Y_a f(D) = d/de f(D exp(-i e sigma_a/2)).
  On sympy's D^j_{m'k'} (m' = -m, k' = -k):  J_+ F_m = -sqrt(j(j+1)-m(m+1)) F_{m+1},  J_- F_m = -sqrt(j(j+1)-m(m-1)) F_{m-1}
  (real and NEGATIVE; the minus is the left-multiplication sign) -- this also should explain C'=-C in C221.
  exp(-2 pi i J.n) = (-1)^{2j}, exp(-4 pi i J.n) = 1.
"""

import random

import numpy as np
import sympy as sp
from sympy.physics.quantum.spin import Rotation

th, ph, ps = sp.symbols("theta phi psi", real=True)
I = sp.I
R = sp.Rational
random.seed(17)
pts = [
    (random.uniform(0.4, 2.7), random.uniform(0.1, 6.0), random.uniform(0.1, 6.0)) for _ in range(8)
]
q = [ph, th, ps]
ALL_OK = True


def report(name, good):
    global ALL_OK
    ALL_OK &= bool(good)
    print("PASS" if good else "FAIL", name)


def ev(e, p):
    return complex(sp.N(sp.sympify(e).subs({th: p[0], ph: p[1], ps: p[2]}), 25))


def close(e, tol=1e-9):
    return all(abs(ev(e, p)) < tol for p in pts)


sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
SIG = {"x": sx, "y": sy, "z": sz}


def rot(axis, angle):
    return sp.cos(angle / 2) * sp.eye(2) - I * sp.sin(angle / 2) * axis


# ---------------------------------------------------------------- 1. D and the generators
D = rot(sz, ph) * rot(sy, th) * rot(sz, ps)
report(
    "1.0 D is unitary with det 1",
    close((D.H * D - sp.eye(2))[0, 0]) and close((D.H * D)[0, 1]) and close(D.det() - 1),
)


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
        assert sol, (side, name)
        out[name] = tuple(sp.simplify(sol[0][x]) for x in a)
    return out


FL, FR = fields("L"), fields("R")


def Jop(a, f):  # left / space-fixed:  J_a = -i X_a
    c = FL[a]
    return -I * (c[0] * sp.diff(f, ph) + c[1] * sp.diff(f, th) + c[2] * sp.diff(f, ps))


def Kop(a, f):  # right / body-fixed:  K_a = -i Y_a
    c = FR[a]
    return -I * (c[0] * sp.diff(f, ph) + c[1] * sp.diff(f, th) + c[2] * sp.diff(f, ps))


def Jp(f):
    return Jop("x", f) + I * Jop("y", f)


def Jm(f):
    return Jop("x", f) - I * Jop("y", f)


t = (
    sp.sin(th) ** 2 * sp.exp(I * (2 * ph + ps))
    + sp.cos(th / 2) * sp.exp(-I * ps / 2)
    + sp.sin(th) * sp.exp(-I * ph)
)

print("explicit generators (coefficients of d/dphi, d/dtheta, d/dpsi):")
for a in "xyz":
    print(f"  X_{a} (left)  =", FL[a])
for a in "xyz":
    print(f"  Y_{a} (right) =", FR[a])

report(
    "1.1 definition: J_a D_rc = -(sigma_a D / 2)_rc  for a = x, y, z and all entries",
    all(
        close(Jop(a, D[r, c]) + (SIG[a] * D / 2)[r, c])
        for a in "xyz"
        for r in range(2)
        for c in range(2)
    ),
)
report(
    "1.2 definition: K_a D_rc = -(D sigma_a / 2)_rc  for a = x, y, z and all entries",
    all(
        close(Kop(a, D[r, c]) + (D * SIG[a] / 2)[r, c])
        for a in "xyz"
        for r in range(2)
        for c in range(2)
    ),
)
report(
    "1.3 [J_x, J_y] = +i J_z (standard)",
    close(Jop("x", Jop("y", t)) - Jop("y", Jop("x", t)) - I * Jop("z", t)),
)
report(
    "1.4 [K_x, K_y] = -i K_z (body-fixed: anomalous sign)",
    close(Kop("x", Kop("y", t)) - Kop("y", Kop("x", t)) + I * Kop("z", t)),
)
report(
    "1.5 [J_a, K_b] = 0 for all 9 pairs",
    all(close(Jop(a, Kop(b, t)) - Kop(b, Jop(a, t))) for a in "xyz" for b in "xyz"),
)
J2 = lambda f: sum(Jop(a, Jop(a, f)) for a in "xyz")
K2 = lambda f: sum(Kop(a, Kop(a, f)) for a in "xyz")
report("1.6 Casimirs J^2 = K^2", close(J2(t) - K2(t)))
report(
    "1.7 J_z = -i d/dphi and K_z = -i d/dpsi",
    close(Jop("z", t) + I * sp.diff(t, ph)) and close(Kop("z", t) + I * sp.diff(t, ps)),
)

# ---------------------------------------------------------------- 2. phase convention
Kz = lambda f: Kop("z", f)
Jp_form = lambda f: (
    sp.exp(I * ph) * (sp.diff(f, th) + I * sp.cot(th) * sp.diff(f, ph) + Kz(f) / sp.sin(th))
)
Jm_form = lambda f: (
    sp.exp(-I * ph) * (-sp.diff(f, th) + I * sp.cot(th) * sp.diff(f, ph) + Kz(f) / sp.sin(th))
)
report(
    "2.1 convention A: J_+ = e^{i phi}(d_th + i cot d_ph - (i/sin) d_psi) = e^{i phi}(d_th + i cot d_ph + K_z/sin)",
    close(Jp(t) - Jp_form(t))
    and close(
        Jp(t)
        - sp.exp(I * ph)
        * (sp.diff(t, th) + I * sp.cot(th) * sp.diff(t, ph) - (I / sp.sin(th)) * sp.diff(t, ps))
    ),
)
report("2.2 convention A: J_- has the SAME sign of the K_z/sin term", close(Jm(t) - Jm_form(t)))

# convention B: psi_B = -psi (D_B = Rz(phi) Ry(theta) Rz(-psi_B)); function g(phi,theta,psi_B) = F(phi,theta,-psi_B)
psB = sp.symbols("psi_B", real=True)
g = sp.sin(th) ** 2 * sp.exp(I * (2 * ph + psB)) + sp.cos(th / 2) * sp.exp(-I * psB / 2)
F_of_psi = g.subs(psB, -ps)  # the same function written in the convention-A variable
lhs = Jp(F_of_psi).subs(ps, -psB)  # J_+ of convention A, then expressed in psi_B
rhs = sp.exp(I * ph) * (
    sp.diff(g, th) + I * sp.cot(th) * sp.diff(g, ph) + (I / sp.sin(th)) * sp.diff(g, psB)
)
ok_B = all(
    abs(complex(sp.N((lhs - rhs).subs({th: p[0], ph: p[1], psB: p[2]}), 25))) < 1e-9 for p in pts
)
report(
    "2.3 convention B (psi_B = -psi): the d/dpsi_B term flips sign (+i/sin), weight k_B = -k; K_z/sin unchanged",
    ok_B,
)
k_test = R(-1, 2)
Yt = sp.sin(th) ** 3 * sp.exp(2 * I * ph) + sp.cos(th / 2) * sp.exp(-I * ph)
report(
    "2.4 on e^{-i psi/2} Y (K_z = -1/2): J_+ = e^{i phi}(d_th + i cot d_ph - 1/(2 sin)) Y, i.e. c = -e^{i phi}/(2 sin theta)",
    close(
        Jp(sp.exp(I * k_test * ps) * Yt) * sp.exp(-I * k_test * ps)
        - sp.exp(I * ph)
        * (sp.diff(Yt, th) + I * sp.cot(th) * sp.diff(Yt, ph) - Yt / (2 * sp.sin(th)))
    ),
)

# ---------------------------------------------------------------- 3. complex ladder transitions
# 3a. convention fix at j = 1/2: sympy's D^{1/2} against our matrix D, entry by entry (complex)
half = R(1, 2)
idx = {half: 0, -half: 1}
report(
    "3.1 sympy Rotation.D(1/2, m, m') equals the matrix D entry by entry (complex values, same Euler convention)",
    all(
        close(Rotation.D(half, m1, m2, ph, th, ps).doit() - D[idx[m1], idx[m2]])
        for m1 in idx
        for m2 in idx
    ),
)


def Fm(j, m, k):
    return Rotation.D(j, -m, -k, ph, th, ps).doit()


def ratio(out, tgt):
    rs = []
    for p in pts:
        tv = ev(tgt, p)
        if abs(tv) > 1e-6:
            rs.append(ev(out, p) / tv)
    if len(rs) < 3:
        return None
    return rs[0] if max(abs(r - rs[0]) for r in rs) < 1e-8 * max(1, abs(rs[0])) else None


def chart_ops(chart, k):
    c = (lambda x: sp.tan(x / 2)) if chart == "N" else (lambda x: 1 / sp.tan(x / 2))
    cp = lambda Y: (
        sp.exp(I * ph) * (sp.diff(Y, th) + I * sp.cot(th) * sp.diff(Y, ph) + k * c(th) * Y)
    )
    cm = lambda Y: (
        sp.exp(-I * ph) * (-sp.diff(Y, th) + I * sp.cot(th) * sp.diff(Y, ph) + k * c(th) * Y)
    )
    return cp, cm


n_euler = n_N = n_S = 0
bad = []
for j in (R(1, 2), R(1), R(3, 2)):
    for k in [j - i for i in range(int(2 * j) + 1)]:
        ms = [j - i for i in range(int(2 * j) + 1)]
        cpN, cmN = chart_ops("N", k)
        cpS, cmS = chart_ops("S", k)
        for m in ms:
            src = Fm(j, m, k)
            srcN, srcS = (
                src.subs(ps, -ph),
                src.subs(ps, ph),
            )  # sections psi = -phi (north) and psi = +phi (south)
            for sgn, op, opN, opS, mt in ((+1, Jp, cpN, cpS, m + 1), (-1, Jm, cmN, cmS, m - 1)):
                if abs(mt) > j:
                    continue
                want = -sp.sqrt(
                    j * (j + 1) - m * (m + sgn)
                )  # complex prediction: real and negative
                tgt = Fm(j, mt, k)
                a_e = ratio(op(src), tgt)
                a_N = ratio(opN(srcN), tgt.subs(ps, -ph))
                a_S = ratio(opS(srcS), tgt.subs(ps, ph))
                for tag, a in (("euler", a_e), ("N", a_N), ("S", a_S)):
                    good = a is not None and abs(a - complex(sp.N(want))) < 1e-8
                    if tag == "euler":
                        n_euler += 1
                    elif tag == "N":
                        n_N += 1
                    else:
                        n_S += 1
                    if not good:
                        bad.append((j, m, k, sgn, tag, a, want))
report(
    f"3.2 complex ladder coefficient = -sqrt(j(j+1)-m(m+-1)) (real, negative): Euler picture {n_euler}, N chart {n_N}, S chart {n_S} transitions",
    not bad,
)
for b in bad[:6]:
    print("   mismatch:", b)

# 3c. dictionary spinor field <-> function on SU(2):  f(D) = <D e_2 | Psi(n(D))>,  and C221's pair
s2, c2 = sp.sin(th / 2), sp.cos(th / 2)
psi_up = sp.Matrix([-(s2**2), s2 * c2 * sp.exp(I * ph)])
psi_dn = sp.Matrix([s2 * c2 * sp.exp(-I * ph), -(c2**2)])
De2 = D * sp.Matrix([0, 1])


def f_of(Psi):
    return sp.expand((De2.H * Psi)[0, 0])


Lp_ = lambda g_: sp.exp(I * ph) * (sp.diff(g_, th) + I * sp.cot(th) * sp.diff(g_, ph))
Lm_ = lambda g_: sp.exp(-I * ph) * (-sp.diff(g_, th) + I * sp.cot(th) * sp.diff(g_, ph))
splus, sminus = sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([[0, 0], [1, 0]])
vec = lambda op, v: sp.Matrix([op(v[0]), op(v[1])])
JpPsi = lambda Psi: vec(Lp_, Psi) + splus * Psi
JmPsi = lambda Psi: vec(Lm_, Psi) + sminus * Psi
JzPsi = lambda Psi: vec(lambda g_: -I * sp.diff(g_, ph), Psi) + sz / 2 * Psi

f_up, f_dn = f_of(psi_up), f_of(psi_dn)
report(
    "3.3 dictionary is equivariant: <De2| J_+ Psi> = J_+ <De2|Psi>  (complex, both states)",
    close(f_of(JpPsi(psi_up)) - Jp(f_up)) and close(f_of(JpPsi(psi_dn)) - Jp(f_dn)),
)
report(
    "3.4 dictionary is equivariant for J_- and J_z",
    close(f_of(JmPsi(psi_up)) - Jm(f_up))
    and close(f_of(JmPsi(psi_dn)) - Jm(f_dn))
    and close(f_of(JzPsi(psi_up)) - Jop("z", f_up))
    and close(f_of(JzPsi(psi_dn)) - Jop("z", f_dn)),
)
report(
    "3.5 f_up = e^{-i psi/2} e^{i phi/2} sin(theta/2) and f_dn = -e^{-i psi/2} e^{-i phi/2} cos(theta/2)",
    close(f_up - sp.exp(-I * ps / 2) * sp.exp(I * ph / 2) * s2)
    and close(f_dn + sp.exp(-I * ps / 2) * sp.exp(-I * ph / 2) * c2),
)
report(
    "3.6 f_up = +D^{1/2}_{-1/2,1/2} and f_dn = -D^{1/2}_{1/2,1/2} (sympy, complex): the minus of C'=-C is the left-multiplication sign",
    close(f_up - Rotation.D(half, -half, half, ph, th, ps).doit())
    and close(f_dn + Rotation.D(half, half, half, ph, th, ps).doit()),
)
report(
    "3.7 pair of C221(b): J_- f_up = +1 * f_dn and J_+ f_dn = +1 * f_up (complex constants)",
    close(Jm(f_up) - f_dn) and close(Jp(f_dn) - f_up) and close(Jp(f_up)) and close(Jm(f_dn)),
)

# charts: amplitudes and their complex transition
YN_up, YN_dn = f_up.subs(ps, -ph), f_dn.subs(ps, -ph)
YS_up, YS_dn = f_up.subs(ps, ph), f_dn.subs(ps, ph)
report(
    "3.8 north chart (psi=-phi): Y^N_up = e^{i phi} sin(theta/2), Y^N_dn = -cos(theta/2)",
    close(YN_up - sp.exp(I * ph) * s2) and close(YN_dn + c2),
)
report(
    "3.9 south chart (psi=+phi): Y^S_up = sin(theta/2), Y^S_dn = -e^{-i phi} cos(theta/2)",
    close(YS_up - s2) and close(YS_dn + sp.exp(-I * ph) * c2),
)
report(
    "3.10 N -> S transition on the amplitudes: Y^S = e^{-i phi} Y^N (both states, complex)",
    close(YS_up - sp.exp(-I * ph) * YN_up) and close(YS_dn - sp.exp(-I * ph) * YN_dn),
)
k_ = R(-1, 2)
cpN, cmN = chart_ops("N", k_)
cpS, cmS = chart_ops("S", k_)
Ye_up, Ye_dn = (
    sp.exp(I * ph / 2) * s2,
    -sp.exp(-I * ph / 2) * c2,
)  # amplitudes in the single frame eta
cp_e = lambda Y: (
    sp.exp(I * ph) * (sp.diff(Y, th) + I * sp.cot(th) * sp.diff(Y, ph) - Y / (2 * sp.sin(th)))
)
cm_e = lambda Y: (
    sp.exp(-I * ph) * (-sp.diff(Y, th) + I * sp.cot(th) * sp.diff(Y, ph) - Y / (2 * sp.sin(th)))
)
report(
    "3.11 ladder constants are the SAME complex number (+1) in the eta frame, the N chart and the S chart",
    close(cm_e(Ye_up) - Ye_dn)
    and close(cp_e(Ye_dn) - Ye_up)
    and close(cp_e(Ye_up))
    and close(cm_e(Ye_dn))
    and close(cmN(YN_up) - YN_dn)
    and close(cmS(YS_up) - YS_dn)
    and close(cpN(YN_dn) - YN_up)
    and close(cpS(YS_dn) - YS_up)
    and close(cpN(YN_up))
    and close(cpS(YS_up))
    and close(cmN(YN_dn))
    and close(cmS(YS_dn)),
)

# ---------------------------------------------------------------- 4. rotations by 2 pi and 4 pi
report(
    "4.1 D(psi+2pi) = -D, D(phi+2pi) = -D, D(psi+4pi) = D (exact)",
    all(
        close((D.subs(ps, ps + 2 * sp.pi) + D)[r, c])
        and close((D.subs(ph, ph + 2 * sp.pi) + D)[r, c])
        and close((D.subs(ps, ps + 4 * sp.pi) - D)[r, c])
        for r in range(2)
        for c in range(2)
    ),
)
from scipy.linalg import expm

sig_np = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]]),
    np.array([[1, 0], [0, -1]], dtype=complex),
]
ok42 = True
for i in range(10):
    nv = np.random.default_rng(100 + i).normal(size=3)
    nv /= np.linalg.norm(nv)
    sn = sum(nv[a] * sig_np[a] for a in range(3))
    ok42 &= np.allclose(expm(-1j * 2 * np.pi * sn / 2), -np.eye(2), atol=1e-9)
    ok42 &= np.allclose(expm(-1j * 4 * np.pi * sn / 2), np.eye(2), atol=1e-9)
report(
    "4.2 matrix exponential: exp(-i 2pi sigma_n/2) = -1 and exp(-i 4pi sigma_n/2) = +1 for 10 random axes n",
    ok42,
)

n_ok = 0
n_all = 0
for j in (R(1, 2), R(1), R(3, 2), R(2)):
    for k in [j - i for i in range(int(2 * j) + 1)]:
        for m in [j - i for i in range(int(2 * j) + 1)]:
            F = Fm(j, m, k)
            n_all += 1
            sign = (-1) ** int(2 * j)
            ok1 = close(F.subs(ps, ps + 2 * sp.pi) - sign * F) and close(
                F.subs(ph, ph + 2 * sp.pi) - sign * F
            )
            ok2 = close(F.subs(ps, ps + 4 * sp.pi) - F) and close(F.subs(ph, ph + 4 * sp.pi) - F)
            n_ok += ok1 and ok2
report(
    f"4.3 Wigner functions: F(psi+2pi) = F(phi+2pi) = (-1)^(2j) F and the 4pi shift gives F, for j up to 2 ({n_all} functions)",
    n_ok == n_all,
)

rng = np.random.default_rng(5)
rep_ok = True
for j in (R(1, 2), R(1), R(3, 2)):
    for k in [j - i for i in range(int(2 * j) + 1)]:
        ms = [j - i for i in range(int(2 * j) + 1)]
        basis = [Fm(j, m, k) for m in ms]
        spts = pts
        A = np.array([[ev(b, p) for b in basis] for p in spts])
        Ms = {}
        for a in "xyz":
            B = np.array([[ev(Jop(a, b), p) for b in basis] for p in spts])
            coef, res, rank, sv = np.linalg.lstsq(A, B, rcond=None)
            rep_ok &= np.allclose(A @ coef, B, atol=1e-8)
            Ms[a] = coef
        rep_ok &= np.allclose(Ms["x"] @ Ms["y"] - Ms["y"] @ Ms["x"], 1j * Ms["z"], atol=1e-8)
        rep_ok &= np.allclose(
            Ms["x"] @ Ms["x"] + Ms["y"] @ Ms["y"] + Ms["z"] @ Ms["z"],
            float(j * (j + 1)) * np.eye(len(ms)),
            atol=1e-7,
        )
        for _ in range(6):
            nv = rng.normal(size=3)
            nv /= np.linalg.norm(nv)
            Mn = nv[0] * Ms["x"] + nv[1] * Ms["y"] + nv[2] * Ms["z"]
            w, V = np.linalg.eig(Mn)
            rep_ok &= np.allclose(sorted(w.real), sorted([float(m) for m in ms]), atol=1e-7)
            for ang, want in ((2 * np.pi, (-1) ** int(2 * j)), (4 * np.pi, 1)):
                U = V @ np.diag(np.exp(-1j * ang * w)) @ np.linalg.inv(V)
                rep_ok &= np.allclose(U, want * np.eye(len(ms)), atol=1e-7)
report(
    "4.4 matrices of J_a built from the operators on the (2j+1)-dim space: algebra, Casimir j(j+1), spectrum -j..j, and exp(-i 2pi J.n) = (-1)^(2j), exp(-i 4pi J.n) = 1 for random axes",
    rep_ok,
)

Yeta_up = sp.exp(I * ph / 2) * s2
report(
    "4.5 amplitudes: in the eta frame Y(phi+2pi) = -Y; in the N and S charts Y(phi+2pi) = +Y",
    close(Yeta_up.subs(ph, ph + 2 * sp.pi) + Yeta_up)
    and close(YN_up.subs(ph, ph + 2 * sp.pi) - YN_up)
    and close(YS_dn.subs(ph, ph + 2 * sp.pi) - YS_dn)
    and close(YN_dn.subs(ph, ph + 2 * sp.pi) - YN_dn),
)
report(
    "4.6 the spinor field Psi = Y eta is single-valued; the frame eta changes sign (so does Y), the product does not",
    all(
        close(psi_up[r].subs(ph, ph + 2 * sp.pi) - psi_up[r])
        and close(psi_dn[r].subs(ph, ph + 2 * sp.pi) - psi_dn[r])
        for r in range(2)
    ),
)
report(
    "4.7 the body-fixed generator: K_z e^{ik psi} = k e^{ik psi}; psi -> psi + 2 pi gives e^{2 pi i k} = -1 for half-integer k (frame sign flip)",
    close(Kop("z", sp.exp(-I * ps / 2)) + sp.exp(-I * ps / 2) / 2)
    and close(sp.exp(-I * (ps + 2 * sp.pi) / 2) + sp.exp(-I * ps / 2)),
)

print("ALL PASS" if ALL_OK else "SOME FAILED")
