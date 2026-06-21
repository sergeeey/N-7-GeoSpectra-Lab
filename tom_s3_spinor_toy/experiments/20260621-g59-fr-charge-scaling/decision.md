# G59 decision — NULL (hard closed)

**Date:** 2026-06-21
**Verdict:** NULL
**Tests:** 18/18 PASS (0.34s)

## Result summary

| Gate | Result | Key value |
|------|--------|-----------|
| A1 PASS | ∂V_str/∂ρ₆ < 0 everywhere | 6/6 parametrized points |
| A2 PASS | factored form correct; inner factor > 0 | algebraic identity verified |
| B1 PASS | f₀_SM ≈ 4412, EH minimum shifts to ρ₆=1.00 | confirmed by brentq |
| B2 NULL | ratio f₀_SM/f₀ ≈ 15,420 >> KILL_RATIO=100 | 154× over threshold |
| C1 PASS | V_EH(ρ₆=1, f₀_SM) ≈ -29 (AdS, not Minkowski) | shallower than -520 |
| D1 PASS | ρ₆_min ∝ f₀^α, α ∈ [1.8, 2.8] scale ratio | power law confirmed |
| NULL PASS | |V_Cas/V_curv| < 10⁻⁴ at any charge | Casimir never relevant |

## What was falsified

"FR minimum can reach SM window with natural SM charges (q₃q₆=1)."

**Falsified:** shifting the FR minimum to ρ₆≈1 requires f₀ ≈ 15,400× larger than the SM-charge value. Even if achieved, the vacuum is still AdS (~-29).

## If REJECT: Kill Analysis

**Killed:** curvature-flux competition as a NATURAL stabilizer at SM scale.

**NOT killed:**
- G56 (KKLT-like NP stabilization) — uses non-perturbative terms, different mechanism
- Physical reality of FR minimum at ρ₆≈0.337 for q₃q₆=1 (it's a genuine 4D AdS vacuum)
- Future: change of charge normalization convention (but ratio ~10⁴ is robust to factors of π)

## Chain closure: G54–G59

| Gate | Result | Mechanism | Status |
|------|--------|-----------|--------|
| G54-A | V_flux = const on SM constraint | Freund-Rubin | PASS |
| G54-D/E | ζ_FP 3 radii: min/UV-pole/zero | Casimir spectral | PASS |
| G54-F | Dine-Seiberg runaway (V_flux+V_Cas only) | EH rescaling | PASS |
| G55 | V_flux_min = q₃q₆=1 | 2D system exact | PASS |
| G56 | KKLT AdS min at ρ₆*≈1.09 | NP term | PASS (2 free params) |
| G57 | UV-selection ray → ρ₆*≈1.09 | c_{1/2}=0 condition | PASS |
| G58 | V_curv min at ρ₆≈0.337, deep AdS | curvature + EH | NULL |
| **G59** | **f₀_SM/f₀≈15,400 >> 100** | **charge scaling** | **NULL** |

**Conclusion:** classical (curvature + flux) stabilization gives wrong scale. Only KKLT-like NP (G56) gives correct scale, with 2 free parameters.
