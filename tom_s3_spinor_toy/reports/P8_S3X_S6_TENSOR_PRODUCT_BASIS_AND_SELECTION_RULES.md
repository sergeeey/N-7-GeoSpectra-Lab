# P8 S3xS6 Tensor Product Basis and Selection Rules

Date: 2026-06-08

## Executive Verdict

```text
TENSOR_PRODUCT_ORDERING_REVIEW_PASSED
```

## Scope

Only the basis/order bridge between the validated S3 scaffold, the frozen S6
labels, and the audited SU(4)/SU(3)c gauge metadata.

No fermion-generation claim.

No Standard Model reproduced claim.

No V-selection promotion.

## Bridge

[CODE] The bridge order is fixed as:

```text
S3 basis × S6 labels × SU4 labels, lexicographic tensor order
```

[CODE] The S3 ordering is the validated lowest spinor frame:

```text
plus_plus, plus_minus, minus_plus, minus_minus
```

[CODE] The S6 ordering is the frozen round-sphere label stack:

```text
k ascending; sign (+,-); multiplicity per signed level
```

[CODE] The SU4 ordering is taken from the audited generalized Gell-Mann basis
and the standard SU(3)c upper-left embedding.

## Claim Classification

```text
tensor_product_derived:
  - s3_spinor_basis_order
  - s6_spectrum_level_order
  - tensor_product_label_order

basis_ordering_dependent:
  - su4_generator_order
  - su3c_embedding_labels

normalization_dependent:
  - lambda_15_normalization
  - candidate_Y_W

requires_physical_input:
  - full fermion generation claim
  - Standard Model reproduced claim

smoke_only:
  - physical V-selection rule

failed:
  - failed bridge claim
```

[INFERRED] The bridge does not justify promotion of `V-selection rules`.

## Tests

[VERIFIED] Targeted smoke test passed locally:

```text
python -m pytest -q tests/test_p8_tensor_product_basis_and_selection_rules.py
2 passed
```

## Status

```text
P8_S3xS6_TENSOR_PRODUCT_BASIS_AND_SELECTION_RULES = passed
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

## Next Gate

```text
P9_MATRIX_ELEMENT_SELECTION_RULES
```
