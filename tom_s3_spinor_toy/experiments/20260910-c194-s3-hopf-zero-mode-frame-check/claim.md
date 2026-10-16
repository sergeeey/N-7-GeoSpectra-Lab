# C194 Claim — Does "U(θ,φ,ψ)·v" give Tom's four k=0 S³ spinors a non-constant Hopf form?

**Date:** 2026-09-10
**FL tier:** [ ] Micro [x] Standard [ ] Full
**Question type:** [x] descriptive [ ] predictive [ ] causal

---

## Prior Result Gate (MANDATORY — filled before writing anything below)

1. **Exact claim:** the map `ψ(θ,φ,ψ) = U(θ,φ,ψ)·v` (constant `v ∈ ℂ²`, `U`
   the already-verified Euler/Hopf `SU(2)` matrix from `c184_two_questions.py`)
   gives a genuinely `(θ,φ,ψ)`-dependent expression for Tom's four requested
   `k=0` objects `ψ_{(1/2,0)}`, `ψ_{(-1/2,0)}`, `ψ_{(0,1/2)}`, `ψ_{(0,-1/2)}`.
2. `decision.md` grep (`"U(theta,phi,psi)"`, `"group trivialization"`, `"zero mode"`):
   [x] done — hits reviewed: `C184` decision.md (defines the constants, does
   NOT compute this multiplication), `C184c`'s "F" section (substitutes Hopf
   into the **k=1** eigenspinors only, not k=0 — this round's own finding B
   is exactly that my candidate reproduces that k=1 result).
3. `round*_claim.md` + scripts grep: [x] done — `20260623-s3-spin-connection-to-tom-operators`
   found (single-angle spin connection, not this construction); `C187`/`C187b`
   found (independent vielbein+Cartan-connection attempt at an S³ Dirac
   operator — **failed**, 144 sign/pairing combinations, zero matches per
   `C188` decision.md §1 — a *different* failed route to a related goal, cited
   as related but not duplicate: C187 built a whole new operator, this round
   only tests one candidate frame map against the already-correct `D₀`).
4. `null_results/` + `parked/` grep: [x] done, 0 hits for this specific claim.
5. `git log -S/-G` pickaxe: [x] done, 0 hits (`Uh` and `HOPF` exist in prior
   commits but never multiplied together this way).
6. Primary source re-read: [x] done — Tom's 2026-09-10 letter, the exact
   sentence: *"I would like these harmonics expressed directly in the Hopf
   coordinates... These could be derived via the local ket spaces or using
   another method."*
7. **Status:** [x] NEW

---

## Estimand

**Population:** the 2-dimensional `D₀=0` eigenspace of the S³ Dirac-type
operator at `k=0` (the `(0,1/2)` chirality; the `(1/2,0)` chirality is the
mirror construction).
**Intervention:** apply the candidate frame map `ψ = U(θ,φ,ψ)·v`.
**Comparator:** the already-published `k=1` result (`C184c` §F) and the raw
constant-in-`x`-coordinates form (`C184` §1).
**Endpoint:** whether the resulting `(θ,φ,ψ)`-expression is (a) genuinely
non-constant and (b) still annihilated by the correctly-transformed `D₀`.
**Summary measure:** pass/fail on each of checks A–D below.
**MCID:** not applicable — this is an existence/identity question, not a
magnitude comparison.

---

## Claim

**H:** `U(θ,φ,ψ)·v` is a valid, non-constant, `D₀=0` Hopf-coordinate
expression for Tom's requested k=0 objects.

---

## Kill criterion

| Kill condition | Threshold |
|---|---|
| Candidate reproduces an *already-published, different-`k`* result | exact symbolic match (up to scalar) to any prior decision.md's printed spinor |
| Candidate is provably incapable of producing non-constant k=0 dependence at all | `U` shown to be homogeneous of degree ≠ 0 in `(x₀..x₃)`, while the true k=0 level is degree-0 by definition |

---

## Checks planned

| # | Check | Negative control |
|---|---|---|
| A1 | `U(θ,φ,ψ)` re-verified `== x₀I+x₁(iσ₁)+x₂(iσ₂)+x₃(iσ₃)|_Hopf` | if wrong, a random `(θ,φ,ψ)` point would show nonzero numeric residual — checked at 30-digit precision, not by symbolic `simplify` alone (known to under-simplify mixed exp/half-angle forms) |
| B1/B2 | candidate `U·(1,0)ᵀ` compared against `C184c`'s own printed `D₀=+3` (k=1) eigenspinor | if the candidate were genuinely a *new*, independent k=0 object, this comparison would show a generic, non-proportional difference — instead it is exactly proportional (−1), which is the kill signal itself |
| C1/C2 | `C188`'s closed-form `X_a^R` (Euler angles) applied to a symbolic constant and to `sp.Integer(1)` | if any `X_a^R` secretly carried a zeroth-order (non-derivative) term, `C1` would report a nonzero result on the constant `1` — it does not |
| D1 | `U`'s matrix entries checked for polynomial degree in `(x₀..x₃)` | a degree-0 (constant) result would refute the "dimension trap" explanation — instead degree is exactly 1, uniformly |

---

## What this does NOT mean

1. Does NOT prove no Hopf-coordinate-dependent expression can ever exist for
   these objects under ANY convention — only that this specific, most-natural
   candidate (left-multiplication by the fundamental `SU(2)` matrix) does not
   supply one, and that the operator `D₀` as this project has built it cannot
   distinguish among constants by position at all.
2. Does NOT touch `C184`/`C184b`/`C185`'s established results — the S²
   formulas and the S³ Dirac spectrum are unaffected.
3. Does NOT resolve what Tom actually wants when he asks for "expressed
   directly in Hopf coordinates" if the true answer is "there is nothing
   beyond the constant, in this operator's own frame" — that disambiguation
   is for the reply, not for this computation.

---

## Fence

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**REJECT** (the specific candidate H) — see `decision.md`.
**Evidence:** `[VERIFIED-sympy 6/6]`
**Status:** CLOSED — REJECT with a positive, quotable byproduct (see decision.md §3).
