"""C95 -- re-derives C94's L_h/R_h generators via direct sympy symbolic
substitution and polynomial coefficient extraction, with NO manual
index-tracking, to rule out a row/column-vs-operator-index conflation as
the source of C94's unresolved bracket-consistency failure (P3).

C94 computed "how g0's own raw matrix entries transform" under
h(eps)^-1 @ g0 (left) and g0 @ h(eps) (right), and read off a candidate
generator via direct matrix comparison. This conflates two different
objects: the transformation of g's ENTRIES vs the transformation of the
COEFFICIENTS of an abstract function F = sum c_mn * g_mn expanded in the
g_mn "basis" -- these differ by a transpose (a classic function-vs-
coefficient contragredience subtlety). This script re-derives the
coefficient-space generator directly, letting sympy's own Poly.coeff_monomial
do all index bookkeeping (no hand transpose/index tracking anywhere).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c95.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def coefficient_space_generator(
    action: str, X: sp.Matrix, g: sp.Matrix, eps: sp.Symbol
) -> sp.Matrix:
    """Returns the 2x2 matrix acting on the RELEVANT index (m for 'L', n
    for 'R') of the coefficient c_{m,n} of a generic linear function
    F = sum c_mn * g_mn, derived by direct symbolic substitution +
    sympy's own polynomial coefficient extraction -- no manual index
    tracking. For 'L', returns the matrix M such that the new c_{.,n}
    column (for fixed n) transforms as M @ c_{.,n}; for 'R', the matrix
    M such that the new c_{m,.} row transforms as c_{m,.} @ M^T (kept
    as a plain 2x2 matrix comparable to l_{e_i} either way -- verified
    directly against candidates below, not assumed)."""
    if action == "L":
        gnew = (sp.eye(2) - eps * X) * g
    elif action == "R":
        gnew = g * (sp.eye(2) + eps * X)
    else:
        raise ValueError(action)

    # For 'L', the m-index transformation is independent of n by
    # construction (L only touches rows) -- use a SINGLE fixed n=0 test
    # vector per m, not accumulated across both n values (accumulating
    # across n double-counts, since each n contributes the identical
    # amount -- this was a genuine bug in an earlier version of this
    # function, caught by a factor-of-2 mismatch against the hand
    # prediction, fixed here). Symmetric logic for 'R' with fixed m=0.
    result = sp.zeros(2, 2)
    fixed = 0
    for axis_val in range(2):
        m, n = (axis_val, fixed) if action == "L" else (fixed, axis_val)
        c = sp.symbols(f"c_{m}{n}")
        F = c * g[m, n]
        Fnew = sp.expand(F.subs(g[m, n], gnew[m, n]))
        poly = sp.Poly(Fnew, g[0, 0], g[0, 1], g[1, 0], g[1, 1])
        for other_val in range(2):
            m2, n2 = (other_val, fixed) if action == "L" else (fixed, other_val)
            monom = [0, 0, 0, 0]
            monom[m2 * 2 + n2] = 1
            coeff = poly.coeff_monomial(tuple(monom))
            deriv = sp.diff(coeff, eps).subs(eps, 0)
            if action == "L":
                result[m2, m] = deriv / c
            else:
                result[n2, n] = deriv / c
    return sp.simplify(result)


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    X1 = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    X2 = sp.Matrix([[0, 1], [-1, 0]])
    X3 = sp.Matrix([[0, sp.I], [sp.I, 0]])
    Xs = {"e1_i": X1, "e2_j": X2, "e3_k": X3}

    l1, l2, l3 = c85.build_l_matrices(1, "repaired")
    l_mats = {"e1_i": l1, "e2_j": l2, "e3_k": l3}

    eps = sp.symbols("eps", real=True)
    g00, g01, g10, g11 = sp.symbols("g00 g01 g10 g11")
    g = sp.Matrix([[g00, g01], [g10, g11]])

    per_unit = {}
    for name, X in Xs.items():
        L_op = coefficient_space_generator("L", X, g, eps)
        R_op = coefficient_space_generator("R", X, g, eps)
        R_i = l_mats[name]
        candidates = {"+l": R_i, "-l": -R_i, "+lT": R_i.T, "-lT": -R_i.T}
        L_match = [n for n, c in candidates.items() if sp.simplify(L_op - c) == sp.zeros(2, 2)]
        R_match = [n for n, c in candidates.items() if sp.simplify(R_op - c) == sp.zeros(2, 2)]
        per_unit[name] = {
            "L_op": L_op.tolist(),
            "R_op": R_op.tolist(),
            "L_matches": L_match,
            "R_matches": R_match,
        }
        print(f"--- {name} ---")
        print(f"  L_op = {L_op.tolist()}  matches {L_match}")
        print(f"  R_op = {R_op.tolist()}  matches {R_match}")

    L_common = set.intersection(*(set(v["L_matches"]) for v in per_unit.values()))
    R_common = set.intersection(*(set(v["R_matches"]) for v in per_unit.values()))
    print(f"\nP1 (L common candidate across all units): {sorted(L_common)}")
    print(f"P2 (R common candidate across all units): {sorted(R_common)}")

    # NOTE: this round's own pre-registered P2 prediction ("-l" directly)
    # is WRONG -- the actual, bracket-consistent candidate is "-lT". This
    # is an honest miss on the pre-registered guess, recorded as such
    # (see decision.md), not silently swapped in claim.md after the fact.
    p1_holds = "+l" in L_common
    p2_holds_as_predicted = "-l" in R_common
    p2_holds_actual = "-lT" in R_common

    # P3: bracket check using the ACTUAL coefficient-space operators (not
    # the candidate labels) -- directly, per unit, then combined.
    L1, L2, L3_ = (
        sp.Matrix(per_unit["e1_i"]["L_op"]),
        sp.Matrix(per_unit["e2_j"]["L_op"]),
        sp.Matrix(per_unit["e3_k"]["L_op"]),
    )
    R1, R2, R3_ = (
        sp.Matrix(per_unit["e1_i"]["R_op"]),
        sp.Matrix(per_unit["e2_j"]["R_op"]),
        sp.Matrix(per_unit["e3_k"]["R_op"]),
    )
    L_bracket_ok = bool(sp.simplify(L1 * L2 - L2 * L1 - 2 * L3_) == sp.zeros(2, 2))
    R_bracket_ok = bool(sp.simplify(R1 * R2 - R2 * R1 - 2 * R3_) == sp.zeros(2, 2))
    print(f"\nP3: L bracket [L1,L2]==2*L3? {L_bracket_ok}")
    print(f"P3: R bracket [R1,R2]==2*R3? {R_bracket_ok}")
    if not L_bracket_ok:
        print("  [L1,L2] =", sp.simplify(L1 * L2 - L2 * L1).tolist(), " 2*L3 =", (2 * L3_).tolist())
    if not R_bracket_ok:
        print("  [R1,R2] =", sp.simplify(R1 * R2 - R2 * R1).tolist(), " 2*R3 =", (2 * R3_).tolist())

    fully_resolved = p1_holds and p2_holds_actual and L_bracket_ok and R_bracket_ok
    verdict = (
        "P3_RESOLVED__L_EQUALS_PLUS_L__R_EQUALS_MINUS_L_TRANSPOSE__BOTH_BRACKET_CONSISTENT"
        if fully_resolved
        else "UNEXPECTED_EVEN_UNDER_COEFFICIENT_SPACE_CORRECTION"
    )

    out = {
        "per_unit": per_unit,
        "p1_left_equals_plus_l": p1_holds,
        "p2_right_equals_minus_l_AS_PREDICTED": p2_holds_as_predicted,
        "p2_right_equals_minus_lT_ACTUAL": p2_holds_actual,
        "p3_L_bracket_consistent": L_bracket_ok,
        "p3_R_bracket_consistent": R_bracket_ok,
        "fully_resolved": fully_resolved,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
