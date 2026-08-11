# decision — complexification bridge: root-level match succeeds, full intertwiner still not found, gap localized precisely

## Verdict

`COMPLEX_CSA_FIX_CONFIRMED__ROOT_MATCH_CLEAN__INTERTWINER_NOT_YET_FOUND__GAP_LOCALIZED` →
**C68 PARTIAL — real progress, not resolution.**
**Date:** 2026-08-11 · L0: descriptive · `results_complexification_bridge.json` persisted.

---

## Summary against predictions

| # | predicted | found |
|---|---|---|
| **P1** direct ordering fails | most likely fails | **Fails, as predicted** — `hom_dim=4` under the raw given ordering, no nondegenerate `S` in 300 trials |
| **P2** complex CSA fix resolves the earlier crash | should | **Confirmed** — `extract_csa_and_roots_complex` (round128's method, real-coefficient assertion dropped) succeeds cleanly for both `su(3)` presentations, 6 genuine roots each, exact `A₂` hexagon structure |
| **P3** some candidate yields a valid nonzero intertwiner | expected | **Not found** — across all 48 candidate correspondences (all sign/ordering variants passing the exact-hexagon-residual filter), every single one gives `hom_dim=4` exactly, `best_det=0.0` exactly (not just small — genuinely zero across 300 random trials each) |

## Diagnosis: this is a localized implementation gap, not a root-matching problem or a contradiction of C65

Three facts together pin the issue down precisely:

1. **Root-matching itself is clean.** All 48 candidates pass the exact-hexagon-residual filter
   (`< 1e-6`) — the `A₂` root systems of both `su(3)` presentations align correctly at the
   Cartan-Weyl level.
2. **`mu`-fitting is clean.** For every candidate, the least-squares fit over the real bracket
   relations converges to machine-epsilon residual (`~1e-16`) — the root-vector rescaling
   consistently satisfies the structure-constant relations.
3. **`hom_dim` is uniformly 4, not the 6 representation theory predicts.** `Hom_su(3)(V,V)` for
   `V=1⊕1⊕3⊕3̄` (both sides, established in C65) should be **6**-dimensional (`4` from the
   `2×2` singlet-mixing freedom `+1` from `3` `+1` from `3̄`, by Schur) for **any** valid
   correspondence — this dimension is a property of the module structure alone and should not
   vary across the 12 `Aut(su(3))`-related candidates. Getting a **uniform, wrong** value across
   all 48 attempts (not a scatter of different wrong values) points at a **systematic** error in
   the transported-Cartan-generator formula (`Phi_H1 = T[0,0]·H1_g102 + T[0,1]·H2_g102`),
   directly reused from round128's own code — whose own comment explicitly flags this exact step
   as one that needed careful direction-checking the first time it was written ("`M_c` itself,
   NOT its inverse... caught by skeptic review, verified independently"). This round did not
   re-verify that directionality for the new pair; that is the concrete, localized next check.

## Why this is not evidence against C65, and not a mathematical surprise

C65 already established, via general representation theory (identical Casimir, identical module
type), that an isomorphism between round59's `Σ` and G102's `channel_v` **exists**. This round's
`hom_dim=4≠6` finding is a **self-inconsistency internal to this specific numerical construction**
(the predicted dimension for a correct construction is a fixed representation-theoretic fact,
`6`, independent of implementation) — not a new fact about the geometry. Per this round's own
pre-registered kill criterion: a failure to find `U` despite C65's existence guarantee indicates
a procedural gap, to be diagnosed rather than reported as a mathematical result. Diagnosed here as
precisely as time allowed; the exact line-level fix is the next step, not completed today.

## Kill Analysis

**Not killed:** C65 (module-type match, unaffected) or the belief that an explicit isomorphism
exists (still guaranteed by general theory).

**Localized, not resolved:** the earlier BLOCKED-SUBSTRATE finding (real/complex reality-type
mismatch) is now **fixed** — `extract_csa_and_roots_complex` works. What replaces it is a
narrower, more specific implementation bug in the Cartan-generator transport step, evidenced by
a wrong-but-uniform `hom_dim`. This is genuine progress in localization (external review's own
framing: "не «найти обычную unitary basis change», а сначала определить правильный
real/complexification intertwiner" — the complexification half is now done; what remains is a
implementation-level fix, not a further conceptual gap).

**Relaxation Map — the control check was run (cheap, same session), and it decisively narrows
the search.** `Hom_su3(V,V)` computed independently for **each side alone** (no cross-construction
matching at all — round59's `Σ` against itself, G102's `channel_v` against itself) gives **exactly
6 for both**, matching the representation-theory prediction precisely.
`[VERIFIED-numpy]`. This rules out `hom_basis` itself and rules out either individual
construction as the source of the discrepancy — **both are fine on their own.** The bug is
therefore definitively isolated to the **cross-construction correspondence-building pipeline**
specifically (root-matching, `Phi_H1`/`Phi_H2` Cartan transport, or `mu`-fitting, in some
combination) — not upstream of it. The concrete next step: re-derive the `Phi_H1`/`Phi_H2`
transport formula's directionality from first principles for this pair (matching round128's own
"verified independently" derivation, not just reusing its final formula), now knowing precisely
which stage of the pipeline to inspect.

## What this does NOT show

1. Does **not** find the explicit isomorphism `U` — the actual goal, not reached.
2. Does **not** contradict C65 — the existence guarantee stands untouched.
3. Does **not** mean the reality-type fix (P2) was pointless — it resolved a genuine blocker and
   is reused correctly; the new gap is a different, narrower issue one level downstream.
4. Nothing about `N_gen=3`'s CONDITIONAL status changes.

## What this DOES show, honestly stated (not overclaimed either direction)

Per the external review's own calibration: this is **not** "bridge confirmed, explicit alignment
open" (C65's own prior framing) anymore, and it is **not** "resolved" either. The accurate
status: **the alignment search is now running on correct machinery (complex CSA, clean root
match) and fails at a specific, identified, narrower step (Cartan-generator transport) than
before (the reality-type boundary).** One further localization, not yet a positive result.

## Check (reproduces this derivation)

```
cd experiments/20260811-ob11ii-complexification-bridge-test
python ob11ii_complexification_bridge.py
```
Expect: `p1_direct_ordering_works: false`, `p2_complex_csa_extraction_succeeded: true`,
`hom_dim_distribution: [4]` (uniform across 48 candidates, not the predicted 6),
`p3_isomorphism_found: false`, `verdict: NO_ISOMORPHISM_FOUND_DESPITE_COMPLEX_SEARCH`.
