# C142 -- DESIGN-ONLY round. Scopes C141's own falsifiable escape route
# ("the first twist bundle whose kernel EXCEEDS its own graded rank-
# nullity floor would be the first genuinely dynamical result in this
# whole research line") into a concrete candidate, computable BEFORE any
# Dirac-operator construction, per C141's own explicit recommendation.
# No physics computation happens in this round -- only representation
# theory design work, deciding whether a real, buildable candidate exists
# at all before spending a full round's effort building one.

## Why this is design-only, and why it matters before building anything

C141 found (independently hand-verified by the orchestrating session) that
EVERY twist-bundle-kernel test run in this project's history (round59/T0,
C139, C141, T1 -- 4 of 4) has its observed kernel EXACTLY equal to a
graded rank-nullity floor computable from pure `su(3)` branching data
alone. This raises an uncomfortable structural question, worked through
here rather than assumed: **could the test family, AS PRACTICED, ever
have shown otherwise?**

## The structural reason all 4 prior tests were incapable of surfacing a
   counterexample -- worked out here, not previously stated explicitly

For a connection-invariant summand pairing (a piece of the domain
`ODD_IDX`-side irrep against a piece of the target `EVEN_IDX`-side irrep,
or the twist bundle's own analogous split), the graded floor equals the
ACTUAL kernel contribution whenever the relevant `su(3)`-equivariant `Hom`
space between the paired constituents is **1-dimensional** -- because
Schur's lemma then forces the connection's action to be a SINGLE complex
scalar, and "is this one scalar zero or not" is exactly, and only, what
round59's Killing eigenvalue (`-sqrt(3)`) and C139's `Term2`
(`-2*sqrt(3)/3`) each individually answered. A single nonzero scalar
ALWAYS achieves the maximum possible rank (`1`) for a `1x1` (or, summed
appropriately, a floor-matching) block -- there is no way for a *single*
scalar to be "not quite full rank" short of being exactly zero, which is
exactly what "matches the floor" already covers on both sides (zero =
kernel exceeds floor by exactly the amount a vanishing scalar would add;
nonzero = kernel matches floor exactly).

**Checked directly, `[VERIFIED-tool]` (reusing round59/C139/C141/T1's own
already-computed multiplicities, no new construction):** every
`{connection}`-invariant summand pairing appearing in ALL FOUR prior
tests has `Hom`-space dimension exactly `1` on whichever side is
non-trivial (`EVEN_IDX`'s `1(x)1->1` and `3bar(x)3->1` channels; `ODD_IDX`'s
analogous channels; `m`'s `3(x)3bar->1` channel) -- **none of the four
prior tests ever had a genuinely MULTI-dimensional equivariant `Hom`
space to test.** This means the test family, as practiced, was
STRUCTURALLY INCAPABLE of ever showing `kernel > floor` -- not merely
empirically consistent with the floor by coincidence 4/4, but unable in
principle to have shown otherwise, given the specific summand structures
chosen so far.

## The candidate this suggests, already partially surfaced by C141's own
   exhaustive search (F7) but never built

C141 Section 2 (finding F7) already ran a brute-force search over
`(mult_1, mult_3, mult_3bar)` module types achieving round59's own shape
`(2,1)`, and found **two** solutions: `(1,0,1)` (`= EVEN_IDX` itself,
already tested via `T0`/`T1`) and **`(0,1,2)`** -- module type
`W_cand = 3 (+) 3bar (+) 3bar` (ONE copy of `3`, TWO copies of `3bar`) --
**never built or tested.**

**Why this candidate is structurally different, not just numerically
different:** with `mult_3bar = 2`, the equivariant `Hom` space pairing
`W_cand`'s `3bar`-content against `ODD_IDX`'s single `3`-constituent is
now **2-dimensional** (Frobenius reciprocity: `Hom_su3(3, W_cand) =
Hom_su3(3, 3bar+3bar) `, dimension `2`, one for each copy of `3bar`) --
the first genuinely multi-dimensional equivariant channel this project
would ever test, IF the two copies of `3bar` carry genuinely INDEPENDENT
connection data (not two labels for the same geometric object).

**If the two copies' connection data turn out to be independent:** the
resulting map is a genuine `2x1`-or-`1x2`-shaped (or larger, depending on
the target side) linear combination of TWO scalars, not one -- and
whether this combination achieves full rank or degenerates (both copies'
contributions cancelling, or aligning in a rank-reducing way) becomes a
REAL geometric question, not decided by Schur's lemma alone. THIS is
where `kernel > floor` becomes possible in principle for the first time.

**If the two copies' connection data turn out to be forced-proportional**
(e.g. built from the same geometric source with only a normalization
difference): the test collapses back to an effectively 1-dimensional
question, no different in kind from the four prior tests -- and this
round's job is to determine, honestly, which case actually holds BEFORE
committing to a full build.

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(exists entity) AND (exists
falsifiable predicate) AND (exists measurable outcome)`, all three
required.

- **Entity:** the candidate twist bundle `W_cand = 3 (+) 3bar (+) 3bar`
  (module type `(0,1,2)`, from C141's own F7 search), and whether a
  genuinely 2-dimensional, independently-sourced connection action on its
  two `3bar` copies can be constructed from this project's own existing
  geometric data (not invented ad hoc).
- **Falsifiable predicate:** either (a) a real, independently-motivated
  geometric source for a SECOND copy of `3bar` exists in this project
  (e.g. a differently-normalized or differently-sourced su(3)-equivariant
  map, not simply the same `NOMIZU`/`m`-derived `3bar` relabelled), making
  `W_cand` a genuinely buildable, potentially-informative test -- or (b)
  no such independent second source exists without inventing new,
  unmotivated structure, in which case `W_cand` (like the su(3)-adjoint
  alternative C139 Section 2 already rejected for the same reason) is NOT
  ready to build, and the escape route named by C141 remains open but
  currently unreachable within this project's existing geometric content.
- **Measurable outcome:** an explicit answer, with citation to specific
  existing project files/constructions if (a), or an honest statement of
  what would need to be invented and why that is out of scope if (b).

**If no genuinely independent second source can be found, this round
should report `DESIGN NOT YET READY` and say so plainly -- this is
explicitly permitted and is not a failure. A structurally-forced-
proportional finding would itself be interesting: it would mean this
project's own geometric content is currently too "thin" (every su(3)-
irrep it produces comes from a single source) to ever test C141's escape
route at all, which is itself worth knowing and registering.**

## What this round does NOT show

- Does NOT build or compute a Dirac operator for `W_cand` -- this is
  design/feasibility work only.
- Does NOT, even if `W_cand` is found buildable, predict what its kernel
  will be -- only whether the test would be STRUCTURALLY capable of
  showing something new, unlike the four prior tests.
- Does NOT reopen C123-C141's verdicts.
- Does NOT change `N_gen=3`'s CONDITIONAL status.
- Does NOT solicit Tom Lawrence's Part 5.

## Verification plan

- Reuse round59/C139/C141's own already-computed multiplicities and
  `Hom`-space dimensions where possible -- do not recompute from scratch
  what is already certified.
- Search this project's own codebase (not memory) for any existing,
  independently-derived `su(3)`-equivariant map into `3bar` (or `3`)
  beyond the ones already used by `m`/`Sigma`/`EVEN_IDX`/`ODD_IDX` --
  candidates to check explicitly: G102's own triality-channel
  constructions (`8_v`/`8_s`/`8_c`), round59/C70/C71's per-channel
  intertwiners `U_v`/`U_s`/`U_c`, and any other `su(3)`-module content
  already certified in this project's `docs/` or `experiments/` history.
- Cite `[VERIFIED]`/`[CITED]`/`[INFERRED]`/`[SPECULATIVE]` throughout.
- No FL Step 8a skeptic pass required for a design-only round with no
  computed physics claim to falsify -- but a plain self-check IS
  required: does the proposed `W_cand` construction, if found buildable,
  actually test what C141's escape route asks (kernel possibly exceeding
  a NON-trivial floor), or does it quietly reduce to an easier question?
  State this explicitly.
