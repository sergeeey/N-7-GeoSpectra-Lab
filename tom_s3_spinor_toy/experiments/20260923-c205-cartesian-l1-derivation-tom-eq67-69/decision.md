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
| 2 | Assembled 3x3 matrices (M_Lz, M_Ly, M_Lx), in Tom's own eq(76) row=input index convention, compared directly to his eq(106)-(108) `[Gamma_3(T_ij)]` | Exact match, in ONE step, no separate sign flip needed |
| 3 | Applied Tom's own `z` (eq 118) directly to the Stage-2 result | Exact match to his eq(123)-(125), the matrices his 2026-09-23 message specifically asked us to reach via this route |

## A real convention bug, caught by independent user review against the actual PDF (not the reporting agent's summary) -- REVISED

The first version of this round reported: "applying eq(67)-(69) directly
lands on eq(103)-(105) [T_ij] first; Tom's own eq(99) sign flip is then a
SEPARATE step needed to reach eq(106)-(108) [Gamma_3(T_ij)]." The user
independently re-derived the calculation by hand against Tom's actual PDF
and found this framing was wrong -- not physically, but as a description of
where the extra minus sign came from.

**Root cause, confirmed by direct computation:** `build_matrix()`'s original
implementation assembled the matrix via `sp.Matrix(rows).T`, i.e. column j =
image of basis_j -- the STANDARD linear-algebra "matrix of a linear map"
convention. But Tom's own eq(76) states the index placement explicitly:
`(-delta_x^I d_I |phi_gamma>) = (i Gamma_d(T_ij))_gamma^delta |phi_delta>`
-- gamma (the INPUT basis label) is the row-like first index, delta (the
output expansion coefficient) is the second. That is `sp.Matrix(rows)`
WITHOUT the transpose. Since these generators are antisymmetric
(`M^T = -M`), assembling the matrix with the wrong (transposed) convention
exactly flips the overall sign -- which is precisely why the first version
landed on `T_ij` (eq 103-105) instead of `Gamma_3(T_ij)` (eq 106-108)
directly, and "needed" an extra negation that was really just undoing the
convention error.

**Corrected result:** building the matrix in Tom's own row=input convention
reproduces eq(106)-(108) DIRECTLY, in a single step -- exactly as his own
general theory says it should (his eq96, `Gamma_d(g)=g^-1=g^T`, applied to
an antisymmetric generator gives `Gamma_d(T)=-T` immediately, no detour
through `T` itself required). The standard linear-algebra transpose
convention is kept in the script's output ONLY as an explicit, clearly
labeled side-by-side comparison -- and it is genuinely useful there,
because it shows mechanically, not just abstractly, exactly where the
"-1"/transpose ambiguity comes from that Tom's own document raises in a
bracketed aside right after eq(99) ("I don't like this -- can it be dealt
with in any way?"). This round's corrected computation gives that
long-standing self-doubt a fully mechanical answer: the ambiguity is a
row/column (input/output) index-placement choice, and once you fix it to
match his own eq(76) as literally written, there is no residual sign
ambiguity anywhere in the chain.

## Two further observations from the same re-check (recorded, NOT sent to Tom)

1. **Page 15, eq(107)/(108) possible typesetting slip.** Verified by direct
   visual inspection of the actual page image (not a text extraction):
   eq(106) is printed correctly as `-T_23`. eq(107) and eq(108), however, are
   printed as matrices that equal `T_31` and `T_12` themselves -- NOT
   `-T_31`/`-T_12` as their own equation labels explicitly state
   (`Gamma_3(T_ij) = -T_ij = (T_ij)^T`). This looks like an isolated
   typesetting slip on 2 of 3 equations, not a conceptual error -- his own
   eq(96) general theory and eq(109)-(112)'s own worked L_x example both
   unambiguously intend `Gamma_3(T)=-T`, and this round's Step 2 comparison
   above used that intended formula, not the possibly-mistyped printed one.
2. **Page 14, dimension formula.** Tom's own text states: "the multiplet
   therefore has `d=2j` dimensions if `j` is a half-integer or `d=2j+1`
   dimensions if `j` is an integer." Standard representation theory gives
   `dim = 2j+1` for ANY `j`, half-integer or integer -- e.g. at `j=1/2`
   (the spinor case, which his own adjacent sentence and his own eq(101)
   correctly show as 2-dimensional), his stated formula gives `d=2(1/2)=1`,
   contradicting his own immediately-preceding text. A genuine,
   self-contradicted slip in his document, confirmed by direct re-reading
   of the page -- not yet raised with him.

Neither observation changes this round's own verdict (both are about a
DIFFERENT part of Tom's document than what this round's own chain of
equations 67-125 needed to use). Recorded for the user's own judgment on
whether/when to mention them -- gently, as questions, per this project's
established correspondence discipline -- not unilaterally added to any
draft reply.

## A second, unrelated build-time bug caught and fixed (self-caught, not Tom's)

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
