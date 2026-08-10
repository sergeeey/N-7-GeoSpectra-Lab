# A1 — does `ι` really flip the Dirac operator? Verify it, do not inherit it.

**Experiment id:** `20260810-c11-a1-iota-flips-dirac`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessor:** C54 — which named A1 as the single load-bearing unverified input

---

## Why this and not another escape route

Every round from C45 to C54 carried the same line in its `does_not_imply`:

> **ASSUMPTION A1**, inherited from C39 + the standard orientation-reversal result,
> **not re-derived here**: `U_ι D^{1/2} U_ι† = −D^{1/2}`.

C54 made the exposure explicit: **A1 is exactly what makes `[D_M, U_ι] = 2 D_M U_ι`
unbounded**, so C50, C51, C53 and C54 all rest on it. If A1 is false, `U_ι` could lie in
the Lipschitz algebra `𝔅` and four claims need rebuilding. It has been carried for ten
rounds on the strength of "standard result" plus C39's orientation check — which
established that `ι` **reverses orientation**, not that it flips `D`.

## The claim under test

> **C55.** On `S³ = SU(2)` with the bi-invariant metric and its unique spin structure,
> the operator implementing `ι(g) = g⁻¹` conjugates the Levi-Civita Dirac operator to
> **minus itself**: `U_ι D^{1/2} U_ι† = −D^{1/2}`.

**This is verifiable, not merely citable,** because Peter–Weyl makes the whole spectrum
and the whole `ι`-action explicit:

- `L²(SU(2), S) = ⊕_j V_j ⊗ (V_j* ⊗ V_{1/2}) = ⊕_j V_j ⊗ (V_{j+1/2} ⊕ V_{j−1/2})`;
- label each isotypic piece by `(j, k)` = (left spin, right spin), `k = j ± ½`;
- `ι(g) = g⁻¹` exchanges left and right translations, so `ι*` maps `(j,k) → (k,j)`.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **A1a** | the Dirac eigenvalue on the `(j,k)` piece is `λ(j,k) = (j+k+1)·sign(k−j)`, and this reproduces round67's spectrum **and multiplicities** exactly — `±(n+3/2)` with `(n+1)(n+2)` — an **independent** derivation of the data this whole project has been using |
| **A1b** | `λ(k,j) = −λ(j,k)` **identically**: the swap preserves `j+k+1` and flips `sign(k−j)`. Dimensions `(2j+1)(2k+1)` are symmetric, so it is a bijection |
| **A1c** | level by level, `ι` maps the `+(n+3/2)` eigenspace **onto** the `−(n+3/2)` eigenspace with equal multiplicity, for `n = 0…N` |
| **A1d** | consequence: `U_ι D^t U_ι† = −D^{1−t}` — which is **exactly C44's mirror relation**, derived here from `ι` rather than from the closed form. Independent cross-check of a result reached another way |
| **NC** | **negative control:** an orientation-**preserving** map (left translation — C39's own control) acts *within* each `(j,k)` block, does **not** swap the labels, and therefore does **not** flip the eigenvalue |
| **DISC** | **discrimination:** drop the `sign(k−j)` factor (i.e. use `|D|`) and the swap no longer flips anything — showing that factor is what carries the result |

## What this can and cannot settle

**Can:** that the `ι`-pullback maps every `D`-eigenspace onto the corresponding
`(−D)`-eigenspace, with exactly matching multiplicities. That is the content A1 is used
for in C50/C51/C53/C54 — those arguments need `U_ι D U_ι† = −D` as an operator identity,
and it follows once `U_ι` maps `λ`-eigenspaces onto `(−λ)`-eigenspaces.

**Cannot:**
- **The lift's phase.** The geometric spinor lift may differ from the bare pullback by a
  unitary. The conclusion survives any such factor that preserves the isotypic
  decomposition — a much weaker input than A1 itself, but it **is** an input, and I name
  it **A1-lift**.
- **`U_ι² = ±1`**, still open since C45. Nothing here settles the sign.
- Convention: whether the `C²` spin factor attaches to the left or right index. The
  conclusion is convention-independent precisely because `ι` swaps the two roles — worth
  checking rather than asserting.

## kill_criterion

C55 fails if `λ(k,j) ≠ −λ(j,k)`, if the multiplicities do not match under the swap, or if
the Peter–Weyl formula does not reproduce round67's spectrum. Any of those would
invalidate A1 and force C50/C51/C53/C54 to be rebuilt.
