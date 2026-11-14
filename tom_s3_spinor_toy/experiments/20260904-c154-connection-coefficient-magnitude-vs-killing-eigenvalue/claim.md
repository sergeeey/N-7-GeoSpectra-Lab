# C154 — does `|c(∇)| = (2/3)·μ(∇)` hold across the whole connection family?

**Question type (EstimandOps L0): DESCRIPTIVE.**

## ⚠️ SECOND CORRECTION, same day — the "family-wide law" is forced, not discovered

This file went through two skeptic-driven reversals in one day. Both are
kept, in order, per this project's discipline.

**v1 (original):** scalarisation `⟨ψ₊,D_Σ(∇)ψ₊⟩/⟨ψ₊,ψ₊⟩`, found FALSIFIED
at the independent basis direction (`μ=0` there).

**v2:** a context-blind skeptic (could not execute code) showed v1's
scalarisation was an arbitrary projection discarding the `ψ₋` component
(`D_Σ(∇_LC∘J)ψ₊ = i√3·ψ₋`, hand-derived, then tool-verified). Corrected to
the full norm `μ(∇) := ‖D_Σ(∇)ψ₊‖/‖ψ₊‖`, found CONFIRMED at 3 points
(`∇_LC`, `∇_LC∘J`, their sum), reported as "a genuine, non-tautological
3-point confirmation, not a 1-point coincidence."

**v3 (this version):** a SECOND context-blind skeptic pass, independently
re-checking the corrected package, found v2's own "non-tautological"
framing was wrong. **Verified directly by tool execution, not taken on
either skeptic's word:**

```
<psi_+, psi_-> = 0                                          [exact orthogonality,
                                                               visible from their raw
                                                               definitions, C147b/round59]
<D(nabla_LC)psi_+, D(nabla_LC.J)psi_+> = 0                   [FORCED by the line above]
mu(a,b) = sqrt(3)*sqrt(a^2+b^2)  EXACTLY, at a RANDOM (a,b)  [closed form, not
                                                               just the 3 tested points]
c_B/c_A = i   (C147b's own already-registered exact result)
Re(conj(c_A)*c_B) = 0                                        [FORCED by the line above]
|c(a,b)|/mu(a,b) = 2/3  EXACTLY, at the SAME random (a,b)
```

**Both quadratic forms `|c(∇)|²` and `μ(∇)²` are forced to be conformal
(`∝ a²+b²`) by facts already on record before this round ran** — `ψ₊⊥ψ₋`
(visible from their definitions in `round59_route_a_independent.py`, no
computation needed) and `c_B = i·c_A` (C147b, already committed). Given
conformality on both sides, agreement at a THIRD point (`∇_LC+∇_LC∘J`) adds
**zero** new information beyond agreement at the first two — it does not
distinguish this from a proportionality that was forced to hold everywhere
the moment both cross-terms vanished.

**The only genuinely new number in this whole investigation is the single
ratio at the Levi-Civita point, `|c(∇_LC)|/μ(∇_LC) = 2/3`** — the same
2-point (`S⁶`, `SU(3)/T²`) coincidence this round set out to explain,
**not strengthened into family-wide evidence**. This is the same class of
overclaim this project already downgraded once today (C153's per-plane law,
forced by Schur's lemma) — here the forcing mechanism is orthogonality +
an already-registered exact ratio, not Schur's lemma, but the shape of the
error is identical: a numeric pattern that looked like a discovery collapses,
under closer inspection, to already-known structure plus one number.

## What survives

- The `S⁶` closed form is real and exact: `|c(a,b)| = (2/√3)√(a²+b²)`,
  `μ(a,b) = √3·√(a²+b²)`, ratio `= 2/3` identically — but this is a
  **derivation**, not independent evidence: it follows in two lines from
  `ψ₊⊥ψ₋` and C147b's `c_B=i·c_A`, both already on record.
- `|c(∇_LC)|/μ(∇_LC) = 2/3` remains true and **still unexplained** — no
  mechanism for why this specific ratio holds AT the Levi-Civita point
  itself was found by this round.

## `SU(3)/T²` — a genuine, separate, previously-unflagged gap found in C153

Independent of the `S⁶` question: `experiments/20260904-c153.../
c153_step2_exact_rational_verification.py`'s `sector_basis_exact()` builds
`dom_sym`/`tgt_sym` from raw `sympy.Matrix.nullspace()` output with **no
Gram-Schmidt orthonormalisation** — unlike `S⁶`'s `c147b`, which explicitly
calls `R59.gram_schmidt(...)`. Checked directly: both Grams happen to equal
`2·I₃` exactly (a fortunate accident of this particular nullspace call, not
guaranteed by construction), so `SU(3)/T²`'s `c(∇)` values are proportional
to genuine invariants, but scaled by an unaccounted factor relative to a
properly unit-normalised convention (a factor of `2` in `‖c‖²`, i.e. `√2`
per side) — meaning C153's own "uniform magnitude `2`" finding, and every
number derived from it since, has never been checked against a
unit-normalised target sector. **This does not change any C153 verdict**
(ratios and sign patterns computed there are scale-invariant), but it is a
real, load-bearing gap in what "the connection coefficient's magnitude" on
`SU(3)/T²` actually means in absolute terms, and should be fixed before any
future round compares `SU(3)/T²`'s `c` magnitude against anything external.

Given this, and given the Frobenius-norm-based family test on `SU(3)/T²`
(6 basis directions: ratio `2√2`, constant but `≠2/3`; the sum: `2√6`; the
actual Levi-Civita vector: `2√6/3`) did not reproduce `2/3` at ANY point
even before normalisation is fixed, `SU(3)/T²` remains **genuinely open**,
now for two compounding reasons: an unresolved scalarisation choice AND an
unnormalised basis.

## What this does NOT establish

1. Does NOT establish a family-wide `S⁶` "law" as independent evidence —
   it is a 2-line consequence of already-registered facts (C147b, and the
   raw definitions of `ψ₊`/`ψ₋`).
2. Does NOT explain the single surviving fact — `2/3` at the Levi-Civita
   point on `S⁶`, and separately (now known to be on an unnormalised
   basis) on `SU(3)/T²` — no mechanism found.
3. Does NOT establish anything on `SU(3)/T²` — genuinely open, compounded
   by the newly-found normalisation gap in C153.
4. Does NOT bear on `N_gen=3` or any physical claim.
5. Does NOT claim the "3-point / non-tautological" framing from the
   previous version of this file — withdrawn, see the correction above.
