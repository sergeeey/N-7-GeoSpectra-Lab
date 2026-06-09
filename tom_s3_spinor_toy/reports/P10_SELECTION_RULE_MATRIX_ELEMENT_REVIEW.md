# P10 Selection Rule Matrix Element Review

Date: 2026-06-08

## Executive Verdict

```text
SELECTION_RULE_MATRIX_ELEMENT_REVIEW_CLOSED
```

## Scope

Terminal review fence for the frozen matrix-element scaffold.

No new V operator.

No V-selection promotion.

No fermion-generation claim.

No Standard Model reproduced claim.

## Inputs

[CODE] The review consumes the already-passed P9 audit as fixed input:

```text
P9_MATRIX_ELEMENT_SELECTION_RULES = passed
```

[CODE] The current working scaffold is kept frozen at the direct Haar/unit-
coframe reduced matrix-element convention:

```text
normalization status = ANALYTIC_DIRECT_HAAR_CONVENTION
claim scope = engineering smoke tests only; no quantitative physics claims
```

## Review Result

```text
selection_rule_matrix_element_review_closed
```

[CODE] The fence remains:

```text
v_scaffold_shape = (16, 16)
v_scaffold_hermitian = True
v_scaffold_nonzero = True
selection_rule_status = smoke_only
```

## Classification

```text
tensor_product_derived:
  - v_scaffold_shape
  - v_scaffold_hermiticity

normalization_dependent:
  - working reduced matrix elements
  - final Ben Achour E/E' basis mapping

smoke_only:
  - physical V-selection rule

requires_physical_input:
  - full fermion generation claim
  - Standard Model reproduced claim
```

[INFERRED] The review does not justify promotion of `V-selection rules`.

## Tests

[VERIFIED] Targeted smoke test passed locally:

```text
python -m pytest -q tests/test_p10_selection_rule_matrix_element_review.py
2 passed
```

## Status

```text
P10_SELECTION_RULE_MATRIX_ELEMENT_REVIEW = passed
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

## Next Gate

```text
none; expand only if a new validated matrix-element derivation is supplied
```
