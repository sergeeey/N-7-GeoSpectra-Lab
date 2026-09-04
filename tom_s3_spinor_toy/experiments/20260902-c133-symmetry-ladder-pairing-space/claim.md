# C133 claim -- which symmetry assumption buys which reduction of the
# S6-channel <-> S3-t-sector pairing-rule space? (C132's top-ranked
# candidate P0, ready-to-run sketch A)

## Mode declaration

**Convergent-mode round** (unlike C132, which was divergent/scouting).
This round tests ONE specific, pre-registered claim to completion --
promote, weaken, or kill it -- following this project's standard FL
Full-Ladder discipline used throughout C123-C132.

## Question type (EstimandOps L0)

**Descriptive.** Not causal, not predictive. The question is: given this
project's already-certified branching data (`8_v`, `8_s`, `8_c` under
`G2` and `Spin(8)`, and the explicit triality element constructed in
`pearl_registry` row 33), what does invariance under each of three
progressively larger symmetry groups (`G2` alone; `Spin(8)`; `Spin(8)`
plus the explicit triality `Z3`) actually permit for a hypothetical
coupling between the S6 triality-channel label and the S3 connection-
family sector -- stated as a sequence of Schur-lemma computations on
already-certified representation content, not a claim about which
coupling is physically realized.

## Background, stated honestly before any computation

Read, in full, before doing anything else:
- `experiments/20260902-c132-13d-parent-action-survey/decision.md`,
  especially the `P0` candidate write-up (search for "### `P0`"), Section
  2 ("The two obstructions that organize the space"), Section 6's
  "Sketch A" (this claim.md is built directly from that sketch -- follow
  its kill criterion and negative control exactly, do not weaken them),
  and Section 7 (the skeptic pass that corrected the first draft's `P0`
  -- read this carefully, it documents a real error already made once on
  this exact question: the first draft of C132 claimed `G2`-equivariance
  FORCES channel symmetry; this is FALSE, `G2` acts trivially on the
  channel label and therefore constrains nothing about it. Do not repeat
  this error.)
- `pearl_registry/INDEX.md` rows 33, 34, 37 (the explicit triality
  construction, the G2-level channel-mixing counterexample, and the
  G86B Hopf/Liouville argument) -- read these directly, do not rely on
  C132's paraphrase alone.
- `null_results/INDEX.md` entry `G44` (triality collapses under bare
  `G2`: `8_v|_G2 = 8_s|_G2 = 8_c|_G2 = 7+1`).
- `experiments/20260717-round95-l5-tension-check/decision.md` Section 3
  (the `n_L = n_R` cubic-anomaly arithmetic this round's own anomaly
  step, if included, must not overclaim beyond -- C132 already found the
  anomaly step does NOT discriminate among the three symmetry rungs, it
  only excludes one-sector assignments for every `N_gen >= 1`; do not
  re-claim discriminating power for it without a genuinely new argument).
- `experiments/20260901-c125-full-gauge-equivalence-gate/decision.md`
  (C125 left the relative M4-S6 orientation `UNDECIDED`, gated on
  round95 -- do NOT claim a "3 elements -> 2 up to relabelling"
  reduction; C132's first draft made exactly this error and withdrew it).

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(exists entity) AND (exists
falsifiable predicate) AND (exists measurable outcome)`, all three
required.

- **Entity:** the symmetry ladder itself -- three named groups (`G2`,
  `Spin(8)`, `Spin(8)` extended by the explicit triality element of
  `pearl_registry` row 33) acting on the combined channel bundle
  `E_v (+) E_s (+) E_c` over `S6`.
- **Falsifiable predicate:** each rung buys EXACTLY the stated reduction
  -- `G2`: no constraint; `Spin(8)`: block-diagonal only (independent
  per-channel coefficients allowed); triality: equal per-channel
  coefficients forced.
- **Measurable outcome:** three explicit Schur-lemma computations on
  already-certified branching data, each either confirming or refuting
  its stated rung.

## Falsifiable claim

On the frozen background, `G2`-equivariance imposes NO constraint on the
channel-dependence of a hypothetical coupling between the S6 triality
label and any other structure; `Spin(8)`-equivariance forces block
diagonality (no channel mixing) but still permits independent
per-channel coefficients; and ONLY invariance under the explicit
triality `Z3` element forces equal per-channel coefficients, reducing
the abstract pairing-rule space to exactly `{all-to-t=0, all-to-t=1,
all-to-both}`.

## Kill criterion (three independent ways it can fire -- per C132's sketch, do not weaken)

FALSE if:
(a) a `G2`-equivariant channel-mixing map does NOT exist (this would
contradict `pearl_registry` row 34's explicit construction -- re-verify
that construction directly, do not just cite it);
(b) `Hom_{Spin(8)}(8_v, 8_s) != 0` (this would contradict Schur's lemma
applied to inequivalent irreducible representations -- if `8_v` and
`8_s` are NOT actually inequivalent as `Spin(8)`-representations, the
whole block-diagonality rung fails and must be reported as failing, not
patched);
(c) the specific triality element constructed in `pearl_registry` row 33
does NOT actually conjugate the three blocks into one another (re-derive
this directly from Baez's `S3 subset F4` construction cited there, do
not assume the prior round's construction was correct without checking).

## Mandatory negative control (per C132's sketch -- run this, do not skip it)

Run the identical three-rung argument on a case where the answer is
known independently: three MUTUALLY EQUIVALENT irreducible
representations (not `8_v/8_s/8_c`, an actual known equivalent triple).
Even `Spin(8)`-level equivariance should PERMIT mixing in that control
case (Schur's lemma does not force block-diagonality between equivalent
irreps -- it permits an arbitrary linear combination). If this round's
machinery "proves" block-diagonality in the control case too, the
computation is not actually sensing inequivalence, and the whole result
is void -- report this honestly, do not paper over it.

## What this round must NOT claim (explicit, because C132's first draft made these exact errors)

- Must NOT claim the anomaly/cubic-`SU(4)` step discriminates among the
  three symmetry rungs -- round95's own `n_L=n_R` arithmetic excludes
  one-sector assignments for EVERY `N_gen >= 1`, so it is a consistency
  filter, not a differentiator, and its survivor (`all-to-both`, i.e.
  standard Pati-Salam generation content) is the assumed input, not a
  new prediction.
- Must NOT claim a "3 elements reduces to 2 up to `t<->1-t` relabelling"
  -- C125's own verdict is the opposite (`t=0` vs `t=1` remains a
  genuine physical choice), and the relevant orientation question is
  explicitly `UNDECIDED`, gated on round95.
- Must NOT claim the triality-`Z3` rung is free or derived -- it is an
  explicitly assumed symmetry of a hypothetical parent action, and this
  round must state plainly that it draws on the same un-derived
  fiber-`Spin(8)`/triality credit line that `N_gen=3` itself already
  rests on (G102) -- naming this shared dependence explicitly is part of
  this round's own deliverable, not an incidental caveat.
- Must NOT tag round90's anomaly coefficients as `[DOCS]` -- round95's
  own "Assumptions carried, unresolved" section tags them `[WEAK]`
  (Wikipedia + an unverified modern-paper cluster); carry that tag
  forward accurately.

## What this round does NOT show

- Does NOT supply or verify any actual parent action.
- Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda=
  FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
- Does NOT close H1c, OB1, or round95's own diagnosed gap.
- Does NOT reopen C123-C132's verdicts.
- Does NOT solicit Tom Lawrence's Part 5.

## Verification plan

- Read all cited files in full before any computation.
- Perform the three Schur-lemma computations explicitly (symbolic or by
  hand, shown not asserted), plus the mandatory negative control.
- Cite `[VERIFIED]`/`[CITED]`/`[INFERRED]`/`[SPECULATIVE]` per this
  project's evidence-marker discipline throughout.
- FL Step 8a skeptic pass (context-blind: only claim.md + decision.md +
  any code, no session history) before this round's finding enters the
  permanent record. Given this is a cheap, narrow, mostly-symbolic round
  (not a high-stakes PROMOTE closing a major Relaxation Map item), a
  single pass suffices unless it finds something that changes the
  verdict's direction, in which case run a second, differently-worded
  pass per this project's established Paraphrase-Sensitivity Probe
  practice.
