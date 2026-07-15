# Round63-WrappedS3InstantonChannel Decision — PROMOTE (corrected), same qualitative finding, different formula

**Date:** 2026-07-15
**Verdict: PROMOTE [WEAKENED, CORRECTED]** — a genuine EFT-valid minimum exists
for a bounded range of the free normalization, systematically ~2-14% above
the established constant-λ result. Route A's own draft decision (below,
preserved) correctly flagged "Step 8a skeptic review not yet performed" as
outstanding — that review ran, found a real dimensional-consistency error in
BOTH routes' shared substitution formula, and this decision replaces the
draft with the corrected result.

This round is a textbook case of the Skeptic Response Matrix working as
intended: FALSIFIED sub-finding → FIX → independent re-verification → same
qualitative verdict, corrected numbers.

---

## What happened (full honest sequence)

1. **claim.md** froze a substitution: replace the constant $\lambda$ in
   $f(\rho_6)=1-\exp(\lambda(1/\rho_6^{*2}-1/\rho_6^2))$ with
   $\lambda(\rho_6)=c_{\mathrm{eff}}\rho_6^3$ — using eq:slope2-exp's own
   quantity $c(C')^3\rho_6^3$ directly as "$\lambda(\rho_6)$".
2. **Both routes** (independent methods: symbolic critical-point solve;
   coarse-to-fine numerical grid search) faithfully implemented this exact
   substitution, both found a genuine EFT-valid minimum for
   $c_{\mathrm{eff}}\in(0,\approx1.79)$, $\rho_{6,\min}\in[1.205,1.336]$
   (2.2%-13.3% above the established $\approx1.179$), and reported
   PROMOTE[WEAKENED] (see Route A's preserved draft decision, appended below).
3. **Skeptic 0** (assigned to re-audit the exact trajectory-substitution
   algebra, given this topic's documented fragility — `null_results/INDEX.md`
   META-C1) caught a real error: $c(C')^3\rho_6^3$ from eq:slope2-exp is
   $\lambda_{\mathrm{geom}}/\rho_6^2$ (the full, already-reduced, dimensionless
   exponent argument of the *simple* ansatz $\exp(-\lambda_{\mathrm{geom}}/\rho_6^2)$)
   — **not** $\lambda_{\mathrm{geom}}(\rho_6)$ itself (dimension length²,
   actually $c(C')^3\rho_6^5$). Both routes' scripts substituted the reduced,
   dimensionless quantity into a slot ($f(\rho_6)$'s own $\lambda$) that
   expects the raw, length²-dimensioned coupling — a genuine dimensional
   inconsistency, the same class of substitution fragility as META-C1's
   original wrong-trajectory error, recurring here as a $\lambda$ vs
   $\lambda/\rho_6^2$ conflation.
4. **Skeptic 1** independently found the G94 cross-check (a secondary,
   bonus part of Route A) rests on an unjustified coincidence (two
   structurally different terms sharing a numerical window by chance, not
   derivation) — correctly did not affect the core verdict, downgrades only
   that side comparison (already flagged as "coincidence-check only" in
   Route A's own draft, §"G94 cross-check" below — skeptic 1 confirms this
   self-assessment was correct).
5. **Skeptic 2**'s own independent check reproduced the *original (flawed)*
   formula's numbers exactly — this is expected and does NOT refute skeptic
   0: skeptic 2 verified the arithmetic of the formula both routes
   implemented, not whether that formula was the physically correct one to
   implement in the first place. A precise re-verification of the wrong
   question is not a defense of the wrong question.

## Independent correction and re-verification (this decision, before writing PROMOTE)

Re-derived the physically consistent embedding directly from the ground-truth
$V_{\mathrm{total}}$ construction (`tests/test_g62_observables.py`, the
actual validated code the $\rho_{6,\min}\approx1.179$ result comes from, not
just the paper's abbreviated $f(\rho_6)$ notation):
$$v_{\mathrm{np}}(\rho_6)=-A_{\mathrm{np}}\exp(-\lambda/\rho_6^2),\qquad
A_{\mathrm{np}}=V_{\mathrm{flux}}\exp(\lambda/\rho_6^{*2})$$
($A_{\mathrm{np}}$ is calibrated once, at $\rho_6=\rho_6^*$, to enforce the
Minkowski boundary condition $V_{\mathrm{total}}(\rho_6^*)=0$). Replacing the
constant $\lambda$ with the $a=3$ channel's own $\rho_6$-dependence
consistently — including inside $A_{\mathrm{np}}$'s own calibration, evaluated
at $\rho_6=\rho_6^*$ via the *same* eq:slope2-exp formula
$\exp(-\lambda(\rho_6)/\rho_6^2)=\exp(-c(C')^3\rho_6^3)$ — gives, after
simplification:
$$f_{a=3}^{\mathrm{corrected}}(\rho_6)=1-\exp\!\bigl(c_{\mathrm{eff}}(\rho_6^{*3}-\rho_6^3)\bigr).$$
This matches skeptic 0's own proposed correction exactly, independently
re-derived here from the ground-truth code rather than taken on the
skeptic's word (agent's VERIFIED = my INFERRED — checked myself before
accepting).

**High-precision (mpmath, 30 digits) recomputation, positive control
($c_{\mathrm{eff}}=0$: $f\equiv0$, correctly degenerate, matches both
routes' own finding at their boundary):**

| $c_{\mathrm{eff}}$ | $\rho_{6,\min}$ | EFT-valid, genuine min ($V''>0$) |
|---|---|---|
| $\to 0^-$ | $1.1997$ | yes |
| $-0.1$ | $1.2027$ | yes |
| $-0.5$ | $1.2180$ | yes |
| $-1.0$ | $1.2550$ | yes |
| bifurcation $\approx-1.2461$ | $1.3400$ | marginal (min/max merge) |
| $<-1.2461$ | none | — |
| $>0$ (any) | none found (scanned to $\rho_6=15$) | — |

**Corrected result: a genuine EFT-valid minimum exists for
$c_{\mathrm{eff}}\in(-1.246,0)$** (negative, not positive as the flawed
formula gave), $\rho_{6,\min}\in[1.1997,1.340]$, closest approach to the
established $1.1791$ is $1.7\%$ (at $c_{\mathrm{eff}}\to0^-$), growing to
$13.6\%$ at the bifurcation.

## Why the qualitative verdict survives the correction (important, not a coincidence)

The corrected and original (flawed) computations agree on every qualitative
feature: a bounded coefficient window (one sign only), a saddle-node
bifurcation at the upper end of that window (not a hard cutoff), a smooth
monotonic $\rho_{6,\min}(c_{\mathrm{eff}})$ dependence, and a systematic
2-14% offset ABOVE (never below, never coincident with) the established
value. Only the SIGN and precise magnitude of the surviving $c_{\mathrm{eff}}$
window changed. This is expected: near $c_{\mathrm{eff}}=0$ both
parametrizations reduce to the same small perturbation up to an overall sign
convention, so the qualitative structure near that shared degenerate point is
robust to exactly the kind of labeling/dimensional error that was caught here
--- but the specific reported NUMBERS from the original routes (positive
$c_{\mathrm{eff}}$ range, that exact $[1.205,1.336]$ interval) are superseded
by the corrected values above and must not be cited on their own.

## Kill Analysis

**What is killed:** the specific claim, as both routes originally reported
it (positive $c_{\mathrm{eff}}$, $[1.205,1.336]$) — superseded by the
dimensionally-corrected computation above, not a valid standalone result.

**What survives:** the qualitative physics finding — the $a=3$
wrapped-$S^3$-instanton channel, correctly embedded, IS a well-posed,
EFT-valid, genuinely $\rho_6$-dependent candidate for $\lambda_{\mathrm{np}}$'s
origin. It does not reproduce the established constant-$\lambda$
$\rho_{6,\min}\approx1.179$ exactly, but predicts a nearby, structurally
distinct family systematically 1.7%-14% higher, for a bounded coefficient
range with one definite sign. This closes the abstract's own "not computed"
gap for the $a=3$ channel honestly: computed, and it is a **live geometric
candidate**, not a null result like G83-G86B, but also not an exact match to
the zero-fit value.

**What remains genuinely open:** $c_{\mathrm{eff}}$ (equivalently the
original $c$ in eq:buckingham-pi for $a=3$) is a free normalization, exactly
like $\lambda$ was before this round — this round tests one functional FORM,
it does not fix a numerical value. The G94 cross-check (Route A, downgraded
per skeptic 1) does not provide an independent fix for $c_{\mathrm{eff}}$;
that remains a separate open question.

## Pearl (registered in pearl_registry/INDEX.md)

Substituting a "running" (position-dependent) coupling into a formula whose
normalization constant was calibrated via a boundary condition using the
OLD, constant value of that same coupling is a specific, recurring class of
error — the boundary-calibration must be re-evaluated using the SAME running
functional form at the boundary point, not left at its old constant-coupling
value. This is a distinct, useful specific case of the general lesson (fix
one assumption at a time, re-verify the whole formula, not just the changed
term) already partially covered by this project's Minimal Relaxation Rule,
worth naming explicitly since it recurred here in a new guise.

## Recommendation

1. Do NOT cite the original routes' raw numbers standalone — corrected
   values in the table above are authoritative.
2. Optional preprint update (not applied here, needs separate confirmation):
   the abstract/Open Problems $\lambda$-origin entries could note the $a=3$
   channel is now computed (closing "not computed"), with the honest
   qualitative finding (live candidate, systematic 1.7-14% offset, one free
   normalization sign) — this is a real, citable result, unlike G83-G86B's
   clean nulls.
3. Step 8a note: the ORIGINAL asymmetric-context skeptic pass already ran
   (3 skeptics, context-blind per the workflow's own design) and is what
   caught this — no further skeptic round needed before reporting.

## Retroactive code review (Step per pre-commit checklist, run after commit `8da8c6b` — process gap, closed here)

`Agent(reviewer)` on all three Python files (`round63_corrected_v2.py`,
`round63_route_a_critical_points.py`, `round63_route_b_independent_check.py`):
**LGTM, P2 only** (0 blockers, 0 must-fix). Verified independently: both
routes' positive controls check against the correct `tests/test_g62_observables.py`
reference constants; the bifurcation-search bisection's monotonicity
assumption holds (tested directly); the 3 ruff-lint fixes in Route B (two
`lambda`→`def` conversions) did not introduce a late-binding closure bug —
confirmed the `lf=lam_func` default-argument pattern correctly captures each
loop iteration's value (15 distinct survivor `rho6_min` values in the output,
not 15 copies of one). 3 P2 notes recorded (unused `route2_confirmed` filter
field, a cosmetic print-column mismatch, a docstring/code grid-spacing
mismatch) — none affect any reported number.

## Files

- `claim.md` — frozen before running (contains the FLAWED substitution
  specification — kept, not edited, per never-delete discipline; this
  decision.md is the authoritative correction record)
- `round63_route_a_critical_points.py`, `round63_route_b_independent_check.py`
  — both routes' scripts (implement the flawed substitution faithfully;
  valuable as validated $V_{\mathrm{total}}$/positive-control infrastructure,
  reusable for the corrected formula in any follow-on round)
- Corrected recomputation: run directly via Bash/mpmath this session, not
  saved as a separate script file (kept in this decision.md's own numbers
  table; a future round should promote this to a proper committed script if
  built upon further)
- Workflow transcript: `wphnzl177` / `wf_0d77e67c-e05` (journal.jsonl has all
  5 agents' full structured returns including all 3 skeptics' full rationales)

---

## Appendix — Route A's original draft decision (preserved verbatim, superseded by the correction above)

# Round63-WrappedS3InstantonChannel Decision

**Verdict: PROMOTE [WEAKENED] — pending Step 8a skeptic review**

Script: `round63_route_a_critical_points.py`
Results: `results_round63_route_a.json`

### Step 0 re-derivation (mandatory gate)

Re-read `preprint.tex` §sec:lambda directly (not from memory/prompt restatement).
Confirmed by independent symbolic substitution: with $\lambda_{\mathrm{geom}}=c\rho_3^a\rho_6^{2-a}$
and slope-2 trajectory $\rho_3=C'\rho_6^2$,
$\lambda_{\mathrm{geom}}/\rho_6^2 = c(\rho_3/\rho_6)^a = c(C')^a\rho_6^a$, so
$\exp(-\lambda_{\mathrm{geom}}/\rho_6^2)=\exp(-c(C')^a\rho_6^a)$ — matches eq:slope2-exp
exactly. For $a=3$: $\exp(-c(C')^3\rho_6^3)$. `formula_rederived_matches_preprint = True`.

### Positive control (mandatory gate)

Reproduced the established constant-$\lambda$ G62 zero-fit using the exact normalization
of `experiments/20260621-g70-functional-form/vary_exponent.py` (p=2.0 row) and
`experiments/20260626-g94-s3-np-instanton/g94_s3_np_instanton.py` (`RHO6_STAR=1.090`):
computed $\rho_{6,\min} = 1.1790597918$ vs reference $1.1790597996$ — relative error
$6.6\times 10^{-9}$. Setup confirmed correct before touching the a=3 channel.

### a=3 channel result (SUPERSEDED — dimensionally inconsistent substitution, see correction above)

$f_{a=3}(\rho_6) = 1-\exp(c_{\mathrm{eff}}\rho_6^3(1/\rho_6^{*2}-1/\rho_6^2))$ — Skeptic 0
found $c_{\mathrm{eff}}\rho_6^3$ is $\lambda_{\mathrm{geom}}/\rho_6^2$ (already-reduced),
not raw $\lambda_{\mathrm{geom}}(\rho_6)$; substituting it into $f(\rho_6)$'s $\lambda$ slot
double-divides by $\rho_6^2$. Findings under this flawed formula (superseded, kept for
record): EFT-valid minimum for $c_{\mathrm{eff}}\in(0,\approx1.79)$,
$\rho_{6,\min}\in[1.205,1.336]$.

### G94 cross-check (Step 3) — this part's methodology stands independent of the formula fix

Attempted the mapping $c_{\mathrm{eff}}=c_{S3}\cdot(16\pi/15)$ under the hypothesis that
$c$ (eq:buckingham-pi coefficient) and $c_{S3}$ (G94's D-brane coefficient) are literally
the same constant. Honest caveat already self-identified here (confirmed independently by
Skeptic 1): even granting $c=c_{S3}$, the two terms are structurally different functions of
$\rho_6$ once substituted (G94's term gives a pure 6th-power exponent; this round's term
gives a cubic-minus-linear exponent) — reported as a numerical coincidence-check only, not
a derivation that the two channels are the same physics.

### Outstanding (as originally flagged — now resolved)

Step 8a skeptic review not yet performed at the time this draft was written. It has since
run (3 skeptics) and found the formula error corrected above. See the main decision above
this appendix for the final, authoritative result.
