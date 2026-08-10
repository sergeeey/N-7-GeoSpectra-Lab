# C11 (ii) — the block supplies the grading C35 proved impossible for one operator

**Date:** 2026-08-10
**Verdict:** `BLOCK_SUPPLIES_THE_GRADING_C35_PROVED_IMPOSSIBLE_FOR_ONE_OPERATOR`
**Gate:** 3 of PARENT_ACTION_GATE's 6 OB2 fields now supplied (was 2, both toys)

## Why this construction and not round110's

C42 closed the one-operator reading, so the pair is the only live construction.
round110 used a toy `D_block = diag(0,0,3c/2,3c/2)`; C35 analysed
`D = 3(T⊗I₂)`. **Both are toys**, and C35's decisive negative — *no grading can
exist, because `spec(D) = {0,0,3,3}` is not symmetric under `λ → −λ`* — is a
statement about the toy, not about the real pair.

This uses the **actual** operators, via round67's closed form.

## The result [VERIFIED-sympy + VERIFIED-numpy]

With `h_H = 3`:

```
D^t(n,σ) = σ(n + 3/2) + (t − ½)·3

  t=0 :  σ=+1 → n        σ=−1 → −n−3        so  spec(D⁰) = {0,1,2,…} ∪ {−3,−4,…}
  t=1 :  σ=+1 → n+3      σ=−1 → −n          so  spec(D¹) = {0,−1,−2,…} ∪ {3,4,…}
```

**`spec(D¹) = −spec(D⁰)` exactly, multiplicities included** — and it is an
**identity, not a truncation artifact**: the pairing is level-by-level at
*identical* `n`,

```
 −[ n  ] = −n    ↔  D¹'s σ=−1 at the same n, same mult (n+1)(n+2)
 −[−n−3] = n+3   ↔  D¹'s σ=+1 at the same n, same mult (n+1)(n+2)
```

confirmed at `N_MAX = 3, 6, 12, 20` (up to 7084 states per block).

| check | result |
|---|---|
| `spec(D⁰)` alone symmetric | **False** ← C35's obstruction, reproduced |
| `spec(D⁰ ⊕ D¹)` symmetric | **True** |
| `γ² = I`, `γ = γ†`, `{γ, D_block} = 0` | **all True**, γ built explicitly |
| `dim ker(D⁰⊕D¹)` | **4** = 2 + 2, matching C38's `Spin(4)` spinor |

**Negative control passes:** the identical matching logic applied to `D⁰` alone
**fails** to construct a grading — so the code is measuring the spectrum, not
manufacturing a pairing. That control *is* C35's result, reproduced as a control.

## Why this is not a coincidence

C39 established that `ι` is **orientation-reversing**, and reversing orientation
flips a Dirac operator's sign. **The mirror spectra are that fact, expressed
spectrally.** So the grading exists for the pair *because* the two sectors are a
parity pair — the same structure C37 reached from polynomial parity and C39 from
the orientation of a diffeomorphism, now showing up a third time as a spectral
symmetry.

This is the **first positive structural result** for the two-operator reading.
Every prior result on C11's line was a closure or a narrowing.

## PARENT_ACTION_GATE — all six fields, as they stand

| field | status |
|---|---|
| Hilbert space `H` | ✅ `L²(S³,S) ⊕ L²(S³,S)` — the two copies *are* the `t=0` and `t=1` sectors |
| Dirac `D` | ✅ `D_block = D⁰ ⊕ D¹`, both from round67's closed form, self-adjoint |
| **Grading `γ`** | ✅ **NEW — exists, constructed and verified** |
| Algebra `A` | ❌ NOT SUPPLIED — round110's `ℂ⊕ℂ` was a toy and does not follow from the two-operator structure |
| Real structure `J` | ❌ NOT SUPPLIED — C35 found `J` only pointwise on the toy; nothing here extends it |
| Physical interpretation | ❌ NOT SUPPLIED — **nothing here says WHY two copies should coexist** |

**3 of 6.** The three still missing are the actual content of C11.

## What this does NOT establish

1. **Does not resolve C11.** A grading is one field. The remaining three are the
   substance, and the last one — why two copies exist at all — is the physics.
2. **Does not show both `t` are physically realized.** It shows that *if* they
   are, the pair is not obstructed the way the single operator is.
3. **Does not check first-order, orientability, or Poincaré duality.** Those need
   the algebra, which is unsupplied.
4. **The grading is not unique.** Any relabelling within a degenerate level gives
   another; nothing here selects one, and a physical `γ` would need to.
5. Truncated at `N_MAX`; the *mirror* is proved level-by-level and so survives the
   limit, but the explicit matrix `γ` is finite-dimensional.

## Next

The cheapest remaining field is **the algebra `A`** — everything else (first
order, orientability, Poincaré duality) is defined relative to it, so it gates
three checks at once. The physical interpretation is the expensive one and is
genuinely C11's open question.

## Check

```
python experiments/20260810-c11-block-construction/block_vs_gate.py
```
Expect mirror `True`; single-block symmetric `False`; block symmetric `True`;
all three γ axioms `True`; `ker = 4`; control `PASSES`; fields supplied `3/6`.
