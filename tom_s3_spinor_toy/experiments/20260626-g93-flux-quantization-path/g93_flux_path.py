"""G93: Flux quantization as the origin of the path constraint rho3 = rho6^2.

Problem from G92: Casimir stabilizes S³ but the 2D minimum lands at rho3=0.32 < 1
(below string length). Supergravity EFT breaks down for rho < 1. The naive Casimir
result is NOT physically reliable.

Two tasks in G93:
  1. EFT validity map — show which region of (rho3, rho6) is safe (both > 1)
     and verify G91 minimum is inside the valid region.

  2. Flux quantization as path constraint — the S³ and S⁶ each carry quantized
     p-form flux. The quantization condition fixes INTEGER flux numbers N3, N6.
     We look for integer pairs (N3, N6) such that the 2D minimum satisfies
     rho3_min / rho6_min^2 ≈ 1 (recovering the G91 path).

Physical setup:
  The 4-form flux on S³ contributes to the potential as:
    V_flux_S3 = N3^2 / (VOL_S3^2 * rho3^6)   (flux energy density, S3 localized)
  Similarly for an additional flux on S⁶:
    V_flux_S6 = N6^2 / (VOL_S6^2 * rho6^12)   (S6 localized)

  The EXISTING V_FLUX in G91 corresponds to N3=1, N6=0 (only S3 flux).
  Here we test what happens when BOTH fluxes are quantized with integer N3, N6.

Claim: there exist integer (N3, N6) with N3/N6 = O(1) such that the unconstrained
2D minimum has rho3_min ≈ rho6_min^2 (within 5%).
"""

from __future__ import annotations

import json
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g93.json"

# G91 constants
C_SM = 0.986
LAM = 1.0 / 3.0
RHO6_STAR = 1.090

VOL_S3_UNIT = 2 * pi**2
VOL_S6_UNIT = 16 * pi**3 / 15

# G91 V_FLUX (identified with N3-type flux energy)
V_FLUX_G91 = 15 * C_SM**3 / (16 * pi)
A_NP_G91 = V_FLUX_G91 * exp(LAM / RHO6_STAR**2)

# EFT validity: both radii must be > EFT_MIN in string units
EFT_MIN = 1.0  # rho < 1 => sub-stringy, SUGRA invalid
EFT_WARN = 1.5  # comfortable EFT validity margin


# ---------------------------------------------------------------------------
# EFT validity check
# ---------------------------------------------------------------------------


def eft_status(rho3: float, rho6: float) -> str:
    if rho3 < EFT_MIN or rho6 < EFT_MIN:
        return "INVALID"
    if rho3 < EFT_WARN or rho6 < EFT_WARN:
        return "MARGINAL"
    return "VALID"


# ---------------------------------------------------------------------------
# Full potential with two independent flux sectors
# ---------------------------------------------------------------------------


def v_total_flux(
    rho3: float,
    rho6: float,
    n3: float,
    n6: float,
    c_cas: float = 0.0,
) -> float:
    """
    Two-flux potential:
      V_main:   G91 non-perturbative potential (S3 flux encoded in V_FLUX_G91 / A_NP_G91)
      V_s6flux: additional quantized S6 flux (scales as n6^2 / rho6^12)
      V_cas:    optional Casimir term (same as G92)

    V_s6flux represents e.g. a 6-form or product of lower-form fluxes threading S6.
    Coefficient chosen so that at n6=1, rho6=1 the S6 flux energy ~ V_FLUX_G91.
    """
    if rho3 <= 0.05 or rho6 <= 0.05:
        return 1e10

    # (v_main with n3=1 is subsumed into v_main_n3 below)

    # Additional S6 flux: V ~ n6^2 / (VOL_S6^2 * rho6^12)
    # Normalized so V_s6flux(n6=1, rho6=1) ~ V_FLUX_G91
    v_s6 = n6**2 * V_FLUX_G91 / (VOL_S3_UNIT * VOL_S6_UNIT * rho3**3 * rho6**12)

    # Additional S3 flux rescaling: n3 multiplies the existing S3 flux energy
    # V_main already has n3=1 encoded. Adding extra quanta: replace V_FLUX_G91 -> n3^2 * V_FLUX_G91
    v_main_n3 = (n3**2 * V_FLUX_G91 - A_NP_G91 * exp(-LAM / rho6**2)) / (
        VOL_S3_UNIT * VOL_S6_UNIT * rho3**3 * rho6**6
    )

    # Casimir term (from G92, optional)
    v_cas = c_cas / (VOL_S3_UNIT * VOL_S6_UNIT * rho3**4 * rho6**6)

    # Total: use v_main_n3 (n3-scaled) + v_s6 + v_cas
    return v_main_n3 + v_s6 + v_cas


def find_2d_min_flux(n3: float, n6: float, c_cas: float = 0.0) -> dict:
    """Find unconstrained 2D minimum for given flux quanta."""

    def objective(x: np.ndarray) -> float:
        r3, r6 = float(x[0]), float(x[1])
        return v_total_flux(r3, r6, n3, n6, c_cas)

    # Multi-start: avoid local minima
    best = None
    for r3_init in [0.8, 1.2, 1.5, 2.0]:
        for r6_init in [1.0, 1.2, 1.5]:
            x0 = np.array([r3_init, r6_init])
            res = minimize(
                objective,
                x0,
                method="L-BFGS-B",
                bounds=[(0.3, 6.0), (0.3, 6.0)],
                options={"ftol": 1e-14, "gtol": 1e-10, "maxiter": 3000},
            )
            if res.success and res.fun < (best["v"] if best else 1e10):
                best = {"v": res.fun, "x": res.x.copy()}

    if best is None or best["v"] >= 0:
        return {"success": False, "n3": n3, "n6": n6}

    rho3, rho6 = float(best["x"][0]), float(best["x"][1])
    ratio = rho3 / rho6**2

    # Hessian (diagonal only for quick mass estimate)
    h = 1e-4
    dv_rr = (
        objective([rho3 + h, rho6]) - 2 * objective([rho3, rho6]) + objective([rho3 - h, rho6])
    ) / h**2
    dv_66 = (
        objective([rho3, rho6 + h]) - 2 * objective([rho3, rho6]) + objective([rho3, rho6 - h])
    ) / h**2

    m2_s3 = rho3**2 * dv_rr / 7.5  # K_33 = 7.5 from G91 kinetic matrix
    m2_s6 = rho6**2 * dv_66 / 24.0  # K_66 = 24.0

    return {
        "success": True,
        "n3": n3,
        "n6": n6,
        "rho3": rho3,
        "rho6": rho6,
        "v_min": float(best["v"]),
        "rho3_over_rho6_sq": ratio,
        "path_deviation_pct": abs(ratio - 1.0) * 100,
        "eft_status": eft_status(rho3, rho6),
        "m_s3": float(sqrt(max(m2_s3, 0.0))),
        "m_s6": float(sqrt(max(m2_s6, 0.0))),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    print("\n=== G93: Flux quantization as path constraint ===\n")

    # Step 0: EFT validity of G91 and G92 minima
    print("Step 0: EFT validity check")
    g91_rho3, g91_rho6 = 1.3902, 1.1791
    g92_rho3, g92_rho6 = 0.3207, 1.7051
    print(f"  G91 min (rho3={g91_rho3}, rho6={g91_rho6}): {eft_status(g91_rho3, g91_rho6)}")
    print(
        f"  G92 min (rho3={g92_rho3}, rho6={g92_rho6}): {eft_status(g92_rho3, g92_rho6)} <-- EFT breakdown!"
    )
    print(f"  EFT requires rho3 > {EFT_MIN} AND rho6 > {EFT_MIN}")

    # Step 1: Scan integer (N3, N6) pairs
    print("\nStep 1: Scan flux quanta (N3, N6) for path recovery")
    print(
        f"  {'N3':>4} {'N6':>4} {'rho3':>8} {'rho6':>8} {'ratio':>8} {'dev%':>6} {'EFT':>8} {'V_min':>12}"
    )
    print("  " + "-" * 70)

    results = []
    # WHY include N6=0: baseline is G91 (only S3 flux)
    for n3 in [1, 2, 3]:
        for n6 in [0, 1, 2, 3, 4]:
            r = find_2d_min_flux(float(n3), float(n6))
            results.append(r)
            if r["success"]:
                flag = (
                    " <-- PATH RECOVERED"
                    if r["path_deviation_pct"] < 5.0 and r["eft_status"] != "INVALID"
                    else ""
                )
                print(
                    f"  {n3:>4} {n6:>4} {r['rho3']:>8.4f} {r['rho6']:>8.4f}"
                    f" {r['rho3_over_rho6_sq']:>8.4f} {r['path_deviation_pct']:>6.1f}%"
                    f" {r['eft_status']:>8} {r['v_min']:>12.4e}{flag}"
                )
            else:
                print(f"  {n3:>4} {n6:>4}  no valid minimum")

    # Step 2: Best candidate
    valid = [r for r in results if r.get("success") and r.get("eft_status") != "INVALID"]
    if valid:
        best = min(valid, key=lambda r: r["path_deviation_pct"])
        print("\nStep 2: Best path recovery candidate")
        print(
            f"  (N3={best['n3']}, N6={best['n6']}): deviation = {best['path_deviation_pct']:.2f}%"
        )
        print(f"  rho3={best['rho3']:.4f}, rho6={best['rho6']:.4f}, EFT={best['eft_status']}")

        # Compute ratio m_mod / m_KK at this minimum
        m_kk_s3 = 1.5 / best["rho3"]
        m_kk_s6 = 3.0 / best["rho6"]
        m_kk = min(m_kk_s3, m_kk_s6)
        m_mod = best["m_s6"]
        ratio_phys = m_mod / m_kk if m_kk > 0 else None
        if ratio_phys:
            print(f"  ratio m_mod/m_KK = {ratio_phys*100:.4f}%")
    else:
        best = None
        print("\nStep 2: No EFT-valid path recovery found in N3,N6 in [1,3]x[0,4]")

    summary = {
        "gate": "G93",
        "eft_check": {
            "g91_status": eft_status(g91_rho3, g91_rho6),
            "g92_status": eft_status(g92_rho3, g92_rho6),
            "conclusion": "G91 minimum is EFT-VALID; G92 Casimir minimum is EFT-INVALID (rho3<1)",
        },
        "flux_scan": results,
        "best_candidate": best,
        "interpretation": {
            "g92_problem": "Casimir pushes S3 into sub-stringy regime (rho3=0.32 < 1). Not physical.",
            "g93_question": "Does flux quantization (N3,N6) produce EFT-valid minimum on G91 path?",
            "verdict": (
                f"PATH RECOVERED at (N3={best['n3']},N6={best['n6']}), "
                f"dev={best['path_deviation_pct']:.1f}%, EFT={best['eft_status']}"
                if best and best["path_deviation_pct"] < 5.0
                else "Path NOT recovered by integer flux quanta in scanned range"
            ),
        },
    }

    RESULTS_PATH.write_text(json.dumps(summary, indent=2))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
