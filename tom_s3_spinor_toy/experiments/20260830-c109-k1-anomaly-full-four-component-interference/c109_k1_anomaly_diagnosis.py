"""C109 -- diagnoses C108's own open pearl: what exactly causes the k=1
reality-breaking anomaly under M_k^sum? Reuses only certified c85/C104
machinery. See claim.md's Counterfactual Frame for the disclosed
scratch-exploration that preceded this formal script.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy import S
from sympy.physics.quantum.cg import CG

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c109.json"

FOUR_COMPONENTS = [
    (S(1) / 2, S(1) / 2),
    (S(1) / 2, -S(1) / 2),
    (-S(1) / 2, S(1) / 2),
    (-S(1) / 2, -S(1) / 2),
]
COMPONENT_LABELS = ["++", "+-", "-+", "--"]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, k: int):
    """Certified sign/transpose rule -- reused unchanged (matches
    C99-C108's own copy)."""
    l_mats = [l1, l2, l3]
    if k == 1:
        return [m for m in l_mats], [-m.T for m in l_mats]
    return [-m.T for m in l_mats], [m for m in l_mats]


def magnetic_labels(c85_mod, k: int):
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


def eigen_max_imag(matrix_numeric: np.ndarray) -> float:
    eigvals = np.linalg.eigvals(matrix_numeric)
    return float(np.max(np.abs(np.imag(eigvals))))


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

    D1 = dbar_full(1)
    D2 = dbar_full(2)
    n1, n2 = D1.shape[0], D2.shape[0]
    nt = n1 + n2
    D1_np = np.array(D1.evalf().tolist(), dtype=np.float64)
    D2_np = np.array(D2.evalf().tolist(), dtype=np.float64)

    def test_with_M(M: sp.Matrix) -> float:
        Bs = sp.Matrix(sp.kronecker_product(M, sp.eye(2)))
        Bs_np = np.array(Bs.evalf().tolist(), dtype=np.float64)
        DPW = np.zeros((nt, nt), dtype=complex)
        DPW[:n1, :n1] = D1_np
        DPW[n1:, n1:] = D2_np
        DPW[n1:, :n1] = Bs_np
        DPW[:n1, n1:] = Bs_np.T.conj()
        return eigen_max_imag(DPW)

    # --- P0: j1 == j2 (fixed at 1/2) only at k=1 ---
    j1_eq_j2 = {k: (S(k) / 2 == S(1) / 2) for k in (1, 2, 3)}
    p0_ok = j1_eq_j2[1] and not j1_eq_j2[2] and not j1_eq_j2[3]
    print(f"P0: j1==j2 only at k=1: {j1_eq_j2} -> {p0_ok}")

    # --- P1: fully-populated row count, k=1,2,3 ---
    full_row_counts = {}
    M_sums = {}
    for k in (1, 2, 3):
        M = sp.zeros((k + 2) ** 2, (k + 1) ** 2)
        for a, b in FOUR_COMPONENTS:
            M += build_M_ab(c85, k, a, b)
        M_sums[k] = M
        full_row_counts[k] = sum(
            1 for r in range(M.rows) if all(M[r, c] != 0 for c in range(M.cols))
        )
    p1_ok = full_row_counts[1] == 1 and full_row_counts[2] == 0 and full_row_counts[3] == 0
    print(f"P1: fully-populated row counts {full_row_counts} -> {p1_ok}")

    # --- P2: zeroing any single one of the 16 nonzero entries of M_1^sum restores reality ---
    M1s = M_sums[1]
    nz_positions = [(r, c) for r in range(M1s.rows) for c in range(M1s.cols) if M1s[r, c] != 0]
    p2_results = {}
    for r, c in nz_positions:
        Mp = M1s.copy()
        Mp[r, c] = 0
        mi = test_with_M(Mp)
        p2_results[f"{r}_{c}"] = mi
    p2_ok = all(mi < 1e-6 for mi in p2_results.values())
    print(f"P2: {len(nz_positions)} single-entry-zeroed variants, all real: {p2_ok}")

    # --- P3/P4: all 15 nonempty subsets of the 4 components ---
    # NOTE: subset size is tracked explicitly (not inferred from the label
    # string), since the component labels ("++","+-","-+","--") themselves
    # contain "+" characters -- counting "+" in a joined label is NOT a
    # valid proxy for subset size (self-caught before formalizing further).
    comps = dict(zip(COMPONENT_LABELS, [build_M_ab(c85, 1, a, b) for a, b in FOUR_COMPONENTS]))
    subset_results = {}
    for r in range(1, 5):
        for subset in itertools.combinations(COMPONENT_LABELS, r):
            Msub = sp.zeros(9, 4)
            for lbl in subset:
                Msub += comps[lbl]
            mi = test_with_M(Msub)
            subset_results[",".join(subset)] = {"size": r, "max_imag": mi}

    proper_subsets = {k: v["max_imag"] for k, v in subset_results.items() if v["size"] < 4}
    full_subset = {k: v["max_imag"] for k, v in subset_results.items() if v["size"] == 4}
    p3_ok = all(mi < 1e-6 for mi in proper_subsets.values())
    p4_ok = all(mi > 1e-3 for mi in full_subset.values())
    print(f"P3: all {len(proper_subsets)} proper subsets (size 1,2,3) real: {p3_ok}")
    print(f"P4: full subset (size 4) non-real: {full_subset} -> {p4_ok}")

    all_predictions_ok = p0_ok and p1_ok and p2_ok and p3_ok and p4_ok

    verdict = (
        "K1_ANOMALY_REQUIRES_FULL_4COMPONENT_INTERFERENCE__FRAGILE_TO_ANY_SINGLE_PERTURBATION"
        if all_predictions_ok
        else "UNEXPECTED_PATTERN__SEE_DETAILS"
    )

    out = {
        "p0_j1_eq_j2_only_at_k1": p0_ok,
        "full_row_counts_by_k": full_row_counts,
        "p1_ok": p1_ok,
        "p2_single_entry_zero_results": p2_results,
        "p2_ok": p2_ok,
        "p3_proper_subset_results": proper_subsets,
        "p3_ok": p3_ok,
        "p4_full_subset_result": full_subset,
        "p4_ok": p4_ok,
        "all_predictions_ok": all_predictions_ok,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")

    assert p0_ok, "P0 failed"
    assert p4_ok, "P4 failed -- full subset unexpectedly real"


if __name__ == "__main__":
    main()
