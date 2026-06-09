# P13C_NORM Reduced Matrix Element Normalization Audit

Legacy filename retained for compatibility:
`reports/P13C_REDUCED_MATRIX_ELEMENT_NORMALIZATION_AUDIT.md`

Display label: `P13C_NORM`

## Objective

Audit whether the reduced matrix elements and normalization constants for the
candidate S3 V-like operator can be derived, calibrated, or must remain
normalization-dependent.

## Inputs

Frozen inputs:

- P13A ansatz and convention registry
- P13A1 executable Ben Achour `E_i / E'_i` low-mode layer
- P13B symbolic pattern result
- P11/P12 frozen scaffold/oracle pattern
- P7 SU4 generator normalization
- convention registry

## Implemented

- [CODE] Added `p13c_reduced_matrix_element_normalization_audit.py`
- [CODE] Added `tests/test_p13c_reduced_matrix_element_normalization_audit.py`
- [CODE] Updated `convention_registry.py`
- [CODE] Updated `activeContext.md`

## Coefficient Sources

[VERIFIED-SYNTHETIC] The audit separates the coefficient stack into:

- Wigner/CG coefficient: derived pattern-level factor
- reduced matrix element: relative coefficients derived through the working
  direct-Haar scaffold
- Ben Achour `E_i / E'_i` normalization: normalization-dependent
- gamma/Clifford normalization: convention-fixed
- SU4 generator normalization: convention-fixed in P7
- coupling `lambda`: requires physical coupling input

## Pattern vs Coefficients

[VERIFIED-SYNTHETIC] Pattern evidence is already frozen by P11/P12/P13B.
Relative coefficients exist for the working scaffold, but absolute
normalization remains unresolved.

## Ben Achour Normalization

[VERIFIED-SYNTHETIC] The executable low-mode Ben Achour layer is present, but
its exact `E_i / E'_i` normalization is still classified as unresolved. The
audit therefore cannot derive absolute reduced coefficients from the Ben
Achour norm formulas alone.

## Lambda

[VERIFIED-SYNTHETIC] The coupling `lambda` has no internal derivation in this
gate. It remains a physical input requirement.

## Negative Controls

[VERIFIED-SYNTHETIC] The audit checks that:

- wrong normalization changes coefficient values but preserves the selection pattern
- wrong phase changes coefficients and is flagged
- forbidden physical promotion is rejected

## Verification

Targeted bundle:

```text
python -m pytest -q tests/test_p13c_reduced_matrix_element_normalization_audit.py
```

Result:

```text
3 passed
```

## Scope Fence

This gate verifies only:

```text
- coefficient provenance classification
- relative coefficients vs absolute normalization separation
- Ben Achour normalization remains unresolved
- lambda remains physical-input dependent
- negative controls for normalization and phase
```

This gate does not verify:

```text
- physical V-operator derivation
- V-selection promotion
- Standard Model reproduction
- fermion generation claim
- runtime safety
```

Current status:

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

## Current Status

```text
NORMALIZATION_DEPENDENT
```

## Next Gate

```text
none; exact coefficients remain normalization-dependent unless a separate
normalization or physical-coupling repair gate is supplied
```
