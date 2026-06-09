"""S6 / G2 / SU(3) formula-spec scaffold.

This module is a first-class contract for the separate S6 track. It is not an
operator implementation, not a spectrum computation, and not an SU(4)
interpretation layer.

The purpose is to make the S6 formulation explicit before any future numerical
or symbolic implementation:

- `S6 ≅ G2 / SU(3)`;
- reductive split `g2 = su(3) ⊕ m`;
- homogeneous Dirac / Casimir baseline;
- invariant-connection choice left explicit;
- no mixing with the validated S3 basis layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final


S6_HOMOGENEOUS_IDENTITY: Final[str] = "S6 ≅ G2 / SU(3)"
G2_REDUCTIVE_SPLIT: Final[str] = "g2 = su(3) ⊕ m"
DIRAC_CASIMIR_BASELINE: Final[str] = "D ~ C_G + (1/8) s"
TRACK_SCOPE: Final[str] = "S6 formula spec only; no implementation or spectrum claim"


@dataclass(frozen=True)
class S6FormulaSpec:
    """Minimal structured contract for the S6 track."""

    identity: str = S6_HOMOGENEOUS_IDENTITY
    reductive_split: str = G2_REDUCTIVE_SPLIT
    dirac_baseline: str = DIRAC_CASIMIR_BASELINE
    scope: str = TRACK_SCOPE
    metric_normalization: str = "undecided"
    connection_choice: str = "undecided"
    spinor_bundle_convention: str = "undecided"
    selection_rules_status: str = "not started"


def s6_formula_spec() -> S6FormulaSpec:
    """Return the current S6 formula-spec contract."""

    return S6FormulaSpec()


def s6_formula_spec_metadata() -> dict[str, str]:
    """Return a small metadata map for context and report generation."""

    spec = s6_formula_spec()
    return {
        "identity": spec.identity,
        "reductive_split": spec.reductive_split,
        "dirac_baseline": spec.dirac_baseline,
        "scope": spec.scope,
        "metric_normalization": spec.metric_normalization,
        "connection_choice": spec.connection_choice,
        "spinor_bundle_convention": spec.spinor_bundle_convention,
        "selection_rules_status": spec.selection_rules_status,
    }

