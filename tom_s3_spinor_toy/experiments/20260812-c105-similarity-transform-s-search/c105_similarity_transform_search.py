"""C105 -- formal re-derivation of a preliminary scratch exploration
(disclosed in claim.md) searching for the candidate similarity
transform S explaining why the coupled D_PW spectrum (C101-C103) comes
out exactly real. Finds:

P0: S_p(k) := diag(1/sqrt(binomial(k,p))) simultaneously
    anti-Hermitianizes l_{e1}(k), l_{e2}(k), l_{e3}(k) for k=1,2,3 --
    the same binomial normalization C96 derived (then discarded for a
    different, calibration-specific reason) in build_d2_matrix. Since
    rmult_i are ALREADY anti-Hermitian (no r-space fix needed), this
    means S_p(k)(x)I_r correctly Hermitianizes D-bar_k individually,
    for every k.

P1: does a single relative scalar c (the one remaining degree of
    freedom per level, per Schur's lemma for an irreducible su(2) rep)
    make S_total := blockdiag(S_p(1)(x)I_r, c*S_p(2)(x)I_r) also
    Hermitianize the OFF-DIAGONAL M_1 block of the full 2-level D_PW?
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp
from sympy import S as Sym
from sympy.physics.quantum.cg import CG

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c105.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, k: int):
    """Certified sign/transpose rule from C95 (k=1) and C96/C97/C98
    (k=2,3,4) -- reused unchanged (matches C99-C104's own copy)."""
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


def build_multiplication_matrix(c85_mod, k: int) -> sp.Matrix:
    j1 = Sym(k) / 2
    j2 = Sym(1) / 2
    j_target = j1 + Sym(1) / 2
    a = Sym(1) / 2
    b = Sym(1) / 2
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


def S_p(k: int) -> sp.Matrix:
    """Binomial-normalization candidate for the p-space Hermitianizing
    transform -- the same formula C96 derived for build_d2_matrix's
    own unitary-basis draft, before discarding it there for an
    unrelated (calibration-convention) reason."""
    dim = k + 1
    return sp.diag(*[1 / sp.sqrt(sp.binomial(k, p)) for p in range(dim)])


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    # P0: S_p(k) simultaneously anti-Hermitianizes l_e1,l_e2,l_e3, for
    # k=1,2,3, and rmult_i are already anti-Hermitian (no r-fix needed).
    right_mult = [
        c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
    ]
    rmult_anti_hermitian = all(sp.simplify(r.H + r) == sp.zeros(2, 2) for r in right_mult)
    print(f"rmult_i anti-Hermitian (all 3, no r-fix needed): {rmult_anti_hermitian}")

    p0_per_k = {}
    for k in (1, 2, 3):
        l1, l2, l3 = c85.build_l_matrices(k, "repaired")
        dim = k + 1
        Sk = S_p(k)
        Sk_inv = Sk.inv()
        all_anti = True
        for name, l_mat in [("l1", l1), ("l2", l2), ("l3", l3)]:
            lp = sp.simplify(Sk * l_mat * Sk_inv)
            anti = sp.simplify(lp.H + lp) == sp.zeros(dim, dim)
            all_anti = all_anti and anti
        p0_per_k[k] = all_anti
        print(f"P0: k={k} S_p(k) simultaneously anti-Hermitianizes l_e1,l_e2,l_e3: {all_anti}")

    p0_ok = rmult_anti_hermitian and all(p0_per_k.values())
    print(f"P0 overall: {p0_ok}")

    # P1: does a single scalar c solve the cross-level compatibility
    # condition c^2 * P2_joint * M1 == M1 * P1_joint exactly?
    M1 = build_multiplication_matrix(c85, 1)
    dim1, dim2 = 2, 3
    P1_diag = sp.simplify(S_p(1).H * S_p(1))
    P2_diag = sp.simplify(S_p(2).H * S_p(2))
    P1_joint = sp.Matrix(sp.kronecker_product(sp.eye(dim1), P1_diag))
    P2_joint = sp.Matrix(sp.kronecker_product(sp.eye(dim2), P2_diag))

    c = sp.symbols("c", positive=True)
    lhs = c**2 * P2_joint * M1
    rhs = M1 * P1_joint
    diff = sp.simplify(lhs - rhs)
    nonzero_entries = [
        (i, j, diff[i, j]) for i in range(diff.rows) for j in range(diff.cols) if diff[i, j] != 0
    ]
    print(f"\nNonzero entries in c^2*P2*M1 - M1*P1 ({len(nonzero_entries)} total):")
    for i, j, expr in nonzero_entries:
        print(f"  ({i},{j}): {expr} = 0")

    c_solutions_per_entry = []
    for _i, _j, expr in nonzero_entries:
        sols = sp.solve(sp.Eq(expr, 0), c)
        c_solutions_per_entry.append(sols[0] if sols else None)
    distinct_solutions = {sp.simplify(s) for s in c_solutions_per_entry if s is not None}
    print(f"\nDistinct c-values required per entry: {sorted(distinct_solutions, key=str)}")

    p1_single_c_exists = len(distinct_solutions) <= 1
    p2_genuinely_inconsistent = len(distinct_solutions) > 1

    if not p0_ok:
        verdict = "P0_REUSE_BUG__STOP_BEFORE_DRAWING_CONCLUSIONS"
    elif p1_single_c_exists and distinct_solutions:
        verdict = "SINGLE_C_FOUND__CANDIDATE_S_EXPLAINS_REAL_SPECTRUM"
    elif p2_genuinely_inconsistent:
        verdict = "BLOCK_DIAGONAL_S_RULED_OUT__CROSS_LEVEL_CONDITION_GENUINELY_INCONSISTENT"
    else:
        verdict = "UNDERDETERMINED__NO_CONSTRAINT_FOUND_INCONCLUSIVE"

    out = {
        "rmult_anti_hermitian": rmult_anti_hermitian,
        "p0_per_k": {str(k): v for k, v in p0_per_k.items()},
        "p0_ok": p0_ok,
        "nonzero_constraint_entries": [[i, j, str(e)] for i, j, e in nonzero_entries],
        "c_solutions_per_entry": [str(s) for s in c_solutions_per_entry],
        "distinct_c_solutions": [str(s) for s in sorted(distinct_solutions, key=str)],
        "p1_single_c_exists": p1_single_c_exists,
        "p2_genuinely_inconsistent": p2_genuinely_inconsistent,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
