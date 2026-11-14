---
# C188 — rebuild the S³ Euler-angle Dirac operator FROM the quaternion generators

**Date:** 2026-09-09
**FL tier:** [x] Standard (this is the recorded next step from `C187b`'s
decision.md §4c, not a new physics claim — resolves a construction question)
**Question type:** [x] descriptive

---

## Why this round exists

`C187` built the `S³` Dirac operator in Euler angles from an independently
chosen vielbein + Cartan connection. It passed all nine of its own internal
consistency checks and still did not reproduce `C184`/`C186`'s known
spectrum, even after `C187b` correctly derived the `(m,n)` periodicity and
ruled out 144 sign/pairing combinations as the cause (see `C187b`'s
`decision.md` §4). The finding recorded there: self-consistency of a
geometric construction does not certify it equals a specific,
independently-built reference operator.

`C187b`'s own §4c named the fix: **build `D` directly from the quaternion
generators**, expressed in Euler-angle coordinates via the chain rule, rather
than from an independently chosen frame. Since `D₀ = -i Σₐ σₐ Xₐᴿ` is exactly
how `C184`/`C186` define the operator, and `Xₐᴿ` is a specific, already-fixed
vector field (quaternion right multiplication), re-expressing `Xₐᴿ` in new
coordinates is a **change of variables**, not an independent re-derivation —
it is guaranteed to agree with `D₀`, not merely hoped to.

---

## Prior Result Gate

1. `C184`/`C186`: `D₀ = -i Σₐ σₐ Xₐᴿ` on `S³`, exact spectrum `-k` (mult
   `(k+1)(k+2)`), `+(k+2)` (mult `k(k+1)`) for `k=0,1,2,3`.
2. `C187`: built `D` in Euler angles via vielbein + Cartan connection.
   Internally self-consistent (`P1`–`P9`), does not match `D₀`.
3. `C187b`: derived the `(m,n)` periodicity (quaternion "i" axis, not "k").
   Ruled out 144 sign/pairing fixes to `C187`'s construction. Named this
   round's approach as the concrete next step.
4. `null_results/INDEX.md`, `parked/INDEX.md`: 0 hits for a quaternion-native
   Euler-angle Dirac construction in this project.
5. **Status:** [x] NEW.

---

## Step 0a — Mechanism Claim Gate

The design rests on one sentence: *"`Xₐᴿ`, expressed as a `(θ,φ,ψ)`
differential operator via the Jacobian of the Euler-angle embedding, is the
same vector field as `C184`/`C186`'s `Xₐᴿ` — merely a coordinate change."*

This is checked, not assumed, in section A: each `Xₐᴿ` is confirmed
**tangent to `S³`** (least-squares residual against the embedding's own
Jacobian, `< 1e-30`) and matches a stated closed form to the same precision.
**Verdict: HOLDS.**

```
X_0^R = 2 d/dpsi
X_1^R = 2 cos(psi) d/dtheta + 2 sin(psi)/sin(theta) d/dphi - 2 sin(psi)/tan(theta) d/dpsi
X_2^R = -2 sin(psi) d/dtheta + 2 cos(psi)/sin(theta) d/dphi - 2 cos(psi)/tan(theta) d/dpsi
```

---

## Falsifiable claim

Assembling `D = -i Σₐ σₐ Xₐᴿ` directly from these (applying each `Xₐᴿ`
identically to both spinor components, then mixing via `σₐ` — a pure
Kronecker-product structure, no separate spin connection) reproduces the
eigenvalue `-k` at levels `k = 0, 1, 2, 3`, for candidates independently
re-derived (not guessed) at each level via the same i-axis Rosetta-stone
technique `C187b` used for `k=1`:

| `k` | `(m,n)` | `F(θ)` | `G(θ)` | expected `λ` |
|---|---|---|---|---|
| 0 | `(0,0)` | `-1` | `1` | `0` |
| 1 | `(1/2,1/2)` | `-cos(θ/2)` | `cos(θ/2)` | `-1` |
| 2 | `(1,1)` | `-cos(θ/2)²` | `cos(θ/2)²` | `-2` |
| 3 | `(3/2,3/2)` | `-cos(θ/2)³` | `cos(θ/2)³` | `-3` |

**Pre-registered before running:** all four rows above, and the pattern
`F=-cos(θ/2)ᵏ`, `G=+cos(θ/2)ᵏ`, `(m,n)=(k/2,k/2)`, `λ=-k` — obtained by direct
computation for each `k` (`derive_mn_k23.py`, part of this experiment's
provenance), not extrapolated from `k=1` alone.

---

## Kill criterion

**REJECTED** if any of the four `(m,n,F,G,λ)` rows above fails
`D ψ = λ ψ` under direct, high-precision numeric evaluation (multiple random
`θ,φ,ψ`, not a single point).

## Negative/consistency control

Section B (`P9`) checks that `Xₐᴿ`'s own `cos(ψ)`, `sin(ψ)` prefactors — which
could in principle shift the Fourier index `n` when acting on a fixed-`n`
ansatz — do **not** introduce any `φ`-dependence beyond the shared phase.
Section D separately documents, rather than hides, a related but distinct
finding: the half-angle/`kernel_dim` reduction technique from `C185`/`C187`
does **not** transfer cleanly to this construction, because `X₁ᴿ, X₂ᴿ`'s
`cos(ψ)`/`sin(ψ)` prefactors leave an explicit residual `ψ`-dependence in the
reduced equations that the earlier technique's rank computation cannot
absorb without a combinatorial blow-up. This is recorded as a genuine
negative methodological result, not chased further, because claim (b) does
not need it — section C's direct verification already closes it.

## What this establishes

- **The concrete next step named in `C187b` is executed and confirmed.**
  `D` built directly from the quaternion generators reproduces the known
  spectrum at `k=0..3` — by construction guarantee, not by luck, and verified
  independently of that guarantee via direct numeric evaluation.
- **`C187`'s specific construction remains rejected**, for the reason already
  recorded there (not periodicity, not physics — the vielbein/connection
  itself). This round does not diagnose that specific bug; it bypasses it.
- **Does NOT extend beyond `k=3`.** The pattern `(m,n)=(k/2,k/2)`,
  `λ=-k`, `F=-cos(θ/2)ᵏ` is verified at four levels; that it continues for
  all `k` is inference from this project's independently-established general
  theorem (`C184` Part C: `L²(S³)` carries only `(j,j)`), not computed here
  for arbitrary `k`.
- **Does not derive the `+(k+2)` branch** — only the `-k` branch's extreme
  state was checked. The `+(k+2)` branch was already confirmed by `C184`/
  `C186` via the matrix method; this round's purpose was closing the
  Euler-angle construction question, not re-deriving what those already
  established.
- **A genuine limitation surfaced, not swept aside:** the half-angle
  reduction technique that made `C185`/`C187` fast does not transfer to a
  quaternion-native construction, because the coordinate-dependent
  `cos(ψ)`/`sin(ψ)` prefactors in `X₁ᴿ, X₂ᴿ` are a real structural cost of
  building `D` this way, not a bug to be fixed.
