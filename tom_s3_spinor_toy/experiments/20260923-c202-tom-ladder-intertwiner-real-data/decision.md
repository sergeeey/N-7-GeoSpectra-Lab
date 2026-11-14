# C202 Decision — Tom's real (123)-(125) matrices ARE equivalent to our C201 construction

**Date:** 2026-09-23
**Verdict:** PROMOTE (Standard tier, correspondence-support round)

## What was checked (all `[VERIFIED-sympy]`, `c202_tom_ladder_intertwiner.py`)

| Part | Check | Result |
|---|---|---|
| 0 | Reconstruct Tom's eq(123)-(125) from eq(99)+(103)-(105)+(118)+(122) | All 3 match, exactly, after fixing the transcription bug below |
| 1 | Solve for `U` using T_12<->L_z, T_23<->L_x; hold out T_31<->L_y | `U = diag(-1, sqrt(2)/2, 1)`, det != 0; holdout classified **TRANSPOSE** |
| 2 | Scan TRANSPOSE/NEGATIVE/NEGATIVE_TRANSPOSE on the failed holdout | similarity(T_31) == -L_y == L_y^T (both true simultaneously -- automatic, since every so(3) generator built here is antisymmetric, M^T=-M) |
| 3 | Re-check all three under the corrected role map T_31<->-L_y | All 3 pass with the SAME `U` |

## Two self-caught bugs (both real, both fixed, both caught by this round's own built-in checks, not by an external reviewer)

### Bug 1 — transcription: eq(99)'s negation dropped for two of three generators

Tom's eq(99) states `Gamma_3(T_ij) = -T_ij`: the vector-multiplet generators
are the NEGATIVE of the "defining representation" generators T_ij (eq 103-105).
The first draft of this script applied that negation correctly when building
`g_t23`, but for `g_t12` and `g_t31` it used the eq(103)-(105) values directly
(i.e. `T_ij` itself, not `-T_ij`). Part 0's self-check caught this immediately:
reconstructing eq(123)/(125) from the un-negated inputs gave the exact
NEGATIVE of Tom's own stated matrices, while eq(124) (the one generator that
was, by luck, transcribed with the negation already applied) matched. The
asymmetric 2-out-of-3 failure pattern was itself the diagnostic clue -- traced
by hand-verifying `z*T12*z^-1` against the actual PDF text for eq(99) and
eq(108), confirmed via a small standalone diagnostic script
(`_diag_z_convention.py` / `_diag_fixed.py`, both scratch files, deleted after
use) before touching the main script. Not Tom's error -- entirely mine, in
copying eq(103)-(105) directly instead of applying eq(99) uniformly.

### Bug 2 — a "cannot-fail" check: `sp.Matrix == 0` never returns True

The original `zero_check(expr)` helper computed
`sp.simplify(sp.expand_complex(expr)) == 0`, which works for scalar
expressions but NOT for `sympy.Matrix` objects -- a `Matrix` never compares
equal to the Python `int` `0` regardless of its entries, so every Part 0/1/2
comparison silently reported `False` even after Bug 1 was fixed (confirmed
live: after fixing Bug 1, Part 0 STILL printed `ALL MATCH: False`, which was
the tell that a second, independent bug was hiding behind the first). Verified
directly (`sp.zeros(3,3) == 0` returns `False`) before patching. Fixed by
checking each matrix entry individually when the simplified result is a
`MatrixBase`. This is exactly the "cannot-fail check" class already named in
this project's own memory (`feedback-repaired-check-repeats-tautology`,
`cross-repo-cannot-fail-check-class`) and in `audit-verification-gate.md`'s
Validation Theater Guard -- caught here by actually re-running a known-zero
sanity case against the helper before trusting its verdict, not by assuming
"my code looks right."

## Final result, in plain terms

Tom's own l=1 SO(3) generators (his eq 123-125, built by him via a change of
basis from the real vector-multiplet generators) and our own C201 ladder-
operator-derived matrices describe the SAME representation of so(3). The
explicit intertwiner is `U = diag(-1, sqrt(2)/2, 1)`. The one correction
needed is a sign on the third generator's role assignment (T_31 corresponds
to `-L_y`, not `+L_y`, under our respective index-ordering conventions) --
this is a standard, benign labeling ambiguity on an antisymmetric generator
pair (is "T_31" the generator FROM axis 3 TO axis 1, or the reverse?), not a
derivation error on either side.

## Relevance to the July 28 TRANSPOSE_LEMMA

`experiments/20260728-tom-so3-harmonics-sign-check/TRANSPOSE_LEMMA.md`
documents a related but DISTINCT failure mode: comparing a differential
operator's honestly-built matrix to a stated abstract matrix via "matrix
times a combined vector of basis functions" silently yields a transpose for
asymmetric generators. This round's setup never uses that combined-vector
comparison -- it solves a genuine linear system for an intertwiner between
two already-abstract matrices. That the SAME transpose/negative-transpose
failure shape showed up here too is consistent with (not evidence against)
the general lesson: any SO(3)-generator comparison that isn't scoped to a
symmetric/diagonal generator should expect and explicitly test for a
transpose or negative-transpose relationship before calling a mismatch real.

## What this means for the Tom Lawrence correspondence

His original homework request (compare our ladder-operator-derived 3x3
matrices to his own (123)-(125), "do they relate as linear combinations") now
has a complete, tool-verified answer: yes, via an explicit similarity
transform, with one clean sign note on the third generator's labeling. This
closes 2 of his 3 original asks (McMurry, matrix comparison); the third
(Cartesian rework via his eq 67-69) is unblocked by the same document and not
yet separately run. NOT sent to Tom -- per the standing DO NOT INITIATE
CONTACT rule, any reply requires the user's own explicit send decision.

## Reproduce

```
cd experiments/20260923-c202-tom-ladder-intertwiner-real-data
python c202_tom_ladder_intertwiner.py
```
