# decision — A1: `ι` really does flip the Dirac operator

**Verdict:** `A1_VERIFIED__IOTA_FLIPS_THE_DIRAC_OPERATOR` → **C55 STANDS**.
After ten rounds of being carried as an assumption, A1 is **derived**.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_a1.json` persisted.

---

## What was actually assumed, and for how long

Every round from C45 to C54 carried:

> **ASSUMPTION A1**, inherited from C39 + the standard orientation-reversal result,
> **not re-derived here**: `U_ι D^{1/2} U_ι† = −D^{1/2}`.

C39 established that `ι` **reverses orientation**. It never established that `ι` flips
`D`. C54 made the exposure explicit: A1 is precisely what makes `[D_M, U_ι] = 2 D_M U_ι`
unbounded, so C50, C51, C53 and C54 all rest on it.

## The derivation

Peter–Weyl makes both the spectrum and the `ι`-action explicit:

```
L²(SU(2), S) = ⊕_j V_j ⊗ (V_j* ⊗ V_{1/2}) = ⊕_j V_j ⊗ (V_{j+1/2} ⊕ V_{j−1/2})
```

Label each isotypic piece `(j, k)` = (left spin, right spin), `k = j ± ½`.

**A1a — the eigenvalue formula, and an independent check of the project's own data.**

```
λ(j, k) = (j + k + 1) · sign(k − j)        mult = (2j+1)(2k+1)
```

| `j` | `k = j+½` | `λ` | mult | `k = j−½` | `λ` | mult |
|---|---|---|---|---|---|---|
| 0 | ½ | 3/2 | 2 | — | — | — |
| ½ | 1 | 5/2 | 6 | 0 | −3/2 | 2 |
| 1 | 3/2 | 7/2 | 12 | ½ | −5/2 | 6 |
| 3/2 | 2 | 9/2 | 20 | 1 | −7/2 | 12 |

Setting `n = 2j` on the `+` branch and `n = 2j−1` on the `−` branch reproduces
`±(n+3/2)` with multiplicity `(n+1)(n+2)` — **exactly**, for both branches
[VERIFIED-sympy]. That is an **independent derivation of the spectral data this project
has used since round67**, from representation theory rather than from the closed form.

**A1b — the flip, identically.** `ι(g) = g⁻¹` exchanges left and right translations, so
`ι*` maps `(j,k) → (k,j)`. The swap **preserves** `j+k+1` and **flips** `sign(k−j)`:

```
λ(k, j) + λ(j, k) = 0        identically in (j, k)      [VERIFIED-sympy]
```

and `(2j+1)(2k+1)` is symmetric, so the swap is a **bijection** from each `D`-eigenspace
onto the corresponding `(−D)`-eigenspace.

**A1c — level by level.** `(0,½) λ=3/2 mult 2 → (½,0) λ=−3/2 mult 2`; `(½,1) 5/2 6 →
(1,½) −5/2 6`; … verified for `n = 0…8`, magnitudes mirrored and multiplicities equal.

## Cross-check, and it lands on an earlier result

A1 implies `U_ι D^t U_ι† = −D^{1−t}` — **exactly C44's mirror relation**, which C44
obtained from round67's closed form. Two independent routes, same statement. C44 and A1
now corroborate each other rather than sharing a source.

## The negative control discriminates, through the same code path

| label map | flips `λ`? |
|---|---|
| `ι: (j,k) → (k,j)` — orientation-**reversing** | **True** |
| `L_a: (j,k) → (j,k)` — orientation-**preserving** | **False** |

Written as one `flips_under(label_map)` helper applied to both, because the first version
was `λ(j,k) − λ(j,k) == 0` — `x − x`, the **seventh** cannot-fail check of this session.

**Discrimination:** drop the `sign(k−j)` factor (use `|D|`) and the swap flips nothing. So
that factor is exactly what carries A1 — the flip is caused by the **L↔R swap**, which is
what orientation-reversal *means* here, not by "being an isometry".

---

## Kill Analysis

**Killed:** the status of A1 as an unverified inherited assumption.

**What the chain now inherits instead — strictly weaker, and named:**

| | Content | Status |
|---|---|---|
| **A1-lift** | the geometric spinor lift may differ from the bare pullback by a unitary; the conclusion survives any factor **preserving the isotypic decomposition** | still an input, but far weaker than A1 — it constrains a phase, not the sign of `D` |
| **`U_ι² = ±1`** | open since C45 | **unchanged** — nothing here settles it |
| **R** (regularity) | used only when `B` is large | unchanged |

**Consequence for C50, C51, C53, C54:** their load-bearing input is now **derived**, not
assumed. Those four claims' `does_not_imply` entries naming A1 as unverified are updated
to point here.

## What this does NOT show

- It does **not** settle `U_ι² = ±1`. That sign is still open, and C45 flagged it as
  needed for `γ† = γ`.
- It does **not** construct the spinor lift explicitly as an operator; it establishes the
  eigenspace bijection, which is what A1 is used for.
- The `C²` spin-factor convention (left vs right index) is not a loose end: the conclusion
  is convention-independent precisely because `ι` swaps the two roles.
- Nothing about `N_gen = 3` — **step 7 remains untouched by agreement.**
