# P13B1 Spinor State and Selection Rule Repair

## Objective

Repair the spinor-state basis and audit valid selection rules for the
candidate `gamma^a A_a` operator before any coefficient normalization audit.

## Inputs

Frozen inputs:

- P13B0 state / measure / selection-rule audit
- P11 external-oracle matrix-element derivation
- P12 robustness audit
- current spinor basis scaffold

## Implemented

- [CODE] Added `p13b1_spinor_state_selection_rule_repair.py`
- [CODE] Added `tests/test_p13b1_spinor_state_selection_rule_repair.py`
- [CODE] Updated `convention_registry.py`
- [CODE] Updated `activeContext.md`

## State Repair

[VERIFIED-SYNTHETIC] The audit inspects the current spinor state labels through
`k_max = 2` and `k_max = 3`:

- `states_up_to_kmax(2)` count: `40`
- `states_up_to_kmax(3)` count: `80`
- lowest valid spinor state remains the first record in the frozen ordering
- raw tuple `(0,0,0,0)` is `INVALID_SPINOR_STATE` in the spinor context
- the same tuple is only `SCALAR_STATE` under an explicit scalar convention
- scalar tuple is excluded from spinor matrix-element tests

## Selection Rules

[VERIFIED-SYNTHETIC] The lowest valid spinor state has an allowed final-state
set that is consistent with the frozen P11/P12 pattern on the repaired basis.

- left-sector `Δj_L` and `Δm_L`: pattern-supported as derived on the repaired basis
- right-sector `Δj_R` and `Δm_R`: pattern-supported, but not promoted to a physical claim
- the frozen P11/P12 pattern remains valid on the repaired basis

## P13B Rerun Decision

[VERIFIED-SYNTHETIC] P13B does not need to be rerun for this repair gate.

## Verification

Targeted bundle:

```text
python -m pytest -q tests/test_p13b1_spinor_state_selection_rule_repair.py
```

Result:

```text
3 passed
```

## Scope Fence

This gate verifies only:

```text
- spinor basis repair
- scalar tuple exclusion from spinor tests
- selection-rule audit on the repaired basis
- P11/P12 pattern still valid
- no coefficient normalization
```

This gate does not verify:

```text
- coefficient normalization
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
P13B_PATTERN_STILL_VALID
```

## Next Gate

```text
P13C_NORM_REDUCED_MATRIX_ELEMENT_NORMALIZATION_AUDIT
```
