r"""
C158 STEP 2 -- G4 PASSED (ker(M) is W(A_2)=S_3-invariant). Per the
pre-registered branch plan: decompose V_conn (6-dim) and ker(M) (4-dim), and
by extension the 2-dim quotient V_conn/ker(M), into S_3-isotypic pieces via
character theory. NOT pre-registered which irrep the quotient is -- that
would be exactly the post-hoc fit this project's discipline forbids.

S_3 has 3 irreps: trivial (dim 1), sign (dim 1), standard (dim 2).
Conjugacy classes: {e} (size 1), {transpositions} (size 3), {3-cycles} (size 2).
Character table:
    triv:     1   1   1
    sign:     1  -1   1
    std:      2   0  -1
Multiplicity of irrep chi in a representation V:
    m_chi = (1/6) [ 1*dim(V)*chi(e) + 3*tr(W01|V)*chi(transposition)
                     + 2*tr(W012|V)*chi(3-cycle) ]
(all characters real, S_3 real representations, no conjugation needed)

Run:  python c158_step2_isotypic_decomposition.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S1 = load("c158s1", "c158_step1_weyl_action.py")

W01, W12 = S1.W01, S1.W12
W012 = W01 * W12
Ker = S1.Ker
ker_basis = S1.ker_basis

CHAR_TABLE = {
    "trivial": (1, 1, 1),
    "sign": (1, -1, 1),
    "standard": (2, 0, -1),
}


def multiplicity(chi, dim, tr_transp, tr_3cycle):
    ce, ct, c3 = chi
    return sp.Rational(1, 6) * (1 * dim * ce + 3 * tr_transp * ct + 2 * tr_3cycle * c3)


print("=" * 78)
print("STEP 2a  character decomposition of V_conn (the full 6-dim family)")
print("=" * 78)
dimV = 6
tr_transp_V = sp.simplify(W01.trace())
tr_3cycle_V = sp.simplify(W012.trace())
print(f"  tr(W01) [transposition rep] = {tr_transp_V}")
print(f"  tr(W01*W12) [3-cycle rep]   = {tr_3cycle_V}")
mults_V = {}
for name, chi in CHAR_TABLE.items():
    m = multiplicity(chi, dimV, tr_transp_V, tr_3cycle_V)
    mults_V[name] = m
    print(f"  multiplicity of {name:9s} (dim {chi[0]}) in V_conn : {m}")
total_dim_check = sum(chi[0] * mults_V[name] for name, chi in CHAR_TABLE.items())
print(
    f"  dimension check: sum(mult*dim) = {total_dim_check}  (must be 6): "
    f"{sp.simplify(total_dim_check) == 6}"
)

print()
print("=" * 78)
print("STEP 2b  character decomposition of ker(M) (the 4-dim W-invariant kernel)")
print("=" * 78)


def restrict_to_ker(W):
    """W maps ker(M) into itself (G4 confirmed). Express as a 4x4 matrix in
    the ker_basis coordinates, using the same exact-solve approach as Step 1."""
    Gram = sp.simplify(Ker.T * Ker)
    Ker_pinv = Gram.inv() * Ker.T
    cols = []
    for v in ker_basis:
        img = sp.simplify(W * v)
        coords = sp.simplify(Ker_pinv * img)
        cols.append(coords)
    return sp.Matrix.hstack(*cols)


W01_ker = restrict_to_ker(W01)
W012_ker = restrict_to_ker(W012)
print(
    f"  W01 restricted to ker(M), 4x4, orthogonal: {sp.simplify(W01_ker.T * W01_ker) == sp.eye(4)}"
)
dimK = 4
tr_transp_K = sp.simplify(W01_ker.trace())
tr_3cycle_K = sp.simplify(W012_ker.trace())
print(f"  tr(W01|ker)        = {tr_transp_K}")
print(f"  tr(W01*W12|ker)    = {tr_3cycle_K}")
mults_K = {}
for name, chi in CHAR_TABLE.items():
    m = multiplicity(chi, dimK, tr_transp_K, tr_3cycle_K)
    mults_K[name] = m
    print(f"  multiplicity of {name:9s} (dim {chi[0]}) in ker(M) : {m}")
total_dim_checkK = sum(chi[0] * mults_K[name] for name, chi in CHAR_TABLE.items())
print(
    f"  dimension check: sum(mult*dim) = {total_dim_checkK}  (must be 4): "
    f"{sp.simplify(total_dim_checkK) == 4}"
)

print()
print("=" * 78)
print("STEP 2c  the QUOTIENT V_conn/ker(M) -- by SUBTRACTION of characters")
print("         (NOT pre-registered which irrep this is -- read off, not assumed)")
print("=" * 78)
mults_Q = {name: sp.simplify(mults_V[name] - mults_K[name]) for name in CHAR_TABLE}
for name, m in mults_Q.items():
    print(f"  multiplicity of {name:9s} in V_conn/ker(M) : {m}")
total_dim_Q = sum(chi[0] * mults_Q[name] for name, chi in CHAR_TABLE.items())
print(
    f"  dimension check: sum(mult*dim) = {total_dim_Q}  (must be 2): "
    f"{sp.simplify(total_dim_Q) == 2}"
)

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print(f"  V_conn (6-dim)       = {mults_V}")
print(f"  ker(M)  (4-dim)      = {mults_K}")
print(f"  V_conn/ker(M) (2-dim)= {mults_Q}")
is_standard = (
    mults_Q.get("standard") == 1 and mults_Q.get("trivial") == 0 and mults_Q.get("sign") == 0
)
print(f"  quotient IS the standard 2-dim irrep of S_3, cleanly: {is_standard}")
