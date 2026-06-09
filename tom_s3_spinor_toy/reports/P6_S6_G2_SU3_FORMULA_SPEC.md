# P6 S6 / G2 / SU(3) Formula Spec

Date: 2026-06-08

Scope: define the next first-class track for the six-sphere side of the
project. This is separate from the validated S3 spinor-basis layer.

## Executive Position

[INFERRED] `S6` should be treated as a separate homogeneous-space problem:

```text
S6 ≅ G2 / SU(3)
```

[INFERRED] The right first step is a formula specification, not a claim about
`SU(4)` or hypercharge.

## Primary References Used

[CODE] The spec is grounded in the following primary references:

- Chrysikos, Gustad, Winther: invariant connections on strongly isotropy
  irreducible homogeneous spaces, including the relevant classification of
  invariant metric connections with skew torsion on non-symmetric cases.
- Camporesi & Higuchi: homogeneous-space Dirac eigenfunctions and the
  Casimir/radial-part derivation.
- Macfarlane / standard G2–S6 references: `S6` viewed as `G2/SU(3)` and the
  explicit relation between the `G2/SU(3)` coset and the round six-sphere.

[INFERRED] The user-found note about homogeneous-space Dirac operators is
useful as a cross-check against the standard `D = C_G + (1/8)s` template.

## What Is Fixed at Spec Level

### 1. Geometry target

```text
M6 = G2 / SU(3)
```

[INFERRED] The six-sphere should be treated as a homogeneous nearly Kähler / 
naturally reductive geometry with a canonical connection candidate and, where
needed, a family of invariant metric connections with skew torsion.

### 2. Representation target

[INFERRED] The isotropy representation is the SU(3) representation carried by
the tangent space at the base point. For the audit, the exact decomposition of
the tangent and spin bundles must be specified before any spectral claim.

### 3. Dirac baseline target

[INFERRED] The homogeneous-space Dirac operator should be checked against the
Casimir baseline:

```text
D ~ C_G + (1/8) s
```

[INFERRED] This is a validation target, not a claim that the final spectrum has
already been computed for the project.

### 4. Connection target

[INFERRED] The implementation spec must distinguish:

- Levi-Civita connection;
- canonical homogeneous connection;
- any invariant skew-torsion family if used;
- the final choice of connection for the baseline operator.

## Required Formula Blocks for the Future S6 Implementation

### A. Reductive decomposition

Specify the reductive split:

```text
g2 = su(3) ⊕ m
```

and the induced isotropy action on `m`.

### B. Metric and scale

Fix the homogeneous metric normalization before any operator assembly.
Record whether the reference normalization is:

- round `S^6` normalization,
- canonical homogeneous normalization,
- or a rescaled convention chosen only for smoke testing.

### C. Spinor bundle

Specify the spinor bundle convention on `S6` and the chosen spin representation
labels before computing matrix elements.

### D. Dirac operator

Specify the exact operator formula under the chosen connection:

```text
D = gamma^a (∂_a + spin connection terms + possible torsion terms)
```

and derive the equivalent homogeneous-space / Casimir form used as the spectral
cross-check.

### E. Selection rules

Any future `S6` coupling or matrix-element rule must be derived from the chosen
representation data, not from the `S3` selection rule scaffold.

## What This Spec Does NOT Claim

- does not claim an `SU(4)` gauge decomposition;
- does not claim hypercharge;
- does not claim an instanton or index result;
- does not claim a final spectrum has already been implemented;
- does not mix with the validated `S3` basis layer;
- does not alter `V-selection rules` in the `S3` track.

## Acceptance Criteria for the Next S6 Gate

1. A clear `G2/SU(3)` geometry and connection choice is written down.
2. The Dirac operator baseline is fixed in that convention.
3. A Casimir-based cross-check is available.
4. The convention is explicit enough that a future test can be written without
   ambiguity.
5. The result stays separated from the `S3` basis work.

## Next Gate

```text
P6_S6_G2_SU3_FORMULA_SPEC = drafted
P6_S6_G2_SU3_IMPLEMENTATION = not started
runtime = research_only
V-selection rules = smoke_only
```

