r"""C202: apply the C201-calibrated T_i U = U L_i intertwiner test to Tom
Lawrence's own real l=1 matrices (eqs 106-108, 118, 123-125 of "Ket spaces
and harmonics of S^n", v5, 2026-09-07), instead of the C201 known-answer
control.

Part 0 is a transcription self-check: eq(123)-(125) were read off a PDF by
eye, so they are independently reconstructed here from the more primitive
eq(106)-(108) + eq(118) via eq(122) (Gamma'_3(T) = z Gamma_3(T) z^-1) before
anything else is trusted.

Part 1 solves for an intertwiner U using the T_12<->Lz and T_23<->Lx role
correspondence Tom states himself in his own eqs (67)-(69), holding out
T_31<->Ly as an independent check -- same holdout discipline as C201 Part 3.

Part 2, if the holdout fails under U alone, checks the TRANSPOSE/NEGATIVE/
NEGATIVE_TRANSPOSE variants before concluding NO_SIMPLE_RELATION -- this
project's own 2026-07-28 finding (experiments/20260728-tom-so3-harmonics-
sign-check/TRANSPOSE_LEMMA.md) is that an asymmetric so(3) generator
compared the wrong way silently produces exactly a transpose or
negative-transpose artifact, so that must be ruled out before "mismatch" is
reported as a real physics/convention finding.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

IMAG = sp.I
SQRT2 = sp.sqrt(2)


def zero_check(expr: sp.Expr | sp.MatrixBase) -> bool:
    # `sp.Matrix == 0` always returns False regardless of content (Matrix's
    # __eq__ never coerces int 0 to a zero matrix) -- caught live in this
    # round's first run, where every Part 0/1/2 comparison silently reported
    # False no matter what. Must check entrywise for a Matrix input.
    simplified = sp.simplify(sp.expand_complex(expr))
    if isinstance(simplified, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in simplified)
    return simplified == 0


# --- Part 0: reconstruct Tom's eq (123)-(125) from his more primitive
# eq (106)-(108) [real basis, "Gamma_3(T_ij) = -T_ij"] + eq (118) [z] via
# eq (122), as a transcription self-check on eq (123)-(125) read off the PDF.


def part0_transcription_check() -> dict:
    # Tom's eq (103)-(105): T_ij, the DEFINING representation (real basis).
    t23 = sp.Matrix([[0, 0, 0], [0, 0, -IMAG], [0, IMAG, 0]])
    t31 = sp.Matrix([[0, 0, IMAG], [0, 0, 0], [-IMAG, 0, 0]])
    t12 = sp.Matrix([[0, -IMAG, 0], [IMAG, 0, 0], [0, 0, 0]])

    # Tom's eq (99): Gamma_3(T_ij) = -T_ij (vector-multiplet representation).
    # BUG CAUGHT BY THIS SELF-CHECK (first run): T23's negation was applied
    # correctly but T12/T31 were mistakenly transcribed as T_ij itself, not
    # -T_ij -- Part 0 then correctly failed on exactly those two. Fixed here.
    g_t23 = -t23
    g_t31 = -t31
    g_t12 = -t12

    # Tom's eq (118): change-of-basis matrix z (real -> complex/m-eigenbasis).
    z = sp.Matrix([[1, IMAG, 0], [0, 0, 1], [1, -IMAG, 0]])
    z_inv = z.inv()

    # Tom's eq (122): Gamma'_3(T_ij) = z Gamma_3(T_ij) z^-1.
    gp_t12_reconstructed = sp.simplify(z * g_t12 * z_inv)
    gp_t23_reconstructed = sp.simplify(z * g_t23 * z_inv)
    gp_t31_reconstructed = sp.simplify(z * g_t31 * z_inv)

    # Eq (123)-(125) as transcribed by eye from the PDF.
    gp_t12_transcribed = sp.diag(1, 0, -1)
    gp_t23_transcribed = sp.Matrix(
        [[0, -1, 0], [sp.Rational(-1, 2), 0, sp.Rational(1, 2)], [0, 1, 0]]
    )
    gp_t31_transcribed = sp.Matrix(
        [
            [0, -IMAG, 0],
            [IMAG * sp.Rational(1, 2), 0, IMAG * sp.Rational(1, 2)],
            [0, -IMAG, 0],
        ]
    )

    match_t12 = zero_check(gp_t12_reconstructed - gp_t12_transcribed)
    match_t23 = zero_check(gp_t23_reconstructed - gp_t23_transcribed)
    match_t31 = zero_check(gp_t31_reconstructed - gp_t31_transcribed)

    return {
        "match_t12": match_t12,
        "match_t23": match_t23,
        "match_t31": match_t31,
        "reconstructed_t12": str(gp_t12_reconstructed),
        "reconstructed_t23": str(gp_t23_reconstructed),
        "reconstructed_t31": str(gp_t31_reconstructed),
        "all_match": match_t12 and match_t23 and match_t31,
    }


def part1_intertwiner_search() -> dict:
    # Our own C201 Part 2 construction (l=1 ladder-operator matrices).
    lp = SQRT2 * sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    lm = SQRT2 * sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    lz = sp.diag(1, 0, -1)
    lx = sp.simplify((lp + lm) / 2)
    ly = sp.simplify((lp - lm) / (2 * IMAG))

    # Tom's eq (123)-(125), role-identified via his own eq (67)-(69):
    # T_12 <-> L_z (omega^12), T_23 <-> L_x (omega^23), T_31 <-> L_y (omega^31).
    t_role_z = sp.diag(1, 0, -1)  # Gamma'_3(T_12)
    t_role_x = sp.Matrix(
        [[0, -1, 0], [sp.Rational(-1, 2), 0, sp.Rational(1, 2)], [0, 1, 0]]
    )  # Gamma'_3(T_23)
    t_role_y = sp.Matrix(
        [
            [0, -IMAG, 0],
            [IMAG * sp.Rational(1, 2), 0, IMAG * sp.Rational(1, 2)],
            [0, -IMAG, 0],
        ]
    )  # Gamma'_3(T_31), HELD OUT of the solve, used only as independent check

    u = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"u{i}{j}"))

    eqs = list(t_role_z * u - u * lz) + list(t_role_x * u - u * lx)
    sol = sp.solve(eqs, list(u), dict=True)

    if not sol:
        return {"solved": False, "reason": "no solution to T_role_z,T_role_x equations"}

    sol0 = sol[0]
    u_sol = u.subs(sol0)
    free_symbols = sorted({s for s in u_sol.free_symbols}, key=str)

    # Fix free parameters to nonzero generic values to get one concrete U.
    fix = {s: sp.Integer(1) for s in free_symbols}
    u_concrete = sp.simplify(u_sol.subs(fix))
    det_u = sp.simplify(u_concrete.det())

    holdout_lhs = sp.simplify(t_role_y * u_concrete)
    holdout_rhs_direct = sp.simplify(u_concrete * ly)
    holdout_direct_ok = zero_check(holdout_lhs - holdout_rhs_direct)

    u_inv = u_concrete.inv()
    similarity_direct = sp.simplify(u_inv * t_role_y * u_concrete)

    def classify(candidate: sp.Matrix, reference: sp.Matrix) -> str:
        if zero_check(candidate - reference):
            return "EQUAL"
        if zero_check(candidate - reference.T):
            return "TRANSPOSE"
        if zero_check(candidate + reference):
            return "NEGATIVE"
        if zero_check(candidate + reference.T):
            return "NEGATIVE_TRANSPOSE"
        return "NO_SIMPLE_RELATION"

    holdout_classification = classify(similarity_direct, ly)

    return {
        "solved": True,
        "free_symbols": [str(s) for s in free_symbols],
        "n_free_params": len(free_symbols),
        "u_concrete": str(u_concrete),
        "det_u_nonzero": det_u != 0,
        "det_u": str(det_u),
        "holdout_direct_ok": holdout_direct_ok,
        "similarity_direct_minus_ly": str(sp.simplify(similarity_direct - ly)),
        "holdout_classification": holdout_classification,
        "our_lx": str(lx),
        "our_ly": str(ly),
        "our_lz": str(lz),
    }


def part2_scan_alternate_role_maps(intertwiner_result: dict) -> dict:
    r"""If Part 1's straight T_31<->L_y holdout is not EQUAL, scan whether a
    DIFFERENT role assignment (e.g. T_31<->L_y with L_y replaced by -L_y, or
    T_23/T_31 swapped) resolves it with the SAME U -- distinguishing "real
    convention mismatch, name it" from "wrong role map on my part"."""
    if intertwiner_result["holdout_classification"] == "EQUAL":
        return {"needed": False}

    lp = SQRT2 * sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    lm = SQRT2 * sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    ly = sp.simplify((lp - lm) / (2 * IMAG))

    u_concrete = sp.sympify(intertwiner_result["u_concrete"])
    u_inv = u_concrete.inv()
    t_role_y = sp.Matrix(
        [
            [0, -IMAG, 0],
            [IMAG * sp.Rational(1, 2), 0, IMAG * sp.Rational(1, 2)],
            [0, -IMAG, 0],
        ]
    )
    similarity_direct = sp.simplify(u_inv * t_role_y * u_concrete)

    against_minus_ly = zero_check(similarity_direct + ly)
    against_ly_transpose = zero_check(similarity_direct - ly.T)
    against_minus_ly_transpose = zero_check(similarity_direct + ly.T)

    return {
        "needed": True,
        "against_minus_ly": against_minus_ly,
        "against_ly_transpose": against_ly_transpose,
        "against_minus_ly_transpose": against_minus_ly_transpose,
        "similarity_direct": str(similarity_direct),
        "ly": str(ly),
    }


def part3_corrected_role_map(intertwiner_result: dict) -> dict:
    r"""Part 2 found similarity(T_31) == -L_y == L_y^T exactly (both agree
    because L_y, like all so(3) generators built here, is antisymmetric:
    L_y^T = -L_y is automatic, not two separate coincidences). This tests
    whether the SAME U, under the corrected role map T_31 <-> -L_y (a benign
    index-ordering/orientation convention on the antisymmetric pair (3,1) vs
    (1,3), not a physics error), makes ALL THREE generators match exactly
    with no holdout exception -- the genuine completion of the comparison
    Tom originally asked for."""
    lp = SQRT2 * sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    lm = SQRT2 * sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    lz = sp.diag(1, 0, -1)
    lx = sp.simplify((lp + lm) / 2)
    ly = sp.simplify((lp - lm) / (2 * IMAG))

    t_role_z = sp.diag(1, 0, -1)
    t_role_x = sp.Matrix([[0, -1, 0], [sp.Rational(-1, 2), 0, sp.Rational(1, 2)], [0, 1, 0]])
    t_role_y = sp.Matrix(
        [
            [0, -IMAG, 0],
            [IMAG * sp.Rational(1, 2), 0, IMAG * sp.Rational(1, 2)],
            [0, -IMAG, 0],
        ]
    )

    u_concrete = sp.sympify(intertwiner_result["u_concrete"])
    u_inv = u_concrete.inv()

    checks = {
        "T12_vs_Lz": zero_check(u_inv * t_role_z * u_concrete - lz),
        "T23_vs_Lx": zero_check(u_inv * t_role_x * u_concrete - lx),
        "T31_vs_minus_Ly": zero_check(u_inv * t_role_y * u_concrete - (-ly)),
    }
    return {
        "role_map": "T_12<->L_z, T_23<->L_x, T_31<->-L_y",
        "checks": checks,
        "all_pass": all(checks.values()),
    }


def main() -> None:
    results: dict = {}
    results["part0_transcription_check"] = part0_transcription_check()
    results["part1_intertwiner_search"] = part1_intertwiner_search()
    results["part2_scan_alternate_role_maps"] = part2_scan_alternate_role_maps(
        results["part1_intertwiner_search"]
    )
    results["part3_corrected_role_map"] = part3_corrected_role_map(
        results["part1_intertwiner_search"]
    )

    out_path = Path(__file__).parent / "results_c202.json"
    out_path.write_text(json.dumps(results, indent=2, default=str))

    print("=== Part 0: transcription self-check ===")
    p0 = results["part0_transcription_check"]
    print(f"  eq(123) reconstructed == transcribed: {p0['match_t12']}")
    print(f"  eq(124) reconstructed == transcribed: {p0['match_t23']}")
    print(f"  eq(125) reconstructed == transcribed: {p0['match_t31']}")
    print(f"  ALL MATCH: {p0['all_match']}")

    print("\n=== Part 1: intertwiner search (T_12<->Lz, T_23<->Lx solved; T_31<->Ly held out) ===")
    p1 = results["part1_intertwiner_search"]
    if p1["solved"]:
        print(f"  U = {p1['u_concrete']}")
        print(f"  det(U) nonzero: {p1['det_u_nonzero']}  (det = {p1['det_u']})")
        print(f"  Holdout (T_31 <-> L_y) classification: {p1['holdout_classification']}")
    else:
        print(f"  NOT SOLVED: {p1['reason']}")

    print("\n=== Part 2: alternate role-map scan (only if Part 1 holdout failed) ===")
    p2 = results["part2_scan_alternate_role_maps"]
    if p2["needed"]:
        print(f"  similarity(T_31) == -L_y      : {p2['against_minus_ly']}")
        print(f"  similarity(T_31) == L_y^T     : {p2['against_ly_transpose']}")
        print(f"  similarity(T_31) == -(L_y^T)  : {p2['against_minus_ly_transpose']}")
    else:
        print("  not needed (Part 1 holdout already EQUAL)")

    print("\n=== Part 3: corrected role map (T_31 <-> -L_y), all three checked ===")
    p3 = results["part3_corrected_role_map"]
    for name, ok in p3["checks"].items():
        print(f"  {name}: {ok}")
    print(f"  ALL PASS: {p3['all_pass']}")


if __name__ == "__main__":
    main()
