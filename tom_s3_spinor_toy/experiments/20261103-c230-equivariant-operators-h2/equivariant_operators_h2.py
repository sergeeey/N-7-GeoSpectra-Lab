"""C230: which J-equivariant first-order operators on C^2-valued functions on S^2 preserve H2 = span{Psi, Phi}?

Setting (same objects as C228 `h2_j12_block.py`): J = L + sigma/2, L = -i x cross grad, Gamma = sigma.n,
A = 2(1 + sigma.L) is the transformed D0 of C228. Equivariant (commuting with J) first-order operators built from
sigma, n, L:   O = a + b (sigma.L) + c Gamma + d Gamma (sigma.L)        (a, b, c, d complex constants).

Predictions written BEFORE running (from Schur on the j = 1/2 multiplicity space with basis chi (l=0) and Gamma chi (l=1)):
  sigma.L = diag(0,-2), Gamma = swap, Gamma(sigma.L) = [[0,-2],[0,0]], so on that space
  O = [[a, c-2d], [c, a-2b]]; H2 corresponds to v = (-1, 1) (Psi = -chi/2 + Gamma chi/2);
  O preserves H2  <=>  v is an eigenvector  <=>  b + d = 0.  Then O Psi = (a - c - 2b) Psi (b = -d).
  D0-type A has (a,b,c,d) = (2,2,0,0): b + d = 2 != 0, not preserved (agrees with C228).
  The four operators span all 2x2 matrices on that space (so the family is complete on the j = 1/2 block).
Part 2: a constant matrix M added to A: solve (A + M)H2 within H2 exactly.
"""

import sys

import sympy as sp

th, ph = sp.symbols("theta phi", real=True)
I = sp.I
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
SIG = [sx, sy, sz]
Sm = sp.Matrix([[0, 0], [1, 0]])
FAILS = []


def Lp(f):
    return sp.exp(I * ph) * (sp.diff(f, th) + I * sp.cos(th) / sp.sin(th) * sp.diff(f, ph))


def Lm(f):
    return sp.exp(-I * ph) * (-sp.diff(f, th) + I * sp.cos(th) / sp.sin(th) * sp.diff(f, ph))


def Lz(f):
    return -I * sp.diff(f, ph)


def Lx(f):
    return (Lp(f) + Lm(f)) / 2


def Ly(f):
    return (Lp(f) - Lm(f)) / (2 * I)


LOPS = [Lx, Ly, Lz]


def comp(op, F):
    return sp.Matrix([op(F[0]), op(F[1])])


def sigL(F):
    return sum((SIG[k] * comp(LOPS[k], F) for k in range(3)), sp.zeros(2, 1))


n_vec = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
GAM = sum((n_vec[k] * SIG[k] for k in range(3)), sp.zeros(2))


def Gam(F):
    return GAM * F


def GsigL(F):
    return Gam(sigL(F))


def Jk(k, F):
    return comp(LOPS[k], F) + SIG[k] * F / 2


def Jm(F):
    return comp(Lm, F) + Sm * F


def op_family(a, b, c, d):
    return lambda F: a * F + b * sigL(F) + c * Gam(F) + d * GsigL(F)


def is_zero(M):
    """exact zero test for a matrix of trig expressions"""
    for e in M:
        e = sp.simplify(sp.expand(e.rewrite(sp.exp)))
        if e != 0:
            e = sp.simplify(e)
        if e != 0:
            return False
    return True


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def expect_caught(name, cond):
    print(("CAUGHT " if not cond else "MISSED ") + name)
    if cond:
        FAILS.append("self-control not caught: " + name)


# ---- 1. equivariance of the four building blocks, for generic F
f0 = sp.Function("f0")(th, ph)
f1 = sp.Function("f1")(th, ph)
Fg = sp.Matrix([f0, f1])
for name, op in (("1", lambda F: F), ("sigma.L", sigL), ("Gamma", Gam), ("Gamma sigma.L", GsigL)):
    ok = all(is_zero(op(Jk(k, Fg)) - Jk(k, op(Fg))) for k in range(3))
    check(f"[{name}, J_k] = 0 for generic F, k = x,y,z", ok)
# a non-equivariant control: bare L_z
check(
    "control: L_z alone does NOT commute with J_x (equivariance test can fail)",
    not is_zero(comp(Lz, Jk(0, Fg)) - Jk(0, comp(Lz, Fg))),
)

# ---- 2. multiplicity space of j = 1/2 (highest weight m = +1/2)
chi = sp.Matrix([1, 0])  # l = 0
gchi = Gam(chi)  # l = 1
check(
    "sigma.L chi = 0 and sigma.L (Gamma chi) = -2 Gamma chi",
    is_zero(sigL(chi)) and is_zero(sigL(gchi) + 2 * gchi),
)
check("Gamma Gamma chi = chi", is_zero(Gam(gchi) - chi))
Psi = sp.Matrix([-(1 - sp.cos(th)) / 2, sp.exp(I * ph) * sp.sin(th) / 2])
Phi = Jm(Psi)
check(
    "Psi = -chi/2 + Gamma chi/2 (the C228 highest-weight spinor)",
    is_zero(Psi - (-chi / 2 + gchi / 2)),
)
check("Gamma Psi = -Psi (Psi lies in ker(Gamma+1) pointwise)", is_zero(Gam(Psi) + Psi))

a, b, c, d = sp.symbols("a b c d")
O = op_family(a, b, c, d)
# matrix of O on {chi, Gamma chi}
Ochi = O(chi)
Ogchi = O(gchi)


def simp(e):
    return sp.simplify(sp.expand(sp.sympify(e).rewrite(sp.exp)))


def coeffs(vec):
    p, q = sp.symbols("p q")
    eq = sp.simplify(vec - p * chi - q * gchi)
    sol = sp.solve([sp.simplify(e) for e in eq], [p, q], dict=True)
    return (simp(sol[0][p]), simp(sol[0][q])) if sol else None


c1, c2 = coeffs(Ochi), coeffs(Ogchi)
mat = sp.Matrix([[c1[0], c2[0]], [c1[1], c2[1]]])
check(
    "matrix of O on {chi, Gamma chi} = [[a, c-2d],[c, a-2b]]",
    sp.simplify(mat - sp.Matrix([[a, c - 2 * d], [c, a - 2 * b]])) == sp.zeros(2),
)

basis_ops = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
Ms = []
for t in basis_ops:
    Oi = op_family(*t)
    e1, e2 = coeffs(Oi(chi)), coeffs(Oi(gchi))
    Ms.append(sp.Matrix([[e1[0], e2[0]], [e1[1], e2[1]]]).reshape(1, 4))
check(
    "the four operators span all 2x2 matrices on the j=1/2 multiplicity space (rank 4)",
    sp.Matrix.vstack(*Ms).rank() == 4,
)

# ---- 3. when is H2 preserved?
v = sp.Matrix([-1, 1])
Ov = mat * v
cond = sp.simplify(Ov[0] * v[1] - Ov[1] * v[0])  # zero iff v is an eigenvector
check(
    "v = (-1,1) is an eigenvector of O  <=>  b + d = 0 (determinant of [Ov, v])",
    sp.simplify(cond + 2 * (b + d)) == 0 or sp.simplify(cond - 2 * (b + d)) == 0,
)

# direct symbolic check on the actual functions, with b = -d
Obd = op_family(a, b, c, -b)
PsiO = Obd(Psi)
check("b = -d: O Psi = (a - c - 2b) Psi exactly", is_zero(PsiO - (a - c - 2 * b) * Psi))
PhiO = Obd(Phi)
check(
    "b = -d: O Phi = (a - c - 2b) Phi exactly (so H2 is invariant, with eigenvalue a - c - 2b)",
    is_zero(PhiO - (a - c - 2 * b) * Phi),
)

# A of C228 has (a,b,c,d) = (2,2,0,0): leak
A = op_family(2, 2, 0, 0)
# precise statement: the component outside H2 equals ((b+d)/2) * A Psi... verify: O Psi = (a-b-c+d) Psi + ((b+d)/2) (A Psi) with A = 2(1+sigma.L)
APsi = 2 * (Psi + sigL(Psi))
general = op_family(a, b, c, d)(Psi) - ((a - b - c + d) * Psi + (b + d) / 2 * APsi)
check("general O: O Psi = (a - b - c + d) Psi + ((b + d)/2) A Psi", is_zero(general))
# A Psi is orthogonal pointwise to H2 directions (lives in ker(Gamma - 1)), so it cannot be a combination of Psi, Phi
check(
    "A Psi lies in ker(Gamma - 1) pointwise (so it is not in span{Psi,Phi} unless zero)",
    is_zero(Gam(APsi) - APsi) and not is_zero(APsi),
)

# explicit positive example
Ostar = op_family(0, 1, 0, -1)  # (1 - Gamma) sigma.L
check(
    "example O* = (1 - Gamma) sigma.L preserves H2: O* Psi = -2 Psi, O* Phi = -2 Phi",
    is_zero(Ostar(Psi) + 2 * Psi) and is_zero(Ostar(Phi) + 2 * Phi),
)

# ---- 4. constant matrix M added to an operator (part 2)
m = sp.symbols("m0:4")
M = sp.Matrix([[m[0], m[1]], [m[2], m[3]]])
p, q, r, s = sp.symbols("p q r s")
unknowns = list(m) + [p, q, r, s]
pts = [
    (sp.pi / 3, 0),
    (sp.pi / 2, sp.pi / 2),
    (2 * sp.pi / 3, sp.pi),
    (sp.pi / 4, 3 * sp.pi / 2),
    (sp.pi / 2, 0),
    (sp.pi / 6, sp.pi / 3),
]


def const_M_system(Op):
    eqs = []
    for fvec, (x, y) in ((Psi, (p, q)), (Phi, (r, s))):
        res = Op(fvec) + M * fvec - x * Psi - y * Phi
        for t0, p0 in pts:
            for e in res:
                eqs.append(sp.expand(sp.simplify(e.subs({th: t0, ph: p0}))))
    return eqs


# control first: for O* (which preserves H2) the system must be solvable, and M = 0 must satisfy it
eqs_star = const_M_system(Ostar)
sol_star = sp.solve(eqs_star, unknowns, dict=True)
st = sol_star[0] if sol_star else {}
scalar_only = bool(sol_star) and st.get(m[1], None) == 0 and st.get(m[2], None) == 0 and sp.simplify(st.get(m[0], 1) - st.get(m[3], 2)) == 0
check(
    "control: for O* (which preserves H2) the system is solvable and its solutions are exactly M = lambda * 1 (m1 = m2 = 0, m0 = m3); M = 0 is among them",
    scalar_only,
)
print("  solution family for O*:", sol_star)

eqs_A = const_M_system(A)
sol_A = sp.solve(eqs_A, unknowns, dict=True)
print("  solutions of (A + M) H2 in H2 with M constant:", sol_A)
check(
    "no constant 2x2 matrix M makes (A + M) H2 invariant (sample-point system inconsistent)",
    sol_A == [],
)

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
