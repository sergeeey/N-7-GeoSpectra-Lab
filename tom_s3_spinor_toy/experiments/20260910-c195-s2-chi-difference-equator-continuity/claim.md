# C195 Claim — Tom's discontinuity claim: χ₊−χ₋ is continuous only at the equator

**Date:** 2026-09-10
**FL tier:** [x] Micro-scope content, formalized at Standard tier for the permanent record
**Question type:** [x] descriptive [ ] predictive [ ] causal

---

## Prior Result Gate

1. **Exact claim:** the difference `Δ = χ_{+1/2} − χ_{-1/2}` (C184's own
   derived S² doublet) has a branch-cut jump across `φ=0` that vanishes
   exactly at `tan(θ/2)=1` (the equator) and nowhere else on `θ∈[0,π]`.
2. `decision.md` grep: [x] done — `C184` derives `χ_{±1/2}` but never checked
   this specific claim about their difference's continuity. 0 hits.
3. Scripts grep: [x] done, 0 hits for "equator" + "tan(theta/2)" combined.
4. `null_results/`/`parked/`: [x] done, 0 hits.
5. `git log -S/-G`: [x] done, 0 hits.
6. Primary source: Tom's 2026-09-10 letter, verbatim: *"it turns out that it
   is only continuous when tan(θ/2) = 1, that is, on the equator."*
7. **Status:** [x] NEW

---

## Claim

**H:** the branch-cut jump of `Δ(θ,φ)=χ_{+1/2}-χ_{-1/2}` across `φ=0`
vanishes iff `θ=π/2`.

## Kill criterion

| Kill condition | Threshold |
|---|---|
| Jump vanishes at a `θ` other than `π/2`, or at more than one point | any second root on `[0,π]` |
| Jump does not reduce to a function of `θ` alone | leftover `φ`-dependence after substituting the branch point |

## Checks planned

| # | Check | Negative control |
|---|---|---|
| A1-A3 | anti-periodicity of each component and their difference | none needed — this is a sanity re-derivation of already-established structure |
| B1 | jump(θ) closed form | — |
| C1-C2 | root-solve for the vanishing point, compare to `tan(θ/2)=1` | — |
| D1 | a genuinely single-valued (φ-independent) pair must have jump≡0 for ALL θ, not an isolated point | this is the actual negative control: distinguishes "isolated-zero" (half-integer, interesting) from "identically-zero" (integer/single-valued, the case the check must NOT confuse with the claim) |

## What this does NOT mean

1. Does NOT derive a general theorem about when sums of anti-periodic
   functions are continuous — only checks Tom's specific pair.
2. Does NOT check continuity of derivatives (Tom's own separate remark) —
   out of scope for this round.

## Verdict

**CONFIRMED** — see `decision.md`. `[VERIFIED-sympy 7/7]`.
**Status:** CLOSED — PROMOTE.
