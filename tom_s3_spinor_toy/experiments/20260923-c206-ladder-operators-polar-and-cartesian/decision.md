# C206 Decision — full McMurry polar working + new Cartesian L_+/L_- calculation

**Date:** 2026-09-23
**Verdict:** PROMOTE

## Why this round exists

Tom's second, more precise correction (see claim.md for the full quote):
C205's L_x, L_y, L_z are the rotation operators, not the ladder operators.
The ladder operators are L_+ = L_x + i*L_y, L_- = L_x - i*L_y, given in
polar form on McMurry p.144. He asked for two things, explicitly: (1) the
full working for McMurry question 6.3(a) -- previously only the headline
sqrt(2) result was ever shared, not the actual differentiation steps; (2)
a new calculation applying L_+/L_- in Cartesian form to the Cartesian basis
functions x/r, y/r, z/r.

## What was computed (`c206_ladder_operators.py`, all `[VERIFIED-sympy]`)

### Part A -- McMurry 6.3(a), full working, polar form

McMurry's own p.144 definitions:
```
L_+ = e^{i*phi} * (d/d(theta) + i*cot(theta)*d/d(phi))
L_- = e^{-i*phi} * (-d/d(theta) + i*cot(theta)*d/d(phi))
```
applied to the l=1 spherical harmonics (McMurry's own normalization,
`c = sqrt(3/(4*pi))`):
```
y_{1,0}  = c*cos(theta)
y_{1,1}  = -c/sqrt(2) * sin(theta) * e^{i*phi}
y_{1,-1} =  c/sqrt(2) * sin(theta) * e^{-i*phi}
```

All six raising/lowering actions verified exactly, symbolically, with the
raw differentiation result shown before simplification:

| Action | Result |
|---|---|
| `L_+ y_{1,0}`  | `= sqrt(2) * y_{1,1}`  |
| `L_+ y_{1,-1}` | `= sqrt(2) * y_{1,0}`  |
| `L_+ y_{1,1}`  | `= 0` (top of ladder) |
| `L_- y_{1,0}`  | `= sqrt(2) * y_{1,-1}` |
| `L_- y_{1,1}`  | `= sqrt(2) * y_{1,0}`  |
| `L_- y_{1,-1}` | `= 0` (bottom of ladder) |

`PART A ALL PASS: True`. This is the working Tom asked to see for question
6.3(a) -- previously only the sqrt(2) headline number had been reported.

### Part B -- L_+, L_- in Cartesian form, applied to Cartesian basis (new)

Built directly from Tom's own eq(68)-(69):
```
L_x = i*(z*d/dy - y*d/dz)     [his eq 69]
L_y = i*(x*d/dz - z*d/dx)     [his eq 68]
L_+ = L_x + i*L_y
L_- = L_x - i*L_y
```
applied to `x/r, y/r, z/r` (r = sqrt(x^2+y^2+z^2)):

| | `x/r` | `y/r` | `z/r` |
|---|---|---|---|
| `L_+` | `z/r` | `i*z/r` | `-(x+i*y)/r` |
| `L_-` | `-z/r` | `i*z/r` | `(x-i*y)/r` |

**Ladder-structure cross-check**, via the complex combinations `(x+iy)/r`
and `(x-iy)/r` (Tom's own eq115-116 complex-combination pattern, the
Cartesian analogue of `y_{1,pm1}`):
```
L_+ [(x+iy)/r] = 0     -- top of ladder, exactly as expected
L_- [(x-iy)/r] = 0     -- bottom of ladder, exactly as expected
```
Both `True`, confirming the Cartesian L_+/L_- constructed this way behave
as genuine raising/lowering operators on the l=1 representation, exactly
as their polar counterparts do in Part A.

## Part C (added same day, user review) -- reconciling Part A and Part B directly

While drafting the reply letter, the user proposed showing the ladder
structure appearing directly in Tom's own complex basis
`(x+iy, z, x-iy)` (his eq115-116 pattern) and offered a hand derivation
of a three-step chain (e.g. `(x-iy) -L+-> 2z -L+-> -(x+iy) -L+-> 0`) plus
a claim that the raw coefficients `2` and `1` reduce to the standard
`sqrt(2)` once normalization is accounted for.

**Tool-verified before accepting (`sympy`, scratch scripts, deleted after
use):** the SINGLE-STEP raw actions in the user's derivation are all
correct (`L_+(x-iy)=2z`, `L_+(z)=-(x+iy)`, `L_+(x+iy)=0`, and the
symmetric `L_-` actions) -- these match Part B's own results exactly.
**But the literal three-step CHAIN, as written, drops a factor of 2 on
its third link**: since `L_+`/`L_-` are linear, applying `L_+` to the
literal output `2z` (not freshly to `z`) must scale the output by 2:
`L_+(2z) = -2(x+iy)`, not `-(x+iy)` as the chain stated; symmetrically
`L_-(-2z) = -2(x-iy)`, not `(x-iy)`. Confirmed directly with `sympy`
(both the naive by-hand recomputation and a literal chained-application
check agree on `-2(x+iy)`/`-2(x-iy)`).

**Resolution:** the chain display is dropped from the write-up (it added
no information the single-step relations didn't already have, and is an
easy place to lose a factor). In its place, Part C directly reconciles
Part A and Part B: build the SAME normalized `Y_{1,m}` states used in
Part A (McMurry's own `c=sqrt(3/(4pi))` normalization), but written in
`x,y,z` instead of `theta,phi`, and apply the CARTESIAN `L_+/L_-`
(Tom's own eq68-69-built operators, same as Part B) to them directly.
Result: **all six actions reproduce the exact `sqrt(2)` ladder
coefficients from Part A, with zero residual** -- `PART C ALL PASS: True`.
This is the genuine unification the user was after: the McMurry
polar route and the Tom's-own-generators Cartesian route are the SAME
calculation in different coordinates, not two calculations that happen
to agree up to a constant.

The user's confusion (dropped factor of 2 in an illustrative hand
derivation) never reached the committed record or the letter -- caught
by tool-verification before either was finalized, per this project's
standing `audit-verification-gate.md` discipline (a human's re-derivation
gets the same "verify before use" treatment as an agent's).

## Part D (2026-09-24) -- the explicit 3x3 matrices Tom asked for

Tom's follow-up, quoted: "Just spotted, you haven't got the third stage.
Could you please express your results in the form [Ladder operator]
[Column vector of states] = [3 x 3 matrix][Column vector of states]".

Built via a corrected decomposition method -- an earlier draft of this
function divided the operator's output by a single target basis element
(`applied/target`), which silently gives a WRONG answer whenever the
output mixes more than one basis element (exactly what happens for
`L_+(z/r)=-(x+iy)/r` in the real basis: dividing by `x/r` alone leaves a
spurious `y/r` residual instead of cleanly reading off `-1`). Caught
before running, not after -- replaced with a proper linear decomposition
(extract the (x,y,z) coefficient vector by differentiation, since every
output here is a degree-1 homogeneous polynomial once the shared `1/r` is
cleared, then solve the resulting 3x3 linear system against the same
basis's own coefficient matrix).

**Results (real basis `x/r,y/r,z/r`, standard column=input convention,
`[L][v]=[M][v]`):**
```
L_+ = [[0,0,-1],[0,0,-I],[1,I,0]]        L_- = [[0,0,1],[0,0,-I],[-1,I,0]]
```

**Results (complex ladder basis `(x+iy)/r, z/r, (x-iy)/r`, standard
column=input convention):**
```
L_+ = [[0,-1,0],[0,0,2],[0,0,0]]         L_- = [[0,0,0],[-2,0,0],[0,1,0]]
```
This is the genuinely illustrative one -- purely super/subdiagonal, the
textbook ladder-operator shape, matching Part C's individual actions
exactly once assembled (column 1 of `L_+` = image of the top-of-ladder
state = zero; column 3 = image of the bottom state = `2*(middle state)`).

**Cross-check against C205's own certified matrices**
(`M_+ = M_Lx + i*M_Ly`, `M_- = M_Lx - i*M_Ly`, using C205's exact
`M_Lx_tom_convention`/`M_Ly_tom_convention` values copied verbatim from
its `results_c205.json`): residual is the exact zero matrix for both `L_+`
and `L_-`. This ties C206's ladder-operator matrices to C205's
independently-verified rotation-generator matrices, not just to C206's
own internal computation.

Both Tom's own row=input convention (his eq76) and the standard
column=input convention (what his literal request format calls for) are
reported for both bases -- four matrices per operator, eight total,
labeled explicitly to avoid the exact row/column ambiguity that caused
C205's original bug.

## A REAL transpose bug, caught by the user before sending (second
## occurrence of the exact same bug class as C205)

The first PDF draft (`REPLY_TO_TOM_2026-09-24_matrix-form.tex`, rev1)
presented the `standard_column_input` matrices as satisfying
`[Op][v]=[M][v]`, reasoning that Tom's literal phrasing
("[Operator][column vector]=[3x3 matrix][column vector]") matches the
"standard linear-algebra matrix-vector product" form. **This reasoning
was wrong.** The user independently re-derived all four matrices by hand
against the already-established single-step actions and found the PDF's
matrices were exactly transposed relative to what the literal equation
requires.

**Root cause, confirmed with `sympy` before accepting the correction
(not accepted on the user's word alone, per this project's own
`audit-verification-gate.md` -- a human's re-derivation gets the same
"verify before use" treatment as an agent's):** `v` in Tom's request is
literally the column vector of the three basis FUNCTIONS themselves
(`x/r, y/r, z/r`, or the complex combinations). The equation
`operator(v) = M @ v`, read entrywise on the left (apply the operator to
each function in `v`) and as ordinary matrix-vector multiplication on the
right, is a concrete function identity -- computed directly:
`entrywise_L(v) - M_standard @ v` is NOT zero (residual is exactly `2x`
the correct answer, a full sign flip from the antisymmetric generator
structure); `entrywise_L(v) - M_tom_row_input @ v` IS exactly zero, for
all four matrices (`L_+`/`L_-` x real/complex basis).

**Why the "standard convention" reasoning failed:** the `standard_column_
input` matrix is correct for a DIFFERENT question -- "if `v` represents an
ABSTRACT state with constant coefficients `v = v_1 e_1+v_2e_2+v_3e_3`,
what matrix transforms those coefficients under the operator" -- not for
"if `v` IS the literal vector of basis functions, what matrix reproduces
`operator` applied entrywise." These are genuinely different objects that
happen to share the notation `Mv`; conflating them is exactly what
produced C205's original transpose bug, and produced this one too.

**Fix, permanent, not just this-instance:** `build_matrix_both_
conventions()` now contains a MANDATORY gate -- it computes the literal
`operator(v) - M@v` residual for BOTH candidate matrices and raises
`AssertionError` unless EXACTLY ONE of them is the zero vector. The
function will not return silently if this check is ambiguous or if
neither/both conventions satisfy the equation. This makes the specific
failure mode that reached the PDF mechanically impossible to repeat
within this script, per the user's own explicit request for a gate
rather than relying on manual re-reading a second time.

**Nothing was sent to Tom in the wrong form** -- caught in review before
the PDF went out; only `rev1` (never sent) had the error, `rev2`
(independently re-verified against the exact numbers typeset in the
`.tex`, not just against the script's console output) is what was sent.

## What this means for the Tom Lawrence correspondence

Both pieces Tom explicitly asked for, plus the Part 3 complex-basis
reconciliation, went out in the reply letter -- typeset as LaTeX/PDF per
Tom's own stated preference ("Word's equation editor... or even better,
LaTeX"). **SENT 2026-09-24** (`correspondence/DRAFT_REPLY_TO_TOM_2026-09-
23_ladder-operators_rev1.pdf`, gitignored, not in this repo). Awaiting
reply; DO NOT INITIATE CONTACT stands for any further message.

## Reproduce

```
cd experiments/20260923-c206-ladder-operators-polar-and-cartesian
python c206_ladder_operators.py
```

`ruff check` -- clean (verified before this write-up).
