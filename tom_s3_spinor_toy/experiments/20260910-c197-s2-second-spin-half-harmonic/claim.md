# C197 Claim — the actual second spin-1/2 S² harmonic (k=3, weight -1/2)

**Date:** 2026-09-10
**FL tier:** [x] Standard
**Question type:** [x] descriptive [ ] predictive [ ] causal

---

## Prior Result Gate

1. **Exact claim:** the `k=3`, fibre-weight `-1/2` sector, after Hopf
   substitution and phase-stripping, gives a genuine second member of the
   spin-**1/2** tower (same weight as `χ_{±1/2}` itself), double-valued,
   not proportional to either `χ_{+1/2}` or `χ_{-1/2}`.
2. `decision.md` grep: [x] done — `C196` computed the `k=3` weight `-3/2`
   sector (spin-weight 3/2) and explicitly printed that weight `-1/2` is
   also present at `k=3` but did not compute it. 0 hits for this specific
   sector.
3. Scripts/null_results/parked: [x] done, 0 hits.
4. Primary motivation: a round-3 context-blind skeptic pass on the letter
   drafted from `C196` found that the letter's "genuine spinor-type
   content" claim for `C196`'s own object was WEAKENED (it's spin-weight
   3/2, not 1/2) — and separately pointed out the actual spin-1/2 second
   example was one script iteration away, already visible in `C196`'s own
   printed weight list `[-3/2,-1/2,1/2,3/2]`.
5. **Status:** [x] NEW

---

## Claim

**H:** the `k=3`, weight `-1/2`, `m_R=-1/2` object, stripped of its ψ
phase, is a genuine, double-valued, spin-weight-1/2 S² harmonic distinct
from `χ_{±1/2}`.

## Checks

| # | Check | Negative control |
|---|---|---|
| A1 | k=3 level dimension 16 | regression check, reused from C196 |
| B1/B2 | weight `-1/2` sector is 4-dim, splits into 4 distinct `m_R` | same structure C196 verified for weight `-3/2` |
| C1 | ψ-phase exponent = `-1/2`, matching `χ`'s own weight (not `-3/2`) | this is the actual discriminator between "spin-1/2" and "spin-3/2" |
| C2/C3 | ψ drops out; closed form `e^{-iφ/2}cos(θ/2)(3cos²(θ/2)-2)` matches numerically to 30 digits | — |
| D1 | double-valued under `φ→φ+2π` | N1-style: an ordinary single-valued function must fail this |
| D2 | not proportional to `χ_{+1/2}` OR `χ_{-1/2}` | unlike `C196`'s D2 (which could not fail — different φ-periodicity by construction), here both comparisons share the SAME φ-periodicity (weight `-1/2`), so non-proportionality is a real, failable check |

## What this does NOT mean

1. Does NOT derive the general `_{1/2}Y_{j,m}` family for all `j` — a
   second concrete member (`j=3/2`), not an induction proof.
2. Does NOT establish this is an eigenfunction of any specific Dirac-type
   operator on S² — the S² Dirac operator's own eigenfunctions are a
   separate, already-computed result (`C185`); this experiment is about
   the harmonic-decomposition/descent-method content, not re-deriving C185.

## Verdict

**CONFIRMED** — see `decision.md`. `[VERIFIED-sympy 9/9]`.
**Status:** CLOSED — PROMOTE.
