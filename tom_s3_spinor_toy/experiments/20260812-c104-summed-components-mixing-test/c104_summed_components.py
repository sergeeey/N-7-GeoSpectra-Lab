"""C104 -- tests whether summing all four D^1_{a,b} components produces
genuine mixing (multiple nonzero entries per column) instead of C100's
own single-component injective embedding (exactly one nonzero entry
per column). Exploratory test of ONE alternative construction -- see
claim.md's Counterfactual Frame; does not claim this is the physically
correct multiplication operator.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp
from sympy import S
from sympy.physics.quantum.cg import CG
from sympy.physics.wigner import wigner_3j

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c104.json"

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
    (k=2,3,4) -- reused unchanged (matches C99-C103's own copy)."""
    l_mats = [l1, l2, l3]
    if k == 1:
        return [m for m in l_mats], [-m.T for m in l_mats]
    return [-m.T for m in l_mats], [m for m in l_mats]


def magnetic_labels(c85_mod, k: int):
    """Reproduces C99-C103's own m_q, m_p extraction exactly (physical
    spin units, j1=k/2)."""
    l1, l2, l3 = c85_mod.build_l_matrices(k, "repaired")
    L, R = certified_L_R(l1, l2, l3, k)
    L1, R1 = L[0], R[0]
    dim = k + 1
    m_q = [sp.nsimplify(L1[q, q] / sp.I) / 2 for q in range(dim)]
    m_p = [sp.nsimplify(R1[p, p] / sp.I) / 2 for p in range(dim)]
    return m_q, m_p


def cg_via_wigner_3j(j1, m1, j2, m2, j3, m3):
    """Independent recomputation via the CG<->Wigner-3j relation --
    same cross-check method C100 used, reused unchanged."""
    return (-1) ** (j1 - j2 + m3) * sp.sqrt(2 * j3 + 1) * wigner_3j(j1, j2, j3, m1, m2, -m3)


def build_multiplication_matrix_component(c85_mod, k: int, a, b) -> sp.Matrix:
    """Generalizes C100's own M_k assembly to an arbitrary (a,b)
    component, not just the fixed (1/2,1/2) C100/C101/C102/C103 used."""
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


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    per_k = {}
    for k in (1, 2, 3):
        dim_k = k + 1
        dim_kp1 = k + 2

        # P0: reuse sanity -- the already-certified (1/2,1/2) component
        # still cross-checks against the independent Wigner-3j path.
        a0, _b0 = FOUR_COMPONENTS[0]
        j1 = S(k) / 2
        j2 = S(1) / 2
        j_target = j1 + S(1) / 2
        m_q_k, _m_p_k = magnetic_labels(c85, k)
        p0_ok = True
        for q in range(dim_k):
            for p in range(dim_k):
                direct = CG(j1, m_q_k[q], j2, a0, j_target, m_q_k[q] + a0).doit()
                cross = cg_via_wigner_3j(j1, m_q_k[q], j2, a0, j_target, m_q_k[q] + a0)
                if sp.simplify(direct - cross) != 0:
                    p0_ok = False

        components = [
            build_multiplication_matrix_component(c85, k, a, b) for a, b in FOUR_COMPONENTS
        ]
        M_sum = sp.zeros(dim_kp1 * dim_kp1, dim_k * dim_k)
        for M in components:
            M_sum += M

        nonzero_count = sum(1 for e in M_sum if e != 0)
        per_column_counts = [
            sum(1 for row in range(M_sum.rows) if M_sum[row, col] != 0) for col in range(M_sum.cols)
        ]
        max_per_column = max(per_column_counts) if per_column_counts else 0
        columns_with_mixing = sum(1 for c in per_column_counts if c > 1)

        p1_mixing_found = nonzero_count > dim_k * dim_k

        per_k[str(k)] = {
            "p0_ok": p0_ok,
            "dim_k_squared": dim_k * dim_k,
            "sum_nonzero_count": nonzero_count,
            "per_column_nonzero_counts": per_column_counts,
            "max_entries_reached_from_one_input": max_per_column,
            "columns_with_mixing": columns_with_mixing,
            "p1_mixing_found": p1_mixing_found,
        }
        print(f"--- k={k} ---")
        print(f"  P0 ok: {p0_ok}")
        print(f"  dim_k^2 (single-component baseline): {dim_k * dim_k}")
        print(f"  M_sum nonzero count: {nonzero_count}")
        print(f"  per-column nonzero counts: {per_column_counts}")
        print(f"  columns showing mixing (>1 nonzero): {columns_with_mixing}")
        print(f"  P1 mixing found: {p1_mixing_found}")

    all_p0 = all(v["p0_ok"] for v in per_k.values())
    any_p1 = any(v["p1_mixing_found"] for v in per_k.values())
    all_p1 = all(v["p1_mixing_found"] for v in per_k.values())

    if not all_p0:
        verdict = "P0_REUSE_BUG__STOP_BEFORE_DRAWING_CONCLUSIONS"
    elif all_p1:
        verdict = "MIXING_FOUND_AT_ALL_K__SUMMING_COMPONENTS_PRODUCES_GENUINE_MIXING"
    elif any_p1:
        verdict = "MIXING_FOUND_AT_SOME_K_ONLY__PARTIAL_STRUCTURAL_CHANGE"
    else:
        verdict = "NO_MIXING__FOUR_COMPONENTS_IMAGES_REMAIN_DISJOINT_AT_EVERY_K_TESTED"

    out = {"per_k": per_k, "all_p0_ok": all_p0, "any_p1_mixing": any_p1, "verdict": verdict}
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
