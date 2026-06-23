# G79B Decision вЂ” OPEN_MISSING_DERIVATION

**Date:** 2026-06-22
**Verdict:** `OPEN_MISSING_DERIVATION`

## Result

Five bridge routes were audited:

| Route | Current status | Executable as a derivation now? |
|---|---|---:|
| Direct operator matching | `OPEN` | no |
| Dimensional reduction / gauge kinetic function | `OPEN` | no |
| Gaugino condensation | `CONDITIONAL_CANDIDATE_ONLY` | no |
| Wrapped-brane instanton action | `OPEN` | no |
| Numerical coincidence | `INSUFFICIENT_FOR_IDENTITY` | diagnostic only |

No route currently derives `lambda_v_operator=lambda_np`, and the repository
also does not prove that the parameters must differ.

## Required bridge

A successful bridge needs a common normalized action or an equivalent
operator-level matching calculation that:

1. defines both coefficients before field redefinitions;
2. derives the canonical modulus relation, including `T(rho6)`;
3. fixes independent normalization constants;
4. shows equality survives the 4D Einstein-frame reduction.

## Consequence for G78

Gaugino condensation may still be tested as a `CONDITIONAL` derivation of
`lambda_np`. It is blocked as a derivation of `lambda_v_operator` until a
separate bridge is supplied.

## Reproduction

```bash
python tom_s3_spinor_toy/experiments/20260622-g79b-lambda-bridge-feasibility/g79b_lambda_bridge_feasibility.py
python -m pytest tom_s3_spinor_toy/tests/test_g79b_lambda_bridge_feasibility.py -q
python -m pytest tom_s3_spinor_toy/tests/test_g79a_lambda_identity_audit.py tom_s3_spinor_toy/tests/test_g76_parameter_registry.py -q
```
