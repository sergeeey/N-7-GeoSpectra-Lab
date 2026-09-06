r"""
C167 -- P4 diagonal ZZ_p orbifold, Step 1: holonomy-descent check.

Frozen claim (see claim.md, written BEFORE this script was run): quotienting
S^3 = SU(2) by a free left ZZ_p action (ZZ_p subset U(1) subset SU(2)) makes
the left-invariant parallel frame of the t=0 canonical connection descend to
L(p,1) = S^3/ZZ_p with TRIVIAL holonomy for every p, while the right-invariant
parallel frame of the t=1 connection descends with NONTRIVIAL Ad(zeta_p)
holonomy whenever zeta_p is non-central in SU(2), i.e. whenever p >= 3 -- and
TRIVIAL holonomy at p=1,2 (zeta_p in {I,-I}, the center of SU(2)).

This directly removes, for exactly one endpoint (t=1) and not the other
(t=0), the precondition ("S^3 is simply connected, pi_1(S^3)=0, so there is
no monodromy obstruction") that round72/E7's H1b proof used to establish that
BOTH t=0 and t=1 give a globally parallel spinor (hence a zero mode) on the
un-quotiented S^3. See:
  experiments/20260717-round72-e7-t-selection-principle/decision.md, lines 27-57.

AOG-5 discipline (mandatory, per the task brief and per C132's own P4 entry's
explicit circularity warning): the claim is tested as a GENERAL statement
over p, with a symbolic all-p derivation, and only THEN evaluated at the
concrete sweep p=2,3,4,5 -- p=3 is reported as one row of that sweep, not
computed in isolation.

Everything below is EXACT (sympy, roots of unity / trig simplification), not
floating point, so a printed "0" or "Id" means exactly zero / exactly the
identity, not "small".

Run: python c167_holonomy_descent_check.py
"""

from __future__ import annotations

import json

import sympy as sp
from sympy import I, Matrix, cos, eye, pi, simplify, sin, symbols

# ---------------------------------------------------------------------------
# Step 0: SU(2) as 2x2 unitary matrices, su(2) via Pauli matrices.
# Concrete matrix realization is used (not the project's abstract Z1,Z2,Z3
# structure-constant convention from round72) because the periodicity of the
# exponential map / the center of SU(2) are group-level facts that need an
# actual matrix representation to pin down unambiguously; the abstract
# structure-constant picture is cross-checked afterward (Step 5) and agrees.
# ---------------------------------------------------------------------------

sigma1 = Matrix([[0, 1], [1, 0]])
sigma2 = Matrix([[0, -I], [I, 0]])
sigma3 = Matrix([[1, 0], [0, -1]])
pauli = [sigma1, sigma2, sigma3]


def zeta(p: int):
    """zeta_p = diag(exp(2*pi*I/p), exp(-2*pi*I/p)) -- order-p generator of
    the diagonal torus U(1) subset SU(2), i.e. of ZZ_p acting by LEFT
    translation g -> zeta_p * g."""
    theta = 2 * pi / p
    return Matrix([[sp.exp(I * theta), 0], [0, sp.exp(-I * theta)]])


def is_identity(M: Matrix) -> bool:
    return simplify(M - eye(M.rows)) == sp.zeros(M.rows, M.cols)


# ---------------------------------------------------------------------------
# T5 -- freeness: zeta_p^k != I for 0 < k < p (exact).
# ---------------------------------------------------------------------------


def freeness_check(p: int) -> dict:
    z = zeta(p)
    results = {}
    for k in range(1, p):
        zk = simplify(z**k)
        results[k] = not is_identity(zk)  # True = "not fixed", i.e. good
    zp = simplify(z**p)
    results["order_p_confirmed"] = is_identity(zp)
    return results


# ---------------------------------------------------------------------------
# Step 1 / T1: Ad(zeta_p) as a 3x3 REAL matrix acting on su(2) via the Pauli
# basis: zeta * sigma_k * zeta^{-1} = sum_j R_{jk} sigma_j. R is the adjoint
# action in SO(3) (this is the standard double-cover fact, re-derived here
# directly rather than assumed).
# ---------------------------------------------------------------------------


def adjoint_matrix(g: Matrix) -> Matrix:
    ginv = simplify(g.inv())
    cols = []
    for sk in pauli:
        conj = simplify(g * sk * ginv)
        # Express conj in the Pauli basis: conj = sum_j c_j sigma_j.
        # Use trace(sigma_j * conj)/2 = c_j (Pauli matrices are trace-
        # orthogonal: tr(sigma_i sigma_j) = 2 delta_ij).
        col = []
        for sj in pauli:
            c = simplify(sp.trace(sj * conj) / 2)
            col.append(c)
        cols.append(col)
    # cols[k] holds Ad(g)(sigma_k) expressed in the sigma_j basis -> matrix
    # columns.
    R = Matrix.hstack(*[Matrix(c) for c in cols])
    return simplify(R)


def rotation_angle_about_z_numeric(R: Matrix) -> float:
    """Numeric (float) rotation angle about z, for human-readable reporting
    only -- NOT load-bearing. The load-bearing fact ("Ad_is_identity") is
    decided exactly via is_identity(), independent of this readout. Exact
    symbolic atan2 on 5th-root-of-unity entries (p=5) does not simplify to a
    clean closed form, so this reports sp.N(...) instead of forcing an exact
    symbolic simplification that would obscure rather than clarify."""
    r10 = complex(sp.N(R[1, 0])).real
    r00 = complex(sp.N(R[0, 0])).real
    return float(sp.atan2(r10, r00))


# ---------------------------------------------------------------------------
# General-p symbolic derivation (AOG-5: do this BEFORE the concrete sweep).
# ---------------------------------------------------------------------------


def general_p_derivation() -> dict:
    p = symbols("p", positive=True, integer=True)
    theta = 2 * pi / p
    g = Matrix([[sp.exp(I * theta), 0], [0, sp.exp(-I * theta)]])
    R = adjoint_matrix(g)
    # This concrete convention (conjugation zeta*sigma_k*zeta^{-1}, columns
    # read off in the sigma_j basis) gives rotation by angle MINUS 2*theta,
    # i.e. -4*pi/p -- an overall orientation/handedness choice with no
    # bearing on the load-bearing question (whether Ad(zeta) equals the
    # identity), since a rotation by -a is the identity iff a rotation by +a
    # is. Checked here explicitly (rather than silently assumed) so the sign
    # is on record, not hidden inside "matches expected form: false".
    expected_angle = -2 * theta
    R_expected = Matrix(
        [
            [cos(expected_angle), -sin(expected_angle), 0],
            [sin(expected_angle), cos(expected_angle), 0],
            [0, 0, 1],
        ]
    )
    matches_expected_form = simplify(R - R_expected) == sp.zeros(3, 3)
    return {
        "R_symbolic": str(R),
        "expected_rotation_by_minus_4pi_over_p": str(R_expected),
        "matches_expected_form_up_to_orientation_sign": bool(matches_expected_form),
        "Ad_is_identity_condition": "4*pi/p == 0 (mod 2*pi), sign irrelevant to this "
        "condition  <=>  p divides 2  <=>  p in {1,2}",
    }


# ---------------------------------------------------------------------------
# T2 -- exact matrix-identity check of the transformation laws for
# left-invariant vs right-invariant vector fields, on CONCRETE non-diagonal
# sample points g (adversarial: not just g=I).
#
#   X_A(g) := g*A        (left-invariant field generated by A in su(2))
#   Y_A(g) := A*g        (right-invariant field generated by A in su(2))
#
# Claim to verify as EXACT matrix identities, for zeta = zeta_p, for each
# tested p, at a genuinely non-trivial sample point g0 (not the identity):
#   (L_zeta)_* X_A (g0)  ==  X_A(zeta*g0)                      [no twist]
#   (L_zeta)_* Y_A (g0)  ==  Y_{Ad(zeta) A}(zeta*g0)           [Ad-twisted]
#
# (L_zeta)_* acting on a vector v in T_{g0}G, represented concretely as
# v = g0 * A (left-invariant realization) or v = A * g0 (right-invariant
# realization), pushes forward under left multiplication by zeta simply as
# left-multiplication of the representative matrix by zeta (since L_zeta is
# itself left matrix multiplication, a LINEAR map on the ambient matrix
# space, so its differential at any point is literally "multiply by zeta"
# in these matrix coordinates).
# ---------------------------------------------------------------------------


def sample_su2_point() -> Matrix:
    """A concrete, non-identity, non-diagonal point of SU(2): rotate by a
    generic angle phi about the x-axis (sigma1), i.e. g0 = cos(phi/2) I -
    i sin(phi/2) sigma1, at phi = pi/3 (60 degrees) -- arbitrary but fixed
    and manifestly not on the diagonal torus, so this is a genuine
    adversarial check, not a special/degenerate point."""
    phi = sp.pi / 3
    g0 = cos(phi / 2) * eye(2) - I * sin(phi / 2) * sigma1
    return simplify(g0)


def transformation_law_check(p: int) -> dict:
    z = zeta(p)
    g0 = sample_su2_point()
    Ad_z = adjoint_matrix(z)

    out = {}
    for name, A in [("sigma1", sigma1), ("sigma2", sigma2), ("sigma3", sigma3)]:
        # Left-invariant field: X_A(g) = g*A.
        lhs_left = simplify(z * (g0 * A))  # (L_zeta)_* X_A(g0) = zeta*g0*A
        rhs_left = simplify((z * g0) * A)  # X_A(zeta*g0) = (zeta*g0)*A
        left_twist_free = simplify(lhs_left - rhs_left) == sp.zeros(2, 2)

        # Right-invariant field: Y_A(g) = A*g.
        lhs_right = simplify(z * (A * g0))  # (L_zeta)_* Y_A(g0) = zeta*A*g0

        # Y_{Ad(zeta)A}(zeta*g0) with Ad(zeta)A represented back in the
        # Pauli basis, then plugged into Y_B(g)=B*g at g=zeta*g0.
        # Ad(zeta)A = zeta*A*zeta^{-1} directly (matrix form, no basis
        # decomposition needed for this identity check).
        B = simplify(z * A * z.inv())
        rhs_right = simplify(B * (z * g0))

        right_matches_Ad_twist = simplify(lhs_right - rhs_right) == sp.zeros(2, 2)

        out[name] = {
            "left_invariant_no_twist": bool(left_twist_free),
            "right_invariant_matches_Ad_twist": bool(right_matches_Ad_twist),
        }
    out["Ad_zeta_matrix"] = str(Ad_z)
    return out


# ---------------------------------------------------------------------------
# T3 -- edge cases p=1 (trivial) and p=2 (degenerate, zeta=-I central).
# T1 continued -- concrete sweep p = 2,3,4,5 (T4/pi_1 noted alongside).
# ---------------------------------------------------------------------------


def sweep(ps) -> dict:
    results = {}
    for p in ps:
        z = zeta(p)
        R = adjoint_matrix(z)
        R_id = is_identity(R)
        angle = None
        if not R_id:
            angle = rotation_angle_about_z_numeric(R)
        z_is_central = simplify(z - eye(2)) == sp.zeros(2, 2) or simplify(z + eye(2)) == sp.zeros(
            2, 2
        )
        results[p] = {
            "zeta_p": str(z),
            "zeta_p_is_central_(+-I)": bool(z_is_central),
            "Ad_zeta_p": str(R),
            "Ad_is_identity": bool(R_id),
            "rotation_angle_about_z_numeric_radians_if_nontrivial": angle,
            "freeness": {str(k): v for k, v in freeness_check(p).items()},
            "pi1_L(p,1)": f"ZZ_{p}" if p > 1 else "0 (p=1: no quotient, L(1,1)=S^3)",
        }
    return results


# ---------------------------------------------------------------------------
# Step 5 -- cross-check against this project's own abstract structure-
# constant convention (round72/E7: [Z_i,Z_j] = c*eps_ijk*Z_k, c=2).
# Not load-bearing (the matrix computation above is self-contained and
# already exact) -- this only confirms the two pictures agree.
# ---------------------------------------------------------------------------


def structure_constant_cross_check() -> dict:
    c = sp.Integer(2)  # project's established value (E2/round72)
    # ad(Z3) acting on span{Z1,Z2,Z3}: [Z3,Z1]=c*Z2, [Z3,Z2]=-c*Z1, [Z3,Z3]=0.
    ad_Z3 = Matrix([[0, -c, 0], [c, 0, 0], [0, 0, 0]])
    # exp(theta * ad_Z3) should match the SO(3)-rotation-by-(c*theta) picture
    # up to the normalization convention; here we only check the STRUCTURAL
    # claim that ad(Z3) generates rotation in the (1,2) plane and vanishes
    # identically on Z3 -- i.e. the abstract picture has the same qualitative
    # shape (an so(3)-type generator fixing one axis) as the concrete Ad(zeta)
    # computed above, independent of the group-level normalization/period
    # (which the abstract structure-constant convention alone cannot fix).
    fixes_z3_axis = (ad_Z3[2, :] == sp.zeros(1, 3)) and (ad_Z3[:, 2] == sp.zeros(3, 1))
    is_so3_generator_shape = simplify(ad_Z3 + ad_Z3.T) == sp.zeros(3, 3)  # antisymmetric
    return {
        "ad_Z3_matrix": str(ad_Z3),
        "fixes_the_quotient_axis": bool(fixes_z3_axis),
        "is_antisymmetric_so3_generator_shape": bool(is_so3_generator_shape),
        "note": "qualitative cross-check only; group-level periodicity (which "
        "p give central zeta_p) requires the concrete matrix realization "
        "above and is NOT re-derived from the abstract structure constants "
        "alone.",
    }


def main() -> None:
    ps = [1, 2, 3, 4, 5]
    results = {
        "general_p_derivation": general_p_derivation(),
        "concrete_sweep": sweep(ps),
        "transformation_law_checks": {p: transformation_law_check(p) for p in [2, 3, 4, 5]},
        "structure_constant_cross_check": structure_constant_cross_check(),
    }

    # ---- Verdict logic, exactly mirroring claim.md's pre-registered table ----
    sweep_r = results["concrete_sweep"]
    ad_id_flags = {p: sweep_r[p]["Ad_is_identity"] for p in [2, 3, 4, 5]}
    p3_asym = not ad_id_flags[3]
    all_p345_asym = all(not ad_id_flags[p] for p in [3, 4, 5])
    p2_trivial_as_expected = ad_id_flags[2]  # should be True (central)

    left_no_twist_all = all(
        results["transformation_law_checks"][p][name]["left_invariant_no_twist"]
        for p in [2, 3, 4, 5]
        for name in ["sigma1", "sigma2", "sigma3"]
    )
    right_matches_all = all(
        results["transformation_law_checks"][p][name]["right_invariant_matches_Ad_twist"]
        for p in [2, 3, 4, 5]
        for name in ["sigma1", "sigma2", "sigma3"]
    )

    if not left_no_twist_all or not right_matches_all:
        verdict = "K3_INTERNAL_INCONSISTENCY"
    elif not p2_trivial_as_expected:
        verdict = "K4_P2_ANOMALY_UNEXPLAINED"
    elif all_p345_asym:
        verdict = "HOLONOMY-ASYMMETRY-CONFIRMED-ALL-P"
    elif p3_asym and not all_p345_asym:
        verdict = "HOLONOMY-ASYMMETRY-ONLY-AT-P3"
    else:
        verdict = "NO-ASYMMETRY-FOUND"

    results["verdict"] = verdict
    results["verdict_inputs"] = {
        "Ad_identity_flags_p2_p3_p4_p5": ad_id_flags,
        "left_invariant_no_twist_holds_for_all_tested": left_no_twist_all,
        "right_invariant_matches_Ad_twist_for_all_tested": right_matches_all,
    }

    print(json.dumps(results, indent=2, default=str))

    with open("results_c167.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=str, ensure_ascii=False)


if __name__ == "__main__":
    main()
