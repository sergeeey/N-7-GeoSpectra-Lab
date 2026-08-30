"""C114 -- does any proper subset of the (1,1) or (3/2,3/2) matched-
diagonal cell's summed components (C112) break reality, even though the
full sum does not? Surfaced by narrow-discovery-engines Engine 2
(Constraint Relaxation Search) as the highest-scoring, cheapest
untested assumption in the C90-C113 construction family.

Reuses C112's own build_M_ab_general unchanged. Structured subset
sampling (not exhaustive 2^9/2^16 search) per claim.md's Cheapest
Differentiating Test scoping: all size-(n-1) subsets (C109's own
successful method at the anchor), all size-1 subsets, and for the
smaller (1,1) cell, a structured intermediate sample respecting the
(a,b)<->(-a,-b) pairing symmetry.
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
RESULTS_PATH = HERE / "results_c114.json"
C112_CELL_11_MAX_IM = 0.0
C112_CELL_1515_MAX_IM = 3.1217002550592562e-15


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, level: int):
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


def magnetic_range(j) -> list:
    n = int(2 * j) + 1
    return [j - i for i in range(n)]


def build_M_ab_general(c85_mod, k_source: int, j2, a, b) -> sp.Matrix:
    """Reused unchanged from C112."""
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


def pairing_groups(pairs: list[tuple]) -> list[list[tuple]]:
    """Groups (a,b) pairs by the (a,b)<->(-a,-b) symmetry -- self-paired
    (a,b)=(-a,-b) (only (0,0)) forms a singleton group."""
    seen = set()
    groups = []
    for a, b in pairs:
        if (a, b) in seen:
            continue
        partner = (-a, -b)
        if partner == (a, b):
            groups.append([(a, b)])
        else:
            groups.append([(a, b), partner])
        seen.add((a, b))
        seen.add(partner)
    return groups


def max_imag_for_subset(D1_np, D2_np, component_nps: dict, subset: tuple) -> float:
    n1, n2 = D1_np.shape[0], D2_np.shape[0]
    nt = n1 + n2
    M_sum_np = sum(
        (component_nps[key] for key in subset),
        start=np.zeros_like(next(iter(component_nps.values()))),
    )
    B_np = np.kron(M_sum_np, np.eye(2))
    DPW = np.zeros((nt, nt), dtype=complex)
    DPW[:n1, :n1] = D1_np
    DPW[n1:, n1:] = D2_np
    DPW[n1:, :n1] = B_np
    DPW[:n1, n1:] = B_np.conj().T
    eigs = np.linalg.eigvals(DPW)
    return float(np.max(np.abs(np.imag(eigs))))


def run_cell(c85_mod, k_source: int, j2, cell_name: str, do_structured_intermediate: bool) -> dict:
    print(f"\n=== cell {cell_name} (k_source={k_source}, j2={j2}) ===")
    a_vals = magnetic_range(j2)
    pairs = [(a, b) for a in a_vals for b in a_vals]

    def dbar_full(level: int) -> sp.Matrix:
        l1, l2, l3 = c85_mod.build_l_matrices(level, "repaired")
        dbar = c85_mod.build_dbar([l1, l2, l3], rmult)
        dim_q = level + 1
        return sp.Matrix(sp.kronecker_product(sp.eye(dim_q), dbar))

    rmult = [c85_mod.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]
    j1 = S(k_source) / 2
    target_level = int(2 * (j1 + j2))
    D1 = dbar_full(k_source)
    D2 = dbar_full(target_level)
    D1_np = np.array(D1.evalf().tolist(), dtype=np.float64)
    D2_np = np.array(D2.evalf().tolist(), dtype=np.float64)

    print(f"  building {len(pairs)} components...")
    component_nps = {}
    for a, b in pairs:
        M = build_M_ab_general(c85_mod, k_source, j2, a, b)
        component_nps[(a, b)] = np.array(M.evalf().tolist(), dtype=np.float64)

    # P0: full sum
    full_max_im = max_imag_for_subset(D1_np, D2_np, component_nps, tuple(pairs))
    print(f"  P0 full sum max|Im| = {full_max_im}")

    # WHY these diagnostics: FL Step 8a skeptic review of this exact script
    # (context-blind) found the "corner components are structurally special"
    # reading unsupported without them. D1/D2 non-Hermiticity is already a
    # certified project fact (C101 onward, np.linalg.eigvals not eigvalsh
    # throughout this whole series) -- confirmed explicitly below, not just
    # assumed. The other skeptic-named gap (is "safe removal" just removing a
    # near-zero component, trivially) is checked via component_norms.
    #
    # NOT included here: the skeptic's own suggested "projection of each M_ab
    # onto D2's anti-Hermitian part" -- a first attempt at this hit a genuine
    # dimension mismatch (M_ab is the RECTANGULAR dim_target^2 x dim_source^2
    # coupling map, not a member of D2's own dim(dbar) x dim(dbar) square
    # space; kron(M_ab, I_2) does not correctly embed it there either -- the
    # coupling's relationship to D2's spectral structure needs a properly
    # derived embedding, not a bolted-on elementwise product). Left as a named
    # open question, not force-fit incorrectly under time pressure.
    d1_hermitian_err = float(np.max(np.abs(D1_np - D1_np.T.conj())))
    d2_hermitian_err = float(np.max(np.abs(D2_np - D2_np.T.conj())))
    component_norms = {str(k): float(np.linalg.norm(v)) for k, v in component_nps.items()}

    results = {
        "full_sum_max_im": full_max_im,
        "d1_hermitian_err": d1_hermitian_err,
        "d2_hermitian_err": d2_hermitian_err,
        "component_norms": component_norms,
        "subsets": [],
    }
    print(f"  D1 hermitian_err={d1_hermitian_err:.4g}, D2 hermitian_err={d2_hermitian_err:.4g}")
    print(f"  component norms: {component_norms}")

    # size n-1 (remove exactly one)
    for removed in pairs:
        subset = tuple(p for p in pairs if p != removed)
        mi = max_imag_for_subset(D1_np, D2_np, component_nps, subset)
        results["subsets"].append(
            {"type": "remove_one", "removed": str(removed), "size": len(subset), "max_im": mi}
        )

    # size 1 (single component alone)
    for p in pairs:
        mi = max_imag_for_subset(D1_np, D2_np, component_nps, (p,))
        results["subsets"].append({"type": "single", "component": str(p), "size": 1, "max_im": mi})

    # structured intermediate, respecting (a,b)<->(-a,-b) pairing groups
    if do_structured_intermediate:
        groups = pairing_groups(pairs)
        n_groups = len(groups)
        for r in range(1, n_groups):  # proper, non-empty combinations of groups
            for combo in itertools.combinations(range(n_groups), r):
                subset = tuple(item for gi in combo for item in groups[gi])
                if 2 <= len(subset) <= 7:
                    mi = max_imag_for_subset(D1_np, D2_np, component_nps, subset)
                    results["subsets"].append(
                        {"type": "structured_pair_group", "size": len(subset), "max_im": mi}
                    )

    breaking = [s for s in results["subsets"] if s["max_im"] > 1e-9]
    results["n_subsets_tested"] = len(results["subsets"])
    results["n_breaking"] = len(breaking)
    results["breaking_subsets"] = breaking
    print(f"  tested {len(results['subsets'])} subsets, {len(breaking)} broke reality")
    return results


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    cell_11 = run_cell(c85, 2, S(1), "j1=1,j2=1", do_structured_intermediate=True)
    p0_ok_11 = cell_11["full_sum_max_im"] < 1e-9

    cell_1515 = run_cell(c85, 3, S(3) / 2, "j1=3/2,j2=3/2", do_structured_intermediate=False)
    p0_ok_1515 = cell_1515["full_sum_max_im"] < 1e-9

    all_p0_ok = p0_ok_11 and p0_ok_1515
    any_breaking = cell_11["n_breaking"] > 0 or cell_1515["n_breaking"] > 0

    if not all_p0_ok:
        verdict = "P0_MISMATCH__STOP_BEFORE_DRAWING_CONCLUSIONS"
    elif any_breaking:
        verdict = "SUBSET_BREAKS_REALITY__NEW_STRUCTURE_FOUND__NOT_A_SIMPLE_FULL_VS_NONE_PATTERN"
    else:
        verdict = "NO_SUBSET_BREAKS__H_SPECIFIC_FURTHER_STRENGTHENED__ANCHOR_PATTERN_DOES_NOT_GENERALIZE_EVEN_AT_SUBSET_LEVEL"

    out = {
        "cell_j1_1_j2_1": cell_11,
        "cell_j1_1p5_j2_1p5": cell_1515,
        "all_p0_ok": all_p0_ok,
        "any_breaking": any_breaking,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")

    assert all_p0_ok, "P0 mismatch -- see per-cell detail"


if __name__ == "__main__":
    main()
