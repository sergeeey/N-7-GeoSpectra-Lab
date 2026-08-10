# OB2 (b) — Θ is not a real structure, and the toy triple cannot carry one globally

**Date:** 2026-08-10
**Verdict:** `THETA_IS_NOT_A_REAL_STRUCTURE__J_EXISTS_POINTWISE_ONLY__TRIPLE_IS_ODD_AND_DEGENERATE`
**Closes:** C30's own next gate ("check `Θ` against the NCG real-structure
axioms") and item (b) of `activeContext`'s open list.
**Answer to the question C30 raised:** no — `PARENT_ACTION_GATE.md`'s
`Real structure J: NOT ATTEMPTED` field is **still not filled**.

## The headline

C30 found the genuine symmetry of OB2's order parameter is antiunitary,
`Θ = iσ₂K`, `Θ² = −I`, and recorded as its next step: does this fill the
spectral triple's missing `J`? **It does not, and structurally cannot.**

`Θ` was built to satisfy `Θ T Θ⁻¹ = 1 − T` — it **exchanges** the algebra's two
minimal projectors. A real structure must satisfy the **order-zero axiom**
`[a, J b* J⁻¹] = 0` — it **commutes** with the algebra. An operator built to
exchange `A`'s generators cannot commute with them. `Θ` is a symmetry **of** the
algebra; `J` is part of the **spectral data**. Two different roles, and the
resemblance ("both antiunitary, both square to a sign") is what made them look
interchangeable.

Verified: `Θ` lifted as `(iσ₂)⊗I₂` is a valid `J` at **0 of 12** Bloch points.

## What the toy triple *can* carry [VERIFIED-numpy]

| axiom | result |
|---|---|
| grading `γ`, `{γ,D}=0` | **cannot exist** — see below |
| `J` pointwise | **exists at 12/12 points**, unique sign tuple `(J²,JDJ⁻¹/D) = (+1,+1)` |
| `J` globally | **0** — blocked by a determinant obstruction |
| order zero `[a,Jb*J⁻¹]=0` | holds, but as a **consequence** of `JDJ⁻¹=+D` |
| first order `[[D,a],Jb*J⁻¹]=0` | holds **vacuously** — see below |

**The grading cannot exist, and that is stronger than OB2's original wording.**
OB2 recorded "grading γ: ATTEMPTED, FAILS for the naive choice". The real
statement is that no `γ` exists at all: `spec(D) = {0,0,3,3}` is **not symmetric**
under `λ → −λ`, and `{γ,D}=0` requires `γ` to map the `λ`-eigenspace to the
`(−λ)`-eigenspace. There is a `3` and no `−3`. Confirmed independently by
exhaustive search (0 of 16 factorized candidates). The same argument kills
`JDJ⁻¹ = −D`, so the `D`-sign is **forced** to `+1` before any search runs.
**The triple is necessarily odd**, so there is no third sign to report.

**The first-order axiom is vacuous here.** `D = 3(T⊗I₂)` and
`A = span{T,1−T}⊗I₂`, so `D` lies *inside* `A`: `[D,a] = 0` identically, the
one-form module `Ω¹ = span{a[D,b]}` is **zero**, and the first-order condition
is satisfied because there is nothing to satisfy it on. Recorded explicitly
because "first-order condition: PASS" would otherwise read as a result.

## Why `J` never globalizes — the same obstruction C30 found, one level up

Not a search failure. `J` is **antilinear**, so `T ↦ J T J⁻¹` is:

```
conj      : n -> n_bar = (n1, -n2, n3)    a REFLECTION,  det = -1
conj by M : a rotation                     det = +1
composite : det = -1
```

A global `J` would require the composite to be the **identity** on the Bloch
sphere, which has `det = +1`. Impossible. C30's exchange operator was blocked by
`det(−I₃) = −1`; the real structure is blocked by the determinant of the *same*
reflection. **One obstruction, two casualties.**

Pointwise the rotation carrying `n̄` to `n` has its axis `n̄ × n = (−2n₂n₃, 0,
2n₁n₂)` in the `xz`-plane, so the `SU(2)` element is `cos(a/2)I − i sin(a/2)·(real
symmetric)`, whose conjugate is its own inverse — hence `J² = +1` automatically,
for the entire `U(1)` family. That is why the sign tuple is forced rather than
chosen.

## Side-finding: `J_F² = −1` is wrong in eight documents, including the manuscript

Grounding step 0 (what sign tuple does this project already have on record?)
turned up a code/prose contradiction. Loading G18's **actual** `J_F` and
squaring it:

```
J_F: 32x32, entries all real = True
antilinear square  J_F conj(J_F) = +I32
```

`J_F` is 16 real transpositions. For antilinear `J = J_F∘conj`,
`J² = J_F conj(J_F) = J_F²`, and `g18_ncg.py` **asserts** `J_F**2 == eye(32)`.
Its own docstring line 17 says `J_F² = I`. So **`J_F² = +1`**.

But `J_F² = −1` appears in: `docs/gates_tracker.md:38`,
`experiments/20260619-g18-ncg-dirac-df/decision.md:9`,
`g26-ccm-comparison/claim.md` (×2), `ob10-.../claim.md` (×2),
`ob10-.../decision.md`, `OPEN_BLOCKERS.md` (×2), and **`preprint.tex:349,354`**.

**Downstream consequence:** OB10's `claim.md` justified its pseudo-real verdict
as "matching, not contradicting — the finite algebra's own pseudo-real
`J_F²=−1`". That corroboration was wrong twice over: C32 already showed OB10's
own verdict was a convention artifact, and the thing it was being matched
against is `+1`, not `−1`. Two independent reasons the same claim was
unsupported.

**Not fixed in this round** — it touches the manuscript and deserves its own
pass rather than being swept in as a side-edit. Logged as C36 and flagged in
`OPEN_BLOCKERS.md`.

## Two bugs in this round's own script, both caught, both recorded

Same family as OB10's, and the second one is new:

1. **Too-narrow ansatz.** First version searched the 16 factorized Pauli
   products and found 0 solutions *even per-point*. OB10 already hit this
   (naive 16-candidate guess → nothing → widen to 256 → unique solution).
2. **Sampling a measure-zero set.** Second version solved the intertwiner
   equation properly (a real 16-dim space) and then **randomly sampled** it for
   `M` with `M conj(M) = ±I`. Also 0 — because `{M : M conj(M) ∝ I}` is a
   measure-**zero** subvariety. Random draws essentially never land on it.

Both returned a confident "0 solutions"; both were wrong. The fix was to
**construct** the solution from the geometry (the rotation carrying `n̄` to `n`)
rather than search for it. **A search that cannot succeed is not evidence of
absence** — and it looks exactly like evidence of absence in the output.

## What this does NOT establish

1. **Does not resolve OB2.** The physical action (`F6`) remains open, as it was.
   This closes one checklist field with a negative, and sharpens two others.
2. **Does not say the S³×S⁶ geometry admits no real structure.** Everything here
   is about OB2's **finite toy** (`ℂ⁴`, constant-spinor truncation, `D` inside
   `A`). C32/C33's geometric results are a different object and are untouched.
3. **Does not resolve the `J_F²` discrepancy** — only establishes which side the
   code is on, and that the manuscript is on the other one.
4. **Does not check orientability or Poincaré duality**, the two remaining items
   on `PARENT_ACTION_GATE`'s OB2 axiom list. With `Ω¹ = 0` the orientability
   cycle is degenerate too, but that was not computed here.
5. **Does not test whether a different `D`** (one not lying inside `A`) would fix
   any of this. That is the obvious next construction, and it is not this round.

## Next gate

1. Fix the `J_F² = −1` propagation, manuscript included (C36).
2. If OB2 is pursued: replace `D = T⊗H` with a `D` that does **not** commute with
   `A`, so `Ω¹ ≠ 0` and the first-order condition acquires content. Without that,
   every axiom check on this toy is either vacuous or forced.

## Check

```
python experiments/20260810-ob2-theta-ncg-axioms/theta_ncg_axioms.py
```
Expect: `J_F conj(J_F) = +I32`; `spec(D)={0,0,3,3}` non-symmetric with 0 gradings
found; `[D,a]=0` for all `a`; `J` at 12/12 points with tuple `(+1,+1)`; global 0;
`Θ` valid at 0/12; both negative controls pass.
