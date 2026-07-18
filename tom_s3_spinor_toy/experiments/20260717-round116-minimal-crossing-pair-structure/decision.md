# Round116 — Decision

**Date:** 2026-07-17
**Verdict:** `EQUIVALENT_RESTATEMENT_CONFIRMED__T_0_1_ARE_THE_N0_INNERMOST_PAIR__NOT_A_SELECTION_PRINCIPLE__MULTIPLICITY_CAVEAT_ADDED`
(skeptic: `WEAKENED` — numerical claims fully confirmed, framing corrected,
one real content gap identified and added)

**Go/no-go:** claims (1)-(4) hold rigorously for all `n≥0` (proven via the
general closed form, not merely spot-checked). But per skeptic review, the
framing "sharper structural characterization" overclaimed — this is an
**equivalent restatement** of `D^t` being affine in `t` with scalar slope
`h_H=3`, not new information. One genuine content gap (eigenspace
multiplicity, silently dropped) is added below.

## What was computed [VERIFIED-tool: sympy, this round]

1. Recomputed round67's own 6 tabulated crossings from `D^t(n,σ)=σ(n+3/2)
   +(t-1/2)·3=0` — all match exactly.
2. Solved the **general** closed form for symbolic `n`: `t*(n,+1)=-n/3`,
   `t*(n,-1)=n/3+1` — not restricted to round67's own `n=0,1,2` tabulation.
3. Confirmed claims (1)-(4) using the general closed form (not spot-checks
   — see skeptic correction below).

## Skeptic review [context-asymmetric: claim.md + code only] — three findings

**Finding 1 (presentation, not a content gap):** Claim (4)'s spot-check
over `n=0..19` was **redundant and methodologically weaker than the
argument already available** — since `t*(n,+1)=-n/3` and `t*(n,-1)=n/3+1`
are EXACT closed forms (not approximations), `-n/3≤0` and `n/3+1≥1` for
all `n≥0` follow from one line of algebra, no spot-check or further
verification needed. The spot-check wasn't wrong, just unnecessary and
signals uncertainty where none exists. **Corrected characterization:**
claim (4) is rigorously proven for ALL `n≥0` by the closed form alone, not
merely "checked up to n=19."

**Finding 2 (real content gap, accepted and added):** the `(n,σ)`
parametrization captures each eigenVALUE crossing, but **silently drops
the `(n+1)(n+2)` eigenspace multiplicity** at each level — a fact already
established elsewhere in this project (the S³ Dirac spectrum's own
multiplicity structure). Each `t*` listed is actually a crossing of
multiplicity `(n+1)(n+2)` (e.g. `t=0,1`: multiplicity 2 each; `t=-1/3,4/3`:
multiplicity 6 each). This matters specifically because the round's own
framing invokes "spectral flow" (brainstorm item 28) even while explicitly
declining to compute a formal spectral-flow integer — spectral flow is
inherently multiplicity-weighted, and this round's family, while exhaustive
of eigenVALUE crossings (assuming `h_H` acts as a scalar within each
eigenspace, per round67's own established fact), does not track
multiplicity at all. **Added as a new item in "What this does NOT mean."**

**Finding 3 (framing overclaim, corrected):** everything in claims (1)-(4)
follows in one line from `D^t=D+(t-1/2)·h_H` being affine in `t` with
**scalar** slope `h_H=3`: symmetry about `t=1/2` is trivial (the fixed
point where the shift vanishes), even `1/3` spacing is `1/h_H`, and "`n=0`
innermost" is what "innermost" means for any monotonic sequence. **This is
an equivalent rewrite of round67's own tabulation, not new information** —
"sharper structural characterization" (claim.md's original framing)
overstated this. Corrected to "equivalent restatement."

## Applying the corrected verdict

The kill criterion's PASS branch (claims (1)-(4) hold) is met, and the
explicit disclaimer ("NOT a selection principle by itself") already
present in claim.md was CORRECT and is kept. What's corrected: the framing
verb ("sharper" → "equivalent restatement") and the addition of the
multiplicity caveat.

## Kill Analysis

- **What this kills:** nothing new — round67's own crossing structure
  stands unchanged, merely rewritten in an equivalent, if unenlightening,
  form.
- **What this does NOT kill:** the open question of whether ANY physical
  principle prefers `n=0` (lowest KK level) remains exactly as open as
  before this round — this round neither advances nor closes it.
- **What survives, honestly scoped:** a correct, general (not
  spot-checked) proof that `t=0,1` are the unique innermost pair for
  `n≥0`, useful as a citable fact for any FUTURE round that DOES attempt to
  justify a "prefer lowest KK level" principle — but this round does not
  attempt that justification itself.

## What this does NOT mean (corrected, supersedes claim.md's version)

1. Does NOT establish a physical reason to prefer low `n` — a separate,
   unresolved hypothesis.
2. Does NOT compute a formal "spectral flow" integer.
3. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
4. Does NOT re-derive round67's own crossing values — reused by citation.
5. **New, per skeptic:** does NOT account for the `(n+1)(n+2)` eigenspace
   multiplicity of each S³ Dirac level — each `t*` listed is in fact a
   crossing of that multiplicity, silently dropped here. This matters if
   "spectral flow" language is ever invoked more formally in a future
   round; spectral flow is inherently multiplicity-weighted, and this
   round's `(n,σ)`-only family does not track it.
6. **New, per skeptic:** the "structural characterization" is an
   **equivalent restatement**, not new derived content — everything
   follows in one line from `D^t` being affine in `t` with scalar slope.

## Check (reproduces this decision)

```
cd experiments/20260717-round116-minimal-crossing-pair-structure
python e38_minimal_crossing_pair.py
```
Expect all 6 tabulated crossings to match, general closed forms
`t*(n,+1)=-n/3`, `t*(n,-1)=n/3+1`, and all four verdict booleans `True`.
Note: the script's own `n=0..19` spot-check for claim (4) is redundant
(see Finding 1) — the closed form alone proves it for all `n`.
