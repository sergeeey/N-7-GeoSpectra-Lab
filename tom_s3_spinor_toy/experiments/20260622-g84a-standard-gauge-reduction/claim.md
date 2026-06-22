# G84A Claim — Standard Gauge Reduction

**Date:** 2026-06-22  
**Precondition:** G83 = `OPEN_MISSING_ACTION`

## Hypothesis

For an unwarped product metric with constant dilaton prefactor, dimensional
reduction of a standard Yang–Mills term gives a four-dimensional inverse gauge
coupling proportional to the volume wrapped by the gauge sector.

On the project path

`rho3 = C * rho6^2`,

the expected powers are:

- bulk sector on `S3 x S6`: `alpha = 12`;
- sector localized on `S3`: `alpha = 6`;
- sector localized on `S6`: `alpha = 6`;
- point-localized sector: `alpha = 0`.

The four-dimensional Weyl transformation should not alter these powers because
`sqrt(-g) F_mu_nu F^mu_nu` is Weyl invariant in exactly four dimensions.

## Scope and action ansatz

Audit the zero-mode reduction of

`S_YM = -(1/4 g_D^2) integral sqrt(-G) P(rho) Tr(F_MN F^MN)`

for bulk or cycle-localized gauge fields whose retained field strength has only
four-dimensional indices. The baseline sets the extra prefactor `P(rho)` to a
constant. Dilaton and warp dependence are recorded only as compensators, not
assumed.

## Allowed verdicts

- `DERIVED_POSITIVE_POWER_STANDARD_ANSATZ`
- `DERIVED_INVERSE_SQUARE_STANDARD_ANSATZ`
- `MIXED_STANDARD_ANSATZ`
- `FAIL_REDUCTION`

## Pass conditions

Use `DERIVED_POSITIVE_POWER_STANDARD_ANSATZ` only if:

1. direct volume counting and logarithmic differentiation agree;
2. bulk, S3-localized, and S6-localized powers are `12`, `6`, and `6`;
3. the 4D Weyl exponent is exactly zero;
4. no baseline sector produces `alpha = -2`.

## Falsifiers

- A correct direct reduction yielding `alpha = -2` under the baseline ansatz.
- A nonzero Weyl correction to a 4D two-form kinetic term.
- Disagreement between independent exponent calculations.
- Hidden use of a dilaton, warp factor, duality, or field redefinition in the
  baseline result.

## Controls

- Positive control: the internal volume must scale as `rho6^12`.
- Negative control: repeating the Weyl-counting formula in external dimension
  `d != 4` must produce a nonzero Weyl exponent.
- Inverse-square control: an additional prefactor must contribute `-8` to a
  cycle-localized `+6` sector or `-14` to a bulk `+12` sector.

## Interpretation limit

A positive verdict derives powers only within the stated standard ansatz. It
does not identify a hidden gauge group, fix an absolute coupling, prove
gaugino condensation, or connect `lambda_v_operator` to `lambda_np`.
