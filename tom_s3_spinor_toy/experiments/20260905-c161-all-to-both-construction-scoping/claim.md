---
# C161 Claim — scoping the cheapest genuine test of the "all->both"
# channel-uniform coupling pattern, before any new 13D construction attempt

**Date:** 2026-09-05
**FL tier:** [x] Full (touches OB1's central blocker; AI-generated candidate
observation below requires pre-gates)
**Question type:** [x] descriptive (does a specific already-built
construction, re-read correctly, actually derive a specific structure, or
does it not)

**Mode:** This file is a SCOPING document only. Per the orchestrating
session's explicit instruction: no computation, no construction attempt, no
decision.md. It exists to satisfy AOG-5 (independent motivation) before any
future round spends real effort on OB1/H1c's "all->both" target, and to name
the single cheapest next test.

---

## 0. What "all->both" is, precisely (so this file has a fixed target)

`experiments/20260902-c133-symmetry-ladder-pairing-space/decision.md` SS9
(lines 584-616): at the triality-`Z3`-symmetric rung of its symmetry ladder,
the S6-channel<->S3-sector coupling is `Phi = 1_F (x) (lambda_0 w_0 + lambda_1
w_1)`, with `w_0, w_1` spanning the two S3 `t`-sectors (cited to C38). The
full coupling space at that rung is a 2-parameter continuum
(`lambda_0, lambda_1`); imposing a nonzero/zero SUPPORT convention on top of
it gives exactly 3 patterns: `all->t=0` (`lambda_1=0`), `all->t=1`
(`lambda_0=0`), `all->both` (`lambda_0<>0 AND lambda_1<>0`, with the
`Z3`-forced equal-coefficient constraint meaning every one of the 3 channels
carries the SAME `(lambda_0,lambda_1)` pair, not merely that it is non-empty
in aggregate).

C133 SS8a states only that `all->both` is "the assumed Pati-Salam content"
and a "consistency filter" survivor -- explicitly NOT a differentiator, NOT
derived, NOT established. This file's target is precisely: is there a
cheaper-than-a-brand-new-13D-construction way to move `all->both` from
"assumed input, disclaimed" toward either (a) a genuinely DERIVED consequence
of some already-built geometric object in this project, or (b) a
necessary-condition failure that would tell us `all->both`, as commonly
invoked, is degenerate/vacuous once actual coefficients are extracted.

---

## Prior Result Gate (MANDATORY -- filled BEFORE any future round computes
anything)

1. **Exact claim to check.** Between 2026-09-02 and 2026-09-05 this project
   ran a dense pipeline (C132-C137, plus C159 on 2026-09-05) that is the
   direct, complete prior-art record for this question. Read in full this
   session:
   - `experiments/20260902-c132-13d-parent-action-survey/decision.md`
     (1038 lines) -- 18 candidate mechanisms generated, 15 proposed, ranked
     by CDT. Top mechanisms for producing a genuine (not merely postulated)
     pairing structure: `P2` (ECSK torsion, tied CDT 6.5), `P14` (joint 13D
     generalized-Killing-spinor constraint, tied CDT 6.5), `P4` (diagonal Z3
     orbifold, CDT 6.0), `P5` (gauged Spin(8)/SO(4)^2, CDT 4.3).
   - `experiments/20260902-c133-symmetry-ladder-pairing-space/decision.md`
     (916 lines) -- builds the `{all->t=0, all->t=1, all->both}` support-
     pattern space explicitly (SS9), two independent context-blind skeptic
     passes, both `[WEAKENED]`.
   - `experiments/20260902-c134-ecsk-torsion-auxiliary/decision.md` --
     **`P2` KILLED**: `KILL_BRANCH_A_FIRES__SOURCE_VANISHES__t_FORCED_TO_ONE_HALF`.
     The axial-current source this project's own zero modes would supply
     vanishes identically; ECSK forces `t=1/2` for every input, i.e. the
     opposite of a `t in {0,1}` selection.
   - `experiments/20260902-c135-triality-vs-round119-sign-structure/decision.md`
     -- closes `pearl_registry` row 40's own `next_check` (whether the
     explicit triality `Z3` matches round119's `(Gamma_A,Gamma_B)` sign
     structure): **NO** -- there are only 2 distinct sign patterns among the
     3 channels (`8_v` and `8_c` share one), so a `Z3` cannot cyclically
     permute them. This weakens `P5`'s specific realization (using block
     chirality to assign a `t`-sector) without fully killing the broader
     `P5` idea (a genuinely non-`G2` structure could still exist elsewhere).
   - `experiments/20260902-c136-joint-killing-spinor-constraint/decision.md`
     -- **`P14` KILLED** on kill-branch (b): the three channel columns of a
     genuinely-posed joint generalized-Killing-spinor constraint on the
     frozen `M4xS3xS6` background come out IDENTICAL (channel-uniform), for
     a reason traced to already-certified content (E-L3B's identical
     connections + L5's uniform chirality). Two independent context-blind
     skeptic passes, both `[FALSIFIED]`, both concordant after repair: the
     kill is a `[RESTATEMENT]` (round114's own "one-line derivable from a
     cited corollary" criterion fires on the round's OWN headline), not
     independent evidence. **This is the single most load-bearing prior
     result for this file** -- see SS1 below.
   - `experiments/20260902-c137-fermion-condensate-torsion/decision.md` --
     **`P3` REJECTED**: no dynamically-derived condensate is available in
     this project's frozen content (no SUSY, no gauge multiplet, no confining
     sector; G97 already closes the SU(4) realization needed for the
     standard derivation to transfer).
   - `experiments/20260905-c159-round95-link-scoping-parity-check/decision.md`
     -- the parity argument that makes an EXCLUSIVE 3-channels-to-2-sectors
     pairing arithmetically impossible for `N_gen=3` (odd), and the specific
     trace of `all->both` back through E17 (a labeled, BLOCKED hole, not a
     live positive candidate) to C132/C133 (a concrete, later, on-the-record
     structure).
   - `PARENT_ACTION_GATE.md` F4 (the authoritative gate-checklist, read in
     full, lines 237-540+): "must state the specific action/symmetry/
     anomaly/topology principle that selects a specific `t` value... rather
     than leaving it as an arbitrary choice." No candidate in the F4 history
     has ever passed this for an ASYMMETRIC selector; C132-C137 additionally
     show every attempted GENUINE mechanism (not merely a postulated
     symmetry ladder) that has actually been built (`P2`, `P3`, `P14`)
     either dies or, when it survives, comes out channel-UNIFORM
     (C136/`P14`) -- i.e., structurally consistent with `all->both`, not
     with an exclusive selector.

2. **Registry grep, done by hand this session** (`all->both`, `all→both`,
   `non-exclusive`, `channel-uniform`) against `null_results/INDEX.md`,
   `parked/INDEX.md`, `pearl_registry/INDEX.md`, `OPEN_BLOCKERS.md`,
   `PARENT_ACTION_GATE.md`, and the full `experiments/` tree: hits are
   confined to `pearl_registry/INDEX.md` (the C133/C159-sourced rows already
   read above), `OPEN_BLOCKERS.md` (mirrors PARENT_ACTION_GATE.md's F4
   content), and the C132/C133/C136/C159 decision.md files themselves.
   **No round has ever targeted "all->both" AS THE CONSTRUCTION GOAL.**
   Every occurrence found is either (a) C133's own abstract symmetry-ladder
   argument for why it survives as a consistency-filter non-exclusion, or
   (b) C136's construction, which targeted an ASYMMETRIC pairing (`P14`) and
   only incidentally produced a channel-uniform result as its KILL, never
   reframed as evidence FOR `all->both`. **This asymmetry -- 130+ rounds
   attacking the (now parity-impossible) exclusive target, zero rounds
   attacking "does a real construction derive `all->both`'s actual
   coefficients" as the target -- is itself this file's AOG-5 justification;
   see SS1.**
3. `git log --all -S"all->both" -S"all_to_both" -G"lambda_0.*lambda_1"`:
   [ ] to be run by the executing agent -- this file's own grep above did
   not use git pickaxe, only a working-tree grep; re-verify independently,
   do not trust this paragraph alone.
4. Primary source re-read: [x] done this session -- C132, C133, C134, C135
   (first 60 lines), C136 (in full), C159 (in full) all read directly via
   `Read`, not from summary. C137's verdict string read directly.
5. **Status:** [x] NEW as a construction TARGET (see item 2's asymmetry
   finding) -- but built entirely from already-completed, already-verified
   prior rounds. This file itself proposes no new physics; it identifies
   which already-existing artifact (C136's script + C133's language) can be
   cheaply recombined to produce a genuine test, before any brand-new 13D
   derivation is attempted.

---

## Explicit AI-Hypothesis Pre-Gates (mandatory -- this file's central
observation, SS1 below, is this session's own synthesis across two prior
rounds' text, not from primary literature)

**Step -4, Source Trace.** Every input fact used in SS1 is this project's
OWN internal, already-certified result, re-cited at file:line from its own
decision.md files (quoted directly above, not paraphrased from memory) --
not an external claim needing literature verification. The one external
citation load-bearing here (AHL2023's definition of a generalized Killing
spinor, `nabla^g_X psi = A(X)*psi`, `A` symmetric) was itself already
`[VERIFIED-tool]`-checked by C136 against the source PDF in-repo
(`Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf`) -- re-verify that
citation, do not re-trust it from this file alone.

**Step -3, Novelty Check.** Searched `null_results/INDEX.md`, `parked/
INDEX.md`, `pearl_registry/INDEX.md`, `OPEN_BLOCKERS.md`, and the full
`experiments/` tree for "does C136's construction, mapped into C133's
Phi-language, derive nonzero lambda_0 AND lambda_1" -- **0 hits.** This
specific recombination has not been proposed or attempted. The two
ingredients (C133's Phi parametrization, C136's joint-constraint solution
set) were built 3 days apart in the same C123-C137 pipeline, by rounds that
cite each other's OTHER findings (C136 cites C132's P14 spec and C134's
non-transfer result) but never connect C136's own solution-space output back
to C133's own explicit coupling-space language. **This is exactly the kind
of connection the project's own methodology names as cheap and
high-value**: recombining two already-certified artifacts, not inventing a
third. Per this project's brand-new 5-gate "discovery" mandate (C157/C158,
2026-09-05): the expected disposition, if this recombination is attempted
and succeeds, is likely closer to "a small, genuine addition" than "pure
discovery" (in the register of C159 SS4 item (d): "a minor genuine addition...
though it is a small, mechanical accounting step") -- flagged so a future
executing agent does not oversell a positive result.

---

## Estimand

**Population:** This project's own already-built joint generalized-Killing-
spinor construction (`c136_joint_killing_spinor_check.py`, C136's SS4/SS5,
the `results_c136.json` `E_table_3x2` object), re-read against C133's own
explicit `Phi = 1_F (x) (lambda_0 w_0 + lambda_1 w_1)` coupling
parametrization (SS9).

**Intervention:** Extend (not replace) C136's existing script to compute the
actual `(lambda_0, lambda_1)` coefficients the joint constraint's solution
set implies for the `t=0` and `t=1` sectors, per channel -- the quantity
C136 itself left `[UNKNOWN]` for the S6 half (`eta_6` was never built; the
S3 half's `alpha` values ARE already computed in C136 SS5's `3x2` table).
This requires building only the missing S6-side ingredient C136 SS8 names
as assumption 6 ("the twisted S6 operator was not built") -- NOT a new 13D
action, NOT a new symmetry postulate, only the piece C136 already flagged as
its own open gap.

**Comparator:** The status quo, where `all->both` is cited (C133 SS8a, C159
SS1f) as "the assumed Pati-Salam content" with no computed coefficients
behind it at all -- an unexamined placeholder, not a derived or even a
partially-derived structure.

**Endpoint:** Do the computed `(lambda_0, lambda_1)` per channel come out
(a) both nonzero and equal across all 3 channels (a genuine, if restatement-
tier, DERIVATION of `all->both`'s specific support pattern from a real
geometric equation, upgrading its evidence tier); (b) one identically zero
(the construction actually derives `all->t=0` or `all->t=1`, contradicting
the "both" label that has been assumed); or (c) both identically zero (the
construction gives no coupling at all, i.e. `all->both` as invoked in this
project is vacuous and the placeholder should be retired, not merely
disclaimed)?

**Summary measure:** A 3x2 table of computed `(lambda_0, lambda_1)`-style
coefficients (or their C136-native analogue, the per-channel, per-`t` `alpha`
values already in `E_table_3x2`, extended to include the S6 factor), plus a
verdict: PROMOTE-AS-DERIVATION / NULL-DEGENERATE / ALREADY-KNOWN.

**MCID:** Not applicable -- structural (nonzero-vs-zero, equal-vs-unequal)
question, not a magnitude estimate.

**Intercurrent events (ICE):** If building the missing S6 twisted operator
(assumption 6 in C136 SS8) turns out to require re-deriving nearly-Kahler
`S6` machinery not already in this repo (a genuinely new, expensive
sub-derivation rather than a cheap extension), that is an ICE this round
must name explicitly and STOP rather than silently expanding scope --
exactly the "if scoping is impossible, stop and say so rather than grow"
discipline C132's own Sketch B names for a sibling case.

---

## Claim

**Falsifiable statement:** When C136's already-verified joint generalized-
Killing-spinor constraint (kill-branch (b), channel-uniform) is extended to
actually compute its implied S3-sector coupling coefficients per channel
(the piece C136 left `[UNKNOWN]`), the result is EITHER (a) a genuine,
nonzero, equal-across-channels `(lambda_0, lambda_1)` pair -- the first
actual derivation of `all->both`'s specific support pattern from a real
(if restatement-tier) geometric construction, rather than a bare assumption
-- OR (b)/(c) a degenerate/vacuous coupling, which would mean `all->both` as
currently invoked in this project's own registries has never actually been
shown to correspond to a nonzero physical coupling at all.

---

## Kill criterion (MANDATORY -- filled BEFORE any future round computes)

| Outcome | Verdict |
|---|---|
| Both `lambda_0` and `lambda_1` come out nonzero and equal across all 3 channels, computed (not assumed) from the extended construction | PROMOTE-AS-DERIVATION -- upgrades `all->both` from "assumed input" ([WEAK]/disclaimed per C133 SS8a) to `[VERIFIED-tool, RESTATEMENT-TIER]` (per C136's own F7 precedent: likely still one-line derivable from E-L3B+L5, so tier the claim honestly, do not oversell as new physics) |
| One of `lambda_0, lambda_1` comes out identically zero | NULL-CONTRADICTS-LABEL -- the construction actually derives `all->t=0` or `all->t=1`, not `all->both`; report exactly which, and flag every place in the project (C133 SS9, C159 SS1f) that has cited `all->both` as the anomaly-condition survivor, since those citations would need a caveat |
| Both come out identically zero | NULL-DEGENERATE -- `all->both` as invoked is vacuous; the placeholder should be retired from PARENT_ACTION_GATE.md F4's live candidate list, not merely disclaimed as "assumed, not derived" |
| Building the missing S6 twisted operator (assumption 6) requires a genuinely new, expensive sub-derivation not already available in this repo | INCOMPLETE-MACHINERY -- STOP, name the specific missing ingredient, do NOT silently expand into a full new 13D construction under this file's cheap-test framing |
| The specific recombination (C136 output x C133 language) is found to already exist somewhere once the executing agent re-runs Prior Result Gate item 3 (git pickaxe) | ALREADY-KNOWN -- cite it, close this round immediately |

**Explicit escape route:** if the coefficient computation resolves cleanly
(any of the first three outcomes) within one session using only C136's
existing script plus the missing S6 piece (assuming that piece is itself
cheap -- see INCOMPLETE-MACHINERY branch), STOP. Do NOT proceed from there
to a brand-new, from-scratch 13D parent-action derivation in the same round.
That is a separate, much larger undertaking (see "Cost estimate" below) and
deserves its own Prior Result Gate, estimand, and kill criterion once this
cheaper test's outcome is known.

---

## Why this is the cheapest first differentiating test (CDT protocol)

- **Differentiation:** distinguishes "all->both is a real, computed
  consequence of an already-built geometric object" from "all->both is an
  unexamined placeholder" -- a distinction that currently does not exist
  anywhere in this project's registries.
- **Kill power:** genuinely can fail (NULL-CONTRADICTS-LABEL or
  NULL-DEGENERATE are live, plausible outcomes -- C136 itself never checked
  whether its channel-uniform result was nonzero in aggregate, only that the
  three channels agree with EACH OTHER).
- **Rescue power:** if it fails, it does not waste the effort -- a
  NULL-DEGENERATE result is itself informative and cheap to report; it
  redirects effort away from `all->both` and toward the Relaxation Map's
  actual untried route-(b)/(c) candidates (`P4`, `P13`, `P8`) instead of
  continuing to treat `all->both` as a safe fallback.
- **Non-circularity:** does not assume the conclusion -- the coefficients
  are computed from C136's already-existing, already-skeptic-vetted
  construction, not reverse-engineered to match "all->both."
- **Reuse value:** high -- resolves `pearl_registry` row 40's adjacent open
  thread (C133's own V4 Relaxation Map item, partially addressed by C135)
  and directly informs any future F4/F6 gate-fill attempt.
- **Cost:** LOW relative to a new construction -- reuses `c136_joint_
  killing_spinor_check.py` and `results_c136.json` in full; the only new
  ingredient is the S6-side twisted-operator piece C136 already named as
  its own limitation (assumption 6), NOT a new symmetry postulate or a new
  13D action.

---

## Cost estimate, stated honestly (per the orchestrating session's explicit
instruction not to undersell the risk)

**The cheap test above (this file's actual recommendation): plausibly
1 round**, IF the missing S6 twisted-operator piece is itself cheap to add
(nearly-Kahler `S6` spin geometry with the twist bundle `E` this project
already uses elsewhere, e.g. G73/G74A/G74B/E-L3B's own machinery -- these
are already-built ingredients in this repo, not new physics). If that
assumption is wrong, the INCOMPLETE-MACHINERY branch above fires and this
file's own kill criterion requires stopping rather than silently absorbing
the cost.

**A brand-new, from-scratch 13D construction actually deriving `all->both`
(or any exclusive alternative) from first principles, independent of this
cheap test's outcome: this is realistically NOT a 1-3 round test.** The
honest comparison class is this project's own H1c/OB1 search history: 130+
rounds (round62 through C138) have been spent on exactly this class of
question, and within just the most recent, most concentrated attempt
(C132-C137, 6 rounds over 2 days) every one of the three "genuine mechanism"
candidates C132 itself ranked highest (`P2`, `P3`, `P14`) was tried and
killed or rejected, and the fourth (`P5`) was materially weakened (C135).
What remains untried in C132's own Relaxation Map (`P4` diagonal Z3
orbifold, `P13` boundary/defect terms, `P8` S3-bundle-over-S6, `P1`
torsionful spectral action, `P6`/`P7`/`P10`/`P12`) were each already priced
by C132 as more expensive, more postulate-heavy, or carrying named AOG-5
circularity risk than the four just exhausted. A genuinely new construction
attempt from here should therefore be budgeted like the C132-C137 sequence
itself: multi-round (plausibly 5-15+ rounds), with a non-trivial chance of
ending in another KILLED/REJECTED verdict, exactly the pattern of every
attempt so far. **Do not undersell this**: the "low-hanging fruit" reading
of C132's own CDT ranking has now been picked essentially clean.

---

## What this does NOT mean

- Does NOT itself claim `all->both` is or is not physically realized --
  this file proposes a test, computes nothing, and reaches no verdict.
- Does NOT mean the cheap test, even if it succeeds fully (PROMOTE-AS-
  DERIVATION), closes H1c or OB1 -- per C136's own F7 precedent, a result
  one-line-derivable from already-certified content (E-L3B + L5) is a
  restatement-tier upgrade to `all->both`'s evidence marker, NOT a new
  physical mechanism and NOT a parent action satisfying PARENT_ACTION_GATE
  F4/F6.
- Does NOT mean the untried Relaxation Map candidates (`P4`, `P13`, `P8`,
  `P1`, `P6`, `P7`, `P10`, `P12`) are ruled out or deprioritized by this
  file -- they remain the actual candidates for a genuinely NEW mechanism,
  should the user choose to commit to the expensive path instead of the
  cheap test.
- Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda=
  FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
- Does NOT touch OB4, OB11, OB12, OB13, OB14, or the C144-C158 methodology
  thread.
- Does NOT edit `OPEN_BLOCKERS.md`, `PARENT_ACTION_GATE.md`,
  `pearl_registry/INDEX.md`, or `preprint.tex` -- registry updates are the
  orchestrating session's, per C124-C159 precedent.
- Does NOT solicit Tom Lawrence's Part 5.
- Does NOT commit to any further round regardless of outcome -- this is a
  scoping document, not a pre-authorization to proceed.
