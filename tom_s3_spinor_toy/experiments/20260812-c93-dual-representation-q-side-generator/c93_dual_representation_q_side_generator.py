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


def casimir_non_discrimination_check(k: int, l1: sp.Matrix, l2: sp.Matrix, l3: sp.Matrix) -> dict:
    """[VERIFIED-sympy] Same-day correction check: this module's own
    decision.md originally called a Casimir/so(4) check "the genuinely
    decisive next test" for validating L_i. That overclaims: su(2) has a
    unique irrep per dimension, so its Casimir eigenvalue is fully
    determined by dimension alone -- C_L=C_R follows AUTOMATICALLY from
    L_i=-l_{e_i}^T whenever C_R is scalar (since (A^2)^T=(A^T)^2, so
    C_L=C_R^T, and C_R^T=C_R whenever C_R is already scalar). This does
    NOT discriminate L_i from any other valid (k+1)-dim su(2)
    representation -- confirmed directly here, not assumed."""
    dim = k + 1
    C_R = sp.simplify(l1 * l1 + l2 * l2 + l3 * l3)
    L1, L2, L3 = -l1.T, -l2.T, -l3.T
    C_L = sp.simplify(L1 * L1 + L2 * L2 + L3 * L3)
    scalar_val = C_R[0, 0]
    C_R_is_scalar = sp.simplify(C_R - scalar_val * sp.eye(dim)) == sp.zeros(dim, dim)
    C_L_equals_C_R = sp.simplify(C_L - C_R) == sp.zeros(dim, dim)
    C_L_equals_C_R_transpose_shortcut = sp.simplify(C_L - C_R.T) == sp.zeros(dim, dim)
    return {
        "k": k,
        "casimir_eigenvalue": str(scalar_val),
        "C_R_is_scalar": bool(C_R_is_scalar),
        "C_L_equals_C_R": bool(C_L_equals_C_R),
        "matches_transpose_shortcut": bool(C_L_equals_C_R_transpose_shortcut),
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

    print("\n=== Same-day correction check: is the Casimir/so(4) test actually discriminating? ===")
    casimir_results = {}
    for k in range(1, 5):
        l1, l2, l3 = c85.build_l_matrices(k, "repaired")
        cr = casimir_non_discrimination_check(k, l1, l2, l3)
        casimir_results[str(k)] = cr
        print(
            f"  k={k}: casimir_eigenvalue={cr['casimir_eigenvalue']}, "
            f"C_R_is_scalar={cr['C_R_is_scalar']}, C_L_equals_C_R={cr['C_L_equals_C_R']} "
            "(automatic once C_R is scalar -- confirms the check is NOT discriminating)"
        )
    casimir_all_automatic = all(
        v["C_R_is_scalar"] and v["C_L_equals_C_R"] and v["matches_transpose_shortcut"]
        for v in casimir_results.values()
    )
    print(f"\nCasimir match is automatic for every k tested: {casimir_all_automatic}")

    verdict = (
        "DUAL_REPRESENTATION_VALID_SU2_REP__HERMITICITY_MATCHES_KNOWN_R_PATTERN"
        "__CASIMIR_CHECK_CONFIRMED_NON_DISCRIMINATING"
        if p1_all_k_bracket_holds
        and p2_all_k_distinct
        and p3_matches_known_r_pattern
        and casimir_all_automatic
        else "UNEXPECTED_RESULT_REQUIRES_MANUAL_REVIEW"
    )

    out = {
        "per_k": per_k,
        "p1_all_k_bracket_holds": p1_all_k_bracket_holds,
        "p2_all_k_distinct": p2_all_k_distinct,
        "p3_hermiticity_pattern": p3_hermiticity_pattern,
        "p3_matches_known_r_pattern": p3_matches_known_r_pattern,
        "casimir_same_day_correction_check": casimir_results,
        "casimir_confirmed_non_discriminating": casimir_all_automatic,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
