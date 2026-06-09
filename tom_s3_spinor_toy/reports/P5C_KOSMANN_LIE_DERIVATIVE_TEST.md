# P5C Kosmann Lie Derivative Test

Date: 2026-06-08

Scope: test whether the Kosmann / spinorial Lie derivative rescues the recovered
Lawrence fundamental spinor ansatz on `S3`.

## Executive Verdict

<fact> The recovered Lawrence scalar-dragging ansatz is not promoted to a full
non-Cartan spinor representation by the Kosmann path in the current analysis.

<inference> The correct next step is to switch to the standard `S3` spinor
harmonics / Killing spinor basis rather than to keep iterating on the scalar
ansatz.

```text
standard_spinor_harmonics_required
```

## Evidence

<fact> The `S3` coframe used in the Lawrence frame is:

```text
e^1 = rho d alpha
e^2 = rho sin(alpha) d theta
e^3 = rho cos(alpha) d theta_tilde
```

<fact> The torsion-free Cartan equations imply the nonzero connection 1-forms:

```text
omega_12 = - cos(alpha) d theta
omega_13 = + sin(alpha) d theta_tilde
```

<inference> These terms are exactly the pieces that must enter the spin
covariant derivative and the Kosmann derivative; scalar dragging alone omits
them.

<fact> External spin-geometry references confirm that the lowest spinors on `S3`
are Killing spinors / spinor eigensolutions and form the expected two-dimensional
`(1/2, ±1/2)` representations of `so(4)`.

## Remaining Conclusion

<inference> Because the recovered Lawrence ansatz is still scalar-separable and
its non-Cartan coefficients remain `alpha`-dependent, the safe implementation
path is to replace it by standard `S3` spinor harmonics.

## Next Gate

```text
P5C_STANDARD_S3_SPINOR_HARMONICS_IMPLEMENTATION
```

## Verification

<VERIFIED> Targeted regression checks passed locally:

```text
python -m pytest -q tests/test_lawrence_i1r_failure_reproduction.py tests/test_s3_spin_connection_lawrence_frame.py
4 passed
```

<VERIFIED> This preserves the P5C conclusion:

```text
standard_spinor_harmonics_required
research_only
V-selection rules = smoke_only
```
