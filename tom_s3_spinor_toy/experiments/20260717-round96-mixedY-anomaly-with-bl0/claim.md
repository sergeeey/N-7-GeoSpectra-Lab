# Claim — Round96 (E25): Mixed-Y Anomaly Conditions With B-L=0 Substituted

**Question type:** Descriptive (arithmetic re-evaluation of an already-frozen
gauge group's anomaly coefficients using a now-established input value — not
a new causal or predictive claim).

## Section 1 — Background (reused, not re-derived)

Round92 (E22) froze `G_eff = SU(3)_c×SU(2)_L×SU(2)_R` (Option (i), since
`SU(4)` is not geometrically realized, gate G97) and found:
- `[SU(3)_c]^3` — computable, shows NO forcing (both endpoints already
  anomaly-free alone; both are `SU(3)_c` singlets).
- `[SU(3)_c]^2 U(1)_Y`, `[U(1)_Y]^3`, `[grav]^2 U(1)_Y` — **BLOCKED**, since
  no numeric `B-L`/`Y` value had ever been assigned to the twisted S⁶-kernel,
  and `preprint.tex` carried two apparently-distinct, unreconciled
  `Y`-formulas (`Y=K_3+(B-L)/2`, S⁶-side; `Y=T_{3R}+(B-L)/2`, S³-side).

Since round92, two things changed:
1. **Round93 (E23)** proved `K_3 ≡ T_{3R}` — the SAME 32×32 operator, not two
   distinct quantities. This means round92's "two distinct unreconciled
   `Y`-formulas" are, in fact, algebraically the SAME formula
   (`Y = T_{3R} + (B-L)/2`), not a genuine ambiguity requiring a choice.
2. **Round94 (E24)** computed `B-L = 0` for the physical
   `dim ker(D_{S6,twisted})=1` zero mode (`PASS_WITH_DOCUMENTED_CAVEAT`,
   the caveat being a real but structurally-irrelevant non-commutativity of
   `BL_64` with `D_full`, shown not to affect this specific eigenvalue).

**This experiment asks:** with `Y=T_{3R}+(B-L)/2` now unambiguous, and
`B-L=0` supplied by round94, do round92's three previously-BLOCKED mixed-`Y`
anomaly conditions become computable — and if so, do they show the
round90-style forcing pattern (`anomaly(t=0 alone)≠0`,
`anomaly(t=1 alone)≠0`, `anomaly(union)=0`), or not?

## Section 2 — Estimand (L0: descriptive)

- **Population:** the established, exhaustive endpoint kernel content for
  `G_eff=SU(3)_c×SU(2)_L×SU(2)_R` — 1 joint doublet per triality channel, 3
  channels, for each of `t=0` and `t=1` separately (round92 Part 1, reused
  unchanged).
- **Intervention/comparator:** `t=0` alone vs `t=1` alone vs their union, for
  each of the 3 mixed-`Y` anomaly conditions.
- **Endpoint:** the anomaly coefficient for each of
  `[SU(3)_c]^2 U(1)_Y`, `[U(1)_Y]^3`, `[grav]^2 U(1)_Y`, evaluated with
  `Y = T_{3R} + (B-L)/2`, `B-L=0` (round94), `T_{3R}` from the established
  representation table (round92 Section 1: `t=0`→`(1,2)`, `T_{3R}=±1/2`;
  `t=1`→`(2,1)`, `T_{3R}=0` since it is an `SU(2)_R` singlet).
- **ICE:** none (no post-registration events; this is a pure arithmetic
  re-evaluation of frozen inputs).

## Section 3 — Pre-registered criteria (BEFORE running the script)

- **PASS (forcing pattern present):** for at least one of the three
  conditions, `anomaly(t=0 alone)≠0` AND `anomaly(t=1 alone)≠0` AND
  `anomaly(union)=0`.
- **FAIL (no forcing):** all three conditions are computable, but none shows
  the PASS pattern — e.g., because both endpoints are already zero alone
  (nothing for the union to cancel), or because the endpoints give identical
  nonzero values that don't need summing to cancel.
- **BLOCKED:** the substitution of `B-L=0` and `Y=T_{3R}+(B-L)/2` turns out
  to still leave a genuine gap (e.g., if `T_{3R}` is not actually well-defined
  per-component the way assumed, or if the `K_3≡T_{3R}` identification from
  round93 is found on re-check not to license using `B-L=0` here directly).

## Section 4 — What this does NOT test

- Does not test the separate `SU(4)_PS` cubic anomaly (`A(4,2,1)=+2`,
  `A(4̄,1,2)=-2`, round90) — that mechanism requires `SU(4)` gauged, which
  gate G97 already shows is not geometrically realized for `G_eff`. This
  experiment stays within the frozen, geometrically-realized `G_eff` only,
  exactly as round92 did.
- Does not re-derive `B-L=0` (round94) or `K_3≡T_{3R}` (round93) — both
  reused by citation.
- Does not affect `N_gen=3` (G73/G74A/G74B, S⁶-only).
