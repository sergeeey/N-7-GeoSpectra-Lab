"""E2: Does a torsion deformation of the S3 Dirac operator ever produce a zero mode?

Context (see claim.md for full framing): KT-8 (experiments/20260615-g8-chirality-obstruction/,
reports/PROJECT_360_ROUND3_SYNTHESIS.md "KT-8" section) established
[VERIFIED-tool, VERIFIED-external-source Sire&Xu arXiv:2005.01448] that the full product
Dirac operator on S3xS6 has NO zero mode, because D_full^2 = D_S3^2 (x) 1 + 1 (x) D_S6,twisted^2
(Clifford product decoupling, exact algebraic identity) and D_S3's OWN spectrum
+-(n+3/2)/rho3 (n>=0) is bounded away from 0 -- this holds for the LEVI-CIVITA (torsion-free)
connection on S3.

This experiment asks: does deforming the S3 factor's connection away from Levi-Civita, using
the canonical one-parameter family of metric connections that exists on any naturally reductive
homogeneous space (Agricola, "Connections on naturally reductive spaces, their Dirac operator
and homogeneous models in string theory", arXiv:math/0202094, in this repo as
Agricola_2002_Dirac_naturally_reductive.pdf), ever produce ker(D_S3(t)) != 0?

S3 = SU(2) realized as G/H with G=SU(2), H = {e} (trivial) -- i.e. S3 viewed as a Lie group
with its bi-invariant metric, NOT as the symmetric-space presentation (SU(2)xSU(2))/SU(2)_diag
(that presentation is a symmetric space, [m,m] subset h, and Agricola's paper explicitly notes
ALL connections in the one-parameter family coincide for a symmetric space -- i.e. it gives NO
deformation freedom at all). The G/{e} presentation is the one that actually has [m,m] = g
(m = g since h = 0), so the family Nabla^t_X Y = t[X,Y] genuinely varies with t, torsion
T^t = (2t-1)[X,Y], vanishing (Levi-Civita) at t=1/2.

Key facts used from the PDF (page/eq refs to the arXiv v1 PDF read directly this session):
  - eq (5) (section 3.1): D^t psi = sum_i Z_i . Z_i(psi) + t . H . psi
    where H = (3/2) sum_{i<j<k} <[Z_i,Z_j]_m, Z_k> Z_i.Z_j.Z_k  is Kostant's "cubic element",
    a FIXED element of the Clifford algebra Cl(m) (purely algebraic, no differential/orbital
    dependence at all -- it does not know which Peter-Weyl / KK level the spinor lives in).
  - For M = G/{e} = SU(2) (dim m = n = 3): H has only ONE term (i,j,k)=(1,2,3), so
    H = (3c/2) * Z1.Z2.Z3 = (3c/2) * omega, where c := <[Z1,Z2]_m, Z3> is S3's single
    independent structure constant and omega = Z1 Z2 Z3 is Cl(3)'s volume element.
  - Theorem 4.2 (constant spinors): for a constant spinor psi (the j=0 / trivial Peter-Weyl
    block), D^t psi = t . H . psi (the orbital term sum Z_i.Z_i(psi) vanishes identically
    for constant psi), and (D^t)^2 psi = 9 t^2 [Q(rho_g,rho_g) - Q(rho_h,rho_h)] psi.

This script:
  1. [VERIFIED-tool] Builds Cl(3) explicitly via Pauli matrices and verifies the Clifford
     relations {Z_i,Z_j} = -2 delta_ij exactly (sympy, exact arithmetic).
  2. [VERIFIED-tool] Computes omega = Z1.Z2.Z3 and verifies it is EXACTLY a scalar multiple
     of the 2x2 identity matrix (this is the crux structural fact: for n=3 specifically,
     H is a pure scalar operator on the spinor factor, independent of the KK/Peter-Weyl
     level n, BECAUSE H has only one Clifford term and that term is the (central, scalar-
     on-any-irrep) volume element -- this is NOT true for higher-dimensional cosets like S6,
     where H has multiple terms and is not central).
  3. Calibrates the resulting scalar h_H using the project's OWN already-established
     [VERIFIED-sympy, G8/G4] S3 Dirac spectrum +-(n+3/2)/rho3 at n=0 (the constant-spinor /
     j=0 sector), via Theorem 4.2's D^t(constant) = t . h_H relation. This pins h_H up to an
     overall sign (an orientation/labeling convention, not a physical ambiguity).
  4. Builds the closed-form eigenvalue family D^t(n, sigma) = sigma*(n+3/2) + (t - 1/2)*h_H
     for n=0,1,2 and sigma = +-1 (this additive-shift form is a DIRECT, algebraically exact
     consequence of steps 1-3: since H acts as h_H * Identity on the WHOLE spinor Hilbert
     space -- not just the n=0 sector -- eq (5) forces D^t = D^{1/2} + (t-1/2)*h_H exactly,
     with NO further n-dependence beyond what is already in the known D^{1/2} spectrum).
  5. Scans t over [-2, 2] and reports every crossing (t where some D^t(n,sigma) = 0 exactly).

Honesty ledger (see claim.md for the full evidence-marker breakdown):
  - Steps 1-2 (Clifford relations, omega scalar): [VERIFIED-tool], exact symbolic computation,
    no external dependence beyond definitions.
  - eq (5) and Theorem 4.2 themselves: [VERIFIED-external-source] (read directly from the PDF
    this session, not from memory).
  - The "j=0 constant-spinor sector IS exactly the n=0, one specific sigma, sector of the
    known +-(n+3/2) ladder" identification: [INFERRED] -- justified by the multiplicity match
    (dim of constant-spinor space = dim(V_0)*dim(Delta_m) = 1*2 = 2, which equals the project's
    own established multiplicity (n+1)(n+2)=2 at n=0 for ONE sign), but not independently
    cross-checked against a second external source.
  - The claim that H = h_H*Identity therefore shifts EVERY n-level uniformly (not just n=0):
    [DEDUCTION, low-risk] -- a direct consequence of H being literally a scalar multiple of the
    identity MATRIX (step 2) combined with eq (5) being an exact operator identity valid for
    ANY spinor, not a representation-theoretic extrapolation.
  - Whether the generalized product-decoupling formula D_full^2 = D_S6,twisted^2 (x) 1 +
    1 (x) D_S3(t)^2 remains valid once the S3 factor's connection is torsion-deformed (not
    Levi-Civita): [INFERRED, NOT independently literature-verified for this generalized case] --
    see claim.md "What this does NOT mean" for the full caveat. This script does NOT compute
    the full product operator; it only establishes ker(D_S3(t)) for the S3 factor alone.
"""

from __future__ import annotations

import json

import numpy as np
import sympy as sp

I2 = sp.eye(2)


# ---------------------------------------------------------------------------
# Step 1-2: Cl(3) via Pauli matrices, Clifford relations, omega centrality/scalarity
# ---------------------------------------------------------------------------


def pauli_matrices() -> list[sp.Matrix]:
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def clifford_generators() -> list[sp.Matrix]:
    """Z_i = i*sigma_i, giving {Z_i,Z_j} = -2 delta_ij  (Cl(0,3) convention,
    matching Agricola's stated sign {Zi,Zj}=-delta_ij up to the same overall
    normalization ambiguity noted in the module docstring -- what matters
    structurally is only the SIGN of Z_i^2, not the exact numerical prefactor,
    since h_H is calibrated against known physics in step 3 regardless).
    """
    return [sp.I * s for s in pauli_matrices()]


def verify_clifford_relations(Z: list[sp.Matrix]) -> dict[str, bool]:
    """[VERIFIED-tool] Check {Z_i,Z_j} = -2 delta_ij Id exactly, all 6 pairs."""
    results = {}
    for i in range(3):
        for j in range(i, 3):
            anticomm = sp.simplify(Z[i] * Z[j] + Z[j] * Z[i])
            expected = -2 * I2 if i == j else sp.zeros(2, 2)
            results[f"Z{i + 1}Z{j + 1}_anticommutator_matches"] = bool(
                sp.simplify(anticomm - expected) == sp.zeros(2, 2)
            )
    return results


def compute_omega_and_check_scalar(Z: list[sp.Matrix]) -> dict[str, object]:
    """[VERIFIED-tool] omega = Z1.Z2.Z3; check it is a scalar multiple of I2 exactly."""
    omega = sp.simplify(Z[0] * Z[1] * Z[2])
    # is omega proportional to I2?
    off_diag_zero = bool(sp.simplify(omega[0, 1]) == 0 and sp.simplify(omega[1, 0]) == 0)
    diag_equal = bool(sp.simplify(omega[0, 0] - omega[1, 1]) == 0)
    scalar_value = sp.simplify(omega[0, 0]) if (off_diag_zero and diag_equal) else None
    # also check omega commutes with every Z_i (centrality), and omega^2
    commutes = {}
    for i in range(3):
        comm = sp.simplify(omega * Z[i] - Z[i] * omega)
        commutes[f"omega_commutes_Z{i + 1}"] = bool(comm == sp.zeros(2, 2))
    omega_sq = sp.simplify(omega * omega)
    return {
        "omega_matrix": omega,
        "is_scalar_times_identity": off_diag_zero and diag_equal,
        "scalar_value": scalar_value,
        "centrality_checks": commutes,
        "omega_squared": omega_sq,
        "omega_squared_is_identity": bool(sp.simplify(omega_sq - I2) == sp.zeros(2, 2)),
    }


# ---------------------------------------------------------------------------
# Step 3-4: calibrate h_H, build closed-form eigenvalue family
# ---------------------------------------------------------------------------


def calibrate_h_H(known_n0_eigenvalue: sp.Rational = sp.Rational(3, 2)) -> sp.Rational:
    """Calibrate h_H via Theorem 4.2: D^{1/2}(constant spinor) = (1/2)*h_H must equal
    the project's own already-established [VERIFIED-sympy, G8/G4] n=0 eigenvalue 3/2
    (WLOG choosing the '+' branch/sign convention -- the '-' branch just flips the
    overall sign of h_H, giving the mirror-symmetric result t <-> 1-t).
    """
    t_half = sp.Rational(1, 2)
    h_H = known_n0_eigenvalue / t_half
    return sp.nsimplify(h_H)


def eigenvalue_family(
    n: int,
    sigma: int,
    t: sp.Symbol | sp.Rational,
    h_H: sp.Rational,
    rho3: sp.Rational = sp.Integer(1),
) -> sp.Expr:
    """D^t(n,sigma) = sigma*(n+3/2)/rho3 + (t-1/2)*h_H/rho3."""
    return (sigma * (n + sp.Rational(3, 2)) + (t - sp.Rational(1, 2)) * h_H) / rho3


def crossing_t(
    n: int, sigma: int, h_H: sp.Rational, rho3: sp.Rational = sp.Integer(1)
) -> sp.Rational:
    """Solve eigenvalue_family(n,sigma,t,h_H,rho3) = 0 for t (rho3 cancels)."""
    t = sp.symbols("t")
    expr = eigenvalue_family(n, sigma, t, h_H, rho3)
    sols = sp.solve(sp.Eq(expr, 0), t)
    assert len(sols) == 1
    return sp.nsimplify(sols[0])


# ---------------------------------------------------------------------------
# Step 5: numeric scan for a sanity cross-check of the closed form
# ---------------------------------------------------------------------------


def numeric_scan(h_H_val: float, n_max: int = 2, t_range=(-2.0, 2.0), n_points: int = 4001) -> dict:
    """Independent numeric root-find (NOT reusing sympy's solve) on a dense grid, used
    purely as a cross-check that the closed-form crossing_t() formula was not mistyped.
    A grid point landing exactly ON a root (as happens here, since the true roots are
    rational and the grid spacing is also rational) can register as two adjacent
    "sign changes" around np.sign(0)==0; dedupe crossings within 1 grid-step of each
    other before comparing to the exact/symbolic answer.
    """
    ts = np.linspace(t_range[0], t_range[1], n_points)
    step = ts[1] - ts[0]
    crossings = []
    for n in range(n_max + 1):
        for sigma in (+1, -1):
            vals = sigma * (n + 1.5) + (ts - 0.5) * h_H_val
            roots_here = []
            for idx in range(len(ts) - 1):
                v0, v1 = vals[idx], vals[idx + 1]
                if v0 == 0.0:
                    roots_here.append(float(ts[idx]))
                elif v0 * v1 < 0.0:
                    t0, t1 = ts[idx], ts[idx + 1]
                    t_star = t0 - v0 * (t1 - t0) / (v1 - v0)
                    roots_here.append(float(t_star))
            # dedupe near-duplicate roots from adjacent-grid-point detection
            deduped: list[float] = []
            for r in sorted(roots_here):
                if not deduped or abs(r - deduped[-1]) > 2 * step:
                    deduped.append(r)
            for r in deduped:
                crossings.append({"n": n, "sigma": sigma, "t_star_numeric": r})
    return {"crossings": crossings}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> dict:
    Z = clifford_generators()
    clifford_check = verify_clifford_relations(Z)
    clifford_ok = all(clifford_check.values())

    omega_report = compute_omega_and_check_scalar(Z)
    omega_ok = (
        omega_report["is_scalar_times_identity"] and omega_report["omega_squared_is_identity"]
    )

    h_H = calibrate_h_H()

    n_levels = [0, 1, 2]
    sigmas = [1, -1]
    closed_form_crossings = []
    for n in n_levels:
        for sigma in sigmas:
            t_star = crossing_t(n, sigma, h_H)
            closed_form_crossings.append(
                {"n": n, "sigma": sigma, "t_star_exact": str(t_star), "t_star_float": float(t_star)}
            )
    closed_form_crossings.sort(key=lambda r: r["t_star_float"])

    numeric = numeric_scan(float(h_H), n_max=2, t_range=(-2.0, 2.0))
    numeric_ts = sorted(c["t_star_numeric"] for c in numeric["crossings"])
    exact_ts = sorted(c["t_star_float"] for c in closed_form_crossings)
    cross_check_max_abs_err = max(abs(a - b) for a, b in zip(numeric_ts, exact_ts))

    # crux verdict: does ANY crossing exist with |t - 1/2| finite (always true unless h_H=0)?
    any_zero_mode = h_H != 0 and len(closed_form_crossings) > 0

    result = {
        "step1_clifford_relations": clifford_check,
        "step1_clifford_relations_all_ok": clifford_ok,
        "step2_omega": {
            "matrix": str(omega_report["omega_matrix"]),
            "is_scalar_times_identity": omega_report["is_scalar_times_identity"],
            "scalar_value": str(omega_report["scalar_value"]),
            "centrality_checks": omega_report["centrality_checks"],
            "omega_squared": str(omega_report["omega_squared"]),
            "omega_squared_is_identity": omega_report["omega_squared_is_identity"],
        },
        "step2_omega_ok": omega_ok,
        "step3_h_H_calibrated": str(h_H),
        "step4_closed_form_crossings_sorted_by_t": closed_form_crossings,
        "step5_numeric_scan_cross_check": {
            "numeric_t_stars_sorted": numeric_ts,
            "exact_t_stars_sorted": exact_ts,
            "max_abs_error_numeric_vs_exact": cross_check_max_abs_err,
        },
        "verdict": {
            "clifford_and_omega_verified": clifford_ok and omega_ok,
            "numeric_exact_cross_check_passed": cross_check_max_abs_err < 1e-9,
            "any_t_gives_S3_zero_mode": bool(any_zero_mode),
            "label": (
                "PASS_CANDIDATE_MECHANISM_FOUND"
                if (clifford_ok and omega_ok and any_zero_mode)
                else "FAIL_OR_NULL"
            ),
        },
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    out_path = "results_e2.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nSaved: {out_path}")
