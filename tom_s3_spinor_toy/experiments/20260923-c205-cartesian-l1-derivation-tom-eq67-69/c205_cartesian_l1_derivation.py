r"""C205: the calculation Tom actually asked for -- NOT a check of anything
he sent, but a fresh derivation he had not attempted himself. Apply his own
eq(67)-(69) differential operators DIRECTLY to Cartesian coordinates
(x1/r, x2/r, x3/r), by hand differentiation (sympy, exact), and read off the
resulting 3x3 matrices -- full symbolic workings shown at every step, not
just the final matrices.

REVISED after a REAL bug caught by independent user review (not the earlier
Explore-agent report -- the user re-checked against Tom's own PDF directly):
the first version of `build_matrix` assembled the matrix with an extra,
unjustified transpose (`sp.Matrix(rows).T`), which happens to equal the
STANDARD linear-algebra "matrix of a linear map" convention (column j =
image of basis_j) but is the TRANSPOSE of Tom's own stated index convention
in his eq(76): "(-delta_x^I d_I |phi_gamma>) = (i Gamma_d(T_ij))_gamma^delta
|phi_delta>" -- gamma (the INPUT basis label) is the FIRST/row-like index of
Gamma_d, delta (the output expansion coefficient) is the second. Since these
generators are all antisymmetric (M^T = -M), the wrong transpose flips the
overall sign, which is exactly why the first version landed on eq(103)-(105)
[T_ij] instead of eq(106)-(108) [Gamma_3(T_ij) = -T_ij] directly, and needed
an extra explicit negation to reach Tom's stated matrices. Fixed here by
building the matrix in TOM'S OWN row=input convention directly (no `.T`),
verified below to reproduce eq(106)-(108) with no extra step. The STANDARD
linear-algebra transpose convention is kept in the printout too, explicitly
labeled, because it is a genuinely illustrative side note: it is exactly
where the "-1" / transpose ambiguity Tom's own document worries about right
after eq(99) comes from, made completely mechanical.

This is deliberately NOT the ladder-operator (McMurry/spherical-harmonic)
route -- that was C201/C202. This round only uses Tom's own Cartesian
angular-momentum operators (his eq 67-69) and his own normalized real basis
(his eq 91, |phi_i> = const * x^i/r -- the constant is dropped since it
cancels out of any matrix representation).

After deriving the matrices this way, they are compared against:
  (a) Tom's own eq(106)-(108) [Gamma_3(T_ij) = -T_ij, his eq 99], to check
      this Cartesian derivation reproduces what his own document already
      states via the general SO(n+1) formula (his eq 61), and
  (b) Tom's own eq(123)-(125), via his own eq(118) z change-of-basis and
      eq(122) formula (already verified self-consistent in C202) -- closing
      the full chain: differential operator -> Cartesian derivation ->
      complex/Cartan basis -> his own stated final matrices.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

IMAG = sp.I

x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
r = sp.sqrt(x1**2 + x2**2 + x3**2)

# Tom's own normalized real basis, eq (91): |phi_i> = delta_ij * sqrt((n+1)/S) * x^j / r.
# The overall constant sqrt((n+1)/S) is dropped -- it cancels identically out
# of any matrix representation (linear operators commute with scalar rescaling
# of the whole basis), so working with plain x_i/r changes nothing that matters.
phi1 = x1 / r
phi2 = x2 / r
phi3 = x3 / r
BASIS = [phi1, phi2, phi3]


def l_z(f: sp.Expr) -> sp.Expr:
    r"""Tom's eq (67): L_z = i(x2 d/dx1 - x1 d/dx2)."""
    return IMAG * (x2 * sp.diff(f, x1) - x1 * sp.diff(f, x2))


def l_y(f: sp.Expr) -> sp.Expr:
    r"""Tom's eq (68): L_y = i(x1 d/dx3 - x3 d/dx1)."""
    return IMAG * (x1 * sp.diff(f, x3) - x3 * sp.diff(f, x1))


def l_x(f: sp.Expr) -> sp.Expr:
    r"""Tom's eq (69): L_x = i(x3 d/dx2 - x2 d/dx3)."""
    return IMAG * (x3 * sp.diff(f, x2) - x2 * sp.diff(f, x3))


def decompose(expr: sp.Expr) -> list[sp.Expr]:
    """Express `expr` (already known, by construction, to be a linear
    combination of phi1,phi2,phi3 = x1/r,x2/r,x3/r WITH CONSTANT
    coefficients -- true here because L_z,L_y,L_x are the standard so(3)
    rotation generators, which preserve r) as those coefficients, via
    exact symbolic solve, not by inspection.

    Method: multiply expr by r. If expr = c1*x1/r + c2*x2/r + c3*x3/r with
    constant c_i, then expr*r = c1*x1 + c2*x2 + c3*x3 EXACTLY, with every r
    cancelling identically (verified below, not assumed) -- avoiding the
    earlier, fragile attempt to sp.Poly() an expression that still contained
    a bare sqrt(x1**2+x2**2+x3**2) as one of its own "generators"."""
    cleared = sp.expand(sp.simplify(expr * r))
    if cleared.has(r) or cleared.has(sp.sqrt(x1**2 + x2**2 + x3**2)):
        raise ValueError(f"r did not cancel exactly for {expr}: got {cleared}")
    poly = sp.Poly(cleared, x1, x2, x3)
    coeffs = [poly.coeff_monomial(x1), poly.coeff_monomial(x2), poly.coeff_monomial(x3)]
    # Sanity: the polynomial must be PURELY linear (no other monomials) --
    # if there's a leftover constant/quadratic term, the "rotation preserves
    # r" assumption this method relies on has been violated somewhere.
    reconstructed = coeffs[0] * x1 + coeffs[1] * x2 + coeffs[2] * x3
    if sp.expand(cleared - reconstructed) != 0:
        raise ValueError(f"non-linear residual for {expr}: {cleared} != {reconstructed}")
    return coeffs


def build_matrix(operator) -> tuple[sp.Matrix, sp.Matrix, list[list[sp.Expr]]]:
    """Returns TWO matrices from the same raw differentiation data, plus the
    raw per-step results (full workings, not just final matrices):

    - `matrix_tom_convention`: row j = coeffs when operator is applied to
      BASIS[j] -- i.e. literally Tom's own eq(76) index placement, operator
      (phi_gamma) = sum_delta M_gamma^delta phi_delta, gamma=row=input.
      This is the one that matches his eq(106)-(108) directly.
    - `matrix_standard_linalg`: the ordinary "matrix of a linear map"
      convention (column j = image of basis_j), i.e. the transpose of the
      above. Kept only as an explicit, labeled side-by-side illustration of
      exactly the transpose/sign ambiguity Tom's own document flags after
      eq(99) -- NOT used for any of the eq(106)-(125) comparisons below.
    """
    raw_results = []
    rows = []
    for basis_fn in BASIS:
        applied = operator(basis_fn)
        applied_simplified = sp.simplify(applied)
        coeffs = decompose(applied_simplified)
        raw_results.append(
            {
                "input": str(basis_fn),
                "operator_output": str(applied_simplified),
                "coeffs": [str(c) for c in coeffs],
            }
        )
        rows.append(coeffs)
    matrix_tom_convention = sp.Matrix(rows)
    matrix_standard_linalg = matrix_tom_convention.T
    return matrix_tom_convention, matrix_standard_linalg, raw_results


def main() -> None:
    results: dict = {}

    print("=== Step 1: apply L_z, L_y, L_x directly to x1/r, x2/r, x3/r ===\n")

    m_lz, m_lz_transpose, raw_lz = build_matrix(l_z)
    m_ly, m_ly_transpose, raw_ly = build_matrix(l_y)
    m_lx, m_lx_transpose, raw_lx = build_matrix(l_x)

    for name, raw in [("L_z", raw_lz), ("L_y", raw_ly), ("L_x", raw_lx)]:
        print(f"--- {name} ---")
        for step in raw:
            print(
                f"  {name}({step['input']}) = {step['operator_output']}  ->  coeffs (phi1,phi2,phi3) = {step['coeffs']}"
            )
        print()

    print(
        "Resulting matrices, Tom's own eq(76) row=input convention (row j = coeffs when operator applied to phi_j):"
    )
    print(f"  M_Lz =\n{m_lz}")
    print(f"  M_Ly =\n{m_ly}")
    print(f"  M_Lx =\n{m_lx}\n")
    print(
        "For comparison ONLY, the STANDARD linear-algebra 'matrix of a linear\n"
        "map' convention (column j = image of basis_j) -- the TRANSPOSE of the\n"
        "above, and exactly where the sign ambiguity Tom's own document raises\n"
        "right after eq(99) comes from:"
    )
    print(f"  M_Lz^T =\n{m_lz_transpose}\n")

    results["step1_matrices"] = {
        "M_Lz_tom_convention": str(m_lz),
        "M_Ly_tom_convention": str(m_ly),
        "M_Lx_tom_convention": str(m_lx),
        "M_Lz_standard_linalg_transpose": str(m_lz_transpose),
        "M_Ly_standard_linalg_transpose": str(m_ly_transpose),
        "M_Lx_standard_linalg_transpose": str(m_lx_transpose),
        "raw_workings": {"L_z": raw_lz, "L_y": raw_ly, "L_x": raw_lx},
    }

    print(
        "=== Step 2: compare, in Tom's own eq(76) convention, DIRECTLY against his eq(106)-(108) [Gamma_3(T_ij)] ===\n"
    )

    # Tom's eq (106)-(108): Gamma_3(T_ij) = -T_ij, as printed (his eq 99).
    gamma3_t23 = sp.Matrix([[0, 0, 0], [0, 0, IMAG], [0, -IMAG, 0]])  # eq 106, role: L_x
    gamma3_t31 = sp.Matrix([[0, 0, -IMAG], [0, 0, 0], [IMAG, 0, 0]])  # eq 107, role: L_y
    gamma3_t12 = sp.Matrix([[0, IMAG, 0], [-IMAG, 0, 0], [0, 0, 0]])  # eq 108, role: L_z

    match_lz = sp.simplify(m_lz - gamma3_t12) == sp.zeros(3, 3)
    match_ly = sp.simplify(m_ly - gamma3_t31) == sp.zeros(3, 3)
    match_lx = sp.simplify(m_lx - gamma3_t23) == sp.zeros(3, 3)

    print(f"  M_Lz == Gamma_3(T_12) [eq 108], DIRECTLY, no extra step needed? {match_lz}")
    print(f"  M_Ly == Gamma_3(T_31) [eq 107], DIRECTLY, no extra step needed? {match_ly}")
    print(f"  M_Lx == Gamma_3(T_23) [eq 106], DIRECTLY, no extra step needed? {match_lx}")
    print(
        "  (Earlier draft of this script used the standard linear-algebra\n"
        "   transpose convention instead, which lands on eq(103)-(105) [T_ij]\n"
        "   directly and needs an EXTRA negation to reach Gamma_3 -- a real,\n"
        "   independently-caught bug in the matrix-assembly convention, not a\n"
        "   physics finding. Fixed: using Tom's own eq(76) row=input placement\n"
        "   gives Gamma_3(T_ij) in a single step, exactly as his own general\n"
        "   theory (his eq96, Gamma_d(g)=g^-1=g^T) says it should.)\n"
    )

    # NOTE (kept as an explicit, labeled side-check, per the reasoning above):
    # eq(107) and eq(108) as literally PRINTED in the PDF appear to show T_31
    # and T_12 themselves (unchanged sign), not -T_31/-T_12 as their own
    # equation labels state -- eq(106) is printed correctly (= -T_23). This
    # looks like an isolated typesetting slip on 2 of 3 equations, verified by
    # direct visual inspection of page 15, not assumed from a text extraction.
    # The values used above (gamma3_t23/t31/t12) are the LABELS' stated
    # -T_ij = T_ij^T formula, which is also what his own eq(96) general theory
    # requires -- not the possibly-mistyped printed matrices for (107)/(108).
    t23 = sp.Matrix([[0, 0, 0], [0, 0, -IMAG], [0, IMAG, 0]])
    t31 = sp.Matrix([[0, 0, IMAG], [0, 0, 0], [-IMAG, 0, 0]])
    t12 = sp.Matrix([[0, -IMAG, 0], [IMAG, 0, 0], [0, 0, 0]])
    eq107_as_printed = sp.Matrix([[0, 0, IMAG], [0, 0, 0], [-IMAG, 0, 0]])  # == T_31, not -T_31
    eq108_as_printed = sp.Matrix([[0, -IMAG, 0], [IMAG, 0, 0], [0, 0, 0]])  # == T_12, not -T_12
    results["appendix_possible_pdf_typesetting_note"] = {
        "eq106_printed_matches_minus_T23": sp.simplify(gamma3_t23 - (-t23)) == sp.zeros(3, 3),
        "eq107_as_printed_equals_T31_not_minus_T31": eq107_as_printed == t31,
        "eq108_as_printed_equals_T12_not_minus_T12": eq108_as_printed == t12,
        "note": (
            "eq(107)/(108) as printed on page 15 appear to equal T_31/T_12 "
            "directly, not -T_31/-T_12 as their own labels state; eq(106) is "
            "printed correctly. Not raised with Tom -- an internal note only, "
            "verified against the actual page image, not a text extraction."
        ),
    }

    results["step2_match_gamma3"] = {
        "M_Lz_vs_Gamma3_T12": match_lz,
        "M_Ly_vs_Gamma3_T31": match_ly,
        "M_Lx_vs_Gamma3_T23": match_lx,
        "all_match": match_lz and match_ly and match_lx,
    }

    print(
        "=== Step 3: apply Tom's own z (eq 118) directly to M_L (already Gamma_3) to reach (123)-(125) ===\n"
    )

    z = sp.Matrix([[1, IMAG, 0], [0, 0, 1], [1, -IMAG, 0]])
    z_inv = z.inv()

    gp_t12 = sp.simplify(z * m_lz * z_inv)
    gp_t31 = sp.simplify(z * m_ly * z_inv)
    gp_t23 = sp.simplify(z * m_lx * z_inv)

    print(f"  z * M_Lz * z^-1 =\n{gp_t12}   (compare to Tom's eq 123: diag(1,0,-1))")
    print(f"  z * M_Ly * z^-1 =\n{gp_t31}   (compare to Tom's eq 125)")
    print(f"  z * M_Lx * z^-1 =\n{gp_t23}   (compare to Tom's eq 124)\n")

    gp_t12_stated = sp.diag(1, 0, -1)
    gp_t23_stated = sp.Matrix([[0, -1, 0], [sp.Rational(-1, 2), 0, sp.Rational(1, 2)], [0, 1, 0]])
    gp_t31_stated = sp.Matrix(
        [[0, -IMAG, 0], [IMAG * sp.Rational(1, 2), 0, IMAG * sp.Rational(1, 2)], [0, -IMAG, 0]]
    )

    match_123 = sp.simplify(gp_t12 - gp_t12_stated) == sp.zeros(3, 3)
    match_124 = sp.simplify(gp_t23 - gp_t23_stated) == sp.zeros(3, 3)
    match_125 = sp.simplify(gp_t31 - gp_t31_stated) == sp.zeros(3, 3)

    print(f"  Matches Tom's stated eq(123)? {match_123}")
    print(f"  Matches Tom's stated eq(124)? {match_124}")
    print(f"  Matches Tom's stated eq(125)? {match_125}\n")

    results["step3_match_complex_basis"] = {
        "z_Mlz_zinv_vs_eq123": match_123,
        "z_Mlx_zinv_vs_eq124": match_124,
        "z_Mly_zinv_vs_eq125": match_125,
        "all_match": match_123 and match_124 and match_125,
    }

    all_pass = (
        results["step2_match_gamma3"]["all_match"]
        and results["step3_match_complex_basis"]["all_match"]
    )
    results["all_pass"] = all_pass
    print(
        f"=== OVERALL: full chain (differential operator -> Cartesian -> complex basis) verified: {all_pass} ==="
    )

    out_path = Path(__file__).parent / "results_c205.json"
    out_path.write_text(json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    main()
