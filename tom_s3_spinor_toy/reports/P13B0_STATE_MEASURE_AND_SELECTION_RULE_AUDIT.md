# P13B0 State Measure and Selection Rule Audit

## Objective

Repair the validation setup before any further matrix-element pattern claim.
Audit state labels, integration measure, complex matrix elements, spinor /
Ben Achour dependencies, and selection-rule assumptions for the candidate
``gamma^a A_a`` coupling.

## Inputs

Frozen inputs:

- P13A1 executable Ben Achour low-mode geometry layer
- P13A candidate ansatz and convention registry
- P11 external-oracle matrix-element derivation
- P12 robustness audit
- current spinor-harmonic scaffold and measure convention

## Implemented

- [CODE] Added `p13b0_state_measure_selection_rule_audit.py`
- [CODE] Added `tests/test_p13b0_state_measure_selection_rule_audit.py`
- [CODE] Updated `activeContext.md`

## State Labels

[VERIFIED-SYNTHETIC] The audit enumerates the current spinor scaffold states
through `k_max = 2`:

- total states: `40`
- lowest state in the current ordering:
  `k=0, branch=positive, j_L=1/2, m_L=-1/2, j_R=0, m_R=0`
- the raw tuple `(0,0,0,0)` is classified as `INVALID_SPINOR_STATE` in the
  spinor context
- the same tuple is `SCALAR_STATE` only if explicitly reinterpreted under a
  scalar convention

## Measure

[VERIFIED-SYNTHETIC] The S3 Hopf volume density is applied exactly once:

- `sqrt(g) = sin(alpha) * cos(alpha)`
- full volume: `2π²`
- double-counted measure is excluded by the audit

## Complex Matrix Elements

[VERIFIED-SYNTHETIC] The toy candidate matrix-element probe preserves full
complex values. No `.real` truncation is applied in the audit path.

Numerical probe values converge on the tested grids `20 -> 40 -> 80`.

## Dependencies

[VERIFIED-SYNTHETIC] The audit classifies the following dependencies:

- spinor-harmonic low-mode normalization: `BLACK_BOX_DEPENDENCY`
- Ben Achour `E_i / E'_i` low-mode layer: `BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE`
- exact `E_i / E'_i` normalization: `NORMALIZATION_DEPENDENT`
- selection-rule derivation for `gamma^a A_a`: `INCONCLUSIVE`

## Verification

Targeted bundle:

```text
python -m pytest -q tests/test_p13b0_state_measure_selection_rule_audit.py tests/test_p13a1_ben_achour_one_form_mode_implementation.py tests/test_ben_achour_convention_extraction.py tests/test_standard_s3_spinor_harmonics.py
```

Result:

```text
18 passed
```

## Scope Fence

This gate verifies only:

```text
- state-label audit through k_max = 2
- exact S3 measure application once
- complex-valued toy matrix-element probe
- low-mode Ben Achour dependency classification
- selection-rule assumptions remain unpromoted
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
BLOCKED_BY_INVALID_SPINOR_STATE
```

## Next Gate

```text
none; repair the invalid spinor-state assumption before any further pattern claim
```
