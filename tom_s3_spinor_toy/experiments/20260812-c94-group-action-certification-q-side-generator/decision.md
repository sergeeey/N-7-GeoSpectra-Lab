# decision -- group action certified cleanly, C93's sign found wrong, but a genuine unresolved inconsistency surfaced (P3)

## Verdict

`GROUP_ACTION_GENERATORS_CONSISTENT_ACROSS_UNITS_BUT_BRACKET_CHECK_UNRESOLVED`
-> **P1 CONFIRMED (right-translation generator: `-l_{e_i}(1)^T`, uniform
across all 3 units). P2 CONFIRMED but NOT as predicted (left-translation
generator: `+l_{e_i}(1)^T`, uniform across all 3 units -- opposite sign
from C93's own `-l_{e_i}^T`). P3 FAILED (exploratory): the matched
left-translation candidate does not satisfy the expected bracket
relation, and this discrepancy was NOT resolved by further checking.**
**Date:** 2026-08-12 · L0: descriptive · script:
`c94_group_action_certification.py`, results: `results_c94.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** right-translation baseline | matches `l_{e_i}(1)` itself | **PARTIALLY WRONG AS PREDICTED, but internally consistent** -- the actual match, uniform across `e1,e2,e3`, is `-l_{e_i}(1)^T`, not `l_{e_i}(1)` directly. `l_{e_i}` itself does NOT literally correspond to "right multiplication by `e_i`" in this concrete `g=[[a,b],[-b̄,ā]]` embedding -- a new, previously-unknown fact, but NOT a contradiction of anything established elsewhere in this project (nothing prior claimed this specific identification; it was this round's own working assumption for P1, now corrected). | [VERIFIED-sympy] |
| **P2** left-translation | C93's `-l_{e_i}(1)^T` | **WRONG** -- the actual match, uniform across all 3 units, is `+l_{e_i}(1)^T` (opposite sign from C93). Machine-exact symbolic match for all 3 quaternion units independently. | [VERIFIED-sympy] |
| **P3** bracket consistency (exploratory) | `[Y1,Y2]=2Y3` for the matched candidate | **FAILED** -- `[Y1,Y2] = [[0,2i],[2i,0]]`, `2Y3 = [[0,-2i],[-2i,0]]` -- exact opposites. This contradicts the expectation (verified separately: `L_{h1}L_{h2}=L_{h1h2}` holds, both symbolically to first order AND numerically via an explicit 4-operator composition at finite `t`, matching a group-commutator second-order expansion to `O(t^3)` precision) that `dL` of a genuine group representation must be a genuine (non-anti) Lie algebra homomorphism. A follow-up BCH-style hand expansion of `π(h2)^{-1}π(h1)^{-1}π(h2)π(h1)` in terms of `Y1,Y2` was attempted to locate the discrepancy and did NOT cleanly resolve -- recorded as genuinely unresolved, not guessed at further. | [VERIFIED-sympy + numpy], contradiction UNRESOLVED |

## What this genuinely establishes

**C93's sign was WRONG.** The group-action-certified left-translation
generator is `+l_{e_i}(1)^T`, not `-l_{e_i}(1)^T`. This is now
established by DIRECT computation (symbolic differentiation of an
explicit matrix product, cross-checked numerically with the actual
matrix exponential and an explicit 4-step operator composition), not
by further hand algebra -- exactly the discipline this round was
directed to apply.

**But a genuine, more fundamental inconsistency was ALSO found while
verifying this result, and it is NOT resolved.** `+l_{e_i}(1)^T` (the
group-certified candidate) does not satisfy the bracket relation a
representation's own derivative must satisfy, given the group-level
representation property (`L_{h1}L_{h2}=L_{h1h2}`) is independently
confirmed correct. Three independent attempts to trace the source of
this (a direct symbolic bracket check, a numerical group-commutator
expansion, and a BCH-style hand expansion of the 4-operator product)
did not converge on an explanation. This means: **the "correct sign"
found by this round's own direct computation is itself now suspect**,
not because the computation was sloppy (every step was tool-verified
and cross-checked multiple independent ways), but because a basic
Lie-theory consistency check that SHOULD automatically hold for ANY
correctly-extracted generator of a verified representation does not
hold here.

**Honest interpretation:** either (a) there is a subtlety in how
first-order-truncated `h(eps)` curves relate to true one-parameter
subgroups that this round's setup does not correctly capture at the
level needed for bracket consistency (despite passing the standard
"tangent vector at `eps=0`" check), or (b) there is a genuine
convention mismatch between "the Lie bracket as measured via `[e_i,e_j]`
using Hamilton-product commutator" and "the Lie bracket as it actually
governs group-commutator expansion for THIS SPECIFIC representation,"
or (c) some other subtlety not yet identified. This round does not
determine which.

## Kill Analysis

**Killed:** C93's specific claim that `L_i = -l_{e_i}(k)^T` is the
group-action-certified `q`-side generator -- the group action itself
says `+l_{e_i}(1)^T`, not `-l_{e_i}(1)^T`, for the standard `(L_h
f)(g):=f(h^{-1}g)` convention.

**Not killed, but now flagged as unresolved rather than assumed:**
whether EITHER sign (`+l^T` or `-l^T`) is actually the physically
correct `q`-side generator for building the multiplication operator --
this round found `+l^T` is what the STANDARD group-action convention
gives, but also found `+l^T` fails an independent consistency check
that should hold automatically for a correctly-derived generator. This
is a strictly stronger finding than "C93 had the wrong sign" -- it says
the reliable way to determine the sign is not yet in hand.

## Gate status (per the external reviewer's own explicit instruction)

**This gate has NOT passed cleanly.** The reviewer's proposed sequence
(C94 group-action certification -> C95 double-CG certification -> C96
physical spectral-flow experiment) explicitly conditions C95/C96 on C94
being green. C94 found a real, tool-verified correction to C93 (real
progress) but ALSO surfaced a new, unresolved internal inconsistency
(P3) that must be resolved BEFORE this gate can be called passed. Per
the reviewer's own instruction ("я бы запретил любые новые crossing
scans... пока это не решено"), **no C95 or C96 work should proceed
until P3's discrepancy is understood**, not merely until SOME sign is
picked.

## What this does NOT show

1. Does **not** certify a final, trustworthy sign for the `q`-side
   generator -- P3's failure means neither `+l^T` nor `-l^T` (nor `+l`,
   `-l`) can currently be asserted with full confidence.
2. Does **not** resolve the P3 bracket-consistency contradiction --
   three independent attempts within this round did not locate its
   source.
3. Does **not** test `j=1` (`k=2`) as an independent replication --
   deliberately not attempted given P3's own unresolved status; running
   a second-representation check on an already-inconsistent method
   would not add confidence.
4. Does **not** build or test the multiplication operator (C95/C96 in
   the reviewer's sequence) -- explicitly gated, not attempted.
5. Does **not** change `N_gen=3`'s CONDITIONAL status.
6. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c94-group-action-certification-q-side-generator/c94_group_action_certification.py
```
Self-contained -- reuses only C85's own certified `hamilton_product`/
`build_l_matrices`, unmodified. The numerical cross-checks (numpy/scipy
matrix exponential, explicit 4-step operator composition) referenced
in this decision.md were run interactively during this round's own
analysis and are not part of the committed script -- the script itself
contains the symbolic P1/P2/P3 checks that ARE committed and
reproducible.
