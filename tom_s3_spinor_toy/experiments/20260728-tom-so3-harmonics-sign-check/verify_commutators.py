"""Does Tom's own L_x,L_y,L_z (eqs 1-3) satisfy [Lx,Ly]=+iLz (standard) or
-iLz (opposite orientation)? This is checked as a pure differential-operator
identity on a generic test function -- the definitive test."""
import sympy as sp

theta, phi = sp.symbols('theta phi', real=True)
I = sp.I  # noqa: E741
f = sp.Function('f')(theta, phi)

def Lx(g):
    return I*sp.sin(phi)*sp.diff(g, theta) + I*sp.cot(theta)*sp.cos(phi)*sp.diff(g, phi)

def Ly(g):
    return -I*sp.cos(phi)*sp.diff(g, theta) + I*sp.cot(theta)*sp.sin(phi)*sp.diff(g, phi)

def Lz(g):
    return -I*sp.diff(g, phi)

comm_xy = sp.simplify(Lx(Ly(f)) - Ly(Lx(f)))
target_plus = sp.simplify(I*Lz(f))
target_minus = sp.simplify(-I*Lz(f))

print("[Lx,Ly]f =", comm_xy)
print()
print("[Lx,Ly] - (+i Lz)f =", sp.simplify(comm_xy - target_plus))
print("[Lx,Ly] - (-i Lz)f =", sp.simplify(comm_xy - target_minus))
print()

comm_yz = sp.simplify(Ly(Lz(f)) - Lz(Ly(f)))
print("[Ly,Lz] - (+i Lx)f =", sp.simplify(comm_yz - sp.simplify(I*Lx(f))))
print("[Ly,Lz] - (-i Lx)f =", sp.simplify(comm_yz - sp.simplify(-I*Lx(f))))
print()

comm_zx = sp.simplify(Lz(Lx(f)) - Lx(Lz(f)))
print("[Lz,Lx] - (+i Ly)f =", sp.simplify(comm_zx - sp.simplify(I*Ly(f))))
print("[Lz,Lx] - (-i Ly)f =", sp.simplify(comm_zx - sp.simplify(-I*Ly(f))))

# Also check T' matrices' own commutators for comparison
Tpx = sp.Matrix([[0,1,0],[sp.Rational(1,2),0,sp.Rational(-1,2)],[0,-1,0]])
Tpy = sp.Matrix([[0,-I,0],[sp.Rational(1,2)*I,0,sp.Rational(1,2)*I],[0,-I,0]])
Tpz = sp.diag(1,0,-1)
print()
print("[T'x,T'y] - i T'z:", sp.simplify(Tpx*Tpy - Tpy*Tpx - I*Tpz))
print("[T'y,T'z] - i T'x:", sp.simplify(Tpy*Tpz - Tpz*Tpy - I*Tpx))
print("[T'z,T'x] - i T'y:", sp.simplify(Tpz*Tpx - Tpx*Tpz - I*Tpy))
