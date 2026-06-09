"""Reduced matrix-element helpers for the Option B coupling scaffold.

Scope:
    The functions here provide analytic SU(2) triple-harmonic normalization
    factors for the working left-invariant (J_L,J_R)=(1,0) scaffold.

    The invariant coframe normalization used downstream is the exact direct
    Haar/unit-coframe convention on S3. The Ben Achour E/E' basis mapping
    remains a separate representation detail and is kept explicit in metadata.
"""

from __future__ import annotations

import math
from typing import Any

from s3_spinor_spectral_labels import generate_spectral_spinor_records


DIRECT_HAAR_ONE_FORM_SCALE = 1.0
TEMPORARY_ENGINEERING_ONE_FORM_SCALE = DIRECT_HAAR_ONE_FORM_SCALE
TEMPORARY_ENGINEERING_ALPHA = DIRECT_HAAR_ONE_FORM_SCALE

NORMALIZATION_STATUS = "ANALYTIC_DIRECT_HAAR_CONVENTION"
FINAL_BEN_ACHOUR_NORMALIZATION = "unresolved"


def _triangle_allowed(j_a: float, j_b: float, j_c: float, tol: float = 1e-12) -> bool:
    return (
        abs(j_a - j_b) <= j_c + tol
        and j_c <= j_a + j_b + tol
        and abs((j_a + j_b + j_c) - round(j_a + j_b + j_c)) < tol
    )


def compute_reduced_V_element(
    j_L: float,
    j_R: float,
    j_L_prime: float,
    j_R_prime: float,
    J_L: float = 1.0,
    J_R: float = 0.0,
    radius: float = 1.0,
) -> float:
    """Return the working reduced coefficient for the left-invariant scaffold.

    The coefficient uses the normalized Wigner-D triple-product factor:

        sqrt((2 j_L + 1)(2 J_L + 1) / (2 j_L' + 1))

    together with the right-factor analogue. For the working Option B choice
    ``(J_L,J_R)=(1,0)``, the right factor enforces ``j_R'=j_R``.

    The returned value is independent of magnetic labels. It uses the exact
    direct Haar/unit-coframe scale ``1`` and intentionally does not include
    the final Ben Achour one-form reduced normalization.
    """
    if radius <= 0:
        raise ValueError(f"radius must be positive, got {radius!r}")
    if J_L != 1.0 or J_R != 0.0:
        raise NotImplementedError("Only the working left-invariant (J_L,J_R)=(1,0) case is implemented")
    if abs(j_R_prime - j_R) > 1e-12:
        return 0.0
    if j_L == 0.0 and j_L_prime == 0.0:
        return 0.0
    if not _triangle_allowed(j_L, J_L, j_L_prime):
        return 0.0

    left_factor = math.sqrt((2.0 * j_L + 1.0) * (2.0 * J_L + 1.0) / (2.0 * j_L_prime + 1.0))
    right_factor = math.sqrt((2.0 * j_R + 1.0) * (2.0 * J_R + 1.0) / (2.0 * j_R_prime + 1.0))
    return float(TEMPORARY_ENGINEERING_ONE_FORM_SCALE * left_factor * right_factor / radius)


def reduced_elements_for_kmax1(radius: float = 1.0) -> dict[tuple[float, float, float, float], float]:
    """Return all nonzero working reduced coefficients appearing through k_max=1."""
    elements: dict[tuple[float, float, float, float], float] = {}
    records = generate_spectral_spinor_records(k_max=1, radius=radius)
    labels = [
        (
            float(record["su2_L_label"]["j"]),
            float(record["su2_R_label"]["j"]),
        )
        for record in records
    ]

    for j_L, j_R in labels:
        for j_L_prime, j_R_prime in labels:
            value = compute_reduced_V_element(
                j_L=j_L,
                j_R=j_R,
                j_L_prime=j_L_prime,
                j_R_prime=j_R_prime,
                radius=radius,
            )
            if value != 0.0:
                elements[(j_L, j_R, j_L_prime, j_R_prime)] = value
    return elements


def reduced_element_metadata() -> dict[str, Any]:
    """Return metadata that prevents over-claiming the current coefficients."""
    return {
        "normalization_status": NORMALIZATION_STATUS,
        "final_ben_achour_normalization": FINAL_BEN_ACHOUR_NORMALIZATION,
        "one_form_scale": DIRECT_HAAR_ONE_FORM_SCALE,
        "engineering_alpha": TEMPORARY_ENGINEERING_ALPHA,
        "J_L": 1.0,
        "J_R": 0.0,
        "basis": "direct Haar-normalized Wigner-D triple-product factor",
        "not_included": "final Ben Achour E/E' basis mapping",
        "claim_scope": "engineering smoke tests only; no quantitative physics claims",
    }
