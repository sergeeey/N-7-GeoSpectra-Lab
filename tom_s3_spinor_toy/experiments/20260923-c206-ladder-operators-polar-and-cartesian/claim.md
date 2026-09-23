# C206 Claim — the actual ladder operators (not rotation operators), full McMurry working, plus Cartesian L_+/L_-

**Date:** 2026-09-23
**FL tier:** [x] Standard (tooling/derivation round in support of external correspondence; no project physics claim)
**Question type:** [x] descriptive

## Correction that motivated this round

Tom's reply: "What you've applied here [C205] are not the ladder operators,
but the differential operators relating to rotations around each axis, L_x,
L_y and L_z. The ladder operators are L_+ = L_x + i L_y and L_- = L_x - i
L_y. P.144 of McMurry gives these in polar coordinates. If you've done the
bit of question 6.3 I asked for, please supply your working. After that,
what I was looking for was for you to apply L_+ and L_- in Cartesian form
to the basis functions also in Cartesians."

Two distinct gaps this closes:
1. C201 computed the McMurry 6.3(a) polar-coordinate ladder result (sqrt(2))
   but only the headline number was ever shared with Tom -- not the actual
   step-by-step working he explicitly asked to see.
2. C205 applied L_x, L_y, L_z (rotation generators) to x/r,y/r,z/r -- a
   different, valid calculation, but not the one originally requested
   (ladder operators specifically, and in Cartesian form).

## Prior Result Gate

1. Exact claim: (a) McMurry's own L_+/L_- (polar form, p.144) applied to the
   l=1 spherical harmonics give the standard sqrt(2) ladder coefficients,
   with every intermediate differentiation step shown, not just the final
   number; (b) L_+ = L_x+iL_y, L_- = L_x-iL_y, built from Tom's own Cartesian
   L_x,L_y (eq 68-69), applied directly to x/r,y/r,z/r, give a specific,
   fully-derived set of six results.
2. `grep` of `experiments/`, `null_results/`, `parked/` for prior Cartesian-
   ladder-operator work: no hits (only C201's polar route and C205's
   rotation-operator route exist).
3. **Status:** [x] NEW.

## Estimand

**Population:** the l=1 representation of so(3), examined via the ladder
operators specifically (not the rotation generators), in two coordinate
systems.
**Intervention/method:** exact symbolic differentiation (sympy) of (a)
McMurry's polar-form L_+/L_- applied to Y_{1,0}, Y_{1,1}, Y_{1,-1}; (b) the
Cartesian combinations L_+ = L_x+iL_y, L_- = L_x-iL_y (built from Tom's own
eq 68-69) applied to x/r, y/r, z/r.
**Comparator:** the standard textbook ladder relation `L_+/- |1,m> propto
sqrt(2) |1,m+/-1>` for part (a); internal consistency (raising/lowering
structure, correct termination at the ladder's ends) for part (b), since
there is no pre-existing "target" matrix to compare against -- this is a
first-principles Cartesian construction Tom asked to see, not a check
against something already stated.
**Endpoint:** exact symbolic residual (zero required) for each of the six
polar-form actions; the six Cartesian results themselves, cross-checked for
internal ladder consistency via the complex combinations (x+iy)/r and
(x-iy)/r (Tom's own eq 115-116 pattern).

## Kill criterion

| Condition | Consequence |
|---|---|
| Any of the six polar-form actions does not reduce to exactly sqrt(2) times the expected neighbor (or 0 at the ladder ends) | McMurry-internal-consistency claim FALSIFIED for that action -- report the exact discrepancy |
| The Cartesian L_+ does not annihilate (x+iy)/r, or L_- does not annihilate (x-iy)/r | The Cartesian ladder construction is internally inconsistent -- a real error in the L_+/L_- combination or the underlying L_x/L_y, not a reportable "finding" |

If FAIL → kills: the claim that these are genuinely the l=1 ladder
operators behaving as such in either coordinate system.
If PASS → survives: full, tool-verified workings for both the polar (as
explicitly requested, "if you've done the bit of question 6.3, please
supply your working") and Cartesian (the new calculation) routes.

## What this does NOT mean

1. Does NOT redo C205's rotation-operator (L_x,L_y,L_z) result -- that
   stands on its own, unaffected by this round.
2. Does NOT touch this project's own G2/SU(3)/Spin(8) triality-channel
   physics claims -- unrelated substrate.
3. Does NOT constitute a reply to Tom yet -- purely the computation itself;
   the letter is a separate step.

## Fence

- `safe_for_runtime = False`. No `lambda` symbol introduced.

## Verdict

**PROMOTE.** Part A: all six polar-form ladder actions match the expected
`sqrt(2)` (or 0 at the ladder termini) exactly, symbolically, with full
intermediate steps captured. Part B: the six Cartesian L_+/L_- results are
internally consistent -- `L_+` on the top-of-ladder combination `(x+iy)/r`
and `L_-` on the bottom-of-ladder combination `(x-iy)/r` both vanish exactly,
confirming the construction behaves as genuine raising/lowering operators.

**Evidence:** [VERIFIED-sympy 6/6] (Part A, polar) + [VERIFIED-sympy 6/6 +
2/2 structural cross-checks] (Part B, Cartesian).

**Status:** CLOSED PROMOTE.
