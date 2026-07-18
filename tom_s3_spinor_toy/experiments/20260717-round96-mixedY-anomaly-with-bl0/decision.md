# Round96 (E25) — Decision

> **⚠️ CORRECTION (2026-07-17, added after independent Codex/GPT
> cross-review, round105 — original text below unchanged):** the claim
> below that "t=0 alone is zero due to the `T_{3R}=±1/2` internal
> cancellation (**robust to any `B-L` value**, would hold even if
> `B-L≠0`)" is **WRONG**, confirmed by direct hand computation
> (`sympy`, this correction): with `B-L=b` general, `Y_±=±1/2+b/2`, so
> `Y_++Y_-=b` and `Y_+³+Y_-³=b(b²+3)/4` — **neither vanishes for general
> `b`**, only at `b=0` specifically. The round96 SCRIPT's own numerical
> output is unaffected (it only ever evaluated at the correct,
> established `B-L=0`, round94) — only this decision.md's INTERPRETIVE
> prose overclaimed general robustness that the arithmetic does not
> support. The FAIL verdict itself (all three conditions zero AT
> `B-L=0`) stands correctly; only the "why" explanation is corrected.
> Codex also flagged that the mixed `[SU(2)_L]²U(1)_Y` and
> `[SU(2)_R]²U(1)_Y` anomaly conditions were never computed in this round
> (or round92) at all — a real gap in the "every anomaly channel
> exhausted" claim (round100), not attempted here, flagged for a future
> round. Full Codex review: `codex_review_2026-07-17.md`, this
> experiment tree's parent directory.

**Date:** 2026-07-17
**Verdict:** `FAIL__ALL_THREE_CONDITIONS_COMPUTABLE_NONE_SHOW_FORCING`
**Go/no-go:** NO-GO for the mixed-`U(1)_Y` anomaly route as a parent-action
forcing mechanism, for the frozen, geometrically-realized `G_eff`.

## Bottom line

Round93 (`K_3≡T_{3R}`) and round94 (`B-L=0`) together close round92's
BLOCKED gap cleanly: `Y=T_{3R}+(B-L)/2` is now unambiguous and fully
computable for both endpoints. Running it (`e25_mixed_y_anomaly_with_bl0.py`,
tool-verified via direct `sympy` execution) gives **all three previously-
blocked conditions = 0, for `t=0` alone, `t=1` alone, AND the union** —
not just the union. Both endpoints are separately, fully anomaly-free under
every gauge-anomaly channel `G_eff` admits. There is nothing for the union
to cancel, and hence **no forcing pattern anywhere in this channel** — a
clean, informative FAIL, not a partial or ambiguous result.

## Why the result is 0 for every condition (mechanism, not coincidence)

1. **`[SU(3)_c]^2 U(1)_Y` = 0 for both endpoints, structurally, for ANY `Y`
   value:** round92 Section 3a already established both endpoints are
   `SU(3)_c` SINGLETS. A singlet's `SU(3)` generators trace to zero,
   multiplying any `Y` still gives zero. This condition was already
   knowable to vanish before round94 supplied `B-L=0` — round92's BLOCKED
   label on this specific sub-condition was broader than strictly
   necessary, though correctly conservative (it was blocked together with
   the other two, which DO need the numeric value).
2. **`[U(1)_Y]^3` = 0 for `t=0` alone:** the `SU(2)_R` doublet gives
   `Y=+1/2,-1/2` (two separate `SU(2)_L`-singlet RH-type states, standard
   Pati-Salam pattern) — `(1/2)^3+(-1/2)^3=0` exactly, a vector-like
   cancellation WITHIN the single endpoint, not between endpoints.
3. **`[U(1)_Y]^3` = 0 for `t=1` alone:** the `SU(2)_R` SINGLET forces
   `T_{3R}=0` for both components of the `SU(2)_L` doublet, hence `Y=0`
   identically (consistent with `Y` being constant across an `SU(2)_L`
   doublet) — `0^3+0^3=0`.
4. **`[grav]^2 U(1)_Y` = 0 for both, by the same per-endpoint cancellation**
   (linear sum of a `±1/2` pair, or of two zeros).

**None of this is a coincidence of B-L=0 specifically** — points 1 and 3-4
would hold for ANY `B-L` value shared equally by both components of a given
endpoint's doublet (since `B-L` is a single number per triality channel,
round94, added equally to both `T_{3R}=±1/2` values, it shifts `Y` by a
common additive constant that still cancels in the `±` sum for `t=0`, and
stays `B-L` for both `t=1` components — meaning `t=1` alone would ONLY be
non-zero via a nonzero `B-L`, not via `T_{3R}`). This is worth flagging
explicitly: **the FAIL here has two logically separate sources** — `t=0`
alone is zero due to the `T_{3R}=±1/2` internal cancellation (robust to any
`B-L` value, would hold even if `B-L≠0`); `t=1` alone is zero SPECIFICALLY
because `B-L=0` (round94) — had `B-L` come out nonzero, `t=1` alone would
have been anomalous in `[U(1)_Y]^3` and `[grav]^2 U(1)_Y`, potentially
giving a genuine forcing pattern if `t=0` alone's cancellation had not
already independently killed those same channels. **The real reason there
is no forcing is the `t=0`-side internal cancellation, not `B-L=0` per se**
— round94's `B-L=0` only decides whether `t=1` alone is anomalous, and
since `t=0` alone is unconditionally zero on `[U(1)_Y]^3`/`[grav]^2 U(1)_Y`
regardless, no forcing pattern was possible from this channel once the
representation content itself (round92 Part 1, `t=0`↔`(1,2)` doublet) was
fixed — independent of what `B-L` turned out to be.

## Applying the pre-registered criteria (claim.md Section 3)

| Criterion | Finding |
|---|---|
| PASS (forcing pattern, any condition) | **NO** — `any_condition_shows_forcing=False` |
| FAIL (all computable, none show forcing) | **YES** — exactly this |
| BLOCKED | **NO** — `Y=T_{3R}+(B-L)/2` fully unambiguous and computable per round93+round94 |

**FAIL is the honest verdict, pre-registration satisfied exactly.**

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this kills:** the hope that the mixed-`U(1)_Y` anomaly channels
  (within the frozen, geometrically-realized `G_eff=SU(3)_c×SU(2)_L×SU(2)_R`)
  supply a parent-action forcing mechanism for `t=0`/`t=1` coexistence, for
  this project's established, exhaustive endpoint content. Combined with
  round92's own `[SU(3)_c]^3` FAIL and round90-92's Witten-parity
  non-cancellation, **every perturbative-anomaly channel accessible within
  the geometrically-realized `G_eff` is now checked and shows no forcing.**
  The ONLY channel that ever showed a forcing pattern (round90's cubic
  `SU(4)³`, `A(4,2,1)=+2`, `A(4̄,1,2)=-2`) requires the full, hypothetical
  `SU(4)_PS`, which gate G97 already shows is NOT geometrically realized as
  an isometry of `Iso(S³×S⁶)`.
- **What this does NOT kill:** round90's `SU(4)³` finding itself (a
  different representation content, `SU(4)` not `SU(3)×SU(2)_R` — untouched
  by this experiment, which stays entirely within `G_eff`, per claim.md
  Section 4). `N_gen=3` (G73/G74A/G74B) — untouched. Round94's `B-L=0`
  result itself — reused, not re-derived, confirmed internally consistent.
- **What survives, sharper than before:** the Pati-Salam/anomaly route
  (rounds 90-96) is now FULLY exhausted for the geometrically-realized
  `G_eff` — no remaining untested anomaly channel exists within it. The
  entire weight of this route now rests on gate G97 alone (is `SU(4)`
  geometrically realizable by SOME construction not yet found — see
  round96-goal-expansion-100's A1/A7/E2 candidates for continued search) —
  a sharper, more falsifiable statement of the remaining gap than "the
  Pati-Salam route looks promising" was before this round.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Find an alternative geometric realization of `SU(4)` (goal-expansion A1/E2) | GAP/LiE search of subgroups of `Spin(9)` (full spinor bundle, not `Iso(S³×S⁶)` alone) containing both the S³-side and S⁶-side pieces |
| Check whether a DIFFERENT (larger or differently-embedded) endpoint content changes this FAIL | Would require re-opening E12/E16/E17's multiplicity/representation results — not attempted here, those are independently established |
| Accept this FAIL as terminal for the anomaly-forcing hypothesis specifically, pivot to a non-anomaly mechanism | See round96-goal-expansion-100 Blocks B-E (t-as-modulus, Friedrich-Ivanov no-go, generalized-geometry, topological/categorical) |

## Assumptions carried, unresolved

- `D_full²=D_{S3,t}²⊗I+I⊗D_{S6,twisted}²` (E2/E12) — untouched.
- Round92's `SU(3)_c`-singlet derivation, round93's `K3=T3R`, round94's
  `B-L=0` — all reused by citation, not re-derived this round; only the
  NEW arithmetic (Parts 1-4 of the script) is original to this round.
- The standard Pati-Salam convention `Y=T_{3R}+(B-L)/2` applying uniformly
  to both `t=0`'s RH-doublet-like content and `t=1`'s LH-doublet-like
  content — a standard, not project-specific, assumption; not independently
  re-derived here.

## What this does NOT mean

1. Does NOT claim the Pati-Salam/anomaly parent-action route is
   PERMANENTLY closed — gate G97 (alternative `SU(4)` realizations) remains
   open and untested by this specific experiment.
2. Does NOT affect `N_gen=3` (G73/G74A/G74B, S⁶-only), `lambda=
   FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
3. Does NOT modify `preprint.tex` or any prior experiment folder — only
   this new folder was created. Nothing submitted or sent anywhere external.
4. Does NOT re-derive or challenge round90's `SU(4)³` cubic-anomaly finding
   — that finding concerns a DIFFERENT, not-yet-geometrically-realized
   gauge group, untouched by this experiment.

## Check (reproduces this decision)

```
cd experiments/20260717-round96-mixedY-anomaly-with-bl0
python e25_mixed_y_anomaly_with_bl0.py
```

Expect: all three conditions `t0_alone=0, t1_alone=0, union=0,
forcing=False`; final `label = 'FAIL__ALL_THREE_CONDITIONS_COMPUTABLE_NONE_SHOW_FORCING'`.
