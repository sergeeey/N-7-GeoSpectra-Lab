# Round116 — Claim

**OB1 mechanism search, continued.** Brainstorm item 28 ("spectral flow,
`N_gen = SF{D(u)}`" — a dynamical alternative to summing three separate
indices) applied, in a modest, honest form, directly to round67's own
already-computed `D^t` crossing structure — not a new external technique,
not a new computation of the crossings themselves, purely a structural
reading of numbers already on record.

## Source facts (already established, cited not re-derived)

Round67 (`e2_s3_torsion_deformation.py`, `results_e2.json`) computed the
**exact, closed-form** zero-crossings of `D^t(n,σ)=σ(n+3/2)+(t-1/2)·3` for
`n=0,1,2`, `σ=±1`:

```
t* ∈ { -2/3, -1/3, 0, 1, 4/3, 5/3 }
```

## L0 gate (EstimandOps)

**Question type: Descriptive.** Reading an already-computed, exact list
of numbers for a structural pattern (spacing, symmetry, which pair is
closest to a reference point) is arithmetic/observation, not a causal or
predictive claim. **Whether that structural pattern constitutes a genuine
physical selection principle is a separate, explicitly NOT-descriptive
question, kept apart below.**

## Falsifiable claim (descriptive part)

1. The six crossings are evenly spaced at intervals of exactly `1/3`.
2. They are symmetric about `t=1/2` (the Levi-Civita point).
3. `t=0` and `t=1` are the crossings closest to `t=1/2` (i.e., the
   smallest `|t*-1/2|`), corresponding to the lowest KK/Peter-Weyl level
   `n=0` on each side (`σ=+1` gives `t=0`, `σ=-1` gives `t=1`).
4. No other crossing lies strictly between `t=0` and `t=1`.

## Kill criterion (pre-registered)

- If (1)-(4) do not hold on direct recomputation from round67's own
  formula → this round's own framing is wrong, stop, do not proceed to
  any interpretive claim.
- If (1)-(4) do hold (expected, since they follow algebraically from
  `D^t(n,σ)` being linear in `t` with slope `±3` and round67's own already-
  verified numbers) → this is a **sharper structural characterization**
  of why `t=0,1` might be a distinguished pair (the innermost, lowest-`n`
  crossings) — explicitly **NOT** a selection principle by itself. The
  actual physical claim ("lowest-lying/lowest-energy modes are the
  physically accessible or relevant ones") is a SEPARATE, additional
  hypothesis this round does **not** establish — it only shows that IF
  such a "prefer lowest `n`" principle existed, it WOULD single out
  exactly `t=0,1` and no other pair, cleanly. Whether such a principle is
  itself justified (e.g. from an energy/mass argument, a genuine
  low-energy-effective-theory truncation) is explicitly flagged as
  unresolved and NOT attempted here.

## What this does NOT mean (pre-registered)

1. Does NOT establish a physical reason to prefer low `n` — that is a
   separate, unresolved hypothesis, named but not tested here.
2. Does NOT compute a formal "spectral flow" integer (which would require
   resolving a boundary-crossing convention at `t=0,1` themselves, an
   error-prone technical detail avoided here in favor of the more modest,
   safely-stated structural facts (1)-(4) above).
3. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
4. Does NOT re-derive round67's own crossing values — reused by citation.
