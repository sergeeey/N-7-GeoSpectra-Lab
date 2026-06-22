"""G84A: symbolic standard dimensional reduction of gauge kinetic terms."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g84a.json"

ALLOWED_VERDICTS = {
    "DERIVED_POSITIVE_POWER_STANDARD_ANSATZ",
    "DERIVED_INVERSE_SQUARE_STANDARD_ANSATZ",
    "MIXED_STANDARD_ANSATZ",
    "FAIL_REDUCTION",
}

D_EXTERNAL = 4
DIM_S3 = 3
DIM_S6 = 6
RHO3_POWER = 2
RHO6_POWER = 1


@dataclass(frozen=True)
class Sector:
    name: str
    wrapped_s3_dimensions: int
    wrapped_s6_dimensions: int


SECTORS = (
    Sector("BULK_S3XS6", DIM_S3, DIM_S6),
    Sector("LOCALIZED_S3", DIM_S3, 0),
    Sector("LOCALIZED_S6", 0, DIM_S6),
    Sector("POINT_LOCALIZED", 0, 0),
)


def volume_power(sector: Sector) -> int:
    """Power of rho6 after rho3=C*rho6^2 is imposed."""
    return (
        sector.wrapped_s3_dimensions * RHO3_POWER
        + sector.wrapped_s6_dimensions * RHO6_POWER
    )


def logarithmic_derivative_power(sector: Sector) -> int:
    """Independent symbolic extraction of d ln(V_sector) / d ln(rho6)."""
    rho6, c = sp.symbols("rho6 c", positive=True)
    rho3 = c * rho6**RHO3_POWER
    coefficient = rho3 ** sector.wrapped_s3_dimensions
    coefficient *= rho6 ** sector.wrapped_s6_dimensions
    return int(sp.simplify(rho6 * sp.diff(sp.log(coefficient), rho6)))


def weyl_power_in_omega(external_dimension: int, form_rank: int = 2) -> int:
    """Power under g_J=Omega^2*g_E for sqrt(g)|F_p|^2."""
    return external_dimension - 2 * form_rank


def required_prefactor_power(target_alpha: int, baseline_alpha: int) -> int:
    """Extra rho6 power required from dilaton/warp/duality prefactors."""
    return target_alpha - baseline_alpha


def run() -> dict:
    rows = []
    for sector in SECTORS:
        direct = volume_power(sector)
        derivative = logarithmic_derivative_power(sector)
        rows.append(
            {
                **asdict(sector),
                "direct_volume_alpha": direct,
                "log_derivative_alpha": derivative,
                "baseline_alpha": direct,
                "inverse_square_obtained": direct == -2,
                "prefactor_alpha_required_for_minus_two": required_prefactor_power(
                    -2, direct
                ),
            }
        )

    baseline_alphas = {
        row["name"]: row["baseline_alpha"]
        for row in rows
        if row["name"] != "POINT_LOCALIZED"
    }
    independent_methods_agree = all(
        row["direct_volume_alpha"] == row["log_derivative_alpha"] for row in rows
    )
    weyl_4d = weyl_power_in_omega(4)
    negative_control_5d = weyl_power_in_omega(5)
    any_inverse_square = any(row["inverse_square_obtained"] for row in rows)

    expected = {
        "BULK_S3XS6": 12,
        "LOCALIZED_S3": 6,
        "LOCALIZED_S6": 6,
    }
    positive_power_match = baseline_alphas == expected

    if (
        independent_methods_agree
        and positive_power_match
        and weyl_4d == 0
        and not any_inverse_square
    ):
        verdict = "DERIVED_POSITIVE_POWER_STANDARD_ANSATZ"
    elif any_inverse_square and independent_methods_agree and weyl_4d == 0:
        verdict = "DERIVED_INVERSE_SQUARE_STANDARD_ANSATZ"
    elif independent_methods_agree:
        verdict = "MIXED_STANDARD_ANSATZ"
    else:
        verdict = "FAIL_REDUCTION"

    gates = {
        "G84A-1_independent_power_methods_agree": independent_methods_agree,
        "G84A-2_expected_positive_powers": positive_power_match,
        "G84A-3_4d_yang_mills_weyl_invariant": weyl_4d == 0,
        "G84A-4_weyl_detector_negative_control": negative_control_5d != 0,
        "G84A-5_no_baseline_inverse_square": not any_inverse_square,
        "G84A-6_verdict_allowed": verdict in ALLOWED_VERDICTS,
    }

    return {
        "gate": "G84A",
        "verdict": verdict,
        "action_ansatz": (
            "unwarped product metric; constant dilaton/warp prefactor; "
            "zero-mode F_mu_nu only"
        ),
        "project_path": "rho3=C*rho6^2",
        "external_dimension": D_EXTERNAL,
        "sector_results": rows,
        "weyl_scaling": {
            "formula": "Omega^(d-2p) for sqrt(g)|F_p|^2",
            "form_rank": 2,
            "power_in_4d": weyl_4d,
            "negative_control_power_in_5d": negative_control_5d,
            "changes_rho6_power_in_4d": False,
        },
        "derived_baseline_alphas": baseline_alphas,
        "inverse_square_derived": any_inverse_square,
        "required_compensators": {
            "bulk_prefactor_alpha": required_prefactor_power(-2, 12),
            "s3_localized_prefactor_alpha": required_prefactor_power(-2, 6),
            "s6_localized_prefactor_alpha": required_prefactor_power(-2, 6),
        },
        "supports_lambda_np_pi_over_9": False,
        "supports_lambda_v_identity": False,
        "falsified_within_ansatz": [
            "4D Weyl rescaling alone converts positive volume power to -2",
            "standard constant-prefactor bulk or cycle reduction yields alpha=-2",
        ],
        "open_routes": [
            "rho-dependent dilaton prefactor",
            "warped cycle volume",
            "dual modulus or T-duality",
            "spectral determinant origin independent of gauge modulus",
        ],
        "next_gate": "G84B_SPECTRAL_EXPONENTIAL_ORIGIN",
        "gates": gates,
        "reproduction_commands": [
            "python tom_s3_spinor_toy/experiments/20260622-g84a-standard-gauge-reduction/g84a_standard_gauge_reduction.py",
            "python -m pytest tom_s3_spinor_toy/tests/test_g84a_standard_gauge_reduction.py -q",
        ],
    }


def main() -> int:
    result = run()
    RESULTS_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "derived_baseline_alphas": result["derived_baseline_alphas"],
                "required_compensators": result["required_compensators"],
                "gates": result["gates"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if all(result["gates"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
