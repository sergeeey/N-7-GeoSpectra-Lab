# C158 STEP 3 — PRE-REGISTRATION (spin lift of the Weyl action, written before any exponential is computed)

**Date:** 2026-09-05. **Tier:** FL Full. **L0: DESCRIPTIVE.**
**Mandate (standing):** autonomy over computation, NOT over declaring
"discovery".

## Why the naive Pin lift is avoided

Decomposing R01 (an O(6) element) into a product of unit-vector reflections
and multiplying the corresponding Clifford vectors is the textbook Pin(n)
construction, but it carries a SIGN AMBIGUITY (the Pin(n)->O(n) cover is
2-to-1; a given O(n) element has TWO lifts, v1...vk and -v1...vk, and which
one you land on depends on the arbitrary choice of factorization).

**The principled fix, used here:** `SU(3)` is simply connected. The adjoint
map `SU(3) -> SO(m)` (already built as `g |-> R_of(g)` in Step 1) therefore has
a **UNIQUE** continuous lift `SU(3) -> Spin(m)`, obtained by exponentiating the
corresponding **Lie algebra** map `su(3) -> so(m) -> spin(m)` along the SAME
path `g(theta) = exp(theta A_pq)` already used to define `g01 = g(pi/2)`,
`g12` similarly. No factorization choice, no sign ambiguity — uniqueness is a
Lie-theory fact, not a computational trick.

## Construction (fixed, to be built in this order)

1. `A_01`, `A_12`: real antisymmetric `su(3)` generators with
   `exp((pi/2) A_pq) = g_pq` (already used in Step 1 to define `g01`, `g12`).
2. `ad_on_m(A)`: generalize C153's `cartan_on_m` (which only handled diagonal
   `A`) to ANY anti-Hermitian traceless `3x3` `A` — commute with `M_BASIS`,
   project via `to_m`. **Regression:** `ad_on_m(cartan-type A)` must reproduce
   `T2_M` exactly for the two Cartan directions already used.
3. `L_pq := ad_on_m(A_pq)`, a real antisymmetric `6x6` matrix.
   **Regression:** the derivative `d/dtheta R(theta)|_{theta=0}`, where
   `R(theta) := R_of(g(theta))` (Step 1's own construction, symbolic in
   `theta`), must equal `L_pq` EXACTLY. This ties the new infinitesimal
   generator back to the already-verified finite rotation `R01`, `R12`.
4. `S_pq(theta) := exp(theta * spin_lift(L_pq))`, an `8x8` matrix (Sigma is
   8-dimensional here). Evaluate at `theta = pi/2`.
5. **Decisive regression (must hold, or nothing below means anything):**
   conjugation by `S_pq(pi/2)` on the Clifford VECTORS `E_1..E_6` (embedded
   `m` inside `Cl^1(m)`) reproduces `R01`/`R12` exactly:
   `S v S^{-1} = sum_j R[i,j] E_j` for `v = E_i`.

## The actual questions (fixed now, before computing)

- **Q1 (order):** does `S_01(pi/2)^2 = +1` or `= -1` (or something else) on
  `Sigma`? This is NOT assumed either way — Spin(n) double-cover theory makes
  BOTH answers plausible a priori (a lift of an order-2 rotation is generically
  order 4 in the double cover, landing on `-1` at the square; whether it does
  here depends on the SPECIFIC rotation, not decided by hand).
- **Q2 (psi_+ transformation):** does `S_01(pi/2) . psi_+` equal `psi_+`,
  `-psi_+`, or something that is NOT a scalar multiple of `psi_+`? Only the
  first two cases make an ORDINARY (non-projective) equivariance statement
  for `M` possible.
- **Q3 (equivariance of D_Sigma):** does
  `S * D_Sigma(v) * S^{-1} = D_Sigma(R.v)` hold for `v` ranging over the
  family basis? (Expected to hold generically, as a structural Clifford-
  algebra fact once Q's regression in step 5 holds — but stated as a
  question, checked, not assumed.)
- **Q4 (equivariance of M itself):** does
  `S . M(v) = M(R.v)` (ordinary sense) or
  `S . M(v) = chi(g) * M(R.v)` for a SIGN CHARACTER `chi` (projective sense,
  if Q1/Q2 land on `-1`)? Compute directly, both sides, compare.

## What a `-1` at Q1/Q2 would mean (stated in advance, not spun after the fact)

If `S_01^2 = -1` on `Sigma` (or on the relevant subspace), `M`'s equivariance
is not broken — it means `W(A_2)` does not act ordinarily on `Sigma`, only
PROJECTIVELY (through its `Spin`-level double cover), which is a genuine,
well-known phenomenon (this project's own past Pin-structure discussions are
exactly this class of fact), not a defect in this round's construction. The
correct statement of "equivariance" would then carry an explicit sign
character, and that character itself would be data, not embarrassment.

## What this will NOT establish, whatever Q1-Q4 say

1. Nothing about `N_gen=3`, `lambda`, triality, or any physical claim.
2. Not novelty-audited, not skeptic-reviewed — this is construction + a direct
   computational answer, not a publication-ready result.
3. Not a general theorem — one homogeneous space, fixed conventions.
