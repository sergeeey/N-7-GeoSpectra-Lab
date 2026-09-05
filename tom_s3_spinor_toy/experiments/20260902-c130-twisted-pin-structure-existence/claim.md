# C130 claim -- does the TWISTED Pin structure the anomaly actually needs
# exist? (C129's Relaxation Map item Z1, "cheaper than round95, the single
# highest-value next step")

## Question type (EstimandOps L0)

**Descriptive/existence.** Not causal, not predictive. C129 established
that the BARE tangential structure of the relevant mapping torus admits
both Pin^+ and Pin^- (structure-existence, no fermion content involved).
This round asks the question C129 explicitly declined to answer (§7d,
called there "a plausibility remark, not a result"): does the TWISTED
structure -- the one a genuine Dai-Freed anomaly argument on the ACTUAL
fermion content requires -- exist?

## Background, stated honestly before any computation

Read, in FULL, before doing anything else:
- `experiments/20260901-c127-bordism-global-anomaly-scoping/decision.md`,
  especially its own FL Step 8a skeptic pass finding 1 (§0), which
  established: the fermion representation `R(0) = (1,2)` is **half-integral**
  under `SU(2)_b` (its central `-1` acts as `(-1)^F`), so the tangential
  structure it actually requires is `Spin ×_{Z2} SU(2)_b` at `t=0` (and
  `Spin ×_{Z2} SU(2)_a` at `t=1`, isomorphic by the label-swap `σ`) --
  **not bare Spin**. This is the exact PIN analogue of the question this
  round must answer, one structure type down (`Pin`, not `Spin`, because
  C128 §4/§6b established the relevant relating map is orientation-
  reversing, making the object non-orientable).
- `experiments/20260902-c128-nabla-t-gauge-group-reconciliation/decision.md`
  §5, which settles: the frozen ansatz uses C125's category (a metric
  affine connection on the frame bundle -- fixing the vielbein is a
  *complete* gauge-fixing of C126's Yang-Mills gauge group `𝒢`). This is
  what fixes `G` for this round's twisted structure `Pin^± ×_{Z2} G` --
  read §5's table and §5a/§5b carefully to determine exactly what `G`
  this project's own frozen content licenses (it is NOT free choice; C128
  §5's converse point is explicit that nothing in the frozen ansatz
  commits to an independent Yang-Mills sector).
- `experiments/20260902-c129-pin-structure-existence-mapping-torus/decision.md`
  §7d (the exact question this round continues) and §4 (the `H²(M_ι;𝔽₂)=0`
  theorem, proven 5 independent ways, which is the single fact any twisted
  argument must correctly use or correctly show does NOT simply carry
  over). Also read §2a/§2c for the primary Kirby-Taylor source already
  retrieved and read this session, and the project's own established
  correction there (`Pin^+ ⟺ w₂=0`, `Pin^- ⟺ w₂+w₁²=0`).

**The exact trap this round must not fall into, stated explicitly because
C129 itself flagged it and refused to take the shortcut:** "the twisted
obstruction also lands in `H²(M;𝔽₂)`, which C129 showed is zero, so it
trivially vanishes too" is NOT a licensed inference without justification.
Twisting by a nontrivial `G`-bundle can change which characteristic class
is actually the obstruction, potentially requiring cohomology of a
DIFFERENT bundle/space (e.g. `H²` of the total space of a `G`-bundle over
`M`, or a class that does not simply factor through `H²(M;𝔽₂)` at all,
depending on the precise central extension defining `Pin^± ×_{Z2} G`). This
round's central job is to determine, with an actual derivation or a
directly-applicable primary citation, which of these is really true here
-- not to assume the convenient answer.

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(∃ entity) ∧ (∃ falsifiable
predicate) ∧ (∃ measurable outcome)`, all three required.

- **Entity:** the precise twisted tangential structure `Pin^{c'} :=
  Pin^± ×_{Z2} G` on `M_ι` (or the relevant mapping torus), for the
  SPECIFIC `G` and central extension determined by this project's own
  frozen fermion content (per C127 finding 1's `Spin ×_{Z2} SU(2)` template
  and C128 §5's fixing of `G`). **This round's FIRST job, matching C127's
  and C128's own discipline, is to determine whether this entity can even
  be named precisely from the frozen content** -- state the exact group,
  the exact central extension/cocycle, and the exact representation data
  that determines it, or explain precisely why it cannot be pinned down
  with what this project has certified so far.
- **Falsifiable predicate:** the twisted structure's obstruction class
  (defined precisely, with a citation for the general formula) is zero in
  its own home cohomology group -- stated as a specific, checkable
  yes/no, not "probably fine because a related group vanished".
- **Measurable outcome:** an explicit computation, or a directly-
  applicable, actually-read citation, of that obstruction class for this
  specific manifold/bundle -- not an analogy to C129's untwisted result.

**If the twisted entity cannot be named precisely from this project's own
frozen content, or if the obstruction's home cohomology group cannot be
determined or computed with real confidence, this round should return
`BLOCKED (missing ingredient named)` or explicit `[UNKNOWN]` -- NOT
assume C129's untwisted vanishing transfers, NOT guess, and NOT silently
narrow the question to whatever is easiest to compute.** This is
explicitly permitted and is not a failure of the round.

## Falsifiable claim (only if the Zero-Signal Gate passes)

The twisted structure `Pin^± ×_{Z2} G` (for the specific `G` and extension
fixed by this project's frozen content) exists, does not exist, or the
question is genuinely undetermined by what has been computed -- stated
with an explicit derivation or citation for the obstruction class, and an
explicit statement of whether/why C129's `H²(M;𝔽₂)=0` result does or does
not settle it.

**Kill criterion:** the round fails its own purpose if it (a) asserts
existence or non-existence of the twisted structure without exhibiting or
citing the actual obstruction-class formula for a `Pin^± ×_{Z2} G`
structure and evaluating it (not merely gesturing at C129's untwisted
result), (b) cannot precisely name `G` and the central extension from
this project's own frozen content but proceeds to compute anyway, or (c)
conflates "the untwisted group vanished" with "the twisted obstruction
therefore vanishes" without an explicit justification for why the two
classes coincide (or an explicit argument for why they must, even if
distinct, both vanish).

## What this round does NOT show

- Does not touch round95's missing S⁶-S³ link (C127's ingredient 2) --
  that is a separate, later question about which specific type
  (`Pin^+`-twisted vs `Pin^-`-twisted) the actual physics needs, distinct
  from whether EITHER twisted structure exists at all.
- Does not evaluate any anomaly or attempt C127's A2/X6's actual anomaly
  computation -- existence of the structure is the entire scope, exactly
  as C127/C128/C129 each separated "does it exist" from "does it force
  the pair".
- Does not reopen C125's `FALSIFIED`, C126's `WEAKENED`, C127's
  `BLOCKED`, C128's `OUTCOME_B`, or C129's verdict -- builds on all four
  as given.
- Does not change `N_gen=3`'s CONDITIONAL status, `lambda=
  FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
- Does not solicit Tom Lawrence's Part 5.

## Verification plan

- Read all four cited decision.md files in full before anything else.
- Literature-first: search for the precise definition and existence
  criterion of twisted `Pin`/`Spin-G` structures (`Pin^c`-type
  constructions, or the specific `Spin ×_{Z2} G` / `Pin ×_{Z2} G`
  formalism used in the Dai-Freed anomaly literature this project has
  already cited -- García-Etxebarria & Montero arXiv:1808.00009, and any
  paper it or Kirby-Taylor cites for the twisted case). Retrieve and read
  primary sources directly where possible, matching C129's own standard
  (it explicitly retired a `[MEMORY, unverified]` tag this way).
- Determine `G` and the extension precisely from C127 finding 1 and C128
  §5, not by re-guessing.
- Compute or cite the obstruction class for THIS specific manifold and
  bundle. If it turns out to genuinely reduce to `H²(M_ι;𝔽₂)`, prove that
  reduction explicitly (do not assert it); if it does not reduce that way,
  compute or cite what it actually is.
- FL Step 8a skeptic pass, and -- matching C128's and C129's own precedent
  for a load-bearing conclusion closing a live Relaxation Map item -- a
  SECOND independent pass with a differently-worded prompt (Paraphrase-
  Sensitivity Probe) unless the first pass returns a clean, unqualified
  confirmation with zero findings.
