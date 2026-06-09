# S3 Ben Achour One-Form Normalization P1c

Date: 2026-06-07

## Scope

[CODE] This report audits whether the homogeneous left-invariant coframe component `e^i` can be assigned a final Ben Achour `E/E'` one-form normalization for the current Option B coupling scaffold.

No code is changed by this report. No spectrum is computed. No `D = D0 + V` matrix is built. No instanton, index, chirality, spectral-flow, eta-invariant, crossing, or zero-mode claim is made.

## Inputs From Ben Achour et al.

[CODE] The local project uses the Ben Achour Hopf coordinate convention:

```text
alpha in [0, pi/2]
ds^2 = d alpha^2 + cos^2(alpha) d theta^2 + sin^2(alpha) d phi^2
dmu = sin(alpha) cos(alpha) d alpha d theta d phi
```

[CODE] The paper defines Killing one-forms:

```text
xi  = partial_phi + partial_theta
xi' = partial_phi - partial_theta
```

with:

```text
* d xi  = -2 xi
* d xi' = +2 xi'
```

[CODE] The co-exact one-form modes are built from scalar modes as:

```text
E_i  = (L + 2) B_i  + C_i
E'_i = (L + 2) B'_i - C'_i
```

with squared norm:

```text
||E_{L,m_+,m_-}||^2  = 2 L (L + 1) (L^2 - 4 m_+^2)
||E'_{L,m_+,m_-}||^2 = 2 L (L + 1) (L^2 - 4 m_-^2)
```

The boundary values where the relevant `m` reaches `+/- L/2` have zero norm and are excluded from the corresponding family.

## Candidate Identification

[INFERRED] A homogeneous left-invariant coframe component on `S3 ~= SU(2)` should transform as one spin-1 object under one of the two `SU(2)` factors and as a scalar under the other:

```text
(J_L, J_R) = (1, 0)
```

or, for the mirrored right-invariant convention:

```text
(J_L, J_R) = (0, 1)
```

[INFERRED] The current Option B scaffold uses the working left-invariant hypothesis:

```text
(J_L, J_R) = (1, 0)
```

## Norm Obstruction In A Single E Family

[INFERRED] If one tries to identify the full left-invariant coframe purely with the `E` family, the natural `L=2` candidate sector with edge magnetic values runs into the Ben Achour zero-norm exclusion:

```text
||E_{2,m_+,m_-}||^2 = 2 * 2 * 3 * (4 - 4 m_+^2)
```

For:

```text
m_+ = +/- 1
```

the norm vanishes:

```text
||E_{2,+/-1,m_-}||^2 = 0
```

[INFERRED] A single `E` family therefore cannot by itself supply all three spin-1 magnetic components with nonzero norm under this naive identification.

The mirrored issue applies to `E'` with `m_- = +/- 1`.

## Consequence

[INFERRED] The homogeneous coframe normalization cannot be closed by extracting one scalar coefficient from a single Ben Achour `E` or `E'` family alone.

The likely resolution requires one of:

- an explicit linear combination of `E` and `E'` families;
- a direct Killing one-form normalization route using `xi`, `xi'`;
- an independent invariant-coframe normalization matched to Haar measure;
- the original authors' TeX/normalization convention for the one-form basis.

## Current Coefficient Status

[CODE] The current implementation in `s3_reduced_matrix_elements.py` intentionally uses:

```text
ANALYTIC_DIRECT_HAAR_CONVENTION
```

and explicitly marks:

```text
Ben_Achour_E_Eprime_one_form_normalization_unresolved
```

[VERIFIED-SYNTHETIC] This is sufficient for the current scaffold tests:

- nonzero `V`;
- Hermiticity;
- working `(J_L,J_R)=(1,0)` selection rules;
- real finite reduced factors.

[NEEDS-REAL-DATA] It is not sufficient for quantitative spectrum claims.

## Decision

[INFERRED] Do not treat the exact unit coframe scale as evidence that the Ben Achour `E/E'` basis mapping is derived.

[CODE] The current `V` scale uses the exact direct Haar-unit coframe convention, while the Ben Achour `E/E'` basis mapping remains a separate unresolved representation detail.

## Allowed Next Steps

Allowed:

- refine the explicit `E/E'` linear combination for `e^i` if a future representation-layer match is required;
- add a metadata-only representation flag if it is clearly labelled as separate from the coframe scale;
- keep testing Hermiticity and selection rules.

Forbidden for now:

- building `D = D0 + V` for spectrum interpretation;
- claiming level crossings;
- claiming zero modes;
- claiming index;
- calling the current `V` a final physical gauge-background operator.

## Current Verdict

[UNCERTAIN] Ben Achour `E/E'` basis mapping is still unresolved as a separate representation detail.

[CODE] No further code change is required for the direct Haar/unit-coframe scale; future changes would only concern the separate `E/E'` basis mapping.
