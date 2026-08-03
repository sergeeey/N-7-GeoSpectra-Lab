"""Build the FULL 3x3 matrices of Lx,Ly,Lz in the (psi_11,psi_10,psi_1,-1)
basis directly (apply to each basis function separately, decompose result
into the basis), then compare element-by-element against T'x,T'y,T'z."""
import sympy as sp

theta, phi = sp.symbols('theta phi', real=True)
I = sp.I  # noqa: E741

def Lx(f):
    return I*sp.sin(phi)*sp.diff(f, theta) + I*sp.cot(theta)*sp.cos(phi)*sp.diff(f, phi)
def Ly(f):
    return -I*sp.cos(phi)*sp.diff(f, theta) + I*sp.cot(theta)*sp.sin(phi)*sp.diff(f, phi)
def Lz(f):
    return -I*sp.diff(f, phi)

basis = [sp.sin(theta)*sp.exp(I*phi), sp.cos(theta), sp.sin(theta)*sp.exp(-I*phi)]  # psi_11, psi_10, psi_1,-1
labels = ["psi_1,1", "psi_1,0", "psi_1,-1"]

def decompose(result, basis):
    """Express result as a linear combo of basis functions -- solve for coefficients."""
    c1, c2, c3 = sp.symbols('c1 c2 c3')
    combo = c1*basis[0] + c2*basis[1] + c3*basis[2]
    diff = sp.expand_trig(sp.simplify(result - combo))
    # Try a few sample points to solve for c1,c2,c3 (result must be an exact combo, no residual)
    eqs = []
    for th_val, ph_val in [(sp.Rational(1,3), 0), (sp.Rational(1,3), sp.pi/4), (sp.Rational(2,3), sp.pi/3)]:
        eqs.append(diff.subs({theta: th_val, phi: ph_val}))
    sol = sp.solve(eqs, [c1, c2, c3])
    return sol

def build_matrix(opfunc):
    cols = []
    for b in basis:
        r = sp.expand(sp.simplify(opfunc(b).rewrite(sp.cos)))
        sol = decompose(r, basis)
        if not sol:
            cols.append(None)
        else:
            cols.append([sp.nsimplify(sol[sp.Symbol('c1')]), sp.nsimplify(sol[sp.Symbol('c2')]), sp.nsimplify(sol[sp.Symbol('c3')])])
    return cols

for name, op in [("Lx", Lx), ("Ly", Ly), ("Lz", Lz)]:
    cols = build_matrix(op)
    print(f"=== {name} matrix (columns = action on {labels}) ===")
    for i, c in enumerate(cols):
        print(f"  {labels[i]} ->", c)
    print()

Tpx = sp.Matrix([[0,1,0],[sp.Rational(1,2),0,sp.Rational(-1,2)],[0,-1,0]])
Tpy = sp.Matrix([[0,-I,0],[sp.Rational(1,2)*I,0,sp.Rational(1,2)*I],[0,-I,0]])
Tpz = sp.diag(1,0,-1)
print("T'x columns:", [list(Tpx[:,i]) for i in range(3)])
print("T'y columns:", [list(Tpy[:,i]) for i in range(3)])
print("T'z columns:", [list(Tpz[:,i]) for i in range(3)])
