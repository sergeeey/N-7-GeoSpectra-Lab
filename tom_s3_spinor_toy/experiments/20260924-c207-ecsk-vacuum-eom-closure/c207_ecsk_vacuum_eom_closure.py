r"""C207: close F6 for the C134/ECSK candidate -- does the frozen M4xS3xS6
background satisfy the vacuum Einstein equation Ric(g)=0 at the one point
(t=1/2) where C134's own torsion equation of motion is self-consistent?

This is a SYNTHESIS round, not a new derivation from scratch. It chains
three already-certified project facts:

  1. C134 (2026-09-02): in vacuum, for 4D-chiral fermion content, ECSK's
     torsion equation of motion forces T=0, hence t=1/2 -- the ONLY point
     where the torsion ansatz is self-consistent at all.
  2. KT-8 (certified 3x + literature): the full twisted Dirac operator has
     NO zero modes at t=1/2. So psi=0 there -- trivially, not
     approximately -- meaning the fermion stress tensor T_{MN} vanishes
     identically and the metric equation reduces to the PURE VACUUM
     Einstein equation Ric(g)=0, with no matter source to balance it.
  3. round111 (2026-07-17): the S3 factor's Ricci tensor (Killing-form
     metric) is Ricci^t(Z_a,Z_b) = 8t(1-t)*delta_ab, an Einstein metric;
     Scal_LC = 6 at the Levi-Civita point.

Plus one standard, textbook fact this round applies (not invents): the
Ricci tensor of a Riemannian product M4 x S3 x S6 is block-diagonal --
Ric(M4 x S3 x S6) = Ric(M4) (+) Ric(S3) (+) Ric(S6), with NO cross terms
(O'Neill, "Semi-Riemannian Geometry", Prop 7.44 or equivalent). This means
a single nonzero block is enough to make the TOTAL Ricci tensor nonzero,
regardless of what the S6 block turns out to be -- so this round does NOT
need to derive the nearly-Kahler S6 curvature to reach a conclusion.

Verified here (sympy, exact symbolic arithmetic, not re-derived from a
new geometric computation -- this is a consistency check on round111's
own already-published numbers):
  - Scal(t) = 3 * 8t(1-t) = 24t(1-t) matches round111's independently
    stated formula exactly (internal consistency, not a new derivation).
  - At t=1/2: Ric_S3 = 2 * I_3 (the 3x3 identity times 2), confirmed
    nonzero as a matrix (all three eigenvalues = 2 =/= 0), not just via
    its trace.
  - Therefore Ric(g) on the full M4 x S3 x S6 product is nonzero at
    t=1/2, REGARDLESS of the S6 block -- the vacuum Einstein equation
    Ric(g)=0 is violated.
  - Corollary check: Ric_S3's eigenvalue 8t(1-t) is manifestly homogeneous
    of degree -2 in an overall radius rescaling (Killing-form metric
    scales as rho^2, Ricci as 1/rho^2 times a fixed positive number here),
    so NO choice of rho_3 sets Ric_S3 to zero for any FINITE radius --
    the conclusion is radius-independent, not an artifact of the
    currently-used unit-radius convention.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

t, rho3 = sp.symbols("t rho3", real=True, positive=True)


def ricci_s3_eigenvalue(t_val: sp.Expr) -> sp.Expr:
    r"""round111: Ricci^t(Z_a,Z_b) = 8t(1-t)*delta_ab (unit-radius Killing-form metric)."""
    return 8 * t_val * (1 - t_val)


def scal_s3(t_val: sp.Expr) -> sp.Expr:
    r"""round111's own stated formula: Scal(t) = 24t(1-t)."""
    return 24 * t_val * (1 - t_val)


def main() -> None:
    checks = {}

    # --- Consistency check: trace(Ric_S3) == Scal(t), for a 3-dimensional
    # Einstein space Ric_ab = lambda*delta_ab, Scal = 3*lambda.
    lam = ricci_s3_eigenvalue(t)
    trace_from_eigenvalue = 3 * lam
    residual = sp.simplify(trace_from_eigenvalue - scal_s3(t))
    checks["trace_consistency_residual_should_be_zero"] = str(residual)
    checks["trace_consistency_holds"] = residual == 0

    # --- Evaluate at t=1/2 (KT-8's zero-fermion-content point).
    lam_at_half = sp.nsimplify(lam.subs(t, sp.Rational(1, 2)))
    checks["ricci_s3_eigenvalue_at_t_half"] = str(lam_at_half)
    checks["ricci_s3_eigenvalue_at_t_half_is_nonzero"] = lam_at_half != 0
    checks["ricci_s3_eigenvalue_at_t_half_is_positive"] = bool(lam_at_half > 0)

    ric_s3_matrix_at_half = lam_at_half * sp.eye(3)
    eigenvalues = ric_s3_matrix_at_half.eigenvals()
    checks["ric_s3_matrix_at_t_half"] = str(ric_s3_matrix_at_half)
    checks["ric_s3_matrix_eigenvalues"] = {str(k): v for k, v in eigenvalues.items()}
    checks["ric_s3_matrix_all_eigenvalues_nonzero"] = all(k != 0 for k in eigenvalues)

    scal_lc_check = sp.simplify(scal_s3(sp.Rational(1, 2)) - 6)
    checks["scal_lc_matches_round111_published_value_6"] = scal_lc_check == 0

    # --- Radius independence: rescale the Killing-form metric by rho3^2;
    # Ricci (a curvature, dimension 1/length^2) then scales as 1/rho3^2.
    # Confirm the eigenvalue, as a function of rho3, is never zero for any
    # finite positive rho3.
    lam_rescaled = lam_at_half / rho3**2
    checks["ricci_s3_eigenvalue_rescaled_by_radius"] = str(lam_rescaled)
    no_finite_positive_root = sp.solveset(sp.Eq(lam_rescaled, 0), rho3, domain=sp.S.Reals)
    checks["no_finite_rho3_sets_ricci_s3_to_zero"] = no_finite_positive_root == sp.EmptySet

    # --- Product-manifold conclusion: Ric(g) on M4 x S3 x S6 is
    # block-diagonal (standard fact, not computed here) -- a single
    # nonzero block (S3, just confirmed) makes the TOTAL Ricci nonzero,
    # independent of the S6 block's own value.
    checks["conclusion"] = (
        "Ric(S3) at t=1/2 is exactly 2*I_3, nonzero and positive-definite, "
        "for ANY finite S3 radius. Since Ric(M4 x S3 x S6) is block-diagonal "
        "(standard product-manifold fact), Ric(g) on the full frozen "
        "background is nonzero at t=1/2 -- the vacuum Einstein equation "
        "Ric(g)=0 is violated at the ONE point where C134's torsion "
        "equation is self-consistent and KT-8 guarantees zero fermion "
        "content. F6 for the ECSK+C134 candidate closes PARTIAL -> REJECT. "
        "The argument does not depend on the S6 block's own curvature value."
    )

    all_pass = (
        checks["trace_consistency_holds"]
        and checks["ricci_s3_eigenvalue_at_t_half_is_nonzero"]
        and checks["ricci_s3_eigenvalue_at_t_half_is_positive"]
        and checks["ric_s3_matrix_all_eigenvalues_nonzero"]
        and checks["scal_lc_matches_round111_published_value_6"]
        and checks["no_finite_rho3_sets_ricci_s3_to_zero"]
    )
    checks["all_pass"] = all_pass

    print("=" * 70)
    print("C207: closing F6 for the ECSK/C134 candidate")
    print("=" * 70)
    for key, value in checks.items():
        print(f"  {key}: {value}")

    out_path = Path(__file__).parent / "results_c207.json"
    out_path.write_text(json.dumps(checks, indent=2, default=str))


if __name__ == "__main__":
    main()
