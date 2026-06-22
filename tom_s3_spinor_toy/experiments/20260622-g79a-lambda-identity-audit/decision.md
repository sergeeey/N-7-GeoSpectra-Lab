# G79A Decision — OPEN_IDENTITY_UNPROVEN

**Date:** 2026-06-22  
**Verdict:** `OPEN_IDENTITY_UNPROVEN`

## Result

The deterministic audit classified **1977** repository occurrences:

| Class | Count |
|---|---:|
| `V_OPERATOR_COUPLING` | 576 |
| `NP_EXPONENT` | 563 |
| `NUMERICAL_PLACEHOLDER` | 112 |
| `UNRELATED` | 726 |
| `AMBIGUOUS` | 0 |

The V-operator coupling and the NP exponent are both instantiated in the
repository, but no derivation identifies them and no derivation proves them
different. The only direct cross-sector reference is the G76 registry test,
which checks that their scopes are distinct; this is bookkeeping evidence, not
a physical derivation.

They therefore remain two distinct audit categories:

- `lambda_v_operator`: V-operator coupling;
- `lambda_np`: non-perturbative exponent.

Later gates must not assume `lambda_v_operator = lambda_np` unless they provide
an explicit derivation. A bridge used only as a model assumption must be marked
`CONDITIONAL`, not presented as an identity.

Therefore:

- `PASS_SAME_LAMBDA` is not justified;
- `FAIL_DISTINCT_LAMBDAS` is not justified;
- code and documentation do not currently disagree, so `MIXED` is not justified;
- the correct status is `OPEN_IDENTITY_UNPROVEN`.

## Scope

This is a symbol-provenance audit. It does not derive either coupling and does
not modify G4's `FREE_COUPLING_PARAMETER` theorem for the V-operator sector.

Run the deterministic audit and focused tests:

```bash
python tom_s3_spinor_toy/experiments/20260622-g79a-lambda-identity-audit/g79a_lambda_identity_audit.py
python -m pytest tom_s3_spinor_toy/tests/test_g79a_lambda_identity_audit.py -q
python -m pytest tom_s3_spinor_toy/tests/test_g61_lambda_origin.py tom_s3_spinor_toy/tests/test_g62_observables.py tom_s3_spinor_toy/tests/test_g76_parameter_registry.py -q
```

The generated `results_g79a.json` contains the complete occurrence inventory.
