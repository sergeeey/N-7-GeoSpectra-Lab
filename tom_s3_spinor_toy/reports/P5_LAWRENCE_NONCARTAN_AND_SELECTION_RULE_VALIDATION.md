# P5 Lawrence Non-Cartan and Selection-Rule Validation

Date: 2026-06-07

Scope: validate the Lawrence S3 non-Cartan generators, their action on the
fundamental spinor ansatz, the `cot(2 alpha)` diagnostic, and the consequences
for `V` selection rules.

## Executive Verdict

<fact> Cartan-layer mapping for Lawrence S3 is already recovered and set to
`research_only`.

<inference> P5 is the next unresolved layer: non-Cartan generators, alpha
dependence, and the `cot(2 alpha)` constraint.

<unknown> The current runtime status for Lawrence-specific claims at this layer
is not yet safe.

## Required Checks

<fact> The validation target is the recovered Lawrence S3 spinor ansatz under:

- `I_{1L}`, `I_{2L}`, `I_{1R}`, `I_{2R}`;
- `SU(2)_L x SU(2)_R` commutators;
- action on the four fundamental spinor states;
- `cot(2 alpha)` consistency;
- `V`-selection rule implications.

## Remaining Blockers

- non-Cartan closure not yet verified;
- `cot(2 alpha)` unresolved;
- spinor-harmonic ansatz not yet validated as a full representation;
- `V` selection rules not yet derived from the validated representation theory.

## Next Gate

```text
P5B_CORRECT_SPINOR_HARMONIC_ANSATZ_SEARCH
```
