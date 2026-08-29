"""C108 -- tests whether D_PW built from C104's summed multiplication
operator M_k^sum (genuine 4-fold CG mixing, summed over all 4 (a,b)
components) still has an exactly real coupled spectrum, at k=1..4. See
claim.md's Counterfactual Frame for the disclosed scratch-exploration
that preceded this formal script. Returns to the pure C90-C106 numerical
track after the C107 OB1-bridge detour.
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
RESULTS_PATH = HERE / "results_c108.json"

FOUR_COMPONENTS = [
    (S(1) / 2, S(1) / 2),
    (S(1) / 2, -S(1) / 2),
    (-S(1) / 2, S(1) / 2),
    (-S(1) / 2, -S(1) / 2),
]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, k: int):
    """Certified sign/transpose rule from C95 (k=1) and C96/C97/C98
    (k=2,3,4) -- reused unchanged (matches C99-C107's own copy)."""
    l_mats = [l1, l2, l3]
    if k == 1:
        return [m for m in l_mats], [-m.T for m in l_mats]
    return [-m.T for m in l_mats], [m for m in l_mats]


def magnetic_labels(c85_mod, k: int):
    """Reproduces C99-C107's own m_q, m_p extraction exactly."""
    l1, l2, l3 = c85_mod.build_l_matrices(k, "repaired")
    L, R = certified_L_R(l1, l2, l3, k)
    L1, R1 = L[0], R[0]
    dim = k + 1
    m_q = [sp.nsimplify(L1[q, q] / sp.I) / 2 for q in range(dim)]
    m_p = [sp.nsimplify(R1[p, p] / sp.I) / 2 for p in range(dim)]
    return m_q, m_p


def build_M_ab(c85_mod, k: int, a, b) -> sp.Matrix:
    """C104's own build_multiplication_matrix_component, reused
    unchanged."""
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


def build_M_sum(c85_mod, k: int) -> sp.Matrix:
    """C104's own summed multiplication operator: sum over all 4 (a,b)
    components."""
    dim_k = k + 1
    dim_kp1 = k + 2
    M = sp.zeros(dim_kp1 * dim_kp1, dim_k * dim_k)
    for a, b in FOUR_COMPONENTS:
        M += build_M_ab(c85_mod, k, a, b)
    return M


def eigen_multiplicities_general(
    matrix_numeric: np.ndarray,
) -> tuple[list[tuple[float, int]], float]:
    """Same certified convention as C101-C107: np.linalg.eigvals, NOT
    eigvalsh (D-bar is not symmetric as a raw matrix)."""
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
    rmult = [c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]

    def dbar_full(k: int) -> sp.Matrix:
        l1, l2, l3 = c85.build_l_matrices(k, "repaired")
        dbar = c85.build_dbar([l1, l2, l3], rmult)
        dim_q = k + 1
        return sp.Matrix(sp.kronecker_product(sp.eye(dim_q), dbar))

    # --- P0: M_1^sum entrywise real ---
    M1_sum = build_M_sum(c85, 1)
    p0_ok = not any(sp.im(sp.simplify(e)) != 0 for e in M1_sum)
    print(f"P0: M_1^sum entrywise real: {p0_ok}")

    # --- P1: M_1^sum genuinely differs from the single-component M_1 ---
    half = S(1) / 2
    M1_fixed = build_M_ab(c85, 1, half, half)
    diff = sp.simplify(M1_sum - M1_fixed)
    p1_ok = diff != sp.zeros(*diff.shape)
    print(f"P1: M_1^sum != M_1 (single component): {p1_ok}")

    def test_level(k: int) -> float:
        Dk = dbar_full(k)
        Dk1 = dbar_full(k + 1)
        nk, nk1 = Dk.shape[0], Dk1.shape[0]
        nt = nk + nk1
        Msum = build_M_sum(c85, k)
        Bsum = sp.Matrix(sp.kronecker_product(Msum, sp.eye(2)))
        Dk_np = np.array(Dk.evalf().tolist(), dtype=np.float64)
        Dk1_np = np.array(Dk1.evalf().tolist(), dtype=np.float64)
        Bsum_np = np.array(Bsum.evalf().tolist(), dtype=np.float64)
        DPW = np.zeros((nt, nt), dtype=complex)
        DPW[:nk, :nk] = Dk_np
        DPW[nk:, nk:] = Dk1_np
        DPW[nk:, :nk] = Bsum_np
        DPW[:nk, nk:] = Bsum_np.T.conj()
        _, max_imag = eigen_multiplicities_general(DPW)
        return max_imag

    max_imags = {}
    for k in range(1, 5):
        mi = test_level(k)
        max_imags[str(k)] = mi
        print(f"k={k}->{k + 1}: max|Im(eig)| = {mi:.6e}")

    p2_ok = max_imags["1"] > 1e-3
    p3_ok = max_imags["2"] < 1e-6
    p4_ok = max_imags["3"] < 1e-6
    p5_ok = max_imags["4"] < 1e-6

    print(f"P2 (k=1 clearly non-real): {p2_ok}")
    print(f"P3 (k=2 exactly real): {p3_ok}")
    print(f"P4 (k=3 exactly real): {p4_ok}")
    print(f"P5 (k=4 exactly real): {p5_ok}")

    all_predictions_ok = p0_ok and p1_ok and p2_ok and p3_ok and p4_ok and p5_ok

    if p2_ok and p3_ok and p4_ok and p5_ok:
        verdict = "SUMMED_MIXING_BREAKS_REALITY_AT_K1_ONLY__HOLDS_AT_K_GEQ_2"
    elif not p2_ok and p3_ok and p4_ok and p5_ok:
        verdict = "SUMMED_MIXING_PRESERVES_REALITY_UNIFORMLY"
    elif p2_ok and not (p3_ok and p4_ok and p5_ok):
        verdict = "SUMMED_MIXING_BREAKS_REALITY_UNIFORMLY_OR_BEYOND_K1"
    else:
        verdict = "UNEXPECTED_PATTERN__SEE_DETAILS"

    out = {
        "p0_entrywise_real": p0_ok,
        "p1_genuinely_different": p1_ok,
        "max_imags_by_k": max_imags,
        "p2_k1_nonreal": p2_ok,
        "p3_k2_real": p3_ok,
        "p4_k3_real": p4_ok,
        "p5_k4_real": p5_ok,
        "all_predictions_ok": all_predictions_ok,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")

    assert p0_ok, "P0 failed -- M_1^sum has unexpected complex entries"
    assert p1_ok, "P1 failed -- M_1^sum is not actually different from M_1"


if __name__ == "__main__":
    main()
