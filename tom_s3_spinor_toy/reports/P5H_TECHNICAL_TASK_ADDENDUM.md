# P5H Technical Task Addendum

Date: 2026-06-08

This addendum captures the useful external information gathered for the current
`S3` / `S6` research split. It is intentionally conservative: it adds
structure, not claims.

## What Is Useful Right Now

### 1. Kosmann lift is a reference, not a rescue proof

[INFERRED] The Kosmann formula for spinor fields is useful as a geometric
reference, but it does **not** by itself prove that the original Lawrence
scalar/spinor ansatz is rescued.

[INFERRED] The current repository state still treats the Kosmann path as an
explored alternative, not as a promoted runtime verdict.

### 2. S6 has a first-class homogeneous-space reference

[INFERRED] The search result you found is directly useful for the separate `S6`
track:

- `S6 = G2/SU(3)` as a strongly isotropy irreducible homogeneous space;
- invariant connection families with skew torsion are available in the
  literature;
- the isotropy representation is of complex type;
- this gives a real baseline for a later `S6` formula spec.

[INFERRED] This means the `S6` track should begin from a formula specification
and homogeneous-space baseline, not from a free-form claim about `SU(4)` or
hypercharge.

### 3. Homogeneous Dirac/Casimir baseline is the right cross-check

[INFERRED] The homogeneous-space Dirac formula you found is a useful
cross-check:

```text
D = C_G + (1/8) s
```

[INFERRED] For `S3`, this is consistent with the existing exact clean baseline.
For `S6`, it suggests a future Casimir-based baseline should be part of the
design before any spectrum interpretation.

## What This Changes in the Task

### Keep

- the validated standard `S3` spinor basis;
- the explicit non-Cartan coordinate generators;
- the commutator convention audit;
- the current `V` scaffold as a smoke layer only.

### Do Not Promote

- do not promote `Kosmann` to a rescue proof;
- do not promote `V-selection rules` above `smoke_only`;
- do not mix `S6` into the `S3` spinor-basis task;
- do not start `SU(4)` or hypercharge interpretation from the current `S3`
  layer.

## Suggested Next Technical Gates

### For `S3`

```text
P5H_S3_CAS_ORACLE_REVIEW
```

Use this only if a fully symbolic or published coordinate-space proof is added
for the non-Cartan ladder action or if the current basis layer needs a formal
oracle cross-check beyond the smoke tests.

### For `S6`

```text
P6_S6_G2_SU3_FORMULA_SPEC
```

Use this as the first gate for the separate `S6` track. The gate should start
from:

- the `G2/SU(3)` homogeneous-space geometry;
- the invariant connection family from the literature;
- the Casimir-based Dirac baseline;
- a clear statement of what is and is not being claimed.

## Bottom Line

```text
Kosmann = reference only
S6 = separate first-class track
V-selection rules = smoke_only
runtime = research_only
```

