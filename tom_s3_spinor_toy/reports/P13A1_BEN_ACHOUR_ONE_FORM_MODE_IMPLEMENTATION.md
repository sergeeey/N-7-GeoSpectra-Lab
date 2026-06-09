# P13A1 Ben Achour One-Form Mode Implementation

## Objective

Implement the source-supported Ben Achour S3 one-form families `E_i` and
`E'_i` as an executable low-mode geometry layer. Do not construct or promote a
physical V-operator.

## Inputs

Frozen inputs:

- Ben Achour scalar harmonic conventions from `ben_achour_scalar_modes.py`
- Ben Achour source-supported geometry registry entry
- P13A ansatz and convention registry
- current protocol / convention registry stack

## Implemented

- [CODE] Added `ben_achour_one_form_modes.py`
- [CODE] Added `tests/test_p13a1_ben_achour_one_form_mode_implementation.py`
- [CODE] Updated `convention_registry.py` with a P13A1 registry entry
- [CODE] Updated `reports/CONVENTION_NORMALIZATION_REGISTRY.md`
- [CODE] Updated `activeContext.md`

## Source-Supported Geometry

[VERIFIED-SYNTHETIC] The repo now exposes executable low-mode Ben Achour
one-form modes:

- Hopf coordinates in the project convention
- scalar mode metadata and symbolic low-mode scalar `Phi`
- Killing one-forms `xi_tilde` and `xi_prime_tilde`
- low-mode `B`, `B'`, `C`, `C'`, `E`, and `E'` families

The exact normalization of `E_i` / `E'_i` remains normalization-dependent.

[CODE] The earlier P13A readiness blocker on missing executable `E_i` / `E'_i`
functions is resolved at the low-mode symbolic level.

## Verification

Targeted bundle:

```text
python -m pytest -q tests/test_p13a1_ben_achour_one_form_mode_implementation.py tests/test_p13a_v_operator_ansatz_convention_registry.py tests/test_ben_achour_convention_extraction.py tests/test_convention_registry.py
```

Result:

```text
11 passed
```

## Scope Fence

This gate verifies only:

```text
- executable Ben Achour low-mode one-form geometry
- low-mode scalar / Killing-vector source identities
- source-supported `B`, `B'`, `C`, `C'`, `E`, `E'` construction
- normalization-dependent classification
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
BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
```

Normalization classification:

```text
NORMALIZATION_DEPENDENT
```

## Next Gate

```text
P13B_SYMBOLIC_V_MATRIX_ELEMENT_PATTERN_BUILD
```

The next gate, if opened, can use the executable low-mode geometry layer to
build a symbolic candidate V-pattern. It remains non-promotional.
