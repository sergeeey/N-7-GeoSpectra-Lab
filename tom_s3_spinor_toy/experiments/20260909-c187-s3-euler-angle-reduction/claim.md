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

## Kill criterion (for claim (b) — RESOLVED 2026-09-09, see `c187b_periodicity_and_operator_check.py`)

> Reject (b) as stated only after the correct `(m,n)`-periodicity is derived
> and still fails to reproduce the known spectrum.

Both halves of that condition are now met. The periodicity is derived: `C186`'s
Cartan axis choice (quaternion `k`, index `a=2`) was arbitrary, and this
project's Euler-angle embedding has its own preferred axis — `X₀ᴸ = 2∂_φ` and
`X₀ᴿ = 2∂_ψ` exactly (quaternion `i`, index `a=0`), confirmed to `1e-30`
numerically. Rebuilding `C186`'s weight decomposition on that axis (a
relabelling, not new physics — `[D₀,J_L]=0`, `[D₀,J_R]=0` hold identically)
makes every extreme-weight state a single, clean Fourier mode, exactly the
shape this round's ansatz assumed. Applying `C187`'s own committed `D` operator
to that now-correctly-labelled candidate still does **not** return a constant
eigenvalue, checked under all 144 combinations of (which Pauli matrix pairs
with which vielbein leg) × (connection sign) × (operator sign).

**Verdict: claim (b) as stated is REJECTED — but the rejection is precise, not
generic.** The failure is not periodicity (that is closed) and not the
underlying physics (`C184`/`C186` untouched). It is localized to `C187`'s own
geometric construction of `D` — see decision.md §4 for the full account and
what would be needed to actually build the operator correctly.

## What this establishes

- **Claim (a): CONFIRMED.** The half-angle reduction mechanism generalises to
  the `S³` Dirac operator in Euler angles exactly as the pearl predicted —
  fast, polynomial, no transcendental slowdown.
- **Claim (b): REJECTED, precisely.** The `(m,n)` periodicity question is
  closed (derived, confirmed). What remains open is a distinct, narrower
  question: `C187`'s specific frame/connection construction of `D` does not
  match `C184`/`C186`'s operator, for a reason not yet isolated beyond "not a
  labelling issue, not a simple sign".
- **Does NOT touch any physics claim** in this project — `C184`/`C186`'s
  spectrum stands, verified by an entirely different method there, and is now
  cross-confirmed as internally consistent under an axis relabelling.
- **A general, reusable finding**, independent of `S³`: a geometric
  construction's own internal self-consistency checks (frame reproduces the
  metric, Cartan's equation solved with zero residual) do **not** certify that
  the resulting operator equals a specific, independently-built reference
  operator. That requires a cross-construction check — this round's real
  methodological contribution.
