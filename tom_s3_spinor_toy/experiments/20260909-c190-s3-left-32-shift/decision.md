# C190 Decision — PROMOTE, with a correction. The `3/2` magnitude holds for the left-acting operator; the letter's handedness-to-sign assignment does not.

**Date:** 2026-09-09
**Verdict:** **PROMOTE** — `16 of 16` checks pass. The connection-correction
constant for the LEFT-acting `S³` Dirac operator is derived, the same way
`C189` derived the right-acting one, to be exactly `+3/2`. That confirms the
letter's stated *magnitude*. It does **not** confirm the letter's stated
*handedness-to-sign assignment*: cross-checking both candidate signs against
the known-correct external spectrum shows the derived pairing is
right→`−3/2`, left→`+3/2` — the reverse of what the letter states.

All numbers trace to `c190_left_32_shift.py` and `run_output.txt`.

---

## 0. Novelty check, done before writing this up as new

`pearl_registry/INDEX.md`, `null_results/INDEX.md`, `parked/INDEX.md`: no
prior entry derives a left-handed connection-correction constant on `S³` for
this project. `C189` derived the right-handed constant; nothing before this
round built the left-handed connection.

## 1. What was open

The letter states, in passing: *"the left-acting version is an equally good
operator, and it produces the mirror-image spectrum, with the constant below
coming out `−3/2` instead of `+3/2`"* — i.e. right→`+3/2`, left→`−3/2`. This
was never derived for either handedness before `C189`/`C190`; `C189` closed
the right-handed half. This round closes the left-handed half, the same way.

## 2. What is now closed

`D₀ᴸ = -i Σₐ σₐ Xₐᴸ` (left-multiplication generators, established since
`C184`) omits the same spin-connection term `C189` restored for the
right-acting operator. This round builds it from the actual Levi-Civita
connection in the `{X₀ᴸ,X₁ᴸ,X₂ᴸ}` frame:

1. **The frame is orthonormal**, exactly, on the unit sphere — `g(Xₐᴸ,X_bᴸ) =
   δₐ_b·(x0²+..+x3²)` identically (`P1`).
2. **`Xₐᴸ` in Euler-angle coordinates**, derived via least-squares against
   the embedding Jacobian and cross-checked against a closed form to
   `<1e-25` (`P2a/b`–`P4a/b`).
3. **The Levi-Civita connection**, solved from Cartan's structure equation in
   the dual `L`-coframe, unique solution (`P6`), zero residual (`P7`):
   ```
   ω₀₁ = (sin φ/2, 0, −sin θ cos φ/2)
   ω₀₂ = (−cos φ/2, 0, −sin φ sin θ/2)
   ω₁₂ = (0, 1/2, cos θ/2)
   ```
4. **`D_full^L − D₀ᴸ` is exactly `diag(+3/2, +3/2)`** — a
   position-independent scalar matrix (`P8`), value `+3/2` exactly (`P9`).

## 3. `D₀ᴸ`'s own spectrum really is `D₀ᴿ`'s mirror image

Computed directly via the harmonic-basis operator-matrix method (same method
`C184`/`C188` used for `D₀ᴿ`), for `k=0,1,2`: `D₀ᴸ`'s spectrum is exactly
`D₀ᴿ`'s spectrum negated — `{+k: (k+1)(k+2), −(k+2): k(k+1)}` against the
known `D₀ᴿ = {−k: (k+1)(k+2), +(k+2): k(k+1)}` (`P10`–`P12`, all three
levels exact, no approximation). **This part of the letter's claim is
correct** — the two operators genuinely are mirror images of each other.

## 4. The discrepancy — checked twice, not asserted once

Feeding `D₀ᴿ`'s own already-verified spectrum (`N=20` levels) through both
candidate shifts and testing against the known-correct external pattern
`±(l+3/2)`, multiplicity `(l+1)(l+2)` per sign (`P13`):

| shift applied to `D₀ᴿ` | eigenvalues checked | mismatches | spurious sub-`3/2` values |
|---|---|---|---|
| `−3/2` (`C189`'s + this round's derived value for R) | 36 | **0** | none |
| `+3/2` (the letter's stated expectation for R) | 33 | **32** | `±1/2` |

`S³`'s positive curvature forbids `\|λ\| < 3/2` for the Dirac spectrum — the
`+3/2`-for-right reading produces eigenvalues the geometry itself rules out,
on top of failing 32 of 33 comparable entries. The `−3/2`-for-right reading
(this project's actual derivation) matches all 36 with zero error. **The
letter's aside on which handedness gets which sign was, by the letter's own
admission elsewhere, never itself derived** — this is a correction of an
unverified guess, not a disagreement with a previously-computed result.

## 5. Floor–Ceiling (Step 4a)

Same metric as `C189`: **is the connection-correction term a constant, and
which one.**

| | construction | result |
|---|---|---|
| **floor** | no connection at all (`ω=0`) | extra term `= 0` exactly |
| **ceiling / observed** | the Cartan-derived L-connection | extra term `= diag(+3/2,+3/2)` exactly |

Floor = 0. Ceiling = 3/2 (the value the correct connection attains exactly,
not approached). Observed = 3/2. Efficiency = (observed - floor) / (ceiling
- floor) = (3/2 - 0) / (3/2 - 0) = 1.0 -- the derivation lands exactly on
the ceiling, not partway between floor and ceiling.

## 6. What this does NOT establish

- **Does not re-derive `C189`'s right-handed result** — `C189`'s `−3/2` for
  `D₀ᴿ` is reused here as an already-verified input for §4's cross-check,
  not recomputed from scratch.
- **Does not re-derive `D₀ᴸ`'s own spectrum beyond `k=0,1,2`** — the pattern
  is exact at every level checked and follows the same construction
  `C184`/`C188` already validated more broadly for `D₀ᴿ`, but this round did
  not re-run the broader-`k` sweep for the `L`-side specifically.
- **Does not touch `S²` (`C185`) or the Euler-angle periodicity question
  (`C187b`)** — orthogonal to both.
- **Does not establish why the letter's aside had the assignment backwards**
  — only that it does; no claim is made here about the origin of that
  specific error.

## 7. Consequence for the letter

The letter's aside — *"the left-acting version... constant coming out `−3/2`
instead of `+3/2`"* — is factually backwards per this derivation: the
correct pairing is right→`−3/2`, left→`+3/2`. **The draft has not been
edited.** Per this session's standing practice (same as `C189` §6),
changing sent-adjacent text re-opens the blind-read and Submission Gate it
already passed in its current wording; that is the user's call, not made
here.

Unchanged: the letter is not sent, cooling-off has not elapsed, and **DO NOT
INITIATE CONTACT** with Tom Lawrence stands.

## 8. Reproduction

```
cd experiments/20260909-c190-s3-left-32-shift
python c190_left_32_shift.py
```

`16/16`. `ruff check` and `ruff format`: clean.
