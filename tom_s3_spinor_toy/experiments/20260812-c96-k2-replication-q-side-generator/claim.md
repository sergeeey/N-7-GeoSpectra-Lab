# C96 -- does C95's q-side generator formula (L_i=+l_{e_i}) generalize beyond k=1?

**Experiment id:** `20260812-c96-k2-replication-q-side-generator`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C95 (resolved C94's bracket-consistency contradiction
at `k=1`/`j=1/2` only: `L_i=+l_{e_i}(1)` directly, `R_i=-l_{e_i}(1)^T`,
both bracket-verified).

---

## Why this is needed before building anything on top of C95

C95's entire construction used `D^{1/2}(g)=g` literally -- the
2x2 defining representation matrix. This is a SPECIAL case: `k=1`
is self-conjugate/the fundamental representation, and identities that
hold there are not automatically guaranteed for general `k` (Peter-Weyl
levels used throughout this project go up to `k=5` and beyond). The
reviewer's own original proposal explicitly named `j=1` as the required
independent replication step before trusting the result. This round
does that, using C95's own validated method (fully symbolic
coefficient extraction, no hand index-tracking), not a new hand
derivation.

## Method

Build the `k=2` (`j=1`, spin-1) representation as the symmetric square
of the defining representation: for `v=(v0,v1)` transforming as
`v -> g @ v`, the normalized basis `e_p := v0^{k-p} v1^p /
sqrt(binomial(k,p))` (`p=0,1,2`) gives a UNITARY representation matrix
`D^{(2)}(g)` as an explicit polynomial in `g`'s own entries. Apply
C95's exact coefficient-extraction method to this `D^{(2)}(g)` instead
of `g` itself.

**Calibration check, not optional:** before trusting anything about the
`q`-side (`L`) result, first verify the `p`-side (`R`) result against
C85's own certified `l_{e_i}(2)`. If `R` does not cleanly match one of
the four candidates (`+l,-l,+lT,-lT`), the normalization of the
symmetric-square basis itself is wrong and nothing downstream is
trustworthy -- stop and fix the normalization before proceeding, per
this round's own `kill_criterion`.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P0 (calibration)** | `R_i(k=2)` matches `-l_{e_i}(2)^T` uniformly across `e1,e2,e3` (same pattern as C95's `k=1` result) | pending |
| **P1** | `L_i(k=2)` matches `+l_{e_i}(2)` directly (same pattern as C95) | pending |
| **P2** | both `[L1,L2]=2L3` and `[R1,R2]=2R3` hold exactly at `k=2` | pending |

## kill_criterion

If P0 fails, this round's own construction (not C95's result) is
broken -- stop, do not draw any conclusion about whether C95
generalizes. If P0 holds but P1 fails, C95's `L_i=+l_{e_i}` formula is
`k=1`-specific (a real, useful, narrowing finding -- would mean the
multiplication-operator build needs a `k`-dependent formula, not a
single fixed rule). If P0 and P1 both hold but P2 fails, the k=1
bracket-consistency resolution itself does not generalize, and the
multiplication-operator build must not proceed until that is
understood too.

## What this cannot show

- Does **not** test `k>=3` -- if `k=2` confirms the pattern, `k=3` would
  still be a reasonable further check before fully trusting a general
  formula, not automatically implied by one data point beyond `k=1`.
- Does **not** build the multiplication operator itself.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
