# G84A Decision — Standard Gauge Reduction

**Date:** 2026-06-22  
**Verdict:** `DERIVED_POSITIVE_POWER_STANDARD_ANSATZ`

## Result

For the preregistered unwarped product action with constant dilaton and warp
prefactors, the reduced four-dimensional inverse gauge coupling scales with
the wrapped internal volume.

On `rho3 = C * rho6^2`:

| Gauge-sector support | Derived power |
|---|---:|
| bulk `S3 x S6` | `alpha = +12` |
| localized on `S3` | `alpha = +6` |
| localized on `S6` | `alpha = +6` |
| point-localized | `alpha = 0` |

Direct volume counting and symbolic logarithmic differentiation agree exactly.

## Weyl-frame result

For `g_J = Omega^2 g_E`,

`sqrt(-g) |F_p|^2 -> Omega^(d-2p) sqrt(-g_E) |F_p|_E^2`.

For a Yang–Mills two-form in `d=4`, the exponent is zero. Therefore the
four-dimensional Einstein-frame Weyl rescaling does not turn `+6` or `+12`
into `-2`.

The detector was checked with `d=5`, where the exponent is `+1`.

## Inverse-square requirement

To obtain `alpha = -2`, an additional radius-dependent prefactor must supply:

- bulk sector: `-14`;
- S3-localized sector: `-8`;
- S6-localized sector: `-8`.

Such a factor could only come from additional physics such as a running
dilaton, warped volume, duality, or a non-gauge-modulus spectral mechanism. It
is absent from the baseline action.

## Consequences

- Standard dimensional reduction does not support `T proportional to
  1/rho6^2`.
- `lambda_np = pi/9` remains unsupported.
- `lambda_v_operator` remains separate.
- The result is action-level only within the explicitly stated toy ansatz; it
  is not a microscopic string embedding.

## Next gate

`G84B_SPECTRAL_EXPONENTIAL_ORIGIN`

Test whether heat-kernel, proper-time, or determinant terms built from
eigenvalues `lambda_n^2 proportional to 1/rho6^2` can generate the implemented
functional form without identifying `1/rho6^2` as a gauge kinetic modulus.

## Reproduction

```bash
python tom_s3_spinor_toy/experiments/20260622-g84a-standard-gauge-reduction/g84a_standard_gauge_reduction.py
python -m pytest tom_s3_spinor_toy/tests/test_g84a_standard_gauge_reduction.py -q
python -m pytest tom_s3_spinor_toy/tests/test_g83_gauge_kinetic_modulus_scaling.py tom_s3_spinor_toy/tests/test_g54f_4d_eh_frame.py tom_s3_spinor_toy/tests/test_g28_spectral_action.py -q
python -m compileall -q tom_s3_spinor_toy
git diff --check
```
