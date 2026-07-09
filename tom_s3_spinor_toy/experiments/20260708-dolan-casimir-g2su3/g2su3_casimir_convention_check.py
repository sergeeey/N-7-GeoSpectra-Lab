"""
Round 14 continuation (2026-07-09): resolve the C_2(G2;7)=2-vs-4 puzzle
by computing G2's Casimir eigenvalues DIRECTLY from the root system, in
the standard "long roots have length^2=2" convention (the convention
implicitly used throughout this whole experiment, since it's the one
that made su(3)'s adjoint Casimir come out to the textbook value 3).

This sidesteps needing to know exactly what convention Agricola 2002
used -- it independently re-derives the RIGHT-HAND-SIDE numbers from
first principles (Weyl dimension formula + Casimir formula), so we can
check which Dynkin label (1,0) or (0,1) gives dim=7 vs dim=14, and what
C_2 each carries in this convention.
"""
import sympy as sp

# G2 simple roots: alpha1 = SHORT, alpha2 = LONG (standard Bourbaki-ish labeling)
# long root^2 = 2  =>  short root^2 = 2/3 (ratio 3:1 for G2)
a1_sq = sp.Rational(2, 3)   # short
a2_sq = sp.Rational(2)      # long
# Cartan matrix A_ij = 2(ai,aj)/(aj,aj), standard G2: A = [[2,-1],[-3,2]]
A = sp.Matrix([[2, -1], [-3, 2]])
a1_dot_a2 = sp.Rational(-1) * a2_sq / 2   # from A12 = 2(a1,a2)/(a2,a2) = -1
# sanity: A21 should be 2(a2,a1)/(a1,a1) = -3
check_A21 = 2 * a1_dot_a2 / a1_sq
print(f"Cartan matrix sanity: A21 computed = {check_A21} (expect -3)")

gram_alpha = sp.Matrix([[a1_sq, a1_dot_a2], [a1_dot_a2, a2_sq]])
print(f"Gram matrix of simple roots (alpha_i . alpha_j):\n{gram_alpha}")

# Fundamental weights omega_i defined by 2(omega_i, alpha_j)/(alpha_j,alpha_j) = delta_ij
# i.e. (omega_i, alpha_j) = delta_ij * (alpha_j,alpha_j)/2
# Express omega_i = x*alpha1 + y*alpha2, solve linear system per i.
x, y = sp.symbols('x y')

def omega(i):
    eqs = []
    for j, aj_sq in enumerate([a1_sq, a2_sq], start=1):
        lhs = (x * a1_sq + y * a1_dot_a2) if j == 1 else (x * a1_dot_a2 + y * a2_sq)
        rhs = (1 if i == j else 0) * aj_sq / 2
        eqs.append(sp.Eq(lhs, rhs))
    sol = sp.solve(eqs, [x, y])
    return sol[x] * sp.Matrix([1, 0]) + sol[y] * sp.Matrix([0, 1])  # coeffs in alpha-basis

om1 = omega(1)
om2 = omega(2)
print(f"omega_1 (short-root direction) in alpha-basis: {list(om1)}")
print(f"omega_2 (long-root direction) in alpha-basis: {list(om2)}")

def inner(v, w):
    """v, w given as coeffs in alpha-basis; use gram_alpha."""
    return (sp.Matrix([v]) * gram_alpha * sp.Matrix([w]).T)[0, 0]

delta = om1 + om2  # half-sum of positive roots = sum of fundamental weights

def casimir(n1, n2):
    lam = n1 * om1 + n2 * om2
    lam_plus_2delta = lam + 2 * delta
    return sp.simplify(inner(list(lam), list(lam_plus_2delta)))

def weyl_dim():
    """Positive roots of G2 (6 of them) in alpha-basis, for Weyl dim formula."""
    # G2 positive roots: a1, a2, a1+a2, 2a1+a2, 3a1+a2, 3a1+2a2
    pos_roots = [
        sp.Matrix([1, 0]), sp.Matrix([0, 1]), sp.Matrix([1, 1]),
        sp.Matrix([2, 1]), sp.Matrix([3, 1]), sp.Matrix([3, 2]),
    ]
    return pos_roots

pos_roots = weyl_dim()

def dim_weyl(n1, n2):
    lam = n1 * om1 + n2 * om2
    d = sp.Integer(1)
    for r in pos_roots:
        num = inner(list(lam + delta), list(r))
        den = inner(list(delta), list(r))
        d *= num / den
    return sp.simplify(d)

print("\n" + "=" * 70)
print("Representation (1,0): n1=1,n2=0")
print("=" * 70)
c10 = casimir(1, 0)
d10 = dim_weyl(1, 0)
print(f"  dim = {d10}")
print(f"  C2  = {c10}")

print("\n" + "=" * 70)
print("Representation (0,1): n1=0,n2=1")
print("=" * 70)
c01 = casimir(0, 1)
d01 = dim_weyl(0, 1)
print(f"  dim = {d01}")
print(f"  C2  = {c01}")

print("\n" + "=" * 70)
print("Adjoint (highest root = 3a1+2a2 = 1*omega... check via (0,1) or (1,0)?)")
print("=" * 70)
# adjoint highest weight should coincide with whichever of (1,0)/(0,1) has dim=14
print(f"  (1,0) dim={d10}  -> {'ADJOINT' if d10==14 else 'FUNDAMENTAL-7' if d10==7 else '?'}")
print(f"  (0,1) dim={d01}  -> {'ADJOINT' if d01==14 else 'FUNDAMENTAL-7' if d01==7 else '?'}")

print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)
print("This pins down, convention-transparently (long root^2=2, the SAME")
print("normalization verified to reproduce su(3) adjoint C2=3 elsewhere in")
print("this experiment), what C2(G2;7) and C2(G2;14) actually are, and")
print("resolves whether Agricola's '(1,0)' label refers to the 7 or the 14.")
