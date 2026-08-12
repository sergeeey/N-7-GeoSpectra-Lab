# decision -- naive left-mult q-side generator is structurally blocked for j,k

## Verdict

`NAIVE_LEFT_MULT_ANALOG_BLOCKED_FOR_J_K__ONE_SIDED_COMPLEX_STRUCTURE_CONFIRMED`
-> **P1 CONFIRMED (e1 is C-linear). P2 CONFIRMED (e2, e3 are NOT C-linear
in the same encoding).**
**Date:** 2026-08-12 · L0: descriptive · script:
`c92_left_regular_generator_obstruction.py`, results: `results_c92.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** `e1(i)` C-linear | yes | **CONFIRMED** -- `residual_a=0`, `residual_b=0` exactly (symbolic, sympy). Candidate matrix `diag(i,i)` -- literally scalar multiplication by `i`, since `i` commutes with itself. | [VERIFIED-sympy] |
| **P2** `e2(j)`, `e3(k)` NOT C-linear | yes | **CONFIRMED** -- both have nonzero symbolic residuals (`e2`: `residual_a=-2*I*bx`, `residual_b=2*I*ax`; `e3`: `residual_a=2*bx`, `residual_b=-2*ax`), proving the naive derivative-based linear approximation does not capture the full transformation -- there is a genuine antilinear (conjugate-linear) component the construction cannot express as a single complex matrix. | [VERIFIED-sympy] |

**Cross-check (not predicted, done for completeness):** even for `e1`,
where left-mult IS C-linear, the resulting candidate (`diag(i,i)`) does
NOT equal Meier's own `l_{e1}(k=1)` (`diag(-i,i)`), nor its negative --
confirming these are genuinely different operators, not the same
construction up to an overall sign.

## What this genuinely establishes

**The one-sided complex-linearity of quaternion multiplication is the
real obstruction, not a coding artifact.** C85's `right_mult_matrix_on_ab`
works for ALL THREE units because the `(a,b)` parametrization's own
complex structure is specifically built around left-multiplication-by-`i`
(the standard `a+bj` Cayley-Dickson encoding of quaternions from two
complex numbers), and RIGHT multiplication by any quaternion is always
C-linear with respect to that structure (right and left multiplication
commute, and `i`'s own left-action defines "complex" here). LEFT
multiplication by `j` or `k` (which do NOT commute with `i`) breaks that
same complex structure -- this is not specific to Meier's construction
or this project's conventions, it is the general algebraic fact that
`H` is a two-dimensional space over `C` in TWO genuinely different ways
(left-`i`-linear and right-`i`-linear), and a map can be linear with
respect to one without being linear with respect to the other.

**Consequence for task #59 (the multiplication-operator build):** the
most natural first hypothesis for a `q`-side ("left-regular
representation") generator -- literally swap the product order in the
same construction that built `l_{e_i}` -- does not produce a valid
`(k+1)`-dimensional complex matrix for 2 of the 3 generators. Building a
genuine `q`-side generator will need either (a) the opposite-handed
complex structure (parametrize `(a,b)` via right-multiplication-by-`i`
invariance instead, which would then presumably make left-mult by `j,k`
linear -- but this has NOT been checked, and would need its own
consistency verification against Meier's own already-fixed `p`-index
convention), (b) an explicit antilinear/conjugate-linear treatment for
`j,k` specifically (a genuinely different kind of operator, not
expressible as this round's simple 2x2 matrix ansatz), or (c) reading
Meier's own definition of the Peter-Weyl multiplicity index directly --
this project does not have primary-source access to that this session.

## Kill Analysis

**Killed:** the specific hypothesis "the q-side generator is the same
`hamilton_product`-based construction as `right_mult_matrix_on_ab`, just
with the product order swapped" -- for `j,k`, this construction does not
even define a valid complex-linear operator, so it cannot be the answer.

**Not killed:** the broader goal of finding SOME q-side generator (this
round only falsifies one specific, natural-but-naive hypothesis) or the
multiplication-operator construction itself, which C90 already verified
is mathematically viable via the abstract Clebsch-Gordan route
(independent of how the concrete `(q,p,r)` basis realizes it).

## What this does NOT show

1. Does **not** construct any working `q`-side generator.
2. Does **not** try the opposite-handed complex structure (option (a)
   above) -- named as the most promising next hypothesis, not attempted.
3. Does **not** determine what `q` actually is in Meier's own
   construction beyond ruling out this one hypothesis.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.
5. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c92-left-regular-generator-obstruction/c92_left_regular_generator_obstruction.py
```
Self-contained -- reuses only C85's own verified `hamilton_product` and
`build_l_matrices` (unmodified); no new quaternion-algebra convention
introduced.
