# C139 claim -- does a genuinely DIFFERENT twist bundle (not S+, not S-,
# not a sign/bigrading relabelling of round59's own Sigma=Lambda^bullet(C^3)
# construction -- a different su(3)-module type entirely, e.g. NOT
# 1+1+3+3bar) give an S6 twisted Dirac operator whose invariant-sector
# kernel is NOT 1, supplying the wrong-twist negative control this
# project's headline result has never had?

## Mode declaration

**Convergent-mode round.** Tests ONE specific, pre-registered claim to
completion. This is the direct, previously-scoped-but-unbuilt next step
from `pearl_registry/INDEX.md` row 89 (last updated by C73b,
2026-08-11) and the A3 item of the 2026-09-04 dependency/blast-radius
audit (`experiments/_audits/20260904-a1a2a3-dependency-blast-radius-audit.md`),
which independently recommended this as the single highest-value next
test in the whole OB1/N_gen=3 program: the only untested-assumption
item that is BOTH high blast-radius (6 direct `CLAIM_LEDGER.yaml`
dependents, including `C4_NGEN3_HEADLINE` itself) AND fully internally
computable (unlike A1's fiber-Spin(8) postulate, which is
BLOCKED-EXTERNAL pending Tom Lawrence).

## Question type (EstimandOps L0)

**Descriptive** -- existence of a specific mathematical object (a
twisted S6 Dirac operator on a genuinely different representation) and
its kernel dimension. Explicitly NOT causal, NOT predictive.

## The bar this round must clear, stated precisely (do not lower it)

Read, in full, before doing anything else -- this is not optional, it
is how this round avoids repeating FOUR already-failed attempts:

1. **`experiments/20260714-round59-trivial-rank-certification/decision.md`**
   IN FULL -- the original construction this round must twist
   DIFFERENTLY from. `Sigma = Lambda^bullet(C^3)`, an `su(3)`-module of
   type `1+1+3+3bar` (degrees 0,1,2,3 of the exterior algebra), the
   Killing-spinor-based S6 Dirac operator, `rank(D+|1)=1`,
   `(a,b)=(-1,-sqrt(3))`, `s=4`.
2. **`experiments/20260811-c73-round59-real-twisted-dirac-battery/decision.md`**
   and **`experiments/20260811-c73b-torsion-family-genuine-deformation-and-twist-control/decision.md`**
   IN FULL -- FOUR prior attempts at a wrong-twist negative control,
   ALL of which failed to discriminate, for FOUR DIFFERENT reasons, all
   already diagnosed. Do not repeat any of them:
   (a) Nomizu sign flip -- `|b|` unchanged, only flips sign, not
   discriminating for kernel structure.
   (b) alternate bigrading pairing (`even_odd -> odd_odd`) -- gives the
   EXACT SAME `(a,b)` as the physical pairing, a hidden even/odd
   duality in `Sigma` (plausibly the top-wedge element `y1y2y3` acting
   as an even<->odd swap), not an independent test.
   (c) mismatched-parity pairing (`odd_even -> odd_odd`) -- identically
   zero, but ALGEBRAICALLY FORCED (`D` preserves the second `Sigma`
   factor's Clifford parity exactly), not a physics discrimination.
   (d) twisting by `S+` instead of `S-` -- same magnitude structure,
   consistent with a known conjugation symmetry (`S+/S-` mirrors
   round59's own `psi_+/psi_-` branches), still not discriminating.
3. **`pearl_registry/INDEX.md` row 89** (find it, quote it exactly) --
   states precisely what is needed: *"Building D_S6 twisted by a
   DIFFERENT representation than Sigma (a non-(1+1+3+3bar)-type
   bundle, or a deliberately non-G2-equivariant twist) and checking
   that the resulting invariant-sector kernel is NOT 1 would supply a
   genuine discriminating negative control for the first time."* Also
   quote its explicit warning: *"before citing round59's kernel=1
   result as having passed a negative control (it has not, honestly)."*
4. **`experiments/20260811-c73b-.../decision.md`**'s own "What survives,
   as a genuinely scoped next step" section (search for that header) --
   the precise specification this round implements: *"a twist bundle
   that is NOT related to S- by any symmetry of Sigma's own
   construction (not S+, not a sign flip, not a bigrading relabeling)
   -- e.g. a twist by a representation with a DIFFERENT su(3)-module
   type entirely (not 1+1+3+3bar), or an explicitly non-G2-equivariant
   perturbation. This is a substantial new construction, comparable in
   scope to round59's own original build, not attempted here."*
5. **`experiments/20260705-g102-spin8-fiber-obstruction/decision.md`**
   -- for context on which `su(3)`-modules are already certified in
   this project's S6 construction (`Hom_{su(3)}` structure, the
   triality-channel decomposition), so this round's chosen alternate
   representation is stated relative to what already exists, not
   invented in a vacuum.

## Choosing the alternate representation -- the hardest part of this
## round, do it carefully and justify the choice explicitly

The kill criterion below does not pre-specify WHICH different
`su(3)`-module to twist by -- that choice must be made and justified
by this round, honestly, BEFORE computing the kernel (pre-registration
discipline, not picking a representation post-hoc because it gives the
"interesting" answer). Candidates to consider and choose among,
stating the reasoning:

- A representation with a DIFFERENT total dimension than `Sigma`'s 8
  (e.g. the `su(3)` adjoint, dimension 8 but module type `8` not
  `1+1+3+3bar` -- same dimension, different module type, isolates
  "module type matters" cleanly from "dimension matters").
- A representation with a genuinely different dimension (e.g. `6`, the
  fundamental-of-`SO(6)`-flavored real vector rep, if a consistent
  Clifford-module twist can be built from it).
- An explicitly non-`G2`-equivariant perturbation of `Sigma` itself
  (breaking `G2`-equivariance directly, as the alternative pearl row 89
  and C73b both name), if a module-type change proves hard to
  construct consistently.

State explicitly, before computing anything, which option is chosen
and why, and what a DIFFERENT choice would have looked like -- per
this project's Anti-Overfitting Gate, this is a pre-registration
requirement, not a formality.

## Background reading beyond the bar above

- `null_results/INDEX.md` -- check no other round has already
  attempted a non-`(1+1+3+3bar)` twist under a different name (the
  audit and C73b's own text both state this is "the only unexplored
  route" as of 2026-08-11/2026-09-04 -- confirm this is still true,
  do not just trust the citation).
- `CLAIM_LEDGER.yaml` entry `C2_ROUND59_KERNEL_DIM1` and
  `C4_NGEN3_HEADLINE` -- read the `depends_on` and `notes` fields, so
  this round understands exactly what is at stake if the kernel turns
  out to be `!=1` for a legitimate alternate twist (it would NOT
  immediately falsify `N_gen=3` -- it would show round59's specific
  twist choice needs independent justification beyond "it works",
  which is a different, narrower conclusion; state this distinction
  explicitly in the verdict, do not overclaim).

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(exists entity) AND (exists
falsifiable predicate) AND (exists measurable outcome)`, all three
required.

- **Entity:** a twisted S6 Dirac operator `D_{S6,twist'}`, built with
  the SAME Killing-spinor/homogeneous-space machinery round59 used
  (same base geometry, same calibration discipline), but twisted by an
  explicitly chosen, explicitly justified representation that is NOT
  `Sigma=Lambda^bullet(C^3)` and NOT related to it by any of the four
  already-tested symmetries (sign flip, bigrading relabel, parity
  mismatch, `S+` conjugate).
- **Falsifiable predicate:** the invariant-sector kernel of
  `D_{S6,twist'}` is either `=1` (matching round59, in which case this
  STILL does not discriminate, report honestly) or `!=1` (a genuine
  discriminating result, the first one this project has ever had for
  this question).
- **Measurable outcome:** the explicit kernel dimension, computed the
  same way round59's own three routes computed it (or as close a match
  as the different representation allows), with the calibration
  procedure applied to confirm this is a legitimate comparison, not an
  apples-to-oranges one.

**If no consistent, well-motivated alternate twist can be constructed
at all (e.g. the natural candidates all turn out to reduce to `Sigma`
under change of basis, or none admit a consistent Clifford-module
twist with this project's calibration procedure), this round should
report `BLOCKED` and name exactly what obstruction was found -- this
would itself be an interesting, informative result (a structural
reason `Sigma` might be the UNIQUE admissible twist, which would
actually strengthen round59's result rather than leave it uncontrolled).
This is explicitly permitted and is not a failure of the round.**

## Falsifiable claim

A genuinely different twist bundle (not `S+`, not a sign/bigrading
relabelling of `Sigma`) for the S6 Dirac operator, built with the same
calibration discipline round59 used, gives an invariant-sector kernel
dimension different from 1 -- supplying, for the first time, a real
discriminating negative control for round59's kernel=1 result.

## Kill criterion

FALSE if: (a) the kernel is `=1` for the chosen alternate twist too,
in which case this round reports NULL/NOT-DISCRIMINATING honestly
(matching the pattern of all four prior attempts) -- this is the
single most likely outcome given four consecutive prior failures on
this exact question, and should be reported as such, not dressed up;
(b) no consistent alternate twist can be constructed at all -- report
BLOCKED, name the obstruction (see above, this is itself informative);
(c) the "different" representation chosen turns out, on closer
inspection, to be related to `Sigma` by an undisclosed symmetry (the
exact trap that caught attempt (b) in C73) -- if found, this round
must catch and report this itself, not let a skeptic pass find it
first, per this project's own repeated lesson this session (C137,
C138) that self-caught defects still get real credit if diagnosed
honestly, and are worse if the round's own self-check misses them.

## What this round does NOT show

- Does NOT, if kernel turns out `!=1`, immediately falsify `N_gen=3`
  or `C2_ROUND59_KERNEL_DIM1` -- it would show round59's SPECIFIC
  twist choice needs independent physical justification beyond "it
  gives kernel=1", a narrower and more actionable finding, not a
  refutation. State this distinction explicitly if it arises.
- Does NOT, if kernel turns out `=1` again, prove no discriminating
  control can ever exist -- it would be the FIFTH data point in an
  accumulating pattern (per C73b's own reasoning: "makes it
  substantially more likely... simply does not have an
  internally-accessible wrong-twist control"), not a proof.
- Does NOT reopen C123-C138's verdicts (the OB1/H1c t-selection work is
  a separate question from this round, which concerns `N_gen=3`'s own
  evidentiary chain, not `t`-selection).
- Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda =
  FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
  `safe_for_runtime = False`.
- Does NOT solicit Tom Lawrence's Part 5.

## Verification plan

- Read all cited files in full before any computation, especially the
  four already-failed attempts (C73/C73b) -- build an explicit
  checklist confirming the chosen alternate twist is NOT any of the
  four, stated plainly in the decision.md.
- Pre-register the choice of alternate representation BEFORE computing
  the kernel, with explicit reasoning, per the Anti-Overfitting Gate.
- Reuse round59's own calibration procedure as closely as possible, so
  a `kernel != 1` result (if found) is a genuine physics difference,
  not an artifact of a different, uncalibrated computational setup --
  state explicitly how calibration was adapted or why it could not be.
- Cite `[VERIFIED]`/`[CITED]`/`[INFERRED]`/`[SPECULATIVE]` throughout.
- FL Step 8a skeptic pass (context-blind: only claim.md + decision.md +
  code, no session history). Given this round is high-stakes (directly
  touches the headline `N_gen=3` evidentiary chain, 6 ledger
  dependents per the 2026-09-04 audit) and involves a genuinely novel
  construction with real risk of an undisclosed-symmetry trap (exactly
  what caught attempt (b) in C73), run a SECOND, differently-worded
  pass (Paraphrase-Sensitivity Probe) regardless of the first pass's
  verdict, unless the first pass returns a clean, unqualified
  confirmation with zero findings.
