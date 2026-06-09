# P13H S3 Absolute Normalization Integral Test

## Objective
Compute one explicit low-mode S3 matrix element for the candidate V-like
operator, using the repaired P13B1 spinor basis, the source-fixed Ben Achour
E_i/E'_i layer, the P13D convention stack, and the Lawrence/Hopf measure.

The gate checks whether the chosen matrix element reduces to
`coefficient × lambda` and whether the coefficient is invariant under the
allowed phase convention.

## Inputs
- P13A ansatz and convention registry
- P13B1 repaired spinor basis / selection-rule repair
- P13C source-fixed Ben Achour E_i / E'_i identities
- P13D convention and Hermiticity audit
- P13E reduced-scale no-go record
- P13F final V-operator no-go record
- P13G handoff / limitations package
- P11/P12 frozen oracle and robustness pattern

## Implemented
- Added `p13h_s3_absolute_normalization_integral_test.py`
- Added `tests/test_p13h_s3_absolute_normalization_integral_test.py`
- Added a registry entry for `P13H_S3_ABSOLUTE_NORMALIZATION_INTEGRAL_TEST`
- Updated the convention registry report and active context

## Verification
Targeted exact test bundle:

```text
python -m pytest -q tests/test_p13h_s3_absolute_normalization_integral_test.py tests/test_convention_registry.py
```

Expected result:
- one exact S3 integral is computed
- the Lawrence/Hopf measure is applied once
- the phase-twisted control is invariant
- the result reduces to `coefficient × lambda`
- the coefficient is `16*pi**2*rho**3/15`

## Scope Fence
This gate verifies only one explicit low-mode normalization integral.

This gate does not verify:
- a physical V-operator
- V-selection promotion
- fermion generation claims
- Standard Model reproduction
- runtime safety

Current status:

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

## Current Status
`P13H = NORMALIZATION_DEPENDENT_NO_GO`

The explicit integral is derived, but `lambda` remains a free coupling
parameter.

## Plain Language Summary

We found the structure and checked it.
We also computed one explicit low-mode S3 integral.
The result is still proportional to `lambda`, so the branch does not become a
physical V-operator.

In short:

```text
scaffold = yes
pattern = yes
Hermiticity = yes
exact low-mode integral = yes
physical V-operator = no
lambda = free
```

## Next Gate
None on this branch without a new external physical principle or a source-fixed
coupling derivation that actually fixes `lambda`.
