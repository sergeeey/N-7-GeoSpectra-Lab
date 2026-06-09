# S3 Dirac P1c Gauge Background Design Gate

Date: 2026-06-07

## Scope

[CODE] This design gate defines safe next options for extending the clean diagonal `S3` spectral Dirac prototype with a gauge-background term.

This document does not implement an operator and does not claim:

- an `SU(2)` instanton result;
- an index theorem result;
- zero modes;
- spectral flow;
- eta invariant;
- validation of Tom Lawrence's theory.

## Current Starting Point

[CODE] The current implemented stack is:

```text
P0: s3_dirac_exact_baseline.py
P1a: s3_spinor_spectral_labels.py
P1b: s3_dirac_spectral_operator.py
```

[VERIFIED-SYNTHETIC] P1b builds a diagonal sparse matrix in the exact clean spectral branch basis and reproduces:

```text
lambda_{k,+/-} = +/- (k + 3/2) / R
degeneracy per sign = (k + 1)(k + 2)
```

[INFERRED] This is a clean negative-control operator. A gauge-background extension must be treated as a new mathematical problem, not as a trivial modification of the diagonal baseline.

## Main Risk

[INFERRED] A 4D BPST instanton is not automatically a 3D `S3` object. On `S3`, the safer language is:

- an `SU(2)` background connection on `S3`;
- a homogeneous connection on `S3 ~= SU(2)`;
- a boundary/spectral-flow setup related to a 4D instanton;
- or a full 4D Dirac problem.

[HYPOTHESIS] If these are mixed, false low modes or invalid index claims are likely.

## Option A: Pure Spectral Toy Hermitian SU(2) Perturbation

### Operator

[INFERRED] A finite-dimensional Hermitian perturbation of the P1b diagonal matrix:

```text
D_toy = D_clean + epsilon * V
V = V^\dagger
```

where `V` is built in the spectral branch basis with explicit selection rules.

### Required Data / Formulas

- a declared finite cutoff;
- a deterministic Hermitian matrix construction;
- selection rules, even if toy-level;
- perturbation strength `epsilon`;
- random seed only if the toy perturbation is stochastic.

### Matrix Elements

[INFERRED] Matrix elements can be synthetic/toy couplings between compatible spectral labels. They must not be described as physical gauge couplings.

### Hermiticity Check

```text
||D_toy - D_toy^\dagger|| = 0
```

or a declared numerical tolerance if floating-point couplings are used.

### Allowed Claim

[VERIFIED-SYNTHETIC] This can test matrix infrastructure: Hermiticity, branch bookkeeping, cutoff handling, and spectral stability diagnostics.

### Forbidden Claim

This cannot claim:

- physical `SU(2)` gauge coupling;
- instanton;
- index;
- zero mode;
- Tom-theory support.

### Kill Criteria

- Hermiticity fails.
- The toy term is not explicitly labelled synthetic.
- The implementation starts producing physical claims.

### Verdict

```text
GO_ONLY_AS_TOY_INFRASTRUCTURE_TEST
```

## Option B: Homogeneous SU(2) Connection On S3 ~= SU(2)

### Operator

[INFERRED] A Dirac operator coupled to a geometrically defined `SU(2)` connection on the group manifold:

```text
D_A = D_clean + gamma^a A_a
```

where `A_a` is expressed in a left- or right-invariant coframe on `S3 ~= SU(2)`.

### Required Data / Formulas

- explicit coframe convention;
- gamma/Pauli matrix convention;
- `SU(2)` gauge generator convention;
- coupling constant;
- representation of the spinor under the gauge group;
- matrix elements in the spectral/Wigner basis;
- measure and inner product.

### Matrix Elements

[INFERRED] Matrix elements should be derived from `SU(2)` representation theory, likely through Clebsch-Gordan / Wigner `3j`-type couplings. This is the first physically/geometrically meaningful `S3` gauge-background candidate.

### Hermiticity Check

- analytic Hermiticity of the connection term under the chosen inner product;
- numerical sparse-matrix check after truncation;
- stability under cutoff increase.

### Allowed Claim

[INFERRED] If implemented and tested, this can claim a controlled `S3` homogeneous gauge-background spectral experiment.

### Forbidden Claim

Do not call this a BPST instanton unless a precise 4D relation or boundary construction is supplied.

Do not claim index or zero modes from this alone.

### Kill Criteria

- no explicit coframe/gauge convention;
- no inner-product/Hermiticity proof or check;
- spectrum changes under cutoff in an uncontrolled way;
- representation labels are inconsistent with P1a.

### Verdict

```text
BEST_CANDIDATE_FOR_REAL_P1C_AFTER_FORMULA_SPEC
```

## Option C: Boundary / Spectral-Flow Picture Of 4D BPST Instanton

### Operator

[INFERRED] A family of 3D Dirac operators on `S3` slices or boundary data associated with a 4D instanton configuration.

### Required Data / Formulas

- the 4D manifold and metric;
- instanton gauge potential;
- relation between 4D radial/time coordinate and the `S3` slice;
- induced 3D connection on each slice;
- spectral-flow parameter;
- boundary conditions;
- eta-invariant or APS-type framework if index language is used.

### Matrix Elements

[INFERRED] Matrix elements are slice-dependent and require a parameterised family, not one fixed `S3` matrix.

### Hermiticity Check

- Hermiticity for each slice operator;
- spectral continuity across the flow parameter;
- convergence under cutoff.

### Allowed Claim

[INFERRED] With a full setup, this can study spectral flow related to a 4D instanton.

### Forbidden Claim

Do not claim the result from a single fixed diagonal `S3` matrix.

Do not call a toy perturbation an instanton boundary problem.

### Kill Criteria

- no explicit 4D gauge field;
- no flow parameter;
- no boundary condition / APS framework;
- zero-mode claim appears before the setup is defined.

### Verdict

```text
DESIGN_RESEARCH_ONLY
```

## Option D: Full 4D Instanton Dirac Problem

### Operator

[INFERRED] A 4D Dirac operator coupled to a BPST instanton on a specified 4D geometry.

### Required Data / Formulas

- 4D spin geometry;
- 4D gamma matrices;
- BPST gauge potential;
- gauge representation;
- boundary/compactification conditions;
- numerical or analytic solution strategy;
- index theorem setup.

### Matrix Elements

[INFERRED] This is not an `S3` spectral-matrix extension. It is a separate 4D project.

### Hermiticity Check

Depends on Euclidean/Lorentzian signature and boundary conditions.

### Allowed Claim

Only after a dedicated 4D formulation and verification.

### Forbidden Claim

Do not use the current P1b `S3` diagonal prototype as evidence for this.

### Kill Criteria

- attempted implementation inside the current P1b scaffold;
- missing 4D geometry;
- index claim without a full index setup.

### Verdict

```text
OUT_OF_SCOPE_FOR_CURRENT_TRACK
```

## Recommended Next Step

[INFERRED] The next safe step is not physical instanton code. It is:

```text
P1c_NEXT = Option B formula specification
```

Minimum deliverable before code:

- choose left- or right-invariant `S3` coframe;
- define gamma/Pauli conventions;
- define `SU(2)` gauge representation;
- write a candidate homogeneous connection `A`;
- derive or cite the spectral/Wigner matrix-element selection rules;
- state the inner product;
- specify Hermiticity checks;
- define what spectrum comparison is allowed.

## Backlog

[INFERRED] These remain backlog:

- toy Hermitian perturbation infrastructure test;
- physical homogeneous `SU(2)` connection implementation;
- boundary/spectral-flow instanton design;
- full 4D instanton Dirac problem;
- index/chirality/zero-mode claims.

## Claim Discipline

[CODE] Until a gauge-background design is fully specified and tested, allowed wording is:

```text
We have a clean exact S3 spectral Dirac baseline and a diagonal spectral prototype.
We are designing possible gauge-background extensions.
```

Forbidden wording:

```text
We implemented an SU(2) instanton.
We verified an index.
We found zero modes.
The current S3 matrix proves a gauge-field claim.
```
