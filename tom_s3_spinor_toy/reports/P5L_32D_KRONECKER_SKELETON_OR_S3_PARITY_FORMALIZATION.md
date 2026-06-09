# P5L 32D Kronecker Skeleton or S3 Parity Formalization

Date: 2026-06-08

## Executive Verdict

KRONECKER_SKELETON_PASSED_PARITY_FORMALIZED

## Scope

Only S3 algebra scaffold and parity formalization.
No S6.
No SU4.
No V promotion.

## Kronecker Skeleton

- dimension: 32
- factor ordering: `spinor / chirality / internal / flavor / placeholder`
- basis ordering: lexicographic binary order on five tensor factors
- Clifford result: Euclidean anticommutators pass on the scaffold

## Parity Formalization

- formalized candidate: P2 coordinate-swap smoke candidate
- radius preservation: preserved
- standard basis closure: passed for P2
- limitations: P1 remains inconclusive; this is still a smoke/formalization
  layer, not a physical parity claim.

## Tests

Command:

```text
python -m pytest -q tests/test_p5l_s3_kronecker_skeleton.py tests/test_p5l_s3_parity_formalization.py
```

Result:

```text
3 passed
```

## Status

```text
P5L_32D_KRONECKER_SKELETON_OR_S3_PARITY_FORMALIZATION = passed
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

## Next Gate

```text
P5M_S3_SELECTION_RULE_REVIEW_AFTER_PARITY_FORMALIZATION
```
