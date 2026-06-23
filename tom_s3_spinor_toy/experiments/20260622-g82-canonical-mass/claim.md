# G82 Claim вЂ” Canonical Radion Mass Audit

**Date:** 2026-06-22
**Type:** identifiability and normalization audit

## Question

Is the G62 quantity `sqrt(V''(rho6)/m_KK^2)` already the physical,
canonically normalized modulus/KK mass ratio?

## Assumed reduction identity

For a 4D Einstein-frame reduction with logarithmic radii
`beta_i = ln(rho_i)` and internal dimensions `(n3,n6)=(3,6)`, test the
standard sigma-model metric

`G_ij = n_i delta_ij + n_i n_j/(d-2)`, with `d=4`.

On the imposed path `rho3=C*rho6^2`, the tangent in beta-space is `(2,1)`.

## Gates

- G82-1: compute the path kinetic coefficient exactly.
- G82-2: independently transform the Hessian from `rho6` to the canonical coordinate.
- G82-3: quantify the metric-only correction to the G62 proxy.
- G82-4: determine whether the physical mass ratio is identifiable without `M4/Ms`
  and an explicitly normalized reduced action.
- G82-5: negative control вЂ” the result must change under a deliberately noncanonical
  field rescaling.

## Verdict rules

- `PASS_CANONICAL`: G62's 2.02% is already canonical and fully normalized.
- `CONDITIONAL`: a canonical proxy can be computed only after explicit normalization assumptions.
- `FAIL`: algebraic transformation or controls disagree.
