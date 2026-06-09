# S3 Dirac Temporary Coupling Smoke P1d

Date: 2026-06-07

## Scope

[CODE] This report records the direct Haar-unit coframe smoke layer for:

```text
D = D0 + V
```

at:

```text
k_max <= 3
```

This is not:

- final Ben Achour `E/E'` one-form normalization;
- a physical homogeneous `SU(2)` gauge-background result;
- an instanton calculation;
- an index calculation;
- a chirality claim;
- a spectral-flow or eta-invariant calculation;
- a zero-mode claim;
- validation of Tom Lawrence's theory.

## Temporary Convention

[CODE] The exact direct Haar-unit coframe convention is:

```text
ANALYTIC_DIRECT_HAAR_CONVENTION
||e^i|| scale = 1
```

The final Ben Achour basis mapping remains:

```text
final_ben_achour_normalization = unresolved
```

## Implemented Files

[CODE] The smoke layer uses:

```text
s3_reduced_matrix_elements.py
s3_coupling_v_option_b.py
s3_dirac_with_temp_coupling.py
tests/test_s3_dirac_temp_coupling.py
```

## Operator Contract

[CODE] `build_temp_coupled_dirac(k_max<=3, lambda_val=1.0, radius=1.0, alpha=None)` returns:

```text
D
D0
V
metadata
```

where:

```text
D0 = clean diagonal spectral Dirac prototype
V  = current symbolic Option B coupling scaffold with direct Haar-unit scale
D  = D0 + V
```

## Verification Contract

[VERIFIED-SYNTHETIC] Tests verify:

- `lambda_val = 0` returns `D0`;
- `D` is Hermitian;
- `V` is nonzero for `lambda_val = 1`;
- matrix dimensions match `total_number_of_modes(k_max)` within the supported smoke range;
- metadata includes `ANALYTIC_DIRECT_HAAR_CONVENTION`;
- final Ben Achour normalization is explicitly unresolved.

## Claim Discipline

[CODE] Allowed wording:

```text
Direct Haar-unit coframe smoke layer for D0 + V is implemented and Hermitian.
```

Forbidden wording:

```text
We have a physical gauge-background spectrum.
We found or excluded zero modes.
We verified an index.
We implemented an instanton.
The Ben Achour normalization is closed.
```

## Next Safe Step

[INFERRED] A spectrum visualization may be produced only as an engineering/debug artifact and must be labelled:

```text
preliminary
exact direct Haar-unit coframe scale
separate Ben Achour E/E' basis mapping unresolved
no physical claims
```

[CODE] Supported smoke range:

```text
0 <= k_max <= 3
```

