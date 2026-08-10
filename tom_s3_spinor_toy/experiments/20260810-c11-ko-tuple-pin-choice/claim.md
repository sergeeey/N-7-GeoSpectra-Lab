# The KO-dimension tuple — and whether the Pin⁺/Pin⁻ choice actually changes it

**Experiment id:** `20260810-c11-ko-tuple-pin-choice`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C48 (computed sector signs, **declined** to combine them), C56 (said the
`ε''` sign flips with the Pin choice)

---

## What is being closed, and what it is worth

C48 wrote: *"NOT a KO-dimension claim: only the sector-factor signs are computed here, and
combining them with `S³`'s own tuple is exactly the step C36 showed is easy to get wrong.
Left OPEN rather than asserted."* C56 then reported that the `ε''` sign **flips** with the
Pin⁺/Pin⁻ choice, leaving the tuple as the one item still open.

**Worth saying up front:** C49 showed the index pairing vanishes and Poincaré duality
fails; C52 showed orientability fails. **The doubled triple is already known not to be a
spectral geometry.** So this is bookkeeping on a non-geometry — closure and correction,
not discovery. It is worth doing because it is the last deferred computation and because
C56 made a claim about it that I have not checked.

## The claim under test

> **C57.** The sign tuple `(ε, ε', ε'')` of the doubled triple, with
> `J² = ε`, `J D = ε' D J`, `J γ = ε'' γ J`, is computable from `S³`'s KO-dim-3 inputs
> (`J_M² = −1`, `J_M D_M = D_M J_M`) plus the sector data — and the **Pin⁺/Pin⁻ choice
> changes it**, as C56 stated.

**Falsifier, fixed in advance:** if the Pin phase cancels between `γ` and
`J_M U_ι J_M⁻¹`, then C56's `U5` was an incomplete accounting and must be corrected.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **K1** | `J D = ε' D J` forces `ε' = +1` (the `D_M` part cannot flip) **and** `[k, s3] = 0`, i.e. `k` **diagonal**. Non-diagonal `k` (`s1`, `s2`) must FAIL — otherwise the constraint is vacuous |
| **K2** | `J γ = ε'' γ J` further forces `k ∈ {I, s3}` up to phase; `diag(1,i)` must FAIL |
| **K3** | `ε = J² = −1` **always**, inherited from `J_M² = −1`, since `k` unitary diagonal gives `k·k̄ = I` |
| **K4** | **the Pin choice CANCELS.** `γ = c·U_ι⊗s1` with `U_ι = c'·W` (`W` = the real swap) and `c·c' = ±1`, so `γ = ±W⊗s1` is a **real** operator **independent of the split between `c` and `c'`**. The `c̄/c` flip C56 noted is exactly compensated by `η = J_M U_ι J_M⁻¹ / U_ι = c̄'/c'`. **If so, C56's U5 is WRONG and this round corrects it.** |
| **K5** | the surviving tuples are `(−1, +1, +1)` and `(−1, +1, −1)`, selected by `k = I` vs `k = s3` — an internal choice in `J`, **not** a geometric one |
| **CTRL** | the table lookup must reproduce a known case: the `S³` factor alone has `(ε, ε') = (−1, +1)` with no `γ` → **KO-dim 3**, which is the declared input. If the machinery cannot recover that, the lookup is not trustworthy |

## The honest expectation

I expect **K4 to fire**, i.e. to be correcting my own C56 claim. C56's `U5` looked only at
`J(cX)J⁻¹ = c̄ J X J⁻¹` and never asked what `J_M` does to `U_ι` — which carries the same
phase in the opposite direction. Two flips, one net effect: none.

## What this cannot show

- **The KO table itself is not re-derived.** The identification of a sign tuple with a
  KO-dimension mod 8 follows the literature (CCM 2006 / Connes), and is used as
  `[DOCS]` — exactly the handling `preprint.tex` now uses for `J_F`, after C36 showed
  this is the step that goes wrong.
- It does **not** revisit C49/C52: the object still fails PD and orientability, so a
  KO-dimension does not make it a geometry.
- The metric dimension is 3 (Weyl asymptotics of `D_block` on `S³ ⊕ S³`); a
  KO/metric mismatch is normal in NCG (the SM has 6) and is reported, not interpreted.
- Nothing about `N_gen = 3` — step 7 untouched by agreement.

## kill_criterion

C57 stands as worded only if some sign in the tuple genuinely depends on the Pin choice.
If every one is Pin-independent, C57 is **REFUTED as worded** and C56's `U5` is amended.
