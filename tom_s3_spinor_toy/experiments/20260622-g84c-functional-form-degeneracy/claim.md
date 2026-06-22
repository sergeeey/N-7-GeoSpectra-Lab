# G84C Claim — Functional-Form Degeneracy Negative Control

**Date:** 2026-06-22  
**Precondition:** G84A and G84B completed locally

## Hypothesis

The inverse-square exponential

`exp(-b / rho6^2)`

is distinguishable from positive-power alternatives such as

`exp(-a * rho6^6)` and `exp(-a * rho6^12)`

in the project's working region near `rho0 = 1.090`.

This gate is a negative control. It checks whether the chosen inverse-square
shape is a genuine functional choice or only a local reparameterization.

## Tested forms

- `f_inv(rho) = A_inv * exp(-b / rho^2)`
- `f_6(rho) = A_6 * exp(-a * rho^6)`
- `f_12(rho) = A_12 * exp(-a * rho^12)`
- optional power-law control

## Intervals

- narrow: `[1.05, 1.15]`
- project-relevant: `[0.9, 1.3]`
- wide: `[0.8, 1.5]`

## Allowed verdicts

- `FUNCTIONAL_FORM_DISTINGUISHABLE`
- `LOCAL_DEGENERACY_FOUND`
- `VALUE_ONLY_DEGENERACY_SLOPE_FAILS`
- `OPEN_MISSING_TOLERANCE`
- `MIXED`

## Pass conditions

Use `FUNCTIONAL_FORM_DISTINGUISHABLE` if the best-fit positive-power
alternatives miss the inverse-square target beyond the declared audit
threshold on the project-relevant interval.

Use `VALUE_ONLY_DEGENERACY_SLOPE_FAILS` if value matching at `rho0` is possible
but slope matching fails for positive coefficients.

## Falsifiers

- A positive-coefficient positive-power form matches both value and slope at
  `rho0`.
- The fitted positive-power shapes stay within the declared distinguishability
  threshold on the project-relevant interval.

## Analytic check

For `exp(-a * rho^6)` versus `exp(-b / rho^2)`:

- value matching at `rho0` gives `b = a * rho0^8`;
- slope matching at `rho0` gives `b = -3 * a * rho0^8`.

These cannot both hold for positive `a, b`.

## Reproduction

```bash
python tom_s3_spinor_toy/experiments/20260622-g84c-functional-form-degeneracy/g84c_functional_form_degeneracy.py
python -m pytest tom_s3_spinor_toy/tests/test_g84c_functional_form_degeneracy.py -q
```
