r"""E14 (round80): does group inversion iota: g -> g^{-1} on S^3=SU(2) realize the
t<->1-t symmetry of the Cartan-Schouten connection family as a genuine geometric
isometry -- and does this supply a physical mechanism forcing BOTH t=0 and t=1 to
be simultaneously present in the physical spectrum (E12/E13's multiplicity gap)?

Context (see claim.md for full framing): builds on E7 (round72, t=0,1 are the two
flat Cartan-Schouten connections, curvature ~ t(t-1)), E9/round76 (explicit left-
and right-invariant frames on the concrete quaternion model g(x)=x0*I+x1*Z1+x2*Z2
+x3*Z3, Z_i=i*sigma_i; [Zi^L,Zj^L]=c0*eps(ijk)*Zk^L, [Zi^R,Zj^R]=-c0*eps(ijk)*Zk^R,
c0=-2 found concretely there), and E12/E13 (round78/79, the t=0 and t=1 kernels
match a pre-existing 2+2=4 "one generation" S3-side bookkeeping, but with no known
physical mechanism for why BOTH t values would be simultaneously realized).

Four genuinely computable geometric checks, done directly on the SAME concrete
quaternion model round76 already used (reusing its exact conventions), plus a
non-computational, explicitly-labeled interpretive Section D:

  PART A [isometry]: Phi(x):=(x0,-x1,-x2,-x3) preserves the round metric (its
  constant Jacobian J satisfies J^T J = I), maps the unit sphere to itself, and
  Phi(x) literally equals the coordinates of g(x)^{-1} on the unit sphere (i.e.
  iota is concretely realized by Phi, not merely analogous to it). Also records
  det(J) (orientation) and the fixed-point set of Phi on S^3.

  PART B [frame exchange]: the pushforward of Phi sends the left-invariant frame
  {Z_i^L} to {-Z_i^R} and vice versa -- verified as an EXACT vector-field
  pushforward identity (Phi is linear, so its pushforward at any point is just
  "apply the constant Jacobian J to the vector-field's coordinate values"),
  checked symbolically for all i=1,2,3, both directions.

  PART C [connection swap]: generalizes round76 Part 3's b^j(x) machinery (there,
  a single representative case k=0) to ALL THREE k=0,1,2, and directly verifies
  the "cross product of SO(3)-rotated vectors" identity
      sum_{k,l} b_i^k(x)*b_j^l(x)*eps(k,l,m) == sum_p eps(i,j,p)*b_p^m(x)
  for all i,j,m in {0,1,2} (all 27 combinations, including the trivially-true
  diagonal i=j cases, checked anyway as an honesty/sign-error catch). This
  identity is the ONE new computational ingredient needed (combined with Part A,
  Part B, and the elementary Christoffel-symbol torsion formula, all documented
  in decision.md) to conclude iota^*(Nabla^t) = Nabla^{1-t} for ALL t, not just
  t=0,1 -- a genuine strengthening of E7's curvature-formula-level symmetry to an
  actual geometric-operator-level identity.

  PART D [interpretive, non-computational]: records two purely-algebraic facts
  (t=1-t has the unique solution t=1/2; Phi's fixed-point count on S^3 is 2) that
  are load-bearing for the honest discussion in decision.md of whether Parts A-C
  supply a physical mechanism forcing BOTH t=0 and t=1 to be simultaneously
  present -- this part does NOT attempt a PASS/FAIL verdict on that question,
  which is inherently interpretive (see decision.md Section D).

Honesty ledger: Parts A-C are [VERIFIED-tool], exact sympy symbolic identities,
built directly on this project's own established conventions (E9/round76), no
citation-only steps. Part D is explicitly NOT a computational claim.
"""

from __future__ import annotations

import json

import sympy as sp

I2 = sp.eye(2)
t = sp.symbols("t")
x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
XS = [x0, x1, x2, x3]
NORM2 = x0**2 + x1**2 + x2**2 + x3**2


# ---------------------------------------------------------------------------
# Shared machinery, IDENTICAL to E9/round76's own conventions.
# ---------------------------------------------------------------------------


def pauli_matrices() -> list[sp.Matrix]:
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def clifford_generators() -> list[sp.Matrix]:
    """Z_i = i*sigma_i, {Z_i,Z_j} = -2 delta_ij (E2/E9's own convention)."""
    return [sp.I * s for s in pauli_matrices()]


def eps(i: int, j: int, k: int) -> int:
    """Levi-Civita symbol, 1-indexed i,j,k in {1,2,3}."""
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


def group_element(Z: list[sp.Matrix]) -> sp.Matrix:
    return x0 * I2 + x1 * Z[0] + x2 * Z[1] + x3 * Z[2]


def group_conjugate(Z: list[sp.Matrix]) -> sp.Matrix:
    return x0 * I2 - x1 * Z[0] - x2 * Z[1] - x3 * Z[2]


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
    br12 = vf_bracket(X[0], X[1])
    for mu in range(4):
        if X[2][mu] != 0:
            cand = sp.simplify(sp.cancel(br12[mu] / X[2][mu]))
            if not cand.free_symbols:
                return cand
    raise RuntimeError("could not find c0")


def directional_derivative(fld: list[sp.Expr], scalar_fn: sp.Expr) -> sp.Expr:
    total = sp.Integer(0)
    for mu in range(4):
        total += fld[mu] * sp.diff(scalar_fn, XS[mu])
    return total


def express_fk_in_Z_basis(Z: list[sp.Matrix], Binv: sp.Matrix, k: int):
    """b^j(x) for f_k := X_k^R = coords(Z_k*g), i.e. Z_k^R = sum_j b^j(x) Z_j^L.
    b^j(x) := coefficient of Z_j in gbar(x)*Z_k*g(x) / NORM2 (this scaled product
    equals |x|^2 * g(x)^{-1} Z_k g(x), the adjoint action, up to the NORM2 factor
    divided out below -- identical method to round76 Part 3, generalized to
    arbitrary k here instead of the single representative k=0 case there)."""
    g = group_element(Z)
    gbar = group_conjugate(Z)
    conj_scaled = sp.expand(gbar * Z[k] * g)
    coeffs_scaled = coords_in_basis(conj_scaled, Binv)
    i2_component_is_zero = sp.simplify(sp.expand(coeffs_scaled[0])) == 0
    b = [sp.together(coeffs_scaled[j + 1] / NORM2) for j in range(3)]
    return b, i2_component_is_zero


# ---------------------------------------------------------------------------
# PART A: isometry check.
# ---------------------------------------------------------------------------


def run_part_a(Z: list[sp.Matrix]) -> dict[str, object]:
    J = sp.diag(1, -1, -1, -1)  # constant Jacobian of Phi(x) = (x0,-x1,-x2,-x3)

    isometry_check = sp.simplify(J.T * J - sp.eye(4)) == sp.zeros(4, 4)

    Phi = [x0, -x1, -x2, -x3]
    sphere_preserved = sp.simplify(sp.expand(sum(p**2 for p in Phi) - NORM2)) == 0

    g = group_element(Z)
    gbar = group_conjugate(Z)
    g_at_Phi = g.subs(list(zip(XS, Phi)), simultaneous=True)
    phi_realizes_conjugate = sp.simplify(sp.expand(g_at_Phi - gbar)) == sp.zeros(2, 2)

    prod = sp.simplify(sp.expand(g * gbar))
    expected = sp.expand(NORM2) * I2
    g_ginv_is_norm2 = sp.simplify(prod - expected) == sp.zeros(2, 2)

    det_J = J.det()

    fixed_pts = sp.solve(
        [sp.Eq(x1, 0), sp.Eq(x2, 0), sp.Eq(x3, 0), sp.Eq(x0**2, 1)], [x0, x1, x2, x3], dict=True
    )

    return {
        "J": str(J.tolist()),
        "isometry_check_JtJ_eq_I": bool(isometry_check),
        "Phi_maps_sphere_to_itself": bool(sphere_preserved),
        "Phi_realizes_group_conjugate_gbar": bool(phi_realizes_conjugate),
        "g_times_gbar_equals_norm2_I": bool(g_ginv_is_norm2),
        "det_J": str(det_J),
        "Phi_is_orientation_reversing": bool(det_J == -1),
        "fixed_points_x0_x1_x2_x3": [str(fp) for fp in fixed_pts],
        "num_fixed_points": len(fixed_pts),
    }


# ---------------------------------------------------------------------------
# PART B: pushforward / frame-exchange check.
# ---------------------------------------------------------------------------


def run_part_b(Z: list[sp.Matrix], Binv: sp.Matrix) -> dict[str, object]:
    XL, XR = build_invariant_frames(Z, Binv)
    J = sp.diag(1, -1, -1, -1)
    Phi_subs = list(zip(XS, [x0, -x1, -x2, -x3]))

    def apply_J(vec: list[sp.Expr]) -> list[sp.Expr]:
        v = sp.Matrix(vec)
        return list(J * v)

    def at_Phi(vec: list[sp.Expr]) -> list[sp.Expr]:
        return [sp.expand(comp.subs(Phi_subs, simultaneous=True)) for comp in vec]

    l_to_minus_r = []
    r_to_minus_l = []
    for i in range(3):
        lhs_l = apply_J(XL[i])
        rhs_l = [-c for c in at_Phi(XR[i])]
        diff_l = [sp.simplify(sp.expand(lhs_l[mu] - rhs_l[mu])) for mu in range(4)]
        ok_l = all(d == 0 for d in diff_l)
        l_to_minus_r.append({"i": i + 1, "ok": bool(ok_l), "residual": [str(d) for d in diff_l]})

        lhs_r = apply_J(XR[i])
        rhs_r = [-c for c in at_Phi(XL[i])]
        diff_r = [sp.simplify(sp.expand(lhs_r[mu] - rhs_r[mu])) for mu in range(4)]
        ok_r = all(d == 0 for d in diff_r)
        r_to_minus_l.append({"i": i + 1, "ok": bool(ok_r), "residual": [str(d) for d in diff_r]})

    return {
        "pushforward_XL_equals_minus_XR_at_Phi": l_to_minus_r,
        "pushforward_XR_equals_minus_XL_at_Phi": r_to_minus_l,
        "all_L_to_minus_R_ok": bool(all(e["ok"] for e in l_to_minus_r)),
        "all_R_to_minus_L_ok": bool(all(e["ok"] for e in r_to_minus_l)),
    }


# ---------------------------------------------------------------------------
# PART C: connection-swap check (rotation-coefficient identity).
# ---------------------------------------------------------------------------


def run_part_c(Z: list[sp.Matrix], Binv: sp.Matrix) -> dict[str, object]:
    XL, XR = build_invariant_frames(Z, Binv)
    c0 = find_structure_constant(XL)

    # generalize round76 Part 3's b^j(x) to all three k=0,1,2
    b = []  # b[k][j] = b^j(x) for f_k
    i2_zero_all = []
    reconstruction_ok_all = []
    for k in range(3):
        bk, i2_zero = express_fk_in_Z_basis(Z, Binv, k)
        b.append(bk)
        i2_zero_all.append({"k": k + 1, "i2_component_is_zero": bool(i2_zero)})
        reconstructed = [sp.Integer(0)] * 4
        for j in range(3):
            for mu in range(4):
                reconstructed[mu] += bk[j] * XL[j][mu]
        reconstructed = [sp.simplify(sp.together(v)) for v in reconstructed]
        target = [sp.simplify(sp.together(v)) for v in XR[k]]
        ok = all(sp.simplify(sp.together(reconstructed[mu] - target[mu])) == 0 for mu in range(4))
        reconstruction_ok_all.append({"k": k + 1, "reconstruction_matches_XR": bool(ok)})

    # the rotation-coefficient identity:
    # sum_{k,l} b_i^k(x) b_j^l(x) eps(k+1,l+1,m+1) == sum_p eps(i+1,j+1,p+1) b_p^m(x)
    # for all i,j,m in {0,1,2}. This is the ONE new computational ingredient for
    # Part C; see decision.md for how it combines with Parts A/B into the full
    # connection-swap conclusion.
    identity_results = []
    all_identity_ok = True
    for i in range(3):
        for j in range(3):
            for m in range(3):
                lhs = sp.Integer(0)
                for k in range(3):
                    for ll in range(3):
                        e = eps(k + 1, ll + 1, m + 1)
                        if e != 0:
                            lhs += b[i][k] * b[j][ll] * e
                rhs = sp.Integer(0)
                for p in range(3):
                    e = eps(i + 1, j + 1, p + 1)
                    if e != 0:
                        rhs += e * b[p][m]
                diff = sp.simplify(sp.together(sp.expand(lhs - rhs)))
                ok = diff == 0
                all_identity_ok &= ok
                identity_results.append(
                    {"i": i + 1, "j": j + 1, "m": m + 1, "diff": str(diff), "ok": bool(ok)}
                )

    # sanity check: torsion-from-Christoffel formula T^t(Zi,Zj) = (2t-1)*c0*eps(ijk)*Zk
    # (definitional, but verified here rather than merely asserted)
    def christoffel_left(i: int, j: int, k: int) -> sp.Expr:
        return t * c0 * eps(i + 1, j + 1, k + 1)

    torsion_formula_ok = True
    for i in range(3):
        for j in range(3):
            for k in range(3):
                gamma_ij = christoffel_left(i, j, k)
                gamma_ji = christoffel_left(j, i, k)
                bracket_term = c0 * eps(i + 1, j + 1, k + 1)
                torsion_ijk = sp.simplify(gamma_ij - gamma_ji - bracket_term)
                expected = (2 * t - 1) * c0 * eps(i + 1, j + 1, k + 1)
                if sp.simplify(torsion_ijk - expected) != 0:
                    torsion_formula_ok = False

    return {
        "c0_found": str(c0),
        "i2_component_checks": i2_zero_all,
        "reconstruction_checks": reconstruction_ok_all,
        "all_i2_zero": bool(all(e["i2_component_is_zero"] for e in i2_zero_all)),
        "all_reconstructions_ok": bool(
            all(e["reconstruction_matches_XR"] for e in reconstruction_ok_all)
        ),
        "rotation_coefficient_identity_results": identity_results,
        "all_27_identity_checks_ok": bool(all_identity_ok),
        "torsion_formula_T_t_eq_2t_minus_1_c0_eps_verified": bool(torsion_formula_ok),
    }


# ---------------------------------------------------------------------------
# PART D: interpretive load-bearing algebraic facts (NOT a PASS/FAIL verdict).
# ---------------------------------------------------------------------------


def run_part_d() -> dict[str, object]:
    fixed_t = sp.solve(sp.Eq(t, 1 - t), t)
    J = sp.diag(1, -1, -1, -1)
    return {
        "t_eq_1_minus_t_unique_solution": [str(s) for s in fixed_t],
        "t_star_is_one_half": fixed_t == [sp.Rational(1, 2)],
        "det_J_orientation_reversing_recheck": str(J.det()),
        "note": (
            "This section is intentionally NOT a computational PASS/FAIL claim -- "
            "see decision.md Section D for the honest interpretive discussion of "
            "whether Parts A-C supply a physical mechanism for BOTH t=0 and t=1 "
            "to be simultaneously present."
        ),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> dict:
    Z = clifford_generators()
    Binv = basis_inverse(Z)

    part_a = run_part_a(Z)
    part_b = run_part_b(Z, Binv)
    part_c = run_part_c(Z, Binv)
    part_d = run_part_d()

    core_a_pass = bool(
        part_a["isometry_check_JtJ_eq_I"]
        and part_a["Phi_maps_sphere_to_itself"]
        and part_a["Phi_realizes_group_conjugate_gbar"]
        and part_a["g_times_gbar_equals_norm2_I"]
    )
    core_b_pass = bool(part_b["all_L_to_minus_R_ok"] and part_b["all_R_to_minus_L_ok"])
    core_c_pass = bool(
        part_c["all_i2_zero"]
        and part_c["all_reconstructions_ok"]
        and part_c["all_27_identity_checks_ok"]
        and part_c["torsion_formula_T_t_eq_2t_minus_1_c0_eps_verified"]
    )

    if core_a_pass and core_b_pass and core_c_pass:
        overall_label = "PASS_GEOMETRIC_Z2_CONFIRMED__PHYSICAL_MECHANISM_STILL_OPEN"
    elif core_a_pass and core_b_pass and not core_c_pass:
        overall_label = "PARTIAL_ENDPOINT_SWAP_ONLY__GENERAL_T_IDENTITY_FAILS"
    else:
        overall_label = "FAIL_CORE_GEOMETRIC_CLAIM"

    result = {
        "part_a_isometry": part_a,
        "part_b_frame_exchange": part_b,
        "part_c_connection_swap": part_c,
        "part_d_interpretive_facts": part_d,
        "verdict": {
            "core_a_pass": core_a_pass,
            "core_b_pass": core_b_pass,
            "core_c_pass": core_c_pass,
            "label": overall_label,
        },
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    out_path = "results_e14.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nSaved: {out_path}")
