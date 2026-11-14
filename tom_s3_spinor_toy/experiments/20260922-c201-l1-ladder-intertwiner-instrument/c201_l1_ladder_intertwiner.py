"""C201 -- tool-verify McMurry 6.3(a)'s l=1 ladder relations, and pre-validate the
T_i U = U L_i intertwiner test (proposed for Tom Lawrence's (123)-(125) matrices,
once received) on a KNOWN case: does l=1 (spherical harmonics under L+/L-) come
out equivalent to the standard Cartesian vector representation of so(3)?

Also builds a worked "invariant is not automatically irreducible" template: the
commutant of {Lx,Ly,Lz} on the l=1 space must be exactly scalar multiples of the
identity (Schur), computed here rather than assumed.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c201.json"

theta, phi = sp.symbols("theta phi", real=True)
IMAG = sp.I


def l_plus(f):
    return sp.exp(IMAG * phi) * (sp.diff(f, theta) + IMAG * sp.cot(theta) * sp.diff(f, phi))


def l_minus(f):
    return sp.exp(-IMAG * phi) * (-sp.diff(f, theta) + IMAG * sp.cot(theta) * sp.diff(f, phi))


def zero_check(expr) -> bool:
    return sp.simplify(sp.trigsimp(sp.expand_complex(expr))) == 0


def part1_mcmurry_ladder(res: dict) -> None:
    print("=== Part 1: McMurry 6.3(a), l=1 ladder relations (exact symbolic) ===")
    c = sp.sqrt(sp.Rational(3, 1) / (4 * sp.pi))
    # McMurry (4.45), Table B1 (p91): P_1^0 = cos(theta), P_1^1 = sin(theta),
    # P_1^{-1} = (-1)^1 (0!/2!) P_1^1 = -sin(theta)/2 -- used only implicitly via
    # the standard Y_{l,-m} = (-1)^m conj(Y_{l,m}) relation for m<0.
    y10 = c * sp.cos(theta)
    y11 = -c / sp.sqrt(2) * sp.sin(theta) * sp.exp(IMAG * phi)
    y1m1 = c / sp.sqrt(2) * sp.sin(theta) * sp.exp(-IMAG * phi)

    checks = {
        "L+ Y(1,-1) = sqrt(2) Y(1,0)": l_plus(y1m1) - sp.sqrt(2) * y10,
        "L+ Y(1,0)  = sqrt(2) Y(1,1)": l_plus(y10) - sp.sqrt(2) * y11,
        "L+ Y(1,1)  = 0": l_plus(y11),
        "L- Y(1,1)  = sqrt(2) Y(1,0)": l_minus(y11) - sp.sqrt(2) * y10,
        "L- Y(1,0)  = sqrt(2) Y(1,-1)": l_minus(y10) - sp.sqrt(2) * y1m1,
        "L- Y(1,-1) = 0": l_minus(y1m1),
    }
    out = {}
    all_pass = True
    for name, residual in checks.items():
        ok = zero_check(residual)
        all_pass &= ok
        out[name] = ok
        print(f"  {name}: residual==0 -> {ok}")
    res["part1_mcmurry_ladder"] = out
    res["part1_all_pass"] = all_pass
    print(f"  -> all four non-zero relations carry sqrt(2), all six checks pass: {all_pass}\n")


def commutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.simplify(a * b - b * a)


def part2_matrices_and_algebra(res: dict) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    print("=== Part 2: 3x3 matrix form (basis order Y(1,1), Y(1,0), Y(1,-1)) ===")
    lp = sp.sqrt(2) * sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    lm = sp.sqrt(2) * sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    lz = sp.diag(1, 0, -1)
    lx = sp.simplify((lp + lm) / 2)
    ly = sp.simplify((lp - lm) / (2 * IMAG))
    print("  L+ =", lp.tolist())
    print("  L- =", lm.tolist())
    print("  Lz =", lz.tolist())
    print("  Lx =", lx.tolist())
    print("  Ly =", ly.tolist())

    algebra = {
        "[Lx,Ly] == i*Lz": commutator(lx, ly) == IMAG * lz,
        "[Ly,Lz] == i*Lx": commutator(ly, lz) == IMAG * lx,
        "[Lz,Lx] == i*Ly": commutator(lz, lx) == IMAG * ly,
    }
    for name, ok in algebra.items():
        print(f"  {name}: {ok}")
    casimir = sp.simplify(lx * lx + ly * ly + lz * lz)
    casimir_ok = casimir == 2 * sp.eye(3)
    print(f"  Casimir Lx^2+Ly^2+Lz^2 == 2*IMAG (l(l+1)=2 for l=1): {casimir_ok}")
    res["part2_so3_algebra"] = {**algebra, "casimir_is_2I": casimir_ok}
    print()
    return lx, ly, lz


def part3_positive_control_intertwiner(
    res: dict, lx: sp.Matrix, ly: sp.Matrix, lz: sp.Matrix
) -> None:
    print("=== Part 3: KNOWN-CASE positive control -- l=1 spherical vs Cartesian vector rep ===")
    print("  (validates the T_i U = U L_i method BEFORE applying it to Tom's own matrices)")
    # Derive the Cartesian generators the same way as L+/L- above -- by actual
    # differentiation (L_k = -i*epsilon_{kij} x_i d/dx_j), not by typing a
    # remembered matrix.  A first hand-typed version here had a sign error,
    # caught by the very [Lx,Ly]=i*Lz check below (audit the check, not physics).
    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)

    def cart_gen(basis_index: int) -> sp.Matrix:
        # L_k acting on the linear function a*x+b*y+c*z; read off the resulting
        # coefficient matrix from L_k(x), L_k(y), L_k(z) in turn.
        cols = []
        for target in coords:
            terms = sum(
                sp.LeviCivita(basis_index, i, j) * coords[i] * sp.diff(target, coords[j])
                for i in range(3)
                for j in range(3)
            )
            action = sp.expand(-IMAG * terms)
            cols.append([action.coeff(c) for c in coords])
        return sp.Matrix(cols).T

    tx, ty, tz = cart_gen(0), cart_gen(1), cart_gen(2)
    print("  Tx =", tx.tolist(), " Ty =", ty.tolist(), " Tz =", tz.tolist())

    cart_algebra_ok = (
        commutator(tx, ty) == IMAG * tz
        and commutator(ty, tz) == IMAG * tx
        and commutator(tz, tx) == IMAG * ty
    )
    cart_casimir = sp.simplify(tx * tx + ty * ty + tz * tz)
    cart_casimir_ok = cart_casimir == 2 * sp.eye(3)
    print(
        f"  Cartesian generators satisfy so(3) algebra: {cart_algebra_ok}, Casimir=2*IMAG: {cart_casimir_ok}"
    )

    u = sp.Matrix(3, 3, lambda i, j: sp.symbols(f"u_{i}_{j}"))
    eqs = []
    for t_op, l_op in ((tz, lz), (tx, lx)):
        diff_mat = sp.expand(t_op * u - u * l_op)
        eqs.extend(diff_mat[i, j] for i in range(3) for j in range(3))
    sol = sp.solve(eqs, list(u.free_symbols), dict=True)
    u_free_syms = sorted(u.free_symbols, key=str)
    intertwiner_found = False
    u_numeric = None
    if sol:
        s = sol[0]
        remaining = [v for v in u_free_syms if v not in s]
        subs_free = dict.fromkeys(remaining, 1) if remaining else {}
        u_candidate = u.subs(s).subs(subs_free)
        det_u = sp.simplify(u_candidate.det())
        if det_u != 0:
            intertwiner_found = True
            u_numeric = u_candidate
    print(f"  Intertwiner U found (T_i U = U L_i for i=x,z, det(U)!=0): {intertwiner_found}")
    if u_numeric is not None:
        print("  U =", u_numeric.tolist())
        resid_y = sp.simplify(ty * u_numeric - u_numeric * ly)
        print(f"  Residual check on the THIRD generator (Ly, not used to solve for U): {resid_y}")
        y_also_satisfied = resid_y == sp.zeros(3, 3)
        print(f"  -> Ly also satisfied by the same U (independent check): {y_also_satisfied}")
    else:
        y_also_satisfied = False

    res["part3_positive_control"] = {
        "cartesian_algebra_ok": cart_algebra_ok,
        "cartesian_casimir_ok": cart_casimir_ok,
        "intertwiner_found": intertwiner_found,
        "u_matrix": u_numeric.tolist() if u_numeric is not None else None,
        "ly_independently_satisfied": y_also_satisfied,
        "verdict": "EQUIVALENT_REPRESENTATIONS"
        if (intertwiner_found and y_also_satisfied)
        else "INSTRUMENT_SUSPECT",
    }
    print(f"  VERDICT: {res['part3_positive_control']['verdict']}\n")


def part4_irreducibility_template(res: dict, lx: sp.Matrix, ly: sp.Matrix, lz: sp.Matrix) -> None:
    print("=== Part 4: worked template -- 'invariant does not imply irreducible' ===")
    print("  Compute the commutant of {Lx,Ly,Lz} on the l=1 space (Schur's lemma check).")
    x = sp.Matrix(3, 3, lambda i, j: sp.symbols(f"x_{i}_{j}"))
    eqs = []
    for op in (lx, ly, lz):
        d = sp.expand(op * x - x * op)
        eqs.extend(d[i, j] for i in range(3) for j in range(3))
    free_syms = sorted(x.free_symbols, key=str)
    sol = sp.solve(eqs, free_syms, dict=True)
    commutant_dim = None
    if sol:
        s = sol[0]
        remaining = [v for v in free_syms if v not in s]
        commutant_dim = len(remaining)
    is_schur = commutant_dim == 1
    print(
        f"  Free parameters in the commutant: {commutant_dim} (expect exactly 1 -> scalar multiples of IMAG)"
    )
    print(f"  Schur's lemma / irreducibility of l=1 under {{Lx,Ly,Lz}}: {is_schur}")
    res["part4_irreducibility"] = {
        "commutant_dim": commutant_dim,
        "is_irreducible_by_schur": is_schur,
    }
    print()


def main() -> None:
    res: dict = {}
    part1_mcmurry_ladder(res)
    lx, ly, lz = part2_matrices_and_algebra(res)
    part3_positive_control_intertwiner(res, lx, ly, lz)
    part4_irreducibility_template(res, lx, ly, lz)
    RESULTS_PATH.write_text(json.dumps(res, indent=2, default=str))
    print(f"wrote {RESULTS_PATH.name}")


if __name__ == "__main__":
    main()
