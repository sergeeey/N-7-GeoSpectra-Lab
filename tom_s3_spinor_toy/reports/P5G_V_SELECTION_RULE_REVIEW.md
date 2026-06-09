# P5G V-Selection Rule Review

Date: 2026-06-08

## Technical Assignment

### Objective

Review the current `V` coupling scaffold for the `S3` project and verify that
its selection rules remain a controlled engineering smoke layer, not a promoted
physical claim.

### Scope

In scope:

- current `V` scaffold in `s3_coupling_v_option_b.py`;
- the working `k_max <= 3` Hermitian smoke tests;
- the current selection-rule logic encoded by the reduced matrix elements;
- consistency with the validated `S3` spinor basis layer and the lifted
  `su(2)_L x su(2)_R` oracle;
- verification that `V-selection rules` must remain `smoke_only`.

Out of scope:

- `S6 / SU4`;
- instanton, index, chirality, spectral-flow, zero-mode, or heavy spectrum
  claims;
- promotion to runtime-safe;
- any attempt to derive a new physics-level `V` from the Lawrence ansatz.

### Acceptance Criteria

1. The current `V` scaffold is Hermitian.
2. The current working selection rules are explicit and reproducible.
3. The review shows no basis for raising `V-selection rules` above
   `smoke_only`.
4. The review remains compatible with the validated standard `S3` spinor
   basis layer.
5. The review produces a durable report and a minimal regression check.

### Inputs

- `s3_coupling_v_option_b.py`
- `s3_reduced_matrix_elements.py`
- `tests/test_hermiticity_condition_skeleton.py`
- `standard_s3_spinor_harmonics.py`
- `s3_lawrence_noncartan_generators.py`

### Expected Output

- concise review report;
- no runtime-status promotion;
- no `V-selection` promotion;
- optional regression test tightening if needed.

### Risk Notes

- The current `V` is an engineering scaffold, not a final physical operator.
- Selection rules are still tied to the working `(J_L,J_R)=(1,0)` reduced
  matrix-element scaffold.
- A false promotion would overstate the physical interpretation.

## Review Result

### What is already established

- The scaffold is Hermitian by construction and smoke-tested.
- The nonzero entries obey the current working Clebsch-Gordan selection rules.
- The reduced coefficients are real and finite.
- The metadata still marks the final Ben Achour normalization as unresolved.

### What is not established

- No separate Lawrence-compatible selection-rule table has been proven.
- No physical `V`-coupling interpretation has been closed.
- No basis-contract upgrade has been performed from the current engineering
  scaffold to a full runtime claim.

### Conclusion

```text
V-selection rules = smoke_only
runtime = research_only
safe_for_runtime = no
```

## Execution Result

[VERIFIED] Targeted review bundle:

```text
python -m pytest -q tests/test_p5g_v_selection_rule_review.py \
  tests/test_p5e_noncartan_coordinate_generators.py \
  tests/test_standard_s3_spinor_harmonics.py \
  tests/test_lawrence_i1r_failure_reproduction.py \
  tests/test_s3_spin_connection_lawrence_frame.py
17 passed
```

[INFERRED] The review does not justify promotion of the V layer. It confirms
that the current scaffold remains a smoke-layer engineering operator with the
working `(J_L,J_R)=(1,0)` reduced-coefficient convention.

## Evidence Used

- [`s3_coupling_v_option_b.py`](../s3_coupling_v_option_b.py)
- [`s3_reduced_matrix_elements.py`](../s3_reduced_matrix_elements.py)
- [`tests/test_hermiticity_condition_skeleton.py`](../tests/test_hermiticity_condition_skeleton.py)
- [`standard_s3_spinor_harmonics.py`](../standard_s3_spinor_harmonics.py)
- [`reports/P5F_NONCARTAN_COMMUTATOR_CONVENTION_AUDIT.md`](P5F_NONCARTAN_COMMUTATOR_CONVENTION_AUDIT.md)
