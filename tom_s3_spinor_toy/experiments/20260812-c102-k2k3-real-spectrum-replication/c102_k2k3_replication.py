"""C102 -- repeats C101's exact construction at k=2,3 (instead of
k=1,2) to test whether the exactly-real coupled spectrum found there
replicates, or was a coincidence of that one level pair. Code reused
verbatim from C101 (only the level arguments change), per
pearl_registry/INDEX.md's own named next-cheapest-check.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy import S
from sympy.physics.quantum.cg import CG

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c102.json"
K_LOW = 2
K_HIGH = 3


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, k: int):
    """Certified sign/transpose rule from C95 (k=1) and C96/C97/C98
    (k=2,3,4) -- reused unchanged (matches C99/C100/C101's own copy)."""
    l_mats = [l1, l2, l3]
    if k == 1:
        return [m for m in l_mats], [-m.T for m in l_mats]
    return [-m.T for m in l_mats], [m for m in l_mats]


def magnetic_labels(c85_mod, k: int):
    """Reproduces C99/C100/C101's own m_q, m_p extraction exactly
    (physical spin units, j1=k/2)."""
    l1, l2, l3 = c85_mod.build_l_matrices(k, "repaired")
    L, R = certified_L_R(l1, l2, l3, k)
    L1, R1 = L[0], R[0]
    dim = k + 1
    m_q = [sp.nsimplify(L1[q, q] / sp.I) / 2 for q in range(dim)]
    m_p = [sp.nsimplify(R1[p, p] / sp.I) / 2 for p in range(dim)]
    return m_q, m_p


def build_multiplication_matrix(c85_mod, k: int) -> sp.Matrix:
    """Reproduces C100/C101's own M_k assembly exactly (single
    D^1_{1/2,1/2} component, level k -> k+1, (q,p)-only)."""
    j1 = S(k) / 2
    j2 = S(1) / 2
    j_target = j1 + S(1) / 2
    a = S(1) / 2
    b = S(1) / 2
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
    """General (non-Hermitian-assuming) eigenvalue solver -- see C101's
    own decision.md for why eigvalsh must never be used on D-bar or
    operators built from it (self-caught bug there)."""
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

    right_mult = [
        c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
    ]

    def dbar_full(k: int) -> sp.Matrix:
        l1, l2, l3 = c85.build_l_matrices(k, "repaired")
        dbar = c85.build_dbar([l1, l2, l3], right_mult)
        dim_q = k + 1
        return sp.Matrix(sp.kronecker_product(sp.eye(dim_q), dbar))

    D_low_full = dbar_full(K_LOW)
    D_high_full = dbar_full(K_HIGH)

    # P0: reuse sanity.
    D_low_np = np.array(D_low_full.evalf().tolist(), dtype=complex).real
    D_high_np = np.array(D_high_full.evalf().tolist(), dtype=complex).real
    eigs_low, imag_low = eigen_multiplicities_general(D_low_np)
    eigs_high, imag_high = eigen_multiplicities_general(D_high_np)
    expected_low = {-float(K_LOW): (K_LOW + 2) * (K_LOW + 1), float(K_LOW + 2): K_LOW * (K_LOW + 1)}
    expected_high = {
        -float(K_HIGH): (K_HIGH + 2) * (K_HIGH + 1),
        float(K_HIGH + 2): K_HIGH * (K_HIGH + 1),
    }
    found_low = {round(v): m for v, m in eigs_low}
    found_high = {round(v): m for v, m in eigs_high}
    p0_ok = (found_low == expected_low) and (found_high == expected_high)
    print(f"P0: D_{K_LOW}_full eigs {found_low} (expect {expected_low}), max|Im|={imag_low:.2e}")
    print(
        f"P0: D_{K_HIGH}_full eigs {found_high} (expect {expected_high}), max|Im|={imag_high:.2e}"
    )
    print(f"P0 ok: {p0_ok}")

    M_low = build_multiplication_matrix(c85, K_LOW)
    B = sp.Matrix(sp.kronecker_product(M_low, sp.eye(2)))
    print(f"B shape: {B.shape}")

    dim_total = D_low_full.shape[0] + D_high_full.shape[0]
    D_PW = sp.zeros(dim_total, dim_total)
    n_low = D_low_full.shape[0]
    D_PW[:n_low, :n_low] = D_low_full
    D_PW[n_low:, n_low:] = D_high_full
    D_PW[n_low:, :n_low] = B
    D_PW[:n_low, n_low:] = B.H

    D_PW_np = np.array(D_PW.evalf().tolist(), dtype=complex)
    coupled_eigs, coupled_max_imag = eigen_multiplicities_general(D_PW_np)
    p1_real_spectrum = coupled_max_imag < 1e-6
    print(
        f"P1 (the open question from C101): real spectrum = {p1_real_spectrum} "
        f"(max|Im|={coupled_max_imag:.2e})"
    )
    # Hard invariant gate (added: boyko-project-radar Chain 1, sci-code-audit
    # Layer 5 finding) -- see C101's own copy of this comment for why.
    assert coupled_max_imag < 1e-6, (
        f"D_PW spectrum is not real (max|Im|={coupled_max_imag:.2e}) -- "
        "this contradicts the round's own certified result; stop before writing results"
    )

    uncoupled_union = sorted(eigs_low + eigs_high, key=lambda x: x[0])
    coupled_values = sorted(round(v, 6) for v, _m in coupled_eigs)
    uncoupled_values = sorted(round(v, 6) for v, m in uncoupled_union for _ in range(m))
    max_abs_shift = max(abs(c - u) for c, u in zip(coupled_values, uncoupled_values))
    p2_shift_found = max_abs_shift > 1e-6

    print(f"\nUncoupled union eigenvalues: {[(v, m) for v, m in uncoupled_union]}")
    print(f"Coupled D_PW eigenvalues: {coupled_eigs}")
    print(f"Max |coupled - uncoupled| (paired by rank): {max_abs_shift}")
    print(f"P2 shift found: {p2_shift_found}")

    if not p0_ok:
        verdict = "P0_REUSE_BUG__STOP_BEFORE_DRAWING_CONCLUSIONS"
    elif not p1_real_spectrum:
        verdict = "P1_COMPLEX_SPECTRUM__REAL_SPECTRUM_WAS_A_K1K2_COINCIDENCE_NOT_STRUCTURAL"
    elif p2_shift_found:
        verdict = "REAL_SPECTRUM_REPLICATES__SECOND_DATA_POINT_SUPPORTS_STRUCTURAL_ORIGIN"
    else:
        verdict = "REAL_SPECTRUM_REPLICATES_BUT_NO_SHIFT__DIVERGES_FROM_C101"

    out = {
        "k_low": K_LOW,
        "k_high": K_HIGH,
        "p0_reuse_ok": p0_ok,
        "found_low_eigs": found_low,
        "found_high_eigs": found_high,
        "B_shape": list(B.shape),
        "p1_real_spectrum": p1_real_spectrum,
        "p1_max_imag": coupled_max_imag,
        "uncoupled_union_eigs": [[v, m] for v, m in uncoupled_union],
        "coupled_eigs": [[v, m] for v, m in coupled_eigs],
        "max_abs_shift": max_abs_shift,
        "p2_shift_found": p2_shift_found,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
