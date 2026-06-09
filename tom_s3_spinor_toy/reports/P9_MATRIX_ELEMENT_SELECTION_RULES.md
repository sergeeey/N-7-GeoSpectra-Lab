# P9 Matrix Element Selection Rules

Date: 2026-06-08

## Executive Verdict

```text
MATRIX_ELEMENT_SELECTION_RULE_AUDIT_PASSED
```

## Scope

Only the matrix-element selection-rule audit in the already-frozen P5/P6/P7/P8
stack.

No full fermion-generation claim.

No Standard Model reproduced claim.

No V-selection promotion.

## Inputs

[CODE] The audit consumes the already-validated bridge and review layers:

```text
P8_S3xS6_TENSOR_PRODUCT_BASIS_AND_SELECTION_RULES = passed
P6M_S6_SELECTION_RULE_REVIEW = passed
P7_SU4_HYPERCHARGE_GAUGE_BREAKING_AUDIT = passed
```

[CODE] The current matrix-element scaffold is the working Option B Hermitian
scaffold, still tied to the direct Haar/unit-coframe reduced matrix-element
convention.

## Selection-Rule Classification

```text
tensor_product_derived:
  - v_scaffold_shape
  - v_scaffold_hermiticity
  - S3 Cartan weights
  - P8 tensor-product bridge
  - S6 selection review
  - SU4 audit

basis_ordering_dependent:
  - basis ordering of S3/SU4 labels
  - current working selection-rule scaffold labels

normalization_dependent:
  - working reduced matrix elements
  - final Ben Achour E/E' basis mapping

requires_physical_input:
  - full fermion generation claim
  - Standard Model reproduced claim

smoke_only:
  - physical V-selection rule

failed:
  - failed matrix-element claim
```

[INFERRED] The audit does not justify promotion of `V-selection rules`.

## Tests

[VERIFIED] Targeted smoke test passed locally:

```text
python -m pytest -q tests/test_p9_matrix_element_selection_rules.py
2 passed
```

## Status

```text
P9_MATRIX_ELEMENT_SELECTION_RULES = passed
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

## Next Gate

```text
P10_SELECTION_RULE_MATRIX_ELEMENT_REVIEW
```
