"""C92 -- tests whether the naive "swap the product order" analog of
C85's right_mult_matrix_on_ab (i.e. LEFT quaternion multiplication,
expressed in the SAME (a,b) complex-linear encoding used for RIGHT
multiplication) exists as a genuine complex-linear 2x2 matrix, for each
of the three quaternion units e1(i), e2(j), e3(k).

Context: task #59 (building the multiplication-type coupling operator
named in C90) needs a q-side ("left-regular-representation") analog of
Meier's l_{e_i} (which acts on p, the "right-regular" orbital index).
The most natural first hypothesis is the same construction as C85's
right_mult_matrix_on_ab, with hamilton_product(q, unit) replaced by
hamilton_product(unit, q). This script tests that hypothesis directly,
reusing C85's own verified hamilton_product (unmodified) -- no new
quaternion-algebra convention introduced.

Also cross-checks: for e1 specifically, where left-mult IS C-linear,
does the resulting matrix match Meier's own l_{e1}(k=1) (from C85's
certified build_l_matrices)? This distinguishes "coincides with l_{e_i}"
from "is merely linear but a different operator."
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c92.json"

C85 = None  # populated in main via load_module


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def left_mult_linearity_check(unit: tuple) -> dict:
    """Mirrors C85's right_mult_matrix_on_ab exactly, except using
    hamilton_product(unit, q) (LEFT multiplication) instead of
    hamilton_product(q, unit) (RIGHT multiplication). Returns the
    candidate matrix AND whether the complex-linearity check it implies
    actually holds (does NOT assert -- a failure here is the expected,
    informative result for j,k, not a bug)."""
    I_UNIT = sp.I
    aw, ax, bw, bx = sp.symbols("aw ax bw bx", real=True)
    q = (aw, ax, bw, bx)
    result = C85.hamilton_product(unit, q)
    w, x, y, z = result
    a_prime = sp.expand(w + x * I_UNIT)
    b_prime = sp.expand(y + z * I_UNIT)
    m00 = sp.diff(a_prime, aw)
    m01 = sp.diff(a_prime, bw)
    m10 = sp.diff(b_prime, aw)
    m11 = sp.diff(b_prime, bw)
    M = sp.Matrix([[m00, m01], [m10, m11]])
    check_a = sp.expand((m00 * (aw + I_UNIT * ax) + m01 * (bw + I_UNIT * bx)) - a_prime)
    check_b = sp.expand((m10 * (aw + I_UNIT * ax) + m11 * (bw + I_UNIT * bx)) - b_prime)
    is_linear = check_a == 0 and check_b == 0
    return {
        "candidate_matrix": M.tolist(),
        "residual_a": str(check_a),
        "residual_b": str(check_b),
        "is_complex_linear": bool(is_linear),
    }


def main() -> None:
    global C85
    C85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    units = {"e1_i": (0, 1, 0, 0), "e2_j": (0, 0, 1, 0), "e3_k": (0, 0, 0, 1)}
    results = {}
    for name, u in units.items():
        r = left_mult_linearity_check(u)
        results[name] = r
        print(
            f"{name}: C-linear={r['is_complex_linear']}, "
            f"candidate={r['candidate_matrix']}, "
            f"residual_a={r['residual_a']}, residual_b={r['residual_b']}"
        )

    p1_e1_linear = results["e1_i"]["is_complex_linear"]
    p2_e2_e3_not_linear = (
        not results["e2_j"]["is_complex_linear"] and not results["e3_k"]["is_complex_linear"]
    )
    print(f"\nP1 (e1 C-linear): {p1_e1_linear}")
    print(f"P2 (e2,e3 NOT C-linear): {p2_e2_e3_not_linear}")

    print("\n=== Cross-check: does e1's candidate match Meier's own l_e1(k=1)? ===")
    l1, _l2, _l3 = C85.build_l_matrices(1, "repaired")
    e1_candidate = sp.Matrix(results["e1_i"]["candidate_matrix"])
    matches_l1 = sp.simplify(e1_candidate - l1) == sp.zeros(2, 2)
    matches_neg_l1 = sp.simplify(e1_candidate + l1) == sp.zeros(2, 2)
    print(f"l_e1(k=1) = {l1.tolist()}")
    print(f"e1 left-mult candidate == l_e1(k=1): {matches_l1}")
    print(f"e1 left-mult candidate == -l_e1(k=1): {matches_neg_l1}")

    verdict = (
        "NAIVE_LEFT_MULT_ANALOG_BLOCKED_FOR_J_K__ONE_SIDED_COMPLEX_STRUCTURE_CONFIRMED"
        if p1_e1_linear and p2_e2_e3_not_linear
        else "UNEXPECTED_RESULT_REQUIRES_MANUAL_REVIEW"
    )

    out = {
        "per_unit_results": results,
        "p1_e1_c_linear": p1_e1_linear,
        "p2_e2_e3_not_c_linear": p2_e2_e3_not_linear,
        "e1_candidate_matches_l_e1_k1": matches_l1,
        "e1_candidate_matches_neg_l_e1_k1": matches_neg_l1,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
