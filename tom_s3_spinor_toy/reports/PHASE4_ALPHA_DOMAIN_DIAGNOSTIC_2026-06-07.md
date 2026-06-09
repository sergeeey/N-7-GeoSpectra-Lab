# Phase 4 Alpha-Domain Diagnostic — 2026-06-07

Status: lightweight convention diagnostic, not a theory verdict.

## Claim Under Skeptic Check

[HYPOTHESIS] The cot(2 alpha) imaginary inconsistency may be related to extending a half-domain Hopf-like measure/normalization factor to alpha in [0, pi].

## What This Diagnostic Verifies

[VERIFIED] On `alpha in (0, pi)`, excluding endpoints:

- `sin(alpha) cos(alpha)` is positive on `(0, pi/2)` and negative on `(pi/2, pi)`.
- `sin(2 alpha)` is positive on `(0, pi/2)` and negative on `(pi/2, pi)`.
- `sqrt(sin(2 alpha))` is real only where `sin(2 alpha) >= 0`.
- `sqrt(abs(sin(2 alpha)))` stays real across both open intervals.
- `cot(2 alpha)` is real on both open intervals but has poles/sign flips; by itself it is not imaginary.

## Numeric Summary

```json
{
  "sincos": {
    "min": -0.49999999841820014,
    "max": 0.49999999841820014,
    "mean": 6.821210263296961e-17,
    "negative_fraction": 0.5,
    "positive_fraction": 0.5,
    "zero_near_fraction": 0.0,
    "finite_fraction": 1.0,
    "alpha_min": 1e-06,
    "alpha_max": 3.141591653589793
  },
  "sin2": {
    "min": -0.9999999968364004,
    "max": 0.9999999968364004,
    "mean": 1.3642420526593922e-16,
    "negative_fraction": 0.5,
    "positive_fraction": 0.5,
    "zero_near_fraction": 0.0,
    "finite_fraction": 1.0,
    "alpha_min": 1e-06,
    "alpha_max": 3.141591653589793
  },
  "cot2": {
    "min": -499999.999868212,
    "max": 499999.9999993334,
    "mean": 6.55766052659601e-09,
    "negative_fraction": 0.5,
    "positive_fraction": 0.5,
    "zero_near_fraction": 0.0,
    "finite_fraction": 1.0,
    "alpha_min": 1e-06,
    "alpha_max": 3.141591653589793
  },
  "sqrt_sin2_real_fraction": 0.5,
  "sqrt_sin2_imaginary_fraction": 0.5,
  "sqrt_sin2_complex_has_imaginary_part_fraction": 0.5,
  "sqrt_abs_sin2_finite_fraction": 1.0
}
```

## Interval Summary

```json
{
  "left_0_to_pi_over_2": {
    "alpha_min": 1e-06,
    "alpha_max": 1.5707177831013721,
    "sin2_sign": "positive",
    "sqrt_sin2_type": "real",
    "sincos_sign": "positive"
  },
  "near_pi_over_2": {
    "alpha_center": 1.5707963267948966,
    "sin2_sign": "zero crossing",
    "sincos_sign": "zero crossing",
    "cot2": "pole / sign flip",
    "grid_points_near_center": 2
  },
  "right_pi_over_2_to_pi": {
    "alpha_min": 1.5708748704884208,
    "alpha_max": 3.141591653589793,
    "sin2_sign": "negative",
    "sqrt_sin2_type": "imaginary if principal complex sqrt is used",
    "sincos_sign": "negative"
  }
}
```

## Strongest Objection

[SKEPTIC] cot(2 alpha) itself is real on both open intervals and only has poles/sign flips; Tom's inconsistency may come from generator matching, not from a sqrt(sin(2 alpha)) or measure factor.

## Cheapest Falsification

[SKEPTIC] Obtain Tom's exact embedding, measure/Jacobian, I_1R differential operator, and the two coupled equations. If they do not use a sqrt-like sign-sensitive factor, this hypothesis weakens.

## Kill Criterion

[SKEPTIC] If Tom's exact measure is positive by construction and his alpha functions avoid sqrt(sin(2 alpha)) or any half-domain continuation, do not pursue this as the primary explanation.

## Interpretation Guardrail

[INFERRED] This result supports only a convention-level question:

```text
If Tom's alpha really spans [0, pi], is the S3 chart patch-wise, signed,
or using an absolute Jacobian/phase convention?
```

It does not show that Tom made an error, and it does not validate or refute
Covariant Compactification.

## Plot

Generated artifact:

```text
reports/PHASE4_ALPHA_DOMAIN_DIAGNOSTIC_2026-06-07.png
```
