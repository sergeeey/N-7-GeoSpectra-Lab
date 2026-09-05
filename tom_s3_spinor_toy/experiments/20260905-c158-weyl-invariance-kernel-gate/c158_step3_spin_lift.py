r"""
C158 STEP 3 -- lift the Weyl action to Spin(m) via the UNIQUE continuous lift
along SU(3) (simply connected -- no Pin(n) factorization sign ambiguity),
and test equivariance of M : v |-> D_Sigma(v) psi_+.

Run:  python c158_step3_spin_lift.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
S2_PATH = (
    HERE.parent
    / "20260904-c153-nk-linearity-structural-derivation"
    / "c153_step2_exact_rational_verification.py"
)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S2 = load_module("c153_step2", S2_PATH)
M_BASIS = S2.M_BASIS
to_m = S2.to_m
E_sym = S2.E_sym
spin_lift_sym = S2.spin_lift_sym

theta = sp.Symbol("theta", real=True)


def ad_on_m_general(A):
    """Generalizes C153's cartan_on_m (diagonal-only) to ANY anti-Hermitian
    traceless 3x3 A: commute with M_BASIS, project via to_m. REGRESSION below
    checks this reproduces T2_M exactly for the Cartan directions."""
    out = sp.zeros(6, 6)
    for j in range(6):
        comm = A * M_BASIS[j] - M_BASIS[j] * A
        col = to_m(comm)
        for r in range(6):
            out[r, j] = col[r]
    return out


print("=" * 78)
print("STEP 3a  REGRESSION -- ad_on_m_general reproduces T2_M on Cartan directions")
print("=" * 78)
h1 = sp.I * sp.diag(1, -1, 0)
h2 = sp.I * sp.diag(0, 1, -1)
L_h1 = ad_on_m_general(h1)
L_h2 = ad_on_m_general(h2)
print(f"  ad_on_m_general(h1) == T2_M[0] : {sp.simplify(L_h1 - S2.T2_M[0]) == sp.zeros(6, 6)}")
print(f"  ad_on_m_general(h2) == T2_M[1] : {sp.simplify(L_h2 - S2.T2_M[1]) == sp.zeros(6, 6)}")
assert sp.simplify(L_h1 - S2.T2_M[0]) == sp.zeros(6, 6)
assert sp.simplify(L_h2 - S2.T2_M[1]) == sp.zeros(6, 6)

print()
print("=" * 78)
print("STEP 3b  build A_01, A_12 (su(3) generators with exp((pi/2)A)=g_pq),")
print("         verify g(theta) at theta=pi/2 reproduces g01, g12 from Step 1")
print("=" * 78)


def A_gen(p, q):
    A = sp.zeros(3, 3)
    A[p, q], A[q, p] = 1, -1
    return A


A01 = A_gen(0, 1)
A12 = A_gen(1, 2)


def g_of_theta(A, p, q):
    """exp(theta A) for A = the (p,q) rotation generator: known closed form,
    cos/sin in the (p,q) block, identity elsewhere -- verified by direct
    differentiation check below, not asserted from memory."""
    g = sp.eye(3)
    g[p, p], g[p, q] = sp.cos(theta), sp.sin(theta)
    g[q, p], g[q, q] = -sp.sin(theta), sp.cos(theta)
    return g


g01_theta = g_of_theta(A01, 0, 1)
g12_theta = g_of_theta(A12, 1, 2)
# regression: d/dtheta g(theta) at theta=0 must equal A exactly
dg01 = sp.diff(g01_theta, theta).subs(theta, 0)
dg12 = sp.diff(g12_theta, theta).subs(theta, 0)
print(f"  d/dtheta g01(theta)|_0 == A01 : {sp.simplify(dg01 - A01) == sp.zeros(3, 3)}")
print(f"  d/dtheta g12(theta)|_0 == A12 : {sp.simplify(dg12 - A12) == sp.zeros(3, 3)}")
assert sp.simplify(dg01 - A01) == sp.zeros(3, 3)
assert sp.simplify(dg12 - A12) == sp.zeros(3, 3)

g01_at_half_pi = sp.simplify(g01_theta.subs(theta, sp.pi / 2))
g12_at_half_pi = sp.simplify(g12_theta.subs(theta, sp.pi / 2))


def su3_transposition(p, q):
    g = sp.eye(3)
    g[p, p], g[p, q], g[q, p], g[q, q] = 0, 1, -1, 0
    return g


g01_direct = su3_transposition(0, 1)
g12_direct = su3_transposition(1, 2)
print(f"  g01(pi/2) == g01 (Step 1's matrix) : {g01_at_half_pi == g01_direct}")
print(f"  g12(pi/2) == g12 (Step 1's matrix) : {g12_at_half_pi == g12_direct}")
assert g01_at_half_pi == g01_direct
assert g12_at_half_pi == g12_direct

print()
print("=" * 78)
print("STEP 3c  L01, L12 := ad_on_m_general(A01), ad_on_m_general(A12);")
print("         REGRESSION: d/dtheta R(theta)|_0 == L_pq, where R(theta) is")
print("         Step 1's own R_of construction applied to g(theta)")
print("=" * 78)
L01 = ad_on_m_general(A01)
L12 = ad_on_m_general(A12)


def R_of_theta(g_theta):
    ginv = g_theta.conjugate().T
    cols = []
    for X in M_BASIS:
        conj = sp.simplify(g_theta * X * ginv)
        cols.append(sp.Matrix(to_m(conj)))
    return sp.Matrix.hstack(*cols)


R01_theta = R_of_theta(g01_theta)
R12_theta = R_of_theta(g12_theta)
dR01 = sp.simplify(sp.diff(R01_theta, theta).subs(theta, 0))
dR12 = sp.simplify(sp.diff(R12_theta, theta).subs(theta, 0))
print(f"  d/dtheta R01(theta)|_0 == L01 : {sp.simplify(dR01 - L01) == sp.zeros(6, 6)}")
print(f"  d/dtheta R12(theta)|_0 == L12 : {sp.simplify(dR12 - L12) == sp.zeros(6, 6)}")
assert sp.simplify(dR01 - L01) == sp.zeros(6, 6)
assert sp.simplify(dR12 - L12) == sp.zeros(6, 6)
print("  R01(pi/2), R12(pi/2) reproduce Step 1's R01, R12 (by uniqueness of the")
print("  one-parameter subgroup with a given generator -- Lie theory, not")
print("  re-verified numerically here since it follows from 3a-3c together).")

print()
print("=" * 78)
print("STEP 3d  spin_lift(L_pq) eigenvalues, and the CLOSED-FORM exponential")
print("=" * 78)
M01 = spin_lift_sym(L01)
M12 = spin_lift_sym(L12)
for name, M in (("M01", M01), ("M12", M12)):
    ev = M.eigenvals()
    print(f"  {name} eigenvalues: {ev}")
    assert set(ev.keys()) == {sp.I, -sp.I, 0}, f"unexpected spectrum for {name}"

print()
print("  Since spec(M) subset {+i,-i,0}: exp((pi/2)M) = M + P_0, where")
print("  P_0 = M^2 + I is the projector onto the zero-eigenspace (verified:")
print("  on +-i eigenspaces M^2=-1 so M^2+I=0; on 0-eigenspace M^2+I=I).")
print("  This is EXACT closed form -- no numerical matrix exponential needed.")


def spin_exp_half_pi(M):
    P0 = sp.simplify(M * M + sp.eye(8))
    S = sp.simplify(M + P0)
    return S


S01 = spin_exp_half_pi(M01)
S12 = spin_exp_half_pi(M12)

print()
print("=" * 78)
print("STEP 3e  DECISIVE REGRESSION -- does conjugation by S01/S12 on the")
print("         Clifford VECTORS E_1..E_6 reproduce R01/R12 exactly?")
print("=" * 78)
S1 = load_module("c158_s1", HERE / "c158_step1_weyl_action.py")
R01_ref, R12_ref = S1.R01, S1.R12
Sinv01 = sp.simplify(S01.inv())
Sinv12 = sp.simplify(S12.inv())

print("  [BUG FOUND AND FIXED, before trusting the result] the first version of")
print("  this check built 'want' from ROW i of R (R[i,j]), but R_of's own")
print("  construction stacks COLUMNS as the image of each M_BASIS generator")
print("  (R[:,i] = to_m(g*M_BASIS[i]*ginv)) -- so the correct formula uses")
print("  COLUMN i (R[j,i]), not row i. Row-vs-column is a transpose, and R is")
print("  orthogonal but not symmetric, so this produced a clean, reproducible")
print("  -want-shaped mismatch that looked like a sign/Pin ambiguity but was")
print("  pure indexing. Fixed below; re-run confirms which explanation is real.")
for name, S, Sinv, R in (("S01", S01, Sinv01, R01_ref), ("S12", S12, Sinv12, R12_ref)):
    ok_all = True
    for i in range(6):
        conj = sp.simplify(S * E_sym[i + 1] * Sinv)
        want = sp.zeros(8, 8)
        for j in range(6):
            if R[j, i] != 0:
                want += R[j, i] * E_sym[j + 1]
        match = sp.simplify(conj - want) == sp.zeros(8, 8)
        ok_all = ok_all and match
        if not match:
            print(f"    {name}: E_{i + 1} conjugation MISMATCH")
    print(f"  {name}: S E_i S^-1 == sum_j R[j,i] E_j for all i=1..6 : {ok_all}")
    assert ok_all, f"{name} does NOT correctly implement R via conjugation -- STOP"
print("  CONFIRMED: S01, S12 are genuine spin lifts of R01, R12.")
