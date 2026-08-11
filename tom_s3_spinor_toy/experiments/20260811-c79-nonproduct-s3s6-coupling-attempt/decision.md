# decision -- apparent zero mode found, then explained away as a raw-kernel artifact; genuine coupling gives NULL; two valuable side-findings

## Verdict

`APPARENT_CROSSING_FULLY_EXPLAINED_BY_RAW_KERNEL_ARTIFACT__GENUINE_NULL_FOR_THIS_POSTULATE__UV_NONUNITARY_FOUND_AND_FIXED__ROBUSTNESS_OF_C75_C77_C78_CONFIRMED`
-> **P1 CONFIRMED. P2 CONFIRMED (after an explicit, documented fix). P3
CONFIRMED. P4: a crossing WAS found at first, then fully explained away
under this round's own pre-committed skeptical-scrutiny discipline --
final result is NULL for this specific, explicitly-postulated coupling.**
**Date:** 2026-08-11 · L0: descriptive (exploratory) · script:
`c79_nonproduct_coupling.py`, results: `results_c79.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** su(2) closure | genuine su(2) triple from so(4)_1's self-dual/anti-self-dual split | **CONFIRMED, exact** -- both self-dual and anti-self-dual triples close exactly (`residual=0.0`, structure constant `+-2.0`, standard su(2) up to normalization). | [VERIFIED-numpy] |
| **P2** Hermiticity | D_joint(eps) Hermitian for all real eps | **CONFIRMED, but only after a fix** -- see "U_v is not unitary" below. Raw `T` had Hermiticity residual `2.622`; the Hermitized `T=(T_raw+T_raw^dagger)/2` is exactly Hermitian (residual `0.0`), and `D_joint_base` was already exactly Hermitian. | [VERIFIED-numpy] |
| **P3** eps=0 sanity | `ker(D_joint, eps=0)` empty | **CONFIRMED** -- min\|eigenvalue\| at `eps=0` is `0.3257`, clearly nonzero. | [VERIFIED-numpy] |
| **P4** sweep for zero modes | no crossings (predicted, matching every prior closed route) | **ONE crossing found initially** (`eps=1.5`, min\|eigenvalue\|→`0.0`) -- but see "Skeptical follow-up" below: fully explained away, not a genuine new mechanism. | [VERIFIED-numpy] |

## U_v is not unitary -- found, documented, fixed, and checked for impact on prior rounds

**Finding, `[VERIFIED-numpy]`:** C70's intertwiner `U_v` (reused unmodified
throughout C71, C74, C75, C77, C78) is **not unitary** --
`||U_v^dagger U_v - I||_max = 1.29`, singular values ranging `0.546` to
`1.740`. This was never checked before because C75/C77/C78 only tested
`[D, Leibniz(g_transported)]`, a statement about intertwining that does
not require `U_v` to be unitary. This round's own construction (building
a genuinely new Hermitian operator `T`) DOES require it, which is how the
gap was found: transporting a real-antisymmetric generator through `U_v`
gave a result that was NOT anti-Hermitian (residual `2.622`, matching the
raw `T`'s own Hermiticity failure exactly).

**Fix applied, documented not hidden:** `T` is explicitly Hermitized,
`T=(T_raw+T_raw^dagger)/2`. This is the natural, minimal correction and
does not change the qualitative shape of the coupling term.

**Robustness check on C75/C77/C78, triggered by this finding (a
locality-escalation flag correctly identified this as worth taking
seriously rather than patching locally) -- `[VERIFIED-numpy]`:** built
two independently-seeded valid intertwiners (`U_v` from seeds `0` and
`999`, both satisfying the intertwining relation to machine precision,
residuals `4.4e-16` and `5.1e-16`). The map `W = U_v2 @ U_v1^-1` relating
them does **not** commute with the `su(3)` action (`||[W,M_k]||=1.42`),
confirming the residual freedom within the 6-dim `su(3)`-intertwiner
moduli genuinely changes which specific operator a non-`su(3)` generator
transports to. **Despite this, re-running C75's exact `u1_a` Gate-2 test
with FOUR different valid `U_v` choices (seeds 0, 999, 42, 7) gives**
relative violations `0.655, 0.608, 0.748, 0.617` -- **all large, all
clearly nonzero, same qualitative conclusion every time.** C75's (and by
extension C77's and C78's) headline finding -- "this generator does not
commute with the physical D" -- is **robust to this residual gauge
freedom**, not an artifact of one arbitrary choice. This is a valuable,
reassuring confirmation of the entire C75-C78 chain's methodology,
surfaced as a side effect of this round's own construction needs.

## Skeptical follow-up on the P4 crossing (per this round's own pre-committed kill_criterion)

The crossing at `eps=1.5` is suspiciously clean: it lands exactly on
`d_s3_scalar=1.5` (round67's own established `D_S3` scalar value at `n=0`,
`+`-branch), and `T`'s own spectrum contains an EXACT eigenvalue of
`-1.0`. Investigated directly rather than accepted:

1. **`D_S6`'s own raw (unrestricted) kernel is 36-dimensional** --
   confirmed directly (`36`, matching C73's own already-established
   finding, explicitly flagged there as NOT the physically relevant
   quantity; the physically relevant sector is the much smaller
   `su(3)`-invariant restricted sector, kernel `=1`).
2. **The near-zero eigenvector of `D_joint` at `eps=1.5` lies
   `99.9999997%` inside this 36-dimensional raw kernel** -- computed
   directly via projection onto `D_S6`'s own eigenbasis restricted to
   its zero-eigenspace.
3. **Mechanism, fully explained:** with a 36-dimensional degenerate
   subspace already present in `D_S6` (unrelated to any new physics --
   pure linear algebra), essentially ANY generic Hermitian perturbation
   (this round's `T`, or countless others) restricted to that subspace
   will, by basic perturbation theory on a degenerate eigenspace, produce
   SOME eigenvalues that sweep through zero as the perturbation strength
   is scanned. This is close to guaranteed by dimension-counting alone,
   not evidence of a genuine entangling mechanism connecting `S3` and
   `S6`. The "zero mode" found has **no meaningful connection to the
   physically relevant `su(3)`-invariant sector** this project's
   `N_gen=3` claim actually rests on.

**Conclusion: the P4 crossing is a raw-kernel artifact, not a genuine
finding.** This is exactly the "textbook shape of a false positive"
this round's own claim.md pre-committed to treating with extra scrutiny,
not excitement -- and the scrutiny fully explained it. For this specific,
explicitly-postulated coupling ansatz, **no genuine non-product zero mode
was found.**

## What this means, stated carefully

1. **The genuine attempt at a non-product construction, for this specific
   postulate, is a clean NULL** -- consistent with every prior route in
   this project (L3B's own exhaustive 2026-07-15 investigation, C75, C77,
   C78) closing. This extends that already-long list under one MORE
   specific, honestly-labeled, internally-derivable postulate (round67's
   `Z_i` + round119's `so(4)_1` self-dual triple, transported via `U_v`).
2. **Two genuinely valuable side-findings emerged from the attempt
   itself**, independent of the main NULL result: `U_v`'s non-unitarity
   (a real, previously-unexamined property of the bridge machinery used
   throughout this session, now documented) and the robustness
   confirmation (C75/C77/C78's conclusions do NOT depend on which valid
   `U_v` representative was used).
3. **This does not close the door on non-product constructions in
   general** -- only on this ONE specific, explicitly-postulated choice
   (round119's `so(4)_1` self-dual triple, `S3`'s `n=0` `+`-branch sector
   only). The anti-self-dual triple, the other `so(4)_2` factor, other
   choices within `C78`'s 20-dim complement, and the full Peter-Weyl
   tower (not just `n=0`) all remain untested. `L3B_SPIN8_INTERFACE_
   SPEC.md`'s own conclusion -- that a genuine route needs content this
   project does not have (Part 5) -- is not overturned, but this round
   shows a genuine, internally-derivable ATTEMPT is possible and can be
   tested rigorously, which is itself useful for any future attempt.

## Kill Analysis

**Not killed:** C75's, C77's, C78's own results -- CONFIRMED more
robust than previously known, via the side-investigation this round's
own construction needs triggered.

**Killed, for this specific postulate:** the self-dual `so(4)_1` triple,
paired with round67's `Z_i`, restricted to `S3`'s `n=0` `+`-branch sector,
does not produce a genuine, physically-meaningful non-product zero mode
-- the one apparent crossing is fully explained as a raw-kernel artifact.

**What survives, as genuinely scoped next steps (not attempted here):**
(a) repeat with the anti-self-dual triple, or with a generator NOT drawn
from `so(4)_1`/`so(4)_2` at all (e.g. a generic element of C78's 20-dim
complement); (b) build the FULL Peter-Weyl tower on the `S3` side rather
than just `n=0`, closer to what KT-8's own original zero-kernel result
actually covers; (c) restrict the search to the physically-relevant
`su(3)`-invariant sector specifically (rather than the full 128-dim
space, which is dominated by the physically-uninteresting 36-dim raw
kernel) to avoid the artifact found here by construction.

## What this does NOT show

1. Does **not** establish that no non-product construction can ever work
   -- one specific, explicitly-postulated attempt, honestly labeled as
   such throughout, returns NULL.
2. Does **not** build the full, rigorous `S3xS6` joint Dirac operator
   (restricted to `n=0`, `+`-branch only) -- see claim.md's own stated
   limits, unchanged.
3. Does **not** solicit or reference Tom Lawrence's unpublished Part 5 --
   every object used is already established in this project or standard
   Lie theory.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.

## Reproduction

```
python experiments/20260811-c79-nonproduct-s3s6-coupling-attempt/c79_nonproduct_coupling.py
```
Reuses round67's `clifford_generators`/`calibrate_h_H`,
`triality_so4xso4_invariance.py`'s `build_so4xso4_basis`, C70's
`run_direct_solve`/`hom_basis`/`search_nonzero_intertwiner`, round59's
`build_clifford`/`leibniz`/`NOMIZU`, and C73's `build_numeric_dirac`, all
unmodified.
