"""C100 -- assembles the FULL (q,p)-only multiplication-type coupling
operator matrix M_k, level k -> level k+1, using the standard SU(2)
product-of-matrix-elements identity and C99's own verified magnetic-
number labeling (not a naive index-to-m assumption).

M_k[(Q,P),(q,p)] = CG(k/2,m_q; 1/2,1/2 | (k+1)/2, m_q+1/2)
                  * CG(k/2,m_p; 1/2,1/2 | (k+1)/2, m_p+1/2)

nonzero only when Q,P are the literal level-(k+1) indices whose own
magnetic numbers equal m_q+1/2, m_p+1/2 respectively -- looked up via
the same certified L_i/R_i-derived labeling C99 verified, not assumed.

Extends C90's own single-representative extremal-weight check (one
CG value per level) to the FULL matrix, as C90's own decision.md
explicitly scoped as the next step. r's role is NOT addressed here --
this is a (q,p)-only operator, matching C90's own scope exactly.
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
RESULTS_PATH = HERE / "results_c100.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, k: int):
    """CERTIFIED sign/transpose rule from C95 (k=1) and C96/C97/C98
    (k=2,3,4) -- reused unchanged, not re-derived."""
    l_mats = [l1, l2, l3]
    if k == 1:
        L = [m for m in l_mats]
        R = [-m.T for m in l_mats]
    else:
        L = [-m.T for m in l_mats]
        R = [m for m in l_mats]
    return L, R


def cg_via_wigner_3j(j1, m1, j2, m2, j3, m3):
    """Independent recomputation of a Clebsch-Gordan coefficient via
    the standard CG<->Wigner-3j relation:
    CG(j1,m1,j2,m2,j3,m3) = (-1)^(j1-j2+m3) * sqrt(2*j3+1)
                             * wigner_3j(j1,j2,j3,m1,m2,-m3)
    A genuinely different sympy code path (physics.wigner, not
    physics.quantum.cg) -- catches a bug specific to either module
    that a second call to the SAME CG() function would not."""
    return (-1) ** (j1 - j2 + m3) * sp.sqrt(2 * j3 + 1) * wigner_3j(j1, j2, j3, m1, m2, -m3)


def magnetic_labels(c85_mod, k: int):
    """Reproduces C99's own m_q, m_p extraction exactly (physical spin
    units, j1=k/2). Returns (m_q_list, m_p_list) indexed by literal
    q,p=0..k."""
    l1, l2, l3 = c85_mod.build_l_matrices(k, "repaired")
    L, R = certified_L_R(l1, l2, l3, k)
    L1, R1 = L[0], R[0]
    dim = k + 1
    m_q = [sp.nsimplify(L1[q, q] / sp.I) / 2 for q in range(dim)]
    m_p = [sp.nsimplify(R1[p, p] / sp.I) / 2 for p in range(dim)]
    return m_q, m_p


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    a = S(1) / 2
    b = S(1) / 2
    per_k = {}
    for k in (1, 2, 3):
        j1 = S(k) / 2
        j2 = S(1) / 2
        j_target = j1 + S(1) / 2
        dim_k = k + 1
        dim_kp1 = k + 2

        m_q_k, m_p_k = magnetic_labels(c85, k)
        m_q_kp1, m_p_kp1 = magnetic_labels(c85, k + 1)

        # inverse maps: physical m -> literal index at level k+1
        q_index_at_m = {v: idx for idx, v in enumerate(m_q_kp1)}
        p_index_at_m = {v: idx for idx, v in enumerate(m_p_kp1)}

        M = sp.zeros(dim_kp1 * dim_kp1, dim_k * dim_k)
        direct_check_ok = True
        for q in range(dim_k):
            for p in range(dim_k):
                m_q_target = m_q_k[q] + a
                m_p_target = m_p_k[p] + b
                if m_q_target not in q_index_at_m or m_p_target not in p_index_at_m:
                    continue
                Q = q_index_at_m[m_q_target]
                P = p_index_at_m[m_p_target]

                cg_q = CG(j1, m_q_k[q], j2, a, j_target, m_q_target)
                cg_p = CG(j1, m_p_k[p], j2, b, j_target, m_p_target)
                val_q = cg_q.doit()
                val_p = cg_p.doit()
                entry = sp.simplify(val_q * val_p)

                row = Q * dim_kp1 + P
                col = q * dim_k + p
                M[row, col] = entry

                # P1: independently recompute via the Wigner-3j relation
                # (a genuinely different sympy code path, not a second
                # call to the same CG() function) and confirm it matches
                recheck_q = cg_via_wigner_3j(j1, m_q_k[q], j2, a, j_target, m_q_target)
                recheck_p = cg_via_wigner_3j(j1, m_p_k[p], j2, b, j_target, m_p_target)
                if sp.simplify(recheck_q * recheck_p - entry) != 0:
                    direct_check_ok = False

        p0_dims_ok = M.shape == (dim_kp1 * dim_kp1, dim_k * dim_k)

        # P2: cross-check vs C90's own extremal-weight result (m1=j1).
        # The literal index for this extremal state is looked up
        # directly via the magnetic labels (per C99: p=0 at k=1, p=k
        # at k=2,3) -- not assumed.
        m_q_ext = max(m_q_k)
        m_p_ext = max(m_p_k)
        q_ext = m_q_k.index(m_q_ext)
        p_ext = m_p_k.index(m_p_ext)
        Q_ext = q_index_at_m.get(m_q_ext + a)
        P_ext = p_index_at_m.get(m_p_ext + b)
        p2_ok = False
        if Q_ext is not None and P_ext is not None:
            row_ext = Q_ext * dim_kp1 + P_ext
            col_ext = q_ext * dim_k + p_ext
            p2_ok = M[row_ext, col_ext] == 1

        # P3: non-degeneracy -- not the zero matrix, not merely a
        # single-entry / diagonal-only structure
        nonzero_count = sum(1 for e in M if e != 0)
        p3_ok = nonzero_count > 1

        per_k[str(k)] = {
            "matrix_shape": list(M.shape),
            "p0_dims_ok": p0_dims_ok,
            "p1_independent_recheck_ok": direct_check_ok,
            "p2_matches_c90_extremal": p2_ok,
            "p3_nonzero_entry_count": nonzero_count,
            "p3_non_degenerate": p3_ok,
        }
        print(f"--- k={k} -> k+1={k + 1} ---")
        print(f"  M shape: {M.shape}, dims ok: {p0_dims_ok}")
        print(f"  P1 independent recheck ok: {direct_check_ok}")
        print(f"  P2 matches C90 extremal (coeff=1): {p2_ok}")
        print(f"  P3 nonzero entries: {nonzero_count} (non-degenerate: {p3_ok})")

    all_p0 = all(v["p0_dims_ok"] for v in per_k.values())
    all_p1 = all(v["p1_independent_recheck_ok"] for v in per_k.values())
    all_p2 = all(v["p2_matches_c90_extremal"] for v in per_k.values())
    all_p3 = all(v["p3_non_degenerate"] for v in per_k.values())

    if not (all_p0 and all_p1):
        verdict = "ASSEMBLY_BUG__STOP_BEFORE_DRAWING_CONCLUSIONS"
    elif not all_p2:
        verdict = "CONVENTION_MISMATCH_WITH_C90__NEEDS_RECONCILIATION"
    elif not all_p3:
        verdict = "OPERATOR_TRIVIAL_DEGENERATE__NULL_RESULT_FOR_TASK_59"
    else:
        verdict = "FULL_CG_MATRIX_ASSEMBLED_AND_VERIFIED__QP_ONLY_R_STILL_OPEN"

    out = {
        "per_k": per_k,
        "all_p0_dims_ok": all_p0,
        "all_p1_recheck_ok": all_p1,
        "all_p2_matches_c90": all_p2,
        "all_p3_non_degenerate": all_p3,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
