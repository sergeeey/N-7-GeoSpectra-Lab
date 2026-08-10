# `U_ι² = ±1` — the last named unknown in the C11 line

**Experiment id:** `20260810-c11-uiota-squared-sign`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C45 (flagged it), C55 (left it as the only remaining unknown)

---

## What was flagged, and why it looked serious

C45 recorded: *"OPEN, flagged not assumed: whether the Pin-lift satisfies `U_ι² = +1`,
needed for `γ† = γ`."* It has been carried ever since, and after C55 discharged A1 it is
**the only named unknown left in this line**.

The worry has a real basis: `γ = U_ι ⊗ s1` gives `γ² = U_ι² ⊗ I`, so if `U_ι² = −1` then
`γ² = −1` and `γ` is not a grading. C43's entire construction would collapse.

## What I expect to find, stated before testing

**That the question is mis-scoped.** `γ` is only ever used up to a phase, and a phase can
absorb the sign:

- `U_ι² = +1` ⇒ `U_ι` self-adjoint ⇒ take `γ = ±U_ι⊗s1`;
- `U_ι² = −1` ⇒ `U_ι` anti-self-adjoint ⇒ take `γ = ±i·U_ι⊗s1`, and then
  `γ² = (i)²(−1) = +1` and `γ† = γ` **both hold**.

If that is right, the flag has been a false alarm for ten rounds — and I should say so
plainly rather than dress a null as a discovery.

**Why the phase freedom is available at all:** by C55, `U_ι` maps the isotypic piece
`(j, j±½)` onto `(j±½, j)`. Since `j ≠ j±½` always, `U_ι` is **purely off-diagonal** on the
mirror pairs — it has no fixed blocks, so `U_ι² = +1 ⟺ U_ι` self-adjoint and
`U_ι² = −1 ⟺ U_ι` anti-self-adjoint, and multiplying by `i` moves between them.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **U1** | in the project's **canonical** S³ convention (`Z_i = i·σ_i`, `e² = −1`, `Cl(0,3)` — `docs/clifford_convention_registry.md`) the volume element is `ω = Z₁Z₂Z₃ = +I`, so `ω² = +I`. The lift of `dι|_p = −Id` at a fixed point is `±ω`, so the **fibre** part squares to `+1` |
| **U2** | the opposite convention (`Γ_i = σ_i`, `e² = +1`) gives `ω = iI`, `ω² = −I` — so the sign of `ω²` **is** the convention, exactly as C34's registry says. Not a geometric fact on its own |
| **U3** | **the payoff:** `γ = c·U_ι⊗s1` satisfies `γ†=γ`, `γ²=+1`, `{γ,D}=0` for **either** sign of `U_ι²` — `c = ±1` when `+1`, `c = ±i` when `−1` |
| **U3-DISC** | the **mismatched** pairings must FAIL (`c` real with `U_ι²=−1`, `c` imaginary with `U_ι²=+1`) — otherwise U3 is vacuous |
| **U4** | the C50–C55 chain is **phase-independent**: `[D_M, cV] = c[D_M,V]`, so the norm growth and `V ∉ 𝔅` are untouched; `{γ,D}=0` is untouched; C55's L↔R swap is untouched |
| **U5** | where the sign **does** matter: `J` is **antilinear**, so `JγJ⁻¹` picks up `c̄/c` = `+1` for real `c`, `−1` for imaginary `c`. **The `ε''` sign of the KO tuple flips with the choice** — which is exactly the combination C48 declined to make |

## What this cannot settle

- **Pin⁺ vs Pin⁻.** `S³` is parallelizable and admits both; the geometric lift's square is
  fixed only once that choice is made. Nothing here picks one, and nothing in the chain
  needs one picked. I will state that as a **choice**, not a fact.
- The fixed-point computation (U1) constrains the **fibre** map at `ι`'s two fixed points;
  the full `U_ι` also carries the pullback, and pinning its global phase is the Pin choice
  above.
- Nothing about `N_gen = 3` — step 7 untouched by agreement.

## kill_criterion

The flag is real (and C43 collapses) if **no** phase `c` makes `γ† = γ` and `γ² = +1`
simultaneously for `U_ι² = −1`. That is the single thing to check, and U3-DISC makes the
check falsifiable.
