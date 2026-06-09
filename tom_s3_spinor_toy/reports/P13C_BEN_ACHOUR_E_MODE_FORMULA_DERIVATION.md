# P13C Ben Achour E-mode Formula Derivation

## Objective

Derive and audit the exact Ben Achour `E_i / E'_i` one-form mode formula in
the source-supported geometry layer, compare it against the frozen P11/P12
pattern, and keep all reduced-element and physical-normalization questions
separate.

## Inputs

Frozen inputs:

- P13A ansatz and convention registry
- P13A1 executable Ben Achour `E_i / E'_i` low-mode layer
- P13B1 repaired spinor-state basis
- P13C0 toy-gradient formula audit
- P11/P12 frozen scaffold/oracle pattern
- P7 SU4 generator normalization
- convention registry

## Implemented

- [CODE] Added `p13c_ben_achour_e_mode_formula_derivation.py`
- [CODE] Added `tests/test_p13c_ben_achour_e_mode_formula_derivation.py`
- [CODE] Updated `convention_registry.py`
- [CODE] Updated `reports/CONVENTION_NORMALIZATION_REGISTRY.md`
- [CODE] Updated `activeContext.md`

## Exact Formula

[VERIFIED-SYNTHETIC] The source-supported low-mode formula is fixed as:

```text
E_i = (L + 2) B_i + C_i
E'_i = (L + 2) B'_i - C'_i
```

The low-mode boundary case `L = 1` remains `VANISHING_OR_EXCLUDED`, so the
gate uses `L = 2` as the non-boundary source check.

## Coefficient Provenance

[VERIFIED-SYNTHETIC] The gate separates:

- source-fixed Ben Achour one-form identities
- reduced matrix element normalization, which remains unresolved
- toy-gradient relation, which remains normalization-dependent
- frozen P11/P12 pattern support

This gate does not promote the physical operator. The reduced coefficients are
still not fixed as a physical claim.

## Pattern Comparison

[VERIFIED-SYNTHETIC] The exact low-mode formula matches the frozen scaffold
pattern on the repaired basis:

- P11 status: passed
- P12 status: passed
- P13B1 verdict: `P13B_PATTERN_STILL_VALID`
- pattern status: `MATCHES_FROZEN_SCAFFOLD`

## Normalization Boundary

[VERIFIED-SYNTHETIC] The source formula itself is fixed, but the exact reduced
matrix elements remain `NORMALIZATION_DEPENDENT`. The coupling `lambda` is not
derived in this gate.

## Verification

Targeted bundle:

```text
python -m pytest -q tests/test_p13c_ben_achour_e_mode_formula_derivation.py tests/test_convention_registry.py
```

Result:

```text
5 passed
```

## Scope Fence

This gate verifies only:

```text
- source-fixed Ben Achour E/E' one-form identities
- comparison to frozen P11/P12 scaffold
- repaired-basis compatibility via P13B1 and P13C0
- source-vs-normalization separation
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
SOURCE_FIXED
```

## Next Gate

```text
none; exact source identities are fixed, while reduced coefficients remain normalization-dependent unless a separate normalization or physical-coupling repair gate is supplied
```
