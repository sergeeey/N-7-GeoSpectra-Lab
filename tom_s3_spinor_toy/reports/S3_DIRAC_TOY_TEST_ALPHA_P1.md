# S3 Dirac Toy Test Alpha P1

Date: 2026-06-07

## Scope

[CODE] This is a pre-registered engineering smoke test for:

```text
D = D0 + alpha V
```

with:

```text
k_max = 3
alpha = DIRECT_HAAR_ONE_FORM_SCALE = 1
```

This report does not claim:

- a physical homogeneous `SU(2)` gauge-background result;
- an instanton;
- an index theorem result;
- chirality;
- spectral flow;
- eta invariant;
- zero modes;
- validation of Tom Lawrence's theory.

## Temporary Convention

[CODE] The exact direct Haar/unit-coframe convention is:

```text
ANALYTIC_DIRECT_HAAR_CONVENTION
||e^i|| scale = 1
final_ben_achour_normalization = unresolved
```

## Operator

[CODE] The smoke-layer operator is implemented in:

```text
s3_dirac_with_temp_coupling.py
```

and uses the current symbolic Option B scaffold from:

```text
s3_coupling_v_option_b.py
s3_reduced_matrix_elements.py
```

[CODE] The clean reference operator is:

```text
D0 = build_dirac_matrix(k_max=3, radius=1.0)
```

[CODE] The coupled smoke operator is:

```text
D = D0 + V
```

with `V` being a branch-paired engineering projection of the symbolic scaffold.

## Pre-Registered Checks

[VERIFIED-SYNTHETIC] The smoke test was pre-registered to check:

1. `D` is Hermitian.
2. `D != D0` because `V` has nonzero off-diagonal entries.
3. `alpha = 0` returns `D0`.
4. The spectrum stays outside `|lambda| < 1.0`.
5. The spectrum is symmetric about zero.
6. Metadata contains `ENGINEERING_ALPHA` and a direct-Haar normalization warning.

All checks passed.

## Dimension

[CODE] For `k_max = 3`:

```text
total_number_of_modes(3) = 80
```

## First 10 Eigenvalues

[VERIFIED-SYNTHETIC] Sorted eigenvalues of `D` and `D0`:

| index | D0 | D |
|---:|---:|---:|
| 1 | -4.500000000000 | -4.552435702403 |
| 2 | -4.500000000000 | -4.552435702403 |
| 3 | -4.500000000000 | -4.552435702403 |
| 4 | -4.500000000000 | -4.552435702403 |
| 5 | -4.500000000000 | -4.552435702403 |
| 6 | -4.500000000000 | -4.552435702403 |
| 7 | -4.500000000000 | -4.552435702403 |
| 8 | -4.500000000000 | -4.552435702403 |
| 9 | -4.500000000000 | -4.529054582610 |
| 10 | -4.500000000000 | -4.529054582610 |

[VERIFIED-SYNTHETIC] The last 10 eigenvalues are the sign-mirrored partners of the above values, so the spectrum is symmetric to numerical precision.

## Interpretation

[INFERRED] The direct Haar-unit coframe coupling produces systematic but small symmetric shifts relative to `D0`.

[INFERRED] No numerical artifacts were detected by the smoke criteria:

- Hermiticity norm stayed below the threshold;
- the spectrum remained symmetric about zero;
- the smallest absolute eigenvalue stayed above `1.0`.

[UNCERTAIN] This remains an engineering smoke result, not a physical claim.

## Metadata

[VERIFIED-SYNTHETIC] The operator metadata exposes:

```text
ENGINEERING_ALPHA = 1
warning = direct Haar/unit-coframe normalization; final Ben_Achour basis mapping unresolved
normalization_status = ANALYTIC_DIRECT_HAAR_CONVENTION
```

## Verdict

[VERIFIED-SYNTHETIC] The pre-registered engineering smoke test passed.

[INFERRED] The `D = D0 + alpha V` pipeline is numerically stable on `k_max=3` under the direct Haar-unit coframe convention.

[CODE] No physical interpretation should be attached to this result until the Ben Achour `E/E'` basis mapping is separately closed.
