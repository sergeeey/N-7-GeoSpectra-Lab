r"""
C155 STEP 2 -- make Step 1 rank statement CONCRETE, then attack it.

Step 1 found, exactly:
    Re(G_c)  = 8 * I_6          (isotropic, full rank 6)
    Re(G_mu) = rank 2 of 6      (four-dimensional kernel)

Two things must happen before any of that is called a finding:

  (A) CONCRETENESS.  A rank computed from a Gram matrix is one line of
      linear algebra away from a typo.  Exhibit the kernel explicitly and
      verify  D_Sigma(v) psi_+ == 0  as an exact 8-vector identity, for a
      basis of the kernel AND for a random kernel element not in that basis.

  (B) FORCING CHECK (the C153/C154 lesson, applied BEFORE claiming novelty).
      Ask of EACH structure: does it follow from something already on record?
        - Q_c isotropic: weight-orthogonality across the 3 root planes kills
          cross-plane terms; C-linearity (C153 per-plane law) makes each
          2x2 plane block a multiple of I; a Weyl S_3 symmetry permuting the
          3 roots would force the three multiples EQUAL.  If all three hold,
          Q_c = const * I is FORCED and is not a discovery.
        - Q_mu rank 2: if M is C-linear with equal per-plane magnitudes and
          the three planes enter with signs, the image collapses to one
          complex line and the kernel is 2 complex dims = 4 real.  Same
          forcing family.
      Both are tested here numerically-exactly, not asserted.

Run:  python c155_step2_kernel_and_forcing.py
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


print("=" * 78)
print("C155 STEP 2  concreteness + forcing check")
print("=" * 78)

stacked = sp.Matrix.vstack(S2.RHO_SIGMA[0], S2.RHO_SIGMA[1])
inv_ns = stacked.nullspace()
assert len(inv_ns) == 2
v1 = inv_ns[0]
v2 = sp.simplify(inv_ns[1] - (hip(v1, inv_ns[1]) / hip(v1, v1)) * v1)
b2 = sp.Matrix.hstack(v1 / sp.sqrt(hip(v1, v1)), v2 / sp.sqrt(hip(v2, v2)))
D_LC_2 = sp.simplify(b2.conjugate().T * D8_of(S2.lc_vec) * b2)
psi_p = None
psi_m = None
for val, mult, vecs in D_LC_2.eigenvects():
    if sp.nsimplify(val) == 3:
        psi_p = sp.simplify(b2 * vecs[0])
    if sp.nsimplify(val) == -3:
        psi_m = sp.simplify(b2 * vecs[0])
assert psi_p is not None
psi_n2 = sp.simplify(hip(psi_p, psi_p))
print(f"  psi_+ built, ||psi_+||^2 = {psi_n2}")
print(f"  T^2-invariant subspace of Sigma: complex dim {len(inv_ns)}  (= {2 * len(inv_ns)} real)")

fam = [S2.family_sym[:, k] for k in range(6)]


def M_of(vec):
    return sp.simplify(D8_of(vec) * psi_p)


Ms = [M_of(v) for v in fam]

# ===========================================================================
# (A) CONCRETENESS -- exhibit the kernel, verify D psi_+ == 0 as vectors
# ===========================================================================
print()
print("=" * 78)
print("(A)  explicit kernel of  v |-> D_Sigma(v) psi_+   (not a rank number)")
print("=" * 78)

# The map is REAL-linear on the 6 real coordinates; build its real matrix
# by splitting each image 8-vector into (Re, Im) -> 16 real rows.
rows = []
for M in Ms:
    col = []
    for t in range(8):
        col.append(sp.re(M[t]))
        col.append(sp.im(M[t]))
    rows.append(col)
Mreal = sp.Matrix(rows).T  # 16 x 6, columns = images of the 6 basis directions
Mreal = sp.simplify(Mreal)
ker = Mreal.nullspace()
print(f"  real matrix of M : {Mreal.rows} x {Mreal.cols}")
print(f"  rank(M)          = {Mreal.rank()}   (Step 1 predicted image rank 2)")
print(f"  dim ker(M)       = {len(ker)}   (Step 1 predicted 4)")
for idx, kv in enumerate(ker):
    coeffs = [sp.nsimplify(kv[i]) for i in range(6)]
    vec = sp.zeros(90, 1)
    for i in range(6):
        vec += kv[i] * fam[i]
    img = sp.simplify(D8_of(vec) * psi_p)
    is_zero = sp.simplify(img) == sp.zeros(8, 1)
    print(f"    ker[{idx}] coeffs={coeffs}  ->  D_Sigma(v) psi_+ == 0 EXACTLY: {is_zero}")
    assert is_zero, "claimed kernel element does not annihilate psi_+ -- STOP"

# random element of the kernel, NOT one of the basis vectors
if ker:
    rnd = sp.zeros(6, 1)
    for w, kv in zip(
        [sp.Rational(3, 5), sp.Rational(-2, 7), sp.Rational(11, 3), sp.Rational(1, 2)], ker
    ):
        rnd += w * kv
    vec = sp.zeros(90, 1)
    for i in range(6):
        vec += rnd[i] * fam[i]
    img = sp.simplify(D8_of(vec) * psi_p)
    print(
        f"  RANDOM kernel combination annihilates psi_+ EXACTLY: {sp.simplify(img) == sp.zeros(8, 1)}"
    )
    # and it must NOT be in the kernel of c
    I6s = sp.eye(6)

    def C_of(v):
        lam = lam_of(v)
        D = sp.zeros(48, 48)
        for i in range(1, 7):
            D += S2.kron_sym(S2.E_sym[i] * S2.spin_lift_sym(lam[i]), I6s)
            D += S2.kron_sym(S2.E_sym[i], -lam[i])
        return sp.simplify(S2.tgt_sym.conjugate().T * D * S2.dom_sym)

    cmat = C_of(vec)
    cnorm2 = sp.simplify(sum(sp.Abs(cmat[r, c]) ** 2 for r in range(3) for c in range(3)))
    print(
        f"  the SAME connection has  ||c||^2 = {sp.nsimplify(cnorm2)}  (nonzero => c survives where mu dies)"
    )

# does the kernel also annihilate psi_-?
if psi_m is not None and ker:
    vec = sp.zeros(90, 1)
    for i in range(6):
        vec += ker[0][i] * fam[i]
    img_m = sp.simplify(D8_of(vec) * psi_m)
    print(f"  ker[0] also annihilates psi_- : {sp.simplify(img_m) == sp.zeros(8, 1)}")

# ===========================================================================
# (B) FORCING CHECK -- is any of this entailed by already-registered structure?
# ===========================================================================
print()
print("=" * 78)
print("(B)  FORCING CHECK -- run BEFORE calling anything a discovery")
print("=" * 78)

# B1: are the 6 family basis directions plane-local, 2 per root plane?
print("  B1 support of each family basis direction over the 3 root planes")
for k in range(6):
    v = fam[k]
    supp = sorted({(idx // 15) for idx in range(90) if sp.simplify(v[idx]) != 0})
    pairs = sorted({S2.PAIRS6[idx % 15] for idx in range(90) if sp.simplify(v[idx]) != 0})
    print(f"    direction {k}: e-index block {supp}, 2-form pairs {pairs}")

# B2: per-plane magnitudes of BOTH maps -- equal across planes?  (Weyl test)
print()
print("  B2 per-direction magnitudes (equal across planes => Weyl/Schur forced)")
I6s = sp.eye(6)


def C_of2(v):
    lam = lam_of(v)
    D = sp.zeros(48, 48)
    for i in range(1, 7):
        D += S2.kron_sym(S2.E_sym[i] * S2.spin_lift_sym(lam[i]), I6s)
        D += S2.kron_sym(S2.E_sym[i], -lam[i])
    return sp.simplify(S2.tgt_sym.conjugate().T * D * S2.dom_sym)


for k in range(6):
    cm = C_of2(fam[k])
    cn2 = sp.simplify(sum(sp.Abs(cm[r, c]) ** 2 for r in range(3) for c in range(3)))
    mm = Ms[k]
    mn2 = sp.simplify(hip(mm, mm))
    print(
        f"    dir {k}:  ||c||^2 = {sp.nsimplify(cn2)!s:>6}   ||D psi_+||^2 = {sp.nsimplify(mn2)!s:>6}"
    )

print()
print("  B3 image of M inside the T^2-invariant subspace")
inv_basis = sp.Matrix.hstack(*inv_ns)
for k in range(6):
    resid = sp.simplify(inv_basis * (inv_basis.pinv() * Ms[k]) - Ms[k])
    inside = resid == sp.zeros(8, 1)
    print(f"    M(dir {k}) lies in the T^2-invariant subspace: {inside}")
print("    (equivariance predicts YES for all; image is 2 REAL dims inside a")
print("     4-real-dim invariant space, so 2 extra real dims are killed by")
print("     something beyond equivariance -- that is what B2 sign pattern tests)")
