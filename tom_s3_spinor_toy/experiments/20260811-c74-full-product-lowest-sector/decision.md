# decision -- groundwork rigorous (sign match, S3 level, kernel construction); channel-transport step explicitly heuristic, not proof of distinguishability

## Verdict

`GROUNDWORK_VERIFIED__CHANNEL_TRANSPORT_EXPLORATORY_HEURISTIC__DISTINGUISHABILITY_DEFERRED_TO_C75`
-> **P1 CONFIRMED. P2 CONFIRMED. P3 CONFIRMED. P4: nonzero in all three
channels, but reported as [WEAK]/exploratory, not [VERIFIED] evidence for
three distinguishable generations.**
**Date:** 2026-08-11 · L0: descriptive · script:
`c74_product_lowest_sector.py`, results: `results_c74.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** Clifford sign match | `X^2=-I` both sides | **CONFIRMED, exact** -- all 6 of round59's `E_k` and all 3 of round67's `Z_i` satisfy `X^2=-I` exactly (sympy exact arithmetic). No mismatch for this specific pairing (unlike the `s6-harm-g0` construction OB10's registry documents, which has the OPPOSITE sign) -- this exact check had never been run in this codebase before. | [VERIFIED-sympy] |
| **P2** S3 n=0 level | `+-3/2`, mult 2 each | **CONFIRMED, exact** -- reproduced directly from round67's own `eigenvalue_family`/`calibrate_h_H` (h_H=3, t=1/2 Levi-Civita): eigenvalues `3/2` and `-3/2`, each with multiplicity `(0+1)(0+2)=2`, total 4-dim. Reused by citation, not re-derived. | [VERIFIED-sympy, cited] |
| **P3** kernel construction | explicit, normalized, in `ker(D+)` | **CONFIRMED** -- kernel vector norm `1.000000`, `D @ kernel_vec` residual `1.665e-16` (machine precision). Reuses C73's own `invariant_basis`/`build_numeric_dirac` unmodified. | [VERIFIED-numpy] |
| **P4** channel transport | nonzero in all 3 | **Nonzero in all three** -- `channel_v`: norm `1.0005`; `channel_s`: norm `0.8947`; `channel_c`: norm `0.8947` (the `s`/`c` values are numerically equal, a plausible consequence of the `s`/`c` channels' own structural symmetry, not independently investigated further here). All three intertwiners were found independently (`hom_dim=6` each, matching C70/C71's established results), each used ONCE (not composed in a cycle -- explicitly avoiding C71's tautology trap). | [WEAK] -- see caveat below |

## The P4 caveat, stated plainly

The kernel vector, as an SU(3)-invariant combination in `Sigma_odd (x)
Sigma_even`, is a genuinely ENTANGLED bipartite state -- it is NOT, in
general, a simple product `eta (x) xi` for a fixed `xi`. To transport
"the base spinor's own content" through `U_v`/`U_s`/`U_c` (which intertwine
the su(3) action on `Sigma` ALONE, not `Sigma (x) Sigma`), this round used
the MARGINAL over the second (twist) factor -- `kernel_mat.sum(axis=1)` --
as the object to transport. **This is one natural choice, not a
first-principles derivation.** No argument is offered here for why this
marginal is the physically correct extraction (as opposed to, e.g., a
different weighted combination, or projecting onto a specific twist-factor
eigenstate). The finding that all three channels give a nonzero result under
THIS SPECIFIC heuristic is reported honestly as [WEAK] evidence, consistent
with (but not proof of) a genuine three-channel structure -- a future round
would need to either derive the physically correct extraction from first
principles, or show the result is robust across multiple reasonable choices
of extraction (a control this round did not run).

## What this means, stated carefully

1. **The groundwork is solid.** Sign-convention compatibility (a genuine,
   previously-unchecked risk per OB10's own documented history) is
   confirmed, not assumed. The S3 and S6 pieces are each independently
   well-established (by citation and by C73/C73b respectively).
2. **The "assembly" step is exploratory, not rigorous**, and is reported as
   such rather than smoothed into a stronger claim. This is a deliberate,
   disclosed limitation, not an oversight -- the entangled nature of the
   kernel state makes "transport the base spinor's content" genuinely
   ambiguous without additional physical input this round does not supply.
3. **Distinguishability remains entirely open**, exactly as the round
   table's own division of labor anticipated -- three formally-distinct
   constructed objects (living in three different, previously-established
   channel spaces) are not automatically three PHYSICALLY distinguishable
   generations; that requires an observable that tells them apart, which is
   C75's explicit target, not attempted here.

## Kill Analysis

**Not killed:** any of C70-C73b's own established results -- all reused by
citation, unmodified.

**Not killed, but not strengthened either:** the "three sectors" picture --
P4's nonzero result is consistent with it but does not constitute evidence
strong enough to promote the picture from CONDITIONAL toward established,
given the heuristic nature of the extraction step.

**What survives, as a genuinely scoped next step:** (a) derive, or at least
motivate, the physically correct way to extract a transportable state from
an entangled SU(3)-invariant kernel vector (not attempted here); (b)
regardless of (a), proceed to C75's adversarial distinguishability test,
since that question is independent of exactly how the "channel content" is
constructed -- C75 can be scoped against the ALREADY-ESTABLISHED channel
structures (C61/C62/C70-C72) without needing this round's specific
transport heuristic to be resolved first.

## What this does NOT show

1. Does **not** establish physical distinguishability of the three channels
   -- explicitly deferred to C75.
2. Does **not** rigorously justify the marginal-projection heuristic used in
   P4 -- flagged, not smoothed over.
3. Does **not** re-test or contradict KT-8's NULL result, nor revive the
   already-refuted `t=0/1` multiplicity mechanism.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.

## Reproduction

```
python experiments/20260811-c74-full-product-lowest-sector/c74_product_lowest_sector.py
```
Reuses round59's `build_clifford`/`NOMIZU`/`block_global`, round67's
`clifford_generators`/`eigenvalue_family`/`calibrate_h_H`, C70's
`run_direct_solve`/`hom_basis`/`search_nonzero_intertwiner`, C71 step 1's
`su3_g102_on_channel_s`/`_c`, and C73's `invariant_basis`/
`build_numeric_dirac`/`su3_gens64`, all unmodified.
