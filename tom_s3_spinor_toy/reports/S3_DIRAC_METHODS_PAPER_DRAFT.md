# S3 Dirac Methods Paper Draft

Date: 2026-06-07

## Title

Exact Baseline and Engineering Smoke Layers for a Spectral S3 Dirac Pipeline

## Abstract

[CODE] We present a reproducible methods pipeline for a spectral S3 Dirac scaffold built around an exact clean baseline `D0`, a symbolic coupling scaffold `V`, and a preliminary spectrum sweep `D(lambda) = D0 + lambda V` under the direct Haar/unit-coframe convention.

[UNCERTAIN] This is a methods artifact only. It does not claim a physical homogeneous `SU(2)` gauge-background spectrum, an instanton, an index theorem result, chirality, spectral flow, eta invariants, zero modes, or validation of Tom Lawrence's theory.

## Core Contract

[CODE] The current working convention is:

```text
ANALYTIC_DIRECT_HAAR_CONVENTION
||e^i|| scale = 1
final_ben_achour_normalization = unresolved
```

[CODE] The separate Ben Achour `E/E'` basis mapping remains unresolved as a representation-detail problem and is not used as a physical claim.

## Pipeline Summary

### P0: Exact Baseline

[VERIFIED-SYNTHETIC] The clean baseline operator is:

```text
D0
```

with exact spectrum:

```text
lambda_{k, +/-} = +/- (k + 3/2) / R
```

and per-branch degeneracy:

```text
(k + 1)(k + 2)
```

### P1a: Spectral Labels

[VERIFIED-SYNTHETIC] Spectral spinor labels were scaffolded in a way compatible with the exact baseline and the `SU(2)_L x SU(2)_R` bookkeeping.

### P1b: Spectral Operator Prototype

[VERIFIED-SYNTHETIC] A diagonal spectral prototype reproduces the exact baseline spectrum and Hermiticity.

### P1c: Gauge-Background Design

[VERIFIED-SYNTHETIC] The option-B gauge-background design gate selected a homogeneous `SU(2)` connection as the only safe next step.

### P1d: Coupled Smoke Layer

[VERIFIED-SYNTHETIC] The coupled smoke operator is:

```text
D(lambda) = D0 + lambda V
```

with the smoke range supported for:

```text
0 <= k_max <= 3
```

## Quantitative Result

[VERIFIED-SYNTHETIC] Exact-scale sweep summary at `k_max = 3` and `lambda in linspace(0, 1, 11)`:

```text
max_abs_shift  = 0.06112145532459046
mean_abs_shift = 0.031405583903139744
l2_shift       = 0.3520593881833174
min_abs_final  = 1.5206906325745546
max_symmetry_violation = 0.0
```

[VERIFIED-SYNTHETIC] The endpoint spectrum remains symmetric about zero, with smooth small shifts relative to `D0`.

## Numerical Diagnostics

[VERIFIED-SYNTHETIC] The following checks are green:

- `D` is Hermitian;
- `V` is nonzero;
- `lambda = 0` returns `D0`;
- the smoke spectrum avoids `|lambda| < 1.0`;
- the spectrum is symmetric about zero;
- metadata records the direct Haar convention.

## Interpretation

[INFERRED] The current pipeline is stable enough for methods-style reporting and for reproducible engineering discussion.

[UNCERTAIN] The observed shifts should not be interpreted as a physical gauge-background result until the separate Ben Achour `E/E'` basis mapping is closed.

## Claims Allowed in This Draft

[CODE] Allowed:

```text
exact baseline
preliminary spectrum sweep
engineering smoke layer
reproducible spectrum visualization
direct Haar-unit coframe convention
pending separate Ben Achour E/E' basis mapping
```

[CODE] Forbidden:

```text
physical spectrum
instanton
index
zero modes
Tom validation
final normalization
```

## Reproducibility

[CODE] The methods stack is backed by green tests and versioned report artifacts.

[VERIFIED-SYNTHETIC] Current full test status:

```text
72 passed, 12 warnings
```

[UNCERTAIN] Warnings are the existing `np.trapz` deprecation in `geometry_s3_hopf.py`; they do not affect the current methods conclusion.

