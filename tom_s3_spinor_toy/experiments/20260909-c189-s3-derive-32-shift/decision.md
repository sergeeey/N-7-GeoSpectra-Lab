# C189 Decision — PROMOTE. The `3/2` is derived, exactly, and the letter's own honest caveat can now be dropped.

**Date:** 2026-09-09
**Verdict:** **PROMOTE** — `10 of 10` checks pass. The connection-correction
constant relating `D₀` to the genuinely covariant `S³` Dirac operator is
computed from this project's own geometry to be exactly `-3/2`, not fitted
against the literature. The resulting full spectrum matches `±(l+3/2)`,
multiplicity `(l+1)(l+2)` per sign, exactly.

All numbers trace to `c189_derive_32_shift.py` and `run_output.txt`.

---

## 0. Novelty check, done before writing this up as new

Before treating this as a new result, `pearl_registry/INDEX.md` and the
project's own experiment history were checked for prior derivations of the
same constant — not assumed clean. Two adjacent-looking prior rounds exist:
`round67` (2026-07-17) uses `±(n+3/2)` as an input explicitly marked *"not
re-derived here,"* traced back to `G8` (2026-06-15), which hardcodes
`±(m+3/2)/ρ` with no derivation. `A1/C55` (2026-08-10) cross-checks
round67's numbers against a Peter–Weyl representation-theory formula,
`λ(j,k)=(j+k+1)·sign(k−j)` — itself a quoted standard fact, not derived from
this project's geometry, and used there to answer a *different* question
(does the orientation map flip `D`'s sign). **Neither builds the actual
connection.** `C189` is the first round to compute the shift from the
genuine Levi-Civita connection via Cartan's structure equation, on this
project's own frame — see `claim.md` §Prior Result Gate item 4 for the full
account.

## 1. What was open

The letter to Tom flags its own gap, in its own words, twice: *"the `3/2` is
matched, not derived… the spectrum it is matched against I took from the
literature."* This is the one place in the letter where "exact" was used
loosely — everything else in the letter is either computed from this
project's own construction or explicitly marked as a convention.

## 2. What is now closed

`D₀ = -i Σₐ σₐ Xₐᴿ` (from `C184`/`C188`) omits the spin-connection term a
genuinely covariant Dirac operator carries. This round builds that term from
the actual Levi-Civita connection of `S³`, in the frame `{X₀ᴿ,X₁ᴿ,X₂ᴿ}`
already verified exact in `C188`:

1. **The frame is orthonormal**, exactly, on the unit sphere — checked
   directly against the ambient `ℝ⁴` metric (`P1`), not assumed.
2. **The Levi-Civita connection**, solved from Cartan's structure equation
   in the dual coframe (`P2`–`P4`), unique solution, zero residual:
   ```
   ω₀₁ = (sin ψ/2, −sin θ cos ψ/2, 0)
   ω₀₂ = (cos ψ/2, sin ψ sin θ/2, 0)
   ω₁₂ = (0, −cos θ/2, −1/2)
   ```
3. **`D_full − D₀` is exactly `diag(−3/2, −3/2)`** — a position-independent
   scalar matrix (`P5`), value `−3/2` exactly (`P6`). This is the *derived*
   answer to the letter's own open question.

## 3. Cross-check against the literature, done the right way around

Combining the derived `−3/2` with `D₀`'s own already-verified spectrum
(`k=0..N`, `-k` mult `(k+1)(k+2)`, `+(k+2)` mult `k(k+1)`, exact integers)
gives, for `N=12` levels:

```
D_0 nonzero-mult values, shifted by -3/2:
  ..., -6.5, -5.5, -4.5, -3.5, -2.5, -1.5, 1.5, 2.5, 3.5, 4.5, 5.5, ...
```

which matches `±(l+3/2)`, multiplicity `(l+1)(l+2)` **per sign**, for `20`
common eigenvalues checked well inside the truncation range (`P7`, boundary
effects at the extreme ends excluded as truncation artifacts, not
mismatches — verified by extending the range and confirming the boundary
values are simply outside both finite lists, not genuinely absent).

**Note the multiplicity formula simplified.** The letter's own table lists
`(k+1)(k+2)` for the negative branch and `k(k+1)` for the positive branch —
two different-looking formulas. After the `−3/2` shift and relabeling by
`l` (negative branch: `l=k`; positive branch: `l=k−1`), **both branches
carry the same formula, `(l+1)(l+2)`** — the standard, symmetric
Camporesi–Higuchi result. This symmetry was not visible in `D₀`'s own
table and only emerges after the derived shift is applied — a genuine
consequence of the derivation, not built in by construction.

## 4. Floor–Ceiling (Step 4a)

The metric is **is the connection-correction term a constant, and which
one**. Section E (`P8`–`P10`) supplies both ends directly:

| | construction | result |
|---|---|---|
| **floor** | no connection at all (`ω=0`) | extra term `= 0` exactly — the shift is entirely attributable to the connection, not to some artifact of the calculation |
| **wrong-but-still-constant** | one sign flipped (`ω₁₂ → −ω₁₂`) | extra term `= diag(−1/2,−1/2)` — a genuine wrong answer, and importantly still *constant*, which is why "is it constant" alone would not have been a sufficient check |
| **ceiling / observed** | the Cartan-derived connection | extra term `= diag(−3/2,−3/2)` exactly |

Floor = 0. Ceiling = -3/2 (the value the correct connection attains exactly, not approached). Observed = -3/2. Efficiency = (observed - floor) / (ceiling - floor) = (-3/2 - 0) / (-3/2 - 0) = 1.0 — the derivation lands exactly on the ceiling, not partway between floor and ceiling.

**The honest limitation surfaced by this table:** "the extra term is
constant" is *not* by itself a discriminating check — three different wrong
connections were tried and two of them (`ω=0`, `ω₁₂` flipped) also gave
constants (just the wrong ones). What discriminates is the *value*, `−3/2`
specifically, obtained only from the connection that actually satisfies
Cartan's equation with zero residual. `P10`'s genuinely structure-broken
connection (an ad hoc `sin(2θ)` term with no geometric basis) does break the
constancy, confirming the property is not simply forced by the algebra
regardless of input — but it took a more aggressive perturbation than a
sign flip to show that.

## 5. What this does NOT establish

- **Does not derive the mirror (`+3/2`) shift for the left-acting operator.**
  The letter states this exists by a handedness argument; not computed here.
  A natural, cheap follow-up given `X_a^L` is already available throughout
  this project.
- **Does not re-derive `D₀`'s own spectrum** — that is `C184`/`C188`'s
  result, used here as an input, not reproduced from scratch.
- **Does not extend the frame construction** — uses exactly the `{X_a^R}`
  frame `C188` already verified; this round adds the connection on top of
  it.
- **Does not touch anything about the `S²` construction** (`C185`) or the
  Euler-angle periodicity question (`C187b`) — orthogonal to both.

## 6. Consequence for the letter

The letter's caveat — *"the `3/2` is matched, not derived"* — is no longer
accurate as a limitation of this project's own work. **The draft has not been
edited.** Per this session's standing practice, changing sent-adjacent text
re-opens the blind-read and Submission Gate it already passed in its current
wording; that is the user's call. What would change, concretely: the
sentence in `§6`/`§7` naming this as an open exception to "exact" could be
replaced by the derivation above, or the caveat could simply be dropped.

Unchanged: the letter is not sent, cooling-off has not elapsed, and **DO NOT
INITIATE CONTACT** stands.

## 7. Reproduction

```
cd experiments/20260909-c189-s3-derive-32-shift
python c189_derive_32_shift.py
```

`10/10`. `ruff check` and `ruff format`: clean.
