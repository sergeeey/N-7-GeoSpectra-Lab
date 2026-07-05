# NULL: λ_np has no standard 10D non-perturbative origin (UV mechanism sweep)

**Date:** 2026-07-05
**Source experiment:** experiments/20260705-g103-kk-lambda-blindness/ (decision.md carries full Kill Analysis)
**Verdict:** REJECT the branch "derive λ_np in V_NP = A·exp(−λ_np/ρ₆²) from standard 10D sources"

## What was tested
Five source classes of non-perturbative exponentials in a 10D → 4D reduction on S³×S⁶:

| Class | Scaling obtained | Required |
|---|---|---|
| Euclidean branes on S⁶ cycles | exp(−c·ρ₆⁶) (only Vol; H_p(S⁶)=0, 0<p<6) | exp(−λ/ρ₆²) |
| Gaugino condensation | 1/g₄² ~ ρ₆⁶ → exp(−c·ρ₆⁶) | — |
| Worldline instantons | exp(−c·ρ₆) | — |
| Borel/resurgence of α′ series | exp(−c·ρ₆²/α′) — opposite sign | — |
| Non-geometric fluxes | polynomial, no exponential | — |

Every class yields a POSITIVE power of ρ₆ in the instanton action (or no exponential).
The ansatz form exp(−λ/ρ₆²) requires effective cycle dimension p = −2, which no
fundamental object in string/M-theory provides.

## Why this NULL is progress
Combined with G83–G86B (internal λ-map exhaustion) it upgrades
`lambda_np = FREE_COUPLING_PARAMETER` from "internal scan found nothing" to
"no standard UV mechanism can produce the coupling's functional form".
G103 adds the observable-level split: KK tower λ-blind (≤0.41% over 4×),
λ observable only via m_mod ∝ λ^0.493 and V_min ∝ λ.

## What this does NOT kill
- R⁴ gravitational saddle (∫√g·R⁴ ~ ρ₆⁻², correct power) → parked/20260705-r4-gravitational-saddle.md
- Two-modulus emergent T_eff ∝ 1/ρ₆² with torsion-constrained B(T,X) — requires new input
- Non-standard (nonlocal / resummed-determinant) UV sectors — outside the class

## Do NOT re-attempt without
a new condition naming which of the three survivors above is being activated,
per the Adaptive Iteration Branch Rule. Numerology matches to 0.337
(1/3, π/9, n/3, 4/(N(N+2)) all rejected this session) do not count as new conditions.
