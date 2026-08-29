"""C106 -- tests whether the "r-untouched" ansatz (B_1 = M_1 (x) I_r,
used throughout C101-C103/C105) is load-bearing for the real-spectrum
property, by building a Clifford-type r-coupled alternative
B_1^Gamma := sum_i M_1^{(i)} (x) rmult_i and testing it on C101's own
minimal 2-level (k=1,2) D_PW. Reuses only certified c85/C99/C104
machinery -- no new fundamental construction, only an exact Cartesian
change of basis applied to C104's own 4 (a,b) CG components. See
claim.md's Counterfactual Frame for the disclosed scratch-exploration
that preceded this formal script.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy import I as SI
from sympy import S
from sympy.physics.quantum.cg import CG

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c106.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, k: int):
    """Certified sign/transpose rule from C95 (k=1) and C96/C97/C98
    (k=2,3,4) -- reused unchanged (matches C99-C105's own copy)."""
    l_mats = [l1, l2, l3]
    if k == 1:
        return [m for m in l_mats], [-m.T for m in l_mats]
    return [-m.T for m in l_mats], [m for m in l_mats]


def magnetic_labels(c85_mod, k: int):
    """Reproduces C99-C105's own m_q, m_p extraction exactly."""
    l1, l2, l3 = c85_mod.build_l_matrices(k, "repaired")
    L, R = certified_L_R(l1, l2, l3, k)
    L1, R1 = L[0], R[0]
    dim = k + 1
    m_q = [sp.nsimplify(L1[q, q] / sp.I) / 2 for q in range(dim)]
    m_p = [sp.nsimplify(R1[p, p] / sp.I) / 2 for p in range(dim)]
    return m_q, m_p


def build_M_ab(c85_mod, k: int, a, b) -> sp.Matrix:
    """C104's own build_multiplication_matrix_component, reused
    unchanged (generalizes C100's fixed-(1/2,1/2) M_k to arbitrary
    (a,b))."""
    j1 = S(k) / 2
    j2 = S(1) / 2
    j_target = j1 + S(1) / 2
    dim_k = k + 1
    dim_kp1 = k + 2

    m_q_k, m_p_k = magnetic_labels(c85_mod, k)
    m_q_kp1, m_p_kp1 = magnetic_labels(c85_mod, k + 1)
    q_index_at_m = {v: idx for idx, v in enumerate(m_q_kp1)}
    p_index_at_m = {v: idx for idx, v in enumerate(m_p_kp1)}

    M = sp.zeros(dim_kp1 * dim_kp1, dim_k * dim_k)
    for q in range(dim_k):
        for p in range(dim_k):
            m_q_target = m_q_k[q] + a
            m_p_target = m_p_k[p] + b
            if m_q_target not in q_index_at_m or m_p_target not in p_index_at_m:
                continue
            Q = q_index_at_m[m_q_target]
            P = p_index_at_m[m_p_target]
            val_q = CG(j1, m_q_k[q], j2, a, j_target, m_q_target).doit()
            val_p = CG(j1, m_p_k[p], j2, b, j_target, m_p_target).doit()
            M[Q * dim_kp1 + P, q * dim_k + p] = sp.simplify(val_q * val_p)
    return M


def eigen_multiplicities_general(
    matrix_numeric: np.ndarray,
) -> tuple[list[tuple[float, int]], float]:
    """Same certified convention as C101-C103/C105: np.linalg.eigvals,
    NOT eigvalsh (D-bar is not symmetric as a raw matrix)."""
    eigvals = np.linalg.eigvals(matrix_numeric)
    max_imag = float(np.max(np.abs(np.imag(eigvals))))
    rounded = sorted(float(np.real(v)) for v in eigvals)
    grouped: list[list[float | int]] = []
    for v in rounded:
        if grouped and abs(grouped[-1][0] - v) < 1e-6:
            grouped[-1][1] += 1
        else:
            grouped.append([v, 1])
    return [(v, m) for v, m in grouped], max_imag


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    l1_1, l2_1, l3_1 = c85.build_l_matrices(1, "repaired")
    L1_1, _R1_1 = certified_L_R(l1_1, l2_1, l3_1, 1)
    rmult = [c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]

    # --- P0: L_i(1) = -rmult_i exactly, identity transform ---
    p0_per_i = [sp.simplify(L1_1[i] + rmult[i]) == sp.zeros(2, 2) for i in range(3)]
    p0_ok = all(p0_per_i)
    print(f"P0: L_i(1) == -rmult_i for i=1,2,3 (identity transform): {p0_per_i} -> {p0_ok}")

    # --- Build B_1^Gamma := sum_i M_1^{(i)} (x) rmult_i ---
    half = S(1) / 2
    M_pp = build_M_ab(c85, 1, half, half)
    M_pm = build_M_ab(c85, 1, half, -half)
    M_mp = build_M_ab(c85, 1, -half, half)
    M_mm = build_M_ab(c85, 1, -half, -half)
    # Exact Cartesian decomposition -- same quaternion<->SU(2)-matrix
    # convention c85's own hamilton_product/right_mult_matrix_on_ab use
    # (a_prime=aw+I*ax, b_prime=bw+I*bx; unit basis e1=(0,1,0,0) -> ax,
    # e2=(0,0,1,0) -> bw, e3=(0,0,0,1) -> bx).
    M1_x = sp.simplify((M_pp - M_mm) / (2 * SI))
    M1_y = sp.simplify((M_pm - M_mp) / 2)
    M1_z = sp.simplify((M_pm + M_mp) / (2 * SI))

    B_gamma = sp.Matrix(
        sp.kronecker_product(M1_x, rmult[0])
        + sp.kronecker_product(M1_y, rmult[1])
        + sp.kronecker_product(M1_z, rmult[2])
    )
    B_plain = sp.Matrix(sp.kronecker_product(M_pp, sp.eye(2)))  # C101's own r-untouched B_1

    # --- P1: shape matches the r-untouched coupling ---
    p1_ok = B_gamma.shape == (18, 8) and B_gamma.shape == B_plain.shape
    print(f"P1: B_gamma shape {B_gamma.shape} == B_plain shape {B_plain.shape} == (18,8): {p1_ok}")

    # --- P2: genuinely different object ---
    diff = sp.simplify(B_gamma - B_plain)
    p2_ok = diff != sp.zeros(*diff.shape)
    print(f"P2: B_gamma != B_plain: {p2_ok}")

    def dbar_full(k: int) -> sp.Matrix:
        l1, l2, l3 = c85.build_l_matrices(k, "repaired")
        dbar = c85.build_dbar([l1, l2, l3], rmult)
        dim_q = k + 1
        return sp.Matrix(sp.kronecker_product(sp.eye(dim_q), dbar))

    D1_full = dbar_full(1)
    D2_full = dbar_full(2)
    D1_np = np.array(D1_full.evalf().tolist(), dtype=np.float64)
    D2_np = np.array(D2_full.evalf().tolist(), dtype=np.float64)
    n1, n2 = D1_np.shape[0], D2_np.shape[0]
    nt = n1 + n2

    B_gamma_np = np.array(B_gamma.evalf().tolist(), dtype=np.float64)
    B_gamma_has_complex_entries = any(sp.im(sp.simplify(e)) != 0 for e in B_gamma)

    # --- P3: coupled spectrum with B_gamma ---
    DPW_gamma = np.zeros((nt, nt), dtype=complex)
    DPW_gamma[:n1, :n1] = D1_np
    DPW_gamma[n1:, n1:] = D2_np
    DPW_gamma[n1:, :n1] = B_gamma_np
    DPW_gamma[:n1, n1:] = B_gamma_np.T.conj()
    eigs_gamma, max_imag_gamma = eigen_multiplicities_general(DPW_gamma)
    p3_ok = max_imag_gamma < 1e-6
    print(f"P3: r-coupled (Clifford) D_PW real spectrum: {p3_ok} (max|Im|={max_imag_gamma:.2e})")

    # --- P4: negative control, fully asymmetric random real coupling ---
    rng = np.random.default_rng(42)
    p4_max_imags = []
    for _ in range(4):
        B_rand = rng.standard_normal((n2, n1))
        C_rand = rng.standard_normal((n1, n2))
        DPW_asym = np.zeros((nt, nt), dtype=complex)
        DPW_asym[:n1, :n1] = D1_np
        DPW_asym[n1:, n1:] = D2_np
        DPW_asym[n1:, :n1] = B_rand
        DPW_asym[:n1, n1:] = C_rand
        _, mi = eigen_multiplicities_general(DPW_asym)
        p4_max_imags.append(mi)
    p4_ok = all(mi > 1e-3 for mi in p4_max_imags)
    print(
        f"P4 (negative control, fully asymmetric random): max|Im| per trial = {p4_max_imags} -> all clearly nonzero: {p4_ok}"
    )

    # --- P5: negative control, random B/B.T-mirrored real coupling, NOT always real ---
    p5_max_imags = []
    for _ in range(8):
        B_rand = rng.standard_normal((n2, n1))
        DPW_mirror = np.zeros((nt, nt), dtype=complex)
        DPW_mirror[:n1, :n1] = D1_np
        DPW_mirror[n1:, n1:] = D2_np
        DPW_mirror[n1:, :n1] = B_rand
        DPW_mirror[:n1, n1:] = B_rand.T
        _, mi = eigen_multiplicities_general(DPW_mirror)
        p5_max_imags.append(mi)
    n_real = sum(1 for mi in p5_max_imags if mi < 1e-6)
    p5_ok = 0 < n_real < len(p5_max_imags)
    print(
        f"P5 (negative control, random B/B.T-mirrored): {n_real}/{len(p5_max_imags)} trials exactly "
        f"real, max|Im| per trial = {[f'{mi:.4f}' for mi in p5_max_imags]} -> not universal: {p5_ok}"
    )

    all_ok = p0_ok and p1_ok and p2_ok and p3_ok and p4_ok and p5_ok
    if p0_ok and p1_ok and p2_ok:
        if p3_ok:
            verdict = "R_COUPLED_CLIFFORD_ALTERNATIVE_ALSO_REAL__R_UNTOUCHED_NOT_LOAD_BEARING"
        else:
            verdict = "R_COUPLED_CLIFFORD_ALTERNATIVE_BREAKS_REALITY__R_UNTOUCHED_WAS_LOAD_BEARING"
    else:
        verdict = "CONSTRUCTION_ERROR__P0_P1_P2_FAILED"

    out = {
        "p0_L_eq_neg_rmult": p0_ok,
        "p1_shape_match": p1_ok,
        "p2_genuinely_different": p2_ok,
        "p3_real_spectrum_gamma": p3_ok,
        "p3_max_imag": max_imag_gamma,
        "p3_eigenvalues": eigs_gamma,
        "p4_negative_control_fully_asymmetric_max_imags": p4_max_imags,
        "p4_ok": p4_ok,
        "p5_negative_control_mirrored_max_imags": p5_max_imags,
        "p5_n_real_of_total": [n_real, len(p5_max_imags)],
        "p5_ok": p5_ok,
        "b_gamma_entrywise_real": not B_gamma_has_complex_entries,
        "all_predictions_ok": all_ok,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")

    assert p0_ok, "P0 failed -- L_i(1) != -rmult_i, construction premise is wrong"
    assert p1_ok, "P1 failed -- B_gamma shape mismatch, not a valid drop-in replacement"


if __name__ == "__main__":
    main()
