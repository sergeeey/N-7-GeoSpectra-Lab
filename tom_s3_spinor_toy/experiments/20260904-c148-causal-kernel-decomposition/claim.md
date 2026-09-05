# C148 — causal decomposition of every kernel this project has computed, with one level relabelled

## L0 gate (EstimandOps)

**Question type:** Descriptive (accounting/decomposition of already-registered
quantities). Not causal in the statistical sense, not predictive.

## Trigger, and a correction to the proposal as received

User proposed a three-level decomposition
`|ind D| ≤ F_rep ≤ dim ker D`, with `Δ_rep = F_rep − |ind D|` and
`Δ_geo = dim ker D − F_rep`, framed as
`Topology → Representation → Geometry`, and correctly noted it is almost
free on already-existing data.

**Correction made BEFORE computing, not after:** in this project's actual
setting the first level is **not topology**. Every kernel in question is
the kernel of a map between *`su(3)`-invariant sectors*, and there
`dim(domain) − dim(target)` is a difference of **Clebsch–Gordan
multiplicities** — pure representation theory. Using it as the "topological"
level would make `Δ_rep` compare representation theory against
representation theory, and the decomposition would silently measure nothing.
The genuine topological index would be an Atiyah–Singer computation on the
actual bundle over `S⁶` — a different object, and one this project has
already touched with a different answer (`null_results`: `ind(D⊗E) = 7`, not
3, for the `S⁻⊗T^{1,0}S⁶` candidate).

**What is computed instead**, with honest labels:

| level | symbol | what it actually is |
|---|---|---|
| aggregate branching | `A = max(0, dim_domain − dim_target)` | plain rank-nullity on the AGGREGATE invariant-sector shape — the bound C141's first two drafts used |
| graded branching | `F` | C141/C143's per-`{connection}`-invariant-summand floor — finer representation theory, same inputs |
| observed | `K` | the actually computed kernel dimension |

with `Δ_graded = F − A` (what the per-summand refinement adds over the
aggregate count) and `Δ_geo = K − F` (what is left for the operator's own
geometry after all branching information is used).

## Falsifiable claim

Across all four twist-bundle constructions ever computed in this project
(round59/T0, C139/`m`, C141/`m⊕2·1`, T1/`Σ` self-twisted):

1. `A ≤ F ≤ K` holds in every case (the chain is well-ordered).
2. **`Δ_geo = 0` in all four** — no construction's kernel exceeds what pure
   graded branching already forces.
3. `Δ_graded > 0` in exactly one case, **T1**, and it is exactly the case
   whose aggregate shape `(3,3)` says "no information" while its graded
   floor says `1`.

**Kill criterion:** any construction with `Δ_geo ≠ 0`, or a violation of
`A ≤ F ≤ K`, falsifies the claim as stated.

## Data provenance (all read from registered artifacts this session, none from memory)

- `results_c139.json` → `invariant_sector_dims`: `domain_ODD_x_m = 1`,
  `target_EVEN_x_m = 1`, plus round59's own `(2, 1)`.
- `results_c141.json` → `graded_rank_nullity_floor.cases`: all four
  constructions with their summand decompositions, `graded_floor`, and
  `observed_kernel`.

## What this does NOT mean

1. Does NOT compute a topological index for any of these constructions —
   explicitly out of scope after the relabelling above; the "topology" level
   of the user's original framing is **not supplied** by this round, and
   saying otherwise would be the exact error the relabelling exists to
   prevent.
2. Does NOT establish `Δ_geo = 0` for constructions not yet built — it is an
   observation over four cases, all of which have `Hom`-dimension 1 per
   summand (C143's Lemma 1 regime), where C143 already proves the kernel is
   scalar-determined. The interesting regime (`Hom ≥ 2`) is untested and
   remains the place where `Δ_geo > 0` could first appear.
3. Does NOT change `N_gen=3`'s CONDITIONAL status or any registered kernel
   value — this round adds no new computation, only an accounting over
   already-certified numbers.
4. Does NOT by itself justify abandoning `kernel = 1` as an observable — it
   supports the user's stop-rule, but the stop-rule's own scope is the
   `Hom`-dimension-1 class, not all future constructions.
