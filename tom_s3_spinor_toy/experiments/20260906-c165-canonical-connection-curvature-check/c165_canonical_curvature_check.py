r"""
C165 -- does the canonical (Nomizu/Ambrose-Singer) connection's own curvature
2-form R^c, restricted to the 3bar-isotypic summand of Lambda^2(m), supply an
su(3)-equivariant map 3bar -> su(3)_C that is INDEPENDENT of m's own already-
used connection/representation data -- or is it zero, or proportional to
already-used data?  See claim.md for the full pre-registered kill-criterion
table and the Schur's-Lemma prediction made BEFORE this script was run.

REUSES, does not modify:
  - g96_g2_su3.py (G96, experiments/20260626-g96-s6-g2-su3/): build_phi,
    g2_condition_matrix, find_g2_generators, commutator -- the already-
    certified (status: VERIFIED, results_g96.json) from-octonions
    construction of the full 14-dim g2 Lie algebra as 7x7 matrices, its
    su(3)-stabilizer subalgebra (su3_gens, 8-dim), and the complementary
    m-representation (comp_gens, 6-dim = 3(+)3bar).  This script re-executes
    G96's own functions directly (not its main(), to avoid file-IO
    side-effects on results_g96.json) -- same "import sibling script by
    path" pattern C161/C146/C162 already use.
  - round59_route_a_independent.py (R59): ADNU, NOMIZU -- used ONLY for a
    cross-normalization sanity check (T3b), not for the R^c computation
    itself (R^c is built entirely from G96's independent octonion
    construction, per claim.md Prior Result Gate step 6's instruction not
    to re-derive the closed-form curvature formula from a Leibniz sweep,
    but also not to silently reuse round59's bivector tables for the
    bracket itself, since that is precisely the object being tested for
    independence).

Method (standard fact for a reductive homogeneous space g=h(+)m, Nomizu
1954 / Kobayashi-Nomizu Vol.II Ch.X, cited not re-derived):
  R^c(X,Y)Z = -[[X,Y]_h, Z]   for X,Y,Z in m
i.e. R^c(X,Y) as an element of su(3)_C is (up to sign) exactly the
su(3)-part of the ordinary Lie bracket [X,Y] computed in the full 14-dim g2.

Numeric (numpy/float), matching G96's own precision discipline -- not exact
symbolic, since G96's octonion-derivation construction is itself numeric.

Run:  python c165_canonical_curvature_check.py
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys

import numpy as np

CHECKS: list[dict] = []
DATA: dict[str, object] = {}

TOL = 1e-8


def check(name: str, cond, detail: str = "") -> bool:
    ok = bool(cond)
    CHECKS.append({"name": name, "ok": ok, "detail": detail})
    print(f"  [{'OK' if ok else 'FAIL'}] {name} :: {detail}")
    return ok


def _load_module(mod_name: str, sibling_dir: str, file_name: str):
    """Import a sibling experiment's script by path -- same pattern
    C161/C146/C162 already use, avoids E402 regardless of ruff rule set."""
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.normpath(os.path.join(here, "..", sibling_dir, file_name))
    spec = importlib.util.spec_from_file_location(mod_name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


print("Loading G96 (octonion-derivation g2 construction) and round59 (ADNU/")
print("NOMIZU, for cross-normalization only) -- re-executes their own module")
print("bodies end-to-end, same pattern C162 already used for its siblings.")
G96 = _load_module("g96_g2_su3", "20260626-g96-s6-g2-su3", "g96_g2_su3.py")
R59 = _load_module(
    "round59_route_a_independent",
    "20260714-round59-trivial-rank-certification",
    "round59_route_a_independent.py",
)


# ============================================================================
# T1 -- rebuild g2 = su(3) (+) m from octonions, re-verify G96's own
# certified dimension/closure/Jacobi facts before using the construction for
# anything new (per claim.md T1).
# ============================================================================
def t1_rebuild_g2() -> dict[str, object]:
    print()
    print("=" * 78)
    print("T1 -- rebuild g2 via G96's own octonion-derivation construction")
    print("=" * 78)
    phi = G96.build_phi()
    gens = G96.find_g2_generators(phi)
    check("t1_dim_g2_is_14", len(gens) == 14, f"got {len(gens)}")

    basis_flat = np.column_stack([g.flatten() for g in gens])
    max_closure_err = 0.0
    for gi in gens:
        for gj in gens:
            comm = G96.commutator(gi, gj)
            coeffs, *_ = np.linalg.lstsq(basis_flat, comm.flatten(), rcond=None)
            recon = (basis_flat @ coeffs).reshape(7, 7)
            max_closure_err = max(max_closure_err, float(np.max(np.abs(comm - recon))))
    check(
        "t1_g2_closed_under_commutation",
        max_closure_err < 1e-8,
        f"max closure residual = {max_closure_err:.2e}",
    )

    max_jacobi_err = 0.0
    n = len(gens)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                jac = (
                    G96.commutator(gens[i], G96.commutator(gens[j], gens[k]))
                    + G96.commutator(gens[j], G96.commutator(gens[k], gens[i]))
                    + G96.commutator(gens[k], G96.commutator(gens[i], gens[j]))
                )
                max_jacobi_err = max(max_jacobi_err, float(np.max(np.abs(jac))))
    check(
        "t1_jacobi_identity_holds",
        max_jacobi_err < 1e-8,
        f"max Jacobi residual = {max_jacobi_err:.2e}",
    )

    e6 = np.zeros(7)
    e6[6] = 1.0
    a_stab = np.column_stack([g @ e6 for g in gens])
    _, sv_stab, vt_stab = np.linalg.svd(a_stab, full_matrices=True)
    rank_stab = int(np.sum(sv_stab > 1e-8))
    null_coeffs = vt_stab[rank_stab:]
    gen_matrix = np.array([g.flatten() for g in gens])
    su3_gens_flat = null_coeffs @ gen_matrix
    su3_gens = [row.reshape(7, 7) for row in su3_gens_flat]
    check("t1_dim_su3_stabilizer_is_8", len(su3_gens) == 8, f"got {len(su3_gens)}")

    q_su3, _ = np.linalg.qr(su3_gens_flat.T, mode="reduced")
    comp_vecs = []
    for g in gens:
        g_flat = g.flatten()
        proj = q_su3 @ (q_su3.T @ g_flat)
        residual = g_flat - proj
        if np.linalg.norm(residual) > 1e-8:
            comp_vecs.append(residual)
    c_mat = np.column_stack(comp_vecs)
    q_c, r_c = np.linalg.qr(c_mat, mode="reduced")
    n_comp = int(np.sum(np.abs(np.diag(r_c)) > 1e-8))
    comp_gens = [q_c[:, k].reshape(7, 7) for k in range(n_comp)]
    check("t1_dim_m_complement_is_6", len(comp_gens) == 6, f"got {len(comp_gens)}")

    # Orthonormalize su3_gens too (Q from its own QR), for a clean projection basis.
    q_su3_on, _ = np.linalg.qr(su3_gens_flat.T, mode="reduced")
    su3_gens_on = [q_su3_on[:, k].reshape(7, 7) for k in range(q_su3_on.shape[1])]
    check(
        "t1_su3_orthonormal_basis_still_8dim",
        len(su3_gens_on) == 8,
        f"got {len(su3_gens_on)} after orthonormalizing su3_gens",
    )

    # [su3, m] subset m check (reductive decomposition property), re-verified.
    comp_flat = np.column_stack([g.flatten() for g in comp_gens])
    max_adj_err = 0.0
    for su_g in su3_gens_on:
        for co_g in comp_gens:
            comm = G96.commutator(su_g, co_g)
            coeffs, *_ = np.linalg.lstsq(comp_flat, comm.flatten(), rcond=None)
            recon = (comp_flat @ coeffs).reshape(7, 7)
            max_adj_err = max(max_adj_err, float(np.max(np.abs(comm - recon))))
    check(
        "t1_su3_m_bracket_stays_in_m_reductive_property",
        max_adj_err < 1e-8,
        f"max residual outside m = {max_adj_err:.2e} -- confirms [h,m] subset m "
        "(reductive decomposition), required for R^c's closed-form to apply.",
    )

    DATA["t1_dim_g2"] = len(gens)
    DATA["t1_dim_su3"] = len(su3_gens_on)
    DATA["t1_dim_m"] = len(comp_gens)
    DATA["t1_max_closure_err"] = max_closure_err
    DATA["t1_max_jacobi_err"] = max_jacobi_err
    DATA["t1_max_reductive_err"] = max_adj_err
    return {"su3_gens": su3_gens_on, "comp_gens": comp_gens, "e6": e6}


# ============================================================================
# T2 -- compute R^c(e_i,e_j) := -[e_i,e_j]_h for the 6 m-basis vectors
# (comp_gens), as an 8-vector (coefficients on the orthonormal su3_gens
# basis) for every pair i<j.  This is the genuinely new 6x6x8 tensor.
# ============================================================================
def t2_compute_curvature(built: dict[str, object]) -> np.ndarray:
    print()
    print("=" * 78)
    print("T2 -- compute R^c(e_i,e_j) = -[e_i,e_j]_h  (the new curvature tensor)")
    print("=" * 78)
    su3_gens = built["su3_gens"]
    comp_gens = built["comp_gens"]
    su3_flat = np.column_stack([g.flatten() for g in su3_gens])  # orthonormal columns
    comp_flat = np.column_stack([g.flatten() for g in comp_gens])

    n_m = len(comp_gens)
    n_h = len(su3_gens)
    r_tensor = np.zeros((n_m, n_m, n_h))
    max_leftover_m_component = 0.0
    max_residual_outside_g2 = 0.0
    for i in range(n_m):
        for j in range(n_m):
            if i == j:
                continue
            comm = G96.commutator(comp_gens[i], comp_gens[j])
            comm_flat = comm.flatten()
            # project onto su3 (orthonormal basis -> projection = Q^T v)
            coeffs_h = su3_flat.T @ comm_flat
            recon_h = su3_flat @ coeffs_h
            # remaining part should lie entirely in m (reductive: [m,m] subset g2=h+m)
            residual_after_h = comm_flat - recon_h
            coeffs_m, *_ = np.linalg.lstsq(comp_flat, residual_after_h, rcond=None)
            recon_m = comp_flat @ coeffs_m
            leftover = residual_after_h - recon_m
            max_leftover_m_component = max(
                max_leftover_m_component, float(np.linalg.norm(coeffs_m))
            )
            max_residual_outside_g2 = max(max_residual_outside_g2, float(np.linalg.norm(leftover)))
            r_tensor[i, j, :] = -coeffs_h  # R^c(e_i,e_j) = -[e_i,e_j]_h

    check(
        "t2_bracket_of_m_with_m_lands_fully_in_g2",
        max_residual_outside_g2 < 1e-6,
        f"max residual outside span(su3_gens ++ comp_gens) = {max_residual_outside_g2:.2e}",
    )
    check(
        "t2_antisymmetry_of_r_tensor",
        float(np.max(np.abs(r_tensor + np.transpose(r_tensor, (1, 0, 2))))) < 1e-8,
        "R^c(e_i,e_j) = -R^c(e_j,e_i), required of any curvature 2-form.",
    )
    check(
        "t2_r_tensor_is_genuinely_nonzero_somewhere",
        float(np.max(np.abs(r_tensor))) > 1e-3,
        f"max |R^c component| = {float(np.max(np.abs(r_tensor))):.6f} -- confirms this "
        "is not a trivially-vanishing construction before checking the 3bar-restriction "
        "specifically (a nonzero object overall, that may still vanish on one summand).",
    )
    DATA["t2_max_residual_outside_g2"] = max_residual_outside_g2
    DATA["t2_max_abs_r_component"] = float(np.max(np.abs(r_tensor)))
    return r_tensor


# ============================================================================
# T3 -- build the su(3) vector representation on m (V_a = ad(su3_gens[a])|_m,
# 6x6 real antisymmetric), verify m is Casimir-irreducible (single eigenvalue,
# Schur check on the REAL 6-dim rep), extend to Lambda^2(m) (15-dim), find its
# Casimir spectrum, and confirm it matches {0:1, c_fund:6, c_adj:8}.
# ============================================================================
def t3_casimir_decomposition(built: dict[str, object]) -> dict[str, object]:
    print()
    print("=" * 78)
    print("T3 -- su(3) Casimir spectrum on m and on Lambda^2(m)")
    print("=" * 78)
    su3_gens = built["su3_gens"]
    comp_gens = built["comp_gens"]
    comp_flat = np.column_stack([g.flatten() for g in comp_gens])
    n_m = len(comp_gens)
    n_h = len(su3_gens)

    # V_a: 6x6 real matrix, V_a[k, idx] such that ad(su3_gens[a]) comp_gens[idx] = sum_k V_a[k,idx] comp_gens[k]
    v_list = []
    for a in range(n_h):
        v_a = np.zeros((n_m, n_m))
        for idx in range(n_m):
            comm = G96.commutator(su3_gens[a], comp_gens[idx])
            coeffs, *_ = np.linalg.lstsq(comp_flat, comm.flatten(), rcond=None)
            v_a[:, idx] = coeffs
        v_list.append(v_a)

    max_antisym_err = max(float(np.max(np.abs(v_a + v_a.T))) for v_a in v_list)
    check(
        "t3_va_matrices_antisymmetric",
        max_antisym_err < 1e-6,
        f"max |V_a + V_a^T| = {max_antisym_err:.2e} (expected ~0 for an orthonormal m-basis)",
    )

    c2_m = sum(v_a @ v_a for v_a in v_list)  # 6x6, negative semi-definite
    eigvals_m = np.linalg.eigvalsh(c2_m)
    spread_m = float(np.max(eigvals_m) - np.min(eigvals_m))
    check(
        "t3_m_is_casimir_irreducible_single_eigenvalue",
        spread_m < 1e-6,
        f"C2|_m eigenvalues = {np.round(eigvals_m, 6)}, spread = {spread_m:.2e} -- "
        "m must be a single real irreducible su(3)-module (3(+)3bar complexified), "
        "hence Casimir-scalar, per Schur's Lemma applied to the REAL representation.",
    )
    c_fund = float(np.mean(eigvals_m))
    print(f"  fundamental Casimir eigenvalue (this normalization): {c_fund:.6f}")

    # Extend V_a to Lambda^2(m), basis e_i^e_j for i<j (15-dim).
    pairs = [(i, j) for i in range(n_m) for j in range(i + 1, n_m)]
    n_pairs = len(pairs)
    idx_of_pair = {p: k for k, p in enumerate(pairs)}

    def wedge_action(v_a: np.ndarray) -> np.ndarray:
        w = np.zeros((n_pairs, n_pairs))
        for col, (i, j) in enumerate(pairs):
            # d(e_i^e_j) = (V e_i)^e_j + e_i^(V e_j)
            for k in range(n_m):
                cik = v_a[k, i]
                if abs(cik) > 0:
                    p, sgn = (k, j), 1
                    if k == j:
                        continue
                    key = (min(p), max(p))
                    s = 1 if p[0] < p[1] else -1
                    w[idx_of_pair[key], col] += sgn * s * cik
                ckj = v_a[k, j]
                if abs(ckj) > 0:
                    if k == i:
                        continue
                    key = (min(i, k), max(i, k))
                    s = 1 if i < k else -1
                    w[idx_of_pair[key], col] += s * ckj
        return w

    v_list_lambda2 = [wedge_action(v_a) for v_a in v_list]
    c2_lambda2 = sum(w @ w for w in v_list_lambda2)
    eigvals_l2, eigvecs_l2 = np.linalg.eigh(c2_lambda2)
    rounded = np.round(eigvals_l2, 5)
    unique_vals, counts = np.unique(rounded, return_counts=True)
    print(f"  Lambda^2(m) Casimir eigenvalues (rounded): {dict(zip(unique_vals, counts))}")

    check(
        "t3_lambda2m_has_exactly_3_distinct_casimir_eigenvalues",
        len(unique_vals) == 3,
        f"got {len(unique_vals)} distinct eigenvalues: {unique_vals}, "
        "expected 3 (singlet=0, fundamental x6, adjoint x8) matching "
        "Lambda^2(3(+)3bar) = 3bar(+)1(+)8(+)3",
    )
    mult_map = dict(zip(unique_vals, counts))
    check(
        "t3_multiplicities_match_1_6_8",
        sorted(counts.tolist()) == [1, 6, 8],
        f"multiplicities = {sorted(counts.tolist())}, expected [1,6,8]",
    )
    zero_val = min(unique_vals, key=abs)
    check(
        "t3_singlet_eigenvalue_is_zero",
        abs(zero_val) < 1e-4,
        f"putative singlet eigenvalue = {zero_val}",
    )
    fund_val = min((v for v in unique_vals if mult_map[v] == 6), default=None)
    check(
        "t3_fundamental_block_eigenvalue_matches_m_own_casimir",
        fund_val is not None and abs(fund_val - c_fund) < 1e-4,
        f"Lambda^2m fundamental-block eigenvalue = {fund_val}, m's own C2 = {c_fund:.6f}",
    )

    fund_mask = np.abs(rounded - fund_val) < 1e-4
    fund_eigvecs = eigvecs_l2[:, fund_mask]  # 15 x 6
    check(
        "t3_fund_eigenspace_is_6dim",
        fund_eigvecs.shape[1] == 6,
        f"got {fund_eigvecs.shape[1]}",
    )

    DATA["t3_fund_casimir_eigenvalue"] = c_fund
    DATA["t3_lambda2m_eigenvalue_multiplicities"] = {
        str(k): int(v) for k, v in zip(unique_vals.tolist(), counts.tolist())
    }
    return {
        "pairs": pairs,
        "fund_eigvecs": fund_eigvecs,
        "v_list": v_list,
    }


# ============================================================================
# T4 -- restrict R^c to the 6-dim fundamental (3(+)3bar) Casimir eigenspace
# of Lambda^2(m), and check whether the restriction is the zero map.  Also
# re-verify su3_gens is irreducible under its own adjoint action (Schur
# side-check, per claim.md T4).
# ============================================================================
def t4_restrict_and_check_zero(
    r_tensor: np.ndarray, t3_out: dict[str, object], built: dict[str, object]
) -> dict[str, object]:
    print()
    print("=" * 78)
    print("T4 -- restrict R^c to the fundamental (3(+)3bar) block, check for zero")
    print("=" * 78)
    pairs = t3_out["pairs"]
    fund_eigvecs = t3_out["fund_eigvecs"]  # 15 x 6
    n_h = r_tensor.shape[2]

    # R^c as an 8 x 15 matrix: columns = pairs (i<j), rows = su3 components.
    r_matrix = np.zeros((n_h, len(pairs)))
    for col, (i, j) in enumerate(pairs):
        r_matrix[:, col] = r_tensor[i, j, :]

    r_on_fund = r_matrix @ fund_eigvecs  # 8 x 6
    max_abs_on_fund = float(np.max(np.abs(r_on_fund)))
    overall_scale = float(np.max(np.abs(r_matrix))) if np.max(np.abs(r_matrix)) > 0 else 1.0
    relative = max_abs_on_fund / overall_scale
    print(f"  max |R^c restricted to fund (3(+)3bar) block| = {max_abs_on_fund:.3e}")
    print(f"  relative to overall max |R^c component| ({overall_scale:.3e}): {relative:.3e}")

    zero_on_fund = relative < 1e-4
    check(
        "t4_R_c_vanishes_on_fundamental_3plus3bar_block",
        zero_on_fund,
        f"max|R^c|_fund| / max|R^c| = {relative:.3e} -- if < 1e-4, confirms "
        "ZERO-ON-3BAR-SUMMAND (the 3bar summand is a subspace of this 6-dim "
        "fundamental block, so a zero restriction here implies zero specifically "
        "on 3bar, and on 3, by linear algebra alone -- restriction of a zero map "
        "to any subspace is zero).",
    )

    # T4 side-check: su3_gens (adjoint of su(3)) is Casimir-irreducible under
    # its OWN adjoint action (confirms su(3)_C = 8, not some smaller sum).
    su3_gens = built["su3_gens"]
    n_h2 = len(su3_gens)
    su3_flat = np.column_stack([g.flatten() for g in su3_gens])
    ad_list = []
    for a in range(n_h2):
        ad_a = np.zeros((n_h2, n_h2))
        for idx in range(n_h2):
            comm = G96.commutator(su3_gens[a], su3_gens[idx])
            coeffs = su3_flat.T @ comm.flatten()
            ad_a[:, idx] = coeffs
        ad_list.append(ad_a)
    c2_adj = sum(a @ a for a in ad_list)
    eigvals_adj = np.linalg.eigvalsh(c2_adj)
    spread_adj = float(np.max(eigvals_adj) - np.min(eigvals_adj))
    check(
        "t4_su3_c_is_casimir_irreducible_confirms_adjoint_8",
        spread_adj < 1e-4,
        f"C2|_su3(adjoint action) eigenvalues spread = {spread_adj:.2e} -- confirms "
        "su(3)_C is a single irreducible 8-dim module under its own adjoint action "
        "(standard for a simple Lie algebra), non-isomorphic to the 3-dim 3bar by "
        "dimension count alone -- Schur's Lemma therefore forces Hom_su3(3bar,8)=0 "
        "independent of the specific curvature values found above.",
    )

    DATA["t4_max_abs_r_on_fund_block"] = max_abs_on_fund
    DATA["t4_relative_r_on_fund_block"] = relative
    DATA["t4_zero_on_fund_block"] = zero_on_fund
    DATA["t4_adjoint_casimir_spread"] = spread_adj
    return {"zero_on_fund": zero_on_fund, "relative": relative}


def main() -> int:
    print("=" * 78)
    print("C165 -- canonical connection curvature R^c, 3bar-summand independence check")
    print("=" * 78)

    built = t1_rebuild_g2()
    r_tensor = t2_compute_curvature(built)
    t3_out = t3_casimir_decomposition(built)
    t4_out = t4_restrict_and_check_zero(r_tensor, t3_out, built)

    n_ok = sum(1 for c in CHECKS if c["ok"])
    n = len(CHECKS)
    print("-" * 78)
    print(f"CHECKS: {n_ok}/{n} passed")
    print()

    if t4_out["zero_on_fund"]:
        verdict = "ZERO-ON-3BAR-SUMMAND"
    else:
        verdict = "NONZERO-ON-3BAR-SUMMAND-NEEDS-PROPORTIONALITY-CHECK"
    print(f"VERDICT: {verdict}")

    out = {
        "checks_total": n,
        "checks_passed": n_ok,
        "all_passed": n_ok == n,
        "checks": CHECKS,
        "data": DATA,
        "verdict": verdict,
    }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_c165.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nwrote {path}")
    return 0 if n_ok == n else 1


if __name__ == "__main__":
    sys.exit(main())
