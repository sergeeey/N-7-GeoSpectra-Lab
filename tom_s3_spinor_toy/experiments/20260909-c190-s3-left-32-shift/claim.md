---
# C190 — derive the connection-correction shift for the LEFT-acting operator

**Date:** 2026-09-09
**FL tier:** [x] Standard (mirror of `C189`, same scope discipline)
**Question type:** [x] descriptive

---

## Why this round exists

`C189` derived the connection-correction shift for `D₀ᴿ` (`-3/2`, from the
actual Levi-Civita connection, not fitted). The letter to Tom makes a
further, adjacent claim about the left-acting version, in passing:

> using the right-acting generators rather than the left-acting ones is a
> convention: the left-acting version is an equally good operator, and it
> produces the mirror-image spectrum, with the constant below coming out
> `−3/2` instead of `+3/2`.

Read plainly, this says: right-acting → `+3/2`, left-acting → `−3/2`. This
round computes the left-acting shift directly, the same way `C189` computed
the right-acting one, to check that claim rather than assume it.

---

## Prior Result Gate

1. `C189`: `D_full^R − D₀ᴿ = −3/2` exactly, derived via Cartan's structure
   equation, cross-checked against `±(l+3/2)`, mult `(l+1)(l+2)` with zero
   mismatches.
2. `C184`/`C188`: `X_a^L` generators, `[X_a^L,X_b^L]=2εabc X_c^L`, `[X_a^L,
   X_b^R]=0` — established since `C184`.
3. `null_results/INDEX.md`, `parked/INDEX.md`: 0 hits for a derived
   left-handed connection-correction constant on `S³`.
4. **Status:** [x] NEW.

---

## Falsifiable claim

**(a)** `{X_0^L,X_1^L,X_2^L}` is orthonormal on the unit `S³` (same argument
as `C189`'s right-handed check).

**(b)** `D_full^L − D₀ᴸ` is a scalar matrix, position-independent.

**(c)** Its value is `+3/2` (the magnitude the letter states, sign matching
the letter's *own* stated pattern for the left-handed case).

**(d)** `D₀ᴸ`'s own spectrum (no connection) is exactly the *negation* of
`D₀ᴿ`'s spectrum, level by level — the genuinely mirror-image relationship
the letter's broader statement describes.

---

## Kill criterion

**REJECTED** if `D_full^L − D₀ᴸ` is not scalar, or its value is not `3/2`
in magnitude, or `D₀ᴸ`'s spectrum is not `D₀ᴿ`'s negation.

## What was actually found — a correction, not a confirmation

Claims (a), (b), (d) hold exactly, verified the same way as `C189`.

**Claim (c) does not hold as the letter states it.** The computed shift for
`D_full^L − D₀ᴸ` is `+3/2` — correct in *magnitude*, matching the letter —
but this means the letter's implied assignment for the *right*-acting
operator (`+3/2`) is backwards: `C189` already established, and this round
re-confirms by an independent cross-check (§F, below), that the right-acting
shift is `−3/2`, not `+3/2`.

**This is checked twice, not asserted once.** Feeding `D₀ᴿ`'s own
already-verified spectrum through **both** candidate shifts and testing
against the known-correct `±(l+3/2)` pattern:

| shift applied to `D₀ᴿ` | eigenvalues checked | mismatches | spurious sub-floor values |
|---|---|---|---|
| `−3/2` (this project's derived value) | 36 | **0** | none |
| `+3/2` (the letter's implied expectation for R) | 33 | **32** | `±1/2` (physically forbidden — `S³`'s positive curvature forbids `\|λ\|<3/2`) |

The `+3/2`-for-right reading fails decisively and introduces eigenvalues
the sphere's own geometry rules out. The letter's aside on this point was,
by its own admission elsewhere, never itself derived — no connection was
built for either handedness before this session — so this is a correction
of an unverified expectation, not a disagreement with a computed result.

## Negative control

None needed beyond `C189`'s own (§E there): the same Cartan-equation
apparatus, applied here to the `L`-frame, is the identical mechanism already
stress-tested against wrong connections in `C189`.

## What this establishes

- **The magnitude `3/2` is confirmed for both handedness**, derived by the
  same first-principles method for each.
- **The handedness-to-sign assignment in the letter is corrected**: right →
  `−3/2`, left → `+3/2` (not the reverse the letter states).
- **`D₀ᴸ = −D₀ᴿ`'s spectrum, level by level** — genuinely mirror-image, the
  part of the letter's claim that *was* right.
- **Does not re-derive `C189`'s right-handed result** — reuses it as an
  already-verified input for the cross-check in §F.
