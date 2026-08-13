# C102 -- does the k=1,2 D_PW's exactly-real spectrum replicate at k=2,3?

**Experiment id:** `20260812-c102-k2k3-real-spectrum-replication`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C101 (built the smallest 2-level `D_PW`, k=1,2,
under the explicitly-unverified "r-untouched" ansatz; found a genuine
spectral shift AND an exactly-real coupled spectrum -- the latter
unexplained, flagged in `pearl_registry/INDEX.md` with the named
next-cheapest-check being exactly this round).

---

## Why this is needed

C101's own decision.md flagged an open question: is the coupled
`D_PW`'s exactly-real spectrum (`max|Im|=0.0` exactly, not merely
small) a structural fact about this construction, or a coincidence
specific to the one `k=1,2` pair tested? The pearl registry entry
named the cheap next check explicitly: repeat the identical
construction at `k=2,3` using the already-general-`k` code
(`build_multiplication_matrix`, `dbar_full`, both parametrized by `k`
in C101's own script, not `k=1,2`-specific) and see if it stays real.

## Method

Identical to C101, with `k=2,3` in place of `k=1,2`: `D̄_2^full` and
`D̄_3^full` as diagonal blocks (dimensions `2·9=18` and `2·16=32`), the
off-diagonal coupling `M_2⊗I_r` (C100's certified `M_2`, extended
trivially to `r`), assembled into a `50x50` Hermitian-in-form `D_PW`.
Code reused verbatim from C101 (only the level arguments change), to
minimize the risk of a fresh implementation bug being mistaken for a
physics result.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P0 (reuse sanity)** | `D̄_2^full` reproduces `{-2:12, 4:6}` (unchanged from C101 -- this is the same level 2), `D̄_3^full` gives `{-3:20, 5:12}` (from raw `D̄_3` eigenvalues `-3` mult `k+2=5`, `5` mult `k=3`, each ×`dim_q=4`) | pending |
| **P1 (the open question)** | the coupled `D_PW` (k=2,3) ALSO has an exactly real spectrum (`max\|Im\|<1e-6`) | pending |
| **P2 (spectral shift, replication of C101's OTHER finding)** | coupling again produces a genuine, nonzero shift relative to the uncoupled union | pending |

## kill_criterion

If P0 fails, this round's own reuse has a bug -- stop, debug before
drawing any conclusion (per C101's own precedent, where P0 caught a
real eigensolver bug). If P0 holds but P1 FAILS (complex eigenvalues
appear), this is a genuine, informative finding: the real-spectrum
property found at `k=1,2` was a coincidence of that specific pair, NOT
a structural fact -- the `r`-untouched ansatz's viability as a
candidate physical operator would need serious re-examination (a
non-real spectrum is not physically acceptable for an operator meant
to represent an observable). If P0/P1 hold but P2 shows no shift, that
would itself be a surprising, informative divergence from C101's own
`k=1,2` result -- explored honestly either way. If P0/P1/P2 all hold,
this is a SECOND independent data point supporting the real-spectrum
property as structural (not proof, but meaningfully stronger than one
data point alone).

## What this cannot show

- Does **not** prove the real-spectrum property holds for ALL `k` even
  if it replicates here -- 2 consistent points, not a proof.
- Does **not** explain WHY the spectrum is real even if it replicates
  -- the underlying mechanism (possibly a similarity transform `S`
  making `D-bar` Hermitian-equivalent, per C101's own speculation)
  remains uninvestigated.
- Does **not** address `r`'s role beyond the same untouched ansatz, nor
  run a genuine 3+ level test.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
