# P6G S6 Spectrum Operator Stabilization

Date: 2026-06-08

## Objective

Stabilize the S6 spectrum operator fence after review, without computing a
spectrum.

## Implemented

[CODE] Added the operator-stabilization contract:

```text
s6_g2_su3_spectrum_operator_stabilization.py
tests/test_p6g_s6_spectrum_operator_stabilization.py
```

[CODE] The stabilization layer keeps the current S6 contract fixed as:

```text
S6 ≅ G2 / SU(3)
g2 = su(3) ⊕ m
metric normalization = unit round S6 normalization
connection choice = Levi-Civita connection on the canonical homogeneous metric
spinor-bundle convention = canonical spin structure induced by the G2/SU(3) reductive frame
dirac operator = homogeneous Dirac operator with Casimir cross-check target
Casimir cross-check = D ~ C_G + (1/8) s
```

[CODE] The stabilization layer retains the spectrum target:

```text
homogeneous Dirac spectrum on S6, to be derived later
```

[CODE] The stabilization layer deliberately defers:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation.

## Verification

[VERIFIED] Targeted smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6g_s6_spectrum_operator_stabilization.py
2 passed
```

## Scope Fence

[INFERRED] This is an operator stabilization contract only. It does not compute
a spectrum and does not claim an SU(4) or hypercharge result.

[INFERRED] It remains separate from the validated S3 basis work.

## Current Status

```text
P6_S6_G2_SU3_FORMULA_SPEC = drafted
P6_S6_G2_SU3_IMPLEMENTATION = geometry convention fixed / started
P6B_S6_METRIC_CONNECTION_SPINOR_CONVENTION = passed
P6C_S6_DIRAC_CASIMIR_BASELINE = passed
P6D_S6_SPECTRUM_BASELINE = passed
P6E_S6_SPECTRUM_IMPLEMENTATION = passed
P6F_S6_SPECTRUM_OPERATOR_REVIEW = passed
P6G_S6_SPECTRUM_OPERATOR_STABILIZATION = started
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

## Next Gate

```text
P6H_S6_SPECTRUM_OPERATOR_LOCKDOWN
```
