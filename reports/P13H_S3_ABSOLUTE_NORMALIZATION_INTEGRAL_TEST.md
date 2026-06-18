# P13H — S3 Absolute Normalization Integral Test

**Gate:** P13H | **Status:** completed | **Runtime:** research_only

## Scope Fence

Single explicit low-mode S3 integral smoke. Does NOT verify physical V-selection,
coupling strength, fermion generations, SM, or runtime safety.

## Volume element

`dVol = rho^3 * sin(alpha) * cos(alpha) d_alpha d_theta d_theta_tilde`

## Primary pair (P13B1)

`(0, 1)` — matrix element = `coefficient * lambda`

| Quantity | Value |
|----------|-------|
| coefficient (CONV_HAAR_UNIT) | `0j` |
| |M_ij| | `0.000000e+00` |
| P11 pattern compatible | `True` |
| Hermiticity max error | `0.000000e+00` |

## Convention invariance (diagonal 1,1)

| Convention | coeff_11 |
|------------|----------|
| CONV_HAAR_UNIT | `(-8.879766255631694e-09+0j)` |
| CONV_HAAR_HARMONIC_SQRT2 | `(1.5883699688856723e-08+0j)` |
| relative change | `1.559049` |
| invariant | `False` |

## Classification

**`NORMALIZATION_DEPENDENT_NO_GO`**

- lambda: `FREE_COUPLING_PARAMETER`
- P13E/P13F NO_GO preserved: `True`
- promotion: `forbidden_without_separate_gate`

## Frozen inputs (unchanged)

P13A–P13G statuses not modified. P13E remains `NORMALIZATION_DEPENDENT_NO_GO`.

## Raw metrics

```json
{
  "gate_id": "P13H",
  "volume_element": "dVol = rho^3 * sin(alpha) * cos(alpha) d_alpha d_theta d_theta_tilde",
  "hermiticity_max_error": 0.0,
  "primary_pair": [
    0,
    1
  ],
  "primary_coefficient": {
    "re": 0.0,
    "im": 0.0
  },
  "primary_matrix_element": {
    "re": 0.0,
    "im": 0.0
  },
  "p11_pattern_compatible": true,
  "coeff_11_unit": {
    "re": -8.879766255631694e-09,
    "im": 0.0
  },
  "coeff_11_sqrt2": {
    "re": 1.5883699688856723e-08,
    "im": 0.0
  },
  "convention_invariant_for_diagonal_11": false,
  "classification": "NORMALIZATION_DEPENDENT_NO_GO",
  "lambda_role": "FREE_COUPLING_PARAMETER",
  "p13e_status_preserved": true,
  "runtime": "research_only",
  "safe_for_runtime": false,
  "selection_rules": "smoke_only",
  "promotion": "forbidden_without_separate_gate",
  "details": {
    "primary_sqrt2_coeff": {
      "re": 0.0,
      "im": 0.0
    },
    "p12_scale_class_primary": null,
    "p12_scale_class_11": "normalization_dependent",
    "relative_diagonal_11_change": 1.559048989188667,
    "grid_n": 24
  }
}
```
