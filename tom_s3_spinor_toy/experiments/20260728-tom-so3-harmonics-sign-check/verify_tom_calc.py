"""Verify Tom Lawrence's 2026-07-28 PDF calculation: SO(3) generators vs
angular-momentum differential operators acting on the l=1 vector-harmonic
triplet. Checks his own arithmetic (eqs 9,11,13,17-29) and tests whether the
L_x sign discrepancy (eq 30: L_x = -T'_x) is explained by a missing
Condon-Shortley (-1)^m phase on chi_{1,1}.
"""
import sympy as sp

theta, phi = sp.symbols('theta phi', real=True)
I = sp.I  # noqa: E741

def Lx(f):
    return I*sp.sin(phi)*sp.diff(f, theta) + I*sp.cot(theta)*sp.cos(phi)*sp.diff(f, phi)

def Ly(f):
    return -I*sp.cos(phi)*sp.diff(f, theta) + I*sp.cot(theta)*sp.sin(phi)*sp.diff(f, phi)

def Lz(f):
    return -I*sp.diff(f, phi)

# Tom's own basis functions (eq 4, 7)
def psi(m, chi):
    return chi * sp.exp(I*m*phi)

# --- Step 1: reproduce his eq (9),(11),(13) symbolically with generic chi's ---
chi1, chi0, chim1 = sp.Function('chi1')(theta), sp.Function('chi0')(theta), sp.Function('chim1')(theta)
p1, p0, pm1 = psi(1, chi1), psi(0, chi0), psi(-1, chim1)

Lx1, Lx0, Lxm1 = sp.simplify(Lx(p1)), sp.simplify(Lx(p0)), sp.simplify(Lx(pm1))
Ly1, Ly0, Lym1 = sp.simplify(Ly(p1)), sp.simplify(Ly(p0)), sp.simplify(Ly(pm1))
Lz1, Lz0, Lzm1 = sp.simplify(Lz(p1)), sp.simplify(Lz(p0)), sp.simplify(Lz(pm1))

print("=== Step 1: generic chi check against his eqs (9),(11),(13) ===")
print("Lx psi_{1,1} :", Lx1)
print("Lx psi_{1,0} :", Lx0)
print("Lx psi_{1,-1}:", Lxm1)
print("Lz psi_{1,1} (expect = psi_{1,1}):", sp.simplify(Lz1 - p1) == 0)
print("Lz psi_{1,0} (expect = 0):", sp.simplify(Lz0) == 0)
print("Lz psi_{1,-1} (expect = -psi_{1,-1}):", sp.simplify(Lzm1 - (-pm1)) == 0)
print()

# --- Step 2: his specific choice, eq (25): chi_{1,1}=sin, chi_{1,0}=cos, chi_{1,-1}=sin ---
subs_tom = {chi1: sp.sin(theta), chi0: sp.cos(theta), chim1: sp.sin(theta)}

def eval_triplet(op):
    return sp.Matrix([sp.simplify(op(psi(1, sp.sin(theta))).subs(sp.Function('chi1')(theta), sp.sin(theta))) if False else None])

# Direct re-derivation instead of substitution gymnastics: build psi's directly with his chosen chi's
p1_tom = sp.sin(theta) * sp.exp(I*phi)
p0_tom = sp.cos(theta)
pm1_tom = sp.sin(theta) * sp.exp(-I*phi)

def triplet_op(opfunc):
    return sp.Matrix([sp.simplify(opfunc(p1_tom)), sp.simplify(opfunc(p0_tom)), sp.simplify(opfunc(pm1_tom))])

Lx_tom = triplet_op(Lx)
Ly_tom = triplet_op(Ly)
Lz_tom = triplet_op(Lz)

print("=== Step 2: his eq (25) choice -- reproduce his eqs (26),(27) ===")
print("Lx triplet:", Lx_tom.T)
print("Ly triplet:", Ly_tom.T)
print("Lz triplet:", Lz_tom.T)
print()

# His T'_x, T'_y, T'_z action (eq 28,29, and Tz'=diag(1,0,-1))
def Tprime_action(Tx_row_action, triplet):
    pass

Tpx_action = sp.Matrix([sp.cos(theta), I*sp.sin(phi)*sp.sin(theta), -sp.cos(theta)])           # his eq (28)
Tpy_action = sp.Matrix([-I*sp.cos(theta), I*sp.cos(phi)*sp.sin(theta), -I*sp.cos(theta)])        # his eq (29)
Tpz_action = sp.Matrix([p1_tom, 0, -pm1_tom])                                                    # T'_z = diag(1,0,-1)

print("=== Step 3: compare (his own claims eq 30, 31) ===")
print("Lx == -T'x ?", sp.simplify(Lx_tom - (-Tpx_action)) == sp.zeros(3,1))
print("Ly ==  T'y ?", sp.simplify(Ly_tom - Tpy_action) == sp.zeros(3,1))
print("Lz ==  T'z ?", sp.simplify(Lz_tom - Tpz_action) == sp.zeros(3,1))
print()

# --- Step 4: test Condon-Shortley fix: chi_{1,1} -> -sin(theta) (relative minus sign) ---
p1_fix = -sp.sin(theta) * sp.exp(I*phi)
p0_fix = sp.cos(theta)
pm1_fix = sp.sin(theta) * sp.exp(-I*phi)

def triplet_op_fix(opfunc):
    return sp.Matrix([sp.simplify(opfunc(p1_fix)), sp.simplify(opfunc(p0_fix)), sp.simplify(opfunc(pm1_fix))])

Lx_fix = triplet_op_fix(Lx)
Ly_fix = triplet_op_fix(Ly)
Lz_fix = triplet_op_fix(Lz)

# T' actions on the NEW (sign-fixed) triplet -- recompute using the same T'_x,T'_y matrix definitions
Tpm = sp.Matrix([[0,1,0],[sp.Rational(1,2),0,-sp.Rational(1,2)],[0,-1,0]])   # T'_x from eq (19)
Tpy_mat = sp.Matrix([[0,-I,0],[I/2,0,I/2],[0,-I,0]])                          # T'_y from eq (20)
Tpz_mat = sp.diag(1,0,-1)                                                     # T'_z from eq (21)

triplet_fix = sp.Matrix([p1_fix, p0_fix, pm1_fix])
Tpx_action_fix = Tpm * triplet_fix
Tpy_action_fix = Tpy_mat * triplet_fix
Tpz_action_fix = Tpz_mat * triplet_fix

print("=== Step 4: Condon-Shortley fix (chi_{1,1} -> -sin theta), re-test ===")
print("Lx == +T'x now?", sp.simplify(Lx_fix - Tpx_action_fix) == sp.zeros(3,1))
print("Lx == -T'x still?", sp.simplify(Lx_fix - (-Tpx_action_fix)) == sp.zeros(3,1))
print("Ly == +T'y ?", sp.simplify(Ly_fix - Tpy_action_fix) == sp.zeros(3,1))
print("Lz == +T'z ?", sp.simplify(Lz_fix - Tpz_action_fix) == sp.zeros(3,1))
