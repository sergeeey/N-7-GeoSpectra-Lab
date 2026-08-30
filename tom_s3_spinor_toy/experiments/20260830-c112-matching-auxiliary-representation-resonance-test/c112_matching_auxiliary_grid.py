"""C112 -- small (j1,j2) grid testing whether the k=1 exceptional-point
anomaly (C108/C109) correlates with the j1=j2 coincidence specifically,
or is confounded with level-distance / component-count / ignored-CG-
channel-count (all locked together under a single-diagonal test -- see
claim.md's DDD design-review section for the full skeptic finding that
rejected the original single-diagonal design before any code existed).

Generalizes C104's own certified `build_multiplication_matrix_component`
(hardcoded j2=1/2) to an arbitrary auxiliary spin j2, reusing every other
piece of certified machinery (magnetic_labels, certified_L_R, dbar_full,
cg_via_wigner_3j) unchanged.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy import S
from sympy.physics.quantum.cg import CG
from sympy.physics.wigner import wigner_3j

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c112.json"

C108_CERTIFIED_MAX_IM = 0.10592470995283362

# Cheapest-first ordering per the skeptic's own suggestion: (j1=1/2,j2=1)
# first (non-matched, but shares level-distance/component-count with the
# matched (1,1) cell) -- if it already breaks, the diagonal-specific
# story is in trouble before the rest of the grid is spent.
GRID_ORDER = [
    (S(1) / 2, S(1)),  # cheapest-first triage cell
    (S(1) / 2, S(1) / 2),  # C108 anchor / P0 sanity check
    (S(1) / 2, S(3) / 2),
    (S(1), S(1) / 2),
    (S(1), S(1)),  # diagonal test (matched)
    (S(1), S(3) / 2),
    (S(3) / 2, S(1) / 2),
    (S(3) / 2, S(1)),
    (S(3) / 2, S(3) / 2),  # diagonal test (matched)
]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, level: int):
    """Certified sign/transpose rule from C95/C96-C98, reused unchanged."""
    l_mats = [l1, l2, l3]
    if level == 1:
        return [m for m in l_mats], [-m.T for m in l_mats]
    return [-m.T for m in l_mats], [m for m in l_mats]


def magnetic_labels(c85_mod, level: int):
    l1, l2, l3 = c85_mod.build_l_matrices(level, "repaired")
    L, R = certified_L_R(l1, l2, l3, level)
    L1, R1 = L[0], R[0]
    dim = level + 1
    m_q = [sp.nsimplify(L1[q, q] / sp.I) / 2 for q in range(dim)]
    m_p = [sp.nsimplify(R1[p, p] / sp.I) / 2 for p in range(dim)]
    return m_q, m_p


def cg_via_wigner_3j(j1, m1, j2, m2, j3, m3):
    """Independent recomputation via the CG<->Wigner-3j relation --
    reused unchanged from C104, used here as the independent structural
    self-check the DDD review required (not just at k=1)."""
    return (-1) ** (j1 - j2 + m3) * sp.sqrt(2 * j3 + 1) * wigner_3j(j1, j2, j3, m1, m2, -m3)


def magnetic_range(j) -> list:
    """All magnetic values of spin j, from -j to +j in integer steps."""
    n = int(2 * j) + 1
    return [j - i for i in range(n)]


def build_M_ab_general(c85_mod, k_source: int, j2, a, b) -> sp.Matrix:
    """Generalizes C104's build_multiplication_matrix_component: j2 is a
    free parameter (was hardcoded 1/2), target level = 2*(j1+j2)."""
    j1 = S(k_source) / 2
    j_target = j1 + j2
    target_level = int(2 * j_target)
    dim_source = k_source + 1
    dim_target = target_level + 1

    m_q_src, m_p_src = magnetic_labels(c85_mod, k_source)
    m_q_tgt, m_p_tgt = magnetic_labels(c85_mod, target_level)
    q_index_at_m = {v: idx for idx, v in enumerate(m_q_tgt)}
    p_index_at_m = {v: idx for idx, v in enumerate(m_p_tgt)}

    M = sp.zeros(dim_target * dim_target, dim_source * dim_source)
    for q in range(dim_source):
        for p in range(dim_source):
            m_q_t = m_q_src[q] + a
            m_p_t = m_p_src[p] + b
            if m_q_t not in q_index_at_m or m_p_t not in p_index_at_m:
                continue
            Q = q_index_at_m[m_q_t]
            P = p_index_at_m[m_p_t]
            val_q = CG(j1, m_q_src[q], j2, a, j_target, m_q_t).doit()
            val_p = CG(j1, m_p_src[p], j2, b, j_target, m_p_t).doit()
            M[Q * dim_target + P, q * dim_source + p] = sp.simplify(val_q * val_p)
    return M


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )
    rmult = [c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]

    def dbar_full(level: int) -> sp.Matrix:
        l1, l2, l3 = c85.build_l_matrices(level, "repaired")
        dbar = c85.build_dbar([l1, l2, l3], rmult)
        dim_q = level + 1
        return sp.Matrix(sp.kronecker_product(sp.eye(dim_q), dbar))

    cells = {}
    dbar_cache: dict[int, sp.Matrix] = {}

    def get_dbar(level: int) -> sp.Matrix:
        if level not in dbar_cache:
            dbar_cache[level] = dbar_full(level)
        return dbar_cache[level]

    for j1, j2 in GRID_ORDER:
        k_source = int(2 * j1)
        j_target = j1 + j2
        target_level = int(2 * j_target)
        cell_key = f"j1={j1},j2={j2}"
        print(f"\n=== cell {cell_key} (source level={k_source}, target level={target_level}) ===")

        # --- structural self-checks (P_shape), BEFORE trusting any spectrum ---
        expected_source_dim = k_source + 1
        expected_target_dim = target_level + 1
        expected_n_components = (int(2 * j2) + 1) ** 2

        a_vals = magnetic_range(j2)
        components = []
        for a in a_vals:
            for b in a_vals:
                components.append(build_M_ab_general(c85, k_source, j2, a, b))
        n_components = len(components)

        M_sum = sp.zeros(
            expected_target_dim * expected_target_dim, expected_source_dim * expected_source_dim
        )
        for M in components:
            shape_ok_local = M.shape == (
                expected_target_dim * expected_target_dim,
                expected_source_dim * expected_source_dim,
            )
            if not shape_ok_local:
                raise AssertionError(f"{cell_key}: component shape mismatch, got {M.shape}")
            M_sum += M

        shape_ok = n_components == expected_n_components and M_sum.shape == (
            expected_target_dim * expected_target_dim,
            expected_source_dim * expected_source_dim,
        )

        # --- independent CG cross-check, once per distinct (j1,j2) pair ---
        m_q_src, _ = magnetic_labels(c85, k_source)
        a0 = a_vals[0]
        direct = CG(j1, m_q_src[0], j2, a0, j_target, m_q_src[0] + a0).doit()
        cross = cg_via_wigner_3j(j1, m_q_src[0], j2, a0, j_target, m_q_src[0] + a0)
        cg_cross_check_ok = sp.simplify(direct - cross) == 0

        p_shape_ok = shape_ok and cg_cross_check_ok
        print(f"  n_components={n_components} (expected {expected_n_components})")
        print(f"  shape_ok={shape_ok}, cg_cross_check_ok={cg_cross_check_ok}")

        if not p_shape_ok:
            cells[cell_key] = {
                "j1": str(j1),
                "j2": str(j2),
                "k_source": k_source,
                "target_level": target_level,
                "p_shape_ok": False,
                "max_imag": None,
            }
            print(
                f"  STRUCTURAL CHECK FAILED for {cell_key} -- skipping spectrum, per kill_criterion"
            )
            continue

        # --- spectrum test ---
        D1 = get_dbar(k_source)
        D2 = get_dbar(target_level)
        n1, n2 = D1.shape[0], D2.shape[0]
        nt = n1 + n2
        D1_np = np.array(D1.evalf().tolist(), dtype=np.float64)
        D2_np = np.array(D2.evalf().tolist(), dtype=np.float64)
        M_sum_np = np.array(M_sum.evalf().tolist(), dtype=np.float64)
        B_np = np.kron(M_sum_np, np.eye(2))

        DPW = np.zeros((nt, nt), dtype=complex)
        DPW[:n1, :n1] = D1_np
        DPW[n1:, n1:] = D2_np
        DPW[n1:, :n1] = B_np
        DPW[:n1, n1:] = B_np.conj().T

        eigs = np.linalg.eigvals(DPW)
        max_imag = float(np.max(np.abs(np.imag(eigs))))
        breaks_reality = max_imag > 1e-9

        print(f"  max|Im| = {max_imag}")
        print(f"  breaks_reality = {breaks_reality}")

        cells[cell_key] = {
            "j1": str(j1),
            "j2": str(j2),
            "k_source": k_source,
            "target_level": target_level,
            "p_shape_ok": True,
            "n_components": n_components,
            "max_imag": max_imag,
            "breaks_reality": breaks_reality,
        }

    # --- P0: the C108 anchor cell must reproduce the certified value ---
    anchor = cells.get("j1=1/2,j2=1/2")
    p0_ok = (
        anchor is not None
        and anchor.get("p_shape_ok")
        and abs(anchor["max_imag"] - C108_CERTIFIED_MAX_IM) < 1e-9
    )
    print(f"\nP0 (C108 anchor reproduced exactly): {p0_ok}")

    all_shape_ok = all(c["p_shape_ok"] for c in cells.values())

    if not all_shape_ok:
        verdict = "STRUCTURAL_CHECK_FAILED__DO_NOT_INTERPRET_PATTERN"
    elif not p0_ok:
        verdict = "P0_ANCHOR_MISMATCH__STOP_BEFORE_DRAWING_CONCLUSIONS"
    else:
        diag = [cells[f"j1={j},j2={j}"]["breaks_reality"] for j in (S(1) / 2, S(1), S(3) / 2)]
        off_diag = [
            v["breaks_reality"]
            for k, v in cells.items()
            if v["p_shape_ok"] and str(v["j1"]) != str(v["j2"])
        ]
        if all(diag) and not any(off_diag):
            verdict = "CLEAN_DIAGONAL_PATTERN__J1_EQ_J2_IS_THE_TRIGGER"
        elif not any(diag):
            verdict = "NO_DIAGONAL_BREAK__J1_EQ_J2_NOT_SUFFICIENT_AT_HIGHER_SPIN"
        elif all(off_diag) and all(diag):
            verdict = "EVERYTHING_BREAKS__NOT_DIAGONAL_SPECIFIC__CONFOUND_CONFIRMED"
        else:
            verdict = "MIXED_PATTERN__SEE_FULL_GRID__NO_CLEAN_SINGLE_EXPLANATION"

    out = {
        "cells": cells,
        "p0_ok": p0_ok,
        "all_shape_ok": all_shape_ok,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
