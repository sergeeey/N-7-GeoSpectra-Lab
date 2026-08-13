# decision -- C94's bracket inconsistency RESOLVED: L_i=+l_{e_i} directly, R_i=-l_{e_i}^T, both bracket-consistent

## Verdict

`P3_RESOLVED__L_EQUALS_PLUS_L__R_EQUALS_MINUS_L_TRANSPOSE__BOTH_BRACKET_CONSISTENT`
-> **P1 CONFIRMED (`L_i = +l_{e_i}(1)` directly, uniform across all 3
units). P2 -- pre-registered prediction WRONG (`-l` does not match);
ACTUAL result `R_i = -l_{e_i}(1)^T`, uniform across all 3 units. P3
CONFIRMED for BOTH sides: `[L1,L2]=2L3` and `[R1,R2]=2R3`, exactly --
the bracket inconsistency that blocked C94 is resolved.**
**Date:** 2026-08-12 · L0: descriptive · script:
`c95_coefficient_space_refinement.py`, results: `results_c95.json`.

---

## Root cause of C94's inconsistency

C94 computed "how `g0`'s own raw matrix entries transform" under
`h(eps)^-1 @ g0` and read off a candidate generator by direct matrix
comparison (`right_diff` vs `candidate @ g0`). This conflates two
different objects: the transformation of `g`'s literal entries versus
the transformation of the COEFFICIENTS of an abstract function
`F = sum c_mn * g_mn` re-expanded in the same monomial basis after
substitution -- a classic function-vs-coefficient contragredience
subtlety (well known in representation theory: a function transforms
one way, its expansion coefficients transform the transpose/dual way).
These coincide for the RIGHT-translation side in this specific setup
(by an algebraic accident of this particular embedding) but NOT for the
LEFT-translation side, which is exactly why C94 found `+l^T` for left
(wrong) while — checked here for completeness — its `-l^T` for right
happens to still be correct.

## Verification chain (three independent methods, not one)

1. **Technique validated against a known-correct case first.** Before
   trusting any result on the actual `L_h`/`R_h` construction, validated
   the same "first-order `h(eps)=I+eps*X`, differentiate" technique
   against the textbook-unambiguous adjoint representation
   (`d(Ad)(X)(Y)=[X,Y]` exactly) -- confirmed the technique itself is
   sound before reapplying it. [VERIFIED-sympy]
2. **Fully symbolic coefficient extraction, no hand index-tracking.**
   Built a generic function `F = sum c_mn g_mn` (`g_mn` as independent
   symbols, `c_mn` as separate symbols per basis vector), substituted
   `g -> h(eps)^{-1}g` / `g h(eps)`, re-expanded via sympy's own
   `Poly.coeff_monomial` (not manual comparison), differentiated. Found
   and fixed a real factor-of-2 bug in the first draft of this
   extraction (accumulating contributions from both values of the
   untested index instead of using one fixed representative) --
   self-caught via a mismatch against a hand-predicted value, not
   assumed correct. [VERIFIED-sympy]
3. **Independent numerical cross-check via finite differences.** For a
   random coefficient matrix `c` and the actual `scipy.linalg.expm`
   matrix exponential (not the first-order truncation used in 1-2),
   verified `d/dt|_0 F(h(t)^{-1}g0)` (finite-difference, `t` from
   `1e-2` down to `1e-6`) converges to the symbolically predicted value
   with clean `O(t)` scaling (`3.65e-3 -> 3.64e-7` as `t` shrinks by
   10x each step) -- confirms the result independent of both the
   first-order-truncation assumption AND the symbolic coefficient-
   extraction method. [VERIFIED-numpy]

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** | `L_i = +l_{e_i}` | **CONFIRMED**, uniform across `e1,e2,e3`, machine-exact. | [VERIFIED-sympy] |
| **P2** | `R_i = -l_{e_i}` (this round's own pre-registered guess) | **WRONG as predicted** -- actual result `R_i = -l_{e_i}^T`, uniform across `e1,e2,e3`. Honest miss, recorded per this round's own `kill_criterion`. | [VERIFIED-sympy] |
| **P3** | does either corrected candidate satisfy its own bracket relation? | **YES, BOTH.** `[L1,L2]-2L3=0` and `[R1,R2]-2R3=0` exactly (symbolic zero matrices). | [VERIFIED-sympy] |

## What this genuinely establishes

**C94's P3 bracket-consistency contradiction is resolved.** The
group-action-certified generators are:
- `q`-side (left translation): `L_i = +l_{e_i}(1)` -- literally the same
  matrix Meier's own construction already uses for the `p`-index, no
  transform needed.
- `p`-side (right translation), re-derived here for completeness and
  cross-check: `R_i = -l_{e_i}(1)^T`, matching C94's own right-
  translation finding (which was NOT affected by the bug that broke
  C94's left-translation side).

Both are now independently bracket-verified via three separate methods
(technique validated on a known case, bug-fixed symbolic derivation,
independent numerical finite-difference convergence), a materially
stronger verification chain than C92, C93, or C94 individually had.

**This is the fourth attempt at this exact sign determination in one
session (C92, C93, C94, C95).** Given that track record, this result is
reported with appropriate, explicit caution rather than as a final
closed book -- but it is qualitatively different from the prior three:
it is the first to (a) validate its own technique against an
independently-known-correct case before use, (b) use a bug-catching
method (symbolic coefficient extraction where an actual bug was found
and fixed, not assumed clean), and (c) cross-check numerically against
the true exponential map, not just a first-order approximation.

## Gate status

Per C94's own decision.md, C95 (multiplication-operator certification)
and C96 (spectral-flow experiment) in the reviewer's sequence were
gated closed pending resolution of this exact contradiction. **That
specific blocker is now resolved.** Whether to proceed to the actual
multiplication-operator construction is a separate, substantial
decision -- not automatic just because this gate cleared -- and is
deliberately left open here rather than started in the same round,
given the demonstrated fragility of hand-reasoning on this general
class of problem across this session.

## Kill Analysis

**Killed:** this round's own pre-registered P2 prediction (`R_i=-l_{e_i}`
directly) -- the correct form has the transpose (`-l_{e_i}^T`).

**Killed:** C94's `+l_{e_i}^T` left-translation candidate -- superseded
by `+l_{e_i}` (no transpose), traced to a specific, now-understood
conflation (raw-entry transformation vs coefficient-space
transformation).

**Not killed:** C94's own right-translation finding (`-l_{e_i}^T`) --
independently re-derived here via a different, bug-checked method and
confirmed to match.

## What this does NOT show

1. Does **not** by itself unblock the actual multiplication-operator
   construction or spectral-flow experiment -- resolving the specific
   blocker C94 identified is necessary but was never claimed sufficient
   for that separate, larger undertaking.
2. Does **not** retroactively validate any PRIOR round's numerical
   results that used a DIFFERENT candidate for the `q`-side generator
   (none exist yet -- `q` has been a pure spectator throughout C86-C93,
   this is the first round to derive its actual transformation law).
3. Does **not** change `N_gen=3`'s CONDITIONAL status.
4. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c95-coefficient-space-refinement-bracket-still-open/c95_coefficient_space_refinement.py
```
Self-contained -- reuses only C85's own certified `build_l_matrices`,
unmodified. The Ad-representation validation check and the numerical
finite-difference cross-check referenced above were run interactively
during this round's own verification and are not part of the committed
script; the script's own P1/P2/P3 checks are fully symbolic and
reproducible.
