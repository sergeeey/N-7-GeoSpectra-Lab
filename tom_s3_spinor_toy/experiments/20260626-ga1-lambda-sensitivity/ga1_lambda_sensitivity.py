"""GA1: Lambda sensitivity analysis — how does m_mod/m_KK depend on lambda?

G91 fixed lambda=1/3 (free parameter, Bottleneck 1).
GA1 sweeps lambda in [0.15, 0.60] to answer:
  - Is 0.198% robust or highly sensitive to lambda?
  - Does the minimum in rho6 always exist?
  - What is the sensitivity coefficient d(ratio)/d(lambda)?

Claim: ratio m_mod/m_KK varies by less than one order of magnitude
across physically reasonable lambda in [0.20, 0.50].
"""

from __future__ import annotations

import json
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_ga1.json"

C_SM = 0.986
RHO6_STAR = 1.090
V_FLUX = 15 * C_SM**3 / (16 * pi)

VOL_S3_UNIT = 2 * pi**2
VOL_S6_UNIT = 16 * pi**3 / 15

N3, N6, D_EXT = 3, 6, 4

K_MAT = np.diag([float(N3), float(N6)]) + np.outer(
    [float(N3), float(N6)], [float(N3), float(N6)]
) / (D_EXT - 2)
PATH_TANGENT = np.array([2.0, 1.0])
PATH_K = float(PATH_TANGENT @ K_MAT @ PATH_TANGENT)  # = 90.0


def run_for_lambda(lam: float) -> dict | None:
    """Run full G91 calculation for a given lambda. Returns None if no minimum."""
    a_np = V_FLUX * exp(lam / RHO6_STAR**2)

    def v_path(rho6: float) -> float:
        num = V_FLUX - a_np * exp(-lam / rho6**2)
        denom = VOL_S3_UNIT * VOL_S6_UNIT * rho6**6 * rho6**6  # rho3=rho6^2 => rho3^3=rho6^6
        return num / denom

    def v_path_deriv2(rho6: float, step: float = 5e-4) -> float:
        return (v_path(rho6 + step) - 2 * v_path(rho6) + v_path(rho6 - step)) / step**2

    result = minimize_scalar(v_path, bounds=(0.5, 3.0), method="bounded")
    if not result.success:
        return None

    rho6_min = result.x
    v_min = v_path(rho6_min)

    # Require AdS minimum (V < 0) and positive curvature
    if v_min >= 0:
        return None
    vpp = v_path_deriv2(rho6_min)
    if vpp <= 0:
        return None

    m2_mod = rho6_min**2 * vpp / PATH_K

    # KK masses (verified S3/S6 spectra)
    rho3_min = rho6_min**2
    m_kk_s3 = 1.5 / rho3_min
    m_kk_s6 = 3.0 / rho6_min
    m_kk = min(m_kk_s3, m_kk_s6)
    kk_source = "S3" if m_kk_s3 < m_kk_s6 else "S6"

    ratio = sqrt(m2_mod / m_kk**2)

    return {
        "lambda": round(lam, 4),
        "rho6_min": round(rho6_min, 6),
        "rho3_min": round(rho3_min, 6),
        "v_min": float(v_min),
        "m2_mod": float(m2_mod),
        "m_kk": float(m_kk),
        "kk_source": kk_source,
        "ratio": float(ratio),
        "ratio_pct": float(ratio * 100),
        "minimum_exists": True,
    }


def main() -> None:
    lambdas = [0.15, 0.20, 0.25, 1.0 / 3.0, 0.40, 0.45, 0.50, 0.55, 0.60]

    rows = []
    for lam in lambdas:
        r = run_for_lambda(lam)
        if r is None:
            rows.append({"lambda": round(lam, 4), "minimum_exists": False})
        else:
            rows.append(r)

    # Find reference (lambda = 1/3)
    ref = next(r for r in rows if abs(r["lambda"] - 1.0 / 3.0) < 1e-3)
    ref_ratio = ref["ratio_pct"]

    # Compute spread across valid rows
    valid = [r for r in rows if r.get("minimum_exists")]
    ratios = [r["ratio_pct"] for r in valid]
    ratio_min = min(ratios)
    ratio_max = max(ratios)
    spread_factor = ratio_max / ratio_min

    # Sensitivity: d(ratio%)/d(lambda) via finite difference around 1/3
    lam_lo = next((r for r in rows if abs(r["lambda"] - 0.25) < 1e-6), None)
    lam_hi = next((r for r in rows if abs(r["lambda"] - 0.40) < 1e-6), None)
    sensitivity = None
    if lam_lo and lam_hi and lam_lo.get("minimum_exists") and lam_hi.get("minimum_exists"):
        sensitivity = (lam_hi["ratio_pct"] - lam_lo["ratio_pct"]) / (0.40 - 0.25)

    verdict = "ROBUST" if spread_factor < 3.0 else "SENSITIVE"

    results = {
        "gate": "GA1",
        "sweep": rows,
        "summary": {
            "reference_lambda": round(1.0 / 3.0, 6),
            "reference_ratio_pct": ref_ratio,
            "ratio_min_pct": ratio_min,
            "ratio_max_pct": ratio_max,
            "spread_factor": round(spread_factor, 3),
            "sensitivity_pct_per_unit_lambda": round(sensitivity, 4) if sensitivity else None,
            "verdict": verdict,
            "interpretation": (
                "ratio varies by <3x across lambda in [0.15,0.60] => Bottleneck 1 "
                "affects absolute value but not order-of-magnitude physics"
                if verdict == "ROBUST"
                else "ratio is highly sensitive to lambda => fixing lambda is critical"
            ),
        },
    }

    print(f"\n{'lambda':>8}  {'rho6_min':>10}  {'ratio%':>10}  {'kk_source':>10}  status")
    print("-" * 60)
    for r in rows:
        if not r.get("minimum_exists"):
            print(f"{r['lambda']:>8.4f}  {'—':>10}  {'—':>10}  {'—':>10}  NO MINIMUM")
        else:
            marker = " <-- ref" if abs(r["lambda"] - 1.0 / 3.0) < 1e-6 else ""
            print(
                f"{r['lambda']:>8.4f}  {r['rho6_min']:>10.4f}  "
                f"{r['ratio_pct']:>10.4f}  {r['kk_source']:>10}  OK{marker}"
            )

    print(f"\nSpread: {ratio_min:.4f}% — {ratio_max:.4f}%  (factor {spread_factor:.2f}x)")
    print(f"Sensitivity: {sensitivity:.4f} %/unit-lambda" if sensitivity else "")
    print(f"Verdict: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nResults → {RESULTS_PATH}")


if __name__ == "__main__":
    main()
