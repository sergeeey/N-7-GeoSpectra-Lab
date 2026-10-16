---
# C189 — derive the `3/2` shift, don't fit it

**Date:** 2026-09-09
**FL tier:** [x] Standard (single well-scoped derivation building on `C184`/
`C188`'s already-verified `D₀` and `X_a^R`, not a new open-ended physics
programme)
**Question type:** [x] descriptive

---

## Why this round exists

The letter to Tom names its own gap explicitly, twice:

> The `3/2` is matched, not derived. What is derived is the spectrum of `D₀`;
> that the constant's *value* is `3/2` comes from setting `D₀`'s spectrum
> against the known `±(l+3/2)`, which I have taken from the literature rather
> than derived.

and again in the second message:

> One exception to "exact" … the `3/2` … is matched, not derived. The
> spectrum it is matched against I took from the literature.

This round removes that exception: derive the constant from this project's
own geometry, and only afterward compare to the literature value as a
cross-check — not the other way around.

---

## Prior Result Gate

1. `C184`/`C188`: `D₀ = -i Σₐ σₐ Xₐᴿ`, exact spectrum `-k` (mult
   `(k+1)(k+2)`), `+(k+2)` (mult `k(k+1)`), verified by two independent
   methods (matrix, and quaternion-native coordinate construction).
2. `C185`/`C187`/`C188`: this project's established method for building a
   genuine spin connection — solve Cartan's structure equation, verify zero
   residual, never quote a connection formula.
3. `references/camporesi_higuchi_grqc9505009.pdf` (gr-qc/9505009): the source
   the letter cites for `±(l+3/2)`. Used here **only for the final
   cross-check**, after the derivation — not as an input to it.
4. **Novelty Check (Step -3), done properly rather than assumed clean.** The
   pearl registry names two pieces of prior work that *look* adjacent and
   are not the same claim:
   - `experiments/20260717-round67-…` USES `±(n+3/2)` as its input,
     explicitly marked *"already-established, G8/G4, not re-derived here"* —
     traced back to `experiments/20260615-g8-…`, which hardcodes
     `±(m+3/2)/ρ` as a bare formula with no derivation in the code at all.
     A literature citation, same as the letter's own.
   - `experiments/20260810-c11-a1-iota-flips-dirac` ("A1/C55") cross-checks
     round67's numbers against a **second**, independently-sourced formula,
     `λ(j,k)=(j+k+1)·sign(k−j)` from Peter–Weyl representation theory — but
     that formula is itself taken as a standard fact about invariant Dirac
     operators on compact Lie groups, not derived from this project's own
     geometry either. A1's actual target claim was a different question
     (does the orientation-reversal map flip `D`'s sign); the spectrum match
     was a side cross-check, not its own derivation.

   **Neither prior round builds the actual Levi-Civita connection.** Both
   treat `±(l+3/2)` as a known input to be matched or cross-matched. `C189`
   is the first round in this project to compute the connection-correction
   constant from the genuine spin connection, solved via Cartan's structure
   equation on this project's own explicit frame — a third, independent,
   and this time first-principles method. Recorded here so a future reader
   does not mistake round67/A1 for prior derivations of the same fact.
5. **Status:** [x] NEW — by the Novelty Check above, not merely asserted.

---

## The mechanism, stated precisely

`D₀` is built from `Xₐᴿ` treated as bare vector fields — it does not know
that `S³` is curved. The genuinely covariant Dirac operator is
`D_full = -i Σₐ σₐ ∇_{Xₐ}`, where `∇` is the Levi-Civita connection's spin
lift. The two differ by exactly the spin-connection term:

```
D_full - D₀ = -i Σₐ σₐ Γ(Xₐ)
```

where `Γ` is the connection 1-form. **The letter's own argument for why this
difference should be a constant**: `S³` is homogeneous, every point looks
like every other, so a quantity built purely from the local geometry cannot
vary with position. This round checks that argument by direct computation
rather than accepting it as self-evident.

---

## Step 0a — Mechanism Claim Gate

Two sentences do real work here and are checked, not assumed:

1. *"`{X₀ᴿ,X₁ᴿ,X₂ᴿ}` is an orthonormal frame."* Checked directly: `g(Xₐᴿ,
   Xᵦᴿ)` (the ambient `ℝ⁴` dot product, restricted to the unit sphere) equals
   `δₐᵦ` exactly — no rescaling needed. (`P1`)
2. *"The connection-correction term is a constant on `S³`."* Checked by
   actually building the Levi-Civita connection in the `{Xₐᴿ}`-dual coframe
   via Cartan's structure equation (unique solution, zero residual — `P3`,
   `P4`) and computing `D_full - D₀` explicitly. **Verdict: HOLDS** — the
   result is `diag(-3/2, -3/2)`, position-independent (`P5`).

---

## Falsifiable claim

**(a)** `D_full - D₀` is a scalar matrix (proportional to identity),
independent of `(θ,φ,ψ)`.

**(b)** Its value is exactly `-3/2` (matching the letter's fitted magnitude
`3/2`, sign consistent with the letter's own statement that the `k=0` states
sit at `|λ|=3/2` with `D₀`-eigenvalue `0` shifting to a **negative** value).

**(c)** Combining this derived shift with `D₀`'s own already-verified
spectrum reproduces the general `±(l+3/2)`, multiplicity `(l+1)(l+2)` per
sign — computed here from `C184`/`C188`'s own numbers, not copied from
Camporesi–Higuchi.

---

## Kill criterion

**REJECTED** if `D_full - D₀` is not a scalar matrix, or its value is not
`-3/2`, or the shifted `D₀` spectrum does not reproduce `±(l+3/2)` with
multiplicity `(l+1)(l+2)`.

## Negative control

Three deliberately wrong connections are tested (`P8`–`P10`):
- **no connection at all** (`ω=0`) gives extra term `0` — confirms the shift
  genuinely comes from the connection, not from some other artifact of the
  computation.
- **one sign flipped** (`ω₁₂ → -ω₁₂`) gives a *different* constant, `-1/2`,
  not `-3/2` — the check discriminates by value, not merely by
  "is-it-constant" (several wrong connections still happen to give
  constants, an honest finding recorded rather than hidden).
- **genuinely structure-broken** (`ω₁₂` plus an extra `sin(2θ)` term with no
  geometric justification) gives a non-constant, non-diagonal leftover —
  confirming "constant" is not a forced or trivial outcome of this
  calculation.

## What this establishes

- **The `3/2` shift is derived**, not fitted: built from this project's own
  frame, its own metric, and Cartan's structure equation — the same
  discipline `C185`/`C187`/`C188` already used for every other connection in
  this project.
- **The literature value is now a cross-check, not an input.** `±(l+3/2)`,
  mult `(l+1)(l+2)` per sign, comes out of combining the derived shift with
  `D₀`'s own independently-verified spectrum.
- **Does not derive the shift for the left-acting operator** (the letter's
  own mirror-image case, `-3/2 → +3/2`) — not attempted this round, a cheap
  natural follow-up given the machinery already built.
- **Does not extend beyond the frame already verified in `C188`** — this
  round adds the connection on top of that frame, not a new geometric
  construction.
