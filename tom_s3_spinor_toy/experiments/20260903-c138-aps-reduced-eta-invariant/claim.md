# C138 claim -- does the APS REDUCED eta invariant `xi(D^t)=(eta(D^t)+h(t))/2
# mod 1` (as opposed to the RAW eta invariant C121 already tested and found
# NULL) show a special value or discontinuity structure at `t in {0,1}` not
# shared by any other spectral crossing of the S3 torsion family?

## Mode declaration

**Convergent-mode round.** Tests ONE specific, pre-registered claim to
completion. This is the pearl_registry row 116 "genuinely different,
unattempted variant" surfaced by C121's own FL Step 8a skeptic pass --
NOT a new mechanism class, but a materially different quantity built
from C121's own already-certified `eta(D^t)` closed form.

## Question type (EstimandOps L0)

**Descriptive** -- does `xi(D^t)` at `t in {0,1}` take a value
structurally distinguished from its value at other spectral crossings
of the same family? Explicitly NOT causal, NOT predictive.

## Background, stated honestly before any computation

Read, in full, before doing anything else:
- `experiments/20260901-c121-eta-invariant-general-t/decision.md` IN
  FULL -- this round's entire machinery is inherited from there, do not
  re-derive from scratch. Load-bearing facts already certified
  (`[VERIFIED-tool]`, independently re-derived twice by that round's
  own skeptic pass):
  - `eta(a) = P(a) + 2*sum_{n=0}^{J} mu(n)`, `P(a) = a(3-4a^2)/6`,
    `mu(n) = (n+1)(n+2)`, on the `J`-th interval past the base one
    (crossings at `a = +-3/2, +-5/2, +-7/2, ...`, i.e.
    `t = 0, 1, -1/3, 4/3, ...` via `a = 3(t-1/2)`).
  - `eta mod 2` is IDENTICAL on every interval (this is what C121
    found NULL -- do not repeat this test, it is already closed).
  - **A convention subtlety C121's OWN first draft got wrong and its
    skeptic pass corrected**: at a crossing point itself, the naive
    one-sided limit of `P(a)` (e.g. `P(3/2)=-1.5` approaching from
    inside `(0,1)`) is NOT the same as the value AT the crossing point,
    because the crossing eigenvalue is exactly zero there and should
    contribute `sign(0)=0`, not the one-sided limit's implicit
    `sign(+-eps)=+-1`. The corrected value at `t=1` (`a=3/2`) is
    `eta=+1/2`, not `-3/2`/`-1.5`. **This round must use the
    AT-THE-POINT value, not a one-sided limit, or it repeats C121's
    own already-corrected mistake.**
  - Already computed in passing by C121's skeptic pass (§86, quoted
    exactly, re-derive rather than trust): at `t=1`, `h=2` (kernel
    dimension), giving `xi = (eta+h)/2 = (0.5+2)/2 = 1.25`, i.e.
    `1.25 mod 1 = 0.25`. **Verify this number from scratch -- do not
    just copy it.**
- `pearl_registry/INDEX.md` rows 115 and 116 (find them, quote them
  exactly) -- row 115 records C121's full NULL result and names `xi`
  as the one surviving unattempted variant; row 116 is the specific
  pearl this round is closing, and states the falsifiable prediction
  precisely: `xi(t)` may show special structure BECAUSE `h(t)`'s jump
  (`mu(n)=(n+1)(n+2)`, NOT constant across crossings: `2` at `n=0`,
  `6` at `n=1`, `12` at `n=2`, ...) breaks the symmetry that made raw
  `eta mod 2` featureless.
- `null_results/INDEX.md` entry `C121-EtaInvariant` -- read the exact
  wording of what was already ruled out, so this round's own claim
  does not silently re-test it under a new name.
- The APS (Atiyah-Patodi-Singer) index theorem literature's own
  standard definition of the REDUCED eta invariant `xi = (eta+h)/2 mod
  1` (find a citable primary or well-established secondary source for
  this exact definition -- do not invent the `mod 1` convention ad
  hoc; confirm it matches what C121's skeptic pass used).

## What `h(t)` (kernel dimension) actually is, stated precisely

`h(t) = dim ker(D^t)`, the dimension of the zero-eigenspace of the
torsion-deformed S3 Dirac operator at the specific value of `t`. It is
ZERO everywhere except exactly AT a spectral crossing, where it equals
that crossing's multiplicity `mu(n) = (n+1)(n+2)` (already-certified,
from round67/round116's own multiplicity table -- re-verify, do not
just cite). State explicitly, for each crossing `t` computed, which
`n` it belongs to and why (the crossing lattice `a = +-(3/2+n)` for
`n=0,1,2,...` maps to `t` via `a=3(t-1/2)` -- show this map, do not
just assert the `t` values).

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(exists entity) AND (exists
falsifiable predicate) AND (exists measurable outcome)`, all three
required.

- **Entity:** the APS reduced eta invariant `xi(D^t) = (eta(D^t) +
  h(t))/2 mod 1`, evaluated AT each of the first 2-3 spectral crossing
  pairs of the certified `D^t` family (`t=0,1` [n=0]; `t=-1/3,4/3`
  [n=1]; optionally `t=-2/3,5/3` [n=2] if cheap).
- **Falsifiable predicate:** `xi(t=0)` and/or `xi(t=1)` take a value
  that is EITHER (a) distinguished by some structural property (e.g.
  a simple rational with small denominator, an integer, a value
  matching an already-certified physical quantity elsewhere in this
  project) that the OTHER crossings' `xi` values do NOT share, OR (b)
  identical across all crossings (in which case this closes NULL,
  exactly like C121, and the mechanism class is exhausted).
- **Measurable outcome:** an explicit table of `xi(t)` for every
  crossing computed, with the `mod 1` value, stated in lowest terms,
  compared side by side -- not asserted, shown.

**If `xi(t)` turns out to be `t`-independent for the SAME reason C121
found `eta mod 2` t-independent (i.e. the `h(t)` jump exactly cancels
against the even-integer offset structure algebraically, in a way
provable in closed form), this round should report that NULL cleanly
and show the cancellation explicitly -- not declare it "not yet
evaluable" the way C121's own first draft initially mis-stepped on a
different sub-question. This is explicitly permitted and is not a
failure of the round.**

## Falsifiable claim

The APS reduced eta invariant `xi(D^t)`, computed at `t in {0,1}` and
at least one further crossing pair, takes a value at `t in {0,1}` that
is structurally distinguished from its value at the other computed
crossings -- not merely different by happenstance, but distinguished
by some stated, checkable property (rationality with small
denominator, matching an already-certified project quantity, or an
explicit closed-form argument for why `n=0` is special).

## Kill criterion

FALSE if: (a) `xi(t)` is identical (mod 1) across every computed
crossing, exactly as raw `eta mod 2` was in C121 -- report NULL, and
show algebraically WHY (the `h(t)` jump structure, worked through
explicitly, is the natural place to look for the cancellation
mechanism, per C121's own `dP/da=-2(a^2-1/4)` APS variation identity);
(b) `xi(t=0)` and `xi(t=1)` differ from each other by an amount with
no stated structural meaning (a "different number" alone is not
selection -- state what would make the specific values AT `t=0,1`
meaningful, e.g. matching a quantized level already used elsewhere in
this project, before treating any numeric difference as a result);
(c) the computation cannot be completed without importing an
unjustified new convention beyond APS's own standard `mod 1`
definition -- report BLOCKED, name exactly what convention is missing
and why it cannot be fixed from the cited literature alone.

## What this round does NOT show

- Does NOT reopen C121's own already-closed NULL on the RAW `eta mod
  2` invariant -- that question stays closed.
- Does NOT reopen C123-C137's verdicts.
- Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda =
  FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
  `safe_for_runtime = False`.
- Does NOT close H1c, OB1, or round95's own diagnosed gap even if it
  succeeds -- it would supply one candidate F6-shaped mechanism among
  several still needed (per PARENT_ACTION_GATE.md F4/F6).
- Does NOT claim `xi`'s standard APS definition is being invented here
  -- if no citable primary/secondary source confirms the exact `mod 1`
  convention used, say so explicitly rather than presenting an ad hoc
  formula as textbook.
- Does NOT solicit Tom Lawrence's Part 5.

## Verification plan

- Read all cited files in full before any computation, especially
  C121's own decision.md in full (not just the summary in this
  claim.md) and its skeptic-pass correction of the crossing-point
  convention.
- Re-derive `eta(a)=P(a)+2*sum mu(n)` from C121's own two independent
  routes (Hurwitz-zeta and heat-kernel Mellin transform) rather than
  copying the formula uncritically -- at minimum spot-check it at 2-3
  points against C121's own reported values.
- Compute `h(t)` explicitly from the certified multiplicity table,
  showing the `n <-> t` crossing-lattice map.
- Build the `xi(t)` table for at least 2 crossing pairs (4 values:
  `t=0,1,-1/3,4/3`), using AT-THE-POINT values throughout, not
  one-sided limits.
- Actively test whether the observed pattern (distinguished or not)
  survives an algebraic derivation, not just numeric evaluation at a
  handful of points -- if `xi` IS `t`-independent, derive why in closed
  form, the same standard this project holds itself to per C121's own
  precedent.
- Cite `[VERIFIED]`/`[CITED]`/`[INFERRED]`/`[SPECULATIVE]` throughout.
- FL Step 8a skeptic pass (context-blind: only claim.md + decision.md +
  code, no session history). Given this round reuses already-certified
  machinery (lower computational risk than C121's original derivation)
  but has a documented history of exactly this kind of round tripping
  on a convention subtlety (C121 itself), a single pass suffices
  UNLESS it finds something that changes the verdict's direction or
  flags an unresolved convention question, in which case run a second,
  differently-worded pass (Paraphrase-Sensitivity Probe).
