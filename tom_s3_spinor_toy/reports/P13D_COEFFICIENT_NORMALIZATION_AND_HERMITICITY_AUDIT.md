# P13D Coefficient Normalization And Hermiticity Audit

## Objective

Audit whether the reduced coefficient normalization in the Ben Achour
`E_i / E'_i` derivation can be fixed by the existing source identities,
Haar/unit-coframe normalization, Clifford gamma convention, and P7 SU4 trace
convention. Check Hermiticity, coefficient scaling stability, compatibility
with the frozen P11/P12 pattern, and whether any normalization choice is
ad hoc.

## Inputs

Frozen inputs:

- P13A ansatz and convention registry
- P13B1 repaired spinor-state basis
- P13C0 toy-gradient audit
- P13C exact Ben Achour E-mode formula derivation
- P13C reduced matrix-element normalization audit
- P11/P12 frozen oracle and robustness layers
- P7 SU4 / hypercharge gauge audit

## Implemented

- [CODE] Added `p13d_coefficient_normalization_and_hermiticity_audit.py`
- [CODE] Added `tests/test_p13d_coefficient_normalization_and_hermiticity_audit.py`
- [CODE] Updated `convention_registry.py`
- [CODE] Updated `reports/CONVENTION_NORMALIZATION_REGISTRY.md`
- [CODE] Updated `activeContext.md`

## Coefficient Stack

[VERIFIED-SYNTHETIC] The audit separates the current stack into:

- exact Ben Achour source identities: source-fixed
- Haar/unit-coframe normalization: convention-fixed at the current source level
- Clifford gamma convention: convention-fixed
- P7 SU4 generator / trace convention: convention-fixed
- exact reduced coefficient normalization: still normalization-dependent
- coupling `lambda`: still a physical-input requirement

## Hermiticity

[VERIFIED-SYNTHETIC] Hermiticity is preserved under the audited convention
stack:

- P7 algebra layer remains Hermitian
- P12 robustness audit remains Hermitian on the frozen scaffold
- coefficient rescaling controls preserve the pattern while changing
  coefficients

This supports convention consistency, but it does not fix the absolute reduced
normalization.

## Pattern Compatibility

[VERIFIED-SYNTHETIC] Compatibility with the frozen P11/P12 external-oracle
pattern remains intact.

## Ad Hoc Check

[VERIFIED-SYNTHETIC] No ad hoc normalization patch is required to preserve the
audited zero/nonzero pattern, but the exact reduced coefficient scale is still
not derivable from the current source stack alone.

## Verification

Targeted bundle:

```text
python -m pytest -q tests/test_p13d_coefficient_normalization_and_hermiticity_audit.py tests/test_convention_registry.py
```

Result:

```text
5 passed
```

## Scope Fence

This gate verifies only:

```text
- coefficient provenance separation
- Hermiticity compatibility
- coefficient scaling stability
- compatibility with P11/P12 robust pattern
- ad hoc normalization check
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
none; exact coefficient scale remains normalization-dependent unless a separate normalization or physical-coupling repair gate is supplied
```
