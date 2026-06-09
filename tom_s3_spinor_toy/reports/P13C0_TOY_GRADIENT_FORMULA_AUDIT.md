# P13C0 Toy Gradient Formula Audit

## Objective

Audit and repair the P13C toy gradient reduced-element formula before
accepting it as project state.

## Inputs

Frozen inputs:

- P13B1 spinor-state and selection-rule repair
- P13C analytic toy-gradient formula context
- P11/P12 frozen oracle scaffold
- repaired spinor basis through `k_max = 3`

## Implemented

- [CODE] Added `p13c0_toy_gradient_formula_audit.py`
- [CODE] Added `tests/test_p13c0_toy_gradient_formula_audit.py`
- [CODE] Updated `convention_registry.py`
- [CODE] Updated `activeContext.md`

## Formula Status

[VERIFIED-SYNTHETIC] The toy gradient reduced-element formula is classified as:

- `TOY_GRADIENT_REDUCED_ELEMENT_DERIVED`
- `BEN_ACHOUR_E_MODE_FORMULA_PENDING`
- `NORMALIZATION_DEPENDENT`

The repaired basis gate feeding this audit has:

- `P13B1` status: `passed`
- `P13B1` verdict: `P13B_PATTERN_STILL_VALID`

The model uses a repaired low-mode table and does not substitute the exact
Ben Achour `E_i / E'_i` co-exact modes.

## Low-Mode Table Repair

[VERIFIED-SYNTHETIC] The low-mode table bug is repaired:

- `-4*sp.Integer(3)/3` is replaced by `-sp.Rational(4,3)`
- all low-mode table entries match `full_matrix_element()`
- the repaired table stays on the toy-gradient model only

## Spinor State Check

[VERIFIED-SYNTHETIC] The project convention still treats:

- `(0,0,0,0)` as invalid in the spinor context
- `(0.5, -0.5, 0.0, 0.0)` as a valid spinor state

`j_R = 0` is therefore valid in the current spinor convention for the repaired
lowest state.

## Selection Rules

[VERIFIED-SYNTHETIC] The `j_R' = j_R` rule is not derived by this gate. It is
treated as `ASSUMED_BY_MODEL` for the toy gradient audit.

## Verification

Targeted bundle:

```text
python -m pytest -q tests/test_p13c0_toy_gradient_formula_audit.py
```

Result:

```text
3 passed
```

## Scope Fence

This gate verifies only:

```text
- toy gradient reduced-element formula
- low-mode table repair
- repaired spinor state validity checks
- selection-rule assumption tagging
```

This gate does not verify:

```text
- exact Ben Achour E_i / E'_i formula
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
P13C_NORM_REDUCED_MATRIX_ELEMENT_NORMALIZATION_AUDIT
```
