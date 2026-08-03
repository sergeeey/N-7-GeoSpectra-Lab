"""Check Tom's own linear algebra: is his S^{-1} (eq 18) really the inverse
of his S (eq 17)? And does S^{-1} T S reproduce his claimed T'_x,T'_y,T'_z
(eqs 19-21) from the original T_x,T_y,T_z (eqs 14-16)?"""

import sympy as sp

I = sp.I  # noqa: E741

Tx = sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]])
Ty = sp.Matrix([[0, 0, I], [0, 0, 0], [-I, 0, 0]])
Tz = sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]])

S = sp.Matrix([[-1, I, 0], [0, 0, 1], [-1, -I, 0]])
S_inv_claimed = sp.Matrix(
    [
        [sp.Rational(-1, 2), 0, sp.Rational(-1, 2)],
        [sp.Rational(-1, 2) * I, 0, sp.Rational(-1, 2) * I],
        [0, 1, 0],
    ]
)

print("S * S_inv_claimed (expect I):")
print(sp.simplify(S * S_inv_claimed))
print()
print("S actual inverse (sympy computed):")
print(S.inv())
print()

Tpx_claimed = sp.Matrix([[0, 1, 0], [sp.Rational(1, 2), 0, sp.Rational(-1, 2)], [0, -1, 0]])
Tpy_claimed = sp.Matrix([[0, -I, 0], [sp.Rational(1, 2) * I, 0, sp.Rational(1, 2) * I], [0, -I, 0]])
Tpz_claimed = sp.diag(1, 0, -1)

S_inv_actual = S.inv()
Tpx_actual = sp.simplify(S_inv_actual * Tx * S)
Tpy_actual = sp.simplify(S_inv_actual * Ty * S)
Tpz_actual = sp.simplify(S_inv_actual * Tz * S)

print("=== Using the ACTUAL inverse of S (not his stated S^-1) ===")
print("S^-1 Tx S:")
print(Tpx_actual)
print("matches his claimed T'x?", sp.simplify(Tpx_actual - Tpx_claimed) == sp.zeros(3, 3))
print()
print("S^-1 Ty S:")
print(Tpy_actual)
print("matches his claimed T'y?", sp.simplify(Tpy_actual - Tpy_claimed) == sp.zeros(3, 3))
print()
print("S^-1 Tz S:")
print(Tpz_actual)
print("matches his claimed T'z?", sp.simplify(Tpz_actual - Tpz_claimed) == sp.zeros(3, 3))

print()
print("=== Using HIS STATED (possibly wrong) S_inv_claimed instead ===")
Tpx_using_his_Sinv = sp.simplify(S_inv_claimed * Tx * S)
Tpy_using_his_Sinv = sp.simplify(S_inv_claimed * Ty * S)
Tpz_using_his_Sinv = sp.simplify(S_inv_claimed * Tz * S)
print("S_inv_claimed Tx S:")
print(Tpx_using_his_Sinv)
print("S_inv_claimed Ty S:")
print(Tpy_using_his_Sinv)
print("S_inv_claimed Tz S:")
print(Tpz_using_his_Sinv)
