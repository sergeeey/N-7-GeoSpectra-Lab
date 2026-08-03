import sympy as sp

I = sp.I  # noqa: E741

Tx = sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]])
Ty = sp.Matrix([[0, 0, I], [0, 0, 0], [-I, 0, 0]])
Tz = sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]])

S = sp.Matrix([[-1, I, 0], [0, 0, 1], [-1, -I, 0]])
Sinv = S.inv()
print("Correct S^-1 (sympy):")
sp.pprint(Sinv)
print()

Tpx_claimed = sp.Matrix([[0, 1, 0], [sp.Rational(1, 2), 0, sp.Rational(-1, 2)], [0, -1, 0]])
Tpy_claimed = sp.Matrix([[0, -I, 0], [sp.Rational(1, 2) * I, 0, sp.Rational(1, 2) * I], [0, -I, 0]])
Tpz_claimed = sp.diag(1, 0, -1)

print("=== Try T' = S T S^-1 (opposite conjugation order) ===")
Tpx_b = sp.simplify(S * Tx * Sinv)
Tpy_b = sp.simplify(S * Ty * Sinv)
Tpz_b = sp.simplify(S * Tz * Sinv)
print("S Tz S^-1:")
sp.pprint(Tpz_b)
print("matches claimed T'z (diag 1,0,-1)?", sp.simplify(Tpz_b - Tpz_claimed) == sp.zeros(3, 3))
print("S Tx S^-1:")
sp.pprint(Tpx_b)
print("matches claimed T'x?", sp.simplify(Tpx_b - Tpx_claimed) == sp.zeros(3, 3))
print("S Ty S^-1:")
sp.pprint(Tpy_b)
print("matches claimed T'y?", sp.simplify(Tpy_b - Tpy_claimed) == sp.zeros(3, 3))
