# C128 claim -- reconcile C125's and C126's readings of `∇^t`
# (Relaxation Map item X2 from C127, prerequisite for X1 and X6)

## Question type (EstimandOps L0)

**Descriptive/structural.** Not causal, not predictive. The question is:
within this project's own frozen Kaluza-Klein construction (metric ansatz
on `4 × S³ × S⁶`, `∇^t` the Cartan-Schouten family `∇^t_XY = t[X,Y]` on
`S³`, round99/111/113 convention), does `∇^t` instantiate ONE mathematical
structure or genuinely TWO -- and if two, are C125's and C126's treatments
both valid simultaneously (compatible), or does this project's actual
frozen physics commit to one and not the other?

## Background, stated honestly before any computation

C127 (2026-09-02) surfaced this gap while scoping a bordism/global-anomaly
route: it needed to know "which gauge group acts on `∇^t`" to even pose
its question, and found that this project carries two live, apparently
incompatible descriptions, each independently derived and independently
skeptic-verified the same day (2026-09-01), neither aware of the other:

| | description | consequence for the relation `t=0 ↔ t=1` | source |
|---|---|---|---|
| **C125** | `∇^t` is a **metric affine connection**; torsion `T^t=(2t-1)[·,·]` is a **tensor**; the frame bundle's structure group is `O(4)` (or its `SO(3)` factor); relating maps must be genuine isometries of `S³`, which C125 proves must be orientation-reversing (parity) | `t=0,1` **not** gauge-related; the exchange is realized ONLY by the specific isometry `ι(g)=g⁻¹` | C125 §0a, §2a |
| **C126** | `∇^t` is a **Yang-Mills connection** in `Ω¹(S³, 𝔰𝔬(3))`, i.e. an abstract Lie-algebra-valued 1-form, its own action functional `S_YM=∫|R^∇|²` varied over the FULL space of such 1-forms `𝒜`, with gauge group `𝒢` = all maps `S³→SO(3)` | `∇⁰`,`∇¹` are **ONE point of `𝒜/𝒢`**, separated in `𝒜/𝒢₀` (identity component only) by a large gauge transformation `g:S³→SO(3)` of winding number `n=-1` (computed two independent ways) | C126 (N3), §"(2)" |

C126's own decision.md contains a direct, self-aware admission relevant
here: *"the metric `g` itself is never varied anywhere in this round …
the connection/metric split is exactly what `S_YM` cannot see."* This is
the seed of the resolution and should NOT be re-derived from scratch --
read it directly and take it seriously as a first-order clue.

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(∃ entity) ∧ (∃ falsifiable
predicate) ∧ (∃ measurable outcome)`, all three required.

- **Entity:** the specific large gauge transformation `g: S³ → SO(3)`
  that C126 exhibits (winding `n=-1`) relating `∇⁰` and `∇¹` in `𝒜/𝒢₀`.
  This is a fully concrete, already-constructed object -- read C126's own
  derivation (both independent computations of `n=-1`) before doing
  anything else.
- **Falsifiable predicate:** "`g` is (or is not) realizable as the
  derivative/frame action of an actual diffeomorphism `f ∈ Diff(S³)` --
  i.e. is there `f` with `g = df` in the sense that matters for relating
  frame bundles, making `g` an honest frame-bundle automorphism covering
  a base diffeomorphism, not merely an abstract `SO(3)`-valued map with
  no base-space origin."
- **Measurable outcome:** an explicit yes/no on the predicate above, with
  the reasoning shown, not asserted. If yes: is `f` orientation-preserving
  or -reversing? Does `f` coincide with, or differ from, C125's `ι`? If
  `g` is NOT realizable as `df` for any diffeomorphism, that is itself the
  answer -- it means C126's gauge group `𝒢` is **strictly larger** than
  the image of `Diff(S³)` (or `Isom(S³)`) inside it, and the two rounds'
  claims are compatible but about **different transformation groups**,
  not contradictory.

**This round is explicitly permitted to conclude "genuinely distinct,
incompatible readings; a physical choice is required and this round
cannot make it" as a valid, non-failure outcome** -- matching this
project's own Zero-Signal Gate discipline elsewhere (C127, C124). Do NOT
force an artificial reconciliation if none exists honestly.

## Falsifiable claim (only if the Zero-Signal Gate passes)

Either:

**(A) Compatible:** `g` (or some winding-`(-1)` representative of its
class) IS realizable as `df` for an isometry or diffeomorphism `f` of
`S³` -- in which case state explicitly whether `f = ι` (C125's map) or a
genuinely different map, and if different, why C125's own gauge-
equivalence gate (which searched all isometries) did not find it, or why
it lies outside what C125 searched (e.g. `f` orientation-preserving
where `ι` is reversing -- C125 restricted attention to maps realizing
the `t=0↔t=1` swap AND found all candidates orientation-reversing; if a
genuinely orientation-PRESERVING diffeomorphism also relates `∇⁰,∇¹`,
that is new content C125 did not have, and must be checked against
C125's own completeness claim).

**(B) Incompatible / distinct groups:** `g` is NOT realizable as any
`df` -- `𝒜/𝒢` uses a strictly larger transformation group than
`Isom(S³)` or `Diff(S³)`, because Yang-Mills gauge transformations of an
abstract `𝔰𝔬(3)`-valued 1-form need not respect any soldering form or
correspond to any diffeomorphism at all. State this precisely: which
physical question is C126's `S_YM`/winding-number result actually
answering (stability/topology of an AUXILIARY Yang-Mills sector one
could hypothetically attach to this background) versus which physical
question is C125's gauge-equivalence gate answering (whether `t=0,1` are
redundant DESCRIPTIONS of the same physical metric/spin-connection
background) -- and which of these two questions is the one OB1 F4
actually needs answered for a *selection* mechanism.

**Kill criterion:** the round fails its own purpose if it (i) asserts a
reconciliation without exhibiting `f` explicitly (case A) or without
exhibiting a concrete obstruction ruling out any `f` (case B), or (ii)
silently drops either round's already-certified result to make the
"reconciliation" easier, or (iii) resolves the mathematical question but
fails to state which of the two readings this project's OWN frozen
physical construction (the one that actually defines `D_{S³,t}` and
sources the fermion content, per C38/C125 §3a) corresponds to -- the
mathematical resolution alone is not the full task; the physical
attribution is required too.

## What this round does NOT show

- Does not itself complete X1 or X6 -- those remain separate, gated on
  this round's outcome.
- Does not revisit or reopen C125's `FALSIFIED` verdict, C126's
  `WEAKENED` verdict, or C127's `BLOCKED` verdict -- this round asks a
  narrower question about which those verdicts' own internal category
  choices were made, not whether the verdicts themselves were correct
  given that choice.
- Does not change `N_gen=3`'s CONDITIONAL status, `lambda=
  FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
- Does not solicit Tom Lawrence's Part 5.

## Verification plan

- Read C125's `decision.md` and C126's `decision.md` in full (not
  excerpts) before writing anything -- both are already in this
  project's record; re-derive nothing that is already computed there.
- Answer the Zero-Signal Gate predicate with an explicit construction or
  explicit obstruction, not a plausibility argument.
- State the physical attribution (which reading, if either, matches this
  project's actual frozen KK ansatz) explicitly, citing the specific
  place in the ansatz that settles it if one exists, or stating clearly
  that the ansatz itself is silent on this point if it is.
- FL Step 8a skeptic pass on whatever this round produces, positive or
  negative, before it enters the permanent record.
