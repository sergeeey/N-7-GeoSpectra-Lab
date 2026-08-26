# C105 -- searching for the similarity transform S explaining the exactly-real D_PW spectrum

**Experiment id:** `20260812-c105-similarity-transform-s-search`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C101/C102/C103 (found the coupled `D_PW` spectrum is
exactly real across three qualitatively different constructions, with
no explanation -- the pearl_registry's own open question, named as the
third research-audit item still unaddressed after C103/C104).

---

## Why this is needed, and what was already explored before writing this claim.md

The candidate mechanism named in C101's own pearl-registry entry:
`D-bar` (and by extension `D_PW`) might be similar to a Hermitian
matrix via a fixed similarity transform `S`, which `M_k`'s own
construction might respect consistently across levels. Before writing
this claim.md, a preliminary scratch exploration (disclosed here per
this project's own convention -- see C95's precedent) checked the two
most natural candidate ingredients directly:

1. Is `l_{e_i}(k)` (the p-space generator) anti-Hermitian? **Only at
   `k=1`** -- confirms C96's own earlier finding that C85's raw `|p⟩`
   basis is non-orthonormal for `k>=2`.
2. Is `rmult_i` (the r-space generator) anti-Hermitian? **Yes, already,
   for all three units** -- no fix needed on the `r` side at all.
3. Does the binomial-normalization transform `S_p(k) :=
   diag(1/sqrt(C(k,p)))` simultaneously anti-Hermitianize `l_{e1}(k)`,
   `l_{e2}(k)`, `l_{e3}(k)`? **Yes, confirmed directly for `k=2,3,4`.**
   This is the SAME normalization derived (then discarded for a
   different, calibration-specific reason) in C96's own construction
   of `build_d2_matrix`.

Given `S_p(k)⊗I_r` correctly Hermitianizes each diagonal block
`D̄_k` individually, the natural next question -- whether
`S_total := blockdiag(S_p(1)⊗I_r, S_p(2)⊗I_r, ...)` Hermitianizes the
FULL coupled `D_PW` (including the off-diagonal `M_k` blocks) -- is
this round's actual content.

## Method

For the 2-level (`k=1,2`) system (C101's own construction): build
`S_1 := I_{q}⊗S_p(1)⊗I_r`, `S_2 := c·I_q⊗S_p(2)⊗I_r` with `c` an
unknown positive scalar (the one remaining degree of freedom per
level, since Schur's lemma forces `S_p(k)` unique up to an overall
scalar for an irreducible `su(2)` representation -- `l_{e_i}(k)` is
exactly the `(k+1)`-dim irrep, standard and not re-derived here).
Directly compute the cross-level compatibility condition `P_2 M_1 =
c^2 \cdot (\text{scaled }P_2) M_1 \overset{?}{=} M_1 P_1` (where
`P_k := S_p(k)^\dagger S_p(k)`, extended trivially over `q`) as an
EXPLICIT symbolic matrix equation, and check whether any single value
of `c` solves it.

## Predictions, recorded before running (i.e. before this formal, from-scratch symbolic re-derivation -- the scratch exploration above used the same numbers by hand, this round re-derives them cleanly in one script for the record)

| # | Prediction | Outcome |
|---|---|---|
| **P0 (reuse sanity)** | `S_p(k)⊗I_r` individually Hermitianizes `D̄_k` for `k=1,2,3` (reproducing the scratch-exploration finding formally) | pending |
| **P1 (the actual question)** | a single scalar `c` exists solving the cross-level compatibility condition exactly | pending |
| **P2 (if P1 fails)** | do the per-entry constraints on `c` disagree with each other (genuinely inconsistent), or does the system merely leave `c` underdetermined (consistent but not pinned down)? | pending |

## kill_criterion

If P0 fails, this round's own reproduction of the scratch exploration
has a bug -- stop, debug before drawing any conclusion. If P0 holds
and P1 also holds, this closes the pearl_registry's own open question
with an explicit, provable mechanism -- a major positive result. If P0
holds but P1 fails with GENUINELY INCONSISTENT per-entry constraints
(not just underdetermined), this is a real, informative negative
result: the cleanest, most natural candidate mechanism (a block-
diagonal, level-local, `r`-untouched similarity transform) is RULED
OUT as a full explanation of the real-spectrum property. The property
itself remains true (confirmed three times over, C101-C103) -- only
this SPECIFIC candidate explanation for it is killed. Per the Minimal
Relaxation Rule, the next candidate (if pursued) would need to relax
exactly one assumption of this one -- e.g. a non-block-diagonal `S`
that genuinely mixes levels, or abandoning the "similar to Hermitian"
framing entirely in favor of a different structural explanation
(e.g. pseudo-Hermiticity with an indefinite metric).

## What this cannot show

- Does not identify the true mechanism even if this specific
  candidate is ruled out -- narrows the search, does not complete it.
- Does not test whether a NON-block-diagonal `S` (mixing levels)
  could work -- a substantially larger search, not attempted here.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.
