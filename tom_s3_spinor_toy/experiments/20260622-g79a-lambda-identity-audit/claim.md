# G79A Claim — Lambda Identity Audit

**Date:** 2026-06-22  
**Type:** repository-wide symbol provenance audit

## Question

Does the repository derive an identity between:

1. `lambda_v_operator` — the coupling multiplying the V-operator sector; and
2. `lambda_np` — the coefficient in the KKLT-like exponent
   `exp(-lambda_np/rho6^2)`?

## Classification

Every matched usage must be assigned one class:

- `V_OPERATOR_COUPLING`
- `NP_EXPONENT`
- `NUMERICAL_PLACEHOLDER`
- `UNRELATED`
- `AMBIGUOUS`

## Gates

- G79A-1: every occurrence is classified and carries file/line evidence.
- G79A-2: no unclassified or ambiguous occurrence remains.
- G79A-3: both physical lambda sectors are present.
- G79A-4: search for explicit identity/equality assertions between the sectors.
- G79A-5: an identity counts only if an explicit derivation is linked.
- G79A-6: documentation/code disagreement produces `MIXED`.

## Verdicts

- `PASS_SAME_LAMBDA`: identity explicitly derived.
- `FAIL_DISTINCT_LAMBDAS`: an explicit derivation proves they differ.
- `OPEN_IDENTITY_UNPROVEN`: both exist, but no identity or distinction is derived.
- `MIXED`: documentation and code disagree.

## Kill condition

Any `AMBIGUOUS` occurrence or unsupported equality assertion blocks a clean
same-lambda result.

## Reproduction

```bash
python tom_s3_spinor_toy/experiments/20260622-g79a-lambda-identity-audit/g79a_lambda_identity_audit.py
python -m pytest tom_s3_spinor_toy/tests/test_g79a_lambda_identity_audit.py -q
```

