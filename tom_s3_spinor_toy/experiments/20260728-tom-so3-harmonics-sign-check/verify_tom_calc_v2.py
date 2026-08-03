"""More robust version: expand complex exponentials to sin/cos consistently
before comparing, and print actual residual vectors, not just booleans."""
import sympy as sp

theta, phi = sp.symbols('theta phi', real=True, positive=False)
I = sp.I  # noqa: E741

def Lx(f):
    return I*sp.sin(phi)*sp.diff(f, theta) + I*sp.cot(theta)*sp.cos(phi)*sp.diff(f, phi)

def Ly(f):
    return -I*sp.cos(phi)*sp.diff(f, theta) + I*sp.cot(theta)*sp.sin(phi)*sp.diff(f, phi)

def Lz(f):
    return -I*sp.diff(f, phi)

def canon(expr):
    """Expand exp(I*phi) into cos+I sin, then fully simplify."""
    e = expr.rewrite(sp.cos)
    e = sp.expand(e)
    e = sp.simplify(sp.expand_trig(e))
    return sp.nsimplify(sp.trigsimp(e))

def triplet(chi1_expr, chi0_expr, chim1_expr, opfunc):
    p1 = chi1_expr * sp.exp(I*phi)
    p0 = chi0_expr
    pm1 = chim1_expr * sp.exp(-I*phi)
    return sp.Matrix([canon(opfunc(p1)), canon(opfunc(p0)), canon(opfunc(pm1))])

def triplet_vec(chi1_expr, chi0_expr, chim1_expr):
    return sp.Matrix([chi1_expr*sp.exp(I*phi), chi0_expr, chim1_expr*sp.exp(-I*phi)])

Tpx_mat = sp.Matrix([[0,1,0],[sp.Rational(1,2),0,-sp.Rational(1,2)],[0,-1,0]])
Tpy_mat = sp.Matrix([[0,-I,0],[sp.Rational(1,2)*I,0,sp.Rational(1,2)*I],[0,-I,0]])
Tpz_mat = sp.diag(1,0,-1)

def Tp_actions(chi1_expr, chi0_expr, chim1_expr):
    v = triplet_vec(chi1_expr, chi0_expr, chim1_expr)
    ax = (Tpx_mat*v).applyfunc(canon)
    ay = (Tpy_mat*v).applyfunc(canon)
    az = (Tpz_mat*v).applyfunc(canon)
    return ax, ay, az

print("=== ORIGINAL (Tom's own choice: chi_1,1=+sin, chi_1,0=cos, chi_1,-1=+sin) ===")
Lx_o = triplet(sp.sin(theta), sp.cos(theta), sp.sin(theta), Lx)
Ly_o = triplet(sp.sin(theta), sp.cos(theta), sp.sin(theta), Ly)
Lz_o = triplet(sp.sin(theta), sp.cos(theta), sp.sin(theta), Lz)
Tpx_o, Tpy_o, Tpz_o = Tp_actions(sp.sin(theta), sp.cos(theta), sp.sin(theta))
print("Lx:", Lx_o.T)
print("T'x:", Tpx_o.T)
print("Lx + T'x (expect 0 if Lx=-T'x):", (Lx_o+Tpx_o).applyfunc(sp.simplify).T)
print()
print("Ly:", Ly_o.T)
print("T'y:", Tpy_o.T)
print("Ly - T'y (expect 0 if Ly=T'y):", (Ly_o-Tpy_o).applyfunc(sp.simplify).T)
print()
print("Lz:", Lz_o.T)
print("T'z:", Tpz_o.T)
print("Lz - T'z:", (Lz_o-Tpz_o).applyfunc(sp.simplify).T)
print()

print("=== CONDON-SHORTLEY FIX (chi_1,1 -> -sin, chi_1,0=cos, chi_1,-1=+sin) ===")
Lx_f = triplet(-sp.sin(theta), sp.cos(theta), sp.sin(theta), Lx)
Ly_f = triplet(-sp.sin(theta), sp.cos(theta), sp.sin(theta), Ly)
Lz_f = triplet(-sp.sin(theta), sp.cos(theta), sp.sin(theta), Lz)
Tpx_f, Tpy_f, Tpz_f = Tp_actions(-sp.sin(theta), sp.cos(theta), sp.sin(theta))
print("Lx - T'x (expect 0 if fix works, Lx=+T'x):", (Lx_f-Tpx_f).applyfunc(sp.simplify).T)
print("Ly - T'y (expect 0):", (Ly_f-Tpy_f).applyfunc(sp.simplify).T)
print("Lz - T'z (expect 0):", (Lz_f-Tpz_f).applyfunc(sp.simplify).T)
