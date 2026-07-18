# Round112 (E26) — Claim

**Follows up:** `OPEN_BLOCKERS.md` OB8. Round96 (E25) computed 3 of 5 mixed
`U(1)_Y` anomaly conditions (`[SU(3)_c]²U(1)_Y`, `[U(1)_Y]³`, `[grav]²U(1)_Y`)
for both `t=0,1` endpoints separately and found `FAIL` (none show forcing).
Its own correction note (added after Codex's round105 cross-model review)
recorded that **`[SU(2)_L]²U(1)_Y` and `[SU(2)_R]²U(1)_Y` were never
computed**, in round96 or round92 before it — leaving round100's "anomaly
route fully exhausted" framing an overclaim by exactly these two channels.

## L0 gate (EstimandOps)

**Question type: Descriptive.** Computing two specific anomaly-coefficient
values from an already-fixed field/charge assignment (round92's rep table +
round93's `K3=T3R` + round94's `B-L=0`) is arithmetic on an established
input, not a causal or predictive claim.

## Falsifiable claim

For the frozen `G_eff = SU(3)_c x SU(2)_L x SU(2)_R` and the now-unambiguous
`Y = T3R + (B-L)/2` (round93+round94), computing
`A([SU(2)_L]²U(1)_Y) = Σ_i (T3L_i)² Y_i` and
`A([SU(2)_R]²U(1)_Y) = Σ_i (T3R_i)² Y_i` (standard mixed-anomaly formula,
matches the SM's own SU(2)_L² U(1)_Y check: doublet Q gives
`(1/2)²(1/6)×2=1/12` per color, `L` doublet gives `(1/2)²(-1/2)×2=-1/4`,
summing correctly to the known SM cancellation) for `t=0` alone, `t=1`
alone, and their union, using round92's own per-endpoint representation
content (t=0: SU(2)_L singlet / SU(2)_R doublet; t=1: SU(2)_L doublet /
SU(2)_R singlet — unchanged, not re-derived here).

## Kill criterion (pre-registered)

- If **both** conditions vanish at both endpoints separately and in union →
  extends round96's `FAIL` verdict to all 5 conditions; no forcing anywhere
  in the mixed-`U(1)_Y` anomaly class. OB8 closed as `FAIL`, matching round96.
- If **either** condition is nonzero at one endpoint alone but zero in the
  union (`t0_alone != 0 and t1_alone != 0 and union == 0`, exact wording of
  round96's own `forcing_pattern` check) → genuine forcing pattern found,
  `PASS`, would reopen the Pati-Salam/anomaly parent-action route closed by
  gate G97's product-manifold reading (round102/108/109) — a significant,
  surprising result requiring immediate skeptic review before any promotion.

## What this does NOT mean (pre-registered)

1. Does NOT re-derive or question round92's per-endpoint T3L/T3R assignment
   — that is reused as-is, per round96's own precedent.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
3. A `FAIL` result here does not, by itself, close the Pati-Salam/anomaly
   route beyond the mixed-`U(1)_Y` class specifically — cubic non-abelian
   anomalies (`[SU(2)_L]³`, `[SU(2)_R]³`, mixed `SU(2)_L`-`SU(2)_R`-gravity,
   etc.) are a different, not-yet-swept class.

## Counterfactual frame

In what world would this NOT reduce to a mechanical extension of round96?
If the per-endpoint field content were NOT exactly one SU(2) factor singlet
and the other a doublet with `T3` values symmetric about zero (i.e., if
round92's rep table were wrong or if `B-L≠0` at either endpoint) — then the
odd-power cancellation mechanism identified below would not automatically
apply and an actual nonzero result would be possible. This is why the
computation is still worth running explicitly rather than asserting the
outcome from the mechanism alone.
