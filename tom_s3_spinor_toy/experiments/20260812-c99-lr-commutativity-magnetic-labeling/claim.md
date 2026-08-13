# C99 -- [L_i,R_j]=0 commutativity + magnetic-number labeling for the multiplication-operator build

**Experiment id:** `20260812-c99-lr-commutativity-magnetic-labeling`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C85 (certified `l_{e_i}(k)`, q a pure spectator).
C90 (structural no-go for translation-generator couplings; verified,
via sympy's exact `CG` class, ONE representative Clebsch-Gordan
coefficient -- extremal weight only, `m1=j1` -- confirming the
mathematical basis for a multiplication-type coupling operator, but
explicitly NOT building the operator itself). C91-C98 (certified
`L_i(k)` acting on q and `R_i(k)` acting on p, for k=1,2,3,4; found
`L_i(1)=+l_{e_i}(1)`, `R_i(1)=-l_{e_i}(1)^T` at k=1, versus
`L_i(k)=-l_{e_i}(k)^T`, `R_i(k)=+l_{e_i}(k)` for k=2,3,4 -- roles
swap between k=1 and k>=2).

---

## Why this is needed before building the multiplication operator

C90's decision.md explicitly scoped the next step as: "construct the
multiplication-type coupling operator properly in the certified
`(p,q,r)` basis... verify it against the full set of Clebsch-Gordan
coefficients (not just the one representative checked here)." Doing
that requires knowing the correct magnetic-number (`m`) label for
EVERY basis index `q` and `p` at every level `k` -- not just the
single extremal case C90 checked. That labeling is only meaningful if
`q` and `p` genuinely transform under INDEPENDENT `su(2)` actions
(left- and right-translation respectively), which is the standard
`su(2)_L x su(2)_R = so(4)` picture this entire project already
assumes throughout (round59's own `so(4)` machinery, etc.) -- but
**`[L_i(k), R_j(k)]=0` has never actually been verified in this
session**, across the four-attempt, repeatedly-corrected arc that
produced `L_i`/`R_i` (C92-C98). Building a multiplication operator on
an unverified independence assumption would repeat exactly the kind of
error this project's own rules exist to catch (an unstated condition
silently required for a later result to hold).

## Method

1. **P0 (commutativity):** for `k=1,2,3,4`, compute all 9 commutators
   `[L_i(k), R_j(k)]` (`i,j` in `{1,2,3}`) using the certified matrices
   from C95 (k=1) and C96/C97/C98's shared construction (k=2,3,4),
   verify each is exactly zero symbolically.
2. **P1/P2 (magnetic-number extraction):** `l_{e1}(k)` is diagonal
   (Meier eq 6.1, certified in C85), so `L_1(k)` and `R_1(k)` are
   diagonal too (each is `+-l_{e1}(k)` or `+-l_{e1}(k)^T`, and
   transposing a diagonal matrix does nothing) -- extract
   `m_q(k,q) := L_1(k)[q,q]/i` and `m_p(k,p) := R_1(k)[p,p]/i`
   directly from the certified generators (not assumed from `l_{e1}`'s
   own convention, which C96-C98 already showed can differ by sign
   from `L_1`/`R_1` depending on `k`).
3. **P3 (cross-check against C90):** using the derived `m_p(k,p)`,
   recompute C90's own single-representative CG check (`m1=j1`, i.e.
   the extremal-weight case, `p=k`) and confirm it reproduces C90's
   result exactly -- a consistency check between the two independently
   -derived pieces (C90's CG verification, C91-C98's generator
   derivation) before they are combined into anything new.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P0** | `[L_i(k),R_j(k)]=0` exactly, for all `i,j`, at `k=1,2,3,4` (36 checks total) | pending |
| **P1** | `m_q(k,q)` is well-defined (L_1(k) diagonal) and forms a clean, evenly-spaced pattern across `q=0..k` | pending |
| **P2** | `m_p(k,p)` is well-defined similarly | pending |
| **P3** | recomputing C90's extremal-weight CG check using the derived `m_p(k,p)` (at `p=k`) reproduces C90's own result (coefficient `1`, exact) for `k=1,2,3` | pending |

## kill_criterion

If P0 fails for even one `(i,j,k)` combination, the `su(2)_L x
su(2)_R` independence assumption this whole construction relies on is
FALSE for this specific generator pair -- stop, do not build a
multiplication operator on top of this until resolved; this would be a
major, load-bearing finding requiring its own dedicated investigation,
not a quick patch. If P0 holds but P1/P2 show `m_q`/`m_p` is not a
clean evenly-spaced pattern, the "magnetic number" interpretation
itself needs revisiting before CG coefficients can be meaningfully
attached to specific `(q,p)` pairs. If P0-P2 hold but P3 fails
(disagrees with C90), there is a sign/convention mismatch between
C90's own CG check and C91-C98's own generator convention that must be
resolved before either is trusted as an ingredient in the actual
operator build.

## What this cannot show

- Does **not** build the multiplication operator itself, nor verify
  the FULL set of CG coefficients (all `q,p` pairs, not just the
  extremal one) -- that remains the next round after this.
- Does **not** address `r`'s role in the multiplication operator (an
  open question this round explicitly does not attempt to resolve --
  `D^1_{ab}(g)` is scalar-valued and does not obviously touch the
  Clifford index `r` that `build_dbar` uses; how the two combine, if
  at all, is deferred).
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
