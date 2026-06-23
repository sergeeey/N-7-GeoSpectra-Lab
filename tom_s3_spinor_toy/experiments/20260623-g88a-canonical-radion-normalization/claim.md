# G88A Claim: Canonical Radion Normalization Audit

**Question type:** deterministic audit
**Date:** 2026-06-23
**Status target:** falsifiable

## Hypothesis

The G62 headline ratio `m_mod/m_KK = 2.02%` may be a coordinate-space proxy rather
than the physical radion mass ratio. After canonical normalization of the radion
field, the ratio should change.

## Pass condition

The audit passes if:

1. the coordinate-space proxy is reproduced from the existing potential;
2. the canonical radion field is extracted as `phi = q log(rho6)`;
3. the canonical mass proxy differs materially from the coordinate proxy;
4. the metric-only canonical proxy is reproducible by finite differences.

## Fail condition

The audit fails if the canonical and coordinate ratios are numerically the same,
or if the canonical field cannot be defined from the tested Einstein-frame metric.

## Allowed verdicts

- `CANONICAL_PROXY_ONLY`
- `PHYSICAL_CONFIRMED`
- `COORDINATE_ARTIFACT`
- `INSUFFICIENT_ACTION`
- `MIXED`

## Falsifiers

- canonical and coordinate ratios coincide;
- the path metric does not match the expected Einstein-frame coefficient;
- the finite-difference check disagrees with the analytic canonical Hessian.

## Reproduction command

```bash
python tom_s3_spinor_toy/experiments/20260623-g88a-canonical-radion-normalization/g88a_canonical_radion_normalization.py
python -m pytest tom_s3_spinor_toy/tests/test_g88a_canonical_radion_normalization.py -q
```
