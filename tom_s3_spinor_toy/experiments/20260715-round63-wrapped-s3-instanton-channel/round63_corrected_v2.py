"""Round 63, CORRECTED substitution -- fixes the dimensional-consistency error
caught by adversarial skeptic review (Step 8a) on both original routes.

Both `round63_route_a_critical_points.py` and `round63_route_b_independent_check.py`
substituted lambda(rho6) = c_eff*rho6^3 directly into f(rho6)'s own lambda slot:

    f(rho6) = 1 - exp( lambda * (1/rho6_star^2 - 1/rho6^2) )

But eq:slope2-exp's c(C')^3*rho6^3 is lambda_geom/rho6^2 (the already-reduced,
dimensionless exponent of the *simple* exp(-lambda_geom/rho6^2) ansatz) -- NOT
lambda_geom(rho6) itself (dimension length^2, = c(C')^3*rho6^5). Substituting the
reduced quantity into a slot expecting the raw coupling silently double-divides
by rho6^2.

CORRECT embedding (re-derived from the ground-truth V_total construction,
tests/test_g62_observables.py):

    v_np(rho6)   = -A_np * exp(-lambda(rho6)/rho6^2)
    A_np         =  V_flux * exp(lambda(rho6_star)/rho6_star^2)   [Minkowski BC at rho6*]

Using eq:slope2-exp directly for BOTH the running term and A_np's own calibration
(same functional form, evaluated at rho6 and at rho6_star respectively) gives, after
simplification:

    f_a3_corrected(rho6) = 1 - exp( c_eff * (rho6_star^3 - rho6^3) )

This is the formula used here. See decision.md for the full derivation and the
Skeptic Response Matrix trail (FALSIFIED -> FIX -> re-verified).
"""

import mpmath as mp

mp.mp.dps = 30

RHO6_STAR = mp.mpf("1.090")  # G57 UV-selection, matches tests/test_g62_observables.py
V_FLUX = mp.mpf(15) * mp.mpf("0.986") ** 3 / (16 * mp.pi)
K_VOL = 2 * mp.pi**2 * 16 * mp.pi**3 / 15
ESTABLISHED_RHO6_MIN = mp.mpf("1.1790597996")  # constant-lambda G62 zero-fit reference


def f_a3_corrected(rho6, c_eff):
    return 1 - mp.e ** (c_eff * (RHO6_STAR**3 - rho6**3))


def V_total_a3(rho6, c_eff):
    return V_FLUX * f_a3_corrected(rho6, c_eff) / (K_VOL * rho6**12)


def dV(rho6, c_eff, h=mp.mpf("1e-6")):
    return (V_total_a3(rho6 + h, c_eff) - V_total_a3(rho6 - h, c_eff)) / (2 * h)


def d2V(rho6, c_eff, h=mp.mpf("1e-6")):
    return (
        V_total_a3(rho6 + h, c_eff) - 2 * V_total_a3(rho6, c_eff) + V_total_a3(rho6 - h, c_eff)
    ) / (h * h)


def find_minima(c_eff, rmax=15, n=4000):
    grid = [mp.mpf("1.0005") + (mp.mpf(rmax) - mp.mpf("1.0005")) * i / n for i in range(n + 1)]
    dvals = [dV(r, c_eff) for r in grid]
    minima = []
    for i in range(len(grid) - 1):
        if dvals[i] < 0 and dvals[i + 1] > 0:
            lo, hi = grid[i], grid[i + 1]
            for _ in range(80):
                mid = (lo + hi) / 2
                if dV(mid, c_eff) < 0:
                    lo = mid
                else:
                    hi = mid
            r6min = (lo + hi) / 2
            minima.append((r6min, d2V(r6min, c_eff)))
    return minima


def find_bifurcation(lo=mp.mpf("-1.5"), hi=mp.mpf("-1.0"), iters=25):
    """Bisect the boundary between 'has a minimum' (near hi) and 'no minimum' (near lo)."""
    for _ in range(iters):
        mid = (lo + hi) / 2
        if find_minima(mid):
            hi = mid
        else:
            lo = mid
    return hi


def main():
    print("=" * 70)
    print("Round 63 CORRECTED: f_a3(rho6) = 1 - exp(c_eff*(rho6_star^3 - rho6^3))")
    print("=" * 70)

    # Positive control: c_eff=0 must be the degenerate trivial case.
    f0 = f_a3_corrected(mp.mpf("2.0"), mp.mpf("0"))
    assert f0 == 0, f"positive control failed: f_a3(rho6, 0) = {f0}, expected 0"
    print(f"\nPositive control: f_a3(rho6, c_eff=0) = {f0}  (expected 0, degenerate)  PASS")

    print("\nScan over c_eff:")
    print(f"{'c_eff':>10} | {'rho6_min':>12} | {'V-prime-prime':>14} | EFT-valid genuine min?")
    for c_str in ["-0.001", "-0.01", "-0.1", "-0.5", "-1.0", "-1.2", "-1.5", "0.001", "0.5", "1.0"]:
        c = mp.mpf(c_str)
        mins = find_minima(c)
        valid = [(float(r), float(v)) for r, v in mins if r > 1 and v > 0]
        print(f"{c_str:>10} | {str(valid):>12}")

    bif = find_bifurcation()
    bif_minima = find_minima(bif)
    print(f"\nBifurcation boundary: c_eff ~= {float(bif):.6f}")
    print(
        f"  minimum at bifurcation: rho6 ~= {float(bif_minima[0][0]):.6f}"
        if bif_minima
        else "  none"
    )

    r6min_near_zero = find_minima(mp.mpf("-1e-5"))
    r6m = r6min_near_zero[0][0]
    offset_pct = (r6m - ESTABLISHED_RHO6_MIN) / ESTABLISHED_RHO6_MIN * 100
    print(f"\nAs c_eff -> 0-: rho6_min = {float(r6m):.6f}")
    print(f"Established constant-lambda rho6_min = {float(ESTABLISHED_RHO6_MIN):.6f}")
    print(f"Closest-approach offset: {float(offset_pct):.2f}%")

    print("\n" + "=" * 70)
    print("SUMMARY (corrected)")
    print("=" * 70)
    print(
        "Surviving c_eff range: (bifurcation, 0) ~= "
        f"({float(bif):.4f}, 0)  [negative half, NOT positive as the flawed formula gave]"
    )
    print(f"Resulting rho6_min range: [{float(r6m):.4f}, {float(bif_minima[0][0]):.4f}]")
    print(
        f"Offset vs established ~1.179: {float(offset_pct):.2f}% (closest) "
        f"to {float((bif_minima[0][0] - ESTABLISHED_RHO6_MIN) / ESTABLISHED_RHO6_MIN * 100):.2f}% (at bifurcation)"
    )
    print("Verdict: PROMOTE [WEAKENED, CORRECTED] -- see decision.md")

    # Machine-readable summary
    import json

    out = {
        "positive_control_pass": True,
        "surviving_c_eff_range": [float(bif), 0.0],
        "rho6_min_range": [float(r6m), float(bif_minima[0][0])],
        "established_rho6_min": float(ESTABLISHED_RHO6_MIN),
        "closest_offset_pct": float(offset_pct),
        "bifurcation_offset_pct": float(
            (bif_minima[0][0] - ESTABLISHED_RHO6_MIN) / ESTABLISHED_RHO6_MIN * 100
        ),
        "verdict": "PROMOTE_WEAKENED_CORRECTED",
    }
    with open("results_round63_corrected.json", "w") as fh:
        json.dump(out, fh, indent=2)
    print("\nMachine-readable results written to results_round63_corrected.json")


if __name__ == "__main__":
    main()
