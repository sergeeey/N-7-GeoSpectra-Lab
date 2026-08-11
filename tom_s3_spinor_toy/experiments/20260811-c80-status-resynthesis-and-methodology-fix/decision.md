# decision -- pair completed (same artifact both halves); methodology flaw identified; C76-C79 re-synthesized; recommendation given

## Verdict

`PAIR_COMPLETED_SAME_ARTIFACT__TEST_METHODOLOGY_FLAW_IDENTIFIED__NGEN3_STILL_CONDITIONAL__RECOMMEND_PAUSE_ON_BLIND_POSTULATE_SEARCH`
-> **P1 CONFIRMED. P2 CONFIRMED. P3 CONFIRMED.**
**Date:** 2026-08-11 · L0: descriptive · script:
`c80_antiselfdual_completion.py`, results: `results_c80.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** mirror symmetry | anti-self-dual closes with opposite structure constant | **CONFIRMED, exact** -- self-dual: `-2.0` (all 3 cyclic relations, residual `0.0`); anti-self-dual: `+2.0` (all 3, residual `0.0`). | [VERIFIED-numpy] |
| **P2** mirrored crossing | one crossing at `eps=-1.5` | **CONFIRMED, exact** -- self-dual crossing at `eps=+1.5` (min\|eigval\|~`1.4e-15`, reproducing C79 exactly); anti-self-dual crossing at `eps=-1.5` (min\|eigval\|~`9.6e-17`). Both single crossings over a finer 161-point sweep (vs C79's original 81 points) -- no additional crossings found at higher resolution. | [VERIFIED-numpy] |
| **P3** same artifact | anti-self-dual crossing also ~100% in raw kernel | **CONFIRMED** -- `frac_in_raw_kernel = 0.9999999999999996` for the anti-self-dual crossing, matching the self-dual case's `0.9999999999999991` to the same precision. | [VERIFIED-numpy] |

## The methodological lesson, stated precisely

C79 found one crossing, traced it to an artifact, and could have been read
as "this specific postulate happened to hit a coincidence." **This round
shows that reading is wrong.** Both independent halves of `so(4)_1` --
algebraically different objects (opposite-sign structure constants,
genuinely different `su(2)` embeddings) -- produce the identical failure
mode: a crossing that is essentially entirely inside `D_S6`'s pre-existing
36-dimensional raw kernel. The mechanism is generic: `D_S6`'s raw kernel is
large (36 of 64 dimensions) and highly degenerate (all exactly zero); ANY
Hermitian perturbation restricted to a large degenerate eigenspace splits
it into a spread of eigenvalues proportional to the perturbation's own
matrix elements there, and for a strength parameter swept across a
symmetric range, SOME linear combination will generically cross zero for
SOME `eps` -- this is close to guaranteed by the pigeonhole principle
applied to a 36-dimensional spread, not evidence of new physics.

**Consequence for future non-product attempts:** the test design used in
C79/C80 (build `Sigma(x)Sigma`-level coupling, sweep `eps`, look for any
zero-crossing in the full space) is **not a valid discriminating test**
as currently built -- it will very likely report "a crossing" for almost
any sufficiently generic coupling term, regardless of whether that
coupling reflects anything physical. A future attempt (testing `so(4)_2`,
other elements of C78's 20-dim complement, or a different S3 sector
entirely) using this SAME design would very likely reproduce the same
uninformative pattern. **The correct fix, named here but not built:**
restrict the search to the physically-relevant sector (analogous to
C73's own `invariant_basis` restriction to the `su(3)`-invariant sub-block,
where the real `kernel=1` result lives) BEFORE sweeping for crossings --
i.e. project out `D_S6`'s raw 36-dim kernel first, or work directly in the
already-established 2-dim domain / 1-dim target invariant sector, so that
any crossing found there could not be a raw-kernel artifact by
construction.

## Re-synthesis: where C76-C80 collectively leave `N_gen=3`

C76 (immediately after C75) named the single most load-bearing gap as
"a genuine channel-permuting operator does not exist" and flagged the
`SO(4)xSO(4)` transport matrix `T` as the most concrete unattempted lead.
Three rounds later, with substantially more information:

- **The algebraic-symmetry question is now closed exhaustively, not
  piecemeal.** C77 showed `SO(4)xSO(4)` fails Gate 2 (all 12/12
  generators). C78 then proved, in one computation covering the entire
  28-dimensional `so(8)`, that `su(3)` is the FULL commutant of the
  physical `D` -- no candidate of any kind survives. This is strictly
  stronger than "we tried two things and both failed."
- **A genuine, internally-derivable, non-product construction is now
  known to be buildable and testable** (C79), where before this session
  even KT-8/round67's own original work never built one as an explicit
  matrix. The specific postulate tried (round67's `Z_i` coupled to
  `so(4)_1`'s two `su(2)` halves) returns a clean, well-understood NULL --
  not a resolved mechanism, but also not a mysteriously unexplained
  failure.
- **A real methodological gap in the bridge machinery (`U_v`'s
  non-unitarity) was found, fixed, and -- critically -- checked for
  impact on the entire C75-C78 chain, which was found ROBUST.** This
  strengthens confidence in the prior chain rather than casting doubt on
  it.
- **This round's own contribution: the specific non-product test design
  used in C79 is now known to be structurally unable to discriminate
  genuine physics from a large-degenerate-kernel artifact**, for any
  generic coupling of the kind tried. This is itself a piece of load-
  bearing methodological knowledge for any future attempt.

**The pre-commitment (predictions_before_data.md's P1/P3/P5) remains
untouched by any of C77-C80** -- none of these rounds are part of that
frozen table. `N_gen=3` stays CONDITIONAL, exactly as C76 concluded.

## Recommendation: pause the blind non-product postulate search

Given (a) the algebraic-symmetry space is now exhaustively closed (C78),
(b) L3B's own day-long 2026-07-15 investigation already tried multiple
non-product/`G2`-breaking candidates and concluded the surviving route
needs Part 5, (c) this session's own two-candidate non-product attempt
(C79/C80) returned a clean NULL via a mechanism now understood to likely
generalize to any similarly-designed test, and (d) no principled reason
distinguishes the untested candidates (`so(4)_2`, other elements of C78's
complement) from the two already tried in a way that would predict a
different outcome -- **the honest recommendation is that further blind
postulate testing with the CURRENT test design has reached diminishing
returns.** This is not a claim that no non-product construction could
ever work -- it is a claim that testing more of them the SAME way is
unlikely to produce new information.

**Two genuinely different next steps would produce new information,**
named here for a future round, not attempted:
1. **Fix the test design** (project out the raw kernel / restrict to the
   physically-relevant invariant sector) and re-test even the SAME two
   candidates (`so(4)_1`'s two halves) properly -- this could still find
   a genuine signal the current design cannot see, since the artifact
   swamps rather than rules out a real effect.
2. **Escalate to the full Peter-Weyl tower** rather than the `n=0`
   sector alone, closer to what KT-8's own original (product-only)
   zero-kernel result actually covers -- a larger but more decisive
   undertaking.

## Kill Analysis

**Not killed:** any of C76-C79's own results -- all reused/confirmed by
citation, none contradicted.

**Killed:** any reading of C79's single crossing as possibly being a
coincidence of one specific postulate -- confirmed here to be a general
property of the test design, applying identically to both tested
candidates.

**What survives:** the two concretely-scoped next steps named above,
neither attempted in this round.

## What this does NOT show

1. Does **not** test any candidate beyond `so(4)_1`'s two halves.
2. Does **not** redesign the coupling test with the raw kernel excluded --
   named as the correct next step, not built here.
3. Does **not** change `N_gen=3`'s CONDITIONAL status.
4. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260811-c80-status-resynthesis-and-methodology-fix/c80_antiselfdual_completion.py
```
Reuses C79's `get_bridge_to_sigma`/`leibniz_matrix`/`check_su2_closure`/
`self_dual_anti_self_dual_triples` and all of C79's own module-level
reuses, unmodified.
