# G76 Claim вЂ” Parameter Registry Audit

**Date:** 2026-06-22
**Type:** provenance and identifiability audit
**Scope:** G54вЂ“G63 stabilization chain

## Question

Can every parameter used by the stabilization chain be assigned exactly one of
three top-level classes:

1. `fixed` вЂ” fixed within the stated geometric/toy ansatz;
2. `conditional` вЂ” derived only after named assumptions or external inputs;
3. `free` вЂ” not determined by the implemented model?

## Gates

- G76-1: every registry entry has class, provenance, dependencies, scope, and evidence.
- G76-2: all dependencies refer to registered parameters.
- G76-3: external observational inputs remain explicitly marked `external`.
- G76-4: `lambda_np` and `lambda_v_operator` are separate symbols.
- G76-5: `A_np` and uplift `D` are conditional, not free once their assumptions are supplied.
- G76-6: physical mass normalization remains free until the reduced kinetic action and scale map are supplied.

## Kill condition

`FAIL` if any parameter has missing provenance, a dangling dependency, or if the two
unproved lambda parameters are conflated.

## Expected artifacts

- `parameter_registry.json`
- `g76_parameter_registry.py`
- `results_g76.json`
- `decision.md`
- `tom_s3_spinor_toy/tests/test_g76_parameter_registry.py`
