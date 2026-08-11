# C83 -- the genuinely untested remainder of C78's 20-dim complement, plus a new finding along the way

**Experiment id:** `20260811-c83-remaining-complement-test`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C78 (exhaustive `so(8)` commutant of `D_S6` equals
`su(3)`, dim 8, complement dim 20); C77/C79-C82 (all 12 generators of
round119's `so(4)_1+so(4)_2`, both `su(2)` halves each, tested against
`D` two different ways -- Gate 2 and the corrected non-product coupling
test); C81 (the corrected, raw-kernel-excluded test methodology, reused
unmodified here)

---

## A new finding, made while scoping this round (not assumed, computed)

Before designing the coupling test, this round asked precisely how much
of C78's 20-dim complement `so(4)_1+so(4)_2` (12 generators) has actually
already covered, rather than guessing. **Answer, computed three
independent ways and cross-verified: `so(4)_1+so(4)_2`'s 12-dim span has
a genuine, exact 1-dimensional intersection with `su(3)` itself** --
i.e. one specific linear combination of the 12 `so(4)+so(4)` generators
(coefficients `-1/sqrt(6)` on `so(4)_1`'s `e23` and `so(4)_2`'s `e03`,
found via a joint SVD, verified `[D, Leibniz(that combination)] = 2.79e-16`,
machine precision) **commutes with the physical `D` exactly**, even
though C77 correctly found that none of the 12 individual BASIS
generators do. **This does not contradict C77** -- its claim was about
the 12 basis elements individually, which is still true -- but reveals
additional structure C77 could not see by testing basis elements alone.

**Consequence for "how much of the complement is genuinely untested":**
`so(4)_1+so(4)_2`'s shadow WITHIN the complement (i.e., discounting the
1-dim piece that's actually in `su(3)`, not the complement at all) has
rank exactly **11**, not 12 -- computed via projecting the 12 generators'
coordinates onto the complement's own orthonormal basis and taking the
matrix rank (verified rank-aware via SVD, since a naive unpivoted QR
silently mishandles the resulting rank deficiency -- caught and fixed
during this round's own scoping, not glossed over). **The genuinely new,
never-tested part of the complement is therefore `20-11=9`-dimensional**,
with an explicit orthonormal basis extracted (verified: zero overlap with
`so(4)_1+so(4)_2`'s shadow to `4.6e-16`, clean identity Gram matrix, and
every one of the 9 generators individually has a large nonzero commutator
with `D`, confirming they are genuinely within the non-commuting
complement).

**This 9-dim piece does not close as its own Lie subalgebra** (checked:
30-58% of each pairwise bracket falls outside the 9-dim span) -- expected
and unremarkable, since (unlike `so(4)_1`/`so(4)_2`, genuine `so(4)`
subalgebras by explicit construction) this piece is simply "whatever is
left" from an SVD-based decomposition, with no a priori algebraic
structure.

## The claim under test

> **C83 (working).** With no natural `su(2)`-triple structure available
> in the remaining 9 dimensions (unlike `so(4)_1`/`so(4)_2`), this round
> tests it in three natural groups of 3 (the SVD-ordered orthonormal
> basis, generators `[0,1,2]`, `[3,4,5]`, `[6,7,8]` -- a reproducible,
> non-cherry-picked but not physically privileged choice, stated as
> such), each paired with round67's `Z_i` via C81's exact corrected
> (raw-kernel-excluded) methodology. **Prediction:** no genuine crossing
> in any of the three groups -- consistent with every other candidate
> tested in this arc (round124's centralizer, both `so(4)` blocks) under
> the corrected methodology returning clean nulls. This completes the
> ENTIRE 20-dim complement's coverage (11 dims effectively tested via
> `so(4)_1+so(4)_2`, 9 dims tested here) for THIS specific `Z_i`-coupling
> construction restricted to `S3`'s `n=0` sector.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (overlap verification)** | the found `so(4)+so(4) cap su(3)` direction commutes with `D` exactly | pending (already computed during scoping, re-verified in the permanent script) |
| **P2 (remaining-dim computation)** | the genuinely untested complement is exactly 9-dimensional, rank-verified | pending (re-verified in-script) |
| **P3 (group 1, generators 0-2)** | no crossing under C81's corrected test | pending |
| **P4 (group 2, generators 3-5)** | no crossing | pending |
| **P5 (group 3, generators 6-8)** | no crossing | pending |

## kill_criterion

P1/P2 fail if the scoping computation doesn't reproduce -- would mean a
bug in this round's own linear algebra, must stop and fix before
trusting anything downstream. **P3/P4/P5 are the actual test.** A "no
crossing" result completes the FULL 20-dim complement's coverage as a
clean, systematic negative -- not a failure. A crossing in any group
would be the first candidate anywhere in this project's `so(8)` search to
survive the corrected test and must receive the same extra scrutiny
(fine-scan avoided-crossing verification) every prior unexpectedly
positive result in this arc has received before being trusted.

## What this cannot show

- Does **not** test the full Peter-Weyl tower -- `S3`'s `n=0` sector
  only, same scope limit as every prior round in this arc.
- Does **not** claim the specific 3-groups-of-3 partition is uniquely
  correct or physically motivated -- it is a reproducible, systematic
  choice covering the full 9-dim space, not a privileged one.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
