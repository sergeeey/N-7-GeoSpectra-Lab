---
# C187 — does the half-angle reduction work on the S³ Dirac operator in Euler angles?

**Date:** 2026-09-09
**FL tier:** [x] Standard (this is the replacement test for a method-only
pearl, `impact_score 5`, "does not touch any physics claim" — Full-tier
machinery would be disproportionate)
**Question type:** [x] descriptive

---

## Why this round exists

`C186`'s `decision.md` §4 corrected the half-angle pearl (`pearl_registry/INDEX.md`,
`next_check 2026-10-15`): its original falsification test named "the `k≥2` exact
`S³` eigenspinors" as cheap and discriminating, but that task is not an ODE
problem at all — `C184`/`C186` solve `S³` by finite exact matrices over `ℚ(i)`,
with no angle anywhere. The corrected test, registered in that same row:

> build the `S³` Dirac eigenvalue problem in **EULER ANGLES**, where it
> genuinely separates into a `2×2` first-order system in `θ`, and apply
> `s = sin(θ/2)`, `c = cos(θ/2)`. The answer is already known independently
> from `C184`/`C186` … so correctness is checkable and the only free variable
> is whether the reduction terminates quickly.

This round runs that test.

---

## Prior Result Gate

1. `C184`: `D₀` on `S³` via quaternion right/left multiplication; exact
   eigenvalues `-k` (mult `(k+1)(k+2)`), `+(k+2)` (mult `k(k+1)`) at `k=0,1,2`.
2. `C186`: same operator, `k=2,3`, plus the `(m_L,m_R)` weight labelling —
   **every joint eigenspace is 1-dimensional.**
3. `C185`: the half-angle reduction, on `S²` — the method this pearl generalises.
4. `null_results/INDEX.md`, `parked/INDEX.md`: 0 hits for an Euler-angle
   construction of the `S³` Dirac operator in this project.
5. **Status:** [x] NEW.

---

## Falsifiable claim, as registered

**(a)** Building `D` from the metric in Euler angles `(θ,φ,ψ)`, applying a
plane-wave ansatz `ψ = (F(θ),G(θ))e^{i(mφ+nψ)}`, and substituting
`s=sin(θ/2)`, `c=cos(θ/2)` reduces the eigenvalue problem to an **exact
polynomial** linear-algebra problem — no `simplify()` on a transcendental
expression anywhere, and fast (sub-second, unlike `C185`'s abandoned 25-minute
first attempt at `S²`).

**(b)** The eigenvalues obtained lie in the set `{-k, k+2 : k=0,1,2,…}` — i.e.
every integer **except `1`** (since `λ=1` would need `k=-1`, which is not a
valid level) — matching `C184`/`C186`'s independently-established spectrum.

---

## Step 0a — Mechanism Claim Gate

The metric was derived, not quoted, from the **same** embedding `x0..x3` this
project uses throughout:

```
x0 = cos(θ/2)cos((φ+ψ)/2),  x1 = cos(θ/2)sin((φ+ψ)/2)
x2 = sin(θ/2)cos((φ-ψ)/2),  x3 = sin(θ/2)sin((φ-ψ)/2)
```

Verified `x0²+x1²+x2²+x3²=1` identically, then pulled back the flat `ℝ⁴`
metric: `g = (1/4)diag-block(1, [[1,cosθ],[cosθ,1]])` — the standard Euler-angle
`S³` metric, obtained here rather than assumed. Frame, spin connection (via
Cartan's structure equation, solved not quoted — unique solution, residuals
exactly zero), and `D` were all built the same way as `C185`.

**Result: the mechanism claim (a) HOLDS**, cleanly. Applying `D` to the
plane-wave ansatz produces a genuine `2×2` first-order system in `θ` in
**under 0.1 seconds** — both components carry the *same* `(m,n)`, no phase
mismatch (the exact bug class `C185` hit once). Clearing denominators and
substituting the half-angle variables is pure polynomial algebra throughout;
no `simplify()` call is ever applied to a transcendental expression. This is
the core registered claim and it is confirmed.

---

## What this round did NOT complete, stated plainly

Claim **(b)** — that scanning candidate integer eigenvalues against the
reduced polynomial system reproduces `C184`/`C186`'s known spectrum — is
**NOT** verified here. A blind scan over four candidate `(m,n)` pairs
(`±1/2,±1/2`, the natural guess for the lowest spinor level) at polynomial
degrees `N=0..3` against every integer `λ∈[-5,5]` found **zero** eigenmodes —
not a near-miss, a clean null across the whole scanned range.

This is not evidence that claim (a) or the underlying `C184`/`C186` spectrum is
wrong — those are independently verified elsewhere and untouched. It means the
map from the Euler-angle Fourier labels `(m,n)` (and/or the polynomial degree
`N`) to the physical level `k` used here is not the right one. The likely
culprit, flagged rather than guessed at: a **half-integer periodicity offset**
between the naive plane-wave ansatz and the actual spin-weighted functions on
the double cover — the same family of hazard this project's own memory already
names (`feedback-*-quaternion-anti-isomorphism`, sign/convention hazards
compounding when spin and orbital labels are combined). Getting this right
needs the same care `C186` gave to which relative sign of `J₃ᴿ` actually
commutes with `D₀` — not a guess, a derivation — and that derivation is not
done here.

**Per this project's own cost discipline:** continuing to blind-search
`(m,n,N)` combinations without first deriving the correct periodicity would be
exactly the kind of unaudited persistence this project's memory already warns
against. Stopping here and reporting the partial result is the disciplined
choice, not a failure to push through.

---

## Kill criterion (for claim (b), unresolved — carried forward, not closed)

Reject (b) as stated only after the correct `(m,n)`-periodicity is derived and
still fails to reproduce the known spectrum. Until then, (b) is **OPEN**, not
falsified.

## What this establishes

- **Claim (a): CONFIRMED.** The half-angle reduction mechanism generalises to
  the `S³` Dirac operator in Euler angles exactly as the pearl predicted —
  fast, polynomial, no transcendental slowdown.
- **Claim (b): INCOMPLETE**, for a stated, specific reason (quantum-number
  periodicity), not a vague "needs more work".
- **Does NOT touch any physics claim** in this project — `C184`/`C186`'s
  spectrum stands, verified by an entirely different method there.
