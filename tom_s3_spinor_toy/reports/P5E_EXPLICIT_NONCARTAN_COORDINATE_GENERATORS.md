# P5E Explicit Non-Cartan Coordinate Generators

Date: 2026-06-08

Scope: record the explicit coordinate-space non-Cartan generator layer for the
Lawrence/Hopf chart on `S^3`, together with the current verification status on
the validated standard spinor-harmonic basis.

## Current State

```text
P5C_STANDARD_S3_SPINOR_HARMONICS_IMPLEMENTATION = initial layer implemented
P5D_STANDARD_SPINOR_HARMONICS_REPRESENTATION_TESTS = passed
P5E_EXPLICIT_NONCARTAN_COORDINATE_GENERATORS = implemented / smoke-verified
runtime = research_only
V-selection rules = smoke_only
```

## Coordinate Convention

The explicit raw SU(2) Killing fields are recorded in the Euler-angle chart
used by the repository Wigner-D oracle:

```text
a = -theta
b = 2 * alpha
c = -theta_tilde
```

These are the coordinate-space generators used for the local non-Cartan audit.
They are intentionally kept separate from any S6/SU4, instanton, index,
chirality, or heavy spectral claims.

## Implemented Generator Layer

The module [`s3_lawrence_noncartan_generators.py`](../s3_lawrence_noncartan_generators.py)
records the raw left/right ladder fields in `(alpha, theta, theta_tilde)`:

```text
L+ = exp(-i theta) * (0.5 d_alpha - i cot(2 alpha) d_theta + i csc(2 alpha) d_theta_tilde)
L- = exp(+i theta) * (-0.5 d_alpha - i cot(2 alpha) d_theta + i csc(2 alpha) d_theta_tilde)
R+ = exp(-i theta_tilde) * (-0.5 d_alpha - i csc(2 alpha) d_theta + i cot(2 alpha) d_theta_tilde)
R- = exp(+i theta_tilde) * (0.5 d_alpha - i csc(2 alpha) d_theta + i cot(2 alpha) d_theta_tilde)
```

with `L1/L2/L3` and `R1/R2/R3` formed from the usual ladder combinations.

The project aliases remain:

```text
I1L -> L1
I2L -> L2
I3L -> L3
I1R -> R1
I2R -> R2
I3R -> R3
```

## Verification Status

[VERIFIED] The new smoke test bundle passed locally:

```text
python -m pytest -q tests/test_p5e_noncartan_coordinate_generators.py \
  tests/test_standard_s3_spinor_harmonics.py \
  tests/test_lawrence_i1r_failure_reproduction.py \
  tests/test_s3_spin_connection_lawrence_frame.py
13 passed
```

[VERIFIED] The smoke test checks:

- the documented alias map;
- pointwise span-closure of the raw coordinate generators on the validated
  lowest standard `S^3` spinor frame;
- consistency of the generator action across two distinct point sets.

## Remaining Caveat

[INFERRED] The current layer is enough to say that the explicit coordinate-space
generator formulas exist and act consistently on the validated basis at the
smoke-test level.

[INFERRED] It is **not** yet enough to promote the project to runtime-safe or to
raise `V-selection rules` above `smoke_only`.

[INFERRED] The exact commutator normalization remains convention-sensitive and
needs a separate audit before any stronger `su(2)_L \oplus su(2)_R` claim is
promoted from the coordinate-space layer.

## Conclusion

```text
P5E = explicit non-Cartan coordinate generators implemented
runtime = research_only
V-selection rules = smoke_only
next = P5F_NONCARTAN_COMMUTATOR_CONVENTION_AUDIT
```

