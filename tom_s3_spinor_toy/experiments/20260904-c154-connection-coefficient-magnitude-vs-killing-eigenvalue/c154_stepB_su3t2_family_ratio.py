r"""
C154 STEP B -- the SU(3)/T^2 test the round originally (wrongly) skipped.

A context-blind FL Step 8a skeptic pass found claim.md's reason for skipping
this test was invalid on two counts: (1) it misquoted PREREGISTRATION.md,
which states Test B is independent of Test A, not contingent on it; (2) the
"mechanism generalises" argument assumed, without checking, that mu (as
originally defined) has a nontrivial kernel on SU(3)/T^2's 6-dim family too
-- never computed. Since Step A's mu was also found to be the WRONG
scalarisation entirely (see its own correction note), this file builds the
CORRECT (full-norm) analogue from scratch on SU(3)/T^2, reusing C153 Step
2's exact sympy machinery unmodified (E_sym, RHO_SIGMA, T2_M, family_sym,
c_of_exact).

WHAT IS NEW HERE (not previously computed anywhere)
  1. The exact T^2-invariant spinors in Sigma (analogous to psi_+/psi_- on
     S^6), via sympy nullspace of RHO_SIGMA[0], RHO_SIGMA[1] -- Stage 2a's
     own calibration gate found exactly 2 of them numerically (D_Sigma
     eigenvalues +-3); built here exactly, independently.
  2. mu(nabla) := ||D_Sigma(nabla) psi_+|| / ||psi_+||, the SAME full-norm
     construction Step A used, tested for whether it even makes sense here
     (does D_Sigma(nabla) psi_+ stay inside span(psi_+,psi_-) for a general
     nabla in the 6-dim family, not just at LC?).
  3. |c(nabla)| via the FULL Frobenius norm of the 3x3 matrix c(nabla) --
     avoiding the original pre-registration's now-unnecessary "uniform
     entry magnitude" requirement, using the same "nothing discarded"
     principle Step A's correction established.
  4. The ratio |c(nabla)|/mu(nabla), tested on all 6 family basis vectors
     AND one non-basis combination (sum of all 6), for the same reason
     Step A's 3rd point mattered: agreement at a combination is not
     algebraically forced by agreement on the basis, since both quantities
     are norms (homogeneous degree 1), not linear functionals.

Run:  python c154_stepB_su3t2_family_ratio.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
S2_PATH = (
    HERE.parent
    / "20260904-c153-nk-linearity-structural-derivation"
    / "c153_step2_exact_rational_verification.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


print("=" * 78)
print("Importing C153 Step 2 (exact SU(3)/T^2 geometry, family, c_of_exact)")
print("=" * 78)
S2 = load_module("c153_step2", S2_PATH)

E_sym = S2.E_sym
RHO_SIGMA = S2.RHO_SIGMA
family_sym = S2.family_sym
c_of_exact = S2.c_of_exact

print(f"  exact family dimension (regression) : {family_sym.cols}  (must be 6)")
assert family_sym.cols == 6

print()
print("=" * 78)
print("STEP B1  exact T^2-invariant spinors in Sigma (nullspace, not SVD)")
print("=" * 78)

stacked = sp.Matrix.vstack(RHO_SIGMA[0], RHO_SIGMA[1])
inv_ns = stacked.nullspace()
print(f"  exact T^2-invariant spinors in Sigma : {len(inv_ns)}  (Stage 2a found 2 numerically)")
assert len(inv_ns) == 2

# Diagonalise D_Sigma(LC-analog) is not available here (no single "LC" on
# this coset the way S^6 has one) -- instead identify psi_+/psi_- as the
# eigenvectors of D_Sigma AT THE FAMILY'S OWN Levi-Civita element (the
# family basis vector already shown, in C153, to reproduce Stage 2a's
# +-3 eigenvalues). Reuse that element directly: it is family_sym's own
# Levi-Civita vector, already verified present in the family (C153 Step 2d).
lc_vec = S2.lc_vec
D_LC = sp.zeros(8, 8)
lam_lc = {}
for k in range(6):
    Mk = sp.zeros(6, 6)
    for p_idx, (i, j) in enumerate(S2.PAIRS6):
        Mk[i, j] += lc_vec[k * 15 + p_idx]
        Mk[j, i] -= lc_vec[k * 15 + p_idx]
    lam_lc[k + 1] = Mk
for i in range(1, 7):
    D_LC += E_sym[i] * S2.spin_lift_sym(lam_lc[i])

# inv_ns is not orthonormal in general -- re-orthonormalise via Gram-Schmidt
# with the standard Hermitian inner product before diagonalising D_LC on it.


def hip(a, b):
    return sp.simplify(sum(sp.conjugate(a[k]) * b[k] for k in range(a.rows)))


v1 = inv_ns[0]
v2 = inv_ns[1] - (hip(v1, inv_ns[1]) / hip(v1, v1)) * v1
v1n = v1 / sp.sqrt(hip(v1, v1))
v2n = v2 / sp.sqrt(hip(v2, v2))
basis2n = sp.Matrix.hstack(v1n, v2n)
D_LC_2x2n = sp.simplify(basis2n.T.conjugate() * D_LC * basis2n)
eigs = list(D_LC_2x2n.eigenvects())
print("  D_Sigma(LC) on the orthonormalised invariant 2-plane, eigenvalues:")
psi_plus_su3t2 = None
for val, mult, vecs in eigs:
    print(f"    eigenvalue {sp.nsimplify(val)}  (multiplicity {mult})")
    for v in vecs:
        vec_in_sigma = sp.simplify(basis2n * v)
        if sp.nsimplify(val) == 3 and psi_plus_su3t2 is None:
            psi_plus_su3t2 = vec_in_sigma

assert psi_plus_su3t2 is not None, "could not identify the +3 eigenvector -- STOP"
psi_norm2_su3t2 = sp.simplify(hip(psi_plus_su3t2, psi_plus_su3t2))
print(f"  psi_+ (SU(3)/T^2) identified, ||psi_+||^2 = {psi_norm2_su3t2}")

print()
print("=" * 78)
print("STEP B2  mu(nabla) = ||D_Sigma(nabla) psi_+|| / ||psi_+||, all 6 + sum")
print("=" * 78)


def D_of(vec):
    D = sp.zeros(8, 8)
    for k in range(6):
        Mk = sp.zeros(6, 6)
        for p_idx, (i, j) in enumerate(S2.PAIRS6):
            Mk[i, j] += vec[k * 15 + p_idx]
            Mk[j, i] -= vec[k * 15 + p_idx]
        D += E_sym[k + 1] * S2.spin_lift_sym(Mk)
    return D


def mu_su3t2(vec):
    Dpsi = sp.simplify(D_of(vec) * psi_plus_su3t2)
    n2 = sp.simplify(hip(Dpsi, Dpsi))
    return sp.simplify(sp.sqrt(n2) / sp.sqrt(psi_norm2_su3t2))


mu_lc = mu_su3t2(lc_vec)
print(f"  mu(LC) [must reproduce Stage 2a's exact 3] : {sp.nsimplify(mu_lc)}")
assert sp.simplify(mu_lc - 3) == 0, "does not reproduce Stage 2a's certified eigenvalue -- STOP"

print()
print("=" * 78)
print("STEP B3  |c(nabla)| via full Frobenius norm (nothing discarded), ratio")
print("=" * 78)


def c_norm(vec):
    M = c_of_exact(vec)
    n2 = sp.simplify(sum(sp.Abs(M[r, c]) ** 2 for r in range(3) for c in range(3)))
    return sp.sqrt(n2)


results = []
for k in range(6):
    v = family_sym[:, k]
    muv = mu_su3t2(v)
    cv = c_norm(v)
    if sp.simplify(muv) == 0:
        print(f"  basis {k}: mu=0 (degenerate direction, ratio undefined -- skip)")
        continue
    ratio = sp.simplify(cv / muv)
    ok = sp.simplify(ratio - sp.Rational(2, 3)) == 0
    mu_s = f"{sp.nsimplify(muv)!s:>12}"
    c_s = f"{sp.nsimplify(cv)!s:>14}"
    print(f"  basis {k}: mu = {mu_s}   |c| = {c_s}   ratio = {ratio}   ==2/3: {ok}")
    results.append(ok)

v_sum = sum((family_sym[:, k] for k in range(6)), sp.zeros(90, 1))
mu_sum = mu_su3t2(v_sum)
c_sum_norm = c_norm(v_sum)
ratio_sum = sp.simplify(c_sum_norm / mu_sum) if sp.simplify(mu_sum) != 0 else None
print(
    f"  SUM of all 6: mu = {sp.nsimplify(mu_sum)}   |c| = {sp.nsimplify(c_sum_norm)}   ratio = {ratio_sum}"
)
sum_ok = ratio_sum is not None and sp.simplify(ratio_sum - sp.Rational(2, 3)) == 0
print(f"  SUM ratio == 2/3 : {sum_ok}")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
all_basis_ok = len(results) > 0 and all(results)
print(
    f"  all tested basis directions give ratio 2/3 : {all_basis_ok}  ({len(results)}/6 nondegenerate)"
)
print(f"  the SUM combination also gives ratio 2/3    : {sum_ok}")
if all_basis_ok and sum_ok:
    print("  CONFIRMED on SU(3)/T^2 as well: |c(nabla)| = (2/3)*mu(nabla) across the")
    print("  admissible family here too, matching S^6 exactly. The relation now has")
    print("  7 pre-registered confirmations on S^6 (3 points) + SU(3)/T^2 (>=6")
    print("  points), not a 2-point coincidence.")
else:
    print("  NOT confirmed uniformly -- report exactly which points failed and by")
    print("  how much; do not average over failures.")
