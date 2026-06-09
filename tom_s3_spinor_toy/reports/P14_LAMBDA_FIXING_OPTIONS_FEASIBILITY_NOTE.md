# P14 Lambda Fixing Options Feasibility Note

## Objective

Record the plausible next routes for fixing or interpreting the free coupling
`lambda` after the S3-only no-go result.

This is a decision note, not a derivation. It does not claim that `lambda` is
fixed.

## Fixed Inputs

The following inputs are treated as frozen for this note:

- P13A ansatz and convention registry
- P13A1 executable Ben Achour low-mode geometry
- P13B symbolic pattern match
- P13B0 state / measure / selection repair
- P13B1 spinor-state repair
- P13C source-fixed E-mode derivation
- P13C_NORM reduced-coefficient normalization audit
- P13D coefficient normalization and Hermiticity audit
- P13E reduced coefficient no-go
- P13F final no-go record
- P13G handoff / limitations package
- P13H exact low-mode integral audit
- Convention / Normalization Registry

## Anchor Result

The explicit low-mode integral remains:

```text
<psi_i | V | psi_j> = (16*pi**2*rho**3/15) * lambda
```

So the S3-only branch fixes a geometric prefactor, but not `lambda`.

## Decision Rule

Classify each option by:

- required new assumptions
- required equations or missing formalism
- minimal test
- failure condition
- expected cost
- risk of overfitting or ad hoc fitting
- whether it can fix `lambda` or only reinterpret it
- recommended priority

## Option Matrix

| # | Option | New assumptions | Missing formalism | Minimal test | Failure condition | Cost | Overfitting risk | Effect on `lambda` | Priority |
|---:|---|---|---|---|---|---|---|---|---:|
| 1 | S3×S6 scale / radius relation | Shared normalization or coupled radii between S3 and S6; tensor bridge is a physical compactification rather than a label bridge | A reduction formula linking `lambda` to the S3/S6 radius ratio or total volume normalization; a map from P6K conventions to the P13H coefficient | Derive one explicit S3×S6 scale relation and check whether it reproduces the P13H coefficient without post hoc tuning | Relation is introduced after seeing the coefficient or needs ad hoc rescaling | medium | medium-high | conditional fix candidate | 1 |
| 2 | Action-principle requirement | A variational action exists and `lambda` is the unique coefficient of the only symmetry-allowed invariant | An action functional, symmetry classification, Euler-Lagrange derivation, and a normalization convention that makes the coefficient unique | Derive the operator from an action and verify uniqueness of the coefficient from symmetry plus normalization | Multiple invariant terms remain, or the action leaves a free overall prefactor | medium | medium | conditional fix candidate | 2 |
| 3 | Topological / Chern-Simons / winding quantization | The relevant background admits a nontrivial topological sector and `lambda` enters a quantized quantity | A topological functional, quantization condition, or winding / charge formula containing `lambda` | Show whether `lambda` multiplies an integer-valued topological quantity after normalization is fixed | `lambda` stays continuously adjustable or the invariant collapses under convention changes | high | medium-high | conditional fix candidate | 3 |
| 4 | FRGE / UV fixed-point feasibility | `lambda` can be treated as a running effective coupling in a controlled truncation | A beta function, truncation scheme, fixed-point analysis, and a scheme-stability check | Compute or borrow a minimal beta function and check whether a UV fixed point narrows or selects `lambda` | The flow is scheme-dependent or `lambda` remains unconstrained across admissible truncations | high | medium-high | can fix or reinterpret | 4 |
| 5 | Phenomenological calibration | An external observable or benchmark exists and the goal is calibration / interpretation rather than microscopic derivation | A map from `lambda` to one observed quantity plus at least one independent validation quantity | Fit `lambda` to one observable and require an independent cross-check before accepting the calibration | The fit only reproduces the calibration point and does not generalize | low | high | reinterpret only | 5 |
| 6 | ML-assisted pattern search | Sufficient labeled examples or symbolic features exist; output is hypothesis generation only | A validation layer that rejects any ML-suggested relation unless exact symbolic checks pass | Use ML only to propose candidate relations and require each one to survive exact symbolic checking | The proposal collapses under exact math or simply rediscoveries the frozen scaffold | low-to-medium | very high | hypothesis generation only | 6 |

## Summary

The note does not identify a current route that fixes `lambda`.

The most promising next route, if the goal is to constrain `lambda` without
changing the frozen S3 result, is:

1. S3×S6 scale / radius relation
2. Action-principle requirement
3. Topological / Chern-Simons / winding quantization feasibility
4. FRGE / UV fixed-point feasibility
5. Phenomenological calibration
6. ML-assisted pattern search

Interpretation:
- `lambda` is still free under the current S3-only evidence.
- Phenomenological calibration can only reinterpret `lambda`.
- ML can only generate hypotheses.

## Scope Fence

This note verifies only route ranking and feasibility classification.

This note does not verify:

- that `lambda` is fixed
- physical V-operator proof
- V-selection promotion
- fermion generation claims
- Standard Model reproduction
- runtime safety

Current status:

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

## Current Status

```text
P14 = FEASIBILITY_NOTE_COMPLETE
lambda = FREE_COUPLING_PARAMETER
```

## Next Gate

```text
none; continue only if a new physical principle, a new S3×S6 derivation,
or a source-fixed coupling relation is supplied
```
