# C100 decision — full CG matrix assembled and verified; it is an injective embedding, not a mixing operator (for this single component)

**Verdict:** `FULL_CG_MATRIX_ASSEMBLED_AND_VERIFIED__QP_ONLY_R_STILL_OPEN`
**Status:** RESOLVED — first genuine multiplication-operator matrix built for task #59

---

## Summary

Built the full `(q,p)`-only multiplication-operator matrix `M_k`,
level `k -> k+1`, for `k=1,2,3`, using the standard `D^k_{q,p}(g) *
D^1_{1/2,1/2}(g)` product-of-matrix-elements identity and C99's own
verified magnetic-number labeling. This extends C90's own single
extremal-weight check (one `CG` value per level) to every `(q,p)` pair
-- the exact gap C90's own decision.md named as the next step.

## Predictions vs outcome

| # | Prediction | Outcome |
|---|---|---|
| P0 (structure) | `M_k` has dims `(k+2)^2 x (k+1)^2` | **PASSES** — `9x4`, `16x9`, `25x16` for `k=1,2,3`. |
| P1 (entries) | every nonzero entry matches an independently-recomputed value | **PASSES** — recomputed via the Wigner-3j relation (`sympy.physics.wigner`, a genuinely different code path from `sympy.physics.quantum.cg.CG`, not a second call to the same function), exact match every entry, every `k`. |
| P2 (cross-check vs C90) | `M_k[(k+1,k+1)-index, (k,k)-index] = 1` | **PASSES** — reproduces C90's own extremal-weight result exactly, now as one entry inside the fully-assembled matrix rather than a standalone check. |
| P3 (non-degeneracy) | matrix is not zero/trivially diagonal | **PASSES the coded criterion**, but see the precise characterization below — the actual structure is more specific than "non-degenerate" alone conveys. |

## Precise characterization of what was found (beyond the coded P3 check)

**`M_k` has EXACTLY `(k+1)^2` nonzero entries at every `k` tested —
exactly one nonzero entry per column (per level-`k` input state), no
more, no fewer.** Verified directly (`nonzero_count == dim_k**2` holds
exactly for `k=1,2,3`, not merely `>1` as the coded P3 check required).

**What this means physically:** for this SINGLE, FIXED `D^1_{1/2,1/2}`
component, the multiplication operator is an **injective embedding**
(a monomial map) of the level-`k` `(q,p)`-space into a `(k+1)^2`-dim
subspace of the level-`(k+1)` `(q,p)`-space — each input state maps to
exactly one output state, scaled by a single Clebsch-Gordan-product
coefficient, with no superposition across multiple `(Q,P)` for a fixed
input and no collision (two different inputs never map to the same
output). This is NOT a "many-to-many mixing" operator in the sense one
might picture for a coupling term — but it is a genuine,
**nontrivial, nonzero, level-bridging map**, which is qualitatively
different from and strictly stronger than the entire C79-C89
translation-generator family, which C90 proved is EXACTLY ZERO across
levels (no bridging at all, for any assembly of those generators).

**Why this is expected, not a red flag:** `D^k_{q,p}(g) *
D^1_{a,b}(g)` for a SINGLE FIXED `(a,b)` component is, by the
Clebsch-Gordan formula itself, always a single well-defined linear
combination landing in the `J=k/2+1/2` multiplet -- there is exactly
one target `(Q,P)` per `(q,p)` for fixed `(a,b)`, by construction, not
a surprise finding. Genuine "spreading"/superposition across multiple
level-`(k+1)` states would require summing over MULTIPLE `(a,b)`
components (e.g. a genuine wavefunction multiplied by a full matrix
`D^1(g)`, not one fixed matrix element) -- not attempted this round.

## Practical consequence for task #59

The `(q,p)`-only multiplication operator is now concretely built and
verified for `k=1,2,3` (extendable to any `k` using the same code,
reusing C99's labeling machinery). It is a genuine, nonzero,
level-bridging linear map -- the mathematical basis C90 verified is
now realized as an actual matrix, not just a scalar plausibility
check. Two things remain before this becomes the full physical
operator:

1. **Summing over `D^1` components** (if the actual physical
   construction needs the full matrix `D^1(g)`, not one fixed
   element) -- would combine multiple `(a,b)`-indexed `M_k` matrices,
   potentially producing genuine multi-state mixing. Not attempted
   this round; the single-component matrix built here is the base
   ingredient either way.
2. **`r`'s role** — still completely open, as in every prior round.
   `D^1_{ab}(g)` does not touch the Clifford index `r` that
   `build_dbar` uses; how (or whether) the two combine into a single
   physical operator on the full `(p,q,r)` basis remains unresolved.

## What this cannot show

- Does not address `r`'s role or build the full `(p,q,r)`-basis
  operator.
- Does not build the block-tridiagonal `D_PW` or run any
  truncation-convergence test.
- Does not verify the other three `D^1_{ab}` components, nor test
  whether summing over them produces genuine multi-state mixing.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260812-c100-full-cg-multiplication-operator-assembly/`
  — clean, 0 errors.
- Every nonzero matrix entry independently cross-checked via the
  Wigner-3j relation, a different sympy submodule from the one used to
  build the matrix in the first place.
- The precise `nonzero_count == (k+1)^2` structural fact was verified
  directly from `results_c100.json`, not asserted from the weaker
  coded P3 criterion alone.
