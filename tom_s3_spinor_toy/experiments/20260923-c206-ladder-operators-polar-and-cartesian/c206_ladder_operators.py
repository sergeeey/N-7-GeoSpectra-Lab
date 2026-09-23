r"""C206: what Tom actually asked for, precisely, per his latest correction.

C205 applied L_x, L_y, L_z (rotation operators, his eq 67-69) to x/r,y/r,z/r.
Tom clarified: those are NOT the ladder operators. The ladder operators are
L_+ = L_x + i*L_y, L_- = L_x - i*L_y (McMurry p.144 gives these in POLAR
coordinates). He asked for two things:

Part A: full working for McMurry 6.3(a) -- L_+/L_- in POLAR form, applied to
the l=1 spherical harmonics -- not just the sqrt(2) summary result already
reported (C201 computed this but only the headline number was shared).

Part B: L_+ and L_- in CARTESIAN form (built from his own eq 68-69 L_x, L_y),
applied to the CARTESIAN basis functions x/r, y/r, z/r -- a genuinely new
calculation not done in C201 (polar) or C205 (rotation operators only, not
the ladder combinations).

Everything here is symbolic (sympy), exact, with every intermediate step
captured for the write-up, not just final answers.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

IMAG = sp.I

# =====================================================================
# Part A: McMurry 6.3(a), ladder operators in POLAR form, l=1 harmonics.
# =====================================================================

theta, phi = sp.symbols("theta phi", real=True)


def l_plus_polar(f: sp.Expr) -> sp.Expr:
    r"""McMurry p.144: L_+ = e^{i phi} (d/d theta + i cot(theta) d/d phi)."""
    return sp.exp(IMAG * phi) * (sp.diff(f, theta) + IMAG * sp.cot(theta) * sp.diff(f, phi))


def l_minus_polar(f: sp.Expr) -> sp.Expr:
    r"""McMurry p.144: L_- = e^{-i phi} (-d/d theta + i cot(theta) d/d phi)."""
    return sp.exp(-IMAG * phi) * (-sp.diff(f, theta) + IMAG * sp.cot(theta) * sp.diff(f, phi))


def part_a_mcmurry_polar() -> dict:
    c = sp.sqrt(sp.Rational(3, 1) / (4 * sp.pi))  # McMurry's own normalization constant
    y10 = c * sp.cos(theta)
    y11 = -c / sp.sqrt(2) * sp.sin(theta) * sp.exp(IMAG * phi)
    y1m1 = c / sp.sqrt(2) * sp.sin(theta) * sp.exp(-IMAG * phi)

    steps = []

    def check(label, operator, f, target, target_label):
        raw = operator(f)
        raw_simplified = sp.trigsimp(sp.expand_complex(raw))
        residual = sp.simplify(raw_simplified - target)
        residual2 = sp.simplify(raw_simplified + target)  # in case of an overall sign
        steps.append(
            {
                "action": label,
                "raw_result": str(raw),
                "simplified": str(raw_simplified),
                "compared_to": f"{target_label} = {target}",
                "matches_plus_sqrt2": residual == 0,
                "matches_minus_sqrt2": residual2 == 0,
            }
        )
        return raw_simplified

    sqrt2 = sp.sqrt(2)
    check("L_+ y_{1,0}", l_plus_polar, y10, sqrt2 * y11, "sqrt(2) * y_{1,1}")
    check("L_+ y_{1,-1}", l_plus_polar, y1m1, sqrt2 * y10, "sqrt(2) * y_{1,0}")
    check("L_+ y_{1,1}", l_plus_polar, y11, sp.Integer(0), "0 (already top of ladder)")
    check("L_- y_{1,0}", l_minus_polar, y10, sqrt2 * y1m1, "sqrt(2) * y_{1,-1}")
    check("L_- y_{1,1}", l_minus_polar, y11, sqrt2 * y10, "sqrt(2) * y_{1,0}")
    check("L_- y_{1,-1}", l_minus_polar, y1m1, sp.Integer(0), "0 (already bottom of ladder)")

    all_pass = all(s["matches_plus_sqrt2"] or s["matches_minus_sqrt2"] for s in steps)
    return {
        "y10": str(y10),
        "y11": str(y11),
        "y1m1": str(y1m1),
        "c": str(c),
        "steps": steps,
        "all_pass": all_pass,
    }


# =====================================================================
# Part B: L_+, L_- in CARTESIAN form, applied to CARTESIAN basis x/r,y/r,z/r.
# =====================================================================

x, y, z = sp.symbols("x y z", real=True)
r = sp.sqrt(x**2 + y**2 + z**2)
phi1, phi2, phi3 = x / r, y / r, z / r
CART_BASIS = {"x/r": phi1, "y/r": phi2, "z/r": phi3}


def l_x_cart(f: sp.Expr) -> sp.Expr:
    r"""Tom's eq(69): L_x = i(z d/dy - y d/dz)."""
    return IMAG * (z * sp.diff(f, y) - y * sp.diff(f, z))


def l_y_cart(f: sp.Expr) -> sp.Expr:
    r"""Tom's eq(68): L_y = i(x d/dz - z d/dx)."""
    return IMAG * (x * sp.diff(f, z) - z * sp.diff(f, x))


def l_plus_cart(f: sp.Expr) -> sp.Expr:
    r"""L_+ = L_x + i*L_y, built from Tom's own Cartesian L_x, L_y."""
    return l_x_cart(f) + IMAG * l_y_cart(f)


def l_minus_cart(f: sp.Expr) -> sp.Expr:
    r"""L_- = L_x - i*L_y, built from Tom's own Cartesian L_x, L_y."""
    return l_x_cart(f) - IMAG * l_y_cart(f)


def part_b_cartesian_ladder() -> dict:
    steps = []
    results = {}
    for op_name, op in [("L_+", l_plus_cart), ("L_-", l_minus_cart)]:
        for basis_name, basis_fn in CART_BASIS.items():
            raw = op(basis_fn)
            simplified = sp.simplify(raw)
            steps.append(
                {
                    "operator": op_name,
                    "input": basis_name,
                    "result": str(simplified),
                }
            )
            results[f"{op_name}({basis_name})"] = str(simplified)

    # Cross-check against the ladder structure via the complex combinations
    # (x+iy)/r [top of the l=1 ladder, "m=+1"-like] and (x-iy)/r ["m=-1"-like],
    # matching Tom's own eq(115)-(116) complex-combination pattern.
    plus_combo = sp.simplify(phi1 + IMAG * phi2)  # (x+iy)/r
    minus_combo = sp.simplify(phi1 - IMAG * phi2)  # (x-iy)/r

    l_plus_on_plus_combo = sp.simplify(l_plus_cart(plus_combo))
    l_plus_on_minus_combo = sp.simplify(l_plus_cart(minus_combo))
    l_minus_on_plus_combo = sp.simplify(l_minus_cart(plus_combo))
    l_minus_on_minus_combo = sp.simplify(l_minus_cart(minus_combo))

    ladder_check = {
        "L_plus_on_(x+iy)/r_should_be_zero_top_of_ladder": str(l_plus_on_plus_combo),
        "L_plus_on_(x-iy)/r_should_raise_to_something_prop_z/r": str(l_plus_on_minus_combo),
        "L_minus_on_(x+iy)/r_should_lower_to_something_prop_z/r": str(l_minus_on_plus_combo),
        "L_minus_on_(x-iy)/r_should_be_zero_bottom_of_ladder": str(l_minus_on_minus_combo),
        "L_plus_on_plus_combo_is_zero": l_plus_on_plus_combo == 0,
        "L_minus_on_minus_combo_is_zero": l_minus_on_minus_combo == 0,
    }

    return {
        "per_basis_steps": steps,
        "raw_results": results,
        "ladder_structure_check": ladder_check,
    }


# =====================================================================
# Part C: reconcile Part A (polar) with Part B (Cartesian) directly --
# apply the CARTESIAN L_+/L_- to the SAME normalized Y_{1,m} states used in
# Part A (just rewritten in x,y,z instead of theta,phi via x=r sin(theta)
# cos(phi) etc., i.e. sin(theta)*exp(I*phi) -> (x+iy)/r), and confirm the
# exact sqrt(2) ladder coefficients reappear -- not just up to a constant.
# =====================================================================


def part_c_reconcile_polar_and_cartesian() -> dict:
    c = sp.sqrt(sp.Rational(3, 1) / (4 * sp.pi))
    y10_cart = c * (z / r)
    y11_cart = -(c / sp.sqrt(2)) * ((x + IMAG * y) / r)
    y1m1_cart = (c / sp.sqrt(2)) * ((x - IMAG * y) / r)

    sqrt2 = sp.sqrt(2)
    checks = []

    def check(label, lhs, rhs, rhs_label):
        residual = sp.simplify(lhs - rhs)
        checks.append(
            {
                "action": label,
                "lhs": str(sp.simplify(lhs)),
                "compared_to": f"{rhs_label} = {sp.simplify(rhs)}",
                "residual": str(residual),
                "matches": residual == 0,
            }
        )

    check(
        "L_+ Y_{1,-1} (Cartesian-built)",
        l_plus_cart(y1m1_cart),
        sqrt2 * y10_cart,
        "sqrt(2)*Y_{1,0}",
    )
    check(
        "L_+ Y_{1,0} (Cartesian-built)", l_plus_cart(y10_cart), sqrt2 * y11_cart, "sqrt(2)*Y_{1,1}"
    )
    check("L_+ Y_{1,1} (Cartesian-built)", l_plus_cart(y11_cart), sp.Integer(0), "0")
    check(
        "L_- Y_{1,0} (Cartesian-built)",
        l_minus_cart(y10_cart),
        sqrt2 * y1m1_cart,
        "sqrt(2)*Y_{1,-1}",
    )
    check(
        "L_- Y_{1,1} (Cartesian-built)", l_minus_cart(y11_cart), sqrt2 * y10_cart, "sqrt(2)*Y_{1,0}"
    )
    check("L_- Y_{1,-1} (Cartesian-built)", l_minus_cart(y1m1_cart), sp.Integer(0), "0")

    all_pass = all(chk["matches"] for chk in checks)
    return {
        "y10_cart": str(y10_cart),
        "y11_cart": str(y11_cart),
        "y1m1_cart": str(y1m1_cart),
        "checks": checks,
        "all_pass": all_pass,
    }


def main() -> None:
    results: dict = {}

    print("=" * 70)
    print("PART A: McMurry 6.3(a) -- ladder operators in POLAR form, l=1")
    print("=" * 70)
    part_a = part_a_mcmurry_polar()
    results["part_a_mcmurry_polar"] = part_a
    print(f"y_1,0  = {part_a['y10']}")
    print(f"y_1,1  = {part_a['y11']}")
    print(f"y_1,-1 = {part_a['y1m1']}\n")
    for s in part_a["steps"]:
        print(f"  {s['action']}:")
        print(f"    raw        = {s['raw_result']}")
        print(f"    simplified = {s['simplified']}")
        print(f"    compare to = {s['compared_to']}")
        print(
            f"    match (+sqrt2): {s['matches_plus_sqrt2']}   match (-sqrt2): {s['matches_minus_sqrt2']}\n"
        )
    print(f"PART A ALL PASS: {part_a['all_pass']}\n")

    print("=" * 70)
    print("PART B: L_+, L_- in CARTESIAN form, applied to x/r, y/r, z/r")
    print("=" * 70)
    part_b = part_b_cartesian_ladder()
    results["part_b_cartesian_ladder"] = part_b
    for s in part_b["per_basis_steps"]:
        print(f"  {s['operator']}({s['input']}) = {s['result']}")
    print("\nLadder-structure cross-check (via (x+iy)/r and (x-iy)/r):")
    for k, v in part_b["ladder_structure_check"].items():
        print(f"  {k}: {v}")

    print("\n" + "=" * 70)
    print("PART C: reconcile Part A (polar) and Part B (Cartesian) directly --")
    print("apply the CARTESIAN L_+/L_- to the SAME normalized Y_{1,m} states")
    print("=" * 70)
    part_c = part_c_reconcile_polar_and_cartesian()
    results["part_c_reconcile"] = part_c
    print(f"Y_1,0  (Cartesian form) = {part_c['y10_cart']}")
    print(f"Y_1,1  (Cartesian form) = {part_c['y11_cart']}")
    print(f"Y_1,-1 (Cartesian form) = {part_c['y1m1_cart']}\n")
    for chk in part_c["checks"]:
        print(f"  {chk['action']}:")
        print(f"    result     = {chk['lhs']}")
        print(f"    compare to = {chk['compared_to']}")
        print(f"    residual   = {chk['residual']}   matches: {chk['matches']}\n")
    print(f"PART C ALL PASS: {part_c['all_pass']}\n")

    out_path = Path(__file__).parent / "results_c206.json"
    out_path.write_text(json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    main()
