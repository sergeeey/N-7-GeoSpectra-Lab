"""Lawrence/Hopf S3 chart — fixed coordinate convention for P13H."""

from __future__ import annotations

import numpy as np

# Chart declaration (Lawrence/Hopf, rho = 1 on unit S3)
CHART_ID = "lawrence_hopf_unit_rho"
COORD_DOC = (
    "x1 = rho*sin(alpha)*cos(theta); "
    "x2 = rho*sin(alpha)*sin(theta); "
    "x3 = rho*cos(alpha)*sin(theta_tilde); "
    "x4 = rho*cos(alpha)*cos(theta_tilde)"
)
METRIC_DOC = "ds^2 = rho^2 * (dalpha^2 + sin(alpha)^2 dtheta^2 + cos(alpha)^2 dtheta_tilde^2)"
VOLUME_DOC = "dVol = rho^3 * sin(alpha) * cos(alpha) d_alpha d_theta d_theta_tilde"


def lawrence_hopf_coords(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
    rho: float = 1.0,
) -> np.ndarray:
    """Return (4,) embedding components at scalar or broadcast points."""
    sa = np.sin(alpha)
    ca = np.cos(alpha)
    ct = np.cos(theta)
    st = np.sin(theta)
    ctt = np.cos(theta_tilde)
    stt = np.sin(theta_tilde)
    return np.array(
        [
            rho * sa * ct,
            rho * sa * st,
            rho * ca * stt,
            rho * ca * ctt,
        ]
    )


def ben_achour_E_i(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
) -> np.ndarray:
    """P13C source-fixed embedding E_i (rho=1)."""
    return lawrence_hopf_coords(alpha, theta, theta_tilde, rho=1.0)


def ben_achour_E_prime_i(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
) -> np.ndarray:
    """P13C source-fixed tangent-projected E'_i identities."""
    sa = np.sin(alpha)
    ca = np.cos(alpha)
    ct = np.cos(theta)
    st = np.sin(theta)
    ctt = np.cos(theta_tilde)
    stt = np.sin(theta_tilde)
    return np.array(
        [
            ca * ct,
            ca * st,
            -sa * stt,
            -sa * ctt,
        ]
    )


def volume_weight(alpha: float | np.ndarray, rho: float = 1.0) -> float | np.ndarray:
    """Haar weight rho^3 sin(alpha) cos(alpha) — NOT sin^2(alpha)*sin(alpha)."""
    return (rho**3) * np.sin(alpha) * np.cos(alpha)


def total_s3_volume_analytic(rho: float = 1.0) -> float:
    """∫ dVol = 2*pi^2 * rho^3."""
    return 2.0 * np.pi**2 * (rho**3)
