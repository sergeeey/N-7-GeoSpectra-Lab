# KO tuple, finally — is the KO-2/KO-4 split a gauge artifact, or real?

**Experiment id:** `20260810-c11-ko-final-gauge-or-real`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C57 (KO tuple: `k=I → KO-4`, `k=s3 → KO-2`, called *"internal to `J`, not
geometric"*), C59 (the `S³`-factor lift `J_M` is unique up to phase — Schur's lemma)

---

## What C57 left unresolved, and why C59 makes it checkable

C57 found exactly two survivors of order-zero + `JD=ε'DJ` + `Jγ=ε''γJ`: `k=I` (KO-dim 4) and
`k=s3` (KO-dim 2, with `diag(1,−1)=−s3` giving the same tuple). It declared the choice
between them *"internal to `J`, not geometric"* — but did not check whether the two are
secretly **the same physics in two descriptions**, related by a change of basis that
preserves every piece of data the construction actually fixes. C59 just proved the
analogous question for the `S³`-factor lift `J_M` (unique up to phase, via equivariance).
The natural, honestly cheap last step: **does the same kind of check apply to the sector
factor `k`?**

## The claim under test

> **C60 (proposed).** There is a unitary automorphism `V` of the full data
> `(A, H, D_block, γ)` — i.e. `V D_block V† = D_block`, `V A V† = A`, `VγV† = (\text{phase})·γ`
> — that conjugates the `k=I` real structure to the `k=s3` real structure. If so, the KO-2/
> KO-4 split is a **gauge artifact**: one triple, two labels. If not, C57's characterization
> is **confirmed as final**: a genuine, irreducible bifurcation.

**Falsifier, fixed in advance:** exhibiting such a `V` refutes "internal choice, not
geometric" in the strongest possible direction — it would mean there is only **one** KO-
dimension after all, just mislabelled twice.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **G1** | any `V` preserving `D_block` exactly must be **sector-diagonal** (`V = I_M ⊗ v`, `v` a `2×2` unitary), because `D_block`'s sector part `(3/2)I⊗s3` forces `[v,s3]=0` — i.e. `v` diagonal in the `s3` eigenbasis |
| **G2** | requiring `VγV† = (\text{phase})·γ` for such **diagonal** `v = \mathrm{diag}(v_1,v_2)` forces `v_1 = \pm v_2` — i.e. `v ∝ I` or `v ∝ s3`, **nothing else survives** |
| **G3** | conjugating `k=I` by `v=s3`: `k' = s3 \cdot I \cdot \overline{s3} = I` — **fixed**, not moved to `s3` |
| **G4** | conjugating `k=s3` by `v=s3`: `k' = s3 \cdot s3 \cdot \overline{s3} = s3` — **also fixed** |
| **G5 (discriminator)** | run the identical conjugation search on a **known-equivalent** pair first (e.g. `k=\mathrm{diag}(1,-1)$ vs `k=s3`, which C57 already noted give the *same* tuple) — this **must** succeed, or the search machinery itself is broken |
| **G6** | if G1–G4 hold, **no sector-only automorphism relates `k=I` and `k=s3`** — the split survives as genuine. State explicitly what is **not** checked: automorphisms that also act on the `S³` factor (`V = V_M ⊗ v` with `V_M ≠ I`) |

## What this cannot show

- It does **not** search the full automorphism group — only `V = V_M ⊗ v` with `V_M = I`
  (sector-only). A more general `V_M ⊗ v` is **not** tested and is named as the honest
  residual, not silently assumed absent.
- It has **zero** consequence for whether the doubled triple is a geometry: C49 (Poincaré
  duality fails) and C52 (orientability fails) already settled that, independent of KO-
  dimension. This is bookkeeping on bookkeeping on a non-geometry, and is scoped that way.
- Nothing about `N_gen=3` — closed at C58, untouched here.

## kill_criterion

C60 stands if G3 or G4 comes out **moved** rather than fixed, for `v=s3`, or if a broader
search (if attempted) finds any `V` implementing the conjugation.
