# S3 One-Form Norm Numerical P1

Date: 2026-06-07

## Scope

[CODE] This report records a safe numerical norm diagnostic for the left-invariant coframe on unit `S3`.

Despite the task label `P1-NORM-NUMERICAL`, this is not a kNN connection-Laplacian implementation. A one-form graph connection Laplacian would require a validated discrete connection and parallel transport rule. That remains out of scope for this diagnostic.

This report does not claim:

- Ben Achour `E/E'` analytic normalization is closed;
- physical gauge-background spectrum;
- instanton;
- index;
- chirality;
- spectral flow;
- eta invariant;
- zero modes.

## Method

[CODE] Module:

```text
s3_oneform_laplacian_numerical.py
```

Function:

```text
compute_e_coframe_norm_numerical(n_points=5000, k_neighbors=20)
```

The function:

- samples points uniformly on unit `S3` by Muller normalization;
- constructs the left-invariant frame from quaternion left multiplication by `i,j,k`;
- computes the pointwise Gram matrix of the frame in the ambient `R4` metric;
- averages the Gram matrix over the sampled points;
- reports diagnostic Gram eigenvalues.

[CODE] `k_neighbors` is accepted only for API continuity with the rejected graph-Laplacian design. No kNN graph is built.

## Numerical Results

[VERIFIED-SYNTHETIC] With deterministic seed `20260607`:

```text
n_points = 200
raw_component_norm_mean = 1.0
scale_to_direct_haar_norm = 1.0
diagnostic_spectrum = [1.0, 1.0, 1.0]

n_points = 2000
raw_component_norm_mean = 1.0
scale_to_direct_haar_norm = 1.0
diagnostic_spectrum = [1.0, 1.0, 1.0]
```

## Interpretation

[VERIFIED-SYNTHETIC] The embedded left-invariant frame is orthonormal pointwise in the unit `S3` metric:

```text
<e_i, e_j> = delta_ij
```

[INFERRED] Therefore the raw numerical norm diagnostic is consistent with unit coframe normalization.

[CODE] The current exact direct Haar/unit-coframe convention used by the `D0 + V` smoke layer is:

```text
ANALYTIC_DIRECT_HAAR_CONVENTION
||e^i|| scale = 1
```

[INFERRED] The diagnostic confirms that the raw unit coframe is already exact under the direct Haar convention:

```text
1
```

## Caveats

[UNCERTAIN] This does not close the Ben Achour `E/E'` one-form normalization. It only checks the invariant coframe's ambient-metric norm.

[NEEDS-REAL-DATA] This is not a real numerical one-form Laplacian spectrum and cannot be used as evidence for graph discretization convergence.

[INFERRED] It can be used as a reference for the engineering smoke convention, not for quantitative physics claims.

## Current Verdict

[VERIFIED-SYNTHETIC] The raw left-invariant coframe norm is numerically stable and matches the direct Haar unit scale as expected.

[UNCERTAIN] Final Ben Achour `E/E'` analytic normalization remains unresolved.
