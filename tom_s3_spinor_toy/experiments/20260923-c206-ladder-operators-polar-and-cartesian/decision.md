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

## What this means for the Tom Lawrence correspondence

Both pieces Tom explicitly asked for are now done, with full workings
captured (not just final answers) -- ready to include in the next reply.
NOT sent yet; per the standing DO NOT INITIATE CONTACT rule, sending
requires the user's own explicit decision. Tom also asked separately for
better equation formatting ("Word's equation editor... or even better,
LaTeX") -- a formatting-only question, not addressed by this round, left
for the letter-assembly step.

## Reproduce

```
cd experiments/20260923-c206-ladder-operators-polar-and-cartesian
python c206_ladder_operators.py
```

`ruff check` -- clean (verified before this write-up).
