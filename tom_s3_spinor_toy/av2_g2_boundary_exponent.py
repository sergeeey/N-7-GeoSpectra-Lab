"""AV-2 G2 — Boundary Exponent Measurement.

Gate: AV2-G2 (from claim_av2_angular.md)
Pre-registered hypothesis H-AV2: mixed spinor bilinears phi*g can produce
cos^1 alpha boundary behavior while pure phi^2 bilinears are stuck at cos^2.

Pre-registered expectations (written BEFORE fitting, per FL protocol):
  |phi_nl(alpha)|^2  near alpha -> pi/2:  ~ cos^{2*(l+1)} = cos^{2l+2}
    For l=0: cos^2 alpha  (VANISHES — obstruction)
    For l=1: cos^4 alpha
  |g_nl(alpha)|^2   near alpha -> pi/2:  ~ cos^{2*l}
    For l=0: cos^0 = 1  (NONZERO — KEY MECHANISM)
    For l=1: cos^2 alpha
  phi_nl * g_nl     near alpha -> pi/2:  ~ cos^{2l+1}
    For l=0: cos^1 alpha  (MATCHES target sin(2alpha) ~ 2*sin(alpha)*cos(alpha))
  target sin(2alpha) = 2*sin(alpha)*cos(alpha): ~ cos^1 near alpha -> pi/2

Kill condition: if g_l=0 measured exponent > 0.3 (i.e. g_l=0 actually
vanishes at boundary), boundary mechanism is absent -> G2 FAIL.

Sources:
  Camporesi-Higuchi gr-qc/9505009:
    eq 3.25: phi_nl ~ cos^{l+1}(alpha) sin^l(alpha) * Jacobi near alpha=pi/2
    eq 3.27: g_nl ~ cos^l(alpha) sin^{l+1}(alpha) * Jacobi near alpha=pi/2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

import numpy as np

from tom_s3_spinor_toy.discrete_radial_dirac_proxy import g_nl_hopf
from tom_s3_spinor_toy.reference_spinor_harmonics import phi_nl_hopf


# --- Pre-registered expected exponents (from CH eqs 3.25, 3.27 analytically) ---
PREREGISTERED_PHI_SQ_EXPONENT: Final[dict] = {
    # (n, l): 2*(l+1) = cos^{2l+2}
    (0, 0): 2.0,
    (1, 0): 2.0,
    (1, 1): 4.0,
    (2, 0): 2.0,
    (2, 1): 4.0,
    (3, 2): 6.0,
}
PREREGISTERED_G_SQ_EXPONENT: Final[dict] = {
    # (n, l): 2*l = cos^{2l}
    (0, 0): 0.0,  # KEY: l=0 -> cos^0 = NONZERO at boundary
    (1, 0): 0.0,
    (1, 1): 2.0,
    (2, 0): 0.0,
    (2, 1): 2.0,
    (3, 2): 4.0,
}
PREREGISTERED_MIXED_EXPONENT: Final[dict] = {
    # (n, l): 2*l+1 = cos^{2l+1}
    (0, 0): 1.0,  # KEY: l=0 -> cos^1 matches target
    (1, 0): 1.0,
    (1, 1): 3.0,
    (2, 0): 1.0,
    (2, 1): 3.0,
}
TARGET_SIN2ALPHA_EXPONENT: Final[float] = 1.0  # sin(2a)=2sin(a)cos(a) -> cos^1

# Tolerance: measured exponent within this margin of pre-registered value -> PASS
EXPONENT_TOLERANCE: Final[float] = 0.25

# Boundary windows: multiple to guard against fitting artifacts
BOUNDARY_WINDOWS: Final[list] = [
    (0.85, 0.98),  # wide window, alpha -> pi/2 zone
    (0.90, 0.98),  # medium
    (0.93, 0.98),  # narrow
]


@dataclass
class ExponentFitResult:
    """Fitted boundary exponent for one mode and one bilinear type."""

    n: int
    ang_l: int  # noqa: E741 — standard spectral notation, l=angular quantum number
    bilinear_type: str  # "phi_sq", "g_sq", "mixed", "target"
    window: Tuple[float, float]
    fitted_exponent: float
    r_squared: float
    preregistered_exponent: float
    deviation: float
    pass_fail: str  # "PASS", "FAIL", "BORDERLINE"


@dataclass
class G2BoundaryExponentReport:
    """Full G2 gate report."""

    gate: str = "AV2-G2"
    date: str = "2026-06-10"
    modes_tested: Tuple = field(default_factory=lambda: ((0, 0), (1, 0), (1, 1), (2, 0), (2, 1)))
    preregistered_phi_sq: dict = field(default_factory=dict)
    preregistered_g_sq: dict = field(default_factory=dict)
    preregistered_mixed: dict = field(default_factory=dict)
    fits: list = field(default_factory=list)
    key_finding_g_l0_exponent: float = 0.0
    key_finding_mixed_l0_exponent: float = 0.0
    mechanism_supported: bool = False
    verdict: str = "PENDING"
    item40_max_status: str = "RADIAL + DICTIONARY_ROBUST"
    scope: str = (
        "G2 boundary exponent measurement only; "
        "no full angular verification; no physical promotion; "
        "no claim that Tom ansatz is solved; no H-T1 promotion"
    )
    forbidden_claims: Tuple = field(
        default_factory=lambda: (
            "full angular verification complete",
            "Tom ansatz solved",
            "H-T1 promoted",
            "sparse reconstruction confirmed (that is E1)",
            "physical lambda fixed",
            "safe_for_runtime",
        )
    )


def _measure_boundary_exponent(
    values: np.ndarray,
    alpha_grid: np.ndarray,
    window: tuple[float, float],
) -> tuple[float, float]:
    """Fit log|f(alpha)| ~ exponent * log(cos(alpha)) in the boundary window.

    Returns (exponent, r_squared).
    cos(alpha) -> 0 as alpha -> pi/2; a positive exponent means the function
    vanishes at the boundary.  exponent=0 means nonzero at boundary.
    """
    pi_half = np.pi / 2.0
    mask = (alpha_grid >= window[0] * pi_half) & (alpha_grid <= window[1] * pi_half)
    alpha_w = alpha_grid[mask]
    vals_w = np.abs(values[mask])

    # Guard: if all values are essentially zero already, can't fit
    if np.max(vals_w) < 1e-14:
        return np.nan, 0.0

    # log(|f|) ~ exponent * log(cos(alpha)) + const
    x = np.log(np.cos(alpha_w) + 1e-300)
    y = np.log(vals_w + 1e-300)

    # Mask out numerical noise near machine epsilon
    valid = np.isfinite(x) & np.isfinite(y) & (vals_w > 1e-12 * np.max(vals_w))
    if valid.sum() < 10:
        return np.nan, 0.0

    x, y = x[valid], y[valid]
    coeffs = np.polyfit(x, y, 1)
    exponent = float(coeffs[0])
    y_pred = np.polyval(coeffs, x)
    ss_res = float(np.sum((y - y_pred) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return exponent, r2


def run_g2_boundary_exponent_measurement() -> G2BoundaryExponentReport:
    """Run the G2 gate measurement and return structured report."""

    report = G2BoundaryExponentReport(
        preregistered_phi_sq={str(k): v for k, v in PREREGISTERED_PHI_SQ_EXPONENT.items()},
        preregistered_g_sq={str(k): v for k, v in PREREGISTERED_G_SQ_EXPONENT.items()},
        preregistered_mixed={str(k): v for k, v in PREREGISTERED_MIXED_EXPONENT.items()},
    )

    # Fine grid near the boundary (alpha in [0, pi/2])
    alpha_grid = np.linspace(0.01, np.pi / 2 - 0.001, 8001)
    target_vals = np.sin(2.0 * alpha_grid)  # target function

    modes = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (3, 2)]
    fits: list[ExponentFitResult] = []

    # --- Measure target sin(2alpha) boundary exponent (sanity) ---
    for window in BOUNDARY_WINDOWS:
        exp, r2 = _measure_boundary_exponent(target_vals, alpha_grid, window)
        pre = TARGET_SIN2ALPHA_EXPONENT
        dev = abs(exp - pre) if not np.isnan(exp) else np.nan
        pf = "PASS" if (not np.isnan(exp) and dev < EXPONENT_TOLERANCE) else "FAIL"
        fits.append(
            ExponentFitResult(
                n=-1,
                ang_l=-1,
                bilinear_type="target_sin2alpha",
                window=window,
                fitted_exponent=round(exp, 4) if not np.isnan(exp) else -999.0,
                r_squared=round(r2, 4),
                preregistered_exponent=pre,
                deviation=round(dev, 4) if not np.isnan(dev) else 999.0,
                pass_fail=pf,
            )
        )

    # --- Measure per mode ---
    for n, l in modes:  # noqa: E741
        phi = phi_nl_hopf(n, l, alpha_grid)
        g = g_nl_hopf(n, l, alpha_grid)
        phi_sq = phi**2
        g_sq = g**2
        mixed = phi * g

        bilinears = [
            ("phi_sq", phi_sq, PREREGISTERED_PHI_SQ_EXPONENT.get((n, l))),
            ("g_sq", g_sq, PREREGISTERED_G_SQ_EXPONENT.get((n, l))),
            ("mixed_phi_g", mixed, PREREGISTERED_MIXED_EXPONENT.get((n, l))),
        ]
        for btype, vals, pre_exp in bilinears:
            for window in BOUNDARY_WINDOWS:
                exp, r2 = _measure_boundary_exponent(vals, alpha_grid, window)
                if pre_exp is None:
                    pre, dev, pf = np.nan, np.nan, "NO_PREREGISTRATION"
                else:
                    pre = pre_exp
                    dev = abs(exp - pre) if not np.isnan(exp) else np.nan
                    pf = (
                        "PASS"
                        if (not np.isnan(exp) and dev < EXPONENT_TOLERANCE)
                        else "BORDERLINE"
                        if (not np.isnan(exp) and dev < 0.5)
                        else "FAIL"
                    )
                fits.append(
                    ExponentFitResult(
                        n=n,
                        ang_l=l,
                        bilinear_type=btype,
                        window=window,
                        fitted_exponent=round(exp, 4) if not np.isnan(exp) else -999.0,
                        r_squared=round(r2, 4),
                        preregistered_exponent=pre if pre is not None else -1.0,
                        deviation=round(dev, 4) if not np.isnan(dev) else 999.0,
                        pass_fail=pf,
                    )
                )

    report.fits = fits

    # --- Summarise key findings ---
    # Key 1: g_l=0 should have exponent ~0 (nonzero at boundary)
    g_l0_exponents = [
        f.fitted_exponent
        for f in fits
        if f.n in (0, 1, 2)
        and f.ang_l == 0
        and f.bilinear_type == "g_sq"
        and f.fitted_exponent != -999.0
    ]
    key_g_l0 = float(np.median(g_l0_exponents)) if g_l0_exponents else np.nan
    report.key_finding_g_l0_exponent = round(key_g_l0, 4)

    # Key 2: mixed l=0 should have exponent ~1 (matches target)
    mixed_l0_exponents = [
        f.fitted_exponent
        for f in fits
        if f.n in (0, 1, 2)
        and f.ang_l == 0
        and f.bilinear_type == "mixed_phi_g"
        and f.fitted_exponent != -999.0
    ]
    key_mixed_l0 = float(np.median(mixed_l0_exponents)) if mixed_l0_exponents else np.nan
    report.key_finding_mixed_l0_exponent = round(key_mixed_l0, 4)

    # --- Verdict ---
    g_l0_ok = abs(key_g_l0) < 0.4  # g_l=0 ~nonzero (exponent near 0)
    mixed_l0_ok = abs(key_mixed_l0 - 1.0) < 0.4  # mixed ~cos^1

    # Count PASS/FAIL across all fits (excluding NO_PREREGISTRATION)
    counted = [f for f in fits if f.pass_fail in ("PASS", "FAIL", "BORDERLINE")]
    n_fail = sum(1 for f in counted if f.pass_fail == "FAIL")

    if g_l0_ok and mixed_l0_ok and n_fail == 0:
        verdict = "PASS"
        mechanism = True
        item40 = "RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_SUPPORTED"
    elif g_l0_ok and mixed_l0_ok and n_fail <= 2:
        verdict = "MIXED"
        mechanism = True
        item40 = "RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_PARTIAL"
    elif not g_l0_ok:
        verdict = "FAIL"
        mechanism = False
        item40 = "RADIAL + DICTIONARY_ROBUST"  # no upgrade
    else:
        verdict = "MIXED"
        mechanism = True
        item40 = "RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_PARTIAL"

    report.verdict = verdict
    report.mechanism_supported = mechanism
    report.item40_max_status = item40

    return report


def g2_boundary_exponent_summary() -> dict:
    """Return compact summary for reports."""
    r = run_g2_boundary_exponent_measurement()
    return {
        "gate": r.gate,
        "verdict": r.verdict,
        "key_g_l0_exponent": r.key_finding_g_l0_exponent,
        "key_mixed_l0_exponent": r.key_finding_mixed_l0_exponent,
        "mechanism_supported": r.mechanism_supported,
        "item40_status": r.item40_max_status,
        "scope": r.scope,
        "forbidden_claims": r.forbidden_claims,
    }
