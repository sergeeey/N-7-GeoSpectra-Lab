# S3 Dirac Methods Paper Outline

Date: 2026-06-07

## Working Title

Exact Baseline and Engineering Smoke Layers for a Spectral S3 Dirac Pipeline

## Core Message

[CODE] The paper should present a reproducible engineering pipeline for a spectral S3 Dirac scaffold:

```text
D0 -> spectral label scaffold -> diagonal spectral prototype -> homogeneous SU(2) smoke coupling -> exact-scale spectrum sweep
```

[UNCERTAIN] The paper must not claim a physical homogeneous gauge-background result until the separate Ben Achour `E/E'` basis mapping is closed.

## Proposed Sections

### 1. Introduction

- why the exact baseline matters;
- why claim discipline matters;
- why the S3 Dirac scaffold is useful as an engineering benchmark.

### 2. Exact Baseline

- clean Dirac spectrum on unit S3;
- degeneracy bookkeeping;
- no zero modes on the clean baseline.

### 3. Spectral/Wigner Scaffold

- label conventions;
- `SU(2)_L x SU(2)_R` bookkeeping;
- direct compatibility with the clean baseline.

### 4. Coupling Scaffold

- homogeneous `SU(2)` smoke coupling;
- Hermitian `V`;
- exact direct Haar/unit-coframe convention;
- unresolved Ben Achour basis mapping kept separate.

### 5. Exact-Scale Sweep

- `D(lambda) = D0 + lambda V`;
- sweep over `lambda in [0, 1]`;
- symmetric, smooth branch shifts;
- numerical safety checks.

### 6. Numerical Diagnostics

- Hermiticity;
- spectral symmetry;
- minimum absolute eigenvalue threshold;
- stable endpoint behavior.

### 7. Scope and Limits

- no instanton claim;
- no index claim;
- no chirality claim;
- no physical gauge-background claim;
- no validation of Tom Lawrence's theory.

### 8. Reproducibility

- green test suite;
- report artifacts;
- exact metrics;
- exact direct Haar convention.

## Figures

### Figure 1

Clean exact spectrum `D0` versus coupled preliminary sweep `D(lambda=1)`.

### Figure 2

Eigenvalue trajectories across `lambda in [0, 1]`.

### Figure 3

Smoke-test diagnostics summary: Hermiticity, symmetry, and minimum absolute eigenvalue.

## Tables

### Table 1

Exact baseline spectrum formula and degeneracies.

### Table 2

First 10 eigenvalues at `lambda=0` and `lambda=1`.

### Table 3

Quantitative sweep metrics:

```text
max_abs_shift
mean_abs_shift
l2_shift
min_abs_final
max_symmetry_violation
```

## Claim Discipline

[CODE] Allowed:

```text
exact baseline
preliminary spectrum sweep
engineering smoke layer
direct Haar-unit coframe convention
methods paper
reproducible pipeline
```

[CODE] Forbidden:

```text
physical spectrum
instanton
index
zero modes
Tom validation
final normalization
gauge-background claim
```

## Next Actions

1. Turn the outline into a compact methods draft structure.
2. Keep the exact-scale sweep and diagnostics as the main result.
3. Leave the Ben Achour `E/E'` basis mapping as a separate unresolved note.
