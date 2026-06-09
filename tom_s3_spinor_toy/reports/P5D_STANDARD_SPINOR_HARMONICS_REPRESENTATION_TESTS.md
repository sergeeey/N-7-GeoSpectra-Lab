# P5D Standard Spinor Harmonics Representation Tests

Date: 2026-06-08

Scope: verify the standard lowest `S3` spinor-harmonic layer implemented in
`standard_s3_spinor_harmonics.py`.

## Executive Verdict

```text
REPRESENTATION_TESTS_PASSED
```

<fact> The standard `S3` spinor-frame layer now passes the local representation
tests added for the project.

<fact> This is still a local `S3` basis-layer validation, not a promotion of the
full Lawrence construction to runtime-safe status.

## Tested Properties

The new test layer checks:

- Cartan weights for the four matrix entries;
- `su(2)_L` and `su(2)_R` closure on the lifted generators;
- pointwise unitarity and orthonormality of the frame columns;
- regularity at `alpha = 0` and `alpha = pi/2`;
- weighted Haar norms over the `S3` measure;
- comparison against the independent `Wigner-D` oracle already present in the
  repository.

## Verification

<VERIFIED> Local targeted test bundle:

```text
python -m pytest -q tests/test_standard_s3_spinor_harmonics.py \
  tests/test_lawrence_i1r_failure_reproduction.py \
  tests/test_s3_spin_connection_lawrence_frame.py
11 passed
```

## What This Does Not Prove

- not `safe_for_runtime`;
- not full Lawrence theory validation;
- not `S6 / SU4`;
- not instanton / index / chirality;
- not `V`-selection rule promotion by itself.

## Current Status

```text
P5C_STANDARD_S3_SPINOR_HARMONICS_IMPLEMENTATION = initial layer implemented
P5D_STANDARD_SPINOR_HARMONICS_REPRESENTATION_TESTS = passed
runtime = research_only
V-selection rules = smoke_only
```

## Next Step

Keep any later `V`-coupling work separate from this basis-layer audit.

