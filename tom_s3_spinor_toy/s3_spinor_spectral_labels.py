"""P1a spectral spinor label scaffold for the round three-sphere S3.

Scope:
    This module emits representation-level records that connect the exact P0
    Dirac spectrum to future spectral/Wigner-basis work. It does not construct
    spinor wavefunctions, a Dirac matrix, graph transport, gauge fields,
    instantons, index calculations, or zero-mode claims.

Representation scaffold:
    The clean S3 Dirac branches are represented as:
        positive: (j_L, j_R) = ((k + 1) / 2, k / 2)
        negative: (j_L, j_R) = (k / 2, (k + 1) / 2)

    Each branch then has dimension:
        (2 j_L + 1)(2 j_R + 1) = (k + 2)(k + 1)
"""

from __future__ import annotations

from typing import Any

from s3_dirac_exact_baseline import analytic_dirac_spectrum_s3


SUPPORTED_CONVENTIONS = {"ben_achour_displayed_phase"}


def _validate_convention(convention: str) -> None:
    if convention not in SUPPORTED_CONVENTIONS:
        supported = ", ".join(sorted(SUPPORTED_CONVENTIONS))
        raise ValueError(f"Unsupported convention {convention!r}; expected one of: {supported}")


def _su2_labels_for_branch(k: int, branch: str) -> tuple[dict[str, Any], dict[str, Any]]:
    if branch == "positive":
        j_left = (k + 1) / 2.0
        j_right = k / 2.0
    elif branch == "negative":
        j_left = k / 2.0
        j_right = (k + 1) / 2.0
    else:
        raise ValueError(f"Unknown branch {branch!r}")

    return (
        {
            "group": "SU(2)_L",
            "j": j_left,
            "dimension": int(2 * j_left + 1),
            "generator_axis": "L_z",
        },
        {
            "group": "SU(2)_R",
            "j": j_right,
            "dimension": int(2 * j_right + 1),
            "generator_axis": "R_z",
        },
    )


def generate_spectral_spinor_records(
    k_max: int,
    radius: float = 1.0,
    convention: str = "ben_achour_displayed_phase",
) -> list[dict[str, Any]]:
    """Generate spectral spinor branch records through ``k_max``.

    The returned records mirror the exact P0 spectrum and add SU(2)_L x SU(2)_R
    representation metadata for future spectral/Wigner-basis construction.
    """
    _validate_convention(convention)

    records: list[dict[str, Any]] = []
    for entry in analytic_dirac_spectrum_s3(k_max=k_max, radius=radius):
        branch = "positive" if entry["sign"] == "+" else "negative"
        su2_left, su2_right = _su2_labels_for_branch(entry["k"], branch)
        records.append(
            {
                "k": entry["k"],
                "branch": branch,
                "eigenvalue": entry["eigenvalue"],
                "degeneracy_per_branch": entry["degeneracy"],
                "su2_L_label": su2_left,
                "su2_R_label": su2_right,
                "convention": convention,
                "note": (
                    "P1a spectral label scaffold only; not a Dirac matrix, "
                    "not a numerical operator, not chirality, not an index claim."
                ),
            }
        )
    return records
