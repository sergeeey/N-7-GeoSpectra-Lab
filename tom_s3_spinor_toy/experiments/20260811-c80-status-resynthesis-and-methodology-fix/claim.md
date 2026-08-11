# C80 -- complete the self-dual/anti-self-dual pair, extract the methodological lesson, re-synthesize C76-C79

**Experiment id:** `20260811-c80-status-resynthesis-and-methodology-fix`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C76 (last status synthesis, now three rounds stale);
C77 (second Gate-1 candidate fails Gate 2); C78 (exhaustive so(8)
commutant of `D` equals `su(3)` exactly); C79 (first genuine non-product
attempt, NULL, explained as a raw-kernel artifact)

---

## Why this round, and why now

The user's last four instructions ("try a genuinely new construction,"
"go for the non-product construction," then an open "Continue with C80")
left the choice of what C80 should be to this round's own judgement. Ten
rounds into the decisive-experiment program (C70-C79) -- four beyond the
original six-round plan -- with C78 having exhaustively closed the
algebraic-symmetry search and C79 having returned the first genuine
non-product data point, the highest-value use of C80 is not another
blind postulate test: it is (1) a cheap, already-scoped completion of
C79's own pair (the anti-self-dual half of `so(4)_1`, reusing C79's
machinery unmodified), and (2) an honest re-synthesis of what C76-C79
collectively mean for `N_gen=3`, including a clear-eyed recommendation on
whether continuing to enumerate non-product postulates is still the best
use of further rounds.

## The claim under test

> **C80 (working).** The anti-self-dual triple (the other half of
> `so(4)_1`) produces the same qualitative result as C79's self-dual
> triple: exactly one crossing, sign-mirrored (`eps=-1.5` vs `+1.5`,
> matching the opposite structure constants), essentially 100% inside
> `D_S6`'s already-known 36-dim raw kernel. **This is not merely "another
> NULL data point" -- it demonstrates that the test methodology itself
> (sweep coupling strength, look for any crossing in the full 128-dim
> space) cannot distinguish genuine physics from this artifact for ANY
> generic coupling**, not just the two tested. Continuing to test more
> individual generators with the same methodology would very likely
> reproduce the same artifact each time without new information; a
> future non-product attempt needs to redesign the test (exclude/project
> out the raw kernel) before another postulate is worth trying.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (mirror symmetry)** | anti-self-dual triple closes as `su(2)` with the OPPOSITE structure constant sign to C79's self-dual triple (`+2` vs `-2`) | pending |
| **P2 (mirrored crossing)** | exactly one crossing, at `eps=-1.5` (sign-flipped from C79's `+1.5`), matching the sign-flipped structure constant | pending |
| **P3 (same artifact)** | the anti-self-dual crossing's eigenvector also lies essentially 100% inside `D_S6`'s 36-dim raw kernel, confirming the SAME mechanism, not a coincidence specific to the self-dual choice | pending |

## kill_criterion

P1/P2 fail if the anti-self-dual triple does not mirror the self-dual
result in the expected way -- would indicate an error in the self-dual/
anti-self-dual construction itself (C79's own, reused here) and require
revisiting C79's conclusions, not just this round's. P3 fails if the
anti-self-dual crossing's eigenvector is NOT dominated by the raw kernel
-- would mean the artifact explanation was specific to the self-dual
choice, not general, and the "methodology is unreliable" conclusion
above would need to be withdrawn, not merely softened.

## What this cannot show

- Does **not** test any candidate beyond `so(4)_1`'s two halves --
  `so(4)_2`, other elements of C78's 20-dim complement, and the full
  Peter-Weyl tower remain untested, exactly as C79 already noted.
- Does **not** redesign or re-run the coupling test with the raw kernel
  excluded -- names this as the correct next step for a FUTURE attempt,
  does not attempt it here (a genuinely new, separately-scoped
  undertaking).
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
