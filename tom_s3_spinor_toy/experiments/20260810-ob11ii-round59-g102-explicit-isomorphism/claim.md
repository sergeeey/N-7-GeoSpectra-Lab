# OB11(ii), hard half — step 2: the explicit isomorphism between round59's Σ and G102's channel_v

**Experiment id:** `20260810-ob11ii-round59-g102-explicit-isomorphism`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C65 (module-type match), round128 (Cartan-Weyl alignment technique, reused)

---

## What C65 already guarantees, and what this round adds

C65 established that round59's `Σ` and G102's `channel_v` are the **same abstract `su(3)`-module**
(`1⊕1⊕3⊕3̄`, Casimir exactly `-4/3` for both). By standard representation theory, this **guarantees**
an intertwining isomorphism `S` exists — existence is not in question. What's not yet done is
**finding `S` explicitly**, needed before round59's real Clifford multiplication can be transported
into the triality-channel framework and tested for a genuine cross-channel mixing term.

This is the same TYPE of problem round128 already solved for a different pair (`su3_v` from
round124 vs `su3_σ` from G15) — two different concrete presentations of `su(3)` acting on
representation spaces, needing a basis-change intertwiner. round128's own technique (Cartan-Weyl
root matching, tried against all 12 elements of `Aut(su(3))` since the correspondence is only
fixed up to that outer ambiguity, then a least-squares fit for the root-vector scalars, then a
Sylvester/Kronecker nullspace search for the actual intertwiner) is reused directly — its helper
functions (`ad_matrix`, `extract_csa_and_roots`, `orthonormalize`, `find_hexagon_map`) are generic,
not specific to its original pair.

## The claim under test

> **C66 (working).** An explicit intertwiner `S` exists with `S · ρ_round59(X) · S⁻¹ = ρ_G102(X)`
> for all `X ∈ su(3)` (under some correspondence between the two generator presentations, fixed
> up to `Aut(su(3))`'s 12-fold ambiguity), found via the Cartan-Weyl matching + Sylvester-kernel
> technique round128 already validated on a different pair.

**Falsifier, fixed in advance:** if no candidate among the (up to 12) `Aut(su(3))`-related
matchings yields a nonzero intertwiner with small residual, despite C65's guarantee that one must
exist abstractly, that would indicate a bug in the alignment procedure (not a new mathematical
fact — existence is not actually in doubt here, unlike round128's original use of this technique).

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **P1** | both `su3_r59` (round59, on `Σ`) and `su3_g102_v` (G102, restricted to `channel_v`) admit a genuine 2-dim CSA via the random-regular-element technique, with a 6-root hexagon structure (standard `su(3)`/`A₂` root system) |
| **P2** | at least one of the (up to 12) `Aut(su(3))` candidate matchings gives an exact hexagon-residual near zero |
| **P3 (the deliverable)** | for the best candidate, the Sylvester/Kronecker nullspace search finds a nonzero nondegenerate intertwiner `S` (`\|det(S)\|` bounded away from 0 over random trials) with small isomorphism residual, confirming `S·A·S⁻¹=B` numerically for the matched generators |

## What this cannot show

- Does **not** yet transport round59's actual Clifford multiplication through `S` or test it for
  Hermiticity/Clifford-compatibility as a candidate mixing term — that is step 3, not attempted
  here.
- Does **not** resolve OB11(ii).
- Nothing about `N_gen=3`'s CONDITIONAL status changes.

## kill_criterion

Survives if P1–P3 all pass. If P3 fails despite P1/P2 passing, the procedure itself (not the
underlying mathematical fact) has a bug that needs fixing before proceeding — recorded as a
genuine harness failure, not a null result about the geometry.
