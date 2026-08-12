"""C93 -- tests whether the dual/contragredient representation
L_i := -l_{e_i}(k)^T (transpose and negation of Meier's certified
p-generator, C85) defines a genuine su(2) representation, for general k.

Context: C92 falsified the naive "swap quaternion-multiplication order"
hypothesis for the q-side generator (LEFT quaternion multiplication is
not complex-linear in the (a,b) encoding for e2(j)/e3(k)). Scoping this
round clarified WHY: the (a,b) row/column matrix-entry picture is
inescapably antilinear for left translation (unitarity ties a matrix's
rows together via conjugation). The abstract Peter-Weyl decomposition
L^2(G) = V_j (x) V_j* avoids this -- V_j*'s representation is the
CONTRAGREDIENT representation, sigma(X) = -rho(X)^T, a purely linear
construction. This script tests that construction directly.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c93.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def bracket_residuals_for(l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix) -> dict:
    """Same normalization C85's own bracket_residuals checks: [l1,l2]=2*l3 cyclic."""
    r12 = sp.simplify(l1 * l2 - l2 * l1 - 2 * l3)
    r23 = sp.simplify(l2 * l3 - l3 * l2 - 2 * l1)
    r31 = sp.simplify(l3 * l1 - l1 * l3 - 2 * l2)
    dim = l1.shape[0]
    zero = sp.zeros(dim, dim)
    return {
        "bracket_12_holds": r12 == zero,
        "bracket_23_holds": r23 == zero,
        "bracket_31_holds": r31 == zero,
    }


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    per_k = {}
    for k in range(1, 6):
        l1, l2, l3 = c85.build_l_matrices(k, "repaired")
        L1, L2, L3 = -l1.T, -l2.T, -l3.T
        dim = k + 1
        zero = sp.zeros(dim, dim)

        brackets = bracket_residuals_for(L1, L2, L3)
        su2_holds = all(brackets.values())

        same_as_R = (
            sp.simplify(L1 - l1) == zero
            and sp.simplify(L2 - l2) == zero
            and sp.simplify(L3 - l3) == zero
        )
        neg_of_R = (
            sp.simplify(L1 + l1) == zero
            and sp.simplify(L2 + l2) == zero
            and sp.simplify(L3 + l3) == zero
        )
        distinct_from_R = not (same_as_R or neg_of_R)

        r_anti_hermitian = all(sp.simplify(g.H + g) == zero for g in (l1, l2, l3))
        l_anti_hermitian = all(sp.simplify(g.H + g) == zero for g in (L1, L2, L3))

        per_k[str(k)] = {
            "su2_bracket_holds": bool(su2_holds),
            "L_equals_R": bool(same_as_R),
            "L_equals_neg_R": bool(neg_of_R),
            "L_distinct_from_R": bool(distinct_from_R),
            "R_anti_hermitian": bool(r_anti_hermitian),
            "L_anti_hermitian": bool(l_anti_hermitian),
        }
        print(
            f"k={k}: su2_bracket_holds={su2_holds}, L_distinct_from_R={distinct_from_R}, "
            f"R_anti_hermitian={r_anti_hermitian}, L_anti_hermitian={l_anti_hermitian}"
        )

    p1_all_k_bracket_holds = all(v["su2_bracket_holds"] for v in per_k.values())
    p2_all_k_distinct = all(v["L_distinct_from_R"] for v in per_k.values())
    p3_hermiticity_pattern = {k: v["L_anti_hermitian"] for k, v in per_k.items()}
    p3_matches_known_r_pattern = all(
        per_k[k]["L_anti_hermitian"] == per_k[k]["R_anti_hermitian"] for k in per_k
    )

    print(f"\nP1 (su(2) bracket holds, all k=1..5): {p1_all_k_bracket_holds}")
    print(f"P2 (L distinct from +-R, all k=1..5): {p2_all_k_distinct}")
    print(f"P3 Hermiticity pattern (k -> L anti-Hermitian?): {p3_hermiticity_pattern}")
    print(f"P3 L's Hermiticity pattern matches R's own known pattern: {p3_matches_known_r_pattern}")

    verdict = (
        "DUAL_REPRESENTATION_VALID_SU2_REP__HERMITICITY_MATCHES_KNOWN_R_PATTERN"
        if p1_all_k_bracket_holds and p2_all_k_distinct and p3_matches_known_r_pattern
        else "UNEXPECTED_RESULT_REQUIRES_MANUAL_REVIEW"
    )

    out = {
        "per_k": per_k,
        "p1_all_k_bracket_holds": p1_all_k_bracket_holds,
        "p2_all_k_distinct": p2_all_k_distinct,
        "p3_hermiticity_pattern": p3_hermiticity_pattern,
        "p3_matches_known_r_pattern": p3_matches_known_r_pattern,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
