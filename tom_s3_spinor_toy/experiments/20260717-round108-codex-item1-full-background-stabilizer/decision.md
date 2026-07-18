# Round108 (Codex item 1) — Decision

**Date:** 2026-07-17
**Verdict:** `CONFIRMED__STABILIZER_OF_PHI_IS_G2_14DIM__ISOTROPY_AT_POINT_IS_SU3_8DIM__BOTH_LESS_THAN_SU4_15DIM__DOES_NOT_CLOSE_G97`
(two rounds of skeptic review; second pass CONFIRMED-REAL with a standing
overreach guard)
**Go/no-go:** directly computes, rather than merely cites, Codex/round105's
own top-ranked "decisive calculation" — the ambient group for gate G97's
comparison is genuinely smaller than the round-metric `SO(7)` (21-dim),
confirmed two ways (`G₂`=14-dim, `SU(3)`=8-dim), both computed from
first principles. **Does NOT, by itself, resolve or close gate G97** —
an explicit overreach guard from skeptic review, retained below.

## What was computed [VERIFIED-tool: sympy, two skeptic passes]

1. **Sanity check** [VERIFIED-tool]: the tensor-Lie-derivative formula
   used throughout (`(X·T)_{...}=-X_{il}T_{l...}-...`) correctly gives
   `X·g=0` for all 21 `so(7)` generators, by direct computation AND
   independently re-derived by hand by the skeptic (`(X·g)_{ij}=-X_{ij}
   -X_{ji}=0` for antisymmetric `X` — algebraically immediate).
2. **`Stab(φ)` in `so(7)`** [VERIFIED-tool]: using the standard, citable
   associative 3-form (`φ₀=e^{123}+e^{145}+e^{167}+e^{246}−e^{257}
   −e^{347}−e^{356}`, confirmed by skeptic pass 1 as the standard Bryant
   2005 convention, not a wrong-sign variant), the TRUE stabilizer
   dimension (nullspace of the 35×21 linear map `X↦X·φ`, not merely a
   basis-aligned count — which came out to 0, informatively showing the
   stabilizer is NOT aligned with the raw antisymmetric basis) is
   **exactly 14** — confirmed by skeptic pass 1 as a UNIQUE dimensional
   fingerprint among `so(7)`'s subalgebras (per the standard Dynkin
   classification: `so(6)=15`, `g₂=14`, `so(5)⊕so(2)=11`,
   `so(4)⊕so(3)=9` — no ambiguity).
3. **Isotropy of `G₂` at a point `x₀`** [VERIFIED-tool, added after
   skeptic pass 1's correction]: skeptic pass 1 flagged that "stabilizer
   of `φ` alone" (`G₂`) is NOT the same as "stabilizer of the FULL
   background including the almost-complex structure `J`" — since `J` is
   POINT-DEPENDENT (`J_x(v)=x×v`), fixing `φ` everywhere does not fix a
   specific point. Computed the further subalgebra of the 14-dim `G₂`
   that ALSO satisfies `X·x₀=0` (fixes a base point) — dimension **8**,
   matching `su(3)` (the isotropy of `G₂` at a point of `S⁶=G₂/SU(3)`,
   directly matching this project's own coset framing). Skeptic pass 2
   independently re-derived this via the orbit-stabilizer theorem
   (`dim(G₂)-dim(orbit of x₀)=14-6=8`, since `G₂` acts transitively on
   `S⁶`) — confirmed `CONFIRMED-REAL`, and confirmed dimension 8 is
   similarly a UNIQUE fingerprint (`su(3)` is the only compact,
   rank-≤2 real Lie algebra of dimension 8; `G₂` itself has rank 2, so
   any subalgebra has rank ≤2 — `su(2)⊕su(2)=6`, `so(4)=6`, `u(2)=4`,
   `T²=2`, none is 8).

## Applying the pre-registered criteria (claim.md Section 3)

**STABILIZER = 14-DIM, CONSISTENT WITH `G₂`** — confirmed exactly as
pre-registered, PLUS an additional, skeptic-motivated sharpening (the
8-dim `SU(3)` isotropy-at-a-point reading) that was not originally
anticipated but directly addresses what "full background including `J`"
actually requires.

## Kill Analysis

- **What this kills:** any residual ambiguity about whether "`G₂`
  (14-dim)" or "the full round-metric `SO(7)` (21-dim)" is the correct
  comparison group for `SU(3)_c`'s own derivation — directly computed
  now, not merely cited from `preprint.tex`'s own prose. Also computed,
  as a bonus, the SHARPER `SU(3)` (8-dim) reading if `J` specifically
  (not just `φ`) must be preserved.
- **What this does NOT kill — explicit overreach guard, per skeptic pass
  2, retained verbatim:** *"this rules out `SU(4)⊂`Stab(background
  restricted to the `S⁶` factor) by naive dimension, but does NOT rule
  out diagonal embeddings `SU(4)→G_iso(S³)×G_iso(S⁶)` that split
  generators across the product [S³ AND S⁶ factors together]... Framing
  should be: closes the naive same-factor embedding; diagonal/product
  embeddings remain the actual G97 question."** This is exactly
  round102's own earlier-flagged, still-unresolved caveat (goal-
  expansion-100's "diagonal embedding" possibility) — this round
  narrows the SAME-FACTOR question decisively (both `G₂` and `SU(3)`
  readings are `<15=dim(su(4))`) but does NOT address the cross-factor
  (S³-side + S⁶-side combined) possibility, which remains the one
  genuinely open route for an alternative `SU(4)` realization.
- **What survives, sharper than before:** the entire same-factor branch
  of "does an alternative `SU(4)` realization exist" is now closed by
  direct dimension count under EITHER of the two most natural readings
  of "the physically relevant ambient group" — narrowing gate G97's
  remaining open territory specifically to cross-factor/diagonal
  embeddings, a precise, well-defined target for any future attempt.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Check the diagonal-embedding possibility (round102/skeptic-flagged, the one genuinely open route left) | Search for a 15-dim subalgebra of `so(4)⊕so(7)` (or its `G₂`/`su(3)`-restricted subalgebras) that combines S³-side and S⁶-side generators — not attempted here or in round102 |
| Verify the `SU(3)` isotropy subalgebra found here is the SAME `su(3)` already used for `SU(3)_c` elsewhere in this project (e.g. round93's `su3_generators()`) | A direct basis/generator-level cross-check — not attempted here, would further strengthen the physical identification |

## Assumptions carried, unresolved

- The standard associative-3-form convention (`φ₀`, Bryant 2005) is used
  as THE `G₂`-structure on `S⁶` — consistent with, but not independently
  re-derived from, this project's own nearly-Kähler `S⁶=G₂/SU(3)`
  construction elsewhere.
- `x₀=(1,0,0,0,0,0,0)` — an arbitrary but WLOG-valid choice of base point
  (skeptic pass 2 confirmed the norm/specific value of `x₀` is
  irrelevant to the linear computation; any nonzero `x₀` gives the same
  dimension by the orbit-stabilizer argument).

## What this does NOT mean

1. Does NOT resolve or close gate G97 — explicit overreach guard above,
   not to be dropped in any future citation of this round.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`. Does NOT modify `preprint.tex` or any prior
   experiment folder.
3. Does NOT independently verify that this project's actual physical
   twist/torsion data (beyond the bare `G₂`-structure) doesn't further
   shrink the relevant stabilizer below 8 — only `g` and `φ`/`x₀` were
   checked; the specific twisted Dirac operator's own additional
   structure was not incorporated into this stabilizer computation.

## Check (reproduces this decision)

```
cd experiments/20260717-round108-codex-item1-full-background-stabilizer
python e31_full_background_stabilizer.py
```
Expect: `metric_preserved_by_all_21_generators=True`,
`true_stabilizer_dimension=14`, `stabilizer_consistent_with_G2_dim14=True`,
`isotropy_at_x0_dimension=8`, `isotropy_consistent_with_su3_dim8=True`.
