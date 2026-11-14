# C202 Claim — apply the C201-calibrated intertwiner test to Tom Lawrence's own real l=1 matrices

**Date:** 2026-09-23
**FL tier:** [x] Standard (tooling/comparison round in support of external correspondence; no project physics claim)
**Question type:** [x] descriptive (are two explicit 3x3 representations of so(3) equivalent, and is Tom's own document internally consistent)

**Source:** direct continuation of C201. Tom's own document ("Ket spaces and
harmonics of S^n", v5, 2026-09-07 -- re-sent by Tom 2026-09-23 in reply to a
direct request) supplies the previously-missing eq(103)-(105) [T_ij defining
rep], eq(99) [Gamma_3(T)=-T], eq(106)-(108) [Gamma_3(T_ij), vector-multiplet
rep], eq(118) [z, real->complex basis change], and eq(123)-(125) [Gamma'_3(T_ij),
the explicit numeric matrices Tom's own homework request asked to compare
against]. This round runs that comparison for real, using the C201-validated
`T_i U = U L_i` methodology.

## Prior Result Gate

1. Exact claim: (a) Tom's own eq(123)-(125) are exactly reproduced from his
   more primitive eq(99)+(103)-(105)+(118)+(122) -- a transcription/internal-
   consistency self-check, not yet performed on this document. (b) an
   invertible intertwiner `U` exists making Tom's Gamma'_3(T_12,T_23,T_31)
   equivalent to our own C201 (l=1 ladder-operator) L_z,L_x,L_y, under the
   role correspondence Tom states himself in his eq(67)-(69).
2. `grep` of `null_results/INDEX.md`, `parked/INDEX.md`, `pearl_registry/INDEX.md`
   for "ladder operator", "McMurry", "intertwiner": hits found, but all in
   OTHER contexts (G20 Yukawa intertwiner, C70-C79 triality bridges, this
   project's own G2/SU(3) work) or in the DIFFERENT, EARLIER
   `20260728-tom-so3-harmonics-sign-check` round -- see below.
3. **Directly relevant prior result, read in full before proceeding:**
   `experiments/20260728-tom-so3-harmonics-sign-check/` verified a DIFFERENT,
   earlier (2026-07-28) draft of Tom's harmonics notes and found a real,
   reusable lemma (`TRANSPOSE_LEMMA.md`): comparing a differential operator's
   honest per-basis-element matrix against an abstract generator matrix can
   silently produce the TRANSPOSE (or negative-transpose) of the correct
   answer for an asymmetric so(3) generator, while a diagonal/symmetric one
   is unaffected. That round's setup (differential operator vs stated matrix,
   via a suspect "matrix times combined vector" comparison) is NOT identical
   to this round's setup (search for a genuine similarity transform between
   two already-abstract matrix representations), but the transpose/negative-
   transpose failure mode is directly relevant and was explicitly tested for
   here (Part 2) rather than assumed away.
4. **Status:** [x] NEW (this specific comparison, against the September
   document's real numbers, has not been run before).

## Estimand

**Population:** the l=1 (j=1) representation of so(3), realized two ways:
(i) our own C201 construction (ladder operators L_z, L_x=(L++L-)/2,
L_y=(L+-L-)/2i); (ii) Tom's own Gamma'_3(T_12), Gamma'_3(T_23), Gamma'_3(T_31)
[eq 123-125], built by him via a change of basis (eq 118) from the real
vector-multiplet generators (eq 106-108).
**Intervention/method:** exact symbolic (sympy) reconstruction of eq(123)-(125)
from eq(99)+(103)-(105)+(118) [transcription self-check]; search for an
invertible 3x3 `U` solving `T_role U = U L_role` for two of the three role
correspondences Tom states in his own eq(67)-(69) (T_12<->L_z, T_23<->L_x),
holding out the third (T_31<->L_y) as an independent check; if the holdout
fails, classify the failure mode (EQUAL/TRANSPOSE/NEGATIVE/NEGATIVE_TRANSPOSE/
NO_SIMPLE_RELATION) before concluding anything.
**Comparator:** the null/failure outcome would be NO_SIMPLE_RELATION on the
holdout even after the transpose/negative checks -- meaning the two
representations are genuinely NOT equivalent (a real convention or derivation
conflict, not just an index-labeling artifact).
**Endpoint:** boolean match on Part 0 (transcription self-check, all three);
existence/rank of `U` (Part 1); holdout classification (Part 1); and, if the
holdout resolves to TRANSPOSE=NEGATIVE (which is automatic for these
generators since they are all antisymmetric matrices, M^T=-M), whether the
single benign role-correspondence fix (T_31<->-L_y instead of T_31<->+L_y)
makes all three checks pass simultaneously with the SAME U (Part 3).

## Kill criterion

| Condition | Consequence |
|---|---|
| Part 0 transcription self-check does not fully match | Either my transcription of eq(103)-(125) has an error (fix and re-check before proceeding), or Tom's own document has a real internal inconsistency (report explicitly, do not silently "fix" it) |
| No invertible `U` solves T_12<->Lz and T_23<->Lx simultaneously | The two representations are NOT equivalent under the stated role map at all -- stop, do not force a holdout check |
| Part 3's corrected role map does not make all three checks pass | Real, unresolved discrepancy between Tom's construction and ours -- report as NO_SIMPLE_RELATION, do not paper over with a guessed sign |

If FAIL → kills: the claim that our C201 l=1 construction and Tom's own
(123)-(125) describe the "same" so(3) representation in any simple sense.
If PASS → survives: Tom's homework request (compare our ladder-derived
matrices to his own) is answered, with an explicit, reportable intertwiner
and one benign, named convention correction.

## Checks planned

| # | Check | Negative control -- input for which this check MUST fail |
|---|---|---|
| T1 | Part 0 transcription self-check (reconstruct 123-125 from more primitive eqs) | Deliberately negate one primitive input (done live: the first run DID fail here, for a real reason -- see decision.md) |
| T2 | Part 1 intertwiner solve + independent holdout on T_31<->L_y | An unrelated random invertible 3x3 matrix in place of the derived U must NOT satisfy the holdout (not run as a separate control; the FIRST real run already produced a genuine non-EQUAL holdout result, which is itself the informative outcome, not a null-control substitute) |
| T3 | Part 2 transpose/negative scan | If Part 1's holdout were EQUAL, Part 2 is skipped entirely (`needed: False`) -- this branch was exercised for real since Part 1's holdout was NOT EQUAL |

## What this does NOT mean

1. Does NOT constitute a reply to Tom or a claim that his own document
   contains an error -- eq(123)-(125) are exactly, internally consistent
   with his own eq(99)+(103)-(108)+(118)+(122); the only sign issue found
   was in MY OWN transcription (fixed, see decision.md) and MY OWN role-map
   convention choice (T_31<->+L_y vs -L_y, a benign index-ordering matter).
2. Does NOT touch this project's own G2/SU(3)/Spin(8) triality-channel
   physics claims (OB1, N_gen=3) -- unrelated substrate.
3. Does NOT establish anything about Tom's actual S^3 spinor multiplet
   construction (section 3.3 of his own document) -- this round is scoped
   to the already-worked S^2 vector-multiplet example only (his eq 100-132).

## Fence

- `safe_for_runtime = False`. No `lambda` symbol introduced.

## Verdict

**PROMOTE.** All three parts pass by exact symbolic computation (sympy, zero
approximation). Two real bugs were caught and fixed during the run, both
self-caught by the round's own built-in self-checks, not found by an external
reviewer:
1. A transcription bug (eq99's `Gamma_3(T)=-T` negation was applied to T_23
   but mistakenly NOT applied to T_12/T_31 in the first draft) -- caught by
   Part 0's own self-consistency check (all three legitimately failed, for a
   real and identifiable reason), fixed, then Part 0 passed cleanly.
2. A `zero_check` helper bug (`sympy.Matrix == 0` never returns True
   regardless of content; must check entrywise) -- caught by manually
   verifying a known-zero matrix against the helper, which is exactly the
   discipline `audit-verification-gate.md` and this project's own
   `feedback-repaired-check-repeats-tautology` memory both call for before
   trusting any check's PASS/FAIL output.

The final, corrected result: Tom's own (123)-(125) matrices are representation-
equivalent to our C201 ladder-operator construction via the explicit
intertwiner `U = diag(-1, sqrt(2)/2, 1)`, under the role map T_12<->L_z,
T_23<->L_x, T_31<->-L_y (a benign index-ordering sign on the antisymmetric
(3,1)/(1,3) pair, not a derivation error on either side).

**Evidence:** [VERIFIED-sympy 7/7] (3 transcription-reconstruction checks +
1 intertwiner existence/rank check + 3 corrected-role-map checks, all exact).

**Status:** CLOSED PROMOTE.
