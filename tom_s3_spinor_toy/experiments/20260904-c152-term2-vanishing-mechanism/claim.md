# C152 — the mechanism that annihilates `Term2` on `SU(3)/T²`

**Question type (EstimandOps L0): DESCRIPTIVE.** Structural characterisation of
an existing object; no counterfactual, no DAG required.

## Claim (falsifiable)

On `SU(3)/T²` with twist `W = m`, in the `T²`-invariant sector
`(Σ_odd⊗W)^{T²} → (Σ_even⊗W)^{T²}`:

1. `Term1` vanishes **per direction**, forced by weights alone — the domain's
   `Σ_odd` weights and the `Σ_even` weights are disjoint, and `Term1` cannot
   change the `Σ`-weight. The same statement holds on `S⁶`.
2. `Term2` does **not** vanish per direction. Exactly **2 of 6** directions
   are live for each matrix entry; they carry **equal magnitude and opposite
   sign**, and cancel.
3. On `S⁶` the identical construction gives exactly **2 of 6** live
   directions of equal magnitude and the **same** sign, adding to `−1/√3`.
4. The cancellation is forced by **`T²`-equivariance of the connection**, not
   by nearly-Kähler geometry: it holds for every element of the 6-dimensional
   equivariant family and for all 8 invariant almost-complex structures, and
   fails for non-equivariant connections of the same tensorial shape.

## Kill criterion

Any one of these falsifies the claim:

- a `Term2` matrix entry on `SU(3)/T²` with more or fewer than 2 live
  directions, or with live directions of unequal magnitude;
- a `T²`-equivariant connection on `SU(3)/T²` giving a nonzero `Term2` block;
- a non-equivariant connection giving zero;
- failure to reproduce C145 published `1.154701` on the `S⁶` `su(3)` sector,
  or C151 zero on `SU(3)/T²` — both are wired as hard asserts in the scripts.

## What this does NOT establish

1. Does **not** explain WHY the relative sign inside the live pair is `−` on
   `SU(3)/T²` and `+` on `S⁶`. The "root-type vs fundamental-type `m`"
   reading is an n=2 correlation, **not** a demonstrated mechanism.
2. ~~Does **not** reopen or answer the C151 pre-registered question. Whether
   the holomorphy of `c` is a nearly-Kähler universality remains OPEN.~~
   **⚠️ SUPERSEDED 2026-09-04, same day, by this round's own `decision.md`.**
   Written before the FL Step 8a skeptic overturned the sector construction.
   The round DID reopen and DID answer that question: on the corrected
   sector `c(J∇) = +i·c(∇)` exactly, entrywise, 8/8 draws — CONFIRMED. See
   `decision.md`, section "The real yield". Left struck through rather than
   deleted, per this project's discipline on self- and skeptic-caught errors.
3. Does **not** bear on `N_gen = 3`. The `3` is the dimension of a
   `T²`-invariant sector, i.e. a weight count.
4. Does **not** generalise to nearly-Kähler spaces at large — two cosets.
