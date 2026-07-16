"""
Fresh, independent check (2026-07-16): does Round 22's 5-piece decomposition
of D_7^2 (CASIMIR + D64-SQUARED + SU(3)-CURVATURE + TORSION + MIXED_A-B,
g2su3_nomizu_crossterms.py) generalize to D_14^2 on M_14 = Hom_SU(3)(V_14, F)
(the rho=14 adjoint-representation danger zone, g2su3_v14_adjoint_full_matrix.py)?

WHY THIS SCRIPT EXISTS: a prior session claim -- "built the rho=14 analog,
exact match on all 12/12 basis vectors" -- was reported as NOT FOUND anywhere
in the repo (no file, no decision.md entry, no test). This script is a
from-scratch, honest attempt to actually do the construction and report
exactly what happens, without assuming the prior claim was correct.

CONSTRUCTION: reuses V_7's decomposition formula (Round 22) verbatim in
structure, substituting rho=14 representation data:
  - rho_7(e_p)  -> ADE[p]      (ad(e_p) on full 14-dim adjoint, RAW convention,
                                 g2su3_v14_adjoint_full_matrix.build_ad_ep_raw)
  - rho_7(nu_k) -> AD_RAW[k]   (ad(nu_k) on full 14-dim adjoint, RAW convention,
                                 g2su3_v14_adjoint_full_matrix.ad_gen_raw)
  - domain dim 7 -> domain dim 14
T(p,q,r) and curv_h(p,q,k) tables are UNCHANGED (they are properties of the
g2 bracket itself, not of which representation V_7/V_14 is being acted on).

SIGN CONVENTION: Round 22 found empirically that rho_7(e_p) (RAW nu-matrix
convention, no BRACKET_SIGN correction) satisfies
[rho_7(e_p),rho_7(e_q)] = -rho_7([e_p,e_q]) relative to the T/curv_h tables'
own bracket orientation (which ARE built with BRACKET_SIGN=-1 applied, see
g2su3_appendix_a_construction.bracket_e). ADE/AD_RAW (this file's V_14 inputs)
are ALSO built via the RAW convention (g2su3_v14_adjoint_full_matrix.py's
ad_gen_raw/build_ad_ep_raw apply NO BRACKET_SIGN correction) -- so the SAME
sign relationship is expected to hold. This is checked, not assumed: BOTH
sign choices are tried below and compared directly against the ground-truth
D^2_14 matrix rather than asserting one in advance.

GROUND TRUTH: g2su3_v14_adjoint_full_matrix.py's own D^2_14 12x12 matrix,
via its d14_apply (already independently built/reviewed, Round 20), applied
twice to each of the 12 basis intertwiners, exactly as that file's main()
does (STEP 8).
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table, decompose_g2, nu
from g2su3_equivariance_check import build_D_matrix64
from g2su3_explicit_clifford import DIM, IDX
from g2su3_H_element import build_T_table
from g2su3_nomizu_crossterms import build_Mp_matrices
from g2su3_v14_adjoint_full_matrix import (
    build_ad_ep_raw,
    build_eight_copy,
    build_MV14_m,
    build_v14_m_weight_vectors,
    check_only_trivial_solution,
    d14_apply,
    flatten14,
    solve_intertwiner_general,
    verify_closure_m,
)
from g2su3_v7_16dim_full_matrix import build_3_copies, build_3bar_copies
from g2su3_v7_3_3bar_intertwiners import build_MF

N64 = DIM * DIM


def ad_gen_raw(a):
    """ad(nu_a) on the full 14-dim g2, RAW commutator -- same as
    g2su3_v14_adjoint_full_matrix.ad_gen_raw, reimported here directly since
    that file does not export it as a top-level name usable without
    reconstruction (it is only used inline in that file's main())."""
    M = sp.zeros(14, 14)
    for k in range(1, 15):
        comm = sp.simplify(nu(a) * nu(k) - nu(k) * nu(a))
        coeffs = decompose_g2(comm)
        for idx_l, v in coeffs.items():
            M[idx_l - 1, k - 1] = v
    return M


def e_i14(i):
    v = sp.zeros(14, 1)
    v[i] = 1
    return v


def w_at14(w_cols, vec14):
    out = sp.zeros(N64, 1)
    for j in range(14):
        if vec14[j] != 0:
            out += vec14[j] * w_cols[j]
    return out


def casimir_term14(w_cols, i, ADE):
    M_cas = sp.zeros(14, 14)
    for p in range(1, 7):
        M_cas += ADE[p] * ADE[p]
    return -w_at14(w_cols, M_cas * e_i14(i))


def termB_squared14(w_cols, i, D64):
    return sp.simplify(D64 * (D64 * w_cols[i]))


def su3_curvature_term14(w_cols, i, Ms, curv_h, AD_RAW, sign=1):
    out = sp.zeros(N64, 1)
    for (p, q, k), coeff in curv_h.items():
        Mnk14 = AD_RAW[k]
        w_val = w_at14(w_cols, Mnk14 * e_i14(i))
        if w_val == sp.zeros(N64, 1):
            continue
        out += coeff * (Ms[p] * (Ms[q] * w_val))
    return sign * out


def torsion_cross_term14(w_cols, i, Ms, T, ADE, sign=1):
    out = sp.zeros(N64, 1)
    for (p, q, r), coeff in T.items():
        if p >= q:
            continue
        Mr14 = ADE[r]
        w_val = w_at14(w_cols, Mr14 * e_i14(i))
        if w_val == sp.zeros(N64, 1):
            continue
        out += coeff * (Ms[p] * (Ms[q] * w_val))
    return sign * out


def mixed_AB_term14(w_cols, i, Ms, D64, ADE):
    out = sp.zeros(N64, 1)
    for p in range(1, 7):
        Mp14 = ADE[p]
        w_val = w_at14(w_cols, Mp14 * e_i14(i))
        if w_val == sp.zeros(N64, 1):
            continue
        AC_p = Ms[p] * D64 + D64 * Ms[p]
        out += AC_p * w_val
    return -out


def reconstruct_D2_14_full(w_cols, Ms, D64, T, curv_h, ADE, AD_RAW, sign):
    parts = {name: [] for name in ("casimir", "termB_sq", "su3_curv", "torsion", "mixed_AB")}
    for i in range(14):
        parts["casimir"].append(sp.simplify(casimir_term14(w_cols, i, ADE)))
        parts["termB_sq"].append(termB_squared14(w_cols, i, D64))
        parts["su3_curv"].append(
            sp.simplify(su3_curvature_term14(w_cols, i, Ms, curv_h, AD_RAW, sign))
        )
        parts["torsion"].append(sp.simplify(torsion_cross_term14(w_cols, i, Ms, T, ADE, sign)))
        parts["mixed_AB"].append(sp.simplify(mixed_AB_term14(w_cols, i, Ms, D64, ADE)))
    total = []
    for i in range(14):
        s = sp.zeros(N64, 1)
        for name in parts:
            s += parts[name][i]
        total.append(sp.simplify(s))
    return total, parts


def build_basis_w_and_ADE_etc():
    """Reproduces g2su3_v14_adjoint_full_matrix.py's main() STEPs 1-7 to get
    basis_w (12 intertwiners), labels, ADE, AD_RAW, without re-deriving
    anything -- calls that file's own functions verbatim."""
    AD_RAW = {a: ad_gen_raw(a) for a in range(1, 15)}

    group1_vecs, group2_vecs, mblock = build_v14_m_weight_vectors()
    P_g1 = sp.Matrix.hstack(*group1_vecs)
    P_g2 = sp.Matrix.hstack(*group2_vecs)
    Pfull = sp.Matrix.hstack(*group1_vecs, *group2_vecs)
    Pinv = Pfull.inv()
    ok1 = verify_closure_m(mblock, P_g1, slice(3, 6), Pinv)
    ok2 = verify_closure_m(mblock, P_g2, slice(0, 3), Pinv)
    assert ok1 and ok2

    MV14_g1 = build_MV14_m(mblock, P_g1, slice(0, 3), Pinv)
    MV14_g2 = build_MV14_m(mblock, P_g2, slice(3, 6), Pinv)
    MF_3 = build_MF([(1,), (2,), (3,)])
    MF_3bar = build_MF([(1, 2), (1, 3), (2, 3)])

    T3 = solve_intertwiner_general(MV14_g1, MF_3bar, 3)
    T4 = solve_intertwiner_general(MV14_g2, MF_3, 3)
    assert check_only_trivial_solution(MV14_g1, MF_3, 3)
    assert check_only_trivial_solution(MV14_g2, MF_3bar, 3)

    def ad_nuk_su3block_raw(i):
        M = sp.zeros(8, 8)
        for k in range(1, 9):
            comm = sp.simplify(nu(i) * nu(k) - nu(k) * nu(i))
            coeffs = decompose_g2(comm)
            for idx_l, v in coeffs.items():
                if idx_l <= 8:
                    M[idx_l - 1, k - 1] = v
        return M

    MV14_8 = {i: ad_nuk_su3block_raw(i) for i in range(1, 9)}
    y1i, y2i, y3i = IDX[(1,)], IDX[(2,)], IDX[(3,)]
    y12i, y13i, y23i = IDX[(1, 2)], IDX[(1, 3)], IDX[(2, 3)]
    eight_L, T5 = build_eight_copy([y1i, y2i, y3i], [y23i, y13i, y12i], MV14_8)
    eight_R, T6 = build_eight_copy([y23i, y13i, y12i], [y1i, y2i, y3i], MV14_8)

    threes = build_3_copies()
    threebars = build_3bar_copies()

    def build_w14_su3(T, eight_target):
        cols = []
        for j in range(8):
            ej3 = sp.zeros(8, 1)
            ej3[j] = 1
            mapped = T * ej3
            vecF = sum((mapped[row] * eight_target[row] for row in range(8)), sp.zeros(N64, 1))
            cols.append(sp.simplify(vecF))
        cols += [sp.zeros(N64, 1) for _ in range(6)]
        return cols

    def build_w14_m(T, target_vecs, group_P, this_rows):
        cols = [sp.zeros(N64, 1) for _ in range(8)]
        I6 = sp.eye(6)
        for j in range(6):
            ej = I6[:, j]
            coeffs = Pinv * ej
            group_coeffs = coeffs[this_rows, :]
            mapped = T * group_coeffs
            vecF = sum((mapped[row] * target_vecs[row] for row in range(3)), sp.zeros(N64, 1))
            cols.append(sp.simplify(vecF))
        return cols

    basis_w = []
    labels = []
    basis_w.append(build_w14_su3(T5, eight_L))
    labels.append("eight_L")
    basis_w.append(build_w14_su3(T6, eight_R))
    labels.append("eight_R")
    for i, triple in enumerate(threes):
        basis_w.append(build_w14_m(T4, triple, P_g2, slice(3, 6)))
        labels.append(f"three_{i + 1}")
    for i, triple in enumerate(threebars):
        basis_w.append(build_w14_m(T3, triple, P_g1, slice(0, 3)))
        labels.append(f"threebar_{i + 1}")

    ADE = build_ad_ep_raw()
    return basis_w, labels, ADE, AD_RAW


def main():
    print("=" * 70)
    print("SETUP")
    print("=" * 70)
    D64 = build_D_matrix64()
    T = build_T_table()
    curv_h = build_curvature_h_table()
    Ms = build_Mp_matrices()
    basis_w, labels, ADE, AD_RAW = build_basis_w_and_ADE_etc()
    print(f"  built {len(basis_w)} basis intertwiners: {labels}")

    print("\n" + "=" * 70)
    print("STEP A: ground truth D^2_14(w) for each of the 12 basis elements,")
    print("via g2su3_v14_adjoint_full_matrix.d14_apply (already-reviewed, Round 20)")
    print("=" * 70)
    ground_truth = {}
    for w, label in zip(basis_w, labels, strict=True):
        w_prime = d14_apply(w, D64, ADE)
        w_double = d14_apply(w_prime, D64, ADE)
        ground_truth[label] = w_double
        print(f"  ground truth D^2_14({label}) computed")

    print("\n" + "=" * 70)
    print("STEP B: 5-piece reconstruction, sign=+1 (Round 22's V_7 sign choice)")
    print("=" * 70)
    n_match_plus = 0
    max_residual_plus = {}
    for w, label in zip(basis_w, labels, strict=True):
        total, parts = reconstruct_D2_14_full(w, Ms, D64, T, curv_h, ADE, AD_RAW, sign=1)
        diff = sp.simplify(flatten14(total) - flatten14(ground_truth[label]))
        is_zero = diff == sp.zeros(14 * N64, 1)
        n_match_plus += int(is_zero)
        nonzero_entries = sum(1 for x in diff if sp.simplify(x) != 0)
        max_residual_plus[label] = nonzero_entries
        print(
            f"  {label:12s}: 5-piece sum == ground truth D^2_14, EXACTLY? {is_zero}"
            f"{'' if is_zero else f'  (nonzero residual entries: {nonzero_entries}/{14 * N64})'}"
        )

    print(f"\n  SIGN=+1 result: {n_match_plus}/{len(basis_w)} basis vectors match EXACTLY")

    print("\n" + "=" * 70)
    print("STEP C: 5-piece reconstruction, sign=-1 (the OTHER candidate convention,")
    print("tried because sign is not assumed a priori -- only checked)")
    print("=" * 70)
    n_match_minus = 0
    for w, label in zip(basis_w, labels, strict=True):
        total, parts = reconstruct_D2_14_full(w, Ms, D64, T, curv_h, ADE, AD_RAW, sign=-1)
        diff = sp.simplify(flatten14(total) - flatten14(ground_truth[label]))
        is_zero = diff == sp.zeros(14 * N64, 1)
        n_match_minus += int(is_zero)
        nonzero_entries = sum(1 for x in diff if sp.simplify(x) != 0)
        print(
            f"  {label:12s}: 5-piece sum == ground truth D^2_14, EXACTLY? {is_zero}"
            f"{'' if is_zero else f'  (nonzero residual entries: {nonzero_entries}/{14 * N64})'}"
        )

    print(f"\n  SIGN=-1 result: {n_match_minus}/{len(basis_w)} basis vectors match EXACTLY")

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print(f"  SIGN=+1: {n_match_plus}/12 exact matches")
    print(f"  SIGN=-1: {n_match_minus}/12 exact matches")
    if n_match_plus == 12:
        print("  The Round-22-style 5-piece decomposition DOES reproduce D^2_14")
        print("  EXACTLY on all 12/12 basis vectors, sign=+1 (same convention as V_7).")
    elif n_match_minus == 12:
        print("  The 5-piece decomposition reproduces D^2_14 EXACTLY on all 12/12")
        print("  basis vectors, but ONLY with sign=-1 (OPPOSITE convention from V_7's")
        print("  su3_curvature_term/torsion_cross_term) -- the sign is representation-")
        print("  dependent, not a universal constant of the construction.")
    else:
        print("  NEITHER sign choice reproduces the ground truth on all 12 basis")
        print("  vectors -- the naive substitution of rho=14 data into Round 22's")
        print("  formula does NOT work as-is. See per-basis-vector residuals above")
        print("  for where it breaks down.")


if __name__ == "__main__":
    main()
