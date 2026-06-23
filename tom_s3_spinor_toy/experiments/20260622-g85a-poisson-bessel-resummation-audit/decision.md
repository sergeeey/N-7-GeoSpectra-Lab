# G85A Decision вЂ” Poisson/theta resummation audit

**Date:** 2026-06-22
**Verdict:** `POISSON_THETA_FORM_ONLY`

## Observed result

The repository contains genuine Poisson/theta structure in the SВі heat-kernel
analysis and in the Casimir/Hadamard chain:

- SВі Poisson summation removes higher SW coefficients exactly;
- bilateral theta identities appear in the G54 audit chain;
- proper-time / heat-kernel formulas repeatedly contain `exp(-t * c / rho6^2)`;
- zeta / determinant finite parts are present in the same pipeline.

What is missing is the final bridge:

- no Bessel route was found in the local tree;
- no deterministic resummation step promotes the proper-time integrand to a
  final effective `A * exp(-lambda_np / rho6^2)` term;
- `t` remains an integrated or free kernel variable;
- `lambda_np` is not fixed by the repository data;
- no operator-level connection to `lambda_V` appears.

## Interpretation

This is a form-only result, not a derived spectral bridge.

The audit shows that the repository knows about Poisson/theta identities and
heat-kernel structure, but it does not yet turn them into a final inverse-square
non-perturbative exponential.

## What was checked

- local repository scan for Poisson / Bessel / theta / modular / resummation /
  saddle / worldline / proper-time / determinant / zeta / heat kernel /
  spectral action / KKLT / lambda_np / rho6;
- G54-B, G54-C, G54-D, G54-E, G54-F, G56, G84B, README and PROCEEDINGS;
- deterministic classification of candidate routes.

## Reproduction

```bash
python tom_s3_spinor_toy/experiments/20260622-g85a-poisson-bessel-resummation-audit/g85a_poisson_theta_resummation_audit.py
python -m pytest tom_s3_spinor_toy/tests/test_g85a_poisson_theta_resummation_audit.py -q
python -m pytest tom_s3_spinor_toy/tests/test_g84a_standard_gauge_reduction.py tom_s3_spinor_toy/tests/test_g84b_spectral_origin_inverse_square.py tom_s3_spinor_toy/tests/test_g84c_functional_form_degeneracy.py -q
python -m compileall -q tom_s3_spinor_toy
git diff --check
```

## Next gate

`G85B_SPECTRAL_SADDLE_WORLDLINE_AUDIT`
