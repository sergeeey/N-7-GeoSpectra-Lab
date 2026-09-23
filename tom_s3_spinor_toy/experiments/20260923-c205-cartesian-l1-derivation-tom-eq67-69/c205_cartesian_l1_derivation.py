r"""C205: the calculation Tom actually asked for -- NOT a check of anything
he sent, but a fresh derivation he had not attempted himself. Apply his own
eq(67)-(69) differential operators DIRECTLY to Cartesian coordinates
(x1/r, x2/r, x3/r), by hand differentiation (sympy, exact), and read off the
resulting 3x3 matrices -- full symbolic workings shown at every step, not
just the final matrices.

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


def build_matrix(operator) -> tuple[sp.Matrix, list[list[sp.Expr]]]:
    """Column j = operator applied to BASIS[j], decomposed in BASIS.
    Returns both the assembled matrix and the raw per-step results (for
    printing full workings, not just the final matrix)."""
    raw_results = []
    columns = []
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
        columns.append(coeffs)
    matrix = sp.Matrix(columns).T
    return matrix, raw_results


def main() -> None:
    results: dict = {}

    print("=== Step 1: apply L_z, L_y, L_x directly to x1/r, x2/r, x3/r ===\n")

    m_lz, raw_lz = build_matrix(l_z)
    m_ly, raw_ly = build_matrix(l_y)
    m_lx, raw_lx = build_matrix(l_x)

    for name, raw in [("L_z", raw_lz), ("L_y", raw_ly), ("L_x", raw_lx)]:
        print(f"--- {name} ---")
        for step in raw:
            print(
                f"  {name}({step['input']}) = {step['operator_output']}  ->  coeffs (phi1,phi2,phi3) = {step['coeffs']}"
            )
        print()

    print("Resulting matrices (columns = operator applied to phi1,phi2,phi3):")
    print(f"  M_Lz =\n{m_lz}")
    print(f"  M_Ly =\n{m_ly}")
    print(f"  M_Lx =\n{m_lx}\n")

    results["step1_matrices"] = {
        "M_Lz": str(m_lz),
        "M_Ly": str(m_ly),
        "M_Lx": str(m_lx),
        "raw_workings": {"L_z": raw_lz, "L_y": raw_ly, "L_x": raw_lx},
    }

    print(
        "=== Step 2a: compare DIRECTLY against Tom's own eq(103)-(105) [T_ij, defining rep] ===\n"
    )

    # Tom's eq (103)-(105): T_ij, the "defining representation" (real basis).
    t23 = sp.Matrix([[0, 0, 0], [0, 0, -IMAG], [0, IMAG, 0]])
    t31 = sp.Matrix([[0, 0, IMAG], [0, 0, 0], [-IMAG, 0, 0]])
    t12 = sp.Matrix([[0, -IMAG, 0], [IMAG, 0, 0], [0, 0, 0]])

    match_lz_raw = sp.simplify(m_lz - t12) == sp.zeros(3, 3)
    match_ly_raw = sp.simplify(m_ly - t31) == sp.zeros(3, 3)
    match_lx_raw = sp.simplify(m_lx - t23) == sp.zeros(3, 3)

    print(f"  M_Lz == T_12 [eq 105], DIRECTLY, no extra sign? {match_lz_raw}")
    print(f"  M_Ly == T_31 [eq 104], DIRECTLY, no extra sign? {match_ly_raw}")
    print(f"  M_Lx == T_23 [eq 103], DIRECTLY, no extra sign? {match_lx_raw}")
    print(
        "  (i.e.: applying eq(67)-(69) straight to the Cartesian basis functions\n"
        "   reproduces eq(103)-(105) exactly -- the 'defining representation' T_ij,\n"
        "   BEFORE the separate eq(99) sign flip Gamma_3(T)=-T is applied.)\n"
    )

    print(
        "=== Step 2b: apply Tom's own eq(99) [Gamma_3(T_ij) = -T_ij] to reach eq(106)-(108) ===\n"
    )

    gamma3_t23 = -t23  # role: L_x (eq 69: omega^23 <-> L_x)
    gamma3_t31 = -t31  # role: L_y (eq 68: omega^31 <-> L_y)
    gamma3_t12 = -t12  # role: L_z (eq 67: omega^12 <-> L_z)

    match_lz = sp.simplify((-m_lz) - gamma3_t12) == sp.zeros(3, 3)
    match_ly = sp.simplify((-m_ly) - gamma3_t31) == sp.zeros(3, 3)
    match_lx = sp.simplify((-m_lx) - gamma3_t23) == sp.zeros(3, 3)

    print(f"  -M_Lz == Gamma_3(T_12) [eq 108]? {match_lz}")
    print(f"  -M_Ly == Gamma_3(T_31) [eq 107]? {match_ly}")
    print(f"  -M_Lx == Gamma_3(T_23) [eq 106]? {match_lx}\n")

    results["step2_match_real_basis"] = {
        "direct_match_vs_Tij_eq103_105": {
            "M_Lz_vs_T12": match_lz_raw,
            "M_Ly_vs_T31": match_ly_raw,
            "M_Lx_vs_T23": match_lx_raw,
        },
        "M_Lz_vs_Gamma3_T12": match_lz,
        "M_Ly_vs_Gamma3_T31": match_ly,
        "M_Lx_vs_Gamma3_T23": match_lx,
        "all_match": match_lz and match_ly and match_lx,
    }

    print(
        "=== Step 3: apply Tom's own z (eq 118) to (-M_L), the Gamma_3-stage result, to reach (123)-(125) ===\n"
    )

    z = sp.Matrix([[1, IMAG, 0], [0, 0, 1], [1, -IMAG, 0]])
    z_inv = z.inv()

    gp_t12 = sp.simplify(z * (-m_lz) * z_inv)
    gp_t31 = sp.simplify(z * (-m_ly) * z_inv)
    gp_t23 = sp.simplify(z * (-m_lx) * z_inv)

    print(f"  z * (-M_Lz) * z^-1 =\n{gp_t12}   (compare to Tom's eq 123: diag(1,0,-1))")
    print(f"  z * (-M_Ly) * z^-1 =\n{gp_t31}   (compare to Tom's eq 125)")
    print(f"  z * (-M_Lx) * z^-1 =\n{gp_t23}   (compare to Tom's eq 124)\n")

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
        results["step2_match_real_basis"]["all_match"]
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
