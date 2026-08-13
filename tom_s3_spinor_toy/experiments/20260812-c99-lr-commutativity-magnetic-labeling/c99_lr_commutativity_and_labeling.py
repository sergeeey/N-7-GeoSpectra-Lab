"""C99 -- before building the multiplication-type coupling operator
(task #59, scoped by C90's own decision.md), this round:

P0 (SELF-CORRECTED mid-round, see below): the raw (k+1)x(k+1) matrix
    commutator [L_i(k), R_j(k)] is NOT the right object to check --
    L_i and R_i act on DIFFERENT tensor factors (q and p respectively)
    of the (k+1)^2-dim "matrix coefficient" space D^k_{q,p}(g), not on
    the same (k+1)-dim space. Checked directly: the raw commutator is
    nonzero for i!=j at every k, which is EXPECTED and uninformative
    (L_i, R_i are unrelated (k+1)x(k+1) matrices a priori -- nothing
    requires them to commute AS ORDINARY MATRICES). The actually
    meaningful, correctly-posed question is whether the TENSOR-EMBEDDED
    operators L_i(x)I and I(x)R_j^T commute on the full (k+1)^2-dim
    space -- and this is GUARANTEED by plain matrix associativity
    (A(x)I and I(x)B always commute, for ANY A,B) -- it needs no
    empirical/symbolic check at all, and is not informative about
    whether the specific L_i,R_i values found in C91-C98 are correct.
    Verified this directly for one representative case (k=2) as an
    implementation sanity-anchor only, not as a criterion the round's
    verdict depends on.
P1/P2: extracts the magnetic-number labeling m_q(k,q), m_p(k,p)
    DIRECTLY from the certified L_1(k), R_1(k) diagonal entries (not
    assumed from l_{e1}(k)'s own raw convention, which C96-C98 already
    showed can differ by sign depending on k).
P3: identifies which literal p-index corresponds to the extremal
    state (m=j1=k/2) used in C90's own single-representative
    Clebsch-Gordan check, using the ACTUAL R_1(k) values -- not a
    naive assumption that p=k is always the extremal state (which, as
    this round finds, is true for k>=2 but FALSE for k=1, where R_1(1)
    is sign-flipped relative to l_{e1}(1) itself).

L_i(k), R_i(k) are NOT re-derived here -- this round reuses the
already-certified formulas directly (C95 for k=1, C96/C97/C98's shared
construction for k=2,3,4), applying only the certified sign/transpose
rule, since re-deriving already-certified generators would be
redundant with C92-C98's own extensive verification.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp
from sympy import S
from sympy.physics.quantum.cg import CG

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c99.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def certified_L_R(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix, k: int):
    """Applies the CERTIFIED sign/transpose rule from C95 (k=1) and
    C96/C97/C98 (k=2,3,4) -- does not re-derive it."""
    l_mats = [l1, l2, l3]
    if k == 1:
        L = [m for m in l_mats]
        R = [-m.T for m in l_mats]
    else:
        L = [-m.T for m in l_mats]
        R = [m for m in l_mats]
    return L, R


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    # P0 sanity-anchor only (see module docstring for why the raw
    # (k+1)x(k+1) matrix commutator is the wrong object to check): the
    # CORRECTLY tensor-embedded action always commutes, by matrix
    # associativity, for ANY choice of L,R -- verify this directly for
    # one representative case as an implementation check, not a
    # criterion of the round's own verdict.
    k_anchor = 2
    l1a, l2a, l3a = c85.build_l_matrices(k_anchor, "repaired")
    L_anchor, R_anchor = certified_L_R(l1a, l2a, l3a, k_anchor)
    dim_anchor = k_anchor + 1
    I_anchor = sp.eye(dim_anchor)
    L_full = sp.Matrix(sp.kronecker_product(L_anchor[0], I_anchor))
    R_full = sp.Matrix(sp.kronecker_product(I_anchor, R_anchor[1].T))
    tensor_embedded_commutes = sp.simplify(L_full * R_full - R_full * L_full) == sp.zeros(
        dim_anchor * dim_anchor, dim_anchor * dim_anchor
    )
    print(f"P0 sanity-anchor (k={k_anchor}, tensor-embedded [L1,R2]=0): {tensor_embedded_commutes}")

    per_k = {}
    for k in (1, 2, 3, 4):
        l1, l2, l3 = c85.build_l_matrices(k, "repaired")
        L, R = certified_L_R(l1, l2, l3, k)
        dim = k + 1

        # P1/P2: magnetic-number labeling, directly from L_1, R_1's own
        # diagonal entries (both are diagonal since l_{e1}(k) is
        # diagonal and +-transpose of a diagonal matrix is itself).
        L1, R1 = L[0], R[0]
        m_q_raw = [sp.nsimplify(L1[q, q] / sp.I) for q in range(dim)]
        m_p_raw = [sp.nsimplify(R1[p, p] / sp.I) for p in range(dim)]
        # convert to "physical" spin units (j1=k/2, m ranges -j1..j1 in
        # integer steps) -- Meier's own raw convention is 2x this.
        m_q_phys = [v / 2 for v in m_q_raw]
        m_p_phys = [v / 2 for v in m_p_raw]

        q_step_uniform = (
            len({m_q_phys[q + 1] - m_q_phys[q] for q in range(dim - 1)}) <= 1 if dim > 1 else True
        )
        p_step_uniform = (
            len({m_p_phys[p + 1] - m_p_phys[p] for p in range(dim - 1)}) <= 1 if dim > 1 else True
        )

        # P3: which literal p has m_p_phys == j1 (the extremal state
        # C90's own check used, m1=j1)?
        j1 = S(k) / 2
        extremal_p_candidates = [p for p in range(dim) if m_p_phys[p] == j1]

        cg_value = None
        cg_matches_naive_p_equals_k = None
        if extremal_p_candidates:
            p_extremal = extremal_p_candidates[0]
            j2 = S(1) / 2
            m2 = S(1) / 2
            j_target = j1 + S(1) / 2
            cg = CG(j1, j1, j2, m2, j_target, j1 + m2)
            cg_value = str(cg.doit())
            cg_matches_naive_p_equals_k = p_extremal == k

        per_k[str(k)] = {
            "m_q_physical": [str(v) for v in m_q_phys],
            "m_p_physical": [str(v) for v in m_p_phys],
            "q_spacing_uniform": q_step_uniform,
            "p_spacing_uniform": p_step_uniform,
            "extremal_p_index_for_m_equals_j1": extremal_p_candidates,
            "extremal_p_equals_k_naive_assumption": cg_matches_naive_p_equals_k,
            "cg_coefficient_at_extremal": cg_value,
        }
        print(f"--- k={k} ---")
        print(f"  m_q(physical) = {[str(v) for v in m_q_phys]}")
        print(f"  m_p(physical) = {[str(v) for v in m_p_phys]}")
        print(
            f"  extremal p (m=j1={j1}): {extremal_p_candidates}  (naive p=k assumption holds: {cg_matches_naive_p_equals_k})"
        )

    p1_ok = all(per_k[str(k)]["q_spacing_uniform"] for k in (1, 2, 3, 4))
    p2_ok = all(per_k[str(k)]["p_spacing_uniform"] for k in (1, 2, 3, 4))
    p3_ok = all(
        per_k[str(k)]["extremal_p_index_for_m_equals_j1"]
        and per_k[str(k)]["cg_coefficient_at_extremal"] == "1"
        for k in (1, 2, 3)
    )
    k1_sign_flip_found = not per_k["1"]["extremal_p_equals_k_naive_assumption"]

    if not tensor_embedded_commutes:
        # would indicate an IMPLEMENTATION bug (this is guaranteed by
        # matrix associativity for any L,R -- see module docstring),
        # not a physics finding about L_i/R_i themselves
        verdict = "P0_SANITY_ANCHOR_FAILED__IMPLEMENTATION_BUG_NOT_A_PHYSICS_FINDING"
    elif not (p1_ok and p2_ok):
        verdict = "MAGNETIC_LABELING_NOT_CLEAN__REVISIT_BEFORE_CG_ASSEMBLY"
    elif not p3_ok:
        verdict = "P3_MISMATCH_WITH_C90__CONVENTION_RECONCILIATION_NEEDED"
    else:
        verdict = "ALL_VERIFIED__LABELING_READY_FOR_FULL_CG_ASSEMBLY"

    out = {
        "per_k": per_k,
        "p0_tensor_embedded_sanity_anchor_ok": tensor_embedded_commutes,
        "p1_m_q_spacing_uniform_all_k": p1_ok,
        "p2_m_p_spacing_uniform_all_k": p2_ok,
        "p3_matches_c90_extremal_check": p3_ok,
        "k1_extremal_p_sign_flip_found_relative_to_naive_p_equals_k": k1_sign_flip_found,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nk=1 naive-labeling sign flip found: {k1_sign_flip_found}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
