r"""E19 (round89): does this project's OWN Nabla^t / Nabla^{LC} connection-
difference formula turn "Nabla^t-parallel" into an exact AHL2023 Riemannian
Killing-spinor equation? See claim.md for full framing and pre-registered
kill criteria.

Every convention below is reused BYTE-IDENTICAL from prior experiments, not
reinvented:
  - Z_i = i*sigma_i, Clifford relations {Z_i,Z_j}=-2*delta_ij
    (experiments/20260717-round73-e9-explicit-parallel-spinor/
     e9_explicit_parallel_spinor.py:90-99, clifford_generators/
     verify_clifford_relations).
  - Gamma^k_ij(t) = t*c*eps(i,j,k); Omega_i(t) = -(t*c/2)*Z_i, the spin lift
    (same file, christoffel/spin_connection_Omega, lines 137-178).
  - t=0/t=1 = canonical/anticanonical connections; t=1/2 = Levi-Civita
    (experiments/20260717-round72-e7-t-selection-principle/decision.md:
     155-161, 191-192; claim.md:24-25,101,104,126).
  - c0=-2 concrete structure constant vs c=+2 abstract (physics-calibrated)
    (experiments/20260717-round76-e9followup-right-invariant-frame/
     e10_right_invariant_frame.py, find_structure_constant/run_part1).
  - t=1 explicit parallel spinor psi(x)=gbar(x)*psi0, established ONLY under
    c0=-2 (same file, run_part4, psi_is_nabla1_parallel_using_c0).

NEW in this experiment (not previously computed anywhere in this project):
  - Omega_i^LC := Omega_i(t=1/2), and the connection-difference formula
    Omega_i(t) - Omega_i^LC, used to derive/verify that a Nabla^t-parallel
    spinor is an exact Nabla^{LC}-Killing spinor with a computed constant
    lambda(t), compared against AHL2023's own stated +-1/2 (reused via
    experiments/20260717-round86-parent-action-discriminator/decision.md:
    129-141, NOT re-extracted from the PDF here).
"""

from __future__ import annotations

import json

import sympy as sp

I2 = sp.eye(2)
t, c = sp.symbols("t c")
a, b = sp.symbols("a b")
a_, b_ = sp.symbols("a_ b_")
x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
XS = [x0, x1, x2, x3]
NORM2 = x0**2 + x1**2 + x2**2 + x3**2

HALF = sp.Rational(1, 2)


# ---------------------------------------------------------------------------
# Shared machinery, IDENTICAL to E9/E10's own conventions (reused, not redefined)
# ---------------------------------------------------------------------------


def pauli_matrices() -> list[sp.Matrix]:
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def clifford_generators() -> list[sp.Matrix]:
    """Z_i = i*sigma_i, giving {Z_i,Z_j} = -2 delta_ij (E2/E9/E10's convention)."""
    return [sp.I * s for s in pauli_matrices()]


def verify_clifford_relations(Z: list[sp.Matrix]) -> bool:
    for i in range(3):
        for j in range(i, 3):
            anticomm = sp.simplify(Z[i] * Z[j] + Z[j] * Z[i])
            expected = -2 * I2 if i == j else sp.zeros(2, 2)
            if sp.simplify(anticomm - expected) != sp.zeros(2, 2):
                return False
    return True


def eps(i: int, j: int, k: int) -> int:
    """Levi-Civita symbol, 1-indexed i,j,k in {1,2,3} (identical to E7/E9/E10)."""
    p = [i, j, k]
    if len(set(p)) < 3:
        return 0
    sign = 1
    perm = p[:]
    n = 3
    for xx in range(n):
        for yy in range(n - 1 - xx):
            if perm[yy] > perm[yy + 1]:
                perm[yy], perm[yy + 1] = perm[yy + 1], perm[yy]
                sign = -sign
    return sign


def christoffel(i: int, j: int, k: int) -> sp.Expr:
    """Gamma^k_{ij}(t) = t*c*eps(i,j,k) (E9's own formula, unchanged)."""
    return t * c * eps(i + 1, j + 1, k + 1)


def spin_connection_Omega(i: int, Z: list[sp.Matrix]) -> sp.Matrix:
    """Omega_i(t) = (1/4) sum_{j,k} Gamma^k_{ij}(t) * Z_j.Z_k (E9's own formula,
    e9_explicit_parallel_spinor.py:171-178, unchanged)."""
    total = sp.zeros(2, 2)
    for j in range(3):
        for k in range(3):
            coeff = christoffel(i, j, k)
            if coeff != 0:
                total += coeff * (Z[j] * Z[k])
    return sp.simplify(total / 4)


# ---------------------------------------------------------------------------
# PART 0: fresh torsion check -- confirm t=1/2 is genuinely the torsion-free
# (Levi-Civita) member of the family, not merely cited from E7.
# T^k_{ij}(t) := Gamma^k_{ij}(t) - Gamma^k_{ji}(t) - c*eps(i,j,k)
#   (the bracket term [Z_i,Z_j] = c*eps(i,j,k)*Z_k is the THIRD term subtracted,
#    matching E7/E9's own [Z_i,Z_j]=c*eps(i,j,k)*Z_k convention)
# ---------------------------------------------------------------------------


def check_torsion() -> dict[str, object]:
    torsion_entries = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                lhs = christoffel(i, j, k) - christoffel(j, i, k)
                bracket_term = c * eps(i + 1, j + 1, k + 1)
                Tk = sp.simplify(lhs - bracket_term)
                expected = c * (2 * t - 1) * eps(i + 1, j + 1, k + 1)
                matches_expected_form = sp.simplify(Tk - expected) == 0
                torsion_entries.append(
                    {
                        "i": i + 1,
                        "j": j + 1,
                        "k": k + 1,
                        "T": str(Tk),
                        "matches_c_times_2t_minus_1_times_eps": bool(matches_expected_form),
                    }
                )
    all_match_form = all(e["matches_c_times_2t_minus_1_times_eps"] for e in torsion_entries)

    # torsion vanishes identically (for ALL i,j,k, given c != 0) iff (2t-1)=0
    roots = sp.solve(sp.Eq(2 * t - 1, 0), t)
    torsion_zero_iff_t_half = roots == [HALF]

    return {
        "torsion_entries_sample": torsion_entries[:3],
        "all_entries_match_c_times_2t_minus_1_times_eps_form": bool(all_match_form),
        "roots_of_2t_minus_1": [str(r) for r in roots],
        "torsion_zero_iff_t_half": bool(torsion_zero_iff_t_half and all_match_form),
    }


# ---------------------------------------------------------------------------
# PART A: the connection-difference bridge formula, symbolic in t,c.
# ---------------------------------------------------------------------------


def check_diff_formula(Z: list[sp.Matrix]) -> dict[str, object]:
    """Verify Omega_i(t) - Omega_i^LC = -(c/2)(t-1/2)*Z_i exactly (equivalently
    Omega_i^LC - Omega_i(t) = +(c/2)(t-1/2)*Z_i -- the sign that actually
    matters for the Killing-equation derivation used in check_t0_killing/
    check_t1_killing below: Nabla^{LC}psi = [Omega_LC - Omega(t)]*psi when psi
    is Nabla^t-parallel, i.e. lambda(t) = +(c/2)(t-1/2))."""
    diffs = []
    all_match = True
    for i in range(3):
        Omega_t = spin_connection_Omega(i, Z)
        Omega_LC = spin_connection_Omega(i, Z).subs(t, HALF)
        diff = sp.simplify(Omega_t - Omega_LC)
        predicted = sp.simplify(-(c * HALF) * (t - HALF) * Z[i])
        match = sp.simplify(diff - predicted) == sp.zeros(2, 2)
        all_match &= match
        diffs.append(
            {"i": i + 1, "diff": str(diff), "predicted": str(predicted), "match": bool(match)}
        )
    return {"per_i": diffs, "diff_formula_matches": bool(all_match)}


# ---------------------------------------------------------------------------
# PART B: t=0 Killing check.
# ---------------------------------------------------------------------------


def check_t0_killing(Z: list[sp.Matrix]) -> dict[str, object]:
    psi = sp.Matrix([a, b])
    Omega_LC = [spin_connection_Omega(i, Z).subs(t, HALF) for i in range(3)]
    Omega_0 = [spin_connection_Omega(i, Z).subs(t, 0) for i in range(3)]

    # confirm parallel at t=0 first (re-verify, not assumed)
    parallel_0 = all(sp.simplify(Omega_0[i] * psi) == sp.zeros(2, 1) for i in range(3))

    # Nabla^{LC}_{Z_i} psi = Z_i(psi) [=0, psi constant] + Omega_LC[i]*psi
    lambda0_symbolic = sp.simplify(-c * sp.Rational(1, 4))  # candidate, from Omega_LC[i]=-(c/4)Z_i

    lambdas = []
    all_consistent = True
    for i in range(3):
        lhs = sp.simplify(Omega_LC[i] * psi)  # Z_i(psi)=0 for constant psi
        rhs = sp.expand(lambda0_symbolic * Z[i] * psi)
        diff = sp.Matrix([sp.simplify(sp.expand(lhs[r] - rhs[r])) for r in range(2)])
        ok = diff == sp.zeros(2, 1)
        all_consistent &= ok
        lambdas.append({"i": i + 1, "residual": str(diff.T), "matches_lambda0": bool(ok)})

    return {
        "t0_parallel_reverified": bool(parallel_0),
        "lambda_candidates_per_i": lambdas,
        "t0_killing_check": bool(parallel_0 and all_consistent),
        "lambda0_symbolic_in_c": str(lambda0_symbolic),
        "lambda0_at_c2": str(lambda0_symbolic.subs(c, 2)),
        "lambda0_at_c0_minus2": str(lambda0_symbolic.subs(c, -2)),
    }


# ---------------------------------------------------------------------------
# PART C: t=1 Killing check, reusing round76's own g(x)/gbar(x)/directional
# derivative machinery EXACTLY (e10_right_invariant_frame.py).
# ---------------------------------------------------------------------------


def basis_matrices(Z: list[sp.Matrix]) -> list[sp.Matrix]:
    return [I2, Z[0], Z[1], Z[2]]


def basis_inverse(Z: list[sp.Matrix]) -> sp.Matrix:
    basis = basis_matrices(Z)
    cols = []
    for M in basis:
        cols.append([M[0, 0], M[0, 1], M[1, 0], M[1, 1]])
    Bmat = sp.Matrix(cols).T
    return sp.simplify(Bmat.inv())


def coords_in_basis(M: sp.Matrix, Binv: sp.Matrix) -> list[sp.Expr]:
    v = sp.Matrix([M[0, 0], M[0, 1], M[1, 0], M[1, 1]])
    coeffs = Binv * v
    return [sp.simplify(coeffs[i]) for i in range(4)]


def group_element(Z: list[sp.Matrix]) -> sp.Matrix:
    return x0 * I2 + x1 * Z[0] + x2 * Z[1] + x3 * Z[2]


def group_conjugate(Z: list[sp.Matrix]) -> sp.Matrix:
    return x0 * I2 - x1 * Z[0] - x2 * Z[1] - x3 * Z[2]


def build_invariant_frames(Z: list[sp.Matrix], Binv: sp.Matrix):
    g = group_element(Z)
    XL, XR = [], []
    for i in range(3):
        ML = sp.expand(g * Z[i])
        MR = sp.expand(Z[i] * g)
        XL.append(coords_in_basis(ML, Binv))
        XR.append(coords_in_basis(MR, Binv))
    return XL, XR


def vf_bracket(V: list[sp.Expr], W: list[sp.Expr]) -> list[sp.Expr]:
    out = []
    for mu in range(4):
        term = sp.Integer(0)
        for nu in range(4):
            term += V[nu] * sp.diff(W[mu], XS[nu]) - W[nu] * sp.diff(V[mu], XS[nu])
        out.append(sp.expand(term))
    return out


def find_structure_constant(X: list[list[sp.Expr]]) -> sp.Expr:
    """Reused from round76's own find_structure_constant -- concrete c0, found
    (not assumed), via [X_1^L,X_2^L] = c0*eps(1,2,3)*X_3^L = c0*X_3^L."""
    br12 = vf_bracket(X[0], X[1])
    ratio = None
    for mu in range(4):
        if X[2][mu] != 0:
            cand = sp.simplify(sp.cancel(br12[mu] / X[2][mu]))
            if not cand.free_symbols:
                ratio = cand
                break
    return ratio


def directional_derivative(fld: list[sp.Expr], scalar_fn: sp.Expr) -> sp.Expr:
    total = sp.Integer(0)
    for mu in range(4):
        total += fld[mu] * sp.diff(scalar_fn, XS[mu])
    return total


def check_t1_killing(Z: list[sp.Matrix]) -> dict[str, object]:
    Binv = basis_inverse(Z)
    XL, _XR = build_invariant_frames(Z, Binv)
    c0 = find_structure_constant(XL)

    gbar = group_conjugate(Z)
    psi0 = sp.Matrix([a_, b_])
    psi = sp.expand(gbar * psi0)  # round76's own t=1 candidate, run_part4

    def Zi_of_psi(i: int) -> sp.Matrix:
        comps = []
        for row in range(2):
            comps.append(directional_derivative(XL[i], psi[row]))
        return sp.Matrix(comps)

    # Omega_i(1) at c0 (E9's own formula, t=1, c=c0) -- re-verify parallel first
    Omega_1_c0 = [sp.simplify(-(HALF * c0) * Z[i]) for i in range(3)]
    parallel_results = []
    all_parallel = True
    for i in range(3):
        lhs = sp.expand(Zi_of_psi(i) + Omega_1_c0[i] * psi)
        lhs = sp.Matrix([sp.simplify(sp.expand(v)) for v in lhs])
        ok = lhs == sp.zeros(2, 1)
        all_parallel &= ok
        parallel_results.append({"i": i + 1, "is_zero": bool(ok)})

    # Omega_i^LC at c0 (t=1/2, c=c0)
    Omega_LC_c0 = [sp.simplify(-(sp.Rational(1, 4) * c0) * Z[i]) for i in range(3)]

    # Route 1: literal computation, Nabla^{LC}_{Z_i}psi = Z_i(psi) + Omega_LC_c0[i]*psi
    killing_lhs_direct = []
    for i in range(3):
        lhs = sp.expand(Zi_of_psi(i) + Omega_LC_c0[i] * psi)
        lhs = sp.Matrix([sp.simplify(sp.expand(v)) for v in lhs])
        killing_lhs_direct.append(lhs)

    # candidate lambda, symbolic in c0 (structural: lambda(1) = (c/2)(1-1/2) = c/4)
    lambda1_symbolic = sp.simplify(c0 * sp.Rational(1, 4))

    residuals_direct = []
    all_match_direct = True
    for i in range(3):
        rhs = lambda1_symbolic * Z[i] * psi
        rhs = sp.Matrix([sp.expand(v) for v in rhs])
        diff = sp.Matrix(
            [sp.simplify(sp.expand(killing_lhs_direct[i][r] - rhs[r])) for r in range(2)]
        )
        ok = diff == sp.zeros(2, 1)
        all_match_direct &= ok
        residuals_direct.append({"i": i + 1, "residual": str(diff.T), "matches_lambda1": bool(ok)})

    # Route 2 (independent, algebraic shortcut): using the parallel condition
    # Z_i(psi) = -Omega_1_c0[i]*psi, so Nabla^{LC}_{Z_i}psi = (Omega_LC_c0[i] -
    # Omega_1_c0[i]) * psi -- cross-check this equals lambda1 * Z_i * psi too.
    residuals_shortcut = []
    all_match_shortcut = True
    for i in range(3):
        lhs_shortcut = sp.expand((Omega_LC_c0[i] - Omega_1_c0[i]) * psi)
        lhs_shortcut = sp.Matrix([sp.simplify(v) for v in lhs_shortcut])
        rhs = sp.Matrix([sp.expand(v) for v in lambda1_symbolic * Z[i] * psi])
        diff = sp.Matrix([sp.simplify(sp.expand(lhs_shortcut[r] - rhs[r])) for r in range(2)])
        ok = diff == sp.zeros(2, 1)
        all_match_shortcut &= ok
        residuals_shortcut.append(
            {"i": i + 1, "residual": str(diff.T), "matches_lambda1": bool(ok)}
        )

    two_routes_agree = bool(all_match_direct == all_match_shortcut)

    return {
        "c0_found": str(c0),
        "t1_parallel_reverified_using_c0": bool(all_parallel),
        "parallel_checks": parallel_results,
        "lambda1_symbolic_in_c0": str(lambda1_symbolic),
        "route1_direct_residuals": residuals_direct,
        "route1_all_match": bool(all_match_direct),
        "route2_shortcut_residuals": residuals_shortcut,
        "route2_all_match": bool(all_match_shortcut),
        "two_independent_routes_agree": two_routes_agree,
        "t1_killing_check": bool(all_parallel and all_match_direct and all_match_shortcut),
    }


# ---------------------------------------------------------------------------
# PART D: sign-structure check, and AHL2023 comparison.
# ---------------------------------------------------------------------------


def check_sign_structure() -> dict[str, object]:
    lam = lambda tv: sp.simplify((c * HALF) * (tv - HALF))
    lam0 = lam(0)
    lam1 = lam(1)
    opposite_sign_identity = sp.simplify(lam1 + lam0) == 0  # lam1 == -lam0 for ALL c
    return {
        "lambda_t_formula": "(c/2)*(t-1/2)",
        "lambda0_symbolic": str(lam0),
        "lambda1_symbolic": str(lam1),
        "lambda1_equals_minus_lambda0_symbolic": bool(opposite_sign_identity),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> dict:
    Z = clifford_generators()
    clifford_ok = verify_clifford_relations(Z)

    torsion = check_torsion()
    diff_formula = check_diff_formula(Z)
    t0 = check_t0_killing(Z)
    t1 = check_t1_killing(Z)
    sign_structure = check_sign_structure()

    lambda0_at_c0 = sp.simplify(sp.sympify(t0["lambda0_symbolic_in_c"]).subs(c, -2))
    lambda1_at_c0 = sp.sympify(t1["lambda1_symbolic_in_c0"])  # already uses concrete c0

    lambda0_magnitude_is_half = sp.Abs(lambda0_at_c0) == HALF
    lambda1_magnitude_is_half = sp.Abs(lambda1_at_c0) == HALF
    signs_opposite_numeric = bool(sp.simplify(lambda0_at_c0 + lambda1_at_c0) == 0)

    bridge_ok = bool(
        clifford_ok
        and torsion["torsion_zero_iff_t_half"]
        and diff_formula["diff_formula_matches"]
        and t0["t0_killing_check"]
        and t1["t1_killing_check"]
    )
    magnitudes_match_half = bool(lambda0_magnitude_is_half and lambda1_magnitude_is_half)

    if not bridge_ok:
        label = "FAIL_BRIDGE_BROKEN"
    elif not magnitudes_match_half:
        label = "PARTIAL_BRIDGE_OK_MAGNITUDE_MISMATCH"
    elif signs_opposite_numeric and sign_structure["lambda1_equals_minus_lambda0_symbolic"]:
        # opposite-sign pair, forced structurally -- matches AHL2023's GENERAL
        # (other-n) Corollary 3.14 wording, NOT its n=1-specific p.48 same-sign
        # statement (see decision.md for the full comparison and verdict).
        label = "PARTIAL_OPPOSITE_SIGN_STRUCTURAL"
    else:
        label = "PASS_SAME_SIGN_MATCH"

    result = {
        "step0_clifford_ok": clifford_ok,
        "step1_torsion_check": torsion,
        "step2_diff_formula_check": diff_formula,
        "step3_t0_killing_check": t0,
        "step4_t1_killing_check": t1,
        "step5_sign_structure_check": sign_structure,
        "verdict": {
            "clifford_ok": clifford_ok,
            "torsion_zero_iff_t_half": torsion["torsion_zero_iff_t_half"],
            "diff_formula_matches": diff_formula["diff_formula_matches"],
            "t0_killing_check": t0["t0_killing_check"],
            "t1_killing_check": t1["t1_killing_check"],
            "lambda0_at_c0_minus2": str(lambda0_at_c0),
            "lambda1_at_c0_minus2": str(lambda1_at_c0),
            "lambda0_magnitude_is_half": bool(lambda0_magnitude_is_half),
            "lambda1_magnitude_is_half": bool(lambda1_magnitude_is_half),
            "signs_opposite_numeric": signs_opposite_numeric,
            "lambda1_equals_minus_lambda0_symbolic": sign_structure[
                "lambda1_equals_minus_lambda0_symbolic"
            ],
            "bridge_ok": bridge_ok,
            "magnitudes_match_half": magnitudes_match_half,
            "label": label,
        },
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    out_path = "results_e19.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nSaved: {out_path}")
