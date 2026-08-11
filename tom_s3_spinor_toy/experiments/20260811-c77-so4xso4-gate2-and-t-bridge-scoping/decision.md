# decision -- Gate 2 CLOSED for round119's candidate too (NO, all 12/12); T-to-D bridge scoped, not built

## Verdict

`GATE2_TESTED_BOTH_KNOWN_CANDIDATES_NOW_NO__T_BRIDGE_REQUIRES_NEW_INFRASTRUCTURE_NOT_BUILT`
-> **P1 CONFIRMED (exact match to round125). P2 CONFIRMED. P3 CONFIRMED
(positive control clean). P4 CONFIRMED: all 12/12 generators show large,
clean violations, none close to the noise floor.**
**Date:** 2026-08-11 · L0: descriptive · script:
`c77_so4xso4_gate2_check.py`, results: `results_c77.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** basis compatibility | reproduces round125's `(12,10,19,3)` exactly | **CONFIRMED, exact match** -- `dim_A=12, dim_B=10, dim_union=19, dim_intersect=3`. Combining `triality_so4xso4_invariance.py`'s `SO(4)xSO(4)` basis with G102's `su(3)+centralizer` basis in this round reproduces round125's own published numbers exactly, confirming no new convention mismatch was introduced. | [VERIFIED-numpy, matches cited round125] |
| **P2** bridge sanity | `U_v` reproduces its own intertwining property | **CONFIRMED** -- `U_v` det `0.0692...` (identical to C70/C71/C74/C75's own `U_v`), intertwining residual `4.44e-16`. | [VERIFIED-numpy, cited] |
| **P3** positive control | `[D, Leibniz(M_k)]=0` for genuine su(3) generators | **CONFIRMED, exact** -- max commutator over all 8 su(3) generators: `2.776e-17`, identical to C75's own result (same `D`, same `M_k`, reused unmodified). | [VERIFIED-numpy] |
| **P4** Gate 2 test, `SO(4)xSO(4)` | large, clean violation for all 12, per G74A Lemma B's generality | **CONFIRMED for all 12/12** -- Frobenius norms range `2.83` to `28.25` against `\|D\|_F=8.00` (relative violation `35.4%` to `353%`), every single one far above P3's `2.8e-17` noise floor. No generator comes close to commuting. | [VERIFIED-numpy] |

## Per-generator detail (all 12, none near zero)

```
gen  0: rel. violation 3.5311   gen  6: rel. violation 0.3543
gen  1: rel. violation 1.3317   gen  7: rel. violation 0.3543
gen  2: rel. violation 1.3317   gen  8: rel. violation 0.3543
gen  3: rel. violation 1.8489   gen  9: rel. violation 0.3536
gen  4: rel. violation 1.8489   gen 10: rel. violation 0.3543
gen  5: rel. violation 0.3543   gen 11: rel. violation 0.3543
```

The pairing pattern (gens 1/2, 3/4, 5-8, 10/11 sharing near-identical
norms) is consistent with `so(4)+so(4)`'s own block structure (two
independent `su(2)+su(2)`-type factors) inducing paired violation
magnitudes -- noted, not investigated further this round (see Pearl below).

## What this means, stated carefully

1. **Gate 2 is now CLOSED (NO) for BOTH known Gate-1 candidates**, not just
   round124's. C75 showed round124's `su(3)+u(1)+u(1)` (10-dim) fails; this
   round shows round119's `SO(4)xSO(4)` (12-dim) also fails, comprehensively
   (all 12 generators, not just some). Since round125 already established
   these are genuinely different subalgebras (only a 3-dim abelian overlap,
   not one containing the other), this is real, independent confirming
   evidence for G74A's Lemma B's GENERALITY -- the physical `D` fails to
   respect channel-distinguishing extensions of `su(3)` regardless of which
   of the two known constructions is used. This is a stronger statement than
   C75 alone could support.
2. **The actual "T-to-D bridge" (using round119's own triality-automorphism
   matrix `T` to build a genuine channel-permuting operator) is NOT built
   here**, and `claim.md` explains precisely why it is not a same-round
   add-on:
   - `T` is a `12x12` matrix acting on the COORDINATES of the
     `so(4)+so(4)` Lie algebra itself (`build_triality_matrix_T()`), not a
     representation-space intertwiner like `U_v`/`U_s`/`U_c`.
   - Using it to relate round59's `Sigma` (identified with `8_v` via `U_v`)
     to `8_s` and `8_c` under this SAME `SO(4)xSO(4)` structure requires an
     `SO(4)xSO(4)`-equivariant identification of `Sigma` with `8_s` and
     `8_c` specifically -- a genuinely different embedding than C70/C71's
     su(3)-based `U_s`/`U_c` (which round125 shows share only 3 of 12
     dimensions with `SO(4)xSO(4)`). **No such identification exists
     anywhere in this codebase.**
   - `triality_so4xso4_invariance.py`'s OWN end-of-file diagnostic (lines
     289-311, cited not re-run) already found the vector-rep and
     spinor-rep `SO(4)xSO(4)` embeddings are "not yet shown to be the same
     embedding" -- a pre-existing, documented gap in round119's own
     construction, not something introduced by this round.
   - Given (1) above, `SO(4)xSO(4)` itself now ALSO fails Gate 2 -- meaning
     even if the missing infrastructure were built, `T` would be an
     automorphism of a symmetry that is NOT respected by the physical `D`
     in the first place, substantially reducing the motivation for
     building it. This is new information C76 did not have when it named
     `T` as the most promising lead.

## Kill Analysis

**Not killed:** any of C70-C76's own established results, round119's or
round124's own candidate constructions, round125's overlap finding, or
G74A's Lemma B -- all reused/confirmed by citation, and this round's
result is a second, independent computational confirmation of Lemma B's
generality, not a contradiction.

**Killed (for this specific lead):** the motivation, named in C76, for
building the `T`-based channel-permuting bridge as the natural next step.
`SO(4)xSO(4)` failing Gate 2 (like `su(3)+u(1)+u(1)` before it) means both
of this project's two known, independently-constructed Gate-1 candidates
are symmetries the physical `D` does not respect -- `T`, being an
automorphism specifically of the `SO(4)xSO(4)` structure, would relate
non-physical-symmetry generators to each other even if fully built. This
does not make `T` useless (the redundancy/permutation question is still
about whether SOME channel-permuting operator exists, not necessarily one
built from a physical symmetry), but it removes the specific reason C76
named for prioritizing this exact construction next.

**What survives, as a genuinely scoped next step:** the channel-redundancy/
permutation question remains exactly where C76 left it -- fully open, no
non-tautological candidate operator has been constructed by ANY route
tried across C71, C72, or this round. A future round would need either (a)
a genuinely new construction not derived from either known Gate-1
candidate, or (b) to revisit whether "commutes with `D`" is even the right
criterion for a channel-permuting operator to satisfy (a permutation could
in principle map `D`'s spectrum to itself without literally commuting with
every generator of a larger symmetry algebra) -- a conceptual question, not
attempted here.

## What this does NOT show

1. Does **not** build the `T`-based channel-permuting operator -- explicitly
   out of scope, per the reasons above.
2. Does **not** resolve the channel-redundancy/permutation question.
3. Does **not** re-verify round119's own vector-vs-spinor consistency
   diagnostic independently -- cited, not re-run.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.

## Pearl

The 12 per-generator violation magnitudes come in a clear paired pattern
(1/2, 3/4, 5-8, 10/11 near-identical; 0 and 9 distinct) consistent with
`so(4)+so(4)`'s own `su(2)+su(2)+su(2)+su(2)`-type block structure --
unexplained, not investigated. Falsifiable prediction: if this pairing
reflects a genuine `su(2)`-Casimir-type structure, the 12 violations should
organize into exactly 4 groups matching the 4 `su(2)` factors, with
within-group variation attributable only to numerical/basis-normalization
noise -- logged in `pearl_registry/INDEX.md`.

## Reproduction

```
python experiments/20260811-c77-so4xso4-gate2-and-t-bridge-scoping/c77_so4xso4_gate2_check.py
```
Reuses G102's `derivation_basis`/`stabilizer_basis`/`centralizer_dim`,
`triality_so4xso4_invariance.py`'s `build_so4xso4_basis`, C70's
`run_direct_solve`/`hom_basis`/`search_nonzero_intertwiner`, round59's
`build_clifford`/`leibniz`/`NOMIZU`, and C73's `build_numeric_dirac`, all
unmodified.
