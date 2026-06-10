"""AV-2 E2 — Angular Singlet Check.

Gate: AV2-E2 (from claim_av2_angular.md, precondition: E1 STRONG_PASS)
Pre-registration: experiments/.../claim_e2_angular_singlet.md (written BEFORE this code)

Question: Does the bilinear phi_{0,0}*g_{0,0} have a nonzero projection onto the
J=0 (SO(4) singlet) sector of the C-H eigenspinor bilinear algebra?

The n=l=0 C-H eigenspinor on S3 carries the SU(2)_L x SU(2)_R representation (1/2, 0).
The cross bilinear phi*g corresponds to the m_L=(+1/2, -1/2) state in (1/2)x(1/2).
By CG theory, this state has a nonzero singlet component iff
  C = <0,0 | 1/2,+1/2; 1/2,-1/2> != 0.

Pass: C^2 > 0  --> item40 -> RADIAL+ANGULAR_BILINEAR_SUPPORTED
Fail: C = 0   --> item40 -> FORMAL_FIT_ONLY

Scope guards (enforced by tests):
  - No claim "Tom ansatz solved"
  - No claim "full angular verification"
  - No H-T1 promotion
  - lambda = FREE_COUPLING_PARAMETER
  - safe_for_runtime = False
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Tuple

from sympy import Rational
from sympy.physics.quantum.cg import CG


# --- Pre-registered quantum numbers for n=l=0 C-H mode on S3 ---
# Upper component (phi): m_L = +1/2
# Lower component (g):   m_L = -1/2
# Both: j_L = 1/2, j_R = 0 (representation (1/2, 0) of SU(2)_L x SU(2)_R)
J_MODE: Rational = Rational(1, 2)
M_UPPER: Rational = Rational(1, 2)  # phi_{0,0} component
M_LOWER: Rational = Rational(-1, 2)  # g_{0,0} component
J_SINGLET: Rational = Rational(0)
M_SINGLET: Rational = Rational(0)


@dataclass
class E2AngularSingletReport:
    """Full E2 gate report."""

    gate: str = "AV2-E2"
    date: str = "2026-06-10"

    # CG coefficient: <j=0,m=0 | j1=1/2,m1=+1/2; j2=1/2,m2=-1/2>
    cg_exact: object = None  # sympy Rational/sqrt expression
    cg_float: float = 0.0  # numerical float value
    cg_squared: float = 0.0  # |C|^2

    # Antisymmetry check: <0,0|1/2,-1/2;1/2,+1/2> = -<0,0|1/2,+1/2;1/2,-1/2>
    cg_antisym_exact: object = None
    antisymmetry_verified: bool = False

    # Triplet component: <1,0|1/2,+1/2;1/2,-1/2> (should also be nonzero)
    cg_triplet_exact: object = None
    triplet_nonzero: bool = False

    verdict: str = "PENDING"
    item40_max_status: str = "RADIAL + TWO_COMPONENT_RECONSTRUCTION_SUPPORTED"
    scope: str = (
        "E2 angular singlet check: SU(2) CG decomposition for n=l=0 C-H mode only; "
        "no full angular verification; no physical promotion; "
        "no H-T1 promotion; no claim Tom ansatz solved"
    )
    forbidden_claims: Tuple = field(
        default_factory=lambda: (
            "full angular verification complete",
            "Tom ansatz solved",
            "H-T1 promoted",
            "lambda fixed",
            "safe_for_runtime",
            "physical V promoted",
        )
    )


def _compute_cg_exact(
    j1: Rational, m1: Rational, j2: Rational, m2: Rational, j: Rational, m: Rational
) -> object:
    """Compute Clebsch-Gordan coefficient <j,m | j1,m1; j2,m2> via sympy."""
    return CG(j1, m1, j2, m2, j, m).doit()


def run_e2_angular_singlet() -> E2AngularSingletReport:
    """Run the E2 gate and return structured report."""
    report = E2AngularSingletReport()

    # Primary: singlet CG coefficient <0,0 | 1/2,+1/2; 1/2,-1/2>
    cg_val = _compute_cg_exact(J_MODE, M_UPPER, J_MODE, M_LOWER, J_SINGLET, M_SINGLET)
    report.cg_exact = cg_val
    report.cg_float = float(cg_val)
    report.cg_squared = float(cg_val**2)

    # Antisymmetry: <0,0 | 1/2,-1/2; 1/2,+1/2> = -C (by SU(2) antisymmetry)
    cg_antisym = _compute_cg_exact(J_MODE, M_LOWER, J_MODE, M_UPPER, J_SINGLET, M_SINGLET)
    report.cg_antisym_exact = cg_antisym
    report.antisymmetry_verified = bool(cg_antisym == -cg_val)

    # Triplet: <1,0 | 1/2,+1/2; 1/2,-1/2> (should be nonzero: the cross term is mixed)
    cg_triplet = _compute_cg_exact(J_MODE, M_UPPER, J_MODE, M_LOWER, Rational(1), Rational(0))
    report.cg_triplet_exact = cg_triplet
    report.triplet_nonzero = float(cg_triplet**2) > 0

    # Verdict
    if report.cg_squared > 0:
        report.verdict = "PASS"
        report.item40_max_status = "RADIAL + ANGULAR_BILINEAR_SUPPORTED"
    else:
        report.verdict = "FAIL"
        report.item40_max_status = "FORMAL_FIT_ONLY"

    return report


def e2_angular_singlet_summary() -> dict:
    """Return compact summary for reports."""
    r = run_e2_angular_singlet()
    return {
        "gate": r.gate,
        "verdict": r.verdict,
        "cg_singlet_squared": r.cg_squared,
        "cg_singlet_float": r.cg_float,
        "antisymmetry_verified": r.antisymmetry_verified,
        "triplet_nonzero": r.triplet_nonzero,
        "item40_status": r.item40_max_status,
        "scope": r.scope,
    }
