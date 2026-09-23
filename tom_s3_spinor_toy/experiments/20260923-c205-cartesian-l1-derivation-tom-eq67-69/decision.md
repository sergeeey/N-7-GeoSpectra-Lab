# C205 Decision — Tom's own eq(67)-(69), applied directly, reproduce his own (103)-(125) exactly

**Date:** 2026-09-23
**Verdict:** PROMOTE

## Why this round exists

Tom corrected our understanding of his request (see claim.md for the full
quote): he never sent his own ladder-operator work to check, and the task
was never "verify Tom's matrices." He asked for a genuinely new calculation
-- the Cartesian derivation via his own eq(67)-(69) -- which he has not
attempted himself, with full workings requested explicitly. C201 (McMurry,
ladder operators) and C202 (abstract intertwiner comparison against his
matrices) did not do this. This round does exactly that.

## What was computed (all `[VERIFIED-sympy]`, `c205_cartesian_l1_derivation.py`)

| Stage | Method | Result |
|---|---|---|
| 1 | `L_z=i(x2*d/dx1-x1*d/dx2)`, `L_y`, `L_x` (Tom's eq 67-69) applied by direct symbolic differentiation to `x1/r, x2/r, x3/r` (his eq 91 basis, constant dropped) | 9 individual differentiation results, each exactly proportional to one basis function -- shown in full in `run_output.txt` |
| 2a | Assembled 3x3 matrices (M_Lz, M_Ly, M_Lx) compared directly to Tom's eq(103)-(105) `[T_ij]` | Exact match, no sign flip needed |
| 2b | Applied Tom's own eq(99) `Gamma_3(T)=-T` to the Stage-1 matrices | Exact match to his eq(106)-(108) `[Gamma_3(T_ij)]` |
| 3 | Applied Tom's own `z` (eq 118) to the Stage-2b result | Exact match to his eq(123)-(125), the matrices his 2026-09-23 message specifically asked us to reach via this route |

## The one subtlety worth naming explicitly (not a discrepancy)

Applying eq(67)-(69) DIRECTLY to the Cartesian basis functions lands you on
eq(103)-(105) [T_ij] first -- NOT eq(106)-(108) [Gamma_3(T_ij)] directly.
Tom's own eq(99) sign flip (`Gamma_3(T)=-T`) is a SEPARATE, additional step
needed to reach the "vector multiplet" convention his (123)-(125) are stated
in. This is worth being explicit about because Tom's own document contains a
bracketed aside right after eq(99) expressing his own uncertainty about
exactly this index/sign bookkeeping ("I don't like this -- can it be dealt
with in any way?"). This round's direct computation gives that question a
completely mechanical, unambiguous answer: yes, both matrices exist and are
related by exactly the stated eq(99) sign flip, cleanly, with no residual
ambiguity once you track which of his equations produces which matrix.

## A build-time bug caught and fixed (self-caught, not Tom's)

The first version of the `decompose()` helper tried to symbolically clear
denominators via `sp.Poly(expr * r**5, x1, x2, x3)`, which crashed
(`PolynomialError: sqrt(...) contains an element of the set of generators`)
because the bare `r = sqrt(x1**2+x2**2+x3**2)` survived inside the
expression being fed to `Poly`, which cannot treat a `sqrt` sub-expression
as a polynomial generator. Fixed by using the fact that these specific
operators are so(3) rotation generators that PRESERVE `r`: multiplying the
result by `r` directly, verifying `r` cancels completely (a hard
`ValueError` if it doesn't -- not silently trusted), then extracting linear
coefficients from the resulting genuine polynomial in `x1,x2,x3`. Re-run
confirmed identical final results before and after the fix (the crash was in
the verification method, not the underlying differentiation).

## What this means for the Tom Lawrence correspondence

This is the calculation Tom actually asked for. Ready to send, with full
workings (the per-basis-function differentiation results, not just the
final matrices) -- exactly what he said he wants to see. NOT sent yet; per
the standing DO NOT INITIATE CONTACT rule, sending requires the user's own
explicit decision, and Tom separately said he will "respond on the separate
points on SO(6) and SU(3) shortly" -- those are unrelated to this
calculation and this round does not touch them.

## Reproduce

```
cd experiments/20260923-c205-cartesian-l1-derivation-tom-eq67-69
python c205_cartesian_l1_derivation.py
```
