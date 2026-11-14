# C158 — PRE-REGISTRATION (written before any Weyl-action computation)

**Date:** 2026-09-05. **Tier:** FL Full. **L0 (EstimandOps): DESCRIPTIVE.**
**Mandate (standing, unchanged):** autonomy covers search/computation/
literature/hypothesis-switching/negative results. NOT the right to declare
"discovery" — needs theorem + out-of-sample test + null model + novelty audit
+ independent skeptic pass, ALL FIVE, before anything is called a discovery.

## What is already on record (not re-derived, cited)

C155 established, exactly:
- `Q_mu(v) = 4(a0-a2+a4)^2 + 4(a1-a3+a5)^2`, rank 2, on the 6-dim family
  (`a0..a5`, raw `family_sym` coordinates on `SU(3)/T^2`).
- `ker(M) = {a0=a2-a4, a1=a3-a5}`, dimension 4, verified as an exact identity
  (`D_Sigma(v) psi_+ = 0`), not just a Gram-matrix rank number.
- Per-plane magnitudes of BOTH `Q_c` and `Q_mu` are EQUAL across the 3 root
  planes (32 and 8 respectively, on every one of the 6 raw basis directions) —
  a NECESSARY condition for a Weyl symmetry, already checked (C155 Step 2, B2).
- A naive "root relation" test on the OBSERVED coefficient pattern `(1,-1,1)`
  was run against the wrong object (oriented weights) and falsified (C155 Step
  5); C156 Step 1 showed it matches the correct object (positive-root
  relation) exactly.

**None of this is a check that `ker(M)` is invariant under the actual GEOMETRIC
action of `W(A_2) = S_3`** (as linear operators on the 6-dim family, built from
genuine `SU(3)` conjugation) — equal magnitudes is necessary but not
sufficient; a coefficient-pattern match is not the same as subspace
invariance. **That is the one gate this round runs.**

## The construction (built here, not assumed)

`W(A_2) = S_3` acts on `SU(3)`'s Cartan subalgebra by permuting the 3 weights
of the fundamental representation. A representative of the elementary
transposition `(p q)` in `SU(3)` is the matrix equal to `I_3` outside the
`{p,q}` block and equal to `[[0,1],[-1,0]]` inside it — unitary, `det=1`,
conjugation sends `diag(...,a_p,...,a_q,...) -> diag(...,a_q,...,a_p,...)`
(verified below by direct 2x2 computation before any 6-dim object is touched).

Two such representatives, `g_01` (swaps weight-indices 0,1) and `g_12` (swaps
1,2), generate all of `S_3`. Conjugating `M_BASIS`'s six 3x3 generators by
`g_01`/`g_12` and re-expressing the results in `M_BASIS` coordinates (via
`C153`'s own `to_m`, exact, no floats) gives two `6x6` orthogonal matrices
`R_01`, `R_12` — the actual geometric action of `W(A_2)` on `m`.

The induced action on a connection `Lambda in V_conn` (represented as
`Lambda_k`, `k=0..5`) is the standard one for a symmetry of the homogeneous
space: `(sigma.Lambda)_k = sum_j R[k,j] * (R Lambda_j R^{-1})`.

## Gates, in order (each is a kill point, not decoration)

| # | gate | kill condition |
|---|---|---|
| **G1** | `R_01^2 = I`, `R_12^3 = I` (regression on the group relations of `S_3`'s generators, BEFORE anything else) | either fails |
| **G2** | `R_01`, `R_12` map `T2_M` (the pinned Cartan generators) into `span{T2_M[0], T2_M[1]}` — i.e. they act as genuine automorphisms of the torus, not something else | either does not |
| **G3** | `R_01`, `R_12` map `family_sym` (the 6-dim equivariant family, AS A SPAN) into itself | either does not — if this fails, the whole construction is broken and nothing below is meaningful |
| **G4** (**the actual test**) | `R_01`, `R_12`, restricted to `family_sym`'s own 6-dim coordinates, map `ker(M) = {a0=a2-a4, a1=a3-a5}` into itself | either does not |

**G1-G3 are expected to pass** (they are checks that the construction is
correct, not the hypothesis). **G4 is the pre-registered, falsifiable, cheap
gate** the whole round hinges on — fixed now, before it is computed.

## Branch plan (fixed now, before G4's answer is known)

- **G4 FAILS** → `ker(M)` is not Weyl-invariant; the rank-2/kernel-4 structure
  is NOT a Weyl-isotypic phenomenon. Move directly to the `E_W`/`c|_{ker mu}`
  branch (representation content of the 4-dim "hidden" sector), per the
  consortium's Option B. Register REJECT with Kill Analysis; do not re-try
  with a different generator choice or relabelling to force a pass.
- **G4 PASSES** → decompose `V_conn` and `ker(M)` into `S_3`-isotypic pieces
  (character computation: trace of `R_01`, `R_12`, and products, against the
  3 irreps of `S_3` — trivial, sign, 2-dim standard). Report the decomposition
  as data. **Do NOT pre-register** that the quotient is the standard 2-dim
  representation — that would be exactly the kind of post-hoc fit this
  project's own discipline forbids (stated explicitly, per the consortium's
  own caution).

## What this will NOT establish, whatever G4 says

1. Nothing about `N_gen=3`, `lambda`, triality, or any physical claim.
2. Not a theorem for general `G/H` — one homogeneous space, fixed conventions.
3. Not novelty-audited yet — if G4 passes and a genuine isotypic decomposition
   emerges, novelty is Step 4, not assumed.
4. G1-G3 passing is not itself news — they are correctness checks on this
   round's own machinery, not findings.
