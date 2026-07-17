"""
Round94 (E24): does the B-L-proportional U(1) generator act as a well-defined
scalar charge on round59's explicit twisted-kernel vector?

Reuses, by direct import (no reconstruction of their internals):
  - experiments/20260714-round59-trivial-rank-certification/
    round59_route_b_consistency.py:
      DIM, N, fidx, herm, vec64_from_pairs, leibniz64, D_full,
      ODD_IDX, EVEN_IDX  (module-level, safe to import: no code runs on
      import besides building su3-generator caches that this script does not
      touch)
  - experiments/20260708-dolan-casimir-g2su3/g2su3_explicit_clifford.py:
      DIM, SUBSETS, IDX, vec_from_subsets
  - experiments/20260619-g15-hypercharge/g15_hypercharge.py:
      BmL (the actual 8x8 matrix, imported unchanged, not rebuilt by hand)

v_a, v_b, w are RECONSTRUCTED here with the exact coefficient dict literal
round59_route_b_consistency.py:219-221 uses (those three lines define them
inside main(), so they are not importable as module attributes -- the
coefficients are copied verbatim and cited).

Nothing here modifies any existing file. This script and its two output
files (results json + decision.md) are the only new artifacts.
"""

import json
import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, "..", ".."))

_ROUND59 = os.path.join(_REPO, "experiments", "20260714-round59-trivial-rank-certification")
_DOLAN = os.path.join(_REPO, "experiments", "20260708-dolan-casimir-g2su3")
_G15 = os.path.join(_REPO, "experiments", "20260619-g15-hypercharge")

for _p in (_ROUND59, _DOLAN, _G15):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# round59_route_b_consistency.py (cited paths are relative to this file):
from round59_route_b_consistency import (  # noqa: E402
    DIM,
    N,
    fidx,
    herm,
    vec64_from_pairs,
    leibniz64,
    D_full,
)

# g2su3_explicit_clifford.py
from g2su3_explicit_clifford import SUBSETS, IDX  # noqa: E402  (DIM already imported above, same value)

# g15_hypercharge.py -- the actual BmL matrix, imported unchanged.
from g15_hypercharge import BmL as BmL_g15  # noqa: E402

sqrt = sp.sqrt

assert DIM == 8


def popcount3(j):
    return bin(j).count("1")


def g15_index_to_subset(j):
    """Explicit bijection G15's 3-qubit kron index -> dolan-casimir subset.
    g15_hypercharge.py:65-67: sigma3_1=kron(s3,I2,I2) 'qubit1 (bit weight 4)',
    sigma3_2 weight 2, sigma3_3 weight 1 -- i.e. j = 4*i1 + 2*i2 + i3 in the
    standard kron-index convention. i_k=1 means qubit k is in the |1> state;
    we map that to 'k is present in the subset'."""
    i1 = (j >> 2) & 1
    i2 = (j >> 1) & 1
    i3 = j & 1
    return tuple(k for k, bit in zip((1, 2, 3), (i1, i2, i3)) if bit)


def bl_degree_formula(subset):
    """g15_hypercharge.py:71 + T2 (line 104-109): BmL = (2H-3)/3, H=popcount.
    Applied here to a dolan-casimir subset via |subset| standing in for H."""
    k = len(subset)
    return sp.Rational(2 * k - 3, 3)


def main():
    report = {}
    print("=" * 78)
    print("ROUND94 (E24): B-L eigenvalue on round59's twisted-kernel vector")
    print("=" * 78)

    # ========================================================================
    # STEP 1 -- structural compatibility check
    # ========================================================================
    print("\n" + "-" * 78)
    print("[1] Structural compatibility: is G15's 8-dim weight space the SAME")
    print("    vector space as dolan-casimir's Sigma = Lambda-bullet(C^3)?")
    print("-" * 78)

    # 1a. Confirm BmL_g15 is exactly the degree/Hamming-weight formula
    #     (re-verifying g15_hypercharge.py's own T2, cheap spot-check).
    t2_match = all(
        sp.simplify(BmL_g15[j, j] - sp.Rational(2 * popcount3(j) - 3, 3)) == 0 for j in range(8)
    )
    print(f"    BmL_g15[j,j] == (2*popcount(j)-3)/3 for all j=0..7 ? {t2_match}")
    report["bmL_g15_is_pure_hamming_weight_formula"] = t2_match

    # 1b. Explicit bijection j -> subset, and check it carries BmL_g15's
    #     diagonal entries EXACTLY onto the degree-formula value for the
    #     corresponding dolan-casimir subset (not just "same formula in the
    #     abstract" -- an actual entrywise check under one concrete,
    #     explicitly-stated bijection).
    bijection_check = {}
    for j in range(8):
        s = g15_index_to_subset(j)
        lhs = sp.simplify(BmL_g15[j, j])
        rhs = bl_degree_formula(s)
        bijection_check[j] = (str(s), str(lhs), str(rhs), lhs == rhs)
        print(
            f"    j={j} -> subset={s or '()'}: BmL_g15={lhs}, degree-formula={rhs}, match={lhs == rhs}"
        )
    bijection_ok = all(v[3] for v in bijection_check.values())
    report["explicit_bijection_matches_degree_formula"] = bijection_ok

    # 1c. Confirm dolan-casimir's Sigma really does decompose as
    #     Lambda^0 (+) Lambda^1 (+) Lambda^2 (+) Lambda^3 = 1 (+) 3 (+) 3bar (+) 1,
    #     matching G14's decomposition cited in g15_hypercharge.py's own
    #     docstring line 3 (reused by citation, not re-derived: G14 itself is
    #     not re-run here).
    degree_sizes = {k: sum(1 for s in SUBSETS if len(s) == k) for k in range(4)}
    print(f"    Sigma grade sizes (dims of Lambda^0..3): {degree_sizes}  (expected 1,3,3,1)")
    report["sigma_grade_sizes"] = degree_sizes

    structurally_comparable = t2_match and bijection_ok and degree_sizes == {0: 1, 1: 3, 2: 3, 3: 1}
    print(f"\n    VERDICT (step 1): structurally comparable = {structurally_comparable}")
    print(
        "    (Sigma IS G15's 8-dim weight space, under a degree/Hamming-weight-"
        "preserving relabeling; BmL depends ONLY on that degree, so the specific"
        " choice of bijection above is one legitimate representative, not an"
        " arbitrary forcing.)"
    )
    report["structurally_comparable"] = structurally_comparable

    # ========================================================================
    # STEP 2 -- Leibniz-lift BmL to Sigma(x)Sigma, apply to round59's vectors
    # ========================================================================
    print("\n" + "-" * 78)
    print("[2] Leibniz-lift BmL to the 64-dim fibre; apply to round59's v_a, v_b, w")
    print("-" * 78)

    # BL on Sigma, as an explicit 8x8 diagonal matrix built from the SAME
    # degree formula as g15_hypercharge.py's BmL (verified above to agree
    # entrywise under the bijection). Built directly on dolan-casimir's own
    # SUBSETS ordering (IDX), not on G15's kron ordering -- this is the
    # entire point of step 1: the operator is basis-independent because it
    # depends only on |subset|.
    BL_sigma = sp.zeros(8, 8)
    for s in SUBSETS:
        BL_sigma[IDX[s], IDX[s]] = bl_degree_formula(s)
    print(
        f"    BL_sigma diagonal (dolan-casimir SUBSETS order): {[BL_sigma[i, i] for i in range(8)]}"
    )

    # Leibniz lift to the 64-dim fibre -- REUSES round59_route_b_consistency
    # .py's own leibniz64 function verbatim (line 91-106 of that file), just
    # fed BL_sigma instead of an su(3) generator matrix. This is the same
    # additive/Leibniz pattern the project already uses for su(3); nothing
    # new is invented here.
    BL_64 = leibniz64(BL_sigma)
    print(f"    BL_64 = leibniz64(BL_sigma) built ({BL_64.shape[0]}x{BL_64.shape[1]}).")
    is_diag_64 = all(BL_64[r, c] == 0 for r in range(N) for c in range(N) if r != c)
    print(f"    BL_64 is diagonal in the (sL,sR) product basis ? {is_diag_64}")
    report["BL_64_diagonal_in_product_basis"] = is_diag_64

    # Reconstruct v_a, v_b, w -- EXACT coefficient dict literal from
    # round59_route_b_consistency.py:219-221.
    v_a = vec64_from_pairs({((1,), (2, 3)): 1, ((2,), (1, 3)): -1, ((3,), (1, 2)): 1})
    v_b = vec64_from_pairs({((1, 2, 3), ()): 1})
    w = vec64_from_pairs({((), ()): 1})

    BLv_a = BL_64 * v_a
    BLv_b = BL_64 * v_b
    BLw = BL_64 * w

    # eigenvector check: BL(v) == lambda * v for some scalar lambda
    def eigen_check(v, BLv, name):
        nz = [k for k in range(N) if sp.simplify(v[k]) != 0]
        lambdas = {sp.simplify(BLv[k] / v[k]) for k in nz}
        is_eigvec = len(lambdas) == 1 and all(
            sp.simplify(BLv[k] - list(lambdas)[0] * v[k]) == 0 for k in range(N)
        )
        lam = list(lambdas)[0] if len(lambdas) == 1 else None
        print(f"    {name}: eigenvector={is_eigvec}, eigenvalue={lam}")
        return is_eigvec, lam

    va_eig, va_lam = eigen_check(v_a, BLv_a, "v_a")
    vb_eig, vb_lam = eigen_check(v_b, BLv_b, "v_b")
    w_eig, w_lam = eigen_check(w, BLw, "w (target invariant)")
    report["v_a_is_BL64_eigenvector"] = va_eig
    report["v_a_BL64_eigenvalue"] = str(va_lam)
    report["v_b_is_BL64_eigenvector"] = vb_eig
    report["v_b_BL64_eigenvalue"] = str(vb_lam)
    report["w_is_BL64_eigenvector"] = w_eig
    report["w_BL64_eigenvalue"] = str(w_lam)

    domain_common_eigenvalue = va_eig and vb_eig and sp.simplify(va_lam - vb_lam) == 0
    print(
        f"\n    v_a and v_b share the SAME BL_64 eigenvalue ({va_lam}) ? {domain_common_eigenvalue}"
    )
    report["domain_common_eigenvalue"] = domain_common_eigenvalue

    # -- recompute a, b (D-matrix elements) fresh, reusing D_full/herm
    #    unchanged, as a spot-check against round59's own cited a=-1, b=-sqrt3
    #    (decision.md) -- not a re-audit of dim_a=2/dim_b=1 (that search is
    #    reused by citation, not rerun here).
    nrm_va = sp.sqrt(sp.simplify(herm(v_a, v_a)))
    nrm_vb = sp.sqrt(sp.simplify(herm(v_b, v_b)))
    nrm_w = sp.sqrt(sp.simplify(herm(w, w)))
    u1 = sp.Matrix([sp.simplify(x / nrm_va) for x in v_a])
    u2 = sp.Matrix([sp.simplify(x / nrm_vb) for x in v_b])
    w_hat = sp.Matrix([sp.simplify(x / nrm_w) for x in w])

    Du1 = D_full(u1)
    Du2 = D_full(u2)
    a_coeff = sp.simplify(herm(w_hat, Du1))
    b_coeff = sp.simplify(herm(w_hat, Du2))
    print(f"\n    spot-check (fresh, using imported D_full/herm): a={a_coeff}, b={b_coeff}")
    print("    (round59 decision.md cites a=-1, b=-sqrt(3) -- must match)")
    a_b_match_decision = (sp.simplify(a_coeff + 1) == 0) and (sp.simplify(b_coeff + sqrt(3)) == 0)
    report["a_coeff"] = str(a_coeff)
    report["b_coeff"] = str(b_coeff)
    report["a_b_match_round59_decision_md"] = a_b_match_decision

    # kernel vector: nullspace of (alpha,beta) -> alpha*a_coeff + beta*b_coeff,
    # in the ORTHONORMAL (u1,u2) coordinates; lift back to raw (v_a,v_b).
    # solve alpha*a + beta*b = 0  ->  (alpha,beta) prop to (b, -a)
    alpha, beta = b_coeff, -a_coeff
    k_vec = sp.Matrix([sp.simplify(alpha * u1[i] + beta * u2[i]) for i in range(N)])
    Dk = D_full(k_vec)
    k_is_kernel = all(sp.simplify(x) == 0 for x in Dk)
    print(f"\n    kernel vector k = {alpha}*u1 + ({beta})*u2")
    print(f"    D_full(k) == 0 exactly (confirms k IS the physical kernel vector) ? {k_is_kernel}")
    report["kernel_vector_confirmed"] = k_is_kernel

    BLk = BL_64 * k_vec
    k_eig, k_lam = eigen_check(k_vec, BLk, "k (the physical twisted-kernel vector)")
    report["kernel_is_BL64_eigenvector"] = k_eig
    report["kernel_BL64_eigenvalue"] = str(k_lam)

    step2_pass = k_is_kernel and k_eig and va_eig and vb_eig and domain_common_eigenvalue
    print(f"\n    STEP 2 VERDICT: kernel vector is a genuine BL_64 eigenvector = {step2_pass}")
    report["step2_pass"] = step2_pass

    # ========================================================================
    # STEP 4 -- risk-lens check: does BL_64 commute with the FULL D_full?
    #    (Step 3 is skipped: step 1 found the spaces directly comparable, so
    #    there is no "not comparable" branch to report.)
    # ========================================================================
    print("\n" + "-" * 78)
    print("[4] Risk-lens: does BL_64 (built from su(3)+u(1)-only data) commute")
    print("    with the FULL twisted Dirac operator D_full (which uses the")
    print("    torsion/coset directions outside su(3)+u(1), per G98)?")
    print("-" * 78)

    # Fresh, direct check (not merely citing G98's so(6)-generator count):
    # does D_full preserve total Lambda-degree (sL,sR) |-> |sL|+|sR|? BL_64
    # is exactly a function of that total degree, so if D_full does NOT
    # preserve it, [BL_64, D_full] != 0 in general.
    # NOTE: an earlier draft of this check used y1(x)1 as the probe and found
    # D_full(y1(x)1) == 0 identically -- a degenerate, uninformative test
    # (both sides of any commutator vanish trivially). Probed 5 candidate
    # simple tensors directly (y1(x)1, y12(x)1, y1(x)y2, 1(x)y1, y1(x)y12);
    # y1(x)1 -- degree 1 in, D_full output supported ONLY at degree 4 -- is
    # the first with a manifestly nonzero D_full output, so it is used here.
    test_vec = vec64_from_pairs({((1,), ()): 1})  # y1 (x) 1, NOT su(3)-invariant
    D_test = D_full(test_vec)
    support_degrees = set()
    for sL in SUBSETS:
        for sR in SUBSETS:
            c = sp.simplify(D_test[fidx(sL, sR)])
            if c != 0:
                support_degrees.add(len(sL) + len(sR))
    print("    D_full(y1(x)1) [input total degree=1] has output support at total")
    print(f"    degrees: {sorted(support_degrees)}  (degree-preserving would mean == {{1}} only)")
    report["D_full_test_vec_output_degrees"] = sorted(support_degrees)
    report["D_full_test_vec_output_nonzero"] = len(support_degrees) > 0
    degree_preserving_on_test = support_degrees.issubset({1})

    # direct commutator check on the same test vector
    comm_val = BL_64 * D_full(test_vec) - D_full(BL_64 * test_vec)
    comm_nonzero = any(sp.simplify(x) != 0 for x in comm_val)
    print(f"    [BL_64, D_full] applied to y1(x)1 is nonzero ? {comm_nonzero}")
    report["BL64_Dfull_commutator_nonzero_on_test_vec"] = comm_nonzero

    print(
        "\n    Also: domain(v_a,v_b, total degree 3) -> target(w, total degree 0)"
        " under D_full is ITSELF a total-degree change of -3 (already"
        " established in dolan-casimir/round59's own construction,"
        " preprint.tex:806-812) -- an independent confirmation that D_full does"
        " NOT preserve total Lambda-degree in general."
    )
    report["domain_to_target_degree_shift"] = -3

    risk_confirmed = comm_nonzero or (not degree_preserving_on_test)
    print(f"\n    RISK CONFIRMED: BL_64 does NOT commute with D_full in general = {risk_confirmed}")
    report["risk_confirmed_BL64_not_commute_with_Dfull"] = risk_confirmed

    # But: does this risk actually threaten the STEP-2 eigenvalue claim?
    # It would threaten it only if the specific 2-dim domain block were NOT
    # entirely a single BL_64-eigenspace -- already checked directly above
    # (domain_common_eigenvalue). Restate the logic explicitly here.
    risk_neutralized_for_this_claim = domain_common_eigenvalue and k_eig
    print(
        f"    Does this risk undermine the step-2 kernel eigenvalue claim "
        f"specifically? risk_neutralized_for_this_claim = "
        f"{risk_neutralized_for_this_claim}"
    )
    print(
        "    (Reason: BL_64's eigenvalue on the KERNEL does not depend on"
        " a,b -- the D-matrix elements that DO depend on the coset/torsion"
        " structure -- because the ENTIRE 2-dim domain, not just the kernel"
        " direction within it, is already a single BL_64 eigenspace,"
        " confirmed above by direct computation on v_a and v_b separately.)"
    )
    report["risk_neutralized_for_this_specific_claim"] = risk_neutralized_for_this_claim

    # ========================================================================
    # FINAL VERDICT
    # ========================================================================
    print("\n" + "=" * 78)
    print("FINAL VERDICT")
    print("=" * 78)
    if structurally_comparable and step2_pass:
        verdict = "PASS_WITH_DOCUMENTED_CAVEAT"
    elif not structurally_comparable:
        verdict = "BLOCKED"
    else:
        verdict = "FAIL"
    print(f"  structurally_comparable = {structurally_comparable}")
    print(f"  step2_pass (kernel is BL_64 eigenvector) = {step2_pass}")
    print(f"  kernel BL_64 eigenvalue = {k_lam}")
    print(f"  risk_confirmed (BL_64 !commute D_full in general) = {risk_confirmed}")
    print(f"  risk_neutralized_for_this_specific_claim = {risk_neutralized_for_this_claim}")
    print(f"\n  VERDICT: {verdict}")
    report["verdict"] = verdict

    out_path = os.path.join(_HERE, "results_e24.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, default=str)

    print("\nMACHINE_REPORT " + repr(report))
    return report


if __name__ == "__main__":
    main()
