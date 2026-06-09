# P11 External-Oracle Matrix-Element Derivation

Date: 2026-06-08

## Executive Verdict

```text
EXTERNAL_ORACLE_MATCHES_FROZEN_SCAFFOLD
```

## Inputs

Frozen inputs only:

- P5 S3 scaffold
- P6 S6 labels / spectrum result review
- P7 SU4 metadata
- P8 tensor ordering
- P9 matrix-element selection-rule audit
- P10 matrix-element review

## Oracle

[CODE] The external oracle is anchored in classic Wigner-D / Clebsch-Gordan /
Wigner-Eckart machinery and is constructed symbolically for `k_max <= 2`.

[CODE] The oracle uses the same validated representation labels as the frozen
stack, but it is built independently from the frozen scaffold logic.

[CODE] The oracle produces a Hermitianized selection-pattern matrix and
compares its nonzero pattern to the frozen scaffold.

## Comparison

[VERIFIED] For `k_max = 1` and `k_max = 2`, the external oracle selection
pattern matches the frozen `V` scaffold pattern.

[CODE] Exact coefficients remain normalization-dependent, but the nonzero
selection pattern itself is stable under the comparison performed here.

[CODE] No ad hoc basis permutation, phase patch, or normalization patch was
applied to force agreement.

## Classification

```text
EXTERNAL_ORACLE_DERIVED
MATCHES_FROZEN_SCAFFOLD
BASIS_ORDERING_DEPENDENT
NORMALIZATION_DEPENDENT
REQUIRES_PHYSICAL_INPUT
SMOKE_ONLY
```

[INFERRED] The derivation does not promote `V-selection rules`.

## Tests

[VERIFIED] Targeted smoke tests passed locally:

```text
python -m pytest -q tests/test_p11_external_oracle_matrix_element_derivation.py tests/test_p9_matrix_element_selection_rules.py tests/test_p10_selection_rule_matrix_element_review.py
6 passed
```

## Status

```text
P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION = passed
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

## Next

```text
P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT
```
