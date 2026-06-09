# P6K S6 Spectrum Computation

Date: 2026-06-08

## Objective

Turn the frozen S6 operator contract into an explicit analytic Dirac spectrum
computation layer for the round S6 baseline, without widening scope to SU(4),
hypercharge, instantons, index, or chirality.

## Implemented

[CODE] Added the analytic spectrum computation module:

```text
s6_g2_su3_spectrum_computation.py
tests/test_p6k_s6_spectrum_computation.py
```

[CODE] The computation layer uses the standard round-sphere Dirac spectrum:

```text
lambda_{k,+/-} = +/- (k + 3) / R
mu_k = 8 * binomial(k + 5, k)
```

This is the S6 specialization of the standard round S^n Dirac formula
confirmed in the literature.

[CODE] The computation layer preserves the frozen S6 convention:

```text
S6 ≅ G2 / SU(3)
g2 = su(3) ⊕ m
metric normalization = unit round S6 normalization
connection choice = Levi-Civita connection on the canonical homogeneous metric
spinor-bundle convention = canonical spin structure induced by the G2/SU(3) reductive frame
dirac operator = homogeneous Dirac operator with Casimir cross-check target
Casimir cross-check = D ~ C_G + (1/8) s
```

[CODE] The computation layer keeps the deferred claims fenced off:

- selection rules;
- SU(4) / hypercharge interpretation;
- instanton / index / chirality;
- runtime safe promotion.

## Verification

[VERIFIED] Targeted smoke test passed locally:

```text
python -m pytest -q tests/test_p6k_s6_spectrum_computation.py
6 passed
```

[VERIFIED] The computation layer is compatible with the prior S6 chain:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py tests/test_p6c_s6_dirac_casimir_baseline.py tests/test_p6d_s6_spectrum_baseline.py tests/test_p6e_s6_spectrum_implementation.py tests/test_p6f_s6_spectrum_operator_review.py tests/test_p6g_s6_spectrum_operator_stabilization.py tests/test_p6h_s6_spectrum_operator_lockdown.py tests/test_p6i_s6_spectrum_operator_freeze.py tests/test_p6j_s6_spectrum_operator_final_review.py tests/test_p6k_s6_spectrum_computation.py
26 passed
```

## Scope Fence

[INFERRED] This is an analytic round-sphere computation layer only. It does not
claim an SU(4) or hypercharge result.

[INFERRED] It remains separate from the validated S3 basis work.

## Current Status

```text
P6K_S6_SPECTRUM_COMPUTATION = passed
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

## Next Gate

```text
P6L_S6_SPECTRUM_RESULT_REVIEW
```
