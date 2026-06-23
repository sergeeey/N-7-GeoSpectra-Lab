# G85A Claim: Poisson/Bessel Resummation Audit

**Question type:** deterministic audit
**Date:** 2026-06-22
**Status target:** open / falsifiable

## Hypothesis

The repository may contain a route from spectral/heat-kernel proper-time expressions
to a final effective non-perturbative term of the form

`A * exp(-lambda_np / rho6^2)`.

The strongest candidate route is a Poisson/theta resummation or a Bessel-type
re-expression of KK sums or spectral determinants.

## What counts as success

The audit passes only if the repository contains an explicit, reproducible bridge
that simultaneously:

1. identifies a concrete sum, determinant, or kernel;
2. applies a Poisson/Bessel/resummation step;
3. produces a final effective term proportional to `exp(-lambda_np / rho6^2)`;
4. fixes or geometrically constrains `lambda_np`;
5. does not rely on a free proper-time variable `t` remaining inside the final answer.

## What counts as failure

The audit fails, or is only form-level evidence, if the repository shows only:

- Poisson/theta identities without a final effective exponential;
- proper-time integrands such as `exp(-t * c / rho6^2)` with free or integrated `t`;
- zeta or determinant finite parts that remain logarithmic or power-law;
- no Bessel route at all;
- no fixed bridge from the spectral expression to `lambda_np`.

## Allowed verdicts

- `RESUMMATION_BRIDGE_DERIVED`
- `POISSON_THETA_FORM_ONLY`
- `NO_RESUMMATION_BRIDGE`
- `OPEN_MISSING_SUMMATION_DATA`
- `MIXED`

## Falsifiers

- `Bessel` never appears in a usable bridge.
- Poisson/theta structure appears only as a heat-kernel identity.
- The proper-time variable `t` is integrated over or left free.
- The final effective exponential is not derived from the repository data.
- No operator-level connection to `lambda_np` is found.

## Reproduction command

```bash
python tom_s3_spinor_toy/experiments/20260622-g85a-poisson-bessel-resummation-audit/g85a_poisson_theta_resummation_audit.py
python -m pytest tom_s3_spinor_toy/tests/test_g85a_poisson_theta_resummation_audit.py -q
```
