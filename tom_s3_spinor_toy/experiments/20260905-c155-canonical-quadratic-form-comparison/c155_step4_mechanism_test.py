r"""
C155 STEP 4 -- test the MECHANISM, not just the numbers.

claim.md tells a story: the 3 root planes contribute COHERENTLY to mu (all
onto one complex line, so they interfere and the rank collapses) and
INCOHERENTLY to c (onto mutually orthogonal components, so squares add and
Q_c is isotropic).  A story laid over two rank numbers is exactly the failure
mode this project keeps catching.  So make the story itself falsifiable and
test each half separately:

  H-coh   : for EACH of the 3 blocks, M maps the block onto the SAME complex
            line L in Sigma.   Falsified if any block maps elsewhere.
  H-Clin  : M is C-linear per block, i.e. M(dir_{2k+1}) = +-i * M(dir_{2k}).
            Falsified if the ratio is not +-i.
  H-incoh : for the 3 blocks, the images C(block) are mutually ORTHOGONAL in
            Hom(dom,tgt) under the HS inner product.  Falsified by any
            nonzero cross-block HS pairing.

If H-coh and H-Clin both hold, rank(Q_mu) = 2 is EXPLAINED (one complex line),
not merely observed.  If H-incoh holds, Q_c isotropic is EXPLAINED.
If any fails, the mechanism paragraph in claim.md must be rewritten.

Run:  python c155_step4_mechanism_test.py
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


def orthonormalise(B):
    out = []
    for j in range(B.cols):
        w = B[:, j]
        for u in out:
            w = w - hip(u, B[:, j]) * u
        w = sp.simplify(w)
        out.append(sp.simplify(w / sp.sqrt(hip(w, w))))
    return sp.Matrix.hstack(*out)


print("=" * 78)
print("C155 STEP 4  mechanism test: coherent (mu) vs incoherent (c)")
print("=" * 78)

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
assert psi_p is not None

fam = [S2.family_sym[:, k] for k in range(6)]
BLOCKS = {"A": (0, 1), "B": (2, 3), "C": (4, 5)}

Ms = {k: sp.simplify(D8_of(fam[k]) * psi_p) for k in range(6)}

# ---------------------------------------------------------------------------
print()
print("H-Clin : is  M(dir_{2k+1}) = +-i * M(dir_{2k})  for each block?")
print("-" * 78)
h_clin = True
for name, (a, b) in BLOCKS.items():
    Ma, Mb = Ms[a], Ms[b]
    nz = [t for t in range(8) if sp.simplify(Ma[t]) != 0]
    if not nz:
        print(f"  block {name}: M(dir {a}) is ZERO -- cannot form a ratio")
        h_clin = False
        continue
    t0 = nz[0]
    r = sp.simplify(Mb[t0] / Ma[t0])
    same = sp.simplify(Mb - r * Ma) == sp.zeros(8, 1)
    is_pm_i = sp.simplify(sp.re(r)) == 0 and sp.simplify(sp.Abs(r) - 1) == 0
    print(f"  block {name}: ratio = {sp.nsimplify(r)}   proportional: {same}   is +-i: {is_pm_i}")
    h_clin = h_clin and same and is_pm_i
print(f"  H-Clin holds: {h_clin}")

# ---------------------------------------------------------------------------
print()
print("H-coh : do all 3 blocks map onto the SAME complex line in Sigma?")
print("-" * 78)
lines = {}
for name, (a, b) in BLOCKS.items():
    lines[name] = Ms[a]
ref = lines["A"]
h_coh = True
for name in ("B", "C"):
    v = lines[name]
    nz = [t for t in range(8) if sp.simplify(ref[t]) != 0]
    r = sp.simplify(v[nz[0]] / ref[nz[0]])
    same_line = sp.simplify(v - r * ref) == sp.zeros(8, 1)
    print(f"  block {name} vs A: complex ratio = {sp.nsimplify(r)}   same line: {same_line}")
    h_coh = h_coh and same_line
print(f"  H-coh holds (one common complex line): {h_coh}")

# ---------------------------------------------------------------------------
print()
print("H-incoh : are the images C(block) mutually ORTHOGONAL in Hom(dom,tgt)?")
print("-" * 78)
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


Cs = {k: C_of(fam[k]) for k in range(6)}


def hs(X, Y):
    return sp.simplify((X.conjugate().T * Y).trace())


h_incoh = True
for n1, (a1, b1) in BLOCKS.items():
    for n2, (a2, b2) in BLOCKS.items():
        if n1 >= n2:
            continue
        vals = [hs(Cs[i], Cs[j]) for i in (a1, b1) for j in (a2, b2)]
        allzero = all(sp.simplify(x) == 0 for x in vals)
        print(
            f"  blocks {n1}-{n2}: HS pairings = {[sp.nsimplify(x) for x in vals]}  all zero: {allzero}"
        )
        h_incoh = h_incoh and allzero
print(f"  H-incoh holds (cross-block HS pairings vanish): {h_incoh}")

# also: within a block, are the two directions HS-orthogonal for c?
print()
print("  within-block HS pairings for c (real part is what Q_c sees):")
for name, (a, b) in BLOCKS.items():
    p = hs(Cs[a], Cs[b])
    print(
        f"    block {name}: <C(dir{a}),C(dir{b})>_HS = {sp.nsimplify(p)}   Re = {sp.nsimplify(sp.re(p))}"
    )

print()
print("=" * 78)
print("MECHANISM VERDICT")
print("=" * 78)
print(f"  coherent for mu    (H-coh and H-Clin) : {h_coh and h_clin}")
print(f"  incoherent for c   (H-incoh)          : {h_incoh}")
if h_coh and h_clin and h_incoh:
    print("  => the mechanism paragraph in claim.md is SUPPORTED by direct test,")
    print("     not merely consistent with two rank numbers.")
else:
    print("  => mechanism NOT fully supported; claim.md must be rewritten to")
    print("     report only what survived.")
