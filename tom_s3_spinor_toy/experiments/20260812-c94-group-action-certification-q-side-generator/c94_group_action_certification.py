"""C94 -- certifies the q-side generator sign directly from the group
action's own defining formula (differentiate symbolically, don't
hand-derive). Directed by an external reviewer after C92/C93 showed real
risk of sign errors in paper-and-pencil re-derivation.

Convention: (L_h f)(g) := f(h^-1 g), (R_h f)(g) := f(g h) -- the
standard left/right regular representation on functions on SU(2).
F_{m,n}(g) := D^{1/2}_{m,n}(g) = g_{m,n} (defining rep's own matrix
entries, since D^{1/2}(g)=g literally for j=1/2).

No formula in this script is hand-derived and trusted -- every operator
is extracted by sympy differentiation of an explicit symbolic matrix
product, then compared against Meier's own certified l_{e_i}(1) (C85).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c94.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def g_matrix(a: sp.Expr, b: sp.Expr) -> sp.Matrix:
    """The SU(2) defining representation, D^{1/2}(g)=g literally, in the
    SAME (a,b) Cayley-Dickson encoding C85 uses throughout (a=aw+I*ax,
    b=bw+I*bx)."""
    return sp.Matrix([[a, b], [-sp.conjugate(b), sp.conjugate(a)]])


def build_h_eps(unit: tuple, eps: sp.Symbol) -> sp.Matrix:
    """h(eps) = matrix form of the quaternion (1,0,0,0) + eps*unit, to
    first order in eps (the actual exponential map agrees with this to
    O(eps), which is all a first-derivative-at-0 check needs)."""
    w0, x0, y0, z0 = unit
    a = 1 + eps * (x0) * sp.I + eps * w0
    b = eps * y0 + eps * z0 * sp.I
    return g_matrix(a, b)


def build_h_eps_inverse(unit: tuple, eps: sp.Symbol) -> sp.Matrix:
    """h(eps)^-1, to first order: negate the perturbation (quaternion
    inverse of 1+eps*u is 1-eps*u to O(eps) -- verified numerically in
    main(), not assumed)."""
    return build_h_eps(unit, -eps)


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    eps = sp.symbols("eps", real=True)
    aw, ax, bw, bx = sp.symbols("aw ax bw bx", real=True)
    g0 = g_matrix(aw + sp.I * ax, bw + sp.I * bx)

    units = {"e1_i": (0, 1, 0, 0), "e2_j": (0, 0, 1, 0), "e3_k": (0, 0, 0, 1)}

    # Sanity: quaternion inverse to first order really is the negation.
    inv_check = {}
    for name, u in units.items():
        w0, x0, y0, z0 = u
        prod = c85.hamilton_product(
            (1 + eps * w0, eps * x0, eps * y0, eps * z0),
            (1 - eps * w0, -eps * x0, -eps * y0, -eps * z0),
        )
        first_order_zero = all(
            sp.series(sp.Matrix(prod)[i] - (1 if i == 0 else 0), eps, 0, 2).removeO() == 0
            for i in range(4)
        )
        inv_check[name] = bool(first_order_zero)

    l_mats = {}
    l1, l2, l3 = c85.build_l_matrices(1, "repaired")
    l_mats["e1_i"], l_mats["e2_j"], l_mats["e3_k"] = l1, l2, l3

    def matching_candidates(diff_matrix: sp.Matrix, candidates: dict) -> set:
        """Returns the SET of all candidate names matching diff_matrix
        exactly. A symmetric or antisymmetric l_{e_i} can make two of the
        four candidate FORMULAS coincide in VALUE for that one unit --
        report the full set, don't pick one; consistency across units is
        checked by INTERSECTING these sets, not by comparing them for
        equality (equality is the wrong check when different units have
        different symmetry types, see e1/e3 symmetric vs e2 antisymmetric
        l_{e_i} -- self-caught while first analyzing this round's own
        results, not assumed)."""
        return {
            cand_name
            for cand_name, cand in candidates.items()
            if sp.simplify(diff_matrix - cand) == sp.zeros(2, 2)
        }

    per_unit = {}
    for name, u in units.items():
        h_eps = build_h_eps(u, eps)
        h_eps_inv = build_h_eps_inverse(u, eps)
        R_i = l_mats[name]
        candidates = {"+l": R_i, "-l": -R_i, "+lT": R_i.T, "-lT": -R_i.T}

        # RIGHT translation: (R_h F)(g) = F(g h) -- differentiate g0 @ h(eps).
        # d/deps|_0 (g0 @ h(eps)) = g0 @ X_i  =>  candidate multiplies g0
        # FROM THE RIGHT (g0 @ cand), not the left.
        right_prod = g0 * h_eps
        right_diff = sp.simplify(right_prod.applyfunc(lambda e: sp.diff(e, eps).subs(eps, 0)))
        right_candidates = {name_: sp.simplify(g0 * cand) for name_, cand in candidates.items()}
        right_match = matching_candidates(right_diff, right_candidates)

        # LEFT translation: (L_h F)(g) = F(h^-1 g) -- differentiate h(eps)^-1 @ g0.
        # d/deps|_0 (h(eps)^-1 @ g0) = X_i @ g0  =>  candidate multiplies g0
        # FROM THE LEFT (cand @ g0).
        left_prod = h_eps_inv * g0
        left_diff = sp.simplify(left_prod.applyfunc(lambda e: sp.diff(e, eps).subs(eps, 0)))
        left_candidates = {name_: sp.simplify(cand * g0) for name_, cand in candidates.items()}
        left_match = matching_candidates(left_diff, left_candidates)

        per_unit[name] = {
            "right_translation_matches": sorted(right_match),
            "left_translation_matches": sorted(left_match),
        }
        print(f"--- {name} ---")
        print(f"  RIGHT translation matches: {sorted(right_match)}")
        print(f"  LEFT translation matches:  {sorted(left_match)}")

    # Consistency across the 3 units is an INTERSECTION of each unit's
    # match set, not equality of the sets themselves -- a symmetric l_{e_i}
    # (e1, e3) and an antisymmetric one (e2) produce different-looking but
    # equally valid 2-way ambiguities for the SAME underlying rule.
    right_sets = [set(v["right_translation_matches"]) for v in per_unit.values()]
    left_sets = [set(v["left_translation_matches"]) for v in per_unit.values()]
    right_common = set.intersection(*right_sets) if right_sets else set()
    left_common = set.intersection(*left_sets) if left_sets else set()
    p1_right_consistent = len(right_common) >= 1
    p2_left_consistent = len(left_common) >= 1

    print(f"\nP1 (RIGHT translation: candidate common to all 3 units): {p1_right_consistent}")
    print(f"  -> right-translation candidate(s): {sorted(right_common)}")
    print(f"P2 (LEFT translation: candidate common to all 3 units): {p2_left_consistent}")
    print(f"  -> left-translation candidate(s): {sorted(left_common)}")
    print(f"\nQuaternion first-order inverse sanity check: {inv_check}")

    # Bracket-consistency cross-check (P3, added while analyzing P1/P2's own
    # result -- NOT predicted in advance, exploratory): if L_h1 L_h2 = L_h1h2
    # (verified separately, group-level) then dL MUST be a genuine (non-anti)
    # Lie algebra homomorphism, so [Y1,Y2] should equal 2*Y3 for the SAME
    # normalization l_{e_i} itself satisfies. Check this directly against
    # the LEFT-translation candidate found above.
    bracket_consistent = None
    if p2_left_consistent:
        left_cand_name = min(left_common)
        # reconstruct Y_i per unit using the matched candidate formula
        y_by_unit = {}
        for name, u in units.items():
            R_i = l_mats[name]
            lookup = {"+l": R_i, "-l": -R_i, "+lT": R_i.T, "-lT": -R_i.T}
            y_by_unit[name] = lookup[left_cand_name]
        Y1, Y2, Y3 = y_by_unit["e1_i"], y_by_unit["e2_j"], y_by_unit["e3_k"]
        bracket_lhs = sp.simplify(Y1 * Y2 - Y2 * Y1)
        bracket_rhs_pos = sp.simplify(2 * Y3)
        bracket_consistent = bool(sp.simplify(bracket_lhs - bracket_rhs_pos) == sp.zeros(2, 2))
        print(f"\nP3 (bracket consistency, exploratory): [Y1,Y2] == 2*Y3? {bracket_consistent}")
        if not bracket_consistent:
            print("  [Y1,Y2] =", bracket_lhs.tolist())
            print("  2*Y3    =", bracket_rhs_pos.tolist())
            print(
                "  UNRESOLVED: this contradicts the expectation that dL of a verified group "
                "representation (L_h1 L_h2 = L_h1h2, confirmed separately) must be a genuine "
                "Lie algebra homomorphism. A follow-up BCH-based hand derivation did not cleanly "
                "resolve this discrepancy either -- recorded as an open inconsistency, not guessed."
            )

    verdict = (
        "GROUP_ACTION_GENERATORS_CONSISTENT_ACROSS_UNITS_BUT_BRACKET_CHECK_UNRESOLVED"
        if p1_right_consistent and p2_left_consistent and not bracket_consistent
        else (
            "GROUP_ACTION_FULLY_CONSISTENT_INCLUDING_BRACKET"
            if p1_right_consistent and p2_left_consistent and bracket_consistent
            else "INCONSISTENT_ACROSS_UNITS_SETUP_STILL_NEEDS_REVIEW"
        )
    )

    out = {
        "inverse_first_order_sanity": inv_check,
        "per_unit": per_unit,
        "p1_right_translation_consistent": p1_right_consistent,
        "right_translation_candidates": sorted(right_common),
        "p2_left_translation_consistent": p2_left_consistent,
        "left_translation_candidates": sorted(left_common),
        "p3_bracket_consistent_exploratory": bracket_consistent,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
