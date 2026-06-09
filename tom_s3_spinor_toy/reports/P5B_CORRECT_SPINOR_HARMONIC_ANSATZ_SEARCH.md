# P5B Correct Spinor Harmonic Ansatz Search

Date: 2026-06-07

Scope: determine whether the recovered Lawrence fundamental spinor ansatz is a
valid spinor harmonic on `S3`, or whether it must be replaced by a standard
spinorial basis / Kosmann derivative construction.

## Executive Verdict

<inference> P5B is the next unresolved S3 spinor layer after P5 non-Cartan
validation.

<inference> The recovered Lawrence fundamental spinor ansatz is incomplete under
the scalar-dragging operator recovered from the frames. Applying the non-Cartan
generator produces an extra harmonic sector unless

```text
A'(alpha) / A(alpha) = cot(2 alpha)
```

and even after imposing that relation the remaining ladder coefficient is still
`alpha`-dependent.

<inference> Strongest current verdict:

```text
spinorial Lie derivative required
```

<unknown> A fully validated replacement ansatz is not yet established.

## Required Checks

<fact> P5B must address:

- reproduction of the `cot(2 alpha)` failure;
- ODE system for `A(alpha)`;
- ordinary scalar dragging vs spinorial Lie derivative;
- compatibility with standard `S3` spinor harmonics;
- impact on `V` selection rules.

## Reproduction of the Failure

<fact> Using the recovered scalar-dragging form of `I_{1R}` on

```text
psi_{0,1/2} = A_{0,1/2}(alpha) e^{i(theta - theta_tilde)/2}
```

produces two phase sectors:

- an unwanted `e^{+3 i (theta - theta_tilde)/2}` component;
- a desired `e^{- i (theta - theta_tilde)/2}` component.

<inference> Eliminating the unwanted sector forces

```text
A'(alpha) / A(alpha) = cot(2 alpha)
```

which integrates to a `sqrt(sin(2 alpha))`-type radial factor, but the surviving
coupling coefficient remains `alpha`-dependent rather than a constant ladder
coefficient.

<inference> This is the reason the recovered ansatz is not yet a valid full
non-Cartan spinor harmonic.

## Candidate Next Gates

- `P5C_KOSMANN_LIE_DERIVATIVE_TEST`
- `P5C_STANDARD_S3_SPINOR_HARMONICS_IMPLEMENTATION`
- `P5C_CORRECTED_SPINOR_ANSATZ_VALIDATION`

## Verification

<VERIFIED> Targeted regression test passed locally:

```text
python -m pytest -q tests/test_lawrence_i1r_failure_reproduction.py
2 passed
```

<VERIFIED> This preserves the P5B conclusion:

```text
spinorial Lie derivative required
research_only
V-selection rules = smoke_only
```
