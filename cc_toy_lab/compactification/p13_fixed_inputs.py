"""Frozen P13A–P13G inputs. Status claims are IMMUTABLE from P13H."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Literal

# --- P13A: V-operator ansatz registry (fixed) ---
P13A_STATUS: Final[str] = "fixed"
P13A_ANSATZ: Final[str] = "V_S3(x) = lambda * sum_{a,I} gamma^a A_a^I(x) T_I"

# --- P13B1: repaired spinor-state basis (fixed) ---
P13B1_STATUS: Final[str] = "fixed"
P13B1_LOW_MODE_PAIR: Final[tuple[int, int]] = (0, 1)
P13B1_MODE_LABELS: Final[tuple[str, str]] = ("scalar_spinor_j0", "harmonic_spinor_j1_E1")

# --- P13C: Ben Achour E_i / E'_i source identities (fixed) ---
P13C_STATUS: Final[str] = "fixed"
P13C_SOURCE: Final[str] = "ben_achour_lawrence_hopf_embedding"

# --- P13D: convention stack (fixed) ---
P13D_STATUS: Final[str] = "fixed"
P13D_HERMITICITY: Final[str] = "preserved"
P13D_GAMMA_BASIS: Final[str] = "dirac_chiral_4x4"
P13D_SU4_NORM: Final[str] = "trace_normalized_generators"

# --- P13E / P13F: no-go classification (fixed — do not overwrite) ---
P13E_STATUS: Final[str] = "fixed"
P13F_STATUS: Final[str] = "fixed"
P13E_REDUCED_COEFFICIENT_SCALE: Final[str] = "NORMALIZATION_DEPENDENT_NO_GO"

# --- P13G: handoff / limitations (fixed) ---
P13G_STATUS: Final[str] = "fixed"
P13G_LAMBDA: Final[str] = "FREE_COUPLING_PARAMETER"
P13G_RUNTIME: Final[str] = "research_only"
P13G_SAFE_FOR_RUNTIME: Final[bool] = False
P13G_SELECTION_RULES: Final[str] = "smoke_only"
P13G_PROMOTION: Final[str] = "forbidden_without_separate_gate"

AllowedConvention = Literal["CONV_HAAR_UNIT", "CONV_HAAR_HARMONIC_SQRT2"]


@dataclass(frozen=True)
class P13GHandoff:
    """Allowed state-normalization conventions (P13G record)."""

    conventions: tuple[AllowedConvention, ...] = (
        "CONV_HAAR_UNIT",
        "CONV_HAAR_HARMONIC_SQRT2",
    )
    note: str = (
        "Both conventions preserve L2 Haar unit norm for the constant mode; "
        "the harmonic low mode may carry an allowed relative amplitude sqrt(2) "
        "without breaking orthogonality on the smoke grid."
    )


P13G_HANDOFF = P13GHandoff()


def assert_p13_chain_fixed() -> None:
    """Guard: P13A–G statuses remain fixed before P13H runs."""
    assert P13A_STATUS == "fixed"
    assert P13B1_STATUS == "fixed"
    assert P13C_STATUS == "fixed"
    assert P13D_STATUS == "fixed"
    assert P13E_STATUS == "fixed"
    assert P13F_STATUS == "fixed"
    assert P13G_STATUS == "fixed"
    assert P13E_REDUCED_COEFFICIENT_SCALE == "NORMALIZATION_DEPENDENT_NO_GO"
    assert P13G_LAMBDA == "FREE_COUPLING_PARAMETER"
