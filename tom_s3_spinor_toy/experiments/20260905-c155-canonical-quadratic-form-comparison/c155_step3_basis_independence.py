r"""
C155 STEP 3 -- self-attack on the one basis-DEPENDENT claim of Step 1.

Step 1 reported  Re(G_c) = 8*I_6  and called it "isotropic".  That word is
only meaningful relative to a metric on the family V itself.  Ranks
(6 vs 2) and dim ker = 4 are basis-INDEPENDENT and stand regardless; the
isotropy claim does not, unless family_sym is orthonormal for the natural
metric V inherits as a subspace of  m* (x) Lambda^2 m*  -- i.e. the plain
Euclidean structure on the 90 coefficients, since the (e_i, e_i ^ e_j)
basis behind those coefficients is itself orthonormal.

So: compute Gram(family_sym).  Then re-express BOTH forms in a genuinely
orthonormal basis of V and re-test.  If Q_c stays a multiple of I there,
the isotropy claim survives; if not, it was an artifact of the basis and
must be withdrawn, leaving only the rank statement.

Run:  python c155_step3_basis_independence.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
EXP = HERE.parent


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, EXP / rel)
    assert spec and spec.loader
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S2 = load(
    "c153_step2",
    "20260904-c153-nk-linearity-structural-derivation/c153_step2_exact_rational_verification.py",
)


def hip(a, b):
    return sp.simplify(sum(sp.conjugate(a[k]) * b[k] for k in range(a.rows)))


print("=" * 78)
print("C155 STEP 3  is the isotropy claim basis-independent?")
print("=" * 78)

fam = [S2.family_sym[:, k] for k in range(6)]
Gv = sp.Matrix(6, 6, lambda a, b: hip(fam[a], fam[b]))
print("  Gram(family_sym) in the natural 90-coefficient metric:")
for r in range(6):
    print("    " + "  ".join(f"{sp.nsimplify(Gv[r, c])!s:>8}" for c in range(6)))
diagonal = sp.simplify(Gv - sp.diag(*[Gv[i, i] for i in range(6)])) == sp.zeros(6, 6)
equal_norms = len({sp.simplify(Gv[i, i]) for i in range(6)}) == 1
print(f"  family basis is ORTHOGONAL      : {diagonal}")
print(f"  all six have EQUAL norm         : {equal_norms}")
print(f"  => already orthonormal up to one common scale: {diagonal and equal_norms}")

# ---------------------------------------------------------------------------
# Rebuild both forms in a V-orthonormal basis and re-test isotropy.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("  re-expressing both forms in a V-ORTHONORMAL basis")
print("=" * 78)

# Gram-Schmidt on the family itself (w.r.t. the natural metric on V)
onb = []
for j in range(6):
    w = fam[j]
    for u in onb:
        w = w - hip(u, fam[j]) * u
    w = sp.simplify(w)
    onb.append(sp.simplify(w / sp.sqrt(hip(w, w))))
check = sp.Matrix(6, 6, lambda a, b: hip(onb[a], onb[b]))
print(f"  new basis orthonormal in V : {sp.simplify(check - sp.eye(6)) == sp.zeros(6, 6)}")


def lam_of(vec):
    lam = {}
    for k in range(6):
        M = sp.zeros(6, 6)
        for p_idx, (i, j) in enumerate(S2.PAIRS6):
            M[i, j] += vec[k * 15 + p_idx]
            M[j, i] -= vec[k * 15 + p_idx]
        lam[k + 1] = M
    return lam


def D8_of(vec):
    lam = lam_of(vec)
    D = sp.zeros(8, 8)
    for i in range(1, 7):
        D += S2.E_sym[i] * S2.spin_lift_sym(lam[i])
    return D


stacked = sp.Matrix.vstack(S2.RHO_SIGMA[0], S2.RHO_SIGMA[1])
inv_ns = stacked.nullspace()
v1 = inv_ns[0]
v2 = sp.simplify(inv_ns[1] - (hip(v1, inv_ns[1]) / hip(v1, v1)) * v1)
b2 = sp.Matrix.hstack(v1 / sp.sqrt(hip(v1, v1)), v2 / sp.sqrt(hip(v2, v2)))
D_LC_2 = sp.simplify(b2.conjugate().T * D8_of(S2.lc_vec) * b2)
psi_p = None
for val, mult, vecs in D_LC_2.eigenvects():
    if sp.nsimplify(val) == 3:
        psi_p = sp.simplify(b2 * vecs[0])
psi_n2 = sp.simplify(hip(psi_p, psi_p))


def orthonormalise(B):
    out = []
    for j in range(B.cols):
        w = B[:, j]
        for u in out:
            w = w - hip(u, B[:, j]) * u
        w = sp.simplify(w)
        out.append(sp.simplify(w / sp.sqrt(hip(w, w))))
    return sp.Matrix.hstack(*out)


dom_on = orthonormalise(S2.dom_sym)
tgt_on = orthonormalise(S2.tgt_sym)
I6s = sp.eye(6)


def C_of(vec):
    lam = lam_of(vec)
    D = sp.zeros(48, 48)
    for i in range(1, 7):
        D += S2.kron_sym(S2.E_sym[i] * S2.spin_lift_sym(lam[i]), I6s)
        D += S2.kron_sym(S2.E_sym[i], -lam[i])
    return sp.simplify(tgt_on.conjugate().T * D * dom_on)


def M_of(vec):
    return sp.simplify(D8_of(vec) * psi_p / sp.sqrt(psi_n2))


Cs = [C_of(v) for v in onb]
Ms = [M_of(v) for v in onb]
Gc = sp.Matrix(6, 6, lambda a, b: sp.simplify(sp.re((Cs[a].conjugate().T * Cs[b]).trace())))
Gm = sp.Matrix(6, 6, lambda a, b: sp.simplify(sp.re(hip(Ms[a], Ms[b]))))

print()
print("  Re(G_c) in the V-orthonormal basis:")
for r in range(6):
    print("    " + "  ".join(f"{sp.nsimplify(Gc[r, c])!s:>8}" for c in range(6)))
print("  Re(G_mu) in the V-orthonormal basis:")
for r in range(6):
    print("    " + "  ".join(f"{sp.nsimplify(Gm[r, c])!s:>8}" for c in range(6)))

iso = sp.simplify(Gc - Gc[0, 0] * sp.eye(6)) == sp.zeros(6, 6)
print()
print(f"  Q_c IS a multiple of the identity in a TRULY orthonormal basis: {iso}")
print(f"  rank Re(G_c) = {Gc.rank()},  rank Re(G_mu) = {Gm.rank()}   (basis-INDEPENDENT)")
print()
print("  VERDICT on the Step-1 wording:")
if iso:
    print("    isotropy claim SURVIVES -- it was not a basis artifact.")
else:
    print("    isotropy claim WITHDRAWN -- basis artifact; only the rank")
    print("    statement (6 vs 2) and dim ker = 4 survive.")
