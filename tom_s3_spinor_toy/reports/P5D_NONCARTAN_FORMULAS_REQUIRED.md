# P5D Non-Cartan Formulas Required

Date: 2026-06-08

Scope: document the remaining blocker after the initial standard
`S3` spinor-harmonics layer and the representation-sanity tests.

## Current State

```text
P5C_STANDARD_S3_SPINOR_HARMONICS_IMPLEMENTATION = initial layer implemented
P5D_STANDARD_SPINOR_HARMONICS_REPRESENTATION_TESTS = passed
runtime = research_only
V-selection rules = smoke_only
```

## What Is Already Closed

- explicit standard lowest `S3` spinor-frame basis exists in code;
- the basis matches the Wigner-`D` `j=1/2` oracle up to the fixed `sigma_3`
  gauge;
- pointwise unitarity, endpoint regularity, and Haar norms are verified;
- lifted `su(2)_L` and `su(2)_R` generator closure passes as an abstract
  representation test.

## Remaining Bottleneck

<fact> The project still does **not** have a fully verified, explicit set of
non-Cartan differential generators acting on the standard spinor harmonics in
Lawrence coordinates with constant ladder coefficients.

<fact> In particular, the exact coordinate-space formulas for `I_{1L}`, `I_{2L}`,
`I_{1R}`, `I_{2R}` that reproduce the expected constant action on the chosen
spinor basis remain the missing ingredient.

<fact> Without those formulas, the project cannot complete the direct
representation-level audit requested for the standard spinor basis.

## Diagnostics

<inference> The current code is sufficient to establish a clean basis layer, but
it is not yet sufficient to close the non-Cartan action layer in coordinate
space.

<inference> This is the point at which the project should stop with:

```text
FORMULAS_REQUIRED
```

## Required Next Inputs

1. Exact coordinate-space formulas for the non-Cartan vector fields on
   `S3` in the Lawrence/Hopf chart.
2. Exact convention for how those vector fields act on the chosen spinor
   basis.
3. A verified symbolic or published source tying those formulas to the
   standard spinor-harmonic basis, so the ladder coefficients can be checked
   without ambiguity.

## Conclusion

```text
FORMULAS_REQUIRED
```

