# Round112 (E26) — Decision

**Date:** 2026-07-17
**Verdict:** `WEAKENED__ARITHMETIC_CONFIRMED_ZERO_BOTH_CHANNELS__CLOSURE_OF_OB8_IS_NEAR_TAUTOLOGICAL_GIVEN_ROUND94_BL0__NOT_A_GENUINE_TEST_OF_REP_CONTENT`
(skeptic verdict — arithmetic `CONFIRMED-REAL`, framing `WEAKENED`)
**Go/no-go:** OB8 closes as `FAIL`, matching and extending round96 — but the
skeptic found the closure carries far less discriminating power than the
claim's own kill-criterion framing suggested. Recorded honestly, not smoothed
over (matches this project's own additive-correction discipline).

## What was computed [VERIFIED-tool: sympy, re-run before writing this decision]

`A([SU(2)_L]²U(1)_Y) = Σ_i(T3L_i)²Y_i` and `A([SU(2)_R]²U(1)_Y) = Σ_i(T3R_i)²Y_i`,
for `t=0` alone, `t=1` alone, and their union, reusing round92's per-endpoint
representation content (t=0: `SU(2)_L` singlet / `SU(2)_R` doublet; t=1:
`SU(2)_L` doublet / `SU(2)_R` singlet) and round93+round94's
`Y=T3R+(B-L)/2`, `B-L=0`.

**Result: all four values are exactly 0** (`t0_alone=0, t1_alone=0, union=0`
for both conditions). Sanity check (the same formula applied to the known SM
field content: `Q` doublet ×3 colors + `L` doublet) reproduces the SM's own
known `[SU(2)_L]²U(1)_Y` cancellation (`1/4 − 1/4 = 0`) exactly, confirming
the formula itself is correctly stated and applied.

## Skeptic review [context-asymmetric: claim.md + code only]

**Arithmetic and formula: `CONFIRMED-REAL`.** The skeptic independently
re-derived all four values by hand, matched the sympy output exactly, and
confirmed `Σ(T3)²Y` is a valid diagonal component of the standard mixed-anomaly
tensor `Tr(Y·{T^a,T^b})` — no sign or normalization convention flips any of
the four zeros to nonzero.

**Framing: `WEAKENED`, correction accepted and kept, not dismissed.** The
skeptic's central finding: each of the four zeros is forced by a **different,
individually trivial** mechanism, not by a nontrivial cancellation between
competing charges within a genuinely-tested representation content:

1. `[SU(2)_L]²Y` at `t=0` → `(T3L)²≡0` identically (SU(2)_L singlet). Zero
   for **any** `Y` whatsoever — the computation cannot distinguish this from
   a differently-charged input.
2. `[SU(2)_L]²Y` at `t=1` → `Y≡0` identically, because `T3R=0` (SU(2)_R
   singlet) **and** `B-L=0` (round94) — zero for **any** `T3L` whatsoever.
3. `[SU(2)_R]²Y` at `t=0` → since `B-L=0`, `Y=T3R` exactly, so `U(1)_Y` is
   not an independent gauge factor here at all — it **is** the `T3R` Cartan
   generator of `SU(2)_R` itself. `[SU(2)_R]²·T3R` is then the universal
   SU(2) symmetric-trace identity (zero for any SU(2) representation, not a
   fact about this project's specific rep content).
4. `[SU(2)_R]²Y` at `t=1` → `(T3R)²≡0` identically (SU(2)_R singlet), same
   triviality as (1).

**Sharpened conclusion:** at `t=1` specifically, `Y=T3R+(B-L)/2=0+0=0`
identically under the current, frozen input set (round94's `B-L=0` +
`t=1`'s own `T3R=0`) — meaning **every** mixed-`U(1)_Y` anomaly condition
(not just these two; also round96's own three) is forced to zero at
`t=1_alone` for this same structural reason, independent of rep content.
Round96's own `t=1_alone` zeros should be read the same way, in hindsight —
not as 3 separate confirmations, but as one shared structural consequence of
`Y≡0` there.

## Applying the pre-registered kill criterion (claim.md)

The literal kill criterion ("both vanish at both endpoints and in union →
`FAIL`, closes OB8") is met and accepted. But per the skeptic's finding, this
acceptance comes with an honest scope note: **the closure is arithmetically
near-inevitable given round94's `B-L=0` input, not a genuine stress-test of
whether the mixed-`U(1)_Y` anomaly class could force sector coexistence** —
the inputs were already structured (by earlier rounds, correctly) such that
`U(1)_Y` degenerates into an internal `SU(2)` generator or vanishes entirely
at each endpoint. This closes OB8 honestly, but should not be read as adding
much new confidence beyond what round94+round96 already established.

## What this does NOT mean (sharpened per skeptic, supersedes claim.md's version)

1. Does NOT re-derive or question round92's per-endpoint `T3L`/`T3R`
   assignment — reused as-is.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
3. Does NOT close the Pati-Salam/anomaly route beyond the mixed-`U(1)_Y`
   class — cubic non-abelian anomalies (`[SU(2)_L]³`, `[SU(2)_R]³`, mixed
   `SU(2)_L`-`SU(2)_R`-gravity, etc.) remain a genuinely separate,
   not-yet-swept class. Round100's "anomaly route fully exhausted" framing
   must **not** be upgraded on the strength of this round — it was already
   scoped to the mixed-`U(1)_Y` class specifically, and stays so scoped.
4. **New, per skeptic:** does NOT demonstrate the computation *could have*
   detected a forcing pattern if one were present — all four zeros trace to
   `U(1)_Y` being degenerate or vanishing at the relevant endpoint under the
   CURRENT frozen inputs, not to an observed cancellation between
   nondegenerate competing charges. A cleaner test of the code's own
   discriminating power (not attempted here) would use an adversarial input
   with `B-L≠0` at one endpoint to confirm the formula would flag forcing if
   it were actually present — flagged as a future validation-theater guard,
   not required to accept this round's own FAIL verdict.

## Kill Analysis

- **What this kills:** the specific gap Codex flagged (OB8) — "were
  `[SU(2)_L]²U(1)_Y`/`[SU(2)_R]²U(1)_Y` ever computed" — no longer open;
  computed, `FAIL`.
- **What this does NOT kill:** the broader "mixed-`U(1)_Y` anomaly route
  fully exhausted" claim is NOT strengthened much by this round, per the
  skeptic's triviality finding — it was already effectively implied the
  moment round94 fixed `B-L=0`.
- **What survives, sharper than before:** the precise, single-sentence
  reason the `t=1` endpoint is anomaly-free in every mixed-`U(1)_Y` channel
  simultaneously (`Y≡0` there) — a cleaner, unified explanation than
  treating each of round96's three conditions and this round's two as five
  separate coincidental zeros.

## Relaxation Map (future work, not attempted here)

| Option | What it would require |
|---|---|
| Compute `[SU(2)_R]²U(1)_(B-L)` (the genuinely independent U(1) factor, before setting `B-L=0`) instead of `U(1)_Y` | Re-run with `B-L` as a free symbol rather than substituting 0, to see if the formula is sensitive to it at all |
| Adversarial input test (`B-L≠0` at one endpoint, hypothetically) | Confirms the code's own discriminating power per Validation Theater Guard — not a physical claim, a code-sanity check |
| Cubic non-abelian anomaly sweep (`[SU(2)_L]³`, `[SU(2)_R]³`) | Genuinely untested class; would need the full triple-generator trace, not just the diagonal `(T3)²` component used here |

## Check (reproduces this decision)

```
cd experiments/20260717-round112-remaining-mixed-y-anomaly-channels
python e26_remaining_mixed_y_channels.py
```
Expect: `sm_sanity_check_passed=True`, all four `A(...)` values `= 0`,
`any_new_condition_shows_forcing=False`,
`label='FAIL__BOTH_REMAINING_CONDITIONS_COMPUTABLE_NONE_SHOW_FORCING__EXTENDS_ROUND96'`.
