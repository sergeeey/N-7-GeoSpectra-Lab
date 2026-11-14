# C195 Decision — CONFIRMED. Tom's equator/discontinuity claim holds exactly.

**Date:** 2026-09-10
**Verdict:** **CONFIRMED**, `7 of 7` checks pass, exact symbolic arithmetic.
All numbers trace to `c195_equator_continuity_check.py` and `run_output.txt`.

---

## 1. Result

```
Δ(θ,φ) = e^{-iφ/2}cos(θ/2) − e^{iφ/2}sin(θ/2)
jump across φ=0:  2·Δ(θ,0) = 2√2·cos(θ/2 + π/4)
vanishes  ⟺  θ = π/2  ⟺  tan(θ/2) = 1
```

Tom's claim, stated in his 2026-09-10 letter without derivation, is
**exactly right** — the discriminating scalar `cos(θ/2+π/4)` has a single
zero on `[0,π]`, at `θ=π/2`, matching `tan(θ/2)=1` exactly (check C2).

## 2. Why the negative control (D1) matters here

The first version of this check used a "mismatched-phase" pair as its
negative control and it **passed when it should have failed** — both
components carried the same anti-periodic factor `e^{-iφ/2}`, so their
difference was anti-periodic regardless of the internal mismatch; the
control tested nothing. Caught before promotion by actually running it, not
by inspection. Replaced with a pair that is **genuinely single-valued**
(`φ`-independent, `f=cos θ, g=sin θ`): its jump is identically zero for
*every* `θ`, not an isolated point — the qualitatively different behaviour
this round's B/C checks must be able to tell apart from Tom's actual,
isolated-zero-at-the-equator case. This is the same class of near-miss this
project's own memory already tracks under `[AVOID]` (a check that cannot
fail is not a check) — recorded here as the concrete instance, not just
cited.

## 3. Floor–Ceiling (Step 4a)

Metric: **does the computed vanishing locus match Tom's stated claim
exactly, as a fraction of the single root on `[0,π]`.**

FLOOR (mechanism absent) = `0.0`. A construction with no genuine
theta-dependence in the jump (the corrected D1 negative control: a
phi-independent pair) gives jump≡0 for every theta — zero discriminating
power, no located root at all.

CEILING (exact match to the closed-form prediction) = `1.0`. The jump
function has precisely one root on `[0,π]`, located exactly, coinciding with
`tan(θ/2)=1`.

OBSERVED = `1` (checks B1/C1/C2: closed form derived, single root solved
exactly, matches `tan(θ/2)=1` symbolically — not approximately).

EFFICIENCY = `(1-0)/(1-0)` = **`1.0`** — exact match, not partial.

## 4. What this gives the reply

An independent, computed confirmation of Tom's own by-hand result — safe to
tell him it checks out exactly, strengthening trust in both directions
rather than merely accepting the claim.

## 5. What this does NOT establish

- Does not address Tom's separate remark about derivative continuity of
  continuous sums — untouched, out of scope.
- Does not generalize beyond this specific `χ_{±1/2}` pair.

## 6. Reproduction

```
cd experiments/20260910-c195-s2-chi-difference-equator-continuity
python c195_equator_continuity_check.py
```

`7/7`. `ruff check` and `ruff format`: clean.
