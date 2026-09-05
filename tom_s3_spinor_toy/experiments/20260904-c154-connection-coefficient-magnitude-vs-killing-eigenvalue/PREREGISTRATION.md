# PRE-REGISTRATION — C154: is `|c(∇)| / |μ(∇)| = 2/3` a family-wide law, or a
# single-point coincidence?

**Registered:** 2026-09-04, before any NEW computation. The two data points
below are already-committed, source-verified facts; nothing here is fitted.

## L0 gate (EstimandOps): DESCRIPTIVE

Testing whether an already-noticed numeric coincidence between two
independently-defined quantities extends across a whole parameter family.
No counterfactual, no DAG.

## The two known values (verified against source files, not memory)

| | `c(∇_LC)` | `μ(∇_LC)` = untwisted `D_Σ` eigenvalue on the isotropy-invariant spinor `ψ₊` | `\|c\|/\|μ\|` |
|---|---|---|---|
| `S⁶=G₂/SU(3)` | `-2√3/3` (C147b, exact sympy, `experiments/20260904-c147.../decision.md:127`) | `-√3` (round59: `κ=1/(2√3)`, `D_Σψ₊ = 6·κ·(e_i²/6 summed)·ψ₊ = -6κψ₊ = -√3ψ₊`; matches pearl row 24's `b=-√3=-n·μ, n=6`) | `2/3` |
| `SU(3)/T²` | `2i` (C153 Step 2, exact sympy, `experiments/20260904-c153.../results_step2...txt:26`, uniform magnitude `2` on all 6 nonzero entries of the 3×3 matrix) | `3` (C151 Stage 2a calibration gate, `experiments/20260904-c151.../results_c151_stage2a.txt:14`) | `2/3` |

**Both ratios exactly `2/3`, verified from committed source files.**

## Why this is NOT automatically another C153

`c(∇)` is built entirely from Term2 (`Σᵢ Eᵢ⊗conn_W[i]`, C145's own decomposition)
— it never references `D_Σ` in its defining formula. `μ(∇)` is `D_Σ`'s own
eigenvalue on `ψ₊`, a completely different operator. On `SU(3)/T²` the two
live in *different* `T²`-weight sectors of `Σ`: `ψ₊` sits at weight `(0,0)`
(C151 Stage 1b), while `c(∇)`'s domain is `Σ_odd⊗W` restricted to *nonzero*
`Σ`-weights `{(-2,1),(1,1),(1,-2)}` that only become `T²`-invariant after
tensoring with `W`. There is no cheap Schur/weight-matching argument forcing
these two quantities to be proportional — unlike C153's per-plane law, which
*was* forced. If the ratio survives being tested across the whole family
(not just at one point), it is not obviously equivalent to a known theorem.

## The test (cheap, reuses only already-built exact machinery)

Per C147's own pearl (row 164, "sample the basis, not the circle"): both
`c(∇)` and `μ(∇)` are `ℝ`-linear in `∇` (established: `c` linear per
C147/C153; `μ(∇) = Σᵢ ⟨ψ₊, Eᵢ·spin_lift(∇ᵢ)·ψ₊⟩` manifestly linear). A ratio
constant at one point (`∇_LC`) says nothing about whether it is constant
everywhere in the family — that requires checking a *second*, independent
direction.

- **Test A (`S⁶`, 2-dim family, scalar/scalar — clean).** Compute `c(∇)` and
  `μ(∇)` exactly at `∇_LC` (`NOMIZU_A`, reproduces `-2√3/3` and `-√3`) and at
  `∇_LC∘J` (`NOMIZU_B`, C147b's own second, independent family direction).
  If `|c(∇_B)|/|μ(∇_B)|` is also exactly `2/3`, the ratio is constant on
  **both** independent basis directions of a 2-dim family, hence constant
  everywhere in it (linear algebra).

- **Test B (`SU(3)/T²`, 6-dim family — needs a well-posed scalar first).**
  `c(∇)` is 3×3-matrix-valued there; at `∇_LC` all 6 nonzero entries share
  exactly one magnitude (`2`), which is what let the LC-point ratio be
  formed at all. Test whether this **uniform-entry-magnitude property**
  itself holds across the family (not just at `∇_LC`) — this defines
  `|c(∇)|` as a genuine scalar function of `∇`, a claim that has NOT been
  checked anywhere yet and can fail on its own, independent of the ratio.

- **Test C (`SU(3)/T²`, contingent on B).** If B holds, test whether
  `|c(∇)|/|μ(∇)|` is constant `= 2/3` across the 6-dim family, using the same
  independent-basis-vector logic as Test A (6 basis directions, not 1).

## Kill criterion

- Test A: `|c(∇_B)|/|μ(∇_B)| ≠ 2/3` exactly → the `S⁶` "law" was a one-point
  coincidence, not a family-wide fact. Ratio-law FALSIFIED on `S⁶` alone.
- Test B: any family basis vector whose `c(∇)` has non-uniform nonzero-entry
  magnitudes → `|c(∇)|` is not a well-defined scalar on `SU(3)/T²`, and Test C
  cannot even be posed as stated (must be reformulated, e.g. via a norm/trace
  invariant, not asserted to hold by analogy with `S⁶`).
- Test C: any family basis vector where the ratio (however `|c(∇)|` ends up
  defined) differs from `2/3` → the cross-space `2/3` match was a two-point
  coincidence within an already-small population of near-rational numbers
  this project's own pearl row 54 already warns about.

## What would make this a strong result if it survives

A ratio constant across **both** independent 2-dim `S⁶` directions AND all
6 independent `SU(3)/T²` directions, with the SAME value `2/3` in both
spaces, is `2 (dim=6) + 2 (dim=2) - 2 (already known) = 4` new,
pre-registered, independently-falsifiable confirmations of a single
constant — a materially stronger evidential base than the 2-point coincidence
this file starts from, and per this project's own Independent Verification
Strength Ladder, still only "same construction, different connection", not
an independent verification of the CONSTANT's existence by another method.

## What this will NOT establish even if fully confirmed

1. Will NOT explain WHY `2/3` specifically (no derivation attempted here —
   this file tests robustness, not mechanism).
2. Will NOT bear on `N_gen=3` or any physical claim.
3. Will NOT extend beyond the two nearly-Kähler cosets this project can
   build (C140: `CP³`, `S³×S³` are ill-posed for this construction).
4. A confirmed family-wide ratio is still only `n=2` INDEPENDENT SPACES
   (many confirmations within each space are not independent of each
   other — they are the same underlying linear relation, just sampled at
   more points). Per this project's own row-54 discipline, a real third
   space would be needed to move past "a very clean two-point coincidence
   that also happens to be linear."
