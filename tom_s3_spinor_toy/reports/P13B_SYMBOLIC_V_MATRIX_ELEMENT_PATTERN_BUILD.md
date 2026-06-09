# P13B Symbolic V Matrix-Element Pattern Build

## Objective

Build the symbolic zero/nonzero matrix-element pattern for the candidate S3
V-like ansatz and compare it against the frozen P11/P12 scaffold/oracle
pattern. Do not build or promote a physical V-operator.

## Inputs

Frozen inputs:

- P13A V-operator ansatz and convention registry
- P13A1 executable Ben Achour low-mode geometry layer
- P11 external-oracle matrix-element derivation
- P12 robustness audit
- frozen P9/P10 scaffold conventions
- frozen protocol / convention registry stack

## Implemented

- [CODE] Added `p13b_symbolic_v_matrix_element_pattern_build.py`
- [CODE] Added `tests/test_p13b_symbolic_v_matrix_element_pattern_build.py`
- [CODE] Updated `convention_registry.py` with a P13B registry entry
- [CODE] Updated `reports/CONVENTION_NORMALIZATION_REGISTRY.md`
- [CODE] Updated `activeContext.md`

## Symbolic Pattern Build

[VERIFIED-SYNTHETIC] The repo now builds a symbolic zero/nonzero matrix-element
pattern for the candidate S3 V-like ansatz using:

- the frozen P11/P12 Wigner/CG scaffold comparison
- the executable P13A1 low-mode Ben Achour `E_i` / `E'_i` geometry layer
- a real-valued shared reduced-symbol convention for Hermitian cancellation

The symbolic pattern matches the frozen P11/P12 scaffold/oracle pattern for
the tested `k_max = 1, 2, 3` bundle.

Exact coefficients remain normalization-dependent and are not promoted as
physical values.

## Verification

Targeted bundle:

```text
python -m pytest -q tests/test_p13b_symbolic_v_matrix_element_pattern_build.py tests/test_convention_registry.py tests/test_p13a1_ben_achour_one_form_mode_implementation.py tests/test_p13a_v_operator_ansatz_convention_registry.py tests/test_ben_achour_convention_extraction.py
```

Result:

```text
14 passed
```

## Scope Fence

This gate verifies only:

```text
- symbolic zero/nonzero matrix-element pattern build
- comparison against frozen P11/P12 scaffold/oracle pattern
- low-mode Ben Achour geometry as source-supported input support
- normalization-dependent classification
```

This gate does not verify:

```text
- physical V-operator derivation
- V-selection promotion
- exact coefficient physical values
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
SYMBOLIC_PATTERN_MATCHES_P11_P12
```

Normalization classification:

```text
NORMALIZATION_DEPENDENT
```

## Next Gate

```text
none; expand only if coefficient-normalization repair or physical input is supplied
```
