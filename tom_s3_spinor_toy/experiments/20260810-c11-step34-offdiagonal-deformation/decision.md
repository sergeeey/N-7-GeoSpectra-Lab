# decision — C11 steps 3+4: sector grading and the off-diagonal deformation

**Verdict:** `FOUR_DIM_KERNEL_IS_UNSTABLE__STEP5_NOW_DECISIVE` → claim **C47**.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_step34.json` persisted.

---

## Step 3 is a corollary, and is labelled as one

The portfolio's step 3 (`[T,a]` vs `{T,a}`) turned out to be a one-line consequence of
step 1's symbol table: with `T = s3`, `A` is `Z₂`-graded, and its `T`-even part is
**exactly** the twisted diagonal `{diag(f, f∘ι)}` (`even⊗I`, `odd⊗s3` commute with `T`;
`even⊗s1`, `odd⊗s2` anticommute). This restates C46 in a different basis and is recorded
as a corollary — **not** counted as independent support for anything. (The failure mode
being avoided here is the one round110 was caught in: re-packaging round106 as new
evidence.)

## Step 4 is substantive: the deformation, and where it lives

Self-adjointness plus `{γ, D} = 0` with `γ = U_ι ⊗ s1` constrain the two off-diagonal
coefficients in **opposite** ways, because conjugation by `s1` fixes `s1` and flips `s2`:

| term | required `ι`-parity of the coefficient | admissible |
|---|---|---|
| `X ⊗ s1` | **odd** → `X = D^{1/2}` | yes |
| `Y ⊗ s2` | **even** → `Y = Identity` | yes |
| `I ⊗ s1` | even with `s1` — wrong parity | **no** (built-in negative control) |
| `D^{1/2} ⊗ s2` | odd with `s2` — wrong parity | **no** |

So `D(α,β) = D_block + α(I⊗s2) + β(D^{1/2}⊗s1)`, and [VERIFIED-sympy] the eigenvalues
become

```
lambda = mu ± sqrt(9/4 + beta^2 mu^2 + alpha^2),      mu = sigma(n + 3/2)
```

## The 4-dim kernel fails the no-collapse test

Kernel condition: `mu^2 (1 − beta^2) = 9/4 + alpha^2`. At the `n = 0` level (`mu^2 = 9/4`)
this reduces to `alpha^2 + (9/4) beta^2 = 0`, a **positive-definite** real quadratic form
(eigenvalues 1 and 9/4) — so over the reals its **only** zero is the origin.

| `(α, β)` | `dim ker` |
|---|---|
| `(0, 0)` | **4** |
| `(0.1, 0)` / `(0, 0.1)` / `(0.3, 0.2)` | 0 |
| `(0, 0.8)` | 12 |

Higher levels reappear on real curves: `α=0` gives `β = 0.800, 0.9035, 0.9428` for
`n = 1, 2, 3` with kernels **12, 24, 40** — over-production, the same pattern C44 found at
`t = −1/3, 4/3`. The `n=0` "curve" degenerates to the single point.

**A bug in the first version of this file, fixed and recorded:** the probes at
`α = 1e-6` returned `dim ker = 4`, and I nearly reported the kernel as robust for tiny
deformations. At `α = 1e-6` the surviving eigenvalue is `≈ α²/3 ≈ 3e-13` — **inside my
own `atol=1e-9`**. That measured the tolerance, not the operator. Replaced by (a) the
exact positive-definiteness argument above and (b) a scaling check confirming
`min|λ| / (α²/3) = 1.0000, 1.0000, 0.9989` at `α = 1e-3, 1e-2, 1e-1`. The kernel moves
off zero **quadratically** and never stays.

> **C47.** The 4-dim kernel matching C38's Spin(4) spinor is an **isolated point** of the
> admissible deformation family, not a stable feature of the two-operator structure.

## Why this made step 5 decisive rather than decorative

Recorded in advance, before step 5 ran:

- **AGAINST** — the 4-dim kernel is a property of the *undeformed* block, and nothing
  found so far forbids the deformation.
- **FOR** — if the first-order condition forbids the off-diagonal terms, the isolation
  stops being a fragility and becomes a **selection**: `(0,0)` would be the only point
  compatible with the axioms.

Step 5 (`20260810-c11-step5-real-structure`) settled it: **the FOR branch**. `β = 0` by
boundedness, `α = 0` by first-order. See that folder's `decision.md` — including the
result that pulls the other way.

## What this does NOT show

- It does not show the deformation is *physical* — no action principle is involved.
- The family tested is the **minimal** admissible one (`X = D^{1/2}`, `Y = I`); a general
  `X` `ι`-odd and `Y` `ι`-even is a larger family and is **not** swept here.
- Inherits **ASSUMPTION A1** from step 1 (`U_ι D^{1/2} U_ι† = −D^{1/2}`).
- Nothing about `N_gen = 3` (step 7, deferred).
