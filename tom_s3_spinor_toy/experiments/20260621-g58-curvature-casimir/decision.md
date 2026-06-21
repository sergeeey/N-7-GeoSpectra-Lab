# G58 decision — NULL

**Date:** 2026-06-21
**Verdict:** NULL (informative)
**Tests:** 13/13 PASS (0.72s)

## Result summary

| Gate | Result | Key value |
|------|--------|-----------|
| C1 PASS | V_curv^EH < 0, monotone | -(36.2 at ρ₆=1) |
| C2 PASS | Curvature dominates flux | ratio = 7.9×10⁴ |
| C3 PASS | Interior minimum exists | root found by brentq |
| C4 PASS | Minimum outside SM region | ρ₆_min ≈ 0.337 < 0.50 |
| C5 PASS | V_Cas negligible vs V_curv | ratio < 10⁻⁴ |
| C6 NULL | Deep AdS at wrong scale | V_min ≈ −520 |

## What was falsified

G58 tested: "V_curv vs V_Cas competition creates parameter-free minimum at SM scale."

**Falsified:** The minimum exists (C3 PASS) but at ρ₆ ≈ 0.337 — 3× below the Casimir window
[0.953, 1.447] and far from SM physics.

## What was NOT falsified

- G54-F's analysis is internally consistent (Dine-Seiberg in V_flux+V_Cas sector)
- V_curv^EH IS ρ₆-dependent and does compete with V_flux^EH
- A minimum exists in V_curv + V_flux — just at the wrong scale

## Open question

Why does G54-F omit V_curv^EH? Two hypotheses:

1. **Freund-Rubin on-shell cancellation:** In FR background, R_int is sourced by flux.
   The on-shell condition R_mn ∝ F² means V_curv and V_flux partially cancel. The
   RESIDUAL V_curv (after FR balance) might be of order V_Cas — this is untested (G59?).

2. **Convention:** G54-F treats V_Cas as the "quantum" correction to the FR background,
   while V_curv+V_flux are the classical background (already stabilized at tree level).
   Moduli stabilization is then about quantum corrections to a classical stable background.

## If REJECT: Kill Analysis

**Killed:** "V_curv alone (without on-shell FR correction) stabilizes at SM scale"

**NOT killed:**
- Existence of minimum in V_curv + V_flux (proved, at ρ₆≈0.34)
- Possibility that FR-corrected V_curv_residual stabilizes at SM scale (untested)
- G54-F's Casimir analysis (unaffected, different sector)

## Parked Pearl

| observation | falsifiable_prediction | trigger_condition | next_check |
|---|---|---|---|
| V_curv has minimum at ρ₆≈0.34, order 79,000× larger than V_flux | FR on-shell correction reduces V_curv by factor ~10⁵, making V_curv_residual ~ V_Cas | When FR EOM written explicitly for S³×S⁶ moduli space | G59 |
