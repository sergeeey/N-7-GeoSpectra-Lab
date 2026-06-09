# P6D S6 Spectrum Baseline

Date: 2026-06-08

## Objective

Introduce the next fenced S6 layer: a spectrum baseline contract, not a
computed spectrum.

## Implemented

[CODE] Added the spectrum-baseline contract:

```text
s6_g2_su3_spectrum_baseline.py
tests/test_p6d_s6_spectrum_baseline.py
```

[CODE] The baseline keeps the current S6 contract fixed as:

```text
S6 ≅ G2 / SU(3)
g2 = su(3) ⊕ m
metric normalization = unit round S6 normalization
connection choice = Levi-Civita connection on the canonical homogeneous metric
spinor-bundle convention = canonical spin structure induced by the G2/SU(3) reductive frame
dirac operator = homogeneous Dirac operator with Casimir cross-check target
Casimir cross-check = D ~ C_G + (1/8) s
```

[CODE] The baseline sets the spectrum target as:

```text
homogeneous Dirac spectrum on S6, to be derived later
```

[CODE] The baseline deliberately defers:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation.

## Verification

[VERIFIED] Targeted smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6d_s6_spectrum_baseline.py
2 passed
```

[VERIFIED] The spectrum baseline layer also remains compatible with the S6
contract smoke bundle:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py tests/test_p6c_s6_dirac_casimir_baseline.py tests/test_p6d_s6_spectrum_baseline.py
8 passed
```

## Scope Fence

[INFERRED] This is a spectrum baseline contract only. It does not compute a
spectrum and does not claim an SU(4) or hypercharge result.

[INFERRED] It remains separate from the validated S3 basis work.

## Current Status

```text
P6_S6_G2_SU3_FORMULA_SPEC = drafted
P6_S6_G2_SU3_IMPLEMENTATION = geometry convention fixed / started
P6B_S6_METRIC_CONNECTION_SPINOR_CONVENTION = passed
P6C_S6_DIRAC_CASIMIR_BASELINE = passed
P6D_S6_SPECTRUM_BASELINE = passed
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```
