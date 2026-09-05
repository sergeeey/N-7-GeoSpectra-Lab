# C134 claim -- does the Einstein-Cartan-Sciama-Kibble (ECSK) torsion field
# equation, sourced by this project's own S6-twisted zero modes, admit a
# self-consistent solution with 2t-1 != 0 on the frozen S3 background?
# (C132's top-ranked-tied candidate P2, ready-to-run sketch B)

## Mode declaration

**Convergent-mode round.** Tests ONE specific, pre-registered claim to
completion -- promote, weaken, or kill it -- following this project's
standard FL Full-Ladder discipline used throughout C123-C133.

## Question type (EstimandOps L0)

**Descriptive** -- existence of a fixed point. Explicitly NOT causal,
NOT predictive. The question is whether an algebraic self-consistency
equation (torsion sourced by a specific, already-certified fermion
axial current) has a solution with `2t-1 != 0`, not whether that
solution is dynamically preferred, not whether it "causes" anything.

## Background, stated honestly before any computation

Read, in full, before doing anything else:
- `experiments/20260902-c132-13d-parent-action-survey/decision.md`,
  especially the `P2` candidate write-up (search "### `P2`"), and
  Section 6 "Sketch B" (this claim.md is built directly from that
  sketch -- follow its kill criteria and controls exactly, do not
  weaken them). Also read `P2`'s CDT ranking entry and note it is
  TIED with `P14` (a joint 13D Killing-spinor constraint) -- this round
  does not need to out-rank `P14`, it only needs to honestly resolve
  its own question.
- **`experiments/20260717-round72-*/decision.md`** (find via Glob for
  the exact folder name, pattern `*round72*`) -- Section covering the
  "E8 gate" (search for "E8" and "final summary table"). This is the
  MOST IMPORTANT prior-art file for this round, and C132's own first
  draft got this wrong (cited a table round72 itself marks
  `SUPERSEDED-IN-PLACE` 100 lines later, instead of the live
  `BLOCKED/UNDERDETERMINED` status with a registered E8 gate). You
  MUST open against round72's actual, LIVE E8 gate -- its 6 PASS and
  explicit FAIL criteria -- not the superseded row. Read the ENTIRE
  file to find both tables and confirm which one supersedes which
  directly from the file's own text, do not trust any paraphrase
  (including this one) without verifying against the primary source.
  Round72's own adverse preliminary computation must be addressed
  explicitly: for a BOSONIC functional `F(t) = a|R^t|^2 + b|T^t|^2`,
  `F'(t) = 2(2t-1)[aA*t(t-1) + 2bB]`, so `t=1/2` is ALWAYS stationary
  and `t=0,1` are stationary only if `b=0` (i.e. only by discarding the
  torsion-energy term by hand). E8's own FAIL criteria include "the
  stationary point is at t=1/2".
- `experiments/20260717-round111-*/decision.md` (find via Glob) --
  its own Relaxation Map row naming "Derive alpha from an actual
  physical action | Requires committing to a specific action principle
  (Einstein-Cartan, spectral action...)" -- named there, never
  attempted until now.
- `experiments/20260717-round75-e11-*/decision.md` (find via Glob,
  "Q2") -- found ZERO wiring between flux and any torsion object in
  `preprint.tex` at that time. Check whether this is still true or has
  changed since.
- `PARENT_ACTION_GATE.md` F6 ("Background equations") in full -- this
  is "the single largest gap in the whole OB1 program" per the file's
  own words, and this round is the FIRST attempt in the project's
  history to supply an actual derived EOM for it (not just a bare
  action functional's stationarity, which C123/C126 already showed
  carries zero selection content).
- `experiments/20260901-c124-parent-invariant-classification-preregistration/decision.md`
  -- confirm C124's own explicit scope carve-out for "fermion
  bilinears" (its STRUCTURAL_NO_GO does NOT cover them) and cite the
  exact line.
- `experiments/20260901-c125-full-gauge-equivalence-gate/decision.md`
  Section 0a/2a -- the exact form of torsion `T^t = (2t-1)[.,.]` this
  project uses, and C128's finding that the frame bundle's group is
  not a free-standing twisting group (relevant to how you frame `G` if
  a gauge sector enters your construction -- it should not, per O1/GAP-4,
  see below).
- The pre-filters O1, O3, O5, O6, O7 as quoted in C132's decision.md
  Section 1b (search "### 1b. The seven pre-filters") -- your claim
  must clear O1 (product/decoupling), O3 (fermion-bilinear carve-out),
  O5 (torsion/soldering-form functionals are OUTSIDE the dead-on-arrival
  filter), O6 (Kunneth), O7 (epsilon/eta-sector).

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(exists entity) AND (exists
falsifiable predicate) AND (exists measurable outcome)`, all three
required.

- **Entity:** the ECSK torsion field equation on `M4 x S3 x S6` (or its
  S3-restricted form, per the Scoping Discipline below), sourced by the
  ALREADY-CERTIFIED S6-twisted zero-mode axial current
  `<psibar gamma5 gamma^a psi>`, evaluated using this project's own
  chirality result (L5/G74B: `sign(ind)=+1`, all three zero modes in
  `D+`).
- **Falsifiable predicate:** the self-consistency equation (torsion
  sourced by the axial current, axial current computed from a spinor
  satisfying the Dirac equation in that same torsion background) has a
  solution with `2t-1 != 0`, whose SIGN is fixed by the chirality
  input, and this solution is not simply `t=1/2` (zero torsion,
  trivially self-consistent since zero current sources zero torsion).
- **Measurable outcome:** an explicit evaluation of the axial current
  on this project's own zero modes, an explicit statement of the ECSK
  algebraic torsion equation for this background, and the fixed-point
  solution set.

**If the axial current vanishes identically on the homogeneous
background (by symmetry, the same way round80's orbifold mechanism
died forcing t=1/2), or if the self-consistency equation has a
solution for every t (no selection content), this round should report
that honestly as a kill -- NOT force a positive result. This is
explicitly permitted and is not a failure of the round.**

## Falsifiable claim

With an Einstein-Cartan (ECSK) action on `M4 x S3 x S6`, the algebraic
torsion field equation, evaluated self-consistently on this project's
own `S6`-twisted zero modes, admits a solution with `2t-1 != 0` on the
`S3` factor, whose SIGN is fixed by L5's already-certified
`sign(ind)=+1` chirality result -- distinguishing this from a merely
bosonic curvature-plus-torsion functional (round72's E8 gate, which
this claim does NOT reduce to and must explicitly distinguish itself
from, or concede that it does and report the kill).

## Kill criterion (two live branches -- per C132's sketch; a third branch is explicitly UNREACHABLE by construction, do not manufacture a way to make it fire)

FALSE if:
(a) the axial current vanishes identically on the homogeneous
background (this would force `t=1/2` via the algebraic torsion
equation, exactly the same failure mode as round80's already-killed
orbifold mechanism -- if this happens, report it as a genuine kill, not
as an inconclusive result);
(b) the self-consistency equation has a solution for EVERY value of
`t` (i.e. it is satisfied identically, carrying zero selection
content -- this would make the claim's own predicate vacuous).

**NOT a live branch, stated explicitly so it is not manufactured:**
"no solution at all" is unreachable by construction, because `t=1/2`
with zero axial current is always a trivial solution of the algebraic
torsion equation (zero sourcing zero). Do not report this branch as
having fired; if your computation appears to show no solution exists
anywhere, that indicates a computational error, not a genuine result --
find and fix the error, or report the computation as blocked, but do
not claim kill-branch (c).

## Mandatory positive control

Reproduce the standard flat-space (Minkowski, no S3/S6) ECSK
four-fermion contact term's known sign and coefficient after
integrating out the algebraic torsion. Cite the standard result
(search the literature, retrieve and read a primary or well-established
secondary source this session, do not rely on memory alone) and show
your machinery reproduces it. If your machinery cannot recover this
textbook result, the round cannot be trusted on the novel S3/S6
computation -- report this as a blocking failure, do not proceed past
it.

## Mandatory negative control

Re-run the identical self-consistency computation with a NON-CHIRAL
(vector-like) fermion content substituted for this project's actual
chiral zero-mode content. The sourced torsion must vanish, or lose its
sign preference, in this control case. If it does not -- if the
machinery still produces a sign-preferring torsion even for vector-like
content -- the computation is not actually sensing chirality, and the
whole result is void. Report this honestly.

## Scoping discipline (explicit, because C132's sketch names this as essential)

Confine the computation to the `S3` torsion equation, with `S6`
entering ONLY through its already-certified chirality (L5/G74B) and
multiplicity (2 per C64) -- do not attempt to derive a torsion equation
on `S6` itself or couple the two factors' torsion dynamics together.
**If this scoping turns out to be impossible -- if the S3 torsion
equation cannot be meaningfully isolated from S6 without additional,
uncertified assumptions -- STOP and report this explicitly as a
scoping failure, rather than silently growing the computation's scope
to make it work.** This is the single most likely way this round
quietly turns into an uncontrolled expansion; watch for it actively.

## Gate fields this round bears on

**F6 ("Background equations") for the first time with a named, derived
EOM** -- F6's own pass criterion requires "an actual action principle
is named... and its equations of motion are derived or cited, not
merely gestured at." If this round succeeds even partially (reaches a
genuine, checkable EOM, whether or not it selects `t`), it is
informative for F6 regardless of the Zero-Signal-Gate/kill-criterion
outcome on the narrower t-selection question -- state this distinction
clearly in the final decision.md. Also touches F4, F5 by citation.

## What this round does NOT show

- Does NOT claim the resulting torsion equation, even if it selects
  `t in {0,1}`, constitutes a full 13D parent action -- it is a
  partial-EOM result for one sector.
- Does NOT reopen C123-C133's verdicts.
- Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda =
  FREE_COUPLING_PARAMETER`, or `safe_for_runtime = False`.
- Does NOT close H1c, OB1, or round95's own diagnosed gap even if it
  succeeds -- it would supply ONE more piece (an S3-side selection
  mechanism), not the S6-channel pairing round95 itself asks for.
- Does NOT solicit Tom Lawrence's Part 5.

## Verification plan

- Read all cited files in full before any computation, especially
  round72's actual E8 gate (verify which table is live vs superseded
  directly, per the C132 precedent of getting this wrong once already).
- Literature-first for the ECSK algebraic torsion equation's standard
  form and the flat-space four-fermion coefficient (positive control) --
  retrieve and read primary or well-established secondary sources this
  session.
- Perform the axial-current computation on this project's own
  certified zero modes explicitly, shown not asserted.
- Run both mandatory controls (positive: flat-space recovery; negative:
  non-chiral content) before reporting any positive result.
- Cite `[VERIFIED]`/`[CITED]`/`[INFERRED]`/`[SPECULATIVE]` throughout,
  per this project's evidence-marker discipline. Round90's anomaly
  coefficients, if touched, are `[WEAK]` not `[DOCS]` (per round95's
  own assumptions section).
- FL Step 8a skeptic pass (context-blind: only claim.md + decision.md +
  code, no session history). Given the genuine difficulty and novelty
  of this round (first F6 attempt with a derived EOM, and explicit
  prior confusion in C132 about round72's own live status), run a
  SECOND independent pass with a differently-worded prompt
  (Paraphrase-Sensitivity Probe) regardless of the first pass's
  verdict, unless the first pass returns a clean, unqualified
  confirmation with zero findings -- matching this session's
  established practice for consequential, first-of-their-kind rounds.
