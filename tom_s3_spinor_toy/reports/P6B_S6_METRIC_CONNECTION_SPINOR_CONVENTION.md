# P6B S6 Metric / Connection / Spinor Convention

Date: 2026-06-08

## Objective

Fix the geometric convention for the separate S6 track before any Dirac or
Casimir implementation work.

## Implemented

[CODE] The executable S6 contract layer now fixes the geometric choices:

```text
metric normalization = unit round S6 normalization
connection choice = Levi-Civita connection on the canonical homogeneous metric
spinor-bundle convention = canonical spin structure induced by the G2/SU(3) reductive frame
Dirac convention = homogeneous Dirac operator with Casimir cross-check target
```

[CODE] The contract still defers:

- selection-rule status;
- spectrum computation;
- SU(4) / hypercharge interpretation.

## Verification

[VERIFIED] Targeted smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py
4 passed
```

## Scope Fence

[INFERRED] This is a geometry-convention audit only. It does not compute a
spectrum and does not claim an SU(4) or hypercharge result.

[INFERRED] It remains separate from the validated S3 basis work.

## Current Status

```text
P6_S6_G2_SU3_FORMULA_SPEC = drafted
P6_S6_G2_SU3_IMPLEMENTATION = geometry convention fixed / started
P6B_S6_METRIC_CONNECTION_SPINOR_CONVENTION = passed
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```
