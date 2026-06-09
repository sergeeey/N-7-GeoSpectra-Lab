# P13A V-Operator Ansatz and Convention Registry

## Objective

Freeze a concrete candidate V-like ansatz for future symbolic derivation and
record every convention that can drift before any promotion is attempted.

This gate checks readiness for a later symbolic derivation. It does not derive
a physical V operator and does not promote V-selection rules.

## Inputs

Frozen inputs:

- P11 external-oracle matrix-element derivation
- P12 robustness audit
- Ben Achour S3 source-supported geometry extraction
- P7 SU(4) / hypercharge audit
- frozen P9/P10 scaffold conventions
- frozen protocol stack and convention registry

## Implemented

- [CODE] Added `p13a_v_operator_ansatz_convention_registry.py`
- [CODE] Added `tests/test_p13a_v_operator_ansatz_convention_registry.py`
- [CODE] Updated `convention_registry.py` with a P13A registry entry
- [CODE] Updated `reports/CONVENTION_NORMALIZATION_REGISTRY.md`
- [CODE] Updated `activeContext.md`

## Ben Achour Readiness Check

[VERIFIED-SYNTHETIC] The repo now contains source-supported Ben Achour
geometry plus an executable low-mode `E_i` / `E'_i` implementation. Exact
normalization remains dependent.

[CODE] Therefore:

```text
SOURCE_SUPPORTED_GEOMETRY = yes
EXECUTABLE_E_MODES = yes (low-mode)
EXACT_NORMALIZATION = dependent
P13A_READY_FOR_SYMBOLIC_DERIVATION = yes
P13B_SYMBOLIC_BUILD = ready, subject to coefficient normalization
```

## Verification

Targeted bundle:

```text
python -m pytest -q tests/test_p13a_v_operator_ansatz_convention_registry.py tests/test_ben_achour_convention_extraction.py tests/test_convention_registry.py tests/test_p12_matrix_element_derivation_robustness_audit.py tests/test_p11_external_oracle_matrix_element_derivation.py
```

Result:

```text
11 passed
```

## Scope Fence

This gate verifies only:

```text
- candidate symbolic V ansatz registration
- source-supported Ben Achour S3 geometry mapping
- frozen basis / factor / gamma / SU4 conventions
- legal readiness for later symbolic derivation
```

This gate does not verify:

```text
- physical V-operator derivation
- physical V-selection promotion
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

The next symbolic build gate is no longer blocked by missing low-mode
`E_i` / `E'_i` functions; it is only normalization-dependent.

## Current Status

```text
passed
```

Readiness verdict:

```text
P13_READY_FOR_SYMBOLIC_DERIVATION
```

One-form mode implementation blocker:

```text
NORMALIZATION_DEPENDENT
```

Physical promotion status:

```text
REQUIRES_PHYSICAL_INPUT
```

## Next Gate

```text
P13B_SYMBOLIC_V_MATRIX_ELEMENT_PATTERN_BUILD
```

The next gate, if opened, should build symbolic matrix-element patterns from
the frozen ansatz and conventions. It remains non-promotional unless a
separate promotion gate is created.
