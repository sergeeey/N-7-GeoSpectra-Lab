# C101 -- smallest possible 2-level D_PW (k=1,2): does the multiplication-operator coupling produce a real spectral shift?

**Experiment id:** `20260812-c101-smallest-two-level-dpw-spectral-shift-test`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C85 (certified `D-bar` = -Σᵢ l_{e_i}(k) ⊗ rmult_i on
`(p,r)`, eigenvalues `-k` mult `k+2`, `k+2` mult `k`, per Meier eq
6.4). C90 (verified the CG mathematical basis for a multiplication
operator, scoped the final endpoint: "build the resulting genuinely
block-tridiagonal `D_PW`, and THEN run the truncation-convergence
test"). C100 (assembled the full `(q,p)`-only multiplication matrix
`M_k`, verified injective-embedding structure).

---

## Counterfactual Frame (research claim, per this project's own
## discipline for exploratory hypothesis rounds)

This round tests a SPECIFIC, EXPLICITLY UNVERIFIED modeling choice for
how `r` enters the multiplication operator: **the simplest possible
hypothesis, `r` left completely untouched (`M_k ⊗ I_r`)** -- i.e., the
multiplication-by-`D^1_{1/2,1/2}(g)` operator acts only on `(q,p)` (via
C100's own certified `M_k`) and trivially (identity) on the Clifford
index `r`. This is NOT a derived or certified fact -- `D^1_{ab}(g)` is
scalar-valued and there is no existing derivation in this project
connecting it to `r` at all. **The world in which this round's result
is informative is the world where `r`-untouched is (at least
approximately) the right ansatz** -- if the true physical construction
instead requires `D^1(g)` to act ON `r` (identifying its `(a,b)`
indices with `r`'s own 2-dim space, a genuinely different and more
elaborate hypothesis not built here), this round's specific numbers
would not directly carry over, though the STRUCTURAL question it
answers (can a well-formed Hermitian 2-level `D_PW` even be assembled
this way, and does coupling shift anything) would still be a useful
methodological result either way.

## Why this is needed

C90's own decision.md named the actual endpoint of this entire
multi-round arc: build the block-tridiagonal `D_PW` and run the
truncation-convergence/spectral-flow test the reviewer originally
proposed. This round builds the SMALLEST possible instance of that --
a 2-level (`k=1,2`) `D_PW` -- as the cheapest test of whether the
multiplication-operator construction, once assembled, actually DOES
anything to the spectrum (as opposed to being spectrally inert, e.g.
if its image happens to avoid all eigenspace overlap with the diagonal
blocks).

## Method

1. Build `D̄_1` (dim `2·2=4` on `(p,r)`) and `D̄_2` (dim `2·3=6` on
   `(p,r)`) via C85's own certified `build_dbar`.
2. Tensor each with the identity on its own `q`-space to get the FULL
   level operators on `(q,p,r)`: `D̄_1^full = I_{q=2} ⊗ D̄_1` (dim 8),
   `D̄_2^full = I_{q=3} ⊗ D̄_2` (dim 18).
3. Build the off-diagonal coupling `B := M_1 ⊗ I_r` (dim `18x8`),
   reusing C100's own certified `M_1` matrix directly (not
   re-derived).
4. Assemble the Hermitian 2-level operator
   `D_PW = [[D̄_1^full, B†], [B, D̄_2^full]]` (dim 26).
5. Diagonalize `D_PW` numerically and compare its eigenvalue spectrum
   to the UNCOUPLED union (`B=0`): the plain union of `D̄_1^full`'s and
   `D̄_2^full`'s own separately-known eigenvalues
   (`{-1: 6, 3: 2, -2: 12, 4: 6}`, total dim 26).

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P0 (reuse sanity)** | `D̄_1^full`, `D̄_2^full` individually reproduce C85's own certified eigenvalues exactly (`-1:6,3:2` and `-2:12,4:6` respectively) before combining anything | pending |
| **P1 (construction, not a real test -- see note)** | `D_PW` is exactly Hermitian by construction (`[[A,B†],[B,C]]` with `A,C` Hermitian is ALWAYS Hermitian regardless of `B` -- included only as an implementation sanity-check, not treated as informative about the physics) | pending |
| **P2 (the actual test)** | `D_PW`'s eigenvalues DIFFER from the uncoupled union -- i.e. the coupling produces genuine level repulsion/shift, not spectral inertness | pending |

## kill_criterion

If P0 fails, this round's own reuse of C85/C100's certified components
has a bug -- stop, debug before drawing any conclusion. P1 needs no
kill_criterion (it is guaranteed by construction, see note above -- a
failure would indicate an implementation bug, not a physics finding,
exactly as C99's own self-corrected P0 taught). If P0/P1 hold but P2
shows NO shift (eigenvalues exactly match the uncoupled union), this
is a real, informative null result: the `r`-untouched multiplication-
operator construction, AT THIS SMALLEST POSSIBLE SCALE, is spectrally
inert -- a genuine finding that would redirect attention toward the
`r`-touching hypothesis (identifying `D^1`'s `(a,b)` indices with `r`)
as the more promising direction, rather than a failure of this round.
If P2 shows a shift, that is evidence the general construction
APPROACH is not degenerate, though NOT yet evidence that the specific
`r`-untouched ansatz is the physically correct one (see Counterfactual
Frame above).

## What this cannot show

- Does **not** establish that `r`-untouched is the physically correct
  hypothesis -- it is one candidate, explicitly flagged as such.
- Does **not** run a genuine multi-level truncation-convergence test
  (only 2 levels, the smallest possible instance) -- a real
  convergence claim would need k=1,2,3,4+ compared against each other.
- Does **not** sum over the other three `D^1_{a,b}` components.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
