# G84B Claim — Spectral-Origin Inverse-Square Audit

**Date:** 2026-06-22  
**Precondition:** G84A = `DERIVED_POSITIVE_POWER_STANDARD_ANSATZ`

## Hypothesis

The inverse-square non-perturbative shape

`exp(-lambda_np / rho6^2)`

may come from the repository's internal spectral structure rather than from a
standard KKLT gauge-kinetic modulus.

The strongest candidate route is spectral:

- KK, Dirac, Laplacian, or heat-kernel eigenvalues scale as `c / rho6^2`;
- proper-time expressions therefore contain `exp(-t * c / rho6^2)`;
- the audit checks whether that integrand-level form survives into a final
  effective term `A * exp(-lambda_np / rho6^2)`.

## Allowed verdicts

- `SPECTRAL_BRIDGE_DERIVED`
- `SPECTRAL_FORM_FOUND_COEFFICIENT_OPEN`
- `PROPER_TIME_FORM_ONLY`
- `NO_SPECTRAL_BRIDGE`
- `OPEN_MISSING_OPERATOR`
- `MIXED`

## Pass conditions for a true bridge

Use `SPECTRAL_BRIDGE_DERIVED` only if:

1. a concrete repository operator is identified;
2. its eigenvalues or eigenvalue squares scale as `c / rho6^2`;
3. the audit derives a final effective term proportional to
   `exp(-lambda_np / rho6^2)`;
4. `lambda_np` is fixed or geometrically constrained;
5. the result is not just a fitted ansatz or an integrand-level artifact.

## Falsifiers

- `exp(-t * c / rho6^2)` appears only inside proper-time integrals with free
  or integrated `t`.
- zeta/determinant finite parts give logs or powers instead of the final
  inverse-square exponential.
- `lambda_np` remains free.
- No operator-level bridge exists between the spectral candidate and the
  `lambda_v_operator` sector.

## Assumptions

- Repository formulas are evidence, not proof.
- Intermediate heat-kernel or proper-time exponents do not count as a final
  effective exponential unless the code derives the resummed result.
- Numerical closeness to `1/3` or `pi/9` is not sufficient by itself.

## Required artifacts

- deterministic audit script;
- machine-readable JSON result;
- decision record;
- focused pytest coverage.

## Reproduction

```bash
python tom_s3_spinor_toy/experiments/20260622-g84b-spectral-origin-inverse-square/g84b_spectral_origin_inverse_square.py
python -m pytest tom_s3_spinor_toy/tests/test_g84b_spectral_origin_inverse_square.py -q
```
