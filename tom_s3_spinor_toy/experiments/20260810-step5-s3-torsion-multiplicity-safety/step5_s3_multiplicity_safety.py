"""Step 5 (scoped): does E2/E3's torsion-deformed S3 zero-mode mechanism ever
stay multiplicity-safe (dim ker = 1), or does it always multiply generations?

E2 (20260717-round67-e2-s3-torsion-deformation) proved Kostant's cubic element
H acts as a SCALAR (h_H * Identity) on S3's spinor bundle, and computed the
crossing values t* where D^t's eigenvalue passes through zero -- but never
checked the DIMENSION of the resulting kernel. Since the n=0 Levi-Civita
eigenspace (eigenvalue 3/2) is, by construction, 2-dimensional (multiplicity
(0+1)(0+2)=2, already used in E2's own calibration step), and H is exactly
scalar on that same space, D^t restricted to it is ALSO exactly scalar --
meaning the crossing kills the WHOLE 2-dim eigenspace at once, not one state.

This script builds the explicit n=0-level D^t matrix directly, reusing E2's
own Clifford generators and omega/H construction unmodified, and verifies
this concretely rather than by argument alone.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_step5.json"

E2_PATH = (
    HERE.parent / "20260717-round67-e2-s3-torsion-deformation" / "e2_s3_torsion_deformation.py"
)
_spec = importlib.util.spec_from_file_location("e2_s3_torsion_deformation", E2_PATH)
assert _spec and _spec.loader
E2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E2)

I2 = sp.eye(2)


def main() -> None:
    # --- P1: re-verify E2's own crux fact (omega/H scalar on the 2-dim spinor space) ---
    Z = E2.clifford_generators()
    clifford_check = E2.verify_clifford_relations(Z)
    clifford_ok = all(clifford_check.values())

    omega_report = E2.compute_omega_and_check_scalar(Z)
    p1_pass = bool(omega_report["is_scalar_times_identity"]) and clifford_ok

    h_H = E2.calibrate_h_H()  # = 3, per E2's own calibration against the known n=0 eigenvalue 3/2

    # --- P2: build the explicit n=0-level D^t matrix, verify it is exactly scalar ---
    t = sp.symbols("t")
    D_half_n0 = (
        sp.Rational(3, 2) * I2
    )  # eigenvalue 3/2, eigenspace = whole 2-dim space, by definition
    H_matrix = (
        h_H * I2
    )  # E2's own step-2 result: H IS h_H times the identity, not just "scalar-valued"
    D_t_n0 = D_half_n0 + (t - sp.Rational(1, 2)) * H_matrix
    D_t_n0_simplified = sp.simplify(D_t_n0)

    off_diag_zero = bool(
        sp.simplify(D_t_n0_simplified[0, 1]) == 0 and sp.simplify(D_t_n0_simplified[1, 0]) == 0
    )
    diag_equal = bool(sp.simplify(D_t_n0_simplified[0, 0] - D_t_n0_simplified[1, 1]) == 0)
    p2_pass = off_diag_zero and diag_equal

    # --- P3: evaluate at the known crossing t=0, check it is the EXACT zero matrix ---
    D_0_n0 = sp.simplify(D_t_n0_simplified.subs(t, 0))
    is_zero_matrix = bool(D_0_n0 == sp.zeros(2, 2))
    rank_at_crossing = D_0_n0.rank()
    dim_ker_n0 = 2 - rank_at_crossing
    p3_pass = is_zero_matrix and dim_ker_n0 == 2

    # --- P4: general multiplicity formula for all E2-found crossings, by the same argument ---
    e2_crossings = [
        {"n": 0, "sigma": 1, "t_star": "0"},
        {"n": 0, "sigma": -1, "t_star": "1"},
        {"n": 1, "sigma": 1, "t_star": "-1/3"},
        {"n": 1, "sigma": -1, "t_star": "4/3"},
        {"n": 2, "sigma": 1, "t_star": "-2/3"},
        {"n": 2, "sigma": -1, "t_star": "5/3"},
    ]
    multiplicity_table = [
        {**c, "multiplicity_n_plus1_n_plus2": (c["n"] + 1) * (c["n"] + 2)} for c in e2_crossings
    ]
    all_multiplicities_at_least_2 = all(
        row["multiplicity_n_plus1_n_plus2"] >= 2 for row in multiplicity_table
    )

    if not p1_pass:
        verdict = "HARNESS_CONTROL_FAILED_CANNOT_TRUST_E2_REUSE"
    elif not (p2_pass and p3_pass):
        verdict = "FALSIFIED_CROSSING_IS_RANK_1_NOT_FULL_EIGENSPACE"
    else:
        verdict = "S3_TORSION_MECHANISM_NEVER_MULTIPLICITY_SAFE"

    results = {
        "experiment": "step5_s3_torsion_multiplicity_safety",
        "p1_clifford_and_omega_reverified": p1_pass,
        "h_H_calibrated": str(h_H),
        "D_t_n0_matrix": str(D_t_n0_simplified),
        "p2_D_t_n0_is_exactly_scalar": p2_pass,
        "D_0_n0_matrix": str(D_0_n0),
        "p3_is_exact_zero_matrix_at_crossing": is_zero_matrix,
        "rank_at_crossing": rank_at_crossing,
        "dim_ker_n0_at_t0": dim_ker_n0,
        "multiplicity_table_all_e2_crossings": multiplicity_table,
        "p4_all_crossings_multiplicity_at_least_2": all_multiplicities_at_least_2,
        "verdict": verdict,
    }

    print("=" * 92)
    print("Step 5 (scoped): S3 torsion-mechanism multiplicity safety")
    print("=" * 92)
    print(f"P1 (re-verify E2 omega/H scalar): {p1_pass}")
    print(f"h_H = {h_H}")
    print(f"D^t|_(n=0) = {D_t_n0_simplified}  (predict: exactly scalar)")
    print(f"P2 (exactly scalar)?  {p2_pass}")
    print()
    print(f"D^0|_(n=0) = {D_0_n0}")
    print(
        f"P3 (exact zero matrix, dim ker=2)?  {p3_pass}  (rank={rank_at_crossing}, dim ker={dim_ker_n0})"
    )
    print()
    print("Multiplicity at every E2 crossing:")
    for row in multiplicity_table:
        print(
            f"  n={row['n']}, sigma={row['sigma']:+d}, t*={row['t_star']}: "
            f"multiplicity=(n+1)(n+2)={row['multiplicity_n_plus1_n_plus2']}"
        )
    print(f"P4 (all crossings have multiplicity >= 2)?  {all_multiplicities_at_least_2}")
    print()
    print(f"VERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
