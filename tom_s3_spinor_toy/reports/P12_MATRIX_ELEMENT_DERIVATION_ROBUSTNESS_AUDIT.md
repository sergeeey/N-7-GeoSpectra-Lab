# P12 Matrix-Element Derivation Robustness Audit

Date: 2026-06-08

## Executive Verdict

```text
ROBUST
```

## Inputs

Frozen inputs only:

- P9 matrix-element selection-rule audit
- P10 matrix-element review
- P11 external-oracle matrix-element derivation

## Robustness Checks

[CODE] The external Wigner/CG oracle was stress-tested against:

- basis-ordering permutations
- phase-convention rotations
- normalization rescalings
- small `k_max` extension through `k_max = 3`

[VERIFIED] The selection-pattern comparison remains stable:

- basis ordering: `PERMUTED_EQUIVALENT`
- phase convention: `PHASE_DEPENDENT`
- normalization: `NORMALIZATION_DEPENDENT`
- `k_max = 1, 2, 3`: `ROBUST`
- Hermiticity: preserved

[CODE] Exact coefficients remain normalization-dependent, but the zero/nonzero selection pattern stays stable under the tested transformations.

## Comparison

[VERIFIED] The frozen scaffold and external oracle remain aligned through `k_max = 3` in the tested contract.

[CODE] No ad hoc basis permutation, phase patch, or normalization patch was applied to force agreement.

## Tests

[VERIFIED] Targeted smoke bundle passed locally:

```text
python -m pytest -q tests/test_p12_matrix_element_derivation_robustness_audit.py tests/test_p11_external_oracle_matrix_element_derivation.py tests/test_p10_selection_rule_matrix_element_review.py
6 passed
```

## Status

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

## Next

```text
none; expand only if a new physical operator formula or a new validated operator scaffold is supplied
```
