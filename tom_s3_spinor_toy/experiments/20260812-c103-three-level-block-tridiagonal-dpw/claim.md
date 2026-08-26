# C103 -- the first genuinely block-tridiagonal D_PW (k=1,2,3): does truncation converge?

**Experiment id:** `20260812-c103-three-level-block-tridiagonal-dpw`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C90 (named the actual endpoint of this whole arc: "build the
resulting genuinely block-tridiagonal `D_PW`, and THEN run the
truncation-convergence test"). C101 (smallest possible 2-level `D_PW`,
k=1,2, under the explicitly-unverified "r-untouched" ansatz -- found a
real spectral shift AND an exactly-real coupled spectrum). C102
(replicated both findings at k=2,3, independently).

---

## Why this is needed

C101/C102 each tested exactly ONE off-diagonal coupling block (a
2-level system) -- neither can show "truncation convergence" by
itself, since that requires comparing what happens to the
LOW-LYING spectrum as MORE levels are added, not just whether one
coupling does something. This round builds the first genuinely
3-level, block-TRIDIAGONAL `D_PW` (k=1,2,3, with BOTH `M_1⊗I_r` and
`M_2⊗I_r` as simultaneous off-diagonal couplings) -- the literal
construction C90's own decision.md named as the arc's final step.

**Still under the same explicitly-unverified "r-untouched" ansatz** as
C101/C102 (see those files' own Counterfactual Frame) -- this round
does not resolve that open question, only extends the construction one
more level under the same working hypothesis.

## Method

Reuses C101/C102's own `dbar_full(k)` and `build_multiplication_matrix`
functions verbatim (no new construction logic):

```
D_PW_3level = [[ D1_full,  B1^H,     0      ],
               [ B1,       D2_full,  B2^H   ],
               [ 0,        B2,       D3_full]]
```

`D1_full` (dim 8), `D2_full` (dim 18), `D3_full` (dim 32) -- C85's
certified `D-bar` at each level, tensored with `I_q`. `B1 = M_1⊗I_r`
(dim 18x8), `B2 = M_2⊗I_r` (dim 32x18) -- C100's certified
multiplication matrices. Total dimension 58. Note the (1,3) and (3,1)
blocks are explicitly ZERO -- `M_k` only connects ADJACENT levels
(k to k+1), so there is no direct 1-to-3 coupling; any 1↔3 correlation
in the full spectrum is purely an INDIRECT, level-2-mediated effect,
exactly matching the physical picture of a genuine KK-tower coupling.

Following C101's own hardening (boyko-project-radar Chain 1): the
`max|Im|` invariant is hard-asserted AFTER results are written to disk,
not before.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P0 (reuse sanity)** | `D1_full`, `D2_full`, `D3_full` individually reproduce C85's own certified eigenvalues exactly (`{-1:6,3:2}`, `{-2:12,4:6}`, `{-3:20,5:12}`) | pending |
| **P1 (real spectrum, genuinely new territory)** | the 3-level coupled `D_PW`'s spectrum is ALSO exactly real -- NOT guaranteed by C101/C102's own pairwise results, since this round introduces an indirect 1↔3 correlation neither prior round tested | pending |
| **P2 (truncation convergence -- the actual new question)** | the LOWEST-magnitude eigenvalues (closest to 0) of the 3-level system are CLOSE to (within some reasonable tolerance of) the 2-level (k=1,2) system's own lowest eigenvalues -- i.e. adding level 3 does not drastically reshuffle the physically most relevant part of the spectrum | pending |

## kill_criterion

If P0 fails, this round's own reuse has a bug -- stop, debug before
drawing any conclusion. If P0 holds but P1 fails (complex eigenvalues
appear), this is a genuinely important, informative finding: the
exactly-real-spectrum property found at 2 independent 2-level pairs
does NOT survive a genuine 3-level, indirectly-coupled system -- would
strongly suggest the property is a pairwise artifact of this specific
`B, B^H` off-diagonal construction, not a deep structural fact, and
would redirect the open "why is it real" question (pearl_registry
2026-08-12 entry) toward a narrower, correctly-scoped claim ("real for
adjacent-pair couplings, not in general"). If P0/P1 hold but P2 shows
the lowest eigenvalues shift SUBSTANTIALLY from the 2-level result,
that is itself the actual finding this round exists to test: truncation
does NOT converge at this order, and any physical claim built on a
finite-level truncation of this construction would need many more
levels before being trustworthy -- an important, negative-leaning but
genuinely informative result, not a failure of the round.

## What this cannot show

- Does not resolve the "why is the spectrum real" mechanism (candidate
  similarity transform `S`) even if P1 holds again -- three consistent
  points strengthens the empirical pattern further but is still not a
  proof or an identified mechanism.
- Does not test whether summing over multiple `D^1_{a,b}` components
  changes anything -- still the single `a=b=1/2` component throughout.
- Does not resolve `r`'s role -- same explicitly-flagged, unverified
  "r-untouched" ansatz as C101/C102.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.
