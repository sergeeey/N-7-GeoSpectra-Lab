# S3 Dirac Eigenvalue Export Contract

Date: 2026-06-07

## Purpose

[CODE] This contract defines the minimum metadata required for any future real or numerical `S3` Dirac eigenvalue export to be compared against the exact P0 baseline.

The contract is designed to prevent ambiguous claims such as "zero modes appeared" or "the numerical operator matches the exact spectrum" without enough provenance to reproduce and interpret the run.

## Required Per-Row Fields

Every CSV-like row, or every equivalent structured record in NPZ/JSON/Parquet/H5/PKL, must include:

```text
eigenvalue
branch
k_label
```

Field meanings:

```text
eigenvalue
  Signed numerical or analytic eigenvalue.

branch
  Spectral sign/branch, for example "+" or "-".
  Do not call this chirality unless a chirality operator has been explicitly defined.

k_label
  Analytic level label if known. Use null/None/NaN if unknown.
```

## Required Run Metadata

Each export must include run-level metadata. This can be repeated in every CSV row, stored in a sidecar JSON, or stored as NPZ/H5 attributes.

Required fields:

```text
backend
geometry
operator_type
radius_R
k_max
j_max
N_points
k_neighbors
sampling_method
normalization
solver
commit_sha
run_id
zero_threshold
gap_threshold
```

Field meanings:

```text
backend
  Implementation backend, for example analytic_exact, spectral_wigner, hopf_grid,
  point_cloud_knn, or external_library.

geometry
  Geometry being tested, for example round_S3.

operator_type
  Operator actually diagonalized, for example exact_dirac, graph_laplacian,
  candidate_graph_dirac, or spectral_dirac.

radius_R
  Sphere radius used by the run.

k_max
  Maximum analytic Dirac level included, if applicable.

j_max
  Maximum representation cutoff, if applicable.

N_points
  Number of sampled points for graph/point-cloud runs. Use null for analytic runs.

k_neighbors
  kNN neighbor count for graph runs. Use null for non-graph runs.

sampling_method
  Sampling method, for example Haar_random, Hopf_grid, Euler_grid, deterministic_design,
  or not_applicable.

normalization
  Operator normalization convention, including any radius, graph-weight, or volume scaling.

solver
  Eigenvalue solver and relevant mode, for example dense_numpy_eigh,
  scipy_sparse_eigsh, or analytic_formula.

commit_sha
  Git commit SHA or null if unavailable. Do not fabricate this field.

run_id
  Stable run identifier.

zero_threshold
  Absolute threshold used to classify a numerical eigenvalue as zero.

gap_threshold
  Threshold used for spectral-gap claims.
```

## Claim Rules

[NEEDS-REAL-DATA] A synthetic or analytic export must be labelled as such and cannot be used as evidence for numerical convergence.

[INFERRED] For future graph or point-cloud Dirac runs, `branch` means spectral sign, not chirality, unless a chirality-like structure is explicitly defined and tested.

[INFERRED] A zero-mode claim requires at minimum:

- the export contract above;
- Hermiticity/self-adjointness evidence;
- stability under resolution/cutoff changes;
- a declared `zero_threshold`;
- comparison against the exact clean `S3` negative control;
- a clear statement of whether gauge fields are absent or present.

## Minimal CSV Header

For a flat CSV export, the recommended header is:

```text
run_id,commit_sha,backend,geometry,operator_type,radius_R,k_max,j_max,N_points,k_neighbors,sampling_method,normalization,solver,zero_threshold,gap_threshold,k_label,branch,eigenvalue
```

## Status

[CODE] This contract is documentation only. It does not create real eigenvalue data.

[NEEDS-REAL-DATA] No real `S3` kNN Dirac eigenvalue export is currently available in this project.
