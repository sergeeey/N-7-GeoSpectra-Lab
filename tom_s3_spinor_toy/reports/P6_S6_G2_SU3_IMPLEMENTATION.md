# P6 S6 / G2 / SU(3) Implementation

Date: 2026-06-08

## Objective

Create the first executable contract for the separate S6 track, without mixing
it into the validated S3 basis layer.

## Implemented

[CODE] Added the first executable S6 implementation contract layer:

```text
s6_g2_su3_formula_spec.py
tests/test_p6_s6_g2_su3_formula_spec.py
s6_g2_su3_implementation.py
tests/test_p6_s6_g2_su3_implementation.py
```

[CODE] The implementation layer keeps the current S6 contract fixed as:

```text
S6 ≅ G2 / SU(3)
g2 = su(3) ⊕ m
D ~ C_G + (1/8) s
```

[CODE] The implementation contract fixes the following geometric choices:

- metric normalization = unit round S6 normalization;
- connection choice = Levi-Civita connection on the canonical homogeneous metric;
- spinor-bundle convention = canonical spin structure induced by the G2/SU(3) reductive frame;
- Dirac convention = homogeneous Dirac operator with Casimir cross-check target.

[CODE] The implementation contract still defers:

- selection-rule status;
- spectrum computation;
- SU(4) / hypercharge interpretation.

## Verification

[VERIFIED] Targeted smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_implementation.py
2 passed
```

[VERIFIED] The geometry-convention follow-up gate `P6B_S6_METRIC_CONNECTION_SPINOR_CONVENTION`
is now fixed and passed with the same smoke bundle plus the formula-spec check.

## Scope Fence

[INFERRED] This is still only an implementation contract, not a spectrum
computation and not an SU(4) / hypercharge result.

[INFERRED] It remains separate from the validated S3 basis work.

## Current Status

```text
P6_S6_G2_SU3_FORMULA_SPEC = drafted
P6_S6_G2_SU3_IMPLEMENTATION = geometry convention fixed / started
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```
