# decision -- exhaustive so(8) commutant of D EQUALS su(3) exactly, dim 8, no larger symmetry exists

## Verdict

`EXHAUSTIVE_COMMUTANT_EQUALS_SU3_EXACTLY__DIM8__CLOSES_L3B_DYNAMICS_OPEN_ITEM`
-> **P1 CONFIRMED. P2 CONFIRMED. P3 CONFIRMED. P4 CONFIRMED EXACTLY:
`commutant_dim = 8`, matching the predicted `su(3)` exactly.**
**Date:** 2026-08-11 · L0: descriptive · script:
`c78_so8_commutant_exhaustive.py`, results: `results_c78.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** basis sanity | 28 generators, su(3) inside span | **CONFIRMED** -- `len(so8_basis())=28`, su(3) generators reconstruct from the so(8) span with residual `1.11e-16` (machine precision). | [VERIFIED-numpy, cited] |
| **P2** bridge sanity | `U_v` reproduces its own intertwining property | **CONFIRMED** -- identical to C70/C75/C77's own `U_v` (det `0.0692...`, residual `4.44e-16`). | [VERIFIED-numpy, cited] |
| **P3** positive control | su(3) generators lie in the computed commutant | **CONFIRMED, exact** -- `[D, Leibniz(su3_gen)]` max `2.776e-17` (matches every prior round); su(3) coefficients reconstruct from the FOUND null-space span with residual `7.667e-15` -- the method correctly recovers the known-good subspace before its negative-direction result is trusted. | [VERIFIED-numpy] |
| **P4** exhaustive commutant | `dim=8`, exactly su(3) | **CONFIRMED EXACTLY** -- SVD of the `4096x28` commutator map gives rank 20, commutant dimension `28-20=8`. Singular value spectrum: `28.26, {18.55,18.55,18.55}, {13.54,13.54,13.54}, {9.47,9.47,9.47}, {6.94,6.94,6.94}, {4.95,4.95,4.95}, 4.83, {2.64,2.64,2.64}, 0,0,0,0,0,0,0,0` -- 8 exact zeros, no near-zero stragglers (smallest nonzero singular value `2.64`, well-separated from `0`). | [VERIFIED-numpy] |

## What this means, stated carefully

1. **This is an exhaustive, theorem-level statement, not one more failed
   candidate.** C75 showed round124's specific 10-dim `su(3)+u(1)+u(1)`
   candidate fails. C77 showed round119's specific 12-dim `SO(4)+SO(4)`
   candidate fails. **This round shows there is NO OTHER candidate to try**
   -- the entire 28-dimensional `so(8)` has been searched at once via a
   single null-space computation, and `su(3)` (8-dim) is provably the
   ENTIRE commutant. Any future candidate subalgebra of `so(8)` anyone
   might propose is now known in advance to fail, without needing to test
   it individually -- it is contained in the 20-dim complement this round
   already proved does not commute with `D`.
2. **This closes `L3B_SPIN8_INTERFACE_SPEC.md` section 1.5's own
   "Dynamics" open item completely**, not partially. That document's own
   2026-07-15 investigation left open: "No argument shows the actual
   physical Dirac operator, once `G2` is broken this way, remains
   consistent with the index-theorem results... this needs independent
   verification, not assumption." This round supplies exactly that
   verification, exhaustively: breaking `G2` (moving to ANY larger
   subalgebra of `so(8)`) is NEVER consistent with the physical `D`'s own
   symmetry -- `su(3)` is not merely the largest CANDIDATE that happened to
   fail, it is the largest symmetry `D` has, full stop, within `so(8)`.
3. **The clean triplet structure in the singular-value spectrum** (values
   repeating in groups of exactly 3: `{18.55}x3, {13.54}x3, {9.47}x3,
   {6.94}x3, {4.95}x3, {2.64}x3`, plus two singleton values `28.26, 4.83`)
   is consistent with `so(8)/su(3)`'s own decomposition into `su(3)`
   representations of dimension 3 (the `20`-dim complement of `su(3)`
   inside `so(8)` decomposing into copies of `3`/`3-bar`-type irreps under
   `su(3)`'s own adjoint action) -- a structural sanity signature, not
   noise, though not separately verified representation-theoretically this
   round.

## Kill Analysis

**Not killed:** any of C70-C77's own established results -- reused
unmodified, and this round's exhaustive result is fully consistent with
(and generalizes) both C75's and C77's individual negative findings.

**Killed, exhaustively:** the entire class of candidates "some subalgebra
of `so(8)` commutes with the physical `D`, beyond `su(3)`." This closes
the search space this project has been probing piecemeal since C75 --
there is no remaining candidate within `so(8)` left to try.

**What survives, as the genuinely scoped remaining door:** exactly what
`L3B_SPIN8_INTERFACE_SPEC.md`'s own final kill criterion already named --
a channel-distinguishing/permuting structure that is NOT an `so(8)`
Lie-algebra symmetry of the CURRENT product-manifold `D` at all. This
requires either (a) a structurally different, non-product `D` (mixing the
`S3` frame index with the `S6` triality index directly, not as a tensor
product) -- explicitly requiring content this project does not have
(Part 5, unpublished, not solicited); or (b) abandoning the "commutes with
`D`" criterion for a channel-permuting operator entirely, in favor of some
weaker/different notion of "the three channels are physically
distinguishable" not yet formulated in this project.

## What this does NOT show

1. Does **not** address the L3B document's own final kill criterion (a
   non-product, `G2`-breaking `D`) -- explicitly out of reach, restated
   from claim.md.
2. Does **not** resolve the channel-redundancy/permutation question by
   itself -- closes one entire class of candidate mechanisms (any so(8)
   Lie-algebra symmetry), not the question itself.
3. Does **not** independently re-verify `L3B_SPIN8_INTERFACE_SPEC.md`'s
   own Hopf/Liouville PDE argument -- a different, complementary
   computation (algebraic, not analytic).
4. Does **not** change `N_gen=3`'s CONDITIONAL status.

## Reproduction

```
python experiments/20260811-c78-exhaustive-so8-commutant-of-physical-D/c78_so8_commutant_exhaustive.py
```
Reuses G102's `so8_basis`, C70's `run_direct_solve`/`hom_basis`/
`search_nonzero_intertwiner`, round59's `build_clifford`/`leibniz`/
`NOMIZU`, and C73's `build_numeric_dirac`, all unmodified.
