# S3 Dirac Exact Baseline P0 Audit

Date: 2026-06-07

## Scope

[CODE] This report audits the current P0 exact clean Dirac baseline for the round three-sphere `S3`.

This is a reference spectrum for future checks. It is not:

- a numerical Dirac discretization;
- a spinor-transport graph operator;
- a kNN graph Dirac operator;
- an `SU(2)` instanton calculation;
- an index calculation;
- a spectral-flow or eta-invariant calculation;
- a validation or refutation of Tom Lawrence's theory.

## Implemented Baseline

[CODE] The baseline lives in:

```text
s3_dirac_exact_baseline.py
tests/test_s3_dirac_exact_baseline.py
```

[CODE] The implemented analytic spectrum is:

```text
lambda_{k,+/-} = +/- (k + 3/2) / R
degeneracy per sign = (k + 1)(k + 2)
k = 0, 1, 2, ...
R > 0
```

The function `analytic_dirac_spectrum_s3(k_max, radius)` returns records with:

```text
k
sign
eigenvalue
degeneracy
```

The helper `total_number_of_modes(k_max)` returns the degeneracy count for both spectral signs through `k_max`.

## Verified Properties

[VERIFIED-SYNTHETIC] The unit tests check:

- positive/negative spectral symmetry;
- no zero eigenvalues for the clean round `S3` baseline;
- first `R=1` levels: `+/-1.5`, `+/-2.5`, `+/-3.5`;
- degeneracies per sign: `2`, `6`, `12` for `k=0,1,2`;
- radius scaling: `lambda(R) = lambda(R=1) / R`;
- total counted modes through `k_max=2`: `(2 + 6 + 12) * 2 = 40`.

## Caveats

[NEEDS-REAL-DATA] This baseline has not yet been compared to a real numerical Dirac spectrum export.

[INFERRED] A future kNN or point-cloud Dirac operator would require additional mathematical structure before its eigenvalues can be interpreted:

- local tangent frames;
- spin structure;
- spin connection;
- parallel transport between sampled points;
- consistent gamma/Pauli matrices across local frames;
- Hermiticity/self-adjointness checks;
- convergence checks against this exact baseline.

[INFERRED] Until those structures are specified and verified, any low numerical modes from a graph construction should be treated as potential artifacts.

## Current Verdict

[VERIFIED-SYNTHETIC] P0 is suitable as an analytic negative control for clean `S3`.

[NEEDS-REAL-DATA] P0 is not yet a real-data benchmark result.

[INFERRED] The next safe step is an export/data contract and a P1 design specification, not immediate kNN Dirac implementation.
