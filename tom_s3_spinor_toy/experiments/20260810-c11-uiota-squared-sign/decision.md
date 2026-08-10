# decision — `U_ι² = ±1`: the flag was a false alarm

**Verdict:** `QUESTION_MIS_SCOPED__SIGN_IS_A_CHOICE_AND_NOT_LOAD_BEARING` → **C56**.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_uiota.json` persisted.

---

## Stating the null plainly

C45 flagged `U_ι² = ±1` as **OPEN**, "needed for `γ† = γ`". It was carried for ten rounds
and, after C55 discharged A1, was the only named unknown left in this line.

**Nothing was discovered here except that the worry did not apply.** The flag was a false
alarm. That is the result, and it is worth exactly what it is worth — one closed
bookkeeping item, not a finding.

## Why it does not apply

`γ` enters only through `γ† = γ`, `γ² = +1` and `{γ, D} = 0`, and it is only ever used up
to a phase. Write `γ = c·U_ι ⊗ s1`:

| `U_ι²` | `U_ι` is | admissible `c` | `γ† = γ` | `γ² = I` | `{γ,D} = 0` |
|---|---|---|---|---|---|
| `+1` | self-adjoint | `±1` | ✓ | ✓ | ✓ |
| `+1` | self-adjoint | `±i` | **✗** | **✗** | ✓ |
| `−1` | anti-self-adjoint | `±1` | **✗** | **✗** | ✓ |
| `−1` | anti-self-adjoint | `±i` | ✓ | ✓ | ✓ |

[VERIFIED-numpy] on the explicit mirror-block model. For `U_ι² = −1` the phase does both
jobs at once: `γ² = i²·(−1) = +1`, and `γ† = γ` because a unitary with `U² = −1` is
**anti**-self-adjoint and the imaginary phase compensates.

**The mismatched pairings genuinely fail**, so this is not a vacuous rescue —
`{γ,D} = 0` holds in all eight rows (it is phase-blind, as expected and shown), but the
two axioms that were at stake discriminate.

**Why the phase freedom exists at all:** by C55, `U_ι` maps `(j, j±½)` onto `(j±½, j)`, and
`j ≠ j±½` always — so `U_ι` is **purely off-diagonal** on the mirror pairs. An operator
with no fixed blocks satisfies `U² = +1 ⟺ U` self-adjoint, and multiplying by `i` moves
between the two cases.

## What the sign does not affect — the whole chain

[VERIFIED-numpy] `‖[D_M, V]‖ = 11.0, 19.0, 35.0, 67.0` at cutoffs `4, 8, 16, 32` —
**identical** for both lifts, since `[D_M, cV] = c[D_M, V]`. So:

- C50/C51/C53/C54's "`V ∉ 𝔅`" — untouched;
- C52's locality argument — never sees a phase;
- C55's L↔R swap — never sees a phase;
- `{γ, D} = 0` — phase-blind.

## What it does affect — and it explains an earlier abstention

`J` is **antilinear**, so `J(cX)J⁻¹ = c̄·J X J⁻¹`, and `c̄/c` is `+1` for real `c`, `−1` for
imaginary `c`. **The `ε''` sign of the KO-dimension tuple flips with the choice.**

That is precisely the combination **C48 declined to make** ("only the sector-factor signs
are computed here; combining them with `S³`'s own tuple is exactly the step C36 showed is
easy to get wrong — left OPEN rather than asserted"). The abstention now has a reason
rather than only a caution: **the combination depends on a choice nothing in the
construction fixes.**

## The geometric side, and the C34 tie-in

In the project's **canonical** `S³` convention — `Z_i = i·σ_i`, `e² = −1`, `Cl(0,3)`, which
`docs/clifford_convention_registry.md` marks as correctly labelled — the volume element is

```
ω = Z₁Z₂Z₃ = +I        ω² = +I
```

so the **fibre** part of the lift of `dι|_p = −Id` at a fixed point squares to `+1`.
In the opposite convention (`Γ_i = σ_i`, `e² = +1`) the same computation gives `ω = iI`,
`ω² = −I`.

**So the sign of `ω²` is the convention, not a geometric fact** — C34's point, arriving a
third time. Pinning `U_ι²` globally is a **Pin⁺ / Pin⁻ choice**; `S³` is parallelizable and
admits both, and nothing in this chain requires one. Recorded as a **choice**, not a fact.

---

## Kill Analysis

**Killed:** the C45 flag, as an open question. Not by answering it — by showing it does
not need answering.

**Not killed / not claimed:**
- **Pin⁺ vs Pin⁻ is not decided here.** Both exist on `S³`; the geometric lift's square is
  fixed only once that choice is made, and this round does not make it.
- The fixed-point computation constrains the **fibre** map at `ι`'s two fixed points; the
  full `U_ι` also carries the pullback, and its global phase is exactly the Pin choice.
- The KO-dimension tuple remains **OPEN** — now with an explicit reason (U5) rather than
  only C48's caution.

## Where C11 stands after this

Every named unknown in the line is now either derived (A1 → C55) or shown non-load-bearing
(`U_ι²` → here). The construction's status is unchanged: the doubling is unearned from
four directions plus an independent orientability failure, rooted in one conflict —
**anticommutation demands `ι`; orientability forbids it**. What survives is C46 (a
*parity* doubling, if taken) and C47 (isolated kernel, made a selection by C48).

**The remaining open items are no longer internal to this line:** the KO-dimension tuple
(needs a Pin choice) and step 7, `N_gen = 3`, **untouched by agreement**.

## What this does NOT show

- It does **not** determine `U_ι²` geometrically. It shows the determination is a choice
  and that nothing here depends on it.
- It does **not** revisit the doubling verdict — that is C44–C55's business and is
  unchanged.
- Nothing about `N_gen = 3` — **step 7 remains untouched by agreement.**
