# Round124 — Claim

**Gauge/Hilbert/Triality closure program, follow-up (user-requested new
candidate via SU(3)-representation coordinates).** Tests a new,
previously-unexamined distinguishing-structure candidate for L3b (channel
independence), built entirely from `SU(3)` (the isotropy group of
`S⁶=G₂/SU(3)`) and its own centralizer — not from the octonion `H⊕Hℓ`
split used by round119's `SO(4)×SO(4)` candidate.

## Prior Result Gate

Gate G102 (`experiments/20260705-g102-spin8-fiber-obstruction/`) already
established, tool-verified:
- `su(3)` alone (the isotropy subalgebra) gives `Hom_su(3)(α,β)=6` for
  **all** pairs `α,β∈{v,s,c}`, including off-diagonal — i.e. the three
  channels restrict to **isomorphic** `su(3)`-modules. `su(3)` alone
  cannot distinguish them (already closed, not reopened here).
- The centralizer `c_so(8)(su(3))` is exactly 2-dimensional and abelian
  (S4). G102's own text notes these 2 generators are inner elements of
  `so(8)` and "cannot permute triality labels" as an OUTER automorphism —
  but G102 never checked whether `su(3)` **combined with** this
  centralizer (a rank-4 algebra `su(3)⊕u(1)⊕u(1)`, since `su(3)` has
  rank 2) gives a **non-isomorphic** restriction via different `u(1)×u(1)`
  charges on the `su(3)`-isotypic pieces, even though `su(3)` alone sees
  them as the same module. That specific question is genuinely new.

## L0 gate (EstimandOps)

**Question type: Descriptive.** Does `su(3)⊕u(1)⊕u(1)` (su(3) plus its
own centralizer in `so(8)`) distinguish `8_v, 8_s, 8_c` as representations
— i.e. is `Hom_{su(3)⊕u(1)⊕u(1)}(α,β) < 6` for some off-diagonal pair,
ideally `=0` (Schur: non-isomorphic)?

## Falsifiable claim

Using G102's own verified machinery (octonion table, `su(3)` basis,
centralizer basis, `Cl(0,8)`-built `v/s/c` representations, `hom_dim`) —
reused, not re-derived — compute `Hom` for all three pairs
(`v-s`, `v-c`, `s-c`) under the **combined** 10-generator set
(`su(3)`'s 8 generators + the centralizer's 2 generators), not `su(3)`
alone.

## Pre-registered kill criteria

| Outcome | Verdict |
|---|---|
| `Hom` under the combined 10 generators equals `6` for all off-diagonal pairs (unchanged from `su(3)` alone) | **NULL** — the centralizer's 2 extra generators act as pure scalars that don't further constrain the intertwiner space; this candidate closes, no new distinguishing structure |
| `Hom` shrinks but stays `>0` for some pair | **PARTIAL** — some new constraint found, but not full non-isomorphism; report honestly, do not round up to "distinguishes" |
| `Hom=0` for at least one off-diagonal pair | **CANDIDATE FOUND** — genuine non-isomorphism under this rank-4 algebra; proceed to check (a) does `su(3)⊕u(1)⊕u(1)` actually escape confinement to `SO(7)` (does it fix no vector in `8_v`, matching the rank-4-escapes-`SO(7)` argument that worked for `SO(4)×SO(4)`), (b) anti-circularity screen (is this derived from already-fixed structure, not postulated) |
| Any numerical instability / near-zero singular values not cleanly separated from true zero | **INCONCLUSIVE** — do not force a verdict, report the raw singular-value gap |

## What this does NOT mean (pre-registered)

1. Does NOT reopen or contradict G102's own `Hom_su(3)=6` finding — that
   result concerns `su(3)` ALONE, unchanged here.
2. Does NOT itself close L3b even if a candidate is found — matching
   round119's own `SO(4)×SO(4)` precedent, physical realization
   (identification with actual gauge fields, dynamical consistency once
   `G₂` breaks) would remain a separate, likely-still-open question.
3. Does NOT affect `N_gen=3`'s `CONDITIONAL` status, `lambda=FREE_
   COUPLING_PARAMETER`, or `safe_for_runtime=False`.
4. Does NOT modify G102's own script or results — reuses it by import,
   per this project's own established reuse pattern (G102 itself reused
   G68 the same way).
