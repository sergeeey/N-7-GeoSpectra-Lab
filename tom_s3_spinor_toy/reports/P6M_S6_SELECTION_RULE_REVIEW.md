# P6M S6 Selection Rule Review

Date: 2026-06-08

## Objective

Review which selection-rule classes can be derived from the already-passed S6
spectrum computation/review chain, without recomputing the spectrum and
without widening scope to SU(4), hypercharge, instantons, index, or chirality.

## Implemented

[CODE] Added the S6 selection-rule review contract:

```text
s6_g2_su3_selection_rule_review.py
tests/test_p6m_s6_selection_rule_review.py
```

[CODE] The review layer consumes the already-passed S6 spectrum result review
as fixed input and classifies the current rule families as:

```text
round_s6_dirac_spacing_rule -> S6_SPECTRUM_DERIVED
round_s6_multiplicity_rule -> S6_SPECTRUM_DERIVED
casimir_cross_check_rule -> CASIMIR_DERIVED
g2_su3_representation_labels -> REPRESENTATION_CANDIDATE
su4_hypercharge_mapping -> REQUIRES_SU4_HYPERCHARGE
s3xs6_tensor_product_coupling -> REQUIRES_TENSOR_PRODUCT_S3xS6
physical_v_selection_rule -> SMOKE_ONLY
```

[CODE] The review layer explicitly preserves the current fence:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[CODE] The review layer deliberately defers:

- any SU(4) or hypercharge claim;
- any tensor-product coupling claim involving S3×S6;
- any promotion of the physical V-selection rules;
- any new spectrum computation.

## Verification

[VERIFIED] Targeted smoke test passed locally:

```text
python -m pytest -q tests/test_p6m_s6_selection_rule_review.py
2 passed
```

[VERIFIED] The review layer is compatible with the closed S6 chain:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py tests/test_p6c_s6_dirac_casimir_baseline.py tests/test_p6d_s6_spectrum_baseline.py tests/test_p6e_s6_spectrum_implementation.py tests/test_p6f_s6_spectrum_operator_review.py tests/test_p6g_s6_spectrum_operator_stabilization.py tests/test_p6h_s6_spectrum_operator_lockdown.py tests/test_p6i_s6_spectrum_operator_freeze.py tests/test_p6j_s6_spectrum_operator_final_review.py tests/test_p6k_s6_spectrum_computation.py tests/test_p6l_s6_spectrum_result_review.py tests/test_p6m_s6_selection_rule_review.py
31 passed
```

## Scope Fence

[INFERRED] This is a selection-rule review layer only. It does not compute any
new spectrum and does not claim an SU(4) or hypercharge result.

[INFERRED] It remains separate from the validated S3 basis work.

## Current Status

```text
P6M_S6_SELECTION_RULE_REVIEW = passed
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

## Next Gate

```text
none; expand only if a new validated basis contract or a new physical
selection-rule derivation is supplied
```
