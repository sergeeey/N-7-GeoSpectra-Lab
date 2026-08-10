# Step 4 red-team — can the three triality channels reduce to one physical degree of freedom?

**Experiment id:** `20260810-step4-channel-redundancy-redteam`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C61, C62 (this pivot's prior rounds); G102 (`Hom_so8` machinery,
`spin_rep_blocks`); pearl_registry entry dated 2026-07-15 ("attempt to physically
realize U on zero modes")

---

## Continuing in order (per user instruction "го вс по очереди")

The user's step 4: "can a change of basis reduce the three triality channels to one
physical degree of freedom with a triple description — i.e., is '3' redundant, provably
or not?" This question became sharper after C61/C62: those rounds confirmed the three
channels have *identical* `su(3)` content and are *literally triality-fixed* under
`su(3)` — raising a real worry that N_gen=3 might be triple-counting one physical mode
rather than counting three independent ones.

## Pre-work check (Adaptive Iteration Branch Rule) — this is NOT untouched

A targeted search found this exact worry already raised and substantially answered,
informally, in a pearl_registry entry (2026-07-15, in the course of a *different*
investigation — attempting to construct the triality generator `U` — not previously
elevated to its own verified claim): a candidate identification `Φ: E_v→E_s` between
the channels' zero-mode bundles **can trivially be built at the `g2`-only level** (since
`E_v=E_s=E_c` as `G2`-equivariant bundles, per the already-established identical `su(3)`
content), but this `Φ` is explicitly flagged as "**coincidental**" and non-physical: *if*
`Φ` were genuinely `Spin(8)`-equivariant, it would be a nonzero element of
`Hom_Spin(8)(8_v,8_s)`, which **Schur's lemma forces to exactly 0** — `8_v` and `8_s` are
**inequivalent as `Spin(8)`-representations**, which is the *definition* of triality.

This is directly supported by a computation already run and PASSING: G102's own "S5"
check (`hom_dim(vec,sp)`, `hom_dim(vec,sm)`, `hom_dim(sp,sm)`, predicted and found
`(0,0,0)` — `Hom_so8` vanishes for every off-diagonal pair). **This round does not
propose new machinery — it re-verifies that specific, already-run computation directly
(spot-check discipline, since it is about to become the centerpiece of a claim), and
adds one genuinely new, concrete demonstration the prior work stopped short of: actually
building the "coincidental" `Φ` and showing explicitly, not just abstractly, that it
fails to intertwine a generic `so(8)` element.**

## The claim under test

> **C63.** No `so(8)`-equivariant identification exists between any two distinct
> triality channels (`Hom_so8(vec,sp)=Hom_so8(vec,sm)=Hom_so8(sp,sm)=0`, confirmed
> directly). Consequently, any change of basis that makes the three channels "look
> identical" (which is possible, and does exist, restricted to `su(3)⊂g2⊂so(8)`) is
> **not** a genuine symmetry of the construction — it necessarily fails to intertwine
> the action of a **generic** `so(8)` element, i.e. it breaks the very structure
> (`Spin(8)`, hence the `Spin(8)`-representation content that makes the channels a
> triality triple in the first place) that the compactification's fiber content is built
> from. The three channels are therefore **provably not redundant**: "3" cannot be
> reduced to "1" by any basis change that respects the actual geometric symmetry.

**Falsifier, fixed in advance:** if the off-diagonal `Hom_so8` dimensions are found
nonzero (contradicting G102's own prior result), or if the explicitly constructed `Φ`
turns out to intertwine a generic `so(8)` element after all, the claim is refuted and the
redundancy worry would need to be taken seriously.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **P1 (re-verification)** | direct recomputation of `Hom_so8(vec,sp)`, `Hom_so8(vec,sm)`, `Hom_so8(sp,sm)` gives `(0,0,0)` exactly, reproducing G102's own S5 result independently (own re-run of the same function, a spot-check not a new derivation) |
| **P2 (new, concrete)** | building the "coincidental" `su(3)`-level identification `Φ: vec→sp` (via the confirmed-identical `su(3)` action — literally any element of the 6-dim `Hom_su3(vec,sp)` space, e.g. one found by least-squares against the `su(3)` generators alone) and testing it against a **generic** `so(8)` element (not in `g2`) shows `Φ` does **not** intertwine: `‖Φ·ρ_vec(X) − ρ_sp(X)·Φ‖` is large (order 1), not ~0, for generic `X∈so(8)` — concretely displaying why the apparent redundancy is an artifact of the restricted view |
| **P3 (negative control, load-bearing)** | applying the SAME intertwining test to `X∈g2` (not generic) gives near-zero residual — confirming the harness correctly recovers the "coincidental" identification's actual domain of validity, i.e. P2's large residual is due to genericity, not a broken test |

## What this cannot show

- Does **not** newly discover anything about the `Spin(8)`/triality structure — G102 (S5)
  already established the crux fact (`Hom_so8` off-diagonal `=0`); this round re-verifies
  it directly and adds a concrete illustration, not a new theorem.
- Does **not** address whether the compactification's ACTUAL physical fiber structure
  genuinely realizes the full `Spin(8)` action (that is `OB11(iii)`'s harder, still-open
  half, and the separately-tracked `C_G67C3_THIRD_CHANNEL` claim, gates 2-6) — this round
  only shows that *if* the channels are distinguished by `Spin(8)` content (which the
  compactification's index-theorem construction, G73/G74A, already assumes throughout),
  then that distinction is real and cannot be undone by a change of basis.
- Nothing about `N_gen=3`'s CONDITIONAL status changes — this round defends against one
  specific way it *could* have been undermined; it does not newly establish it.

## kill_criterion

C63 survives if P1, P2, P3 all pass as predicted. C63 fails, and the redundancy worry
becomes live, if P1 contradicts G102's prior result, or if P2's constructed `Φ` turns out
to intertwine a generic element after all.
