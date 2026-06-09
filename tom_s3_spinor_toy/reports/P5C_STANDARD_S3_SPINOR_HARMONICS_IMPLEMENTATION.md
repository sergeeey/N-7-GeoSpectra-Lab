# P5C Standard S3 Spinor Harmonics Implementation

Date: 2026-06-08

Scope: implement the standard lowest `S3` spinor-harmonic frame in the
Lawrence/Hopf coordinates used by the project.

## Executive Summary

<fact> The standard lowest `S3` spinor frame is now implemented as a compact
unitary `2 x 2` matrix in Hopf/Lawrence coordinates.

<fact> The implementation is a replacement basis layer, not a rescue of the
recovered Lawrence scalar ansatz.

<fact> The new layer is consistent with the current project status:

```text
runtime = research_only
V-selection rules = smoke_only
```

## Implemented Basis

The basis used in code is:

```text
U(alpha, theta, theta_tilde) =
[
  [ cos(alpha) * exp(+i(theta + theta_tilde)/2),
    sin(alpha) * exp(+i(theta - theta_tilde)/2) ],
  [ -sin(alpha) * exp(-i(theta - theta_tilde)/2),
    cos(alpha) * exp(-i(theta + theta_tilde)/2) ]
]
```

This is the standard SU(2) spin-frame form:

- pointwise unitary;
- regular at `alpha = 0` and `alpha = pi/2`;
- entries carry the expected local Cartan phase weights.

## Representation Checks

Implemented checks cover:

- pointwise unitarity and orthonormality of the two columns;
- local Cartan phase weights for the four matrix entries;
- `su(2)_L` and `su(2)_R` generator closure via `sigma_i / 2` on the left and
  right tensor factors;
- regularity at the coordinate endpoints.

## Verification

<VERIFIED> Targeted local tests passed:

```text
python -m pytest -q tests/test_standard_s3_spinor_harmonics.py \
  tests/test_lawrence_i1r_failure_reproduction.py \
  tests/test_s3_spin_connection_lawrence_frame.py
8 passed
```

## Conclusion

<inference> The standard `S3` spinor-harmonic basis layer is now available for
future `V`-coupling integration.

<inference> This does not change the current Lawrence verdict:

```text
P5C verdict = standard_spinor_harmonics_required
runtime = research_only
V-selection rules = smoke_only
```

## Next Step

Use this basis as the input layer for any later `V`-selection integration work.

