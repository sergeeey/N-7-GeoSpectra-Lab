# G84B Decision — Spectral-Origin Inverse-Square Audit

**Date:** 2026-06-22  
**Verdict:** `PROPER_TIME_FORM_ONLY`

## Result

The repository does contain inverse-square spectral scaling:

- `S6` Dirac ground-state eigenvalues square to `9 / rho6^2`;
- the KK product spectrum contains an explicit `1 / rho6^2` term;
- the spectral-action and Casimir code uses heat-kernel / proper-time
  expressions with exponents of the form `exp(-t * c / rho6^2)`.

What it does not contain is the final bridge from that integrand-level form to
a fixed effective term

`A * exp(-lambda_np / rho6^2)`.

## Why this is not a bridge

The proper-time variable `t` is integrated over or left as a free kernel
parameter. The code does not fix `t` to a geometric constant and does not
perform a resummation or saddle computation that would turn the integrand into
the final non-perturbative exponential.

The determinant/zeta route also does not close the bridge. The available
finite-part computations are power-law or log-like after subtraction and Weyl
division, not an explicit effective inverse-square exponential.

## Coefficient status

- `lambda_np_fixed`: false
- `matches_pi_over_9`: false
- `matches_one_third`: false
- `lambda_v_connection_found`: false

The `pi/9` candidate remains a weak external hypothesis, not a spectral
derivation.

## Operator summary

- `S6_DIRAC_GROUND_STATE`: inverse-square at the eigenvalue-squared level;
- `PRODUCT_KK_SPECTRUM`: inverse-square term present in the mass formula;
- `SPECTRAL_ACTION_HEAT_KERNEL`: proper-time exponent present;
- `CASIMIR_ZETA_FINITE_PART`: zeta finite part present;
- `KKLT_ANSATZ_NP_TERM`: inverse-square exponential appears only as an ansatz.

## Consequences

- `SPECTRAL_BRIDGE_DERIVED` is not supported.
- `PROPER_TIME_FORM_ONLY` is the correct status.
- `lambda_V` remains separate from `lambda_np`.

## Next gate

`G84C_FUNCTIONAL_FORM_DEGENERACY`

Use the project working radius `rho0 = 1.090` to test whether the inverse-square
shape is distinguishable from positive-power alternatives on the relevant
intervals.

## Reproduction

```bash
python tom_s3_spinor_toy/experiments/20260622-g84b-spectral-origin-inverse-square/g84b_spectral_origin_inverse_square.py
python -m pytest tom_s3_spinor_toy/tests/test_g84b_spectral_origin_inverse_square.py -q
python -m pytest tom_s3_spinor_toy/tests/test_g84a_standard_gauge_reduction.py tom_s3_spinor_toy/tests/test_g83_gauge_kinetic_modulus_scaling.py tom_s3_spinor_toy/tests/test_g79b_lambda_bridge_feasibility.py tom_s3_spinor_toy/tests/test_g82_canonical_mass.py -q
python -m compileall -q tom_s3_spinor_toy
git diff --check
```
